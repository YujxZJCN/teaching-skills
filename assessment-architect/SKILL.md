---
name: assessment-architect
description: "Builds assessment instruments for university professors — pipeline Stage 3. 7-agent team covering test blueprints, exam/quiz/question-bank item writing, rubric design (analytic/holistic/single-point), TILT project briefs, AI-era integrity auditing, verified answer keys with worked solutions, and post-exam item analysis. Triggers on: exam, midterm, final, quiz, test questions, rubric, grading criteria, project brief, assignment design, question bank, item analysis, academic integrity, AI-proof, 出题, 试卷, 考试, 测验, 评分标准, 评分量表, 课程项目, 题库, 试题分析, 学术诚信."
metadata:
  version: "1.0.0"
  last_updated: "2026-06-10"
  status: active
  pipeline_stage: 3
  related_skills:
    - course-designer
    - lesson-builder
    - teaching-pipeline
---

# Assessment Architect — Instrument Construction Team

Builds the actual instruments the assessment plan promised: exams, quizzes, question
banks, rubrics, project briefs — then audits them for AI-era integrity and analyzes how
they performed. The plan (types, weights, timing) is Stage 1 work and lives in the Course
Passport; this skill turns each `assessment_plan` entry into something students can sit,
submit, and be fairly graded on.

> **Prime rule:** blueprint before items (Pedagogy Foundations §10). A test written
> question-by-question measures whatever was easy to ask; a test written from a confirmed
> content × Bloom blueprint measures the outcomes. No item is drafted before the
> professor confirms the blueprint — ever.

## Quick Start

```
Write the midterm for CS 201 — it's A1 in the passport
给我的数据结构课出一份期末试卷
Build a rubric for the term paper
Design the semester project brief, AI-disclosure tier
我的考试结果在这个表里，帮我做试题分析
Audit my take-home final for AI vulnerability
```

## Modes

| Mode | Trigger intent | Output |
|------|---------------|--------|
| `exam` | "Write the midterm/final/exam for…" | Blueprint → items → verified key → logistics (versions, accommodations, instructions) |
| `quiz` | "Quiz on this week's material"; low-stakes retrieval | Short retrieval set with key, sized to minutes available (Pedagogy Foundations §5) |
| `question-bank` | "Build a question bank / pool for…" | Tagged item bank with parallel variants for reuse and randomization |
| `rubric` | "Rubric / grading criteria for…" | Analytic, holistic, or single-point rubric + TA calibration notes |
| `project-brief` | "Design the project / assignment for…" | Student-facing TILT brief (Purpose/Task/Criteria) with milestones + instructor block |
| `integrity-check` | "Is this AI-proof?"; pipeline Stage 3 audit | AI-resilience audit per `shared/ai_era_integrity.md` — standalone or pipeline, read-only |
| `item-analysis` | "Analyze my exam results"; post-exam | Difficulty, discrimination, distractor analysis from a professor-provided results table |
| `answer-key` | "Make/check the key for this exam" | Regenerated key for an existing instrument: worked solutions, grading notes, discrepancy flags |

**Mode dispatch rule:** an instrument request that names no passport assessment runs
standalone — intake the context, build, and offer passport write-back at exit (Passport
Iron Rule 5). Detect intent in any language.

### Does NOT trigger

| Scenario | Use instead |
|----------|-------------|
| Deciding assessment types, weights, or timing (the *structure*) | `course-designer` |
| Practice activities and exercises that aren't graded | `lesson-builder` |
| Writing feedback comments on a specific student's work | `student-mentor` |
| Full design → materials → assessment run | `teaching-pipeline` |

## Agent Team (7)

| Agent | Role |
|-------|------|
| `blueprint_agent` | Builds the test blueprint: content × Bloom matrix from passport outcomes, point and time budgets; flags level mismatches |
| `item_writer_agent` | Drafts items per blueprint cell using `references/item_writing_rules.md`; distractors from known misconceptions; bank variants |
| `rubric_designer_agent` | Designs analytic/holistic/single-point rubrics with observable descriptors and TA calibration anchors |
| `project_designer_agent` | Writes TILT-structured project and assignment briefs with milestone staging and scope honesty |
| `integrity_auditor_agent` | Runs the `shared/ai_era_integrity.md` audit procedure; read-only; sets `ai_resilience`; never recommends detectors |
| `answer_key_agent` | Independently *works* every item to produce the key + worked solutions; flags discrepancies, marks `[VERIFY]` where uncertain |
| `item_analyst_agent` | Post-exam statistics: difficulty, discrimination, distractor performance; per-item action recommendations |

