# bayesian

Active skills: 5

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain bayesian --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill bayesian-ppl-diagnostics --skill domain-bayesian-pymc --skill domain-bayesian-simpy --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `bayesian-ppl-diagnostics` (`skills/domain/bayesian/bayesian-ppl-diagnostics`): Executable guidance for Bayesian workflows using Stan/CmdStanPy, brms, PyMC, and ArviZ, with legacy JAGS/OpenBUGS paths and Rcpp acceleration patterns.
- `pymc` (`skills/domain/bayesian/pymc`): Bayesian modeling with PyMC: model specification, priors, NUTS/VI fitting, diagnostics, posterior predictive checks, LOO/WAIC comparison, prediction, and code review.
- `simpy` (`skills/domain/bayesian/simpy`): Build and validate process-based discrete-event simulations in Python with SimPy: entities, resources, queues, event timing, replications, sensitivity analysis, and reporting.
- `statistical-analysis` (`skills/domain/bayesian/statistical-analysis`): Plan and report statistical analyses: estimand framing, test/model choice, assumption checks, power/sensitivity notes, effect sizes, uncertainty, and reproducible reporting.
- `statsmodels` (`skills/domain/bayesian/statsmodels`): Implement and review statsmodels analyses: OLS/GLM/mixed models, time series, robust covariance, diagnostics, coefficient tables, and reproducible inference workflows.

## Main References

- `skills/domain/bayesian/bayesian-ppl-diagnostics/references/reference.md`
- `skills/domain/bayesian/pymc/references/legacy-full-skill.md`
- `skills/domain/bayesian/pymc/references/modeling-workflow.md`
- `skills/domain/bayesian/simpy/references/legacy-full-skill.md`
- `skills/domain/bayesian/simpy/references/simulation-workflow.md`
- `skills/domain/bayesian/statistical-analysis/references/legacy-full-skill.md`
- `skills/domain/bayesian/statistical-analysis/references/statistical-decision-notes.md`
- `skills/domain/bayesian/statsmodels/references/legacy-full-skill.md`
- `skills/domain/bayesian/statsmodels/references/statsmodels-workflow.md`
