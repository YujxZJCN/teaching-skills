# CS 304: Introduction to Machine Learning

**Term:** EXAMPLE TERM (demonstration artifact — this course is not a real offering) · **Credits:** 3 · **Modality:** in-person
**Meetings:** one 90-min lecture + one 90-min lab session per week (room assignments are placeholders in this demonstration)
**Instructor:** Prof. EXAMPLE · cs304-instructor@example.edu · Office hours: two weekly hours, posted on the course site (example values — replace at adoption)
**TA(s):** two TAs (example values); contact and lab-section duties posted on the course site
**Prerequisites:** CS 201 Data Structures, MATH 210 Linear Algebra, STAT 110 Probability

## What this course is about

Machine learning is how modern software learns regularities from data instead of
being told them. This course teaches you to build and — just as importantly — to
*distrust* learned models: you will implement core algorithms from their math,
run honest experiments that separate what a model memorized from what it learned,
and carry one project from raw data to a defensible written result. By the end,
"the model gets 99% on our data" should sound to you like the beginning of an
investigation, not the end of one.

The course assumes you can program well. It does not assume your linear algebra
and probability are fresh — week 1's lab is a refresher, and the math we need is
re-introduced where we use it.

## Learning outcomes

By the end of this course, you will be able to:

1. **(LO1)** Explain the assumptions, inductive biases, and characteristic failure modes of core supervised and unsupervised learning algorithms
2. **(LO2)** Implement linear models, tree ensembles, and neural networks from their mathematical specifications using NumPy and scikit-learn/PyTorch
3. **(LO3)** Apply correct experimental methodology — train/validation/test splits, cross-validation, and hyperparameter search — to fit and tune models on real datasets
4. **(LO4)** Diagnose model failures by analyzing learning curves, bias-variance behavior, and error patterns, and select justified corrective actions
5. **(LO5)** Evaluate the suitability and limits of a trained model for a stated task, including metric choice, data-leakage risks, and ethical considerations
6. **(LO6)** Design and carry out an end-to-end machine learning project, from problem formulation through data preparation, modeling, evaluation, and written report

## Materials

- **Required:** James, Witten, Hastie, Tibshirani — *An Introduction to Statistical
  Learning with Applications in Python*. A free PDF is distributed by the authors
  online; no purchase is needed.
- **Optional:** Bishop — *Pattern Recognition and Machine Learning*, for students
  who want the deeper mathematical treatment.
