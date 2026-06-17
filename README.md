# Teaching Skills for Claude Code

English | [简体中文](README.zh-CN.md)

A comprehensive suite of Claude Code skills for university professors, covering the full
teaching lifecycle: **design → build → assess → deliver → reflect → improve**.

15 skills · 84 modes · 71-agent ensemble · 2 quality gates · 1 Course Passport

> **AI is your teaching assistant, not your replacement.** This suite won't teach for
> you. It handles the structure and the grunt work — drafting outcomes, building
> blueprints before exams, auditing alignment, formatting syllabi, coding evaluation
> comments — so you can focus on what actually requires you: knowing your discipline,
> knowing your students, and deciding what matters. Every consequential decision passes
> through a checkpoint where you decide.

Architecturally inspired by [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)
(Cheng-I Wu) — the research-side sibling of this suite. If you also write papers, the
two compose: `teaching-reflector`'s SoTL mode hands off to ARS's deep-research and
academic-paper skills.

## Install

**Plugin (recommended):**

```text
/plugin marketplace add YujxZJCN/teaching-skills
/plugin install teaching-skills
```

**Manual:** clone this repo and symlink the skill directories into
`~/.claude/skills/` (or the project's `.claude/skills/`).

**Verify:** run `/ts-status` in a directory with a `course_passport.yaml`, or just say
*"Design a new course on X for 60 second-year students."*

## The skills

| Skill | Stage | What it does |
|-------|-------|--------------|
| **course-designer** | 1 DESIGN | Backward design: Bloom-tagged outcomes → assessment plan → semester arc → syllabus. Socratic mode for blank-page starts. |
| **lesson-builder** | 2 BUILD | Lesson plans, lecture notes, slide outlines, active-learning activities, cases, discussion guides, flipped formats. |
| **assessment-architect** | 3 ASSESS | Blueprint-first exams and quizzes, rubrics, TILT project briefs, AI-resilience integrity audits, post-exam item analysis. |
| **student-mentor** | 4 DELIVER | Feedback writing, struggling-student intervention plans, recommendation letters, difficult emails, advising and mentoring plans. |
| **submission-auditor** | 4 DELIVER | Spec-driven submission checking: compile your template/requirements into a checkable spec, audit submissions (single or batch) with located evidence, per-student feedback reports + class pattern report. |
| **teaching-reflector** | 5 REFLECT | Bias-honest evaluation analysis, mid-course feedback, peer observation, teaching portfolio and statement, SoTL design. |
| **teaching-pipeline** | orchestrator | Runs the whole lifecycle over the Course Passport, with two non-skippable gates and a weekly delivery loop. |

**Extension skills** — production, operations, and compliance layers; each works
standalone and the pipeline dispatches them on demand:

| Skill | Stage | What it does |
|-------|-------|--------------|
| **deck-studio** | 2 | Renders actual slide decks (Marp/Pandoc/Beamer/python-pptx), course-wide themes, code-generated figures, handouts, posters. Accessibility enforced, never fakes a render. |
| **lab-forge** | 2 | Executable STEM artifacts: lab packages, per-student synthetic datasets with recoverable ground truth, starter code, autograders, executed reference solutions. |
| **media-scripter** | 2 | Recorded-media scripting: 6–9 min mini-lecture scripts, storyboards, episode series, caption/transcript cleanup, audio adaptations. |
| **course-publisher** | 4 | Student-facing comms from the passport: announcements, weekly emails, static course site, LMS packaging, living FAQ. Drafts only — facts traced, never invented. |
| **ta-coordinator** | 4 | Teaching-team operations: TA handbooks, grading calibration sessions, hours-balanced allocation, meeting agendas, cross-TA consistency checks (no league tables). |
| **accreditation-mapper** | 1 | Outcomes → program outcomes → standards matrices with evidence status, evidence packages, gap analysis, honesty-capped self-study drafts. |
| **bilingual-courseware** | support | Terminology-disciplined bilingual materials: professor-confirmed glossary, glossary-bound translation, paired-version sync, consistency audits. |
| **cohort-analyst** | support | Learner analysis (学情分析): pre-lesson diagnostics, cohort readiness profiles from ability lists/questionnaires, lesson calibration, evidence-based grouping. Aggregates only — individual students route to student-mentor. |

## The pipeline

```
Stage 0 CONTEXT  → Course Passport initialized                 🧑
Stage 1 DESIGN   → course-designer                             🧑
Gate 1.5 ALIGNMENT — constructive-alignment audit              ✓ machine + ack
Stage 2 BUILD    → lesson-builder (just-in-time by default)    🧑
Stage 3 ASSESS   → assessment-architect + integrity audit      🧑
Gate 3.5 QUALITY — AI-integrity, transparency, UDL, workload   ✓ machine + ack
Stage 4 DELIVER  → weekly loop: materials · mentoring · submission audits · midcourse feedback
Stage 5 REFLECT  → teaching-reflector eval-analysis            🧑
Stage 6 IMPROVE  → iteration record → next term re-enters Stage 1
```

🧑 = professor checkpoint (you decide) · ✓ = deterministic gate, then your acknowledgment

Two ideas hold this together:

- **The Course Passport** (`shared/course_passport_schema.md`) — a YAML file that is the
  single source of truth for the course. Outcomes, assessment plan, schedule, policies,
  gate findings, artifact ledger, iteration history. State lives in the passport, not
  the conversation: any fresh session resumes from it. Every skill also works standalone
  without one.
- **Constructive alignment as a machine check** — the Alignment Gate verifies the
  outcome–teaching–assessment triangle is closed before anything is built on it; the
  Quality Gate verifies the built artifacts are transparent (TILT), accessible (UDL),
  integrity-coherent (AI-era), and humanly workloaded — before students see them.

## Showcase: what the output looks like

Two complete, synthetic-but-rule-obeying artifact sets — so you can judge output quality
before installing:

- **[STEM lecture course →](examples/showcase/)** — CS 304 Introduction to Machine
  Learning, 90 students: filled Course Passport, syllabus, alignment gate report with a
  dismissed-warning trail, lesson plan + activity sheet, exam blueprint with sample items
  and a worked key, the AI-integrity audit that redesigned the course project, and a
  rendered HTML course dashboard.
- **[Humanities seminar →](examples/showcase-seminar/)** — HIST 247 The Atlantic World,
  18 students: a discussion/writing course with specs-flavored grading, **plus inspectable
  person-affecting outputs** — a recommendation letter with its claim-to-intake trace
  appendix, the intake ledger behind it, and a feedback report — demonstrating the
  anti-fabrication templates (every claim traces to evidence; no student data in the
  passport).

## Quick start

```
# Full lifecycle
"I'm teaching a new course on environmental economics next fall — run the full pipeline"

# Blank page
"Guide me — I know my field but I've never designed a course"          → socratic

# Single artifacts
/ts-outcomes  /ts-syllabus  /ts-lesson  /ts-exam  /ts-rubric  /ts-letter  /ts-evals

# Mid-entry
"I already have a syllabus, build me week 3's materials"
"Semester's over, here are my student evaluations"                      → eval-analysis

# Status
/ts-status    "What's next for my course?"
```

See [QUICKSTART.md](QUICKSTART.md) for a worked first session and
[MODE_REGISTRY.md](MODE_REGISTRY.md) for all 84 modes.

## Design principles

1. **The professor is the pilot.** Checkpoints at every stage; "key decisions made for
   you" are always surfaced, never buried; "just proceed" is respected
   (`shared/checkpoint_protocol.md`).
2. **Evidence-based defaults, professor's final call.** Recommendations cite
   `shared/pedagogy_foundations.md` (backward design, constructive alignment, active
   learning, retrieval practice, TILT, UDL, cognitive load, feedback research). When you
   overrule a principle, the decision is logged and never re-litigated.
3. **No invented context.** Empty learner profile → the skill asks. Institutional
   policies → `[NEEDS PROFESSOR INPUT]` markers, never plausible filler. Uncertain
   domain claims in generated materials → `[VERIFY]` markers.
4. **Person-affecting outputs are evidence-bound.** Feedback, letters, and intervention
   plans use only material you provided — no invented anecdotes, ever — and always end
   with a verify-before-send reminder. Student data never enters the Course Passport.
5. **Integrity by design, not detection.** The AI-era integrity model
   (`shared/ai_era_integrity.md`) uses per-assignment policy tiers and structural
   resilience patterns. Nothing in this suite relies on AI-detection tools.
6. **The contracts are machine-checked.** The Course Passport has a JSON Schema
   (`shared/course_passport.schema.json`) and validators: `scripts/check_passport.py`
   (cross-reference invariants — id mirrors, weight sums) and
   `scripts/check_alignment_gate.py` (Gate 1.5 executed deterministically, not
   interpreted by a model). CI runs them plus a mutation-test suite on every push.
7. **Honest evidence reading.** Student evaluations are treated as biased,
   small-sample evidence of student experience — analyzed thematically, triangulated,
   and caveated — not as a teaching-quality score.

## Repository layout

```
course-designer/        SKILL.md + agents/ + references/ + templates/
lesson-builder/         〃
assessment-architect/   〃
student-mentor/         〃
submission-auditor/     〃
teaching-reflector/     〃
teaching-pipeline/      SKILL.md + agents/ + references/
deck-studio/            extension skills, same layout
lab-forge/              〃
media-scripter/         〃
course-publisher/       〃
ta-coordinator/         〃
accreditation-mapper/   〃
bilingual-courseware/   〃
cohort-analyst/         〃
shared/                 Course Passport schema (prose + JSON Schema) · pedagogy
                        foundations · gate protocols · AI-era integrity · checkpoints
scripts/                check_passport.py · check_alignment_gate.py · build_dashboard.py · registry lint
tests/                  validator suite (golden fixture + mutation tests)
commands/               /ts-* slash commands
docs/                   ARCHITECTURE.md
.claude-plugin/         plugin + marketplace manifests
skills/                 symlinks for plugin auto-discovery
```

## Languages

English and Simplified Chinese trigger keywords ship by default; intent-based modes
(socratic design, mid-entry routing) work in any language. Add your language's keywords
to a skill's `description` frontmatter to improve trigger matching.

## Portability

This repo is the **Claude Code** distribution (native skills, `/plugin` install, `/ts-*`
slash commands). The suite is three layers with different reach:

- **Skills** (the `SKILL.md` content) follow Anthropic's Agent Skills format and also
  work on other Claude surfaces (claude.ai, Claude Desktop, the IDE extensions) via the
  Skills feature.
- **The Python tooling** (`scripts/`, the JSON Schema, the dashboard) is fully
  tool-agnostic — it runs in any terminal with `python3`, no AI required.
- **The plugin packaging** (marketplace install, slash commands) is Claude-Code-specific.

For **OpenAI Codex CLI**, a sibling distribution is generated from this repo by
`scripts/build_codex.py` and published at
[`YujxZJCN/teaching-skills-codex`](https://github.com/YujxZJCN/teaching-skills-codex) —
the whole suite as a single Codex skill with `ts-*` aliases. It is a build product
(regenerated, never hand-edited), so it never drifts from this source.

## License

MIT. The architecture (skills/agents/gates/passport pattern) is inspired by
[Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)
(CC BY-NC 4.0); no content from that project is reproduced here.
