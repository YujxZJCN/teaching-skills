# Contributing

Thanks for your interest. This suite improves the way it tells professors to improve
courses: with evidence from real use. The most valuable contributions are reports of
what a skill actually did in a real teaching session.

## Reporting skill misbehavior (most wanted)

Every skill's `SKILL.md` states iron rules; the `shared/` protocols state suite-wide
guarantees (no invented institutional policy, evidence-bound person-affecting outputs,
never-fake-a-render, gates that cite passport ids, …). If a skill violated one:

1. Open a **Skill misbehavior** issue (template provided).
2. Include: the skill + mode, what you asked, what it did, and **which stated rule it
   broke** (file + rule number if you can). That mapping is what makes the fix
   targeted — the rules are written precisely so that failures are diagnosable.
3. Strip any student-identifying data and institutional confidential content before
   posting. Reproductions with toy data are ideal.

## Proposing changes

- **A mode or agent change touches three places together**: the skill's `SKILL.md`,
  `MODE_REGISTRY.md`, and `docs/ARCHITECTURE.md`. PRs that update one without the
  others will be asked to complete the set (see `CLAUDE.md`).
- **New shared contracts** go in `shared/`; skills reference them by path. Don't
  duplicate protocol text into skill files.
- **New skills** follow the existing layout (`SKILL.md` + `agents/` + `references/` +
  `templates/`), declare `pipeline_stage` in frontmatter, get a `skills/` symlink, and
  add their modes to the registry. Open an issue first to discuss scope — the suite
  prefers deep, honest skills over many shallow ones.
- **Pedagogy claims need citations.** Anything added to
  `shared/pedagogy_foundations.md` or cited in agent rationale carries a real source.
  Defaults must be overrulable by the professor; nothing in this suite lectures.

## Translations

`README.zh-CN.md` is maintained alongside `README.md` (mirror the heading structure
1:1). Further README translations are welcome — follow the same convention and add a
language-switcher line to all README variants. Trigger-keyword additions for new
languages go in each skill's frontmatter `description` and are very welcome — that's
a high-impact, low-risk PR.

## Style

Match what's here: plain prose over bullets-of-fragments, tables only for enumerable
facts, honesty markers (`[NEEDS PROFESSOR INPUT]`, `[VERIFY]`, `NOT_EVALUABLE`) used
exactly as the shared protocols define them, no emoji beyond the established 🧑 / ✓
checkpoint notation.

## Conduct

Be the colleague you'd want at a department meeting. Disagreements about pedagogy are
welcome when they come with evidence; this repo's own rule applies to its
contributors — state the concern once, plainly, with the citation.
