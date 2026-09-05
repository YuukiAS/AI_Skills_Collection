# statistical-modeling — Long-Term TODO

Canonical maintenance inbox for the `statistical-modeling` plugin.

## Open candidates

### Delegate reader-facing wording without giving away statistical semantics

status: READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER
source: cross-plugin communication boundary audit, 2026-09-05
proposal: Keep `statistical-modeling` as the owner of model choice, assumptions, inferential target/estimand semantics, uncertainty, diagnostics, comparison and statistical conclusion. After those semantics are frozen, use the canonical generic language layer for reader-facing result interpretation, assumption/diagnostic explanations, table/figure captions, bounded conclusions and limitation wording. See `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`.
required boundary: the language layer may translate ordinary English scaffolding and improve explanation, but must not change the estimand/parameter meaning, conditioning set, comparator, uncertainty, calibration statement or conclusion strength. Statistical tables/plots remain statistically owned here even when their captions are rewritten elsewhere.
promotion gate: after task 050 closes and the generic language layer identity is settled, replay one real statistical analysis handoff with a caption/result/conclusion package and verify zero statistical-semantic drift.

### Curriculum-driven capability refinement pilot

status: BLOCKED_NEEDS_EVIDENCE
source: user-approved design direction, 2026-09-01
proposal: Use bounded competency modules backed by authoritative textbooks, methodological papers, and official software guidance. Study/extraction must be reviewed before any active plugin change. See `docs/workflows/CURRICULUM_DRIVEN_DOMAIN_PLUGIN_REFINEMENT.md`.
first pilot: prior specification + prior predictive checking
candidate sources: *Doing Bayesian Data Analysis*, *Bayesian Data Analysis*, *Statistical Rethinking*, and relevant official PyMC / Stan guidance, subject to lawful source access and Planner confirmation.
promotion gate: demonstrate improved reasoning on should-trigger, should-not-trigger, and grey cases; then replay the production path and unrelated regression before release.

No production change is currently frozen from this candidate.

Future TODOs should come from real modeling tasks (Bayesian, causal, inference, simulation, diagnostics, data analysis) and must distinguish scientific/statistical correctness from Presentation/report communication issues.

## Promotion notes

- A wrong assumption, estimand, uncertainty interpretation or calibration claim can qualify as a severe single-project failure.
- A project-specific model choice remains project-local unless it reflects a reusable workflow or diagnostic rule.
- Do not use this plugin to own Presentation layout or manuscript prose.
- Do not fork a second generic say-it-plain/caption-writing rule set; hand off reader-facing wording only after statistical semantics are stable.
