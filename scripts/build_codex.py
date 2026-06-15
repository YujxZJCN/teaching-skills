#!/usr/bin/env python3
"""Codex sibling-distribution generator.

Reads the canonical Teaching Skills suite and emits a complete OpenAI Codex CLI
package — a single Codex skill that vendors every skill's content and routes to
it by intent, emulating the Claude Code `/ts-*` slash commands as aliases.

Why a generator (not a hand-maintained second copy): the Codex package is a
*build product*. The canonical SKILL.md files stay the single source of truth;
this script reproduces them in Codex layout with no drift. Same philosophy as
build_dashboard.py — the artifact is regenerated, never hand-edited.

The package mirrors the proven structure of academic-research-skills-codex:
one router `SKILL.md` (Codex registers exactly one skill), with each upstream
`SKILL.md` vendored under `ts/<skill>/WORKFLOW.md` (renamed so Codex does not
register 15 separate skills).

Usage:
  python3 scripts/build_codex.py [-o dist/teaching-skills-codex] [--date YYYY-MM-DD]

Output is a complete repository tree ready to push to a `teaching-skills-codex`
GitHub repo. Exit codes: 0 = written · 2 = error
"""

import argparse
import datetime
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Independent Codex-package version (tracks the adapter, not the suite).
CODEX_VERSION = "0.1.0"
SUITE_NAME = "teaching-suite"

# Directories that are NOT skills (no SKILL.md, or infrastructure).
NON_SKILL_DIRS = {"shared", "scripts", "commands", "docs", "tests", "skills",
                  "examples", "dist", ".git", ".github", ".claude-plugin"}

# Scripts that travel to Codex (tool-agnostic). The generator itself does not.
VENDORED_SCRIPTS = ["check_passport.py", "check_alignment_gate.py",
                    "check_registry_consistency.py", "build_dashboard.py"]


def sh(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True).stdout.strip()


def discover_skills():
    """Skill dirs = top-level dirs containing a SKILL.md, sorted by pipeline stage then name."""
    skills = []
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name not in NON_SKILL_DIRS and (d / "SKILL.md").exists():
            skills.append(d)
    return skills


def frontmatter(skill_md):
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = m.group(1) if m else ""
    out = {}
    dm = re.search(r'^description:\s*"?(.*?)"?\s*$', fm, re.M)
    if dm:
        out["description"] = dm.group(1)
    sm = re.search(r"pipeline_stage:\s*(\S+)", fm)
    out["stage"] = sm.group(1) if sm else "support"
    return out


def intent_hint(description):
    """Leading sentence of the description = the human-readable 'when to use' hint."""
    first = re.split(r"(?<=[.!?])\s", description.strip())[0]
    return first.rstrip(".")


def trigger_terms(description):
    """Pull the 'Triggers on: ...' tail of a description into a keyword list."""
    m = re.search(r"Triggers on:\s*(.+)$", description)
    if not m:
        return []
    return [t.strip().rstrip(".") for t in m.group(1).split(",") if t.strip()]


def parse_commands():
    """{alias: {skill, mode, desc}} from commands/ts-*.md."""
    cmds = {}
    for f in sorted((ROOT / "commands").glob("ts-*.md")):
        body = f.read_text(encoding="utf-8")
        dm = re.search(r"^description:\s*(.+)$", body, re.M)
        sm = re.search(r"Trigger the `([a-z-]+)` skill in `([a-z-]+)` mode", body)
        if sm:
            cmds[f.stem] = {"skill": sm.group(1), "mode": sm.group(2),
                            "desc": dm.group(1).strip() if dm else ""}
    return cmds


# --- emit: router SKILL.md -----------------------------------------------------

