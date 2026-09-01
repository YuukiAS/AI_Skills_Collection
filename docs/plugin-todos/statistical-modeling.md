# statistical-modeling — Long-Term TODO

Canonical maintenance inbox for the `statistical-modeling` plugin.

## Open candidates

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
