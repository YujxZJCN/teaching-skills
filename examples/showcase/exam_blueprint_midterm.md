# Test Blueprint: Midterm Exam — CS 304

**Course:** CS 304 Introduction to Machine Learning · **Assessment ID:** A3
**Type:** exam (in-class) · **Weight:** 25% · **Scheduled:** W8
**Duration:** 90 min · **Conditions:** closed-book; formula sheet provided with the exam paper; non-programmable calculator permitted; no devices
**Blueprint status:** confirmed_by_professor 2026-06-10

## Outcomes covered

| LO id | Outcome statement | Bloom level | Points on this instrument |
|-------|-------------------|-------------|---------------------------|
| LO1 | Explain the assumptions, inductive biases, and characteristic failure modes of core supervised and unsupervised learning algorithms | understand | 22 |
| LO2 | Implement linear models, tree ensembles, and neural networks from their mathematical specifications using NumPy and scikit-learn/PyTorch | apply | 28 |
| LO3 | Apply correct experimental methodology — train/validation/test splits, cross-validation, and hyperparameter search — to fit and tune models on real datasets | apply | 28 |
| LO4 | Diagnose model failures by analyzing learning curves, bias-variance behavior, and error patterns, and select justified corrective actions | analyze | 22 |

All four outcomes listed in `assessment_plan.A3.outcomes_assessed` carry nonzero
points — no coverage flags. (LO2 mapping note under "Level-honesty flags".)

## Content × Bloom matrix

Cells: `item count × format = points`. Empty cells are intentional, not oversights.
Rows are lettered A-G, columns numbered 1-3; items reference cells as `F2`, `E3`, etc.

| Content area (taught in) | 1 · Understand | 2 · Apply | 3 · Analyze | Points | % |
|--------------------------|----------------|-----------|-------------|--------|---|
| A. Foundations & k-NN (W1) | 2 × MC = 4 | 1 × MC = 2 | — | 6 | 6% |
| B. ML workflow & data discipline (W2) | 2 × MC = 4 | 1 × SA = 6 | — | 10 | 10% |
| C. Linear regression (W3) | 1 × MC = 2 | 1 × MC = 2 · 1 × problem = 14 | — | 18 | 18% |
| D. Linear classification & metrics (W4) | 2 × MC = 4 | 1 × SA = 6 | — | 10 | 10% |
| E. Evaluation methodology (W5) | 1 × MC = 2 | 2 × MC = 4 · 1 × SA = 6 | 1 × data-interp = 8 | 20 | 20% |
| F. Overfitting & regularization (W6) | 2 × MC = 4 | 1 × problem = 14 | 1 × data-interp = 8 | 26 | 26% |
| G. Model selection & hyperparameter search (W7) | 1 × MC = 2 | 1 × MC = 2 | 1 × SA = 6 | 10 | 10% |
| **Totals** | **22** | **56** | **22** | **100** | 100% |

Item inventory: 16 MC × 2 = 32 · 4 short answer × 6 = 24 · 2 data-interpretation × 8 = 16 · 2 multi-step problems × 14 = 28. **24 items, 100 points.**

**Emphasis check:** uniform instructional time would put each of the 7 content
areas near 14%. Deliberate deviations: row F at 26% and row E at 20% concentrate
points on the course's documented difficulty cluster (training-vs-test-error
confusion; `learner_profile.known_difficulties`) — flagged to the professor and
confirmed. Row A at 6% under-weights W1 because its concepts are re-exercised
inside later scenario stems rather than tested in isolation.
**Level-honesty flags:** one note, not a flag — LO2's *coding* facet (NumPy/
PyTorch) is evidenced by A2 labs; this closed-book instrument measures LO2's
mathematical-specification facet only (hand-worked problems C2, F2). Recorded so
nobody reads the 28 points as evidence of coding skill.

## Time budget

Heuristics (adjustable — challenge the constants, not just the total): MC ~1-1.5 min ·
short answer ~3-5 min · problem ~8-15 min · essay ~20-30 min.

| Item type | Count | Est. minutes each | Subtotal |
|-----------|-------|-------------------|----------|
| Multiple choice | 16 | 1.5 | 24 |
| Short answer | 4 | 4 | 16 |
| Data interpretation | 2 | 6 | 12 |
| Multi-step problem | 2 | 13 | 26 |
| **Total** | | | **78 / 90 min** |

Target ≤90% of duration (81 min). Status: **within budget** — 78 min planned, 12 min
real slack for checking work.

## Versions & accommodations

- **Parallel forms:** 2 shuffled versions (Form A / Form B) per
  references/item_writing_rules.md bank discipline: option order and surface
  numbers vary within the same difficulty band; construct, solution-path
  structure, and the misconceptions encoded by distractors do not. Each item
  carries a family id; each form gets its own independently worked key.
- **Extra-time variant (Quality Gate U3):** same instrument at 1.5× clock
  (135 min) — trivially derivable, no reduced-length form needed; seating and
  invigilation logistics arranged per students' accommodation letters.
- **Other anticipated accommodations:** none recorded —
  `learner_profile.accessibility_needs: unknown`; handled per accommodation
  letters as they arrive.

## Integrity tier

**Declared tier:** P — in-class, closed-book, supervised; the midterm measures
unaided fluency (rationale recorded in assessment_plan and the syllabus AI table).
**Audit status:** `ai_resilience: reviewed` — set by integrity_auditor_agent
2026-06-10 (see integrity_audit.md): vulnerability low, tier coherent.