def emit_router(skills, cmds):
    metas = {s.name: frontmatter(s / "SKILL.md") for s in skills}

    # Aggregate trigger keywords across all skills for Codex skill matching.
    all_terms, seen = [], set()
    for s in skills:
        for t in trigger_terms(metas[s.name].get("description", "")):
            key = t.lower()
            if key not in seen and len(t) < 40:
                seen.add(key)
                all_terms.append(t)
    aliases = sorted(cmds)
    alias_phrase = ", ".join(f"/{a}, {a}" for a in aliases)

    routing_rows = "\n".join(
        f"| {intent_hint(metas[s.name].get('description', s.name))} "
        f"| `ts/{s.name}/WORKFLOW.md` |"
        for s in skills)

    alias_rows = "\n".join(
        f"| `/{a}`, `{a}` | `ts/commands/{a}.md` | `ts/{cmds[a]['skill']}/WORKFLOW.md` "
        f"in `{cmds[a]['mode']}` mode |"
        for a in aliases)

    desc = (
        "Codex-native Teaching Skills suite for university professors — the full "
        "teaching lifecycle: course design, lesson building, assessment, student "
        "mentoring, submission auditing, reflection, plus slide-deck rendering, "
        "executable labs, video scripting, course publishing, TA coordination, "
        "accreditation mapping, bilingual courseware, and learner analysis "
        "(学情分析). Use when the user asks to design a course, write "
        "outcomes or a syllabus, build a lesson or slides, write an exam/quiz/rubric, "
        "check student submissions against a standard, give feedback or a "
        "recommendation letter, analyze student evaluations, run a teaching pipeline, "
        "or any Claude-style ts-* alias such as " + alias_phrase + ". "
        "Triggers on: " + ", ".join(all_terms[:60]) + ".")

    return f"""---
name: {SUITE_NAME}
description: >
  {desc}
metadata:
  version: "{CODEX_VERSION}"
  upstream_suite: "teaching-skills"
  codex_adapter: true
allowed-tools: Read, Glob, Grep, WebSearch, Bash(python3 *), Bash(python *)
---

# Teaching Suite for Codex

Codex adapter for the **Teaching Skills** suite (course design → build →
assess → deliver → reflect → improve). The vendored upstream content lives
under `ts/`; route through this file first.

This is the sibling Codex distribution of the Claude Code suite
[`YujxZJCN/teaching-skills`](https://github.com/YujxZJCN/teaching-skills). Same
workflow content, Codex-native packaging.

## First Rule — load lazily

Do **not** load the whole suite by default. Select one workflow, read that
workflow's `ts/<skill>/WORKFLOW.md`, then load only the agent, reference, or
template files needed for the user's current stage. The vendored workflow entry
files are named `WORKFLOW.md` (not `SKILL.md`) so Codex registers only this one
router skill instead of every vendored workflow.

## Non-negotiables (apply in every workflow)

These are the suite's standing rules. Read `ts/shared/checkpoint_protocol.md`
and `ts/shared/pedagogy_foundations.md` when a task touches them; never violate
them even when reading lazily:

1. **The professor is the pilot.** Surface every consequential default at a
   checkpoint; respect "just proceed"; never auto-finalize person-affecting output.
2. **No invented context.** Empty learner/institution facts are asked for or
   marked `[NEEDS PROFESSOR INPUT: …]`; uncertain domain claims get `[VERIFY: …]`.
3. **Person-affecting outputs are evidence-bound** (feedback, letters,
   interventions): only material the professor provided, no invented anecdotes,
   verify-before-send reminder, and **student data never enters the Course
   Passport** (`ts/shared/course_passport_schema.md`).
4. **Integrity by design, not detection** (`ts/shared/ai_era_integrity.md`): no
   AI-detection tools, ever.
5. **Evidence honesty.** Student evaluations are biased small-N signal, not a score.

## Course Passport & validators

State lives in `course_passport.yaml` (`ts/shared/course_passport_schema.md`),
not the conversation. The deterministic layer travels to Codex — run it when
Python 3 is available:

```bash
python3 ts/scripts/check_passport.py course_passport.yaml          # structure + id mirrors
python3 ts/scripts/check_alignment_gate.py course_passport.yaml    # Gate 1.5, A1–D3
python3 ts/scripts/build_dashboard.py course_passport.yaml         # single-file HTML overview
```

## Workflow Router

Choose the workflow by intent, then read its `WORKFLOW.md`:

| User intent | Read first |
|---|---|
{routing_rows}

For a whole-course or multi-stage request ("teach / prepare my course", "new
semester"), start with `ts/teaching-pipeline/WORKFLOW.md`; it orchestrates the
others through the alignment and quality gates.

## Claude-Style Alias Router

Codex does not install Claude slash commands, but this package emulates their
intent. If the request starts with a slash alias (`/ts-exam`) or a plain alias
(`ts-exam`), strip the alias token, read the matching `ts/commands/<alias>.md`
recipe, then route to the workflow below. The `model:` field in any recipe
frontmatter is a Claude hint only — Codex uses the current model.

| Alias | Read recipe | Then route to |
|---|---|---|
{alias_rows}

## What is vendored

`ts/` contains every skill's `WORKFLOW.md` + `agents/` + `references/` +
`templates/`, the `shared/` contracts (passport schema, gate protocols, pedagogy
foundations, AI-era integrity, checkpoint protocol), the tool-agnostic
`scripts/` (validators + dashboard), the `commands/` alias recipes, and
`MODE_REGISTRY.md`. The Claude Code plugin loader files are intentionally not
vendored. See `manifest.json` for the source commit pin.
"""


