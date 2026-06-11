# Diagnose These Four Learning Curves

CS 304 · W6 · Lecture 6 (segment S5)

## Why we're doing this

Reading a learning curve is how ML practitioners decide what to do next — collect
more data, regularize, or change the model — without burning a week guessing. This
exercise practices exactly that diagnosis (outcome LO4), on the four patterns you
will meet most often in your labs and course project.

## Your task

Each scenario below describes a plot of **training error** and **validation error**
as the training set grows. For each one, decide with your partner:
(a) a one-word diagnosis, and (b) the single action you would take next.

1. **Curve A:** training error stays very low and flat; validation error is much
   higher and stays high — a wide, persistent gap between the two.
2. **Curve B:** training and validation error are both high, close together, and
   flat — adding the last 2,000 examples barely moved either one.
3. **Curve C:** both errors are still falling steadily, and the validation curve
   is clearly still sloping downward at the right edge of the plot.
4. **Curve D:** validation error is consistently *below* training error across
   the whole plot.

"Done" looks like: a diagnosis word and a next action written on the sheet for
all four curves.

## Logistics

- **Groups:** pairs — turn to your neighbor (fixed seating; threes are fine at row ends)
- **Time:** 8 minutes (1 think solo · 3 pair · 4 vote-and-share)
- **You'll need:** this sheet, a pen, your vote cards — no devices

## What you'll hand in / report

Nothing is collected. For each curve you'll vote your diagnosis by card, and a
few pairs will be asked to share their reasoning — be ready to say *which feature
of the curve* (the gap, or the level, or the slope) drove your call.

## Debrief

The two questions we'll close on:

1. For each curve: does the *gap* between the curves or the *level* of the curves
   carry the diagnosis?
2. Which of these four situations does "collect more data" actually fix — and
   which does it just make slower?

---
---

# Instructor side — Diagnose These Four Learning Curves

*(not distributed; lives with the lesson plan, segment S5)*

**Technique:** think-pair-share, pairs-only adaptation for a fixed-seat 90-person hall
**Outcome served:** LO4 · **Bloom level rehearsed:** analyze

## Launch script

> "Sheet in front of you — four learning curves, described in words. One minute
> alone: write a one-word diagnosis for each. Then three minutes with your
> neighbor: agree on the diagnosis *and* the one action you'd take next. We vote
> by card at minute four. Go."

## Timing checkpoints

| At min | Do |
|--------|----|
| 0:30 | Launch done; sweep front rows for sheet-side-up compliance |
| 1:00 | Call the switch to pairs; start circulating toward the back rows |
| 3:00 | One-minute warning; pick 2-3 pairs with *different* curve-D answers to call on |
| 4:00 | Hard stop; card votes curve by curve (A, then B, C, D) |
| 8:00 | Hand off to debrief segment S6 |

## Failure modes

| If… | Then… |
|-----|-------|
| Silence at pair phase | Seed it: run the whole-class card vote on curve A *first*, then send them to pairs for B-D — a public split gets pairs arguing |
| Pairs finish fast | Extension on the board: "Sketch what curve A becomes after strong L2 regularization. What about after 10× more data?" |
| Pairs stall on curve D | Prompt: "Which of the two numbers is the model's promise to the outside world? Should the promise ever beat the rehearsal?" |
| Off-task drift in back rows | Circulate there by minute 1 (timing checkpoint); proximity fixes most of it |

## Debrief answers / expected range

- **Curve A — overfitting / high variance.** Gap carries the diagnosis. Good next
  actions: regularize, simplify the model, or get more data. All three accepted;
  ask *why* each attacks the gap.
- **Curve B — underfitting / high bias.** Level carries it. Next action: richer
  model / better features. The common wrong vote is "more data" — both curves have
  already converged; more data makes the same disappointment cheaper. Surface this
  vote explicitly; it is the debrief's most teachable moment.
- **Curve C — not yet data-saturated.** Slope carries it. "More data" is the one
  scenario where it is the clearly right first move.
- **Curve D — something is wrong with the evaluation.** Validation persistently
  beating training is a smell: usual suspects are data leakage into the validation
  set, an evaluation bug, or train-only regularization/augmentation (e.g. dropout
  active only at training). Accept "small-sample noise" as a partial answer; push
  to "check before celebrating."
- **Board synthesis:** 2×2 — *gap* high vs low against *level* high vs low; place
  A, B, C in cells, D outside the table as "audit the pipeline first."
- **Bridge to S7:** "Regularization is the knob that trades curve-A behavior
  toward curve-B behavior on purpose — let's see how it does that."

## Notes

**Assumptions made:** colored vote cards available at room entry; fixed seating
(pairs-only, no regrouping); board visible from back rows for the 2×2 synthesis.
**Alternative route:** votes are anonymous-by-distance and never graded; students
who prefer not to speak when called may pass — reasoning can go on the W6 exit
ticket instead. (Participation is not graded in CS 304; route exists per Quality
Gate U2 anyway.)
**[VERIFY] items in this sheet:** none.
