# presentations — Long-Term TODO

Canonical maintenance inbox for the `presentations` plugin. Detailed project feedback stays in project repos or `docs/provenance/`; this file only tracks generic candidates and evidence.

Current maturity: `alpha / Base v1`.

## Open candidates

### Remove Stage-4 benchmark assumptions from the normal production validator
status: PROMOTE_NOW
source: 038/041 real-paper execution
evidence: `validate_research_presentation_production_entry.py` currently requires a fixed six-job set and clustered-coverage + medical storyline assumptions; real-paper RESULTs record false rejections
target layer: qa
problem: a pure statistics paper can fail validation for lacking medical pages, and a medical paper can fail for lacking benchmark-specific statistical jobs.
candidate action: validate jobs/storyline declared by the current source/deck contract rather than a frozen Stage-4 fixture shape; retain strict source fidelity, selector, CUHK, render and repair-budget checks.
promotion gate: unrelated single-statistics, single-medical and unrelated multi-workstream regressions; no weakening of production gates.

### Diagram geometry and canonical edge/node treatment
status: BLOCKED_NEEDS_EVIDENCE
source: repeated TRACE visual feedback
evidence: `docs/provenance/research-presentation-maintenance-archive-2026-08-30/`, `docs/provenance/RESEARCH_PRESENTATION_CAT_TRACE_*`
target layer: rendering/qa
problem: semantic diagram gate is active, but geometry/style consistency remains partly advisory and repeatedly causes visual defects.
candidate action: renderer-specific canonical primitives and QA for reading direction, alignment, legal edge paths, anchors, arrowheads and peer-level boxes.
promotion gate: at least one new real deck or targeted rendered regression proving the primitive fixes actual output without overconstraining other diagrams.

### Deck-wide style system and terminology hierarchy
status: CANDIDATE_GENERIC
source: repeated real research deck revisions
evidence: `docs/provenance/research-presentation-maintenance-archive-2026-08-30/TODO.md`, `TODO_CAT_TRACE_V2_CANDIDATES_2026_08_27.md`, `TODO_CAT_TRACE_V3_MANDATORY_CANDIDATES_2026_08_27.md`
target layer: reasoning/rendering/qa
problem: sentence case, first-use terminology, question style, dataset/simulation numbering, mini-headers, metric labels, captions and references can drift across a deck.
candidate action: define a small deck-style contract and rendered consistency matrix, probably in shared references/QA rather than in the main skill body.
promotion gate: independent rendered deck showing the contract catches inconsistency without enforcing one visual layout for all scientific objects.

### Math and theory slide hierarchy
status: CANDIDATE_GENERIC
source: repeated statistics and theory deck feedback
evidence: `docs/provenance/research-presentation-maintenance-archive-2026-08-30/`, `docs/provenance/RESEARCH_PRESENTATION_CAT_TRACE_V2_REVIEW_2026_08_27.md`, `docs/provenance/RESEARCH_PRESENTATION_CAT_TRACE_V3_REVIEW_2026_08_27.md`
target layer: reasoning/rendering/qa
problem: short definitions, design settings, estimands, theorem statements and derivation steps can all be rendered as centered display math even when they have different scientific roles.
candidate action: add rendered examples and validator support for formula hierarchy, first-use semantic context, standard limit notation, and theory coverage maps.
promotion gate: theorem-heavy or statistical-method real deck replay plus unrelated math-heavy deck regression.

### Simulation, metric and structured-fact presentation
status: CANDIDATE_GENERIC
source: repeated real statistics deck feedback
evidence: `docs/provenance/research-presentation-maintenance-archive-2026-08-30/TODO.md`
target layer: reasoning/rendering/qa
problem: DGP, estimand, comparison, metric direction, metric purpose, structured dataset facts and seeds/reproducibility metadata can be mixed into prose dumps or weak pseudo-tables.
candidate action: promote compact table/list patterns and QA fields only after a real rendered regression exercises them.
promotion gate: at least one simulation-heavy deck and one real-data deck where rendered output proves the pattern improves scanability.

### Natural scientific slide language
status: CANDIDATE_GENERIC
source: repeated presentation and writing-style feedback
evidence: `docs/provenance/research-presentation-maintenance-archive-2026-08-30/TODO.md`, `docs/plugin-todos/writing-style.md`
target layer: writing/qa
problem: audience-facing slides can retain meta labels, internal workflow language, and templated contrast sentences even after ordinary polishing.
candidate action: decide whether presentation-specific language checks belong in `research-presentations`, `scientific-prose`, or a handoff between the two.
promotion gate: repeated independent English scientific slide evidence and a check that writing-style does not take over scientific structure.

### Real-workflow refinement from TRACE rather than synthetic challenge chains
status: PROMOTE_NOW
source: user decision after 041/042/043
evidence: `RESEARCH_PRESENTATION_CURRENT_ROUND.md` records `BASE_V1_READY_FOR_REAL_WORKFLOW_REFINEMENT` and 043 pause
target layer: reasoning/rendering/qa
problem: additional synthetic challenge tasks were producing more validation machinery than user-visible quality improvement.
candidate action: use the next TRACE revisions as real production feedback; promote only bounded generic failures, replay the original deck, then run unrelated regressions.
promotion gate: each promoted change must identify user-visible before/after and an unrelated regression.

## Recently promoted / established

- Presentation maintenance files were moved out of active runtime source to `docs/provenance/research-presentation-maintenance-archive-2026-08-30/`; the runtime rule subset is now `skills/tools/documents-media/presentations/research-presentations/references/real-world-presentation-guardrails.md`.
- Evidence-first research-group-meeting routing and scientific-object page archetypes.
- Exact CUHK Beamer/PDF default research route for unspecified desktop research talks.
- Source fidelity map, gold composition retrieval, executable scientific layouts, real render/contact-sheet review, bounded one-cycle repair contract.
- Theory framing by scientific guarantee/problem rather than theorem-count taxonomy is confirmed in current revision rules.

## Do not do

- Do not restart the paused 043 synthetic challenge merely to obtain a workflow PASS.
- Do not make consumed holdouts into unseen acceptance again.
- Do not add project/paper names as selector or layout special cases.
- Do not create a new skill for every visual failure; prefer existing reasoning/rendering/QA layers.