def emit_manifest(skills, commit, date):
    return json.dumps({
        "name": SUITE_NAME,
        "adapter_version": CODEX_VERSION,
        "version_file": "VERSION",
        "generated_for": "codex",
        "generated_date": date,
        "source_repositories": [{
            "name": "teaching-skills",
            "url": "https://github.com/YujxZJCN/teaching-skills.git",
            "commit": commit,
            "included_paths": [s.name for s in skills] + [
                "shared", "scripts (validators + dashboard)", "commands",
                "MODE_REGISTRY.md", "docs/ARCHITECTURE.md"],
        }],
        "excluded_patterns": [
            ".git", ".github", ".claude-plugin", "skills/ symlinks",
            "scripts/build_codex.py", "tests/", "examples/showcase/*.html",
        ],
        "rename_rule": "every vendored <skill>/SKILL.md -> ts/<skill>/WORKFLOW.md "
                       "so Codex registers only the root router skill",
    }, indent=2) + "\n"


def emit_plugin_json(date):
    return json.dumps({
        "name": "teaching-skills",
        "version": CODEX_VERSION,
        "description": "Codex-native Teaching Skills suite for university professors: "
                       "course design, lessons, assessment, mentoring, submission "
                       "auditing, reflection, and 8 extension skills.",
        "author": {"name": "Jiaxing Yu"},
        "homepage": "https://github.com/YujxZJCN/teaching-skills-codex",
        "repository": "https://github.com/YujxZJCN/teaching-skills-codex",
        "license": "MIT",
        "keywords": ["teaching", "higher-education", "course-design", "syllabus",
                     "assessment", "rubric", "pedagogy", "codex"],
        "skills": "./skills/",
        "interface": {
            "displayName": "Teaching Skills",
            "shortDescription": "Course design, lessons, assessment, mentoring, and reflection.",
            "longDescription": "Teaching Skills for Codex covers the full university "
                               "teaching lifecycle: backward course design with "
                               "constructive-alignment gates, lesson building, "
                               "blueprint-first assessment with AI-era integrity audits, "
                               "spec-driven submission auditing, student mentoring, "
                               "learner analysis, evaluation analysis, and a one-file "
                               "HTML course dashboard.",
            "developerName": "Jiaxing Yu",
            "category": "Education",
            "capabilities": ["Interactive", "Read", "Write"],
            "websiteURL": "https://github.com/YujxZJCN/teaching-skills-codex",
            "defaultPrompt": [
                "Design a new undergraduate course for 90 students.",
                "Build a blueprint-first midterm exam for my course.",
                "Check these student lab reports against my template.",
            ],
            "brandColor": "#2563EB",
        },
    }, indent=2) + "\n"


def emit_openai_yaml():
    return (
        'interface:\n'
        '  display_name: "Teaching Skills"\n'
        '  short_description: "Teaching lifecycle workflows plus Claude-style ts-* aliases"\n'
        '  brand_color: "#2563EB"\n'
        '  default_prompt: "Use $teaching-suite with ts-course to design a course backward '
        'from learning outcomes."\n'
        '\n'
        'policy:\n'
        '  allow_implicit_invocation: true\n')


