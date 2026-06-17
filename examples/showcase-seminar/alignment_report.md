# Alignment Gate Report (Gate 1.5) — HIST 247 The Atlantic World, 1500–1800

**Run:** 2026-06-15 · **Agent:** alignment_auditor_agent (read-only) · **Mode:** `align-check`
**Input:** course_passport.yaml (passport_version 1.0)
**Protocol:** shared/alignment_gate_protocol.md — checks A1-A5, B1-B4, C1-C4, D1-D3

## Verdict: PASS-WITH-WARNINGS

No BLOCK findings. 3 WARN findings: two dismissed by the professor at the gate checkpoint
with logged reasons (C3, D2), and one (D3) left live and recorded as a sequencing item to
re-check at publication. Gate closed with professor acknowledgment 2026-06-15; status and
findings written to `gates.alignment_gate` — the only passport field this agent touches.

## Findings (ordered BLOCK → WARN)

| # | Check | Severity | Finding (cites passport ids) | Citation | Suggested direction | Resolution |
|---|-------|----------|------------------------------|----------|---------------------|------------|
| 1 | C3 | WARN | No assessment carries a low-stakes weight (≤ 10%); the first high-stakes assessment (A3 primary-source paper, 20%, due W6) is not preceded by a formally low-stakes one. | Pedagogy Foundations §5, §10 | Add a sub-10% assessment early, or confirm an existing mid-stakes one plays the calibration role. | **Dismissed by professor:** "deliberate — the reading responses (A2, 15%) are the calibration instrument: low individual stakes (best 5 of 6, ~3% each), specs-graded pass/revise with a free resubmission, and they begin W2, four weeks before the first paper. They do the job a sub-10% assessment would." Logged; will not be re-raised. |
| 2 | D2 | WARN | Estimated out-of-class workload 6.3 h/wk vs credit-hour target 5.0 h/wk is +26%, just outside the ±25% tolerance — driven by ~70 pp/wk of seminar reading. Affected: none cited (course-level). | Workload heuristics (Rice-estimator style) | If unintended, trim weekly reading or shift some to optional. | **Dismissed by professor:** "acknowledged — a reading-intensive upper-level seminar runs deliberately above the generic credit-hour convention; the reading load is core to the course and will be signalled plainly in the syllabus." Logged; will not be re-raised. |
| 3 | D3 | WARN | W15 lists two major deliverables: A4 (research essay final, 20%) and A5 (take-home synthesis, 15%). Affected: A4, A5, W15. | Pedagogy Foundations §5 | Stagger the two, or confirm the delivery sequencing avoids a single-day pile-up. | **Acknowledged, left live (not dismissed):** professor confirmed the staging is intentional — the research essay is due at the start of the final week; the synthesis is a take-home released that week with a submission window into the exam period — so the two do not in practice land on one day. Kept visible so the sequencing is re-checked when the course is published. |

**NOT_EVALUABLE:** none — the passport contained the data required for every check.

## Check results in full

| Check | Result | Evidence (passport ids) |
|-------|--------|-------------------------|
| A1 — every LO has non-empty `assessed_by` | pass | LO1→{A2,A5}, LO2→{A3}, LO3→{A1,A2,A4}, LO4→{A1,A3,A4,A5}, LO5→{A4} |
| A2 — every LO has non-empty `taught_in` | pass | LO1-LO5 all map to ≥1 schedule week |
| A3 — every assessment's `outcomes_assessed` non-empty, ids exist | pass | A1-A5 all reference existing LO ids |
| A4 — every week maps to ≥1 outcome or is tagged `logistics` | pass | W1-W14 carry outcomes; W15 (final submissions, no new content) tagged `logistics` |
| A5 — no outcome assessed before first taught | pass | A2 (last due W11) assesses LO1 (first taught W1), LO3 (W2); A3 (W6) assesses LO2 (W2), LO4 (W3); A4 (last due W15) assesses LO3 (W2), LO4 (W3), LO5 (W7); A5 (W15) assesses LO1 (W1), LO4 (W3); A1 (ongoing from W2) assesses LO3 (W2), LO4 (W3) |
| B1 — measurable outcome verbs | pass | explain / apply / analyze / evaluate / create |
| B2 — `bloom_level` declared for every LO | pass | LO1-LO5 |
| B3 — Bloom distribution sanity | pass | spread is understand / apply / analyze / evaluate / create — not capped at understand |
| B4 — outcome count reviewable | pass | 5 outcomes (3-8 typical) |
| C1 — weights sum to 100% | pass | 15 + 15 + 20 + 35 + 15 = 100 |
| C2 — no single assessment > 40% | pass | largest is A4 at 35% |
| C3 — low-stakes before first high-stakes | WARN | finding 1 (dismissed) — no sub-10% assessment; A2 (15%) argued to play the role |
| C4 — assessment types plausibly cover outcome levels | pass | LO5 (create) → A4 research essay (project); LO4 (evaluate) → A1 discussion + A3/A4/A5 papers; none of the evaluate/create outcomes rests only on exam/quiz |
| D1 — weekly out-of-class hours computed and recorded | pass | arithmetic below; recorded in `workload_audit` with constants |
| D2 — estimate within ±25% of credit-hour convention | WARN | finding 2 (dismissed) — 6.3 vs 5.0 = +26%, just over tolerance |
| D3 — no week with two major deliverables without sign-off | WARN | finding 3 (live) — A4 + A5 both in W15 |

## Workload arithmetic (D1/D2)

Constants follow shared/alignment_gate_protocol.md heuristics (Rice-estimator style); the
professor may adjust any constant — they are recorded in `workload_audit.constants_used` so
the calculation is re-runnable.

| Component | Calculation | Hrs/week |
|-----------|-------------|----------|
| Seminar reading | ~70 pp/wk × ~400 words/page ÷ 130 wpm (read-to-discuss, annotating) | 3.6 |
| Reading responses (A2) | 6 responses × ~2.5 h ÷ 15 wk | 1.0 |
| Primary-source paper (A3) | ~9 h total ÷ 15 wk | 0.6 |
| Research essay (A4) | ~16 h total (proposal + draft + final + revision memos) ÷ 15 wk | 1.1 |
| **Total** | | **6.3** |

Target: 2 out-of-class hours × 2.5 contact hours = **5.0 hrs/week**. Estimate 6.3 is
**+26%, just outside the ±25% tolerance** → check D2 fires WARN (dismissed). The take-home
synthesis essay (A5) is treated as a redistribution of regular end-of-term study time, not
an addition — a recorded modeling choice, not a fact; adjust if your students' end-of-term
behavior differs. The overage is driven almost entirely by reading load: this is a
reading-intensive seminar and the professor has accepted that as core to the design.

## Notes

- Previously dismissed findings: none on file before this run (first gate run for this
  design); C3 and D2 above were dismissed at this run's checkpoint and will be skipped in
  future runs per protocol. D3 was acknowledged but left live, so it *will* re-surface until
  the publication-stage sequencing is confirmed.
- This gate checks structure, not merit: topic choices, reading selections, and week
  ordering were not evaluated and are not this agent's findings to make.
- No student data was read or required by this gate. The person-affecting artifacts in this
  showcase are standalone and outside the passport.

---
*Checkpoint record: professor acknowledged verdict, dismissed findings C3 and D2 with the
reasons logged above, and confirmed D3 as an intentional sequencing item to re-check at
publication. Gate status `pass`, `last_run: 2026-06-15`.*
