# Teaching Skills Architecture (v1.1.0)

Full pipeline view: flow, stage matrix, passport data flow, skill dependency graph, and
gate inventory. Per-mode reference: `MODE_REGISTRY.md`. Per-skill detail: each skill's
`SKILL.md`.

## 1. Two structural ideas

1. **The Course Passport** is the spine. Every stage reads it and appends to it
   (`shared/course_passport_schema.md`). It is also the resume mechanism: pipeline state
   lives in the passport plus the calendar, never in conversation memory.
2. **Teaching is a cycle, not a pipeline run.** Unlike a paper, a course loops: the
   semester's delivery stage (4) is a weekly loop, and Stage 6 feeds Stage 1 of the next
   term. The architecture is a cylinder, drawn flat below.

## 2. Pipeline flow

```
                ┌──────────────────────────────────────────────────────┐
                │  next term: new-term mode re-enters with evidence    │
                ▼                                                      │
 Stage 0 CONTEXT ──🧑── Stage 1 DESIGN ──🧑── [Gate 1.5 ALIGNMENT] ✓   │
   intake → passport     course-designer        BLOCK → back to 1     │
                                                 (max 3 rounds)        │
                                                      │ pass           │
                                                      ▼                │
                Stage 2 BUILD ──🧑── Stage 3 ASSESS ──🧑── [Gate 3.5 QUALITY] ✓
                 lesson-builder      assessment-architect   BLOCK → back to 2/3
                 (just-in-time ok)   + integrity audit          │ pass
                                                                ▼
                Stage 4 DELIVER  ←──────── weekly loop ─────────┐
                 ├─ next week's materials (lesson-builder)      │
                 ├─ student-mentor on demand (never auto)       │
                 └─ midcourse feedback wk 4–6 (teaching-reflector)
                                │ term ends
                                ▼
                Stage 5 REFLECT ──🧑── Stage 6 IMPROVE ──→ iteration_history ─┘
                 teaching-reflector     prioritized changes + redesign brief
```

🧑 = professor checkpoint (`shared/checkpoint_protocol.md`) · ✓ = gate: deterministic
checklist, then professor acknowledgment. Gates are non-skippable in pipeline mode.

## 3. Stage × dimension matrix

| Stage | Skill (modes used) | Key artifacts | Gate / checkpoint |
|---|---|---|---|
| 0 CONTEXT | teaching-pipeline (intake) | `course_passport.yaml` initialized | 🧑 context confirmed |
| 1 DESIGN | course-designer (full / socratic / redesign) | outcomes, assessment plan, schedule, syllabus, design rationale | 🧑 per phase (outcomes checkpoint is highest-leverage) |
| 1.5 ALIGNMENT | teaching-pipeline → gate_runner | `gates.alignment_gate` findings | ✓ A/B/C/D checks (`shared/alignment_gate_protocol.md`); BLOCK → Stage 1, max 3 rounds |
| 2 BUILD | lesson-builder (week-batch / full) | lesson plans, lecture notes, slide outlines, activity sheets, cases | 🧑 per batch |
| 3 ASSESS | assessment-architect (exam / quiz / rubric / project-brief / integrity-check) | blueprints, instruments, verified keys, rubrics, briefs; `ai_resilience` set | 🧑 blueprint before items; 🧑 per instrument |
| 3.5 QUALITY | teaching-pipeline → gate_runner | `gates.quality_gate` findings | ✓ Q/T/U/I/W checks (`shared/quality_gate_protocol.md`); BLOCK → Stage 2/3 |
| 4 DELIVER | student-mentor (all modes, on demand) + submission-auditor (spec/audit/batch-audit, on demand) + lesson-builder (just-in-time) + teaching-reflector (midcourse) | feedback drafts, outreach drafts, letters, submission audit reports, midcourse report | 🧑 every person-affecting artifact; never auto-sent |
| 5 REFLECT | teaching-reflector (eval-analysis + triangulation) | evaluation analysis report | 🧑 findings + priorities confirmed |
| 6 IMPROVE | teaching-pipeline → iteration_coach | `iteration_history[]` entry + redesign brief | 🧑 record confirmed; offer new-term re-entry |

## 4. Passport data flow

```
professor input ──→ Stage 0 writes course/, learner_profile/
course-designer ──→ learning_outcomes[], assessment_plan[], schedule[], policies
gate_runner     ──→ gates.* (only writer of gate fields; read-only otherwise)
lesson-builder  ──→ schedule[].activities, schedule[].artifact_refs
assessment-architect → assessment_plan[].artifact_ref, .ai_resilience
submission-auditor  → iteration_history[].evidence (anonymous counts only)
teaching-reflector  → iteration_history[].evidence
iteration_coach ──→ iteration_history[] (consolidated record)
ALL skills      ──→ artifacts[] ledger entries (confirmed_by_professor at checkpoints)

NEVER in the passport: data about identifiable students (hard rule —
checkpoint_protocol.md "Person-affecting work" + student-mentor iron rules).
```

