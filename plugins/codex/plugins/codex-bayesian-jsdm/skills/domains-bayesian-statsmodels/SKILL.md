---
name: statsmodels
description: Implement and review statsmodels analyses: OLS/GLM/mixed models, time series, robust covariance, diagnostics, coefficient tables, and reproducible inference workflows.
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
license: BSD License
metadata:
  skill-author: K-Dense Inc.
---
# Statsmodels

## Workflow

1. Confirm outcome type, design matrix, grouping/time structure, missingness, and inferential target.
2. Select model family: OLS/WLS/GLS, GLM, discrete model, mixed model, survival/time series, or robust alternative.
3. Build formulas carefully. Encode categorical variables, interactions, offsets, exposure, and transformations explicitly.
4. Fit the model and inspect diagnostics before interpreting coefficients.
5. Use robust covariance, clustered standard errors, or model alternatives when assumptions are violated.
6. Report coefficients with scale, reference levels, confidence intervals, p-values where appropriate, and diagnostics.

## References

- Read `references/statsmodels-workflow.md` for model-selection and diagnostic checklists.
- Read `references/legacy-full-skill.md` for older code examples and extended API notes.

## Validation

- Formula terms and reference categories are explicit.
- Residual, influence, or convergence diagnostics are addressed.
- Interpretation uses the correct link/scale for the fitted model.
