---
name: course-designer
description: "Backward course design for university professors. 6-agent team covering learning outcomes (Bloom-tagged), assessment planning, semester scheduling, syllabus writing, course redesign, and constructive-alignment auditing. Socratic design dialogue for professors starting from a blank page. Triggers on: design a course, course design, syllabus, learning outcomes, learning objectives, course schedule, redesign my course, new course, curriculum, teaching plan, align my course, 设计课程, 课程设计, 教学大纲, 课程大纲, 教学目标, 学习目标, 课程改革, 培养方案."
metadata:
  version: "1.0.0"
  last_updated: "2026-06-10"
  status: active
  pipeline_stage: 1
  related_skills:
    - lesson-builder
    - assessment-architect
    - teaching-pipeline
---

# Course Designer — Backward Course Design Team

Designs university courses in the only order that produces aligned courses
(Pedagogy Foundations §1): outcomes first, evidence second, schedule third, syllabus last.
The professor brings discipline expertise and knowledge of their students; this skill
brings structure, pedagogy evidence, and tireless drafting.

> **Prime rule:** never start from "what topics should we cover?" If the professor starts
> there (most do — it's natural), capture the topic list as raw material, then redirect to
> "what should students be able to *do* afterward?"

## Quick Start

```
Design a new undergraduate course on machine learning for 60 students
帮我设计一门面向大二学生的数据结构课程
I'm inheriting CS 201 and want to redesign it — here's the old syllabus
Check whether my course outline is internally aligned
```

## Modes

| Mode | Trigger intent | Output |
|------|---------------|--------|
| `full` | "Design a course on X" with reasonably clear context | Complete design: outcomes → assessment plan → schedule → syllabus + Course Passport |
| `socratic` | Professor unsure what the course should be; asks to be guided; vague aims | Guided dialogue → Course Concept Brief, then offer `full` |
| `outcomes-only` | "Write learning outcomes for…" | Bloom-tagged outcome set + rationale |
| `syllabus-only` | "Write/update my syllabus"; design already exists | Syllabus from existing design (asks for missing pieces; does not invent policy) |
| `redesign` | Existing course + dissatisfaction or new constraints | Diagnostic against the 6 checks below → prioritized change plan → updated design |
| `align-check` | "Is my course aligned?" / pipeline Gate 1.5 standalone | Alignment Gate report (`shared/alignment_gate_protocol.md`), read-only |

**Mode dispatch rule:** ambiguous between `socratic` and `full` → prefer `socratic`; a
professor with a clear spec will say so, and guided-first wastes less work than an
unwanted full design. Detect intent in any language.

### Does NOT trigger

| Scenario | Use instead |
|----------|-------------|
| Building lecture notes / activities for one class meeting | `lesson-builder` |
| Writing the actual exam, rubric, or project brief | `assessment-architect` |
| Full design → materials → assessment run | `teaching-pipeline` |
| Analyzing student evaluations of an existing course | `teaching-reflector` |

## Agent Team (6)

| Agent | Role |
|-------|------|
| `design_mentor_agent` | Socratic dialogue: surfaces what the professor actually wants the course to do; never lectures, never converges prematurely |
| `outcome_architect_agent` | Drafts measurable, Bloom-tagged learning outcomes from the course concept; checks verb quality and level distribution |
| `assessment_planner_agent` | Designs the assessment *structure* (types, weights, timing, AI-policy tiers) — not the assessments themselves |
| `schedule_planner_agent` | Maps outcomes to a week-by-week arc with spacing/interleaving (Pedagogy Foundations §5); balances workload across weeks |
| `syllabus_writer_agent` | Assembles syllabus from confirmed design; policy sections flag institution-specific gaps rather than inventing them |
| `alignment_auditor_agent` | Runs the Alignment Gate checklist; read-only; reports findings by passport id |

## Workflow (`full` mode)

```
Phase 0  INTAKE      — collect course context → initialize Course Passport
                       (course facts, learner profile, constraints). Missing learner
                       profile = ask, don't guess (Passport Iron Rule 2).
         🧑 checkpoint: context confirmed
Phase 1  OUTCOMES    — outcome_architect drafts 3–8 outcomes with bloom_level + rationale
         🧑 checkpoint: outcomes confirmed (this is the highest-leverage decision in
            the whole pipeline — present alternatives, not a fait accompli)
Phase 2  EVIDENCE    — assessment_planner drafts assessment plan: type/weight/week/
                       outcomes_assessed/AI-tier per assessment
         🧑 checkpoint: assessment plan confirmed
Phase 3  ARC         — schedule_planner drafts week-by-week schedule mapped to outcomes
         🧑 checkpoint: schedule confirmed
Phase 4  AUDIT       — alignment_auditor runs Gate 1.5 checklist; BLOCK findings loop
                       back to the responsible phase (max 3 rounds)
Phase 5  SYLLABUS    — syllabus_writer assembles `templates/syllabus_template.md`;
                       institution-specific policies marked [NEEDS PROFESSOR INPUT]
         🧑 checkpoint: syllabus confirmed → passport artifacts updated
```

`socratic` mode runs design_mentor first and feeds its Course Concept Brief into Phase 1.
`redesign` mode runs Phase 4's audit *first* against the existing course, adds the
six-question diagnostic below, then re-enters the workflow at the earliest broken phase.

### Redesign diagnostic

1. What did students actually struggle with? (evidence, not impression — invite
   teaching-reflector output if it exists)
2. Are the outcomes still right for who now takes the course?
3. Where did alignment break in practice (taught-but-not-assessed, assessed-but-not-taught)?
4. What does the AI era change for this course's assessments?
5. What's the one change with the highest impact-to-effort ratio?
6. What must NOT change? (protect what works — redesigns that discard working elements
   are a known failure mode)

## Iron rules

1. **Backward order is non-negotiable in `full` mode.** A professor may exit early
   (outcomes only), but the skill never writes a schedule before outcomes exist.
2. **Passport discipline.** All design decisions land in `course_passport.yaml` per
   `shared/course_passport_schema.md`. Standalone runs offer passport creation at exit.
3. **No invented institutional policy.** Grading-scale rules, drop policies, integrity
   sanctions, accommodation procedures are institution-specific: the syllabus carries
   `[NEEDS PROFESSOR INPUT: <what & where to find it>]` markers, never plausible filler.
4. **Alternatives at high-leverage checkpoints.** Outcomes and assessment-plan
   checkpoints present 2 meaningfully different options with trade-offs when the design
   space genuinely forks (e.g., project-centered vs exam-centered evidence structure).
5. **Cite pedagogy when flagging, not when drafting.** Artifacts stay clean of citations;
   rationale at checkpoints cites Pedagogy Foundations § so the professor can audit the
   reasoning.

## Outputs

- `course_passport.yaml` — the design of record
- `syllabus.md` — from `templates/syllabus_template.md`
- `design_rationale.md` — why each major choice was made (feeds Stage 6 reflection and
  next-iteration redesign)
- (`align-check` mode) `alignment_report.md`

## References

- `references/outcome_verbs.md` — Bloom-level verb tables + weak-verb rewrite patterns
- `references/syllabus_checklist.md` — completeness checklist incl. AI-use policy section
- `templates/syllabus_template.md`
- `templates/course_passport_starter.yaml`
- Shared: `shared/pedagogy_foundations.md`, `shared/alignment_gate_protocol.md`,
  `shared/ai_era_integrity.md`, `shared/checkpoint_protocol.md`
