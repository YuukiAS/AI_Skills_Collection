# STAT5060 Software and Workflow Policy V1

- Status: FROZEN_SOFTWARE_DECISIONS_FOR_EXECUTION; installation/build validation is a subsequent Codex gate.
- Date: 2026-09-28.
- Source authority: official package/project documentation and release metadata listed below; original course scripts are historical teaching evidence, not current software authority.
- Relation: statistical meaning is owned by `STAT5060_CANONICAL_KNOWLEDGE_V1.md`. This file owns software roles, equivalence limits, environment strategy and Bayesian demonstration scope. Exact teaching minutes and assessed questions are owned by their respective frozen specifications.

## 1. Decisions, not a menu

**R is the teaching and HW1 reference language.** Teach `stats::glm`, `MASS::glm.nb`, `nnet::multinom` and one scalar random-intercept `lme4::glmer` workflow. Python alternatives for ordinary count/nominal models and simulation are provided as transferable examples, not a second parallel lecture. HW1 may be entirely R, or Python for Questions 1, 2 and 4 with the supplied R runner for Question 3. All students therefore need access to R, but no one must install PyMC, Stan, JAGS, a C++ compiler or two Bayesian systems to complete HW1.

**WinBUGS GUI steps leave the main line completely.** Preserve a short historical explanation of BUGS model declaration, precision parameterization and conditional sampling; do not spend teaching time installing WinBUGS, clicking model/data/compile/update windows or translating obsolete Windows paths. Official MRC material states the original BUGS programs are no longer actively developed [W23]. This is not a claim that the statistical ideas or all BUGS-family software are obsolete.

**JAGS/R2jags is an optional historical bridge.** It remains a reasonable way to run an existing BUGS-language analysis, especially when a legacy model is already validated. It is neither the required Bayesian entry point nor a dead tool. Its separate system dependency and a third API are unnecessary in this sprint [W21–W22].

**Tutorial Bayesian section: exactly ten minutes of workflow, not ten minutes of sampler theory.** Use the same device-count case in PyMC and diagnostics from the current ArviZ ecosystem. Show model declaration, meaningful priors, posterior sampling, R-hat, bulk/tail ESS, divergence count and posterior predictive checks. Do not teach HMC/NUTS derivations, PyTensor internals, custom samplers or backend engineering. There is no assessed Bayesian programming in HW1.

**R-side Bayesian mapping:** `brms` is a high-level model interface; Stan is the modeling/computational engine; CmdStanR is an R interface to CmdStan, not another statistical model. Include one brms counterpart in the appendix, with an explicit prior/parameterization correspondence. Do not give full brms, Stan and PyMC API lessons. Stan coding is optional later-course/project work, not a prerequisite disguised as modernization [W07–W09].

**Rcpp and TMB:** one short 'under the hood' paragraph in the whole-course note; zero Tutorial 1 minutes, zero HW1 marks. Rcpp connects R to C++ and supports performance-sensitive implementation. TMB combines C++ templates, automatic differentiation and Laplace approximation for latent/random-effect likelihoods. End users of glmmTMB benefit from TMB without writing TMB templates. These are developer/performance-engineering tools, not missing applied-modeling prerequisites [W24–W25].

## 2. Audited tool map

'Audited' means a current official documentation/release surface was inspected on the date above. It is not a market-share ranking or a promise that every package has been installed in this planning session. Availability, release metadata and statistical suitability are separate observations.

