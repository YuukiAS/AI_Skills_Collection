# Research Presentation Reviewed Handoff Review

Date: 2026-08-17

Scope: Presentation plugin upgrade to evidence-first `research-group-meeting` mode.

## Planner Decision

Decision: partially merge the Deep Research reference library into the existing `presentations` plugin and `research-presentations` skill. Do not create a new plugin or source-name-triggered skill.

Reason:

- The user-facing task boundary is research presentation planning and QA.
- The new behavior strengthens an existing active skill and shared deck-plan layer.
- Source slide assets have mixed rights and possible embedded third-party/clinical material, so they belong in ignored audit cache only.

Routing contract:

- should trigger: PhD group meeting deck, supervisor discussion slides, research update with failures, next discriminating experiment, advisor decision page, evidence-first group-meeting PPTX, rendered scientific QA for research slides.
- should not trigger: DOCX/PDF conversion, manuscript readiness review, poster generation, generic project dashboard, business roadmap, pure literature summary without deck deliverable.
- neighbor skills: `business-presentations`, `research-reporting`, `scientific-prose`, `publication-figures`, `latex-posters`.
- front door: `presentations` plugin, `research-presentations` skill, `presentation-desktop` profile.

## Executor Boundary

Source-layer edits were made under:

- `skills/tools/documents-media/presentations/`
- `profiles/presentation-desktop.json`
- `scripts/codex_marketplace_config.json`
- `tests/test_presentations.py`
- `tests/fixtures/presentations/research_group_meeting/`
- `docs/provenance/`

Generated layers were rebuilt after source edits:

- `registry.json`
- `docs/SKILL_CATALOG.md`
- `docs/domains/documents-media.md`
- `plugins/codex/plugins/`

No downloaded public deck, whole-slide screenshot, public PDF, original PPTX, private CARE figure, or clinical image is committed.

## Reviewer Gates

- History/provenance gate: `docs/provenance/INTEGRATION_HISTORY.md` and `docs/provenance/RESEARCH_PRESENTATION_REFERENCE_LIBRARY_2026_08_17.md` record source, rights, and decision.
- Trigger boundary gate: `research-presentations/evals/trigger_queries.json` adds natural group-meeting requests and adjacent near-misses.
- Generated-layer discipline: `plugins/codex/plugins/presentations/` contains generated mirrors only; regression generator stays in `tests/fixtures/` and is not packaged into the plugin.
- Scientific QA gate: validator requires Research State, Evidence Board, per-slide scientific objects, evidence status, source evidence ids, fallbacks, and QA criteria for `research-group-meeting`.
- Anti-pattern gate: validator and `visual-qa.md` reject evidence-free cards, empty tables, consulting language, generic arrows, fake visualization, planning-language leakage, and vague next steps when they replace evidence.

Status: PASS for source-layer integration and release preparation.
