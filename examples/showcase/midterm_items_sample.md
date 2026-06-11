# Midterm Items — Sample (5 of 24) — CS 304, Assessment A3

**Produced by:** item_writer_agent (assessment-architect `exam`, Phase 2 ITEMS);
key excerpt by answer_key_agent (Phase 3 KEY, worked independently).
**Status:** professor-confirmed 2026-06-10.

Every item is written *into a blueprint cell* — the cell tags below (B2, E2, E3,
F1, F2) reference the Content × Bloom matrix in exam_blueprint_midterm.md (rows
A-G × columns 1-3). An item without a cell has no reason to exist; a cell without
items is a coverage gap. In a real run the full 24-item instrument and complete
key live in `assessments/A3_midterm.md` and `assessments/A3_key.md`; this sample
shows one item per format. Instructor-side notes (misconception annotations, key
elements) are never distributed with the exam paper.

---

## Item 1 — multiple choice · LO1 · understand · cell F1 · 2 pts

A classifier reaches 99% accuracy on the data it was trained on and 71% on a
held-out test set. Which statement best describes the situation?

- **A.** The model has overfit: the train-test gap indicates it learned patterns specific to the training data.
- **B.** The model's true accuracy is 99%: training accuracy uses the most data, so it is the more reliable number.
- **C.** The 28-point gap mainly reflects test-set noise: a same-size sample of similar data is expected to score this differently.
- **D.** The model has underfit: training longer on the same data will close the gap.