| Tool | 2026 assessment and layer | Student-facing role | Important boundary / primary authority |
|---|---|---|---|
| R stats | Maintained core R modeling/inference; GLM via IRLS | Required now | Formula, family, offset, response coding, likelihood and diagnostics matter more than API inventory. [W01] |
| MASS | Current standard package; `glm.nb` estimates NB shape | Required now | Its theta is kappa in this course, not statsmodels alpha. [W02] |
| nnet | Current standard multinomial ML route | Required now | First response level is baseline; no penalty unless explicitly requested; scale predictors and check convergence. [W03] |
| ordinal | Current CRAN release metadata includes 2026.7-26 | Direct use later, reference only now | `clm` ordinary, `clmm` mixed; ordered cutpoints and minus-sign convention. [W04] |
| lme4 | Current documented ML/LMM/GLMM implementation | Required scalar RI workflow | `glmer` nAGQ=1 is Laplace; higher adaptive quadrature has structural restrictions. `re.form=NA` sets random effects to zero; it does not integrate them. [W05] |
| glmmTMB | Current broader applied GLMM interface built on TMB | Later-course direct use | NB families, dispersion and zero inflation are distinct modeling choices; do not add them automatically. [W06] |
| brms | Current high-level Bayesian regression/multilevel interface | Recognize now; use later | Compiles a model for Stan. Formula similarity does not guarantee identical priors or estimands. [W07] |
| Stan / CmdStanR | Current probabilistic model/engine and its R interface | Know architecture now; optional later programming | Continuous HMC does not directly sample an unconstrained discrete class label; marginalize where required. No live compilation in Tutorial 1. [W08–W09] |
| mclust | Current Gaussian model-based mixture/clustering package | Later direct use | Gaussian covariance families and model-based clustering, not every course mixture regression. [W14] |
| flexmix | Current CRAN metadata includes 2.3-21, 2026-08-25 | Later direct use | Finite mixture regressions, supported component models and concomitant variables. [W15] |
| mice | Current MAR-oriented multiple-imputation workflow; metadata includes 3.19.0 | Later direct use | Proper pooling and compatible imputation models are essential; does not identify MNAR. [W16] |
| depmixS4 | Current ordinary HMM route; metadata includes 1.5-4, 2026-08-24 | Default ordinary HMM example later | Suitable state/emission models, not an automatic implementation of the full HMLVM. [W17] |
| hmmTMB | Current specialist HMM tool; 2025 package/JSS documentation | Optional advanced later | Covariate/random/smooth effects for supported HMMs. TMB-backed does not mean students must learn C++. [W18] |
| JAGS / R2jags | Available and reasonable for validated BUGS-language work | Optional historical bridge | R2jags needs rjags and system JAGS; no mandatory installation. [W21–W22] |
| Rcpp | Current R/C++ integration and package development | Awareness only | Not an estimator or a substitute for choosing a likelihood. [W24] |
| TMB | Current automatic differentiation/Laplace likelihood infrastructure; metadata includes 1.9.25 | Awareness only | Package developer/research-computing layer. [W25] |
| NumPy / pandas | Current array/RNG and data-table foundations | Optional Python route | Same seed is not a cross-language or all-version byte-equivalence guarantee. [W26–W27] |
| SciPy | Current numerical/distribution/optimization layer | Helper use, not an optimization mini-course | Numerical integration can verify population-averaged probabilities; student helper is provided. [W28] |
| statsmodels | Current frequentist ordinary regression/inference route | Optional Q1/Q2/Q4 | Discrete NB estimates alpha; GLM NB family does not estimate its supplied alpha by default. BinomialBayesMixedGLM is Bayesian Laplace/VB, NOT glmer marginal ML. [W12] |
| PyMC | Current Bayesian model declaration/sampling system; stable documentation returned a 6.x line | Ten-minute instructor demo; optional later student use | Declare the sampler and priors; record actual resolved version. It is not a frequentist GLMM shortcut. [W10] |
| ArviZ | Current diagnostics/posterior-analysis ecosystem; 1.x documentation is modular | Interpret output now | Not a model-fitting engine. Do not assume old `az.*` snippets still describe the current API. [W11] |
| scikit-learn mixtures | Current GaussianMixture EM and BayesianGaussianMixture variational tools | Later limited comparison | The latter is not full posterior MCMC; neither is generic mixture regression or Chapter 9 mixed-membership survival. [W20] |
| hmmlearn | Documented ordinary Python HMM implementation | Later basic Python illustration | Use supported emission/transition structures; no claim of equivalence to mixed HMM/HMLVM. Documentation availability is not evidence of rapid release cadence. [W19] |