- **Software:** Python 3 with NumPy, scikit-learn, and PyTorch (all free; lab 0
  setup instructions in week 1's lab).

## How this course works

Lectures alternate short input segments with active work — peer-instruction votes
and pair exercises — because passively watching someone else reason about
overfitting does not build the skill of diagnosing it yourself. Votes are never
graded for correctness; they exist so you (and I) can see misconceptions while
they are still cheap. Lab sessions are where quizzes run, where lab assignments
get unstuck, and where the project clinics happen. Out of class, expect roughly
six hours per week: reading, four lab assignments, and a staged project whose
milestones are spread across the term precisely so the work cannot pile up at
the end.

## Assessment

| Assessment | When | Weight | Outcomes evidenced |
|------------|------|--------|--------------------|
| A1 — Weekly quizzes (best 8 of 10) | lab start, weeks 2-13 (none in W8, W10) | 10% | LO1, LO3 |
| A2 — Lab assignments (4) | due W5, W7, W11, W13 | 20% | LO2, LO3, LO4 |
| A3 — Midterm exam (in-class, closed-book) | W8 | 25% | LO1, LO2, LO3, LO4 |
| A4 — Course project (M1 proposal 4% · M2 progress 8% · M3 final report 18%) | W6 / W10 / W14 | 30% | LO4, LO5, LO6 |
| A5 — Project defense (sampled 5-min oral check) | W15 | required gate, 0% | LO5, LO6 |
| A6 — Final exam (cumulative, emphasis W9-W14) | W16 | 15% | LO1, LO2, LO5 |

Project teams of 3; each milestone after M1 includes a short note on what you
changed in response to the previous milestone's feedback. In week 15, a sample
of teams (about 12 of 30, drawn openly) briefly walk through their project; this
is announced policy for everyone, not a suspicion directed at anyone — being
able to explain your own work is part of the outcome being graded.

**Grading scale:** weighted sum above; no curve. A ≥ 90, B 80-89, C 70-79, D 60-69, F < 60.
**Late work:** labs and milestones — 3 free late days pooled across the term (max 2 on one artifact), then -10% per day up to 3 days. Quizzes: no make-ups; best-8-of-10 absorbs absences. Exams: make-ups only for documented emergencies.
**Regrades:** written request within 7 days of grade release; the whole item is re-marked.
**Feedback:** quizzes — next lab session; labs — within 10 days; project milestones — within 7 days, because the feedback feeds your next milestone.

## AI use in this course

Different assignments have different rules, each chosen for a reason:

| Assignments | Policy | Why |
|-------------|--------|-----|
| Quizzes, midterm, final (A1, A3, A6) | **Tier P — no generative AI** | These measure your own unaided fluency with the concepts; that fluency is what the rest of your ML work stands on. |
| Lab assignments (A2) | **Tier D — permitted with disclosure** | Professionals use these tools when building ML code; learning to use them with judgment — and showing your judgment in the disclosure — is part of the skill. |
| Course project (A4) | **Tier D — permitted with disclosure** | Same reason as labs; the milestones, feedback-response notes, and defense make your own understanding visible regardless of the tools you used. |
| Project defense (A5) | **Tier P — no generative AI** | A live conversation about your own work, by design unaided. |

When AI use is permitted with disclosure, append to your submission: which tool,
what you asked it, and what you changed. Disclosure is never penalized;
non-disclosure where required is an integrity matter.

## Course policies

**Academic integrity:** [NEEDS PROFESSOR INPUT: institutional academic integrity policy link — faculty handbook §academic-conduct]
**Attendance & participation:** attendance is not directly graded; lab sessions are where quizzes run and clinics happen. Peer-instruction votes are never graded for correctness, and nothing in class requires speaking publicly to earn credit.
**Accommodations:** [NEEDS PROFESSOR INPUT: institutional disability-services statement and contact]
**Support & wellbeing:** if circumstances start affecting your work, talk to the instructor early — adjustments are far easier to arrange before a deadline than after.
**Questions & communication:** course questions go to the course forum (answered within 2 working days); personal matters go to the instructor's email above.

## Schedule

| Week | Topic | Due |
|------|-------|-----|
| W1 | The learning problem; types of learning; k-NN as a first model (lab: NumPy & linear algebra refresher) | — |
| W2 | The ML workflow: data, features, train/test discipline; a first end-to-end pipeline | Quiz 1 |
| W3 | Linear regression: least squares, gradient descent | Quiz 2 |
| W4 | Linear classification: logistic regression, decision boundaries, classification metrics | Quiz 3 |
| W5 | Evaluation methodology: train/validation/test splits, cross-validation, metric choice, learning curves (lab: project launch — problem-formulation workshop) | Quiz 4 · Lab 1 |
| W6 | Overfitting, generalization, and regularization | Quiz 5 · Project M1 (proposal) |
| W7 | Model selection and hyperparameter search; the end-to-end project workflow (lab: project pipeline workshop) | Quiz 6 · Lab 2 |
| W8 | **Midterm exam** (covers W1-W7); lab: post-midterm error-analysis clinic | Midterm (A3) |
| W9 | Decision trees and random forests | Quiz 7 |
| W10 | Boosting and ensemble practice (lab: project progress clinic) | Project M2 (progress) |
| W11 | Neural networks I: from perceptron to MLP; backpropagation | Quiz 8 · Lab 3 |
| W12 | Neural networks II: training practice, debugging deep models | Quiz 9 |
| W13 | Unsupervised learning: k-means clustering, PCA | Quiz 10 · Lab 4 |
| W14 | ML in the wild: data leakage, metric pitfalls, fairness and ethics | Project M3 (final report) |
| W15 | Course synthesis and review; sampled project defenses | Defense (A5, sampled) |
| W16 | **Final exam** | Final (A6) |

*Schedule may adjust with notice; assessment dates change only with announced lead time.*
