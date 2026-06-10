# Mode Registry

Canonical list of every mode in the suite. Slash commands in `commands/` map 1:1 onto
entries here. When adding a mode: update the skill's SKILL.md, this registry, and
`docs/ARCHITECTURE.md` together.

## course-designer (6 modes) — Stage 1

| Mode | Command | Purpose |
|------|---------|---------|
| full | `/ts-course` | Complete backward design: outcomes → assessment plan → schedule → syllabus |
| socratic | — (intent-triggered) | Guided dialogue → Course Concept Brief |
| outcomes-only | `/ts-outcomes` | Bloom-tagged learning outcome set |
| syllabus-only | `/ts-syllabus` | Syllabus from existing design |
| redesign | `/ts-redesign` | Diagnostic + prioritized redesign of existing course |
| align-check | `/ts-align` | Read-only constructive-alignment audit (Gate 1.5 standalone) |

## lesson-builder (8 modes) — Stage 2

| Mode | Command | Purpose |
|------|---------|---------|
| full | `/ts-lesson` | Complete package for one class meeting |
| lecture-notes | — | Prose lecture notes for a session |
| slides-outline | — | Assertion-evidence slide outline |
| activities | `/ts-activities` | Active-learning activity design |
| case-study | — | Teaching case + teaching notes |
| discussion-guide | — | Question ladders + facilitation plan |
| flipped | — | Pre-class spec + in-class application session |
| week-batch | — (pipeline) | Build a passport week / range of weeks |

## assessment-architect (8 modes) — Stage 3

| Mode | Command | Purpose |
|------|---------|---------|
| exam | `/ts-exam` | Blueprint → items → verified key → logistics |
| quiz | — | Low-stakes retrieval sets |
| question-bank | — | Item bank with controlled variants |
| rubric | `/ts-rubric` | Analytic / holistic / single-point rubric |
| project-brief | — | TILT-structured assignment brief |
| integrity-check | `/ts-integrity` | AI-resilience audit per `shared/ai_era_integrity.md` |
| item-analysis | — | Post-exam difficulty / discrimination / distractor analysis |
| answer-key | — | Independent worked key for an existing instrument |

## student-mentor (6 modes) — Stage 4

| Mode | Command | Purpose |
|------|---------|---------|
| feedback | `/ts-feedback` | Structured feedback on student work (single / batch) |
| struggling-student | — | Evidence-based intervention plan + outreach draft |
| recommendation-letter | `/ts-letter` | Intake interview → letter draft |
| student-email | — | Difficult communications drafting |
| office-hours | — | Office-hours prep and triage |
| mentoring-plan | — | Advisee expectations doc + milestone map |

## teaching-reflector (6 modes) — Stage 5

| Mode | Command | Purpose |
|------|---------|---------|
| eval-analysis | `/ts-evals` | Thematic, bias-caveated evaluation analysis |
| midcourse | `/ts-midcourse` | Mid-semester feedback instrument + closing the loop |
| peer-observation | — | Observation prep packet / observation protocol |
| portfolio | — | Teaching portfolio assembly from real artifacts |
| teaching-statement | `/ts-statement` | Socratic elicitation → statement draft |
| sotl | — | Classroom-inquiry design (with IRB pointer) |

## submission-auditor (5 modes) — Stage 4

| Mode | Command | Purpose |
|------|---------|---------|
| spec | `/ts-spec` | Compile template / requirements / rubric / exemplar into a confirmed Submission Spec |
| audit | `/ts-audit` | Check one submission against the spec; feedback report draft |
| batch-audit | `/ts-audit` (multiple) | Per-student reports + class pattern report + fairness record |
| self-check | — | Student-facing pre-submission checklist from the spec |
| calibrate | — | Revise spec checks against professor verdicts on sampled findings |

## teaching-pipeline (4 modes) — Orchestrator

| Mode | Command | Purpose |
|------|---------|---------|
| full | `/ts-full` | Stage 0 → 6 lifecycle over the Course Passport |
| mid-entry | — (intent-triggered) | Validate existing materials, enter at the right stage |
| status | `/ts-status` | Passport + calendar position → what's next |
| new-term | — | Stage 6 → Stage 1 redesign re-entry with evidence |

**Total: 43 modes across 7 skills, 38 agents.**