## 3. R/Python equivalence contract

1. **Poisson:** same CSV rows, response, design columns, explicit intercept, exposure offset, log link and unpenalized likelihood. Compare coefficients, log likelihood and predictions. Do not compare a standardized Python design to an unstandardized R design without transforming coefficients.
2. **NB2:** use MASS `glm.nb` and statsmodels discrete `NegativeBinomial(..., loglike_method='nb2')`, estimating shape in both. Convert `kappa=theta_R=1/alpha_statsmodels`. PyMC's `NegativeBinomial(mu,alpha)` instead uses `alpha=kappa`. Covariance implementations can use different information approximations; point estimates can agree more closely than reported SEs.
3. **Nominal:** same explicit baseline, category label mapping, no regularization, intercept and covariate coding. Validate predicted probabilities and the reference-change algebra, not raw coefficient arrays with unknown order.
4. **Binary GLMM:** canonical estimator is R `glmer(...,family=binomial,nAGQ=9)` with one scalar random intercept. Do not substitute statsmodels Bayesian Laplace/VB, PyMC posterior means, GEE or an ordinary logit with cluster-robust SE and call it equivalent. Those answer related but different questions. The supplied R script plus CSV outputs is the Python student's supported bridge; no rpy2 or custom quadrature programming is assessed.
5. **Ordinal:** ordinary OrderedModel is not `clmm`; a plus-sign equation must be converted before comparing with `clm`/`clmm`.
6. **Mixtures/HMMs:** match likelihood, state/component allocation unit, covariance constraints, transition structure and estimation objective before comparing output. Shared names such as 'Bayesian' or 'mixed' do not establish equivalence.

For deterministic common-data checks, use absolute coefficient tolerance 1e-4 for ordinary Poisson/nominal and 1e-3 for NB2 coefficients; probability tolerance 1e-5; log-likelihood tolerance 1e-3 after harmonizing constants. Allow up to 5% relative difference in NB reported SE where a documented expected/observed information convention explains it; investigate larger discrepancies. Do not enforce relative error when a value is near zero. For the scalar GLMM, compare against the private high-order quadrature design pilot within 0.01 per beta, 0.02 for random-effect SD and 0.002 for profile probabilities. Final R results, actual quadrature diagnostics and any justified software-specific tolerance are recorded, not silently rounded into agreement.

## 4. Exact Bayesian demonstration model

Data: frozen `tutorial_devices.csv`. Response faults; predictors service and load; exposure in hundreds of operating hours.

- beta0 ~ Normal(0, 1.5^2).
- beta_service, beta_load independently ~ Normal(0, 1^2).
- log(kappa) ~ Normal(log(2), 0.7^2).
- mu_i=exposure_100h_i * exp(beta0+beta_service*service_i+beta_load*load_i).
- faults_i ~ NB2(mu_i,kappa), variance mu_i+mu_i^2/kappa.

This is a newly authored teaching model, not an original lecturer's prior recommendation. Show a prior predictive check before the posterior result, so 'weakly informative' is not merely asserted.

### PyMC execution

Use four chains, 1,000 warmup and 1,000 retained draws per chain, seed 5060102. Explicitly select the documented built-in PyMC NUTS sampler rather than allowing an installed optional backend to change the default. Current audited syntax uses `nuts_sampler='pymc'` and `nuts={'target_accept':0.9}`; confirm against the locked release's signature during implementation. API adaptation that preserves the exact model/sampler configuration is permitted. No backend performance comparison.

Prior predictive: 500 draws, seed 5060103. Posterior predictive: 500 evenly selected retained posterior draws across chains, seed 5060104; selection indices must be recorded. Retain all chains for sampling diagnostics. Build one zero-frequency posterior-predictive display and one count-distribution/tail display, with the observed statistic marked. These are checks against aspects of observed data, not proofs of correct specification.

