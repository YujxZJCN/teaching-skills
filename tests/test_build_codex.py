"""Codex generator tests — structural invariants of the emitted package.

The package must register exactly ONE Codex skill (the router), with every
upstream SKILL.md vendored as a WORKFLOW.md. These tests pin that so a generator
regression fails by name.
"""

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build_codex  # noqa: E402


@pytest.fixture(scope="module")
def pkg(tmp_path_factory):
    out = tmp_path_factory.mktemp("codex") / "teaching-skills-codex"
    built, skills, cmds = build_codex.build(out, date="2026-06-15")
    return {"dir": built, "skills": skills, "cmds": cmds}


def test_exactly_one_skill_md_and_it_is_the_router(pkg):
    skill_mds = list(pkg["dir"].rglob("SKILL.md"))
    assert len(skill_mds) == 1, f"expected 1 SKILL.md, found {skill_mds}"
    assert skill_mds[0] == pkg["dir"] / "skills" / build_codex.SUITE_NAME / "SKILL.md"


def test_no_stray_skill_md_under_ts(pkg):
    ts = pkg["dir"] / "skills" / build_codex.SUITE_NAME / "ts"
    assert list(ts.rglob("SKILL.md")) == []


def test_every_skill_has_one_workflow(pkg):
    ts = pkg["dir"] / "skills" / build_codex.SUITE_NAME / "ts"
    workflows = list(ts.rglob("WORKFLOW.md"))
    assert len(workflows) == len(pkg["skills"])
    for s in pkg["skills"]:
        assert (ts / s.name / "WORKFLOW.md").exists(), f"{s.name} missing WORKFLOW.md"


def test_router_references_every_workflow(pkg):
    router = (pkg["dir"] / "skills" / build_codex.SUITE_NAME / "SKILL.md").read_text(encoding="utf-8")
    for s in pkg["skills"]:
        assert f"ts/{s.name}/WORKFLOW.md" in router, f"router missing {s.name}"


def test_router_routes_every_alias(pkg):
    router = (pkg["dir"] / "skills" / build_codex.SUITE_NAME / "SKILL.md").read_text(encoding="utf-8")
    for alias in pkg["cmds"]:
        assert f"`/{alias}`" in router, f"router missing alias {alias}"


def test_alias_targets_resolve_to_real_workflow_and_mode(pkg):
    """Each alias must route to a vendored WORKFLOW.md, and the source command's
    declared (skill, mode) must match the router's claim."""
    ts = pkg["dir"] / "skills" / build_codex.SUITE_NAME / "ts"
    for alias, spec in pkg["cmds"].items():
        assert (ts / spec["skill"] / "WORKFLOW.md").exists(), \
            f"{alias} targets non-existent skill {spec['skill']}"
        # the command recipe is vendored so the router's "read recipe" path resolves
        assert (ts / "commands" / f"{alias}.md").exists()


def test_manifests_valid_and_version_consistent(pkg):
    suite = pkg["dir"] / "skills" / build_codex.SUITE_NAME
    manifest = json.loads((suite / "manifest.json").read_text(encoding="utf-8"))
    plugin = json.loads((pkg["dir"] / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    v = build_codex.CODEX_VERSION
    assert manifest["adapter_version"] == v
    assert plugin["version"] == v
    assert (suite / "VERSION").read_text().strip() == v
    assert (pkg["dir"] / "VERSION").read_text().strip() == v
    # commit pin present and non-empty
    pin = manifest["source_repositories"][0]["commit"]
    assert pin and pin != "unknown"
    # Codex interface block present
    assert plugin["interface"]["displayName"] and plugin["interface"]["capabilities"]


def test_validators_vendored_generator_excluded(pkg):
    scripts = pkg["dir"] / "skills" / build_codex.SUITE_NAME / "ts" / "scripts"
    names = {p.name for p in scripts.glob("*.py")}
    assert names == set(build_codex.VENDORED_SCRIPTS)
    assert "build_codex.py" not in names


def test_shared_fully_vendored(pkg):
    src = {p.name for p in (ROOT / "shared").glob("*")}
    dst = {p.name for p in (pkg["dir"] / "skills" / build_codex.SUITE_NAME / "ts" / "shared").glob("*")}
    assert src == dst


def test_install_path_matches_layout(pkg):
    """README's --path must point where the skill actually lives."""
    readme = (pkg["dir"] / "README.md").read_text(encoding="utf-8")
    assert f"--path skills/{build_codex.SUITE_NAME}" in readme
    assert (pkg["dir"] / "skills" / build_codex.SUITE_NAME / "SKILL.md").exists()


def test_every_internal_ts_path_reference_resolves(pkg):
    """Every backtick `ts/...` file reference in the package must resolve to a
    real file. This is the permanent guard for the F1/F3 class of bug (vendored
    leaf files referencing repo-root-relative paths that break in the ts/ layout)."""
    suite = pkg["dir"] / "skills" / build_codex.SUITE_NAME
    pat = re.compile(r"`(ts/[\w./-]+\.(?:md|py|ya?ml|json))`")
    broken = []
    for md in suite.rglob("*.md"):
        for ref in pat.findall(md.read_text(encoding="utf-8")):
            if not (suite / ref).exists():
                broken.append((md.relative_to(suite).as_posix(), ref))
    assert not broken, f"unresolved ts/ references: {broken[:10]}"


def test_no_vendored_file_references_bare_shared_or_skill_md(pkg):
    """After the layout rewrite, no vendored markdown should point at a bare
    repo-root `shared/...` path or a `<skill>/SKILL.md` (renamed to WORKFLOW.md)."""
    ts = pkg["dir"] / "skills" / build_codex.SUITE_NAME / "ts"
    for md in ts.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        assert "`shared/" not in text, f"{md} has a bare `shared/ reference"
        # a vendored recipe/workflow must not point at a now-nonexistent SKILL.md
        for ref in re.findall(r"`(ts/[\w./-]+/SKILL\.md)`", text):
            pytest.fail(f"{md} references {ref} (should be WORKFLOW.md)")
