# PyMC Modeling Workflow Notes

- Start from an estimand and data-generating story, not from a preferred distribution.
- Use prior predictive simulation to reject implausible priors before fitting.
- Prefer named coordinates and dimensions to anonymous shapes.
- Treat divergences as model-geometry information. Try non-centered parameterization, tighter priors, rescaling, or a better likelihood before simply increasing draws.
- Use posterior predictive checks targeted to the scientific question: distributional fit, calibration, tail behavior, group-level fit, and temporal/spatial dependence.
- Use LOO/WAIC only for comparable likelihoods and inspect Pareto-k diagnostics.
- Report posterior intervals, decisions implied by the posterior, sensitivity to priors, and limitations.