Use current `arviz_stats.summary` or its documented 1.x equivalent with unrounded values, 95% intervals and bulk/tail ESS. Own Matplotlib plots from the stored posterior-predictive draws are acceptable and avoid making this a plotting-API lecture. Label credible intervals accurately. Frozen quality targets for beta0, beta_service, beta_load and log(kappa): rank-normalized split R-hat <1.01; bulk and tail ESS at least 400; MCSE(mean)/posterior SD <=0.05; zero post-warmup divergences. These are necessary demonstration quality checks, not sufficient evidence of a correct posterior/model.

Bounded numerical recovery: target_accept 0.95, then up to 2,000 retained draws per chain and 2,000 warmup; keep data, likelihood and priors fixed. Do not discard divergent draws or select only favorable chains. If the bounded run still fails, record failure and return for statistical review; do not fabricate a clean screenshot.

### R counterpart: appendix only

Use an explicit intercept-as-coefficient formulation such as `faults ~ 0 + Intercept + service + load + offset(log(exposure_100h))`, with an explicitly created all-one Intercept column, `family=negbinomial(link='log')`, and proper corresponding class-b priors. This avoids inadvertently assigning a different prior to brms's internally centered default intercept. Shape prior is lognormal(log(2),0.7). CmdStanR is the backend interface. This code is explanatory/optional, not a second required Bayesian run in the sprint and not a HW1 dependency.

## 5. Environment, runtime and fallback policy

### Small required environment

R: a released stable R version, `stats`, `MASS`, `nnet`, `lme4`, `ggplot2`, `jsonlite`, `renv`; a test package may be included for execution checks. Do not install every audited package. Core course analyses can use base R graphics and data frames; a tidyverse bundle is not required. Prefer binary packages on students' Windows/macOS machines where available.

Python core: NumPy, pandas, SciPy, statsmodels, Matplotlib, pytest and a lockfile-capable installer. Bayesian demo is a separate optional environment containing PyMC, the current compatible ArviZ statistics/base components and NetCDF support. Do not contaminate the small HW1 environment with JAGS/Stan/PyMC dependencies.

Freeze concrete dependency versions **after actual clean resolution**, using renv.lock and a Python lockfile with hashes where supported. Only released packages, no R-devel or a development documentation header used as a version pin. Selecting a compatible patch version and adapting changed argument names is an execution decision; changing model families or inferential targets is not.

### Evidence already available versus required next

The planning session ran an actual Python design pilot on NumPy 2.3.5, pandas 2.2.3, SciPy 1.17.0 and statsmodels 0.14.6. These are evidence versions, not an assertion that they are the latest versions in September 2026. Ordinary models and an independently coded scalar random-intercept likelihood ran; 60 versus 90 quadrature nodes agreed in the pilot. Two simulation scenarios with 500 replications each completed. R/lme4, the current PyMC/ArviZ environment, clean-machine builds and rendered PDFs have **not** been certified in this planning session. Codex must actually do those checks.

### Budgets and classroom mode

- Data validation and one ordinary model fit: target <=5 seconds on the recorded reference machine.
- One scalar GLMM fit: target <=30 seconds; otherwise load the precomputed fit in class and keep the real fit in the offline code.
- Complete HW1 core pipeline, excluding installation/PDF build: target <=10 minutes on a CPU laptop with 8 GB RAM; implementation validation ceiling 15 minutes, record hardware and timings. Failure of this target requires code/runtime optimization, not reducing the frozen replication count without review.
- Bayesian instructor run: offline, CPU, target <=15 minutes and 8 GB RAM; use cached results in class. Installation and compilation are never live teaching activities.
- Classroom live calls are limited to data checks, a Poisson fit, an NB fit, a nominal refit/reference change, and at most one pretested GLMM fit or a single simulation iteration. Full simulation and MCMC are precomputed.

If installation fails during class, display the checked HTML/PDF and cached numeric outputs while explaining the same equations. Do not switch estimators to whichever package happens to install. Students receive a tested R setup path, a startup script and the supplied R Question 3 runner before assessment work begins. A documented environment failure is handled as an access/support issue, not evidence of weak statistical understanding.

