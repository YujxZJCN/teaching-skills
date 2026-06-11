# AI-Era Integrity Audit — CS 304 Introduction to Machine Learning

**Run:** 2026-06-10 · **Agent:** integrity_auditor_agent (read-only on instruments) · **Mode:** `integrity-check`
**Scope:** assessment plan A1-A6 (course_passport.yaml) · **Procedure:** shared/ai_era_integrity.md §"The audit procedure"

Vulnerability question applied to each assessment, honestly: *could a current
frontier model complete this to a passing standard with ≤3 prompts and no course
context?* The audit reports risk in plain language; it proposes design options,
never policing measures. `ai_resilience` is the only passport field this agent
writes, and `redesigned` is set only after the professor accepted the changes and
the producing agent implemented them.

## Per-assessment audit (ordered by weight, heaviest first)

| ID | Assessment | Weight | Vulnerability (honest estimate) | Declared tier | Coherence verdict | `ai_resilience` |
|----|------------|--------|--------------------------------|---------------|-------------------|-----------------|
| A4 | Course project (staged M1/M2/M3) | 30% | **High as originally designed** — see redesign case below. **Medium after redesign:** product parts remain AI-assistable (which Tier D permits), but the process trail and live defense are not fakeable in ≤3 prompts. | D — permitted with disclosure | **Coherent after redesign** | `redesigned` |
| A3 | Midterm exam | 25% | **Low** — in-class, closed-book, supervised, no devices; no out-of-room channel to a model. | P — prohibited | Coherent: supervised Tier-P is the anchor pattern (resilience pattern 1). | `reviewed` |
| A2 | Lab assignments (4) | 20% | **High** — take-home code; the core tasks (implement linear models, train an MLP, run CV) are squarely within frontier-model reach with ≤3 generic prompts. | D — permitted with disclosure | **Coherent as Tier D, with accepted residual risk** — see note below. | `reviewed` (accepted-risk note) |
| A6 | Final exam | 15% | **Low** — in-class, supervised, same conditions as A3. | P — prohibited | Coherent (pattern 1). | `reviewed` |
| A1 | Weekly quizzes | 10% | **Low** — administered on paper at lab start, devices away; effectively supervised. | P — prohibited | Coherent (pattern 1). | `reviewed` |
| A5 | Project defense (sampled) | 0% (required gate) | **Low** — live 5-minute oral about the team's own submission. | P — prohibited | Coherent (pattern 5, defense sampling); rate stated below so it is an option, not a wish. | `reviewed` |

## The redesign case: A4

**Original design (2025 Fall):** single-deadline take-home project — code +
report due W14, product-only grading. Declared Tier D, but with **high**
vulnerability and *no process evidence*: a model could produce the entire
submission, and the disclosure requirement had nothing structural to anchor it.
Tier D with nothing measuring the human contribution is disclosure theater.

**Redesign accepted by the professor (logged in `iteration_history`, motivated
independently by 2025 Fall evaluation themes and a 31% late rate):**

1. **Staged milestones** (resilience pattern 2 — process evidence): M1 proposal
   W6 (4%), M2 progress report W10 (8%), M3 final report W14 (18%). M2 and M3
   each include a feedback-response note — what the team changed in response to
   the previous milestone's feedback. A coherent process trail across 8 weeks is
   far harder to fake than a product.
2. **Team-chosen datasets with instructor approval at M1** (pattern 3,
   partially — personalized inputs): generic prompts get generic answers;
   team-specific data does not.
3. **Sampled 5-minute defenses, W15** (pattern 5): ~12 of 30 teams drawn openly,
   announced in the syllabus from day one as policy, not accusation. Cost: ~60
   min of the W15 lab session plus scheduling — stated so the professor chose it
   with eyes open. Recorded as A5 (0%-weight completion gate for M3).

`ai_resilience: redesigned` was set only after the professor accepted these
changes and project_designer_agent rebuilt the brief.

## The accepted-risk case: A2

Labs stay take-home and stay high-vulnerability — redesigning them into
supervised work would cost the lab sessions their clinic function, and Tier D is
the *pedagogically intended* policy: disciplined tool use is part of LO2/LO3
practice as professionals actually do it. Mitigation in place: the disclosure
appendix is **required and graded for quality** (pattern 6), and each lab's
concepts are re-measured unaided in A3/A6 (40% of the grade is supervised).

**Professor accepted the residual risk for the 20% weight; note logged here and
in the passport (A2 `ai_resilience: reviewed` with accepted-risk comment).**
Recorded honestly per procedure step 5 — this is a legitimate outcome, not a
failure, and it is what Quality Gate Q3 will read when it checks that every
≥20% assessment has either a structurally resilient component or exactly this
kind of explicit note.

## Detection tools

**No AI-detection tool is used, recommended, or relied on anywhere in this plan**
(ground truth 1; Quality Gate Q4). Detector false-positive rates make individual
accusations indefensible, and the documented bias against non-native English
writers makes them especially unacceptable in this EMI classroom. Integrity here
is a design property — supervision, process evidence, personalization, defense
sampling — not a forensic one.

## Cross-reference: syllabus AI-policy table

This audit's tier declarations are rendered student-facing in syllabus.md
§"AI use in this course", one rationale line per tier choice, and summarized in
`policies.ai_use_policy`:

| Assessments | Tier | One-line rationale (as shown to students) |
|-------------|------|-------------------------------------------|
| A1, A3, A6 | P | measure unaided fluency the rest of the work stands on |
| A2, A4 | D | professional-practice tools, used with judgment shown in a graded disclosure |
| A5 | P | a live conversation about your own work, by design unaided |

---
*Checkpoint record: professor accepted the A4 redesign and the A2 residual risk
2026-06-10; `ai_resilience` fields updated in the passport (the only fields this
agent writes). Nothing in this report drafts sanction policy — the institutional
integrity policy slot in the passport remains `[NEEDS PROFESSOR INPUT]` for the
professor's own link.*