def emit_readme(skills, commit, date):
    n = len(skills)
    install = (
        'python3 "$HOME/.codex/skills/.system/skill-installer/scripts/'
        'install-skill-from-github.py" \\\n'
        '  --repo YujxZJCN/teaching-skills-codex \\\n'
        '  --ref main \\\n'
        f'  --path skills/{SUITE_NAME} \\\n'
        '  --method git')
    return f"""# Teaching Skills for Codex

Codex-native packaging of the **Teaching Skills** suite — the full university
teaching lifecycle (design → build → assess → deliver → reflect → improve)
for OpenAI Codex CLI. This is the sibling Codex distribution of
[Teaching Skills for Claude Code](https://github.com/YujxZJCN/teaching-skills).

This repository vendors the suite as a **single Codex skill** that routes to
{n} workflows by intent:

```text
skills/{SUITE_NAME}/
  SKILL.md            # router: intent -> workflow, plus ts-* alias emulation
  manifest.json       # adapter metadata + upstream commit pin
  VERSION
  agents/openai.yaml
  ts/                 # vendored content (each upstream SKILL.md -> WORKFLOW.md)
    <{n} skills>/WORKFLOW.md + agents/ references/ templates/
    shared/ scripts/ commands/ MODE_REGISTRY.md
```

> Generated, not hand-edited. The canonical source is the Claude Code repo; this
> package is reproduced by `scripts/build_codex.py` there, with no drift. Do not
> edit files here directly — change the upstream suite and regenerate.

## Which repo do I want?

- **Claude Code** (CLI / VS Code / JetBrains): use
  [`YujxZJCN/teaching-skills`](https://github.com/YujxZJCN/teaching-skills) —
  native skills, `/plugin` install, `/ts-*` slash commands.
- **Codex CLI**: use this repo — the single-suite Codex skill with `ts-*` aliases.

## Install or update

Install the skill from this repo with the Codex skill installer:

```bash
{install}
```

To update, remove the installed copy and reinstall:

```bash
rm -rf "$HOME/.codex/skills/{SUITE_NAME}"
{install}
```

On macOS / most Linux, Python 3 is `python3`. If your only `python` is Python 3,
substitute it.

## Use

Ask in natural language ("design a course on machine learning for 90 students"),
or use a Claude-style alias as a mode shortcut: `ts-course`, `ts-exam`,
`ts-rubric`, `ts-feedback`, `ts-cohort`, `ts-dashboard`, and more. The router
(`skills/{SUITE_NAME}/SKILL.md`) dispatches to the right workflow and enforces
the suite's non-negotiables (professor checkpoints, no invented context,
evidence-bound person-affecting output, integrity-by-design, no student data in
the passport).

**How this works in Codex.** Codex does not register Claude Code slash commands.
The `ts-*` names are *emulated aliases*: the vendored `ts/commands/*.md` files are
prompt recipes the router reads to pick a workflow and mode — they are not
installed commands. Type `ts-exam ...` (with or without a leading slash) and the
router treats it as a mode shortcut. If anything looks wrong after an upstream
change, recover by reinstalling (the update step above) — the skill is a
regenerated build product, so a clean reinstall always restores a consistent state.

The deterministic validators travel too:

```bash
python3 skills/{SUITE_NAME}/ts/scripts/check_passport.py course_passport.yaml
python3 skills/{SUITE_NAME}/ts/scripts/build_dashboard.py course_passport.yaml
```

## Versioning

Codex package `{CODEX_VERSION}`. Vendored from
`YujxZJCN/teaching-skills@{commit[:12]}` on {date}. The package version tracks
the adapter independently of the upstream suite version; see `manifest.json`.

## License

MIT — same as the upstream suite. Architecture inspired by
[academic-research-skills](https://github.com/Imbad0202/academic-research-skills)
and its Codex sibling.
"""


# --- path rewriting (keep vendored references valid in the ts/ layout) --------

OWN_DIR_SEGMENTS = {"templates", "references", "agents", "examples"}
ROOT_SEGMENTS = {"shared", "scripts", "docs"}
BACKTICK = re.compile(r"`([^`\n ]+)`")


def rewrite_refs(text, owner_skill, skill_names):
    """Rewrite repo-root-relative path references in a vendored markdown file to the
    suite-root-relative `ts/...` form used by the router, so every reference in the
    package resolves from one fixed base (the skill root). Only backtick-quoted,
    slash-bearing path tokens whose first segment is a known suite directory are
    touched — bare skill-name mentions and prose are left alone.
    """
    def repl(m):
        t = m.group(1)
        if "://" in t or t.startswith("ts/"):
            return m.group(0)
        first = t.split("/")[0]
        has_slash = "/" in t
        new = None
        if has_slash and first in skill_names:
            rest = t[len(first) + 1:]
            if rest == "SKILL.md":
                rest = "WORKFLOW.md"
            new = f"ts/{first}/{rest}"
        elif has_slash and first in ROOT_SEGMENTS:
            new = f"ts/{t}"
        elif has_slash and first in OWN_DIR_SEGMENTS and owner_skill:
            new = f"ts/{owner_skill}/{t}"
        elif t == "MODE_REGISTRY.md":
            new = "ts/MODE_REGISTRY.md"
        return f"`{new}`" if new else m.group(0)

    return BACKTICK.sub(repl, text)


