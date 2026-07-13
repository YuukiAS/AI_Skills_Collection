---
name: bayesian-modeling
description: Bayesian and statistical modeling workflows with PyMC, diagnostics, simulation, and model reporting.
status: active
provenance: generated
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/domains/bayesian/bayesian-ppl-diagnostics
  - skills/domains/bayesian/pymc
  - skills/domains/bayesian/statsmodels
  - skills/domains/bayesian/statistical-analysis
  - skills/domains/bayesian/simpy
default_prompt:
---

# bayesian-modeling

## Trigger Boundary

Bayesian and statistical modeling workflows with PyMC, diagnostics, simulation, and model reporting.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `bayesian-ppl-diagnostics`: Executable guidance for Bayesian workflows using Stan/CmdStanPy, brms, PyMC, and ArviZ, with legacy JAGS/OpenBUGS paths and Rcpp acceleration patterns. Reference: `_src/diag/source.md`
- `pymc`: Bayesian modeling with PyMC: model specification, priors, NUTS/VI fitting, diagnostics, posterior predictive checks, LOO/WAIC comparison, prediction, and code review. Reference: `_src/pymc/source.md`
- `statsmodels`: Implement and review statsmodels analyses: OLS/GLM/mixed models, time series, robust covariance, diagnostics, coefficient tables, and reproducible inference workflows. Reference: `_src/stats/source.md`
- `statistical-analysis`: Plan and report statistical analyses: estimand framing, test/model choice, assumption checks, power/sensitivity notes, effect sizes, uncertainty, and reproducible reporting. Reference: `_src/analysis/source.md`
- `simpy`: Build and validate process-based discrete-event simulations in Python with SimPy: entities, resources, queues, event timing, replications, sensitivity analysis, and reporting. Reference: `_src/sim/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
