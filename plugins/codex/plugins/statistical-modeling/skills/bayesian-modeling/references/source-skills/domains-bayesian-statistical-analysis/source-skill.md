---
name: statistical-analysis
description: Plan and report statistical analyses: estimand framing, test/model choice, assumption checks, power/sensitivity notes, effect sizes, uncertainty, and reproducible reporting.
status: active
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-03
profile_tags:
recommended_scope: project
license: MIT License
metadata:
  skill-author: K-Dense Inc.
---
# Statistical Analysis

## Workflow inheritance

For complex tasks, first apply the global `codex-workflow-protocol` skill. This skill only adds domain-specific knowledge, gates, and validation requirements. It must not weaken the global completion, escalation, or verification rules.

## Workflow

1. Translate the user question into estimand, outcome, predictors/groups, unit of analysis, and dependency structure.
2. Inspect data quality, missingness, measurement scale, outliers, and study design before choosing tests.
3. Choose the simplest defensible analysis: descriptive summary, hypothesis test, regression, survival model, Bayesian model, or simulation.
4. Check assumptions and identify robust or nonparametric alternatives.
5. Report effect sizes, uncertainty intervals, p-values only when appropriate, multiplicity caveats, and practical significance.
6. Validate by rerunning calculations, checking sensitivity choices, and making the code reproducible.

## Completion boundary

Do not claim completion from a smoke simulation, tiny dryrun, notebook import, or one successful toy run alone. Simulation, inference, or theorem-heavy research coding is complete only when the estimand, model assumptions, data-generating or likelihood assumptions, and requested validation evidence are checked at the intended scale or a precise residual risk is reported.

Bayesian/domain-specific acceptance should include prior justification, convergence diagnostics where applicable, posterior predictive or sensitivity checks where applicable, and a clear distinction between exploratory and confirmatory claims.

## References

- Read `references/statistical-decision-notes.md` for test/model selection and reporting conventions.
- Read `references/legacy-full-skill.md` for older examples and extended background.
- Use `statsmodels` for Python model implementation, `pymc` for PyMC models, `bayesian-ppl-diagnostics` for convergence and PPL diagnostics, and `simpy` for process-based simulation.

## Validation

- The analysis states assumptions, missing-data handling, and unit of analysis.
- Results distinguish exploratory, confirmatory, and sensitivity analyses.
- Budget warnings for full Bayesian/statistics domain installs are advisory only.
