# Quickstart

## 1. Install

```text
/plugin marketplace add YujxZJCN/teaching-skills
/plugin install teaching-skills
```

or clone + symlink the skill directories into `~/.claude/skills/`.

## 2. Your first session — a new course in ~30 minutes of your attention

Say:

```
I'm teaching "Introduction to Machine Learning" next semester.
Undergraduate, 3rd year, about 90 students, 16 weeks, 3 hours/week, in person.
Run the full pipeline.
```

What happens, and where your attention goes:

1. **Stage 0 — Context.** A few questions you can answer in one message (who are these
   students, what do they struggle with, fixed constraints). This creates
   `course_passport.yaml`. Don't skip the learner-profile questions — every later
   artifact is calibrated against them.
2. **Stage 1 — Design.** You'll see 3–8 draft learning outcomes **with an alternative
   set** when the design genuinely forks. This is the highest-leverage checkpoint in
   the whole pipeline — spend your attention here. Then assessment plan (types,
   weights, AI-policy tiers), then the week-by-week arc, then the syllabus with
   `[NEEDS PROFESSOR INPUT]` markers for your institution's policies.
3. **Gate 1.5.** A deterministic alignment audit. BLOCK findings loop back; warnings
   you can dismiss with a reason (logged, never re-raised).
4. **Stages 2–3.** Choose build-ahead depth ("build weeks 1–3 now, rest just-in-time").
   Exams start from a test blueprint you confirm **before** any item is written.
5. **Gate 3.5.** Integrity, transparency, accessibility, workload — then you're ready
   for week 1.

During the semester: `"week 5 — what's due?"`, `"draft feedback for these lab reports"`,
`"a student stopped submitting — help me reach out"`. At week 4–6 the pipeline offers a
mid-course feedback survey while there's still time to act on it.

After finals: `"here are my evals"` → thematic, bias-caveated analysis → iteration
record → next term, `new-term` mode re-enters design with the evidence attached.

## 3. Don't want the pipeline?

Every skill works standalone:

| You say | You get |
|---------|---------|
| `/ts-outcomes` "…for a graduate seminar on X" | Bloom-tagged outcome set |
| `/ts-syllabus` | Syllabus (asks for what it needs) |
| `/ts-lesson` "week on dynamic programming, 80 min" | Lesson plan + notes + slides outline + activity |
| `/ts-exam` | Blueprint → checkpoint → items → verified key |
| `/ts-rubric` "for this project brief" | Rubric + TA calibration notes |
| `/ts-integrity` "audit my take-home final" | AI-resilience audit with redesign options |
| `/ts-feedback` + the work + your judgment notes | Structured, evidence-bound comments |
| `/ts-letter` | Intake interview, then the letter |
| `/ts-evals` + raw comments | Thematic analysis with honest caveats |
| `/ts-statement` | Socratic elicitation, then a draft in your voice |

## 4. Three habits that make it work

- **Answer the intake questions once, well.** The passport remembers; you won't be
  asked twice.
- **Push back at checkpoints.** The agents hold their flags under pushback only when
  the evidence warrants; your discipline and institutional context win, and the
  resolution is logged either way.
- **Bring evidence, not vibes, to redesign.** The Stage 5/6 loop exists so that next
  term's changes trace to this term's data.
