# Changelog

All notable changes to Teaching Skills. The suite is improved against verified findings,
not vibes — major releases trace to a specific audit or use. Versions follow the plugin
manifest; the Codex sibling distribution (`teaching-skills-codex`) tracks its own.

## v1.2.0 — Correctness, guardrails, coverage & adoption (2026-06-15)

A large release implementing a verified 8-dimension improvement audit (42 findings, each
premise-checked). Closes the gap between the suite's promises and its mechanisms.

**Correctness (bugs)**
- Fixed a real pipeline deadlock: `workload_audit` had no writer, so Gate 1.5 check D1
  (BLOCK) would deadlock on every real run. `schedule_planner` now persists it; the gate
  stays read-only.
- Added schema fields that were used-but-undefined: `term_calendar`, `learner_profile.cohort_evidence`.
- `iteration_history` single-writer discipline; removed an orphaned directory.

**Honesty guardrails (prose → structure)**
- The recommendation letter (the suite's self-described "worst single failure") now has a
  template with a `[C#]` claim-to-intake trace appendix — a fabrication shows as a blank
  source cell. Feedback comments likewise template-backed.
- `check_passport.py` P11: structural PII guard (no student email/ID/roster in the passport).
- `check_content_markers.py`: `[NEEDS PROFESSOR INPUT]`/`[VERIFY]` enforced by Gate T4.
- The four-block checkpoint presentation is now a required emission format; a per-artifact
  output self-check (`shared/output_self_check.md`).

**Machine-checkable layer**
- Gate 3.5 is now executable (`check_quality_gate.py`) for its decidable core.
- Registry lint extended (R6–R9) to plugin/marketplace versions, description counts, and
  the ARCHITECTURE version — drift is now CI-enforced.
- Main-repo internal link checker (`check_links.py`).

**Coverage (+5 modes)** — gradebook/grade-distribution analytics, graded group projects +
peer assessment, accommodation operationalization, async-course design, and a carefully
bounded suspected-misconduct (`integrity-case`) companion.

**Adoption** — `render_document.py` (Markdown → DOCX/PDF) and `export_lms.py`
(GIFT / QTI 2.1 / Common Cartridge), so artifacts reach the LMS and the printer.

**Pedagogy & credibility** — honest caveats on the Bloom/active-learning/cognitive-load
claims; new sections on alternative grading and signature (studio/clinical/performance)
pedagogies; a second worked showcase (HIST 247 humanities seminar) with inspectable
person-affecting outputs (recommendation letter + intake trace + feedback report).

Suite: 15 skills · 89 modes · 76 agents. 63 tests; CI enforces gates, links, manifests.

## v1.1.2 — Enriched course dashboard (2026-06-11)
Visual dashboard: at-a-glance cards (grade donut, Bloom bars, semester strip), alignment
matrix, policies, cross-linked navigation. Still one self-contained HTML file.

## v1.1.1 — Learner analysis + course dashboard (2026-06-11)
New `cohort-analyst` skill (学情分析, aggregates-only) and the `dashboard` mode +
`build_dashboard.py`.

## v1.1.0 — Machine-checkable contracts (2026-06-11)
JSON Schema for the Course Passport; `check_passport.py`, `check_alignment_gate.py`,
`check_registry_consistency.py`; test suite + CI. Following advice from the ARS author.

## v1.0.0 — Initial release (2026-06-10)
14 skills, the Course Passport, alignment + quality gates, AI-era integrity model.
Plus a Codex sibling distribution (`teaching-skills-codex`).