> **Instructor note — key A; distractor map (rule 5, each distractor = a logged misconception):**
> - **B** — *training error read as model quality* (the train-vs-test confusion;
>   `learner_profile.known_difficulties` #1 — this is the distractor this item exists for)
> - **C** — *generalization gap dismissed as sampling noise* (no sense of gap magnitude)
> - **D** — *gap attributed to insufficient training*, so more epochs "fix" it
>   (confuses underfitting's remedy with overfitting's symptom)
> Options parallel in form and length (rule 4); no AOTA/NOTA (rule 6); no absolutes (rule 7).

## Item 2 — multiple choice · LO3 · apply · cell E2 · 2 pts

You choose k for a k-NN classifier by picking the k with the lowest error on the
test set, then report that same test-set error as the model's expected
performance on new data. What is the flaw in this procedure?

- **A.** There is no flaw, provided the test set was held out during the initial training runs.
- **B.** The reported error is optimistically biased: the test set was used for model selection, so it no longer estimates generalization.
- **C.** The reported error is pessimistically biased: k should have been tuned on the training set to reach its best value.
- **D.** A test set is unnecessary for k-NN, since the algorithm has no training phase to overfit with.

> **Instructor note — key B; distractor map:**
> - **A** — *"held out once = valid forever"*: misses that selection on a set
>   spends that set
> - **C** — *direction-of-bias confusion*: knows something is biased, guesses the
>   wrong sign
> - **D** — *lazy learner exempt from evaluation discipline*: the API-calling
>   habit (`known_difficulties` #2) — no training loop, so no methodology needed
> Stem is a complete question before options (rule 2); the flaw-finding framing is
> the higher-order error-finding pattern, not trick wording (rule 8).

## Item 3 — data interpretation · LO4 · analyze · cell E3 · 8 pts

A team compares three polynomial regression models using 5-fold cross-validation:

| Model | Training MSE | 5-fold CV MSE |
|-------|--------------|---------------|
| M1 (degree 1) | 18.2 | 18.9 |
| M2 (degree 5) | 6.1 | 7.0 |
| M3 (degree 12) | 0.8 | 14.5 |

**(a)** Which model should the team select, and on which number do you base that? (2 pts)
**(b)** Name M3's failure mode and cite the two values from the table that evidence it. (3 pts)
**(c)** The team proposes collecting 10× more training data to improve M1. Is this a
well-targeted fix for what the table shows about M1? Answer yes/no and justify
from the table. (3 pts)

> **Instructor note:** key elements — (a) M2, lowest *CV* MSE (selecting on
> training MSE = 0 pts even if M2 named); (b) overfitting, evidenced by 0.8 train
> vs 14.5 CV; (c) no — M1's train and CV errors are high *and close* (18.2 / 18.9),
> a bias pattern; more data narrows gaps, it does not lower a converged level.
> Construct mirrors the W6 learning-curve activity (taught material, rule 10) with
> fresh surface data.

## Item 4 — short answer · LO3 · apply · cell B2 · 6 pts

A teammate standardizes the full dataset — using the mean and standard deviation
computed over *all* rows — and then splits it into training and test sets. In 2-3
sentences, explain what is wrong with this order of operations and how to fix it.

*Graded on three things: naming the problem (data leakage), the mechanism (test
rows influence the preprocessing that the model is built on), and the corrected
order of operations.*

> **Instructor note — key elements (a short-answer item without an element list is
> ungradeable consistently):** (1) "data leakage" or equivalent — test information
> enters training, 2 pts; (2) mechanism — the scaler's mean/sd are computed from
> data that includes test rows, so the evaluation is optimistically biased, 2 pts;
> (3) fix — split first, fit the scaler on training data only, apply it to both,
> 2 pts. Acceptable phrasings: "test set contaminates preprocessing", "statistics
> computed on test data", "fit transform on train, apply to test". Expected length
> stated in the stem (rule: specify length and form).

## Item 5 — multi-step problem · LO2 · apply · cell F2 · 14 pts

Regularized linear regression with model ŷ = w₁x + w₀, squared loss
L(w) = (1/n) Σᵢ (ŷᵢ − yᵢ)² + λw₁², and **λ = 0** for parts 1-4.

Training data: (x, y) = (0, 1), (1, 3), (2, 5). Initial weights w₀ = 0, w₁ = 1.
Learning rate η = 0.1. Show your work for every part; exact fractions or decimals
to 3 places both accepted.

1. Compute the model's predictions on the three training points. (2 pts)
2. Compute the loss L(w). (3 pts)
3. Compute the gradient (∂L/∂w₀, ∂L/∂w₁). (4 pts)
4. Perform one gradient-descent update and give the new (w₀, w₁). (3 pts)
5. Suppose now λ > 0. State how the update to w₁ in part 4 changes, and why this
   pushes the model toward the simpler end of the bias-variance trade. No
   computation required. (2 pts)

*Grading notes: per-step points as marked; carry-forward policy — a wrong value
from an earlier part, used correctly later, loses points only once (method marks
in full). Calculator permitted; formula sheet includes the gradient of squared loss.*

---

## Worked key excerpt — Item 5 (answer_key_agent, solved independently of the item author's notes)

| Step | Worked solution | Pts |
|------|-----------------|-----|
| 1 | ŷ = w₁x + w₀ = x → predictions (0, 1, 2) for x = (0, 1, 2) | 2 |
| 2 | residuals ŷ − y = (−1, −2, −3); L = (1 + 4 + 9)/3 + 0 = **14/3 ≈ 4.667** | 3 |
| 3 | ∂L/∂w₀ = (2/3)Σ(ŷᵢ−yᵢ) = (2/3)(−6) = **−4**; ∂L/∂w₁ = (2/3)Σ(ŷᵢ−yᵢ)xᵢ = (2/3)(0 − 2 − 6) = **−16/3 ≈ −5.333** (λ = 0 ⇒ no penalty term) | 4 |
| 4 | w₀ ← 0 − 0.1(−4) = **0.4**; w₁ ← 1 − 0.1(−16/3) = 1 + 8/15 = **23/15 ≈ 1.533** | 3 |
| 5 | With λ > 0 the w₁ gradient gains +2λw₁ (penalty does not touch the bias w₀ by convention), so each update shrinks w₁ toward 0 relative to the unregularized step — smaller weights, smoother function, less variance at the cost of some bias | 2 |

**Carry-forward:** wrong residuals in step 2, applied correctly in steps 3-4,
lose only step 2's points.

> **Discrepancy flag (key-independence in action):** the key author's worked
> answer differed from the item author's intended answer at **step 3** — the
> intended key assumed the unregularized gradient, while the independently worked
> key included the +2λw₁ term, because the original stem declared the ridge
> objective but never fixed λ. Per skill iron rule 3 both solutions went to the
> checkpoint unresolved — the discrepancy is the finding; silently picking one
> hides a broken item or a broken key. **Professor resolved 2026-06-10:** the
> stem now specifies **λ = 0 for parts 1-4**, and the λ > 0 behavior moved into
> part 5 as its own scored construct. Both keys re-worked against the revised
> stem and now agree.
