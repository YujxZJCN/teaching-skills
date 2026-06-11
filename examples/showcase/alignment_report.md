# Alignment Gate Report (Gate 1.5) — CS 304 Introduction to Machine Learning

**Run:** 2026-06-10 · **Agent:** alignment_auditor_agent (read-only) · **Mode:** `align-check`
**Input:** course_passport.yaml (passport_version 1.0)
**Protocol:** shared/alignment_gate_protocol.md — checks A1-A5, B1-B4, C1-C4, D1-D3

## Verdict: PASS-WITH-WARNINGS

No BLOCK findings. 2 WARN findings, both dismissed by the professor at the gate
checkpoint with logged reasons (below). Gate closed with professor acknowledgment
2026-06-10; status and findings written to `gates.alignment_gate` — the only
passport field this agent touches.

## Findings (ordered BLOCK → WARN)

| # | Check | Severity | Finding (cites passport ids) | Citation | Suggested direction | Resolution |
|---|-------|----------|------------------------------|----------|---------------------|------------|
| 1 | C2 | WARN | A4 course project weight 30% is within the 40% single-assessment limit, but A4 (final report M3 due W14) and A6 (final exam, W16) together resolve 45% of the grade in the final six weeks of the term. Affected: A4, A6. | Pedagogy Foundations §5 | If not deliberate, shift weight from M3 toward M2, or move M3 earlier. | **Dismissed by professor:** "deliberate — A4's staged milestones move 12 of its 30 points and the bulk of the project work outside the final six weeks (M1 W6 4%, M2 W10 8%); only the final report (18%) plus A6 (15%) genuinely lands late." Logged; will not be re-raised. |
| 2 | B3 | WARN | Bloom distribution sanity: LO6 (create) is the sole create-level outcome and is evidenced only by A4/A5; if a team's project collapses, no other instrument shows create-level work. Affected: LO6, A4, A5. | Pedagogy Foundations §3 | Optional: add a small create-level component to A2 Lab 4. | **Dismissed by professor:** "acknowledged — one create-level outcome is the intended scope for a first ML course; team-collapse risk is mitigated by milestone feedback at W6 and W10." Logged; will not be re-raised. |

**NOT_EVALUABLE:** none — the passport contained the data required for every check.

## Check results in full

| Check | Result | Evidence (passport ids) |
|-------|--------|-------------------------|
| A1 — every LO has non-empty `assessed_by` | pass | LO1-LO6 all map to ≥1 of A1-A6 |
| A2 — every LO has non-empty `taught_in` | pass | LO1-LO6 all map to ≥1 schedule week |
| A3 — every assessment's `outcomes_assessed` non-empty, ids exist | pass | A1-A6 all reference existing LO ids |
| A4 — every week maps to ≥1 outcome or is tagged `logistics` | pass | W1-W7, W9-W14 carry outcomes; W8 (midterm), W15 (review/defenses), W16 (final) tagged `logistics` |
| A5 — no outcome assessed before first taught | pass | checked against each assessment's first due week: A1 first due W2 (LO1 first taught W1, LO3 W2); A2 first due W5 (LO2 W3, LO3 W2, LO4 W5); A3 W8 (all four LOs taught by W7); A4 first milestone W6 (LO4 W5, LO5 W5, LO6 W5 — project launch workshop); A5 W15; A6 W16 |
| B1 — measurable outcome verbs | pass | explain / implement / apply / diagnose / evaluate / design-and-carry-out |
| B2 — `bloom_level` declared for every LO | pass | LO1-LO6 |
| B3 — Bloom distribution sanity | WARN | finding 2 (dismissed) |
| B4 — outcome count reviewable | pass | 6 outcomes (3-8 typical) |
| C1 — weights sum to 100% | pass | 10 + 20 + 25 + 30 + 0 + 15 = 100 (A5 is a 0%-weight completion gate) |
| C2 — no single assessment > 40% | WARN | finding 1 (dismissed) — A4 at 30% passes the threshold; concentration noted |
| C3 — low-stakes before first high-stakes | pass | A1 quizzes begin W2; first high-stakes is A3 at W8 |
| C4 — assessment types plausibly cover outcome levels | pass | LO6 (create) → A4 project + A5 defense; LO4 (analyze) → A3 data-interpretation cells + A2/A4; LO5 (evaluate) → A4/A5/A6 |
| D1 — weekly out-of-class hours computed and recorded | pass | arithmetic below; recorded in `workload_audit` with constants |
| D2 — estimate within ±25% of credit-hour convention | pass | 6.2 vs 6.0 target = +3.3% (note below) |
| D3 — no week with two major deliverables without sign-off | pass | labs (W5/W7/W11/W13) and milestones (W6/W10/W14) never collide; quizzes are minor by design |

## Workload arithmetic (D1/D2)

Constants follow shared/alignment_gate_protocol.md heuristics (Rice-estimator
style); the professor may adjust any constant — they are recorded so the
calculation is re-runnable.

| Component | Calculation | Hrs/week |
|-----------|-------------|----------|
| Reading | 20 pages/wk × ~450 words/page ÷ 100 wpm (dense technical, read-to-understand) | 1.5 |
| Lab assignments | 4 labs × (4 h professor estimate × 3 novice multiplier) = 48 h ÷ 16 wk | 3.0 |
| Course project | 22 h per-student team-share estimate (incl. all milestones) ÷ 16 wk | 1.4 |
| Quiz preparation | 10 quizzes × 0.5 h ÷ 16 wk | 0.3 |
| **Total** | | **6.2** |

Target: 2 out-of-class hours × 3 contact hours = **6.0 hrs/week**. Estimate 6.2
is **+3.3%, within the ±25% tolerance** → `workload_audit.status: within_range`.
Exam preparation is treated as redistribution of regular study time, not an
addition — a recorded modeling choice, not a fact; adjust if your students'
exam-prep behavior differs.

## Notes

- Previously dismissed findings: none on file before this run (first gate run for
  this design); both WARNs above were dismissed at this run's checkpoint and will
  be skipped in future runs per protocol.
- This gate checks structure, not merit: topic choices and week ordering were not
  evaluated and are not this agent's findings to make.

---
*Checkpoint record: professor acknowledged verdict and dismissed findings 1-2
with the reasons logged above. Gate status `pass`, `last_run: 2026-06-10`.*