### Determinism

Frozen case CSVs are byte-authoritative. Do not regenerate them from a similar seed or a different RNG. Simulation streams use seeds in the student spec; identical seed integers across R and NumPy do not mean identical simulations. Cross-language comparisons must use the same stored response matrices. Preserve warnings, convergence flags, attempted replication counts and final valid denominators. Never retry a failed replication with a new random dataset until it succeeds.

## 6. Primary source register

All accessed 2026-09-28. URLs are durable project/documentation entry points; record package versions actually installed separately. Version metadata above is observational, not a substitute for an installation lock.

- W01 R GLM: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html
- W02 MASS glm.nb: https://stat.ethz.ch/R-manual/R-devel/library/MASS/html/glm.nb.html
- W03 nnet multinom: https://stat.ethz.ch/R-manual/R-devel/library/nnet/html/multinom.html
- W04 ordinal: https://cran.r-project.org/package=ordinal
- W05 lme4: https://lme4.github.io/lme4/reference/glmer.html and https://lme4.github.io/lme4/reference/predict.merMod.html
- W06 glmmTMB: https://glmmtmb.github.io/glmmTMB/reference/glmmTMB.html and https://glmmtmb.github.io/glmmTMB/reference/nbinom2.html
- W07 brms: https://paulbuerkner.com/brms/
- W08 CmdStanR: https://mc-stan.org/cmdstanr/
- W09 Stan diagnostics: https://mc-stan.org/learn-stan/diagnostics-warnings.html
- W10 PyMC: https://www.pymc.io/projects/docs/en/stable/api/generated/pymc.sample.html and https://www.pymc.io/projects/docs/en/stable/api/distributions/generated/pymc.NegativeBinomial.html
- W11 ArviZ: https://python.arviz.org/en/stable/ and https://python.arviz.org/projects/stats/en/stable/api/generated/arviz_stats.summary.html
- W12 statsmodels: https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.NegativeBinomial.html ; https://www.statsmodels.org/stable/generated/statsmodels.genmod.families.family.NegativeBinomial.html ; https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.MNLogit.html ; https://www.statsmodels.org/stable/mixed_glm.html
- W13 ordinary ordered regression: https://www.statsmodels.org/stable/examples/notebooks/generated/ordinal_regression.html
- W14 mclust: https://cran.r-project.org/package=mclust
- W15 flexmix: https://cran.r-project.org/package=flexmix
- W16 mice: https://cran.r-project.org/package=mice ; Python scope: https://www.statsmodels.org/stable/imputation.html
- W17 depmixS4: https://cran.r-project.org/package=depmixS4
- W18 hmmTMB: https://cran.r-project.org/package=hmmTMB ; associated primary methodology: Journal of Statistical Software 114(5), doi:10.18637/jss.v114.i05
- W19 hmmlearn: https://hmmlearn.readthedocs.io/en/stable/
- W20 sklearn mixtures: https://scikit-learn.org/stable/modules/mixture.html
- W21 R2jags: https://cran.r-project.org/package=R2jags
- W22 JAGS: https://mcmc-jags.sourceforge.io/
- W23 MRC Biostatistics Unit BUGS project: https://www.mrc-bsu.cam.ac.uk/software/bugs-project
- W24 Rcpp: https://www.rcpp.org/
- W25 TMB: https://cran.r-project.org/package=TMB
- W26 NumPy RNG: https://numpy.org/doc/stable/reference/random/generator.html
- W27 pandas: https://pandas.pydata.org/docs/
- W28 SciPy: https://docs.scipy.org/doc/scipy/reference/
- W29 Morris, White and Crowther (2019), Using simulation studies to evaluate statistical methods, Statistics in Medicine 38:2074–2102, doi:10.1002/sim.8086; open primary article: https://pmc.ncbi.nlm.nih.gov/articles/PMC6492164/

Do not add popularity claims, 'industry standard' rankings or unsupported maintenance judgments to the rendered note. This audit establishes reasonable current use and exact course roles, not a census of statistical practice.
