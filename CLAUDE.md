# Teaching Skills — routing discipline

This repository is a Claude Code skill suite for university professors. When working in
a session where these skills are installed:

## Routing

- Single-artifact requests go to the specific skill, not the pipeline:
  course-level design → `course-designer` · class-meeting materials → `lesson-builder`
  · graded instruments and rubrics → `assessment-architect` · anything about an
  individual student → `student-mentor` · checking submissions against a standard →
  `submission-auditor` · evidence analysis and career artifacts →
  `teaching-reflector`.
- Lifecycle or multi-stage requests ("prepare my whole course", "new semester") →
  `teaching-pipeline`.
- Ambiguous between guided and direct production → prefer the guided/Socratic mode;
  producing an unwanted full artifact wastes more than a clarifying dialogue.
- If a `course_passport.yaml` exists in the working directory, load it before asking
  the professor for context they already provided.

## Non-negotiables (all skills)

1. Checkpoints per `shared/checkpoint_protocol.md` — the professor decides; surfaced
   defaults; "just proceed" respected.
2. No invented institutional policy, calendar dates, or learner context — ask or mark
   `[NEEDS PROFESSOR INPUT]`.
3. Uncertain domain claims in generated teaching materials carry `[VERIFY]` markers.
4. Person-affecting outputs (feedback, letters, interventions) are evidence-bound,
   draft-only, and end with a verify-before-send reminder. Student data never enters
   the Course Passport.
5. Never recommend AI-detection tools as an integrity mechanism
   (`shared/ai_era_integrity.md`).

## Editing this repo

- A mode or agent change touches three places together: the skill's `SKILL.md`,
  `MODE_REGISTRY.md`, and `docs/ARCHITECTURE.md`.
- New shared contracts go in `shared/`; skills reference them by path rather than
  duplicating content.
- Slash commands in `commands/` map 1:1 to registry entries.
