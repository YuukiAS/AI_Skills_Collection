---
name: pymc
description: Bayesian modeling with PyMC: model specification, priors, NUTS/VI fitting, diagnostics, posterior predictive checks, LOO/WAIC comparison, prediction, and code review.
status: active
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-06-19
profile_tags:
recommended_scope: project
license: Apache License, Version 2.0
metadata:
  skill-author: K-Dense Inc.
---
# PyMC Bayesian Modeling

## Workflow

1. Clarify estimand, data-generating assumptions, likelihood family, grouping structure, missingness, and prediction target.
2. Specify priors before seeing fit results. Use weakly informative or domain-informed priors and run prior predictive checks.
3. Build the PyMC model with named coordinates/dimensions, stable parameterization, and `pm.Data` when predictions or updates are needed.
4. Fit with NUTS by default. Save `InferenceData` with log likelihood when model comparison is needed.
5. Diagnose sampling: divergences, R-hat, ESS, BFMI, tree depth, trace plots, and energy plots. Reparameterize before increasing draws blindly.
6. Validate fit with posterior predictive checks, residual or calibration checks, sensitivity to priors, and domain plausibility.
7. Compare models with LOO/WAIC only when likelihood and data structure make comparison meaningful.
8. Report posterior quantities with uncertainty intervals, model limitations, and reproducible code.

## References

- Read `references/modeling-workflow.md` for prior, likelihood, diagnostic, and reporting checklists.
- Read `references/legacy-full-skill.md` for older PyMC code patterns and examples when needed.
- Read `bayesian-ppl-diagnostics/references/reference.md` when diagnosing Stan/PyMC/ArviZ outputs across PPLs.

## Validation

- Prior predictive checks are shown or explicitly waived with a reason.
- Divergences are investigated, not ignored.
- Posterior claims match the modeled estimand and include uncertainty.
