# Lesson Plan — W6: Overfitting, generalization, and regularization

**Course:** CS 304 Introduction to Machine Learning · **Meeting:** Lecture 6 (the W6 90-min lecture)
**Length:** 90 min · **Modality:** in-person · **Class size:** 90
**Room/platform notes:** fixed-seat lecture hall, projector + whiteboard. No clicker
system assumed — peer-instruction votes use colored cards (assumption: card sets
available at room entry; fallback is hands).

## Outcomes served

- **LO1** — Explain the assumptions, inductive biases, and characteristic failure modes of core supervised and unsupervised learning algorithms
- **LO4** — Diagnose model failures by analyzing learning curves, bias-variance behavior, and error patterns, and select justified corrective actions

**Due this meeting:** — (this week: Quiz 5 at lab start; A4 Milestone 1 — project proposal — due in the lab session)

## Materials & prep

| Item | Who prepares | Status |
|------|--------------|--------|
| Slides outline (segments S2, S4, S7) | instructor | ready |
| Activity sheets, ~50 copies (1 per pair + spares) — activity_W06_bias_variance.md | TA print run | ready |
| Colored vote cards (A/B/C/D) at room entry | TA | ready |
| Degree-sweep figures + error table (regenerate from W6 demo notebook, seed 42) | instructor | **open — see [VERIFY] below** |
| Exit-ticket slips + collection boxes at both doors | TA | ready |
| Board markers (2 colors for train vs test curves) | instructor | ready |

## Segment plan

| Time | Seg | Mode | What the instructor does | What students do | Materials |
|------|-----|------|--------------------------|------------------|-----------|
| 00–08 | S1 | activation | Retrieval starter on W5: poses 3 questions (below), one at a time; cold reveal after each show of cards | Answer from memory, vote, compare with neighbor | slide, cards |
| 08–28 | S2 | input | What overfitting is: training vs test error as two different promises; fitting noise vs fitting signal; sets up polynomial regression on 50 points | Listen, sketch the two curves in notes | slides, board |
| 28–36 | S3 | active | Peer-instruction concept question (below): vote → pair discussion → revote → reveal with misconception debrief | Vote, argue with neighbor, revote | slide, cards |
| 36–52 | S4 | input | Worked example: polynomial degree sweep d = 1…15 on the same data; walks the error table (below); draws the U-curve of test error; names the regimes | Follow the table, predict the next row before it is revealed | slides, board |
| 52–60 | S5 | active | Launches "diagnose these four learning curves" (activity_W06_bias_variance.md, launch script on the instructor side) | Think-pair-share: diagnose curves A–D, vote per curve | activity sheet, cards |
| 60–68 | S6 | check | Debrief of the activity: collects votes per curve, calls 2-3 pairs for reasoning, synthesizes the gap-vs-level table on the board | Report diagnoses, correct their sheets | board |
| 68–82 | S7 | input | Regularization as the deliberate trade: ridge intuition, what the penalty does to weights, λ as a knob between curve A and curve B behavior; one slide on how this connects to the project's model choices | Listen; one-minute paired prediction: "what does λ → ∞ do?" | slides |
| 82–87 | S8 | closure | Exit ticket (below); reminds: proposal M1 due in lab, Quiz 5 at lab start | Write and drop slips in boxes | slips |

(Total planned: 87 min of 90 — 3 min slack per template rule. Input blocks are 20,
16, and 14 min — none exceeds the 20-25 min attention ceiling before an active turn.)

### S1 retrieval starter (from W5)

1. Why do we hold out a test set instead of just evaluating on the training data?
2. A teammate tunes hyperparameters by test-set accuracy, then reports that same number as the model's expected accuracy. What went wrong?
3. We standardize features using the mean and standard deviation of the *full* dataset, then split into train and test. What leaked?

### S3 peer-instruction concept question

> We fit three polynomial models to the same 50 training points:
>
> | Model | Training MSE | Test MSE |
> |-------|--------------|----------|
> | d = 1 | 4.1 | 4.3 |
> | d = 4 | 1.2 | 1.4 |
> | d = 14 | 0.05 | 7.9 |
>
> Which model should we deploy, and which number tells you?

- **A.** d = 14 — it has the lowest training error, so it learned the data best. *(misconception: training error read as model quality — the course's #1 known difficulty)*
- **B.** d = 1 — the simplest model generalizes best, regardless of the numbers. *(misconception: simplicity absolutism; Occam without looking at the evidence)*
- **C.** d = 4 — it has the lowest test error, which estimates performance on new data. **(correct)**
- **D.** We can't decide yet — we should retrain all three on the test set first. *(misconception: test set treated as more training data; destroys the estimate)*

Expected first-vote split: sizable A camp (this is the known difficulty). If first
vote is >70% correct, skip pair phase and harvest one A-voter's reasoning instead.

### S4 worked example — polynomial degree sweep

Same 50-point dataset throughout (W6 demo notebook, seed 42). Reveal row by row;
before each reveal, students predict whether test MSE goes up or down.

| d | Training MSE | Test MSE |
|---|--------------|----------|
| 1 | 4.1 | 4.3 |
| 4 | 1.2 | 1.4 |
| 9 | 0.4 | 2.6 |
| 14 | 0.05 | 7.9 [VERIFY: regenerate from the W6 demo notebook before class — this value came from last year's dataset draw and changes with the seed] |

Talking points: training MSE falls monotonically with d (why it *must*); test MSE
is U-shaped; the d = 14 model passes near every training point and pays for it
between them. Name the regimes underfit / sweet spot / overfit on the board.

## Closure & check

**Closure activity:** exit ticket (paper slips, boxes at both doors) — two prompts:
(1) "Your model: training error 2%, test error 25%. Name one fix and one sentence
on why it should help." (2) "Muddiest point of today, one phrase."
**What I'm checking for:** (a) students separate the roles of training vs test
error when justifying the fix; (b) fixes are matched to the *overfitting* regime
(regularize, simplify, more data) rather than generic ("train longer").
**Forward link:** "Next week: how to choose λ and other hyperparameters *without*
touching the test set — which your project will have to do for real."

## Contingency

**If running long, cut:** S7 compresses to 8 min — ridge intuition and the λ-knob
picture survive; the weight-shrinkage algebra moves to W7's opening. Never cut S8.
**If running short, extend:** prepared second PI question after S4: "Same sweep,
but with 5,000 training points instead of 50 — which rows of the table change, and
in which direction?"
**If the S5 activity stalls:** failure-mode fixes on the instructor side of
activity_W06_bias_variance.md (seed with a whole-class vote on curve A; extension
question for fast finishers).

## [VERIFY] items outstanding

1. S4 table, d = 14 test MSE "7.9" — regenerate from the W6 demo notebook (seed 42)
   before class; the value is seed-dependent and was carried over from last year's
   draw. (The S3 concept question reuses the same three rows — update both together.)

## Post-class notes

*(fill in after teaching — feeds iteration_history and next year's redesign)*

**What the closure check showed:** { }
**Timing reality vs plan:** { }
**Keep / change next time:** { }
