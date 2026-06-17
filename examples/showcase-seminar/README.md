# Showcase: a humanities seminar, and the person-affecting skills

This directory is **worked example output** — a second showcase, the humanities counterpart
to [`examples/showcase/`](../showcase/). Where that one is a 90-person STEM lecture course
(CS 304, Introduction to Machine Learning), this one is a small discussion- and
writing-based seminar — and it deliberately exercises the parts of the suite the STEM
showcase leaves dark: the **person-affecting** skills (recommendation letters, structured
feedback), which produce drafts about individual students and so had no inspectable output
until now.

**Honest framing, before anything else:** HIST 247 "The Atlantic World, 1500–1800" is a
*hypothetical demonstration seminar*. It is not a real offering at any institution. These
artifacts were authored by running the suite's documented procedures (templates, protocols,
schema, validators) against a fixed course brief; all data in them is synthetic — the
workload constants, the dismissed-warning reasons, the iteration history. **The
person-affecting files are illustrative drafts**: "A. Student" and "[STUDENT NAME]" are
obvious placeholders, the recommendation and feedback evidence is invented, and each file
says so at the top. They exist to demonstrate the templates' anti-fabrication structure —
the claim-to-intake trace, the evidence-quoting, the non-removable verify blocks — not to
describe a real person. Where a real run would stop and ask the professor, these artifacts
stop too (the `[NEEDS PROFESSOR INPUT]` markers); that is the point of the demonstration.

## Contents

| File | Produced in real use by | Skill · mode |
|------|-------------------------|--------------|
| [course_passport.yaml](course_passport.yaml) | the ledger every stage reads and appends to; gate fields stamped by `alignment_auditor_agent`, `ai_resilience` by `integrity_auditor_agent` | `course-designer` · `full` (`/ts-course`) → Stage 1–3 |
| [syllabus.md](syllabus.md) | `course-designer` · `syllabus-only` (`/ts-syllabus`) | Stage 1 |
| [alignment_report.md](alignment_report.md) | `alignment_auditor_agent` (read-only) | Gate 1.5 — `course-designer` · `align-check` (`/ts-align`) |
| [research_essay_brief.md](research_essay_brief.md) | `assessment-architect` · project brief (TILT) (`/ts-rubric` family) | Stage 3 |
| [recommendation_letter_draft.md](recommendation_letter_draft.md) | `student-mentor` · `recommendation-letter` (`/ts-letter`) | during-semester (person-affecting) |
| [intake_record.md](intake_record.md) | `student-mentor` · `recommendation-letter` intake step (`/ts-letter`) | during-semester (person-affecting) |
| [feedback_report.md](feedback_report.md) | `student-mentor` · `feedback` (`/ts-feedback`) | during-semester (person-affecting) |

The first four files describe the same course and are mutually consistent: LO ids (LO1–LO5),
assessment ids (A1–A5), week ids (W1–W15), weights, the specs-graded reading responses, and
the per-tier AI policy line up across the passport, syllabus, alignment report, and brief —
that consistency is what the Course Passport exists to enforce. The last three files are
**standalone**: they concern individual students and, by the suite's iron rule, never enter
the passport ledger.

## What to notice

1. **The recommendation letter's claim-to-intake trace.** Every evaluative sentence in
   [recommendation_letter_draft.md](recommendation_letter_draft.md) carries a `[C#]` tag, and
   the trace appendix accounts for all of them against rows in
   [intake_record.md](intake_record.md) — "Untraced claims: none." The intake record is built
   *first*; the letter is drafted only from it. A fabricated anecdote would surface as a blank
   `Intake source` cell in the ledger, not as fluent prose. Note what the professor explicitly
   **declines** to claim (no cross-year ranking, no language-prep comment) — the comparative
   bracket is honest, and both files end with the non-removable verify-before-sending block.

2. **The feedback report quotes the work it judges.** Every comment in
   [feedback_report.md](feedback_report.md) locates or quotes the specific thing in the
   (described) paper it refers to — the opening claim, the §3 close reading, the §6 presentist
   phrase — and is structured goal → status → next step in priority order, ending with one
   habit to carry forward and the non-removable verify-before-releasing block. Feedback the
   student can't connect to their own page isn't actionable.

3. **The specs-flavored grading.** Reading responses (A2) are marked pass / revise against a
   posted spec (a defensible claim · a source read as evidence · contextualization), with a
   one-time resubmission and best-5-of-6 counted — an alternative-grading scheme stated in
   `policies.grading_scheme` and explained in the syllabus. It is also what lets the seminar
   pass the alignment gate without a sub-10% assessment: the gate flags the missing low-stakes
   calibrator (C3), and the professor dismisses it with the reasoning that these low-stakes,
   spec-graded responses *are* the calibrator. That dismissed finding sits, reason attached, in
   `gates.alignment_gate.findings[]`.

4. **A seminar-appropriate Bloom spread.** The five outcomes run understand → apply → analyze →
   evaluate → create — no inflation, but no survey-course flatness either, with the analytical
   and evaluative work (source contextualization, historiography, resisting presentism) that a
   discussion seminar actually trains, and a single create-level outcome (LO5) carried by the
   staged research essay. The course is built backward from those outcomes, not from a topic
   list.

5. **No student data is in the passport.** The person-affecting files are deliberately **not**
   listed in `artifacts[]` and nothing identifiable about any student appears in
   course_passport.yaml — `learner_profile.cohort_evidence` is `null`, and the passport passes
   the validator's P11 PII guard with zero student names, emails, or ids. The recommendation,
   intake, and feedback files stand on their own. Student content and the course ledger are
   kept in separate worlds on purpose.

## Reproducing the checks

Both validators pass on the passport in this directory:

```
python3 scripts/check_passport.py        examples/showcase-seminar/course_passport.yaml   # VALID
python3 scripts/check_alignment_gate.py  examples/showcase-seminar/course_passport.yaml   # PASS-WITH-WARNINGS
```

The alignment gate reports one live WARN (D3 — the research essay and the take-home synthesis
both fall in W15, acknowledged and left visible for publication-stage sequencing) and
suppresses two earlier-dismissed findings (C3 low-stakes calibration; D2 the deliberately
reading-heavy workload), per protocol — a dismissed warning is recorded with its reason and
never re-raised.