Write discipline: append-don't-overwrite; no skill mutates another stage's fields;
`confirmed_by_professor` set only at real checkpoints (Passport Iron Rules 1, 4).

## 5. Skill dependency graph

```
                      teaching-pipeline (orchestrator, 4 agents)
                  /       |          |           |          |         \
     course-designer  lesson-   assessment-  student-  submission-  teaching-
       (6 agents)     builder   architect    mentor    auditor      reflector
           |         (6 agents) (7 agents)  (5 agents) (4 agents)  (6 agents)
           └─────────────┴──────────┴───────────┴───────────┴──────────┘
                                      |
            shared/: course_passport_schema · pedagogy_foundations ·
            alignment_gate_protocol · quality_gate_protocol ·
            ai_era_integrity · checkpoint_protocol
```

Handoffs: course-designer → (outcomes/schedule) → lesson-builder; course-designer →
(assessment_plan) → assessment-architect; assessment-architect → (briefs/rubrics as
spec sources) → submission-auditor; submission-auditor → (class patterns, anonymous) →
iteration evidence; teaching-reflector → (iteration evidence) →
course-designer redesign. teaching-reflector's `sotl` mode hands off externally to the
Academic Research Skills suite for the publication phase.

## 5b. Extension skills (v1.1.0)

Seven extension skills layer production, operations, and compliance work on the core
pipeline. They follow every shared protocol (passport discipline, checkpoints, honesty
markers) and are dispatched on demand — the gates never depend on them.

| Extension | Attaches at | Consumes | Produces |
|-----------|------------|----------|----------|
| deck-studio | Stage 2 | lesson-builder slide outlines, theme spec | rendered decks, themes, code-generated figures, handouts, posters |
| lab-forge | Stage 2–3 | assessment_plan entries, outcomes | executable lab packages, datasets + ground truth (professor-only), starter code, autograders, verified solutions |
| media-scripter | Stage 2 | lecture notes, flipped specs | video scripts, storyboards, episode series, captions/transcripts |
| course-publisher | Stage 4 | passport schedule/policies/artifacts | announcement + weekly-email drafts, static course site, LMS packages, FAQ |
| ta-coordinator | Stage 4 | rubrics, assessment plan | TA handbooks, calibration packages, allocation plans, consistency analyses |
| accreditation-mapper | Stage 1 / 6 | learning_outcomes, artifacts, iteration_history | outcome–standard matrices, evidence indexes, gap analyses, self-study drafts |
| bilingual-courseware | cross-cutting | any course artifact | confirmed glossary, glossary-bound translations, sync registry, terminology audits |

Notable cross-links: lab-forge autograder output feeds submission-auditor's
deterministic checks for code genres; bilingual-courseware's glossary is consumed by
course-publisher (announcements) and media-scripter (caption terminology);
accreditation-mapper's continuous-improvement narrative is built from the Stage 6
`iteration_history` the core pipeline maintains; deck-studio and course-publisher share
the build-product model (markdown/passport is source, rendered output is rebuildable).

## 6. Gate inventory

| Gate | Stage | Blocking checks | Advisory checks |
|------|-------|-----------------|-----------------|
| Alignment (1.5) | post-design | A1–A3 triangle closure, B2 bloom tags, C1 weights sum, D1 workload computed | A4–A5, B1/B3/B4 outcome quality, C2–C4 assessment structure, D2–D3 workload range |
| Quality (3.5) | post-build/assess | Q1 AI policy exists, Q2 integrity audit ran, T1 TILT sections | Q3–Q4 resilience, T2–T3 transparency, U1–U3 UDL, I1–I2 inclusion, W1 workload re-audit |

Shared gate mechanics: findings cite passport ids; BLOCK → return to producing stage
(max 3 rounds, then reframed as a professor decision); WARN dismissible with logged
reason, never re-raised; professor acknowledgment closes the gate.

## 7. Cross-cutting protocols

- **Checkpoints** — `shared/checkpoint_protocol.md`: decision-oriented presentations,
  surfaced defaults, genuine open questions, "just proceed" respected, no sycophancy on
  pushback, hard rule for person-affecting outputs.
- **Honesty markers** — `[NEEDS PROFESSOR INPUT: …]` (institutional/contextual facts),
  `[VERIFY: …]` (domain claims the agent cannot fully verify), `[MANDATED]`
  (accreditation-required outcomes), `NOT_EVALUABLE` (gate checks lacking data).
- **AI-era integrity** — `shared/ai_era_integrity.md`: P/D/O tiers, resilience
  patterns, audit procedure; no detection-tool reliance anywhere in the suite.
- **Evidence honesty** — Pedagogy Foundations §11 governs all reading of student
  evaluations; small-N and bias caveats are mandatory in reports.