## Workflow (`exam` mode)

```
Phase 0  INTAKE      — load the passport assessment entry (id, weight, week,
                       outcomes_assessed, ai_tier) or intake standalone: outcomes,
                       topics taught, exam length, format constraints. Missing
                       context = ask, don't guess (Passport Iron Rule 2).
Phase 1  BLUEPRINT   — blueprint_agent builds the content × Bloom matrix from
                       outcomes_assessed, allocates points, budgets time per item
                       type (`templates/test_blueprint_template.md`)
         🧑 checkpoint: blueprint confirmed BEFORE any item exists (iron rule 1 —
            this is where coverage and difficulty are actually decided)
Phase 2  ITEMS       — item_writer drafts items cell by cell, each tagged with
                       LO id + Bloom level + blueprint cell
Phase 3  KEY         — answer_key_agent works every item from scratch — solving,
                       not transcribing the writer's intent. Discrepancies between
                       worked and intended answers are flagged, never reconciled
                       silently (iron rule 3)
Phase 4  INTEGRITY   — integrity_auditor reviews the assembled instrument against
                       its declared tier per shared/ai_era_integrity.md
Phase 5  ASSEMBLE    — exam document + logistics: version variants if requested,
                       extra-time accommodation variant noted (Quality Gate U3),
                       exam-day instructions, point check against blueprint
         🧑 checkpoint: instrument confirmed → passport artifact_ref + ai_resilience
            updated, confirmed_by_professor recorded
```

`quiz` and `question-bank` run the same spine with a lighter Phase 1 (a mini-blueprint
still shown, still confirmed). `rubric` and `project-brief` go straight to their agent,
then Phase 4. `integrity-check`, `item-analysis`, and `answer-key` are single-agent modes
ending in a checkpoint.

## Iron rules

1. **Blueprint first, always.** No item is written before the professor confirms the
   blueprint. A professor in a hurry gets a fast minimal blueprint, not a skipped one.
2. **Item–outcome traceability.** Every item carries an LO id and Bloom level. An item
   that maps to no outcome is a defect to fix or cut, not a bonus question to keep.
3. **Key independence.** The answer key is produced by *solving each item*, not by
   copying the writer's intended answer. When worked answer and intended answer differ,
   both go to the checkpoint — the discrepancy is the finding; silently picking one hides
   a broken item or a broken key.
4. **`[VERIFY]` honesty.** Domain facts, computed values, and discipline conventions the
   agents cannot fully verify are marked `[VERIFY: <what to check>]`. A confident wrong
   key is the worst artifact this skill can produce.
5. **Integrity audit never inflates.** `ai_resilience` is set only by the audit procedure
   in `shared/ai_era_integrity.md` — `reviewed`, `redesigned`, or `reviewed` with an
   accepted-risk note. No instrument is called "AI-proof"; none is.
6. **Accommodation variant always derivable.** Exam logistics state how the extra-time
   version is produced (same instrument, adjusted clock, or reduced-length variant) so
   Quality Gate U3 passes by construction. Passport write-back (`artifact_ref`,
   `ai_resilience`, `artifacts[]`) happens only after the professor confirms.

## Outputs

- `assessments/<id>_<slug>.md` — the instrument (exam, quiz, bank, or brief)
- `assessments/<id>_key.md` — answer key with worked solutions and grading notes
  (kept separate from the student-facing instrument)
- `assessments/<id>_blueprint.md` — from `templates/test_blueprint_template.md`
- `assessments/<id>_rubric.md` — when a rubric is built
- (`integrity-check` mode) `integrity_audit.md`
- (`item-analysis` mode) `item_analysis_report.md` + passport `iteration_history` evidence entry
- Passport updates: `assessment_plan[].artifact_ref`, `assessment_plan[].ai_resilience`, `artifacts[]`

## References

- `references/item_writing_rules.md` — stem/option rules, per-format guidance,
  higher-order item patterns, bank-variant discipline
- `references/rubric_patterns.md` — rubric-type choice logic, descriptor rules,
  common defects, TA calibration protocol
- `templates/test_blueprint_template.md`
- `templates/project_brief_template.md`
- Shared: `shared/pedagogy_foundations.md`, `shared/ai_era_integrity.md`,
  `shared/quality_gate_protocol.md`, `shared/checkpoint_protocol.md`,
  `shared/course_passport_schema.md`
