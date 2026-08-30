# presentations — Long-Term TODO

Canonical maintenance inbox for the `presentations` plugin. Detailed project feedback stays in project repos or `docs/provenance/`; this file only tracks generic candidates and evidence.

Current maturity: `alpha / Base v1`.

## Open candidates

### Consolidate project-specific TODO files out of active plugin payload
status: PROMOTE_NOW
source: CAT-TRACE v2/v3 revision history + current repository layout
evidence: `skills/tools/documents-media/presentations/research-presentations/TODO*.md`, `CURRENT_RESEARCH_PRESENTATION_REVISION_RULES.md`, matching generated plugin copies
target layer: distribution
problem: project-specific TODO/history files currently live inside the active skill source and are mirrored into the generated plugin, mixing maintenance backlog with runtime capability.
candidate action: migrate project-specific history to `docs/provenance/`; merge mature generic rules into active skill/shared QA/references; move unresolved generic candidates into this file; remove maintenance-only TODO files from generated runtime payload.
promotion gate: preserve every confirmed rule/history pointer; source/plugin parity and presentation regressions must pass.

### Remove Stage-4 benchmark assumptions from the normal production validator
status: PROMOTE_NOW
source: 038/041 real-paper execution
evidence: `validate_research_presentation_production_entry.py` currently requires a fixed six-job set and clustered-coverage + medical storyline assumptions; real-paper RESULTs record false rejections
target layer: qa
problem: a pure statistics paper can fail validation for lacking medical pages, and a medical paper can fail for lacking benchmark-specific statistical jobs.
candidate action: validate jobs/storyline declared by the current source/deck contract rather than a frozen Stage-4 fixture shape; retain strict source fidelity, selector, CUHK, render and repair-budget checks.
promotion gate: unrelated single-statistics, single-medical and unrelated multi-workstream regressions; no weakening of production gates.

### Promote confirmed TRACE revision rules into stable runtime layers
status: CANDIDATE_GENERIC
source: repeated CAT-TRACE real presentation revisions
evidence: `CURRENT_RESEARCH_PRESENTATION_REVISION_RULES.md`, `docs/provenance/RESEARCH_PRESENTATION_CAT_TRACE_*`, confirmed TODO files
target layer: reasoning/rendering/qa
problem: several repeatedly confirmed rules still live in cumulative revision notes rather than the smallest active layer that enforces them.
candidate action: triage rule-by-rule into SKILL narrative guidance, shared layout primitive, rendered QA or backlog; do not dump the entire notes file into SKILL.md.
promotion gate: repeated/confirmed real evidence plus rendered regression for geometry-sensitive rules.

### Diagram geometry and canonical edge/node treatment
status: BLOCKED_NEEDS_EVIDENCE
source: repeated TRACE visual feedback
evidence: current presentation TODO sections on edge crossing, anchors, arrow size, peer node consistency, container-vs-process semantics
target layer: rendering/qa
problem: semantic diagram gate is active, but geometry/style consistency remains partly advisory and repeatedly causes visual defects.
candidate action: renderer-specific canonical primitives and QA for reading direction, alignment, legal edge paths, anchors, arrowheads and peer-level boxes.
promotion gate: at least one new real deck or targeted rendered regression proving the primitive fixes actual output without overconstraining other diagrams.

### Real-workflow refinement from TRACE rather than synthetic challenge chains
status: PROMOTE_NOW
source: user decision after 041/042/043
evidence: `RESEARCH_PRESENTATION_CURRENT_ROUND.md` records `BASE_V1_READY_FOR_REAL_WORKFLOW_REFINEMENT` and 043 pause
target layer: reasoning/rendering/qa
problem: additional synthetic challenge tasks were producing more validation machinery than user-visible quality improvement.
candidate action: use the next TRACE revisions as real production feedback; promote only bounded generic failures, replay the original deck, then run unrelated regressions.
promotion gate: each promoted change must identify user-visible before/after and an unrelated regression.

## Recently promoted / established

- Evidence-first research-group-meeting routing and scientific-object page archetypes.
- Exact CUHK Beamer/PDF default research route for unspecified desktop research talks.
- Source fidelity map, gold composition retrieval, executable scientific layouts, real render/contact-sheet review, bounded one-cycle repair contract.
- Theory framing by scientific guarantee/problem rather than theorem-count taxonomy is confirmed in current revision rules.

## Do not do

- Do not restart the paused 043 synthetic challenge merely to obtain a workflow PASS.
- Do not make consumed holdouts into unseen acceptance again.
- Do not add project/paper names as selector or layout special cases.
- Do not create a new skill for every visual failure; prefer existing reasoning/rendering/QA layers.