def copy_skill(skill_dir, dest, skill_names):
    """Copy a skill dir, renaming SKILL.md -> WORKFLOW.md and rewriting path refs."""
    owner = skill_dir.name
    for src in skill_dir.rglob("*"):
        if src.is_dir() or ".git" in src.parts:
            continue
        rel = src.relative_to(skill_dir)
        target = dest / rel
        if src.name == "SKILL.md":
            target = dest / rel.parent / "WORKFLOW.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix == ".md":
            target.write_text(
                rewrite_refs(src.read_text(encoding="utf-8"), owner, skill_names),
                encoding="utf-8")
        else:
            shutil.copy2(src, target)


def copy_tree_rewritten(src_dir, dest_dir, skill_names, owner=None):
    """Copy a directory, rewriting path refs in .md files (no SKILL.md rename here)."""
    for src in src_dir.rglob("*"):
        if src.is_dir() or ".git" in src.parts:
            continue
        target = dest_dir / src.relative_to(src_dir)
        target.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix == ".md":
            target.write_text(
                rewrite_refs(src.read_text(encoding="utf-8"), owner, skill_names),
                encoding="utf-8")
        else:
            shutil.copy2(src, target)


def build(out_dir, date=None):
    commit = sh("git", "rev-parse", "HEAD") or "unknown"
    date = date or datetime.date.today().isoformat()
    skills = discover_skills()
    cmds = parse_commands()

    out = Path(out_dir)
    if out.exists():
        shutil.rmtree(out)
    suite = out / "skills" / SUITE_NAME
    ts = suite / "ts"
    (suite / "agents").mkdir(parents=True, exist_ok=True)
    ts.mkdir(parents=True, exist_ok=True)

    # router + manifests + version
    (suite / "SKILL.md").write_text(emit_router(skills, cmds), encoding="utf-8")
    (suite / "manifest.json").write_text(emit_manifest(skills, commit, date), encoding="utf-8")
    (suite / "VERSION").write_text(CODEX_VERSION + "\n", encoding="utf-8")
    (suite / "agents" / "openai.yaml").write_text(emit_openai_yaml(), encoding="utf-8")

    skill_names = {s.name for s in skills}

    # vendored skills (SKILL.md -> WORKFLOW.md, path refs rewritten)
    for s in skills:
        copy_skill(s, ts / s.name, skill_names)

    # shared/, commands/, MODE_REGISTRY, ARCHITECTURE (path refs rewritten)
    copy_tree_rewritten(ROOT / "shared", ts / "shared", skill_names)
    copy_tree_rewritten(ROOT / "commands", ts / "commands", skill_names)
    (ts / "MODE_REGISTRY.md").write_text(
        rewrite_refs((ROOT / "MODE_REGISTRY.md").read_text(encoding="utf-8"), None, skill_names),
        encoding="utf-8")
    (ts / "docs").mkdir(exist_ok=True)
    (ts / "docs" / "ARCHITECTURE.md").write_text(
        rewrite_refs((ROOT / "docs" / "ARCHITECTURE.md").read_text(encoding="utf-8"), None, skill_names),
        encoding="utf-8")

    # tool-agnostic scripts only
    (ts / "scripts").mkdir(exist_ok=True)
    for name in VENDORED_SCRIPTS:
        shutil.copy2(ROOT / "scripts" / name, ts / "scripts" / name)

    # repo-level files
    (out / ".codex-plugin").mkdir(exist_ok=True)
    (out / ".codex-plugin" / "plugin.json").write_text(emit_plugin_json(date), encoding="utf-8")
    (out / "README.md").write_text(emit_readme(skills, commit, date), encoding="utf-8")
    (out / "VERSION").write_text(CODEX_VERSION + "\n", encoding="utf-8")
    if (ROOT / "LICENSE").exists():
        shutil.copy2(ROOT / "LICENSE", out / "LICENSE")

    return out, skills, cmds


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("-o", "--out", default=str(ROOT / "dist" / "teaching-skills-codex"))
    ap.add_argument("--date", default=None)
    args = ap.parse_args(argv)
    try:
        out, skills, cmds = build(args.out, args.date)
    except Exception as ex:
        print(f"error: {type(ex).__name__}: {ex}", file=sys.stderr)
        return 2
    print(f"codex package written: {out}")
    print(f"  {len(skills)} skills vendored, {len(cmds)} aliases routed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
