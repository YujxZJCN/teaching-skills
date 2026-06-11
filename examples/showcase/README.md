# Showcase: one course through the pipeline

This directory is **worked example output** — a set of artifacts you can inspect
to judge what this suite actually produces before installing it.

**Honest framing, before anything else:** CS 304 "Introduction to Machine
Learning" is a *hypothetical demonstration course*. It is not a real offering at
any institution. These artifacts were authored by running the suite's documented
procedures (templates, protocols, agent specs) against a fixed course brief; all
data in them is synthetic — the evaluation themes, the late-submission rate, the
workload constants, the iteration history. No real students, instructors, or
institutional policies appear anywhere; names and contacts are explicit
placeholders ("Prof. EXAMPLE"). Where a real run would stop and ask the
professor, these artifacts stop too — that is the point of the demonstration.

## Contents

| File | Produced in real use by | Stage |
|------|-------------------------|-------|
| [course_passport.yaml](course_passport.yaml) | `course-designer` · `full` mode (`/ts-course`); gate fields stamped by `alignment_auditor_agent`, `ai_resilience` fields by `integrity_auditor_agent` | 1 → 3 (the ledger every stage appends to) |
| [syllabus.md](syllabus.md) | `course-designer` · `syllabus-only` mode (`/ts-syllabus`) | 1 |
| [alignment_report.md](alignment_report.md) | `alignment_auditor_agent` via `course-designer` · `align-check` mode (`/ts-align`) | Gate 1.5 |
| [lesson_W06_overfitting.md](lesson_W06_overfitting.md) | `lesson-builder` · `full` mode (`/ts-lesson`) | 2 |
| [activity_W06_bias_variance.md](activity_W06_bias_variance.md) | `lesson-builder` · `activities` mode (`/ts-activities`) | 2 |
| [exam_blueprint_midterm.md](exam_blueprint_midterm.md) | `assessment-architect` · `exam` mode (`/ts-exam`), Phase 1 (`blueprint_agent`) | 3 |
| [midterm_items_sample.md](midterm_items_sample.md) | `assessment-architect` · `exam` mode, Phases 2-3 (`item_writer_agent` + `answer_key_agent`) | 3 |
| [integrity_audit.md](integrity_audit.md) | `integrity_auditor_agent` via `assessment-architect` · `integrity-check` mode (`/ts-integrity`) | 3 |

All eight artifacts describe the same course: LO ids, assessment ids (A1-A6),
week ids (W1-W16), weights, and topic names are consistent across every file —
that consistency is what the Course Passport exists to enforce.

## What to notice

1. **The `[NEEDS PROFESSOR INPUT]` markers are deliberately unfilled.** The
   syllabus carries exactly two (institutional integrity policy, disability-
   services statement) and the passport one (`policies.integrity_policy`). The
   suite never invents institutional policy — it marks the gap and waits. The
   same convention appears as a `[VERIFY]` marker on one numeric claim in the W6
   lesson plan: uncertain domain facts are flagged for the professor, not
   asserted.
2. **The dismissed-warning trail.** alignment_report.md shows a C2 finding
   (grade concentration across A4 + A6) that the professor dismissed *with a
   logged reason* — and the same finding, reason attached, sits in the
   passport's `gates.alignment_gate.findings[]`. Dismissals are recorded, never
   silently dropped, and never re-raised in later runs.
3. **Blueprint before items.** exam_blueprint_midterm.md fixes the Content ×
   Bloom matrix, point totals, and time budget (78 of 90 min, arithmetic shown)
   *before* any item exists; every sample item in midterm_items_sample.md then
   tags the exact cell it fills. Items are written into a measurement plan, not
   improvised.
4. **Tier coherence in the integrity audit.** integrity_audit.md pairs an honest
   vulnerability estimate with the declared P/D/O tier for each of A1-A6 — and
   shows both honest outcomes: a redesign (A4: single-deadline take-home →
   staged milestones + sampled defenses, `ai_resilience: redesigned`) and an
   accepted risk recorded as exactly that (A2 labs, `reviewed` with a logged
   note). No AI-detection tools anywhere, by iron rule.
5. **Item-outcome traceability, both directions.** Each sample exam item carries
   LO id + Bloom level + blueprint cell; the blueprint's outcome table shows
   points per LO; the passport shows the same LOs' `assessed_by` lists. You can
   trace a single multiple-choice distractor back to the misconception in
   `learner_profile.known_difficulties` it was written to catch — and the
   worked-key excerpt shows a real discrepancy flag from the independently
   solved key, resolved by the professor at a checkpoint.
