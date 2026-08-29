# Source Notes: Buerkner 2017 brms Holdout

## Citation

Paul-Christian Buerkner. "brms: An R Package for Bayesian Multilevel Models Using Stan." Journal of Statistical Software 80(1), 1-28, 2017. DOI: 10.18637/jss.v080.i01.

## Paper Scope

The paper presents `brms` as an R formula interface for Bayesian multilevel models fitted through Stan. It emphasizes broad model-family coverage, flexible prior specification, automatic Stan code/data generation, HMC/NUTS estimation, posterior summaries, diagnostic plots, and model comparison with WAIC/LOO.

## Model Description

The response distribution is represented through a likelihood with parameters linked to predictors. Distributional parameters can each have their own predictor. Population-level, group-level, and family-specific parameters are separated so that multilevel formulas map to Stan code.

The paper writes group-level covariance matrices through standard deviations and a correlation matrix:

```tex
\mathbf{V}_k=\mathbf{D}(\boldsymbol{\sigma}_k)\boldsymbol{\Omega}_k\mathbf{D}(\boldsymbol{\sigma}_k),\qquad
\boldsymbol{\Omega}_k\sim \operatorname{LKJ}(\zeta).
```

It also discusses covariance structures of the form:

```tex
\boldsymbol{\Sigma}_k=\mathbf{V}_k\otimes\mathbf{A}_k.
```

## Prior Specification

`brms` uses Stan's NUTS sampler, so priors need not be conjugate. It supports flexible priors on population effects, group-level standard deviations, correlation matrices, and family-specific parameters. The paper also notes that syntactically valid priors are not automatically scientifically meaningful and must be interpreted by the analyst.

## Fitting Workflow

Figure 1 describes the sequence: user model information is passed to `brm`; `brm` calls `make_stancode` and `make_standata`; generated model code/data are passed to `rstan`; Stan translates, compiles, and fits the model; the fitted model is post-processed in `brms`; users inspect results through methods on the fitted object.

## Kidney Example

The worked kidney example models recurrence time for infections in kidney patients. The formula shown in the paper is:

```tex
time \mid cens(censored) \sim age * sex + disease + (1 + age \mid patient)
```

The example reports posterior summaries, WAIC/LOO model comparison, trace and density diagnostics, and marginal effects plots. Figure 3 visualizes marginal effects for age, sex, disease, and the age-by-sex interaction.

## Ordinal Example

The inhaler example demonstrates ordinal modeling for a two-treatment, two-period crossover trial. The paper uses a cumulative ordinal family and discusses thresholds, category-specific effects, discrimination parameters, and alternate ordinal families such as `sratio`, `cratio`, and `acat`.

## Package Comparison

Tables 1 and 2 compare `brms` with `lme4`, `MCMCglmm`, `rstanarm`, and `rethinking`. `brms` covers linear, robust linear, binomial, categorical, count, survival, ordinal, zero-inflated/hurdle, generalized additive, and non-linear models, but the table also records limits such as no missing-value imputation and no modularized interface in that 2017 comparison.

## Limitations and Interpretation

The conclusion frames `brms` as a flexible multilevel modeling interface that is easier than writing Stan manually for many standard models, while retaining Bayesian workflow responsibilities: prior choice, convergence diagnostics, interpretation, and model comparison remain analyst tasks.
