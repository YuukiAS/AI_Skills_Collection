# STAT5060 HW1 Student Specification V1

- Status: FROZEN_COMPLETE_ASSIGNMENT_CONTENT; administrative release fields and instructor policy adoption remain governed by `STAT5060_ASSESSMENT_AI_POLICY_V1.md`.
- Date: 2026-09-28.
- Source authority: newly authored assignment based on the supplied Chapters 1–3 and Tutorial 01; this replaces, rather than parameter-swaps, the old HW1.
- Relation: this file owns all student questions, required outputs, points, data definitions and seed rules. The rubric owns marking; the private solution owns worked reasoning and expected results. A PDF builder must include the exact student-facing AI policy block from the assessment policy. It is a deterministic inclusion, not permission to rewrite policy.

---

# STAT5060 — Advanced Modeling and Data Analysis
## Assignment 1: When the fitted mean is not the whole analysis

**Weight:** 20% of the course. **Total:** 100 assignment points.

**Due:** [INSTRUCTOR TO INSERT: date, time and timezone; use HKT unless explicitly announced otherwise].

**Submit via:** [INSTRUCTOR TO INSERT: official submission location and academic-honesty declaration/VeriGuide instructions].

### Purpose and scope

A learning-support service is reviewing participation patterns. You will study the rate of support requests, preferred contact channels and repeated weekly participation. The central questions are not only whether software can fit a model, but whether the response distribution, exposure, dependence structure, uncertainty and interpretation match the question.

By completing this assignment you should be able to formulate and compare count models; interpret nominal-response probabilities without confusing them with reference logits; distinguish conditional and population-averaged predictions in a random-intercept model; and evaluate uncertainty calibration in a reproducible simulation.

The supplied data are **newly generated synthetic teaching data**, not records of real students or an empirical evaluation of a CUHK service. The reminder indicator should be treated as an observational group variable for interpretation: no randomized causal study is asserted. Do not infer real educational benefits or harms from this dataset.

### Files and data dictionary

Use the supplied CSVs unchanged. Do not regenerate them, delete inconvenient observations or choose a different random seed for these case datasets.

**`hw1_participants.csv`** contains 600 participants, one row each:

| Variable | Meaning |
|---|---|
| participant_id | Unique participant identifier; not a numerical predictor. |
| reminder | 0=no reminder programme, 1=reminder programme. |
| proficiency | A dimensionless baseline proficiency score, approximately between -1 and 1. Use the supplied scale. |
| exposure_weeks | Positive duration over which support requests were counted. |
| requests | Number of support requests during that exposure; multiple requests per week are possible. |
| preferred_channel | One separately elicited preference: online, workshop or drop_in. These are unordered categories. |

**`hw1_weekly.csv`** contains 2,400 observations, four weeks (0,1,2,3) per participant: participant_id, week, reminder, proficiency and active. `active` is 1 if the participant was active that week, otherwise 0. This weekly panel has its own fixed observation window; `exposure_weeks` in the request-count dataset is not an offset for this binary response.

The files are complete by design. Verify this rather than silently imputing or dropping rows. The supplied data manifest records SHA-256 hashes. Both files and their dictionary may be redistributed as original synthetic teaching data under CC0.

### Languages, setup and supplied support

You may use **R for the entire assignment**, or Python for Questions 1, 2 and 4 together with the supplied R script for the mixed-model work in Question 3. The reference R packages are stats, MASS, nnet and lme4. The optional Python route uses NumPy, pandas, SciPy and statsmodels. Plotting may use base R, ggplot2 or Matplotlib. No marks depend on a particular plotting style or on the length of your code.

For Question 3, a tested R runner and helpers for new-participant probability integration and simulated panel checks are supplied. Python users may invoke that runner and read its CSV outputs; implementing a Python–R bridge or numerical quadrature is not assessed. A Bayesian/VB mixed-model fit, GEE or cluster-robust ordinary logistic regression is not an equivalent replacement for the required maximum-likelihood random-intercept fit. A demonstrably equivalent likelihood-based implementation is acceptable if you document the same model and prediction targets, but no unfamiliar implementation is required.

Bayesian coding is **not required**. You do not need PyMC, Stan, JAGS, WinBUGS, Rcpp or TMB to complete HW1.

### Submission and reproducibility

Submit a PDF report of at most eight main-body pages, plus references, the AI-use statement and an optional code appendix. Submit executable source files or a Quarto/R Markdown/Jupyter project, not screenshots of code. All required statistical reasoning and requested tables/figures should be in the report; a console dump is not a substitute for interpretation.

Include a README with one command or a short exact command sequence that reproduces your results from the supplied CSVs, package/session information, and relative file paths. Keep generated tables/figures in an `outputs/` directory. Include warnings and convergence/failure summaries where requested. Do not submit virtual environments, package libraries, raw AI chat histories or unrelated files. Do not fabricate a check that was not performed.

Use the specified seeds for simulation and panel checks. Different R/Python random-number generators need not produce identical values from the same seed; report your language and versions. Your analysis and conclusions must be internally reproducible. Numerical results will be assessed with appropriate numerical/Monte Carlo tolerances rather than an exact-match answer string.

Expected workload with the supplied starter files: **approximately 11–15 hours**, including interpretation and report preparation. This is a planning estimate, not a timed requirement.

### Generative AI and academic honesty

[BUILD DIRECTIVE — NOT PRINTED: insert the complete canonical block under “Student-facing AI policy — canonical English text” from `STAT5060_ASSESSMENT_AI_POLICY_V1.md`, preserving all paragraphs. Include the instructor-adopted policy in the final student PDF. Do not leave this directive or replace the block with an unexplained link.]

## Question 1 — Requests: exposure, variation and model choice (30 points)

Let Y_i be `requests`, e_i be `exposure_weeks`, A_i be `reminder` and z_i be `proficiency`. For the NB2 model use the convention E(Y_i|A_i,z_i,e_i)=mu_i and Var(Y_i|A_i,z_i,e_i)=mu_i+mu_i^2/kappa, kappa>0. Estimate kappa; do not fix an arbitrary package default.

**1(a) Data and model formulation — 6 points.** Verify the number of participants, uniqueness of IDs, missingness, integer nonnegative counts and positive exposure. Give the sample mean and variance of requests and the exposure range. Write a log-link rate model using reminder and proficiency and explain the offset, its coefficient and its units. State the conditional independence/mean assumptions. Explain why the raw sample variance being larger than the raw mean is not, by itself, a decisive test of a conditional Poisson model.

**1(b) Fit two candidate models — 6 points.** Fit Poisson and NB2 models with identical mean predictors, offset and observations. In one compact table report the intercept and two slope estimates, their model-based SEs, AIC, and NB2 shape kappa. For each model report exp(beta_A) and its 95% Wald interval exp(beta_A±1.959964 SE(beta_A)). Label the rate-ratio interpretation and the interval method. State your software's dispersion convention and any conversion used.

**1(c) Diagnostic evidence — 8 points.** For each model calculate Pearson residuals and D=sum_i r_i^2/(n-p), where p=3 is the number of mean coefficients. Treat D as a descriptive check, not an exact hypothesis test. Plot Pearson residuals against fitted means separately for the two models. Report the observed zero proportion and each model's average fitted probability of zero. Use these diagnostics and a same-data AIC comparison to explain what each candidate captures or misses. Do not choose a model using only a p-value or only the fact that it has more parameters.

**1(d) Exposure sensitivity — 6 points.** Refit the NB2 model after deliberately omitting the exposure offset, with the same other predictors and observations. Compare the reminder coefficients/rate interpretations from the two fits. Explain why the comparison matters in this dataset and why overdispersion modeling does not itself adjust for unequal exposure. State your recommended analysis and one remaining limitation; distinguish evidence from a conclusion forced by a package name.

**1(e) A concrete prediction — 4 points.** Using the NB2 model with offset, predict expected requests over **eight weeks** for proficiency=0 with reminder=0 and reminder=1. Give the predicted count difference and ratio. Explain which quantity is an expected count, which is a rate ratio, and why these predictions do not establish that reminders cause improved learning.

## Question 2 — Preferred channel: probabilities and reference categories (18 points)

Use preferred_channel as an **unordered** response, with predictors reminder and proficiency. Start with **online as the reference category**. Fit an unpenalized multinomial-logit model with an intercept in each non-reference equation.

**2(a) Formulate and fit — 5 points.** Write the two reference-logit equations and identify their parameters. Report the two coefficient vectors with SEs, making category order and reference explicit. Do not encode the three channels as a numerical ordinal score.

**2(b) Answer a probability question — 7 points.** Calculate the three fitted probabilities at proficiency=0 for reminder=0 and reminder=1. Show the softmax calculation for at least one of these two profiles using the fitted linear predictors. Plot the three channel probabilities over proficiency from -1 to 1, separately for the two reminder groups. Explain one substantive contrast using probabilities, and explain why a coefficient for a reference logit is not a constant change in a channel's absolute probability.

**2(c) Change the reference — 4 points.** Refit using **workshop as reference**. Show the algebra that transforms the old coefficient vectors into the new ones. Compare fitted probabilities after aligning category labels, and report their maximum absolute difference over the 600 observed covariate rows. Explain why the probabilities should agree up to numerical error even though coefficients change.

**2(d) Connect the questions — 2 points.** Explain why exp of a reminder coefficient in Question 1 and exp of a reminder coefficient in Question 2 answer different questions, even though both models use a log-type link. Use the actual outcome and denominator in each explanation.

## Question 3 — Weekly activity: dependence and prediction targets (25 points)

Use the four-week panel. Treat week as the numerical values 0,1,2,3 and use reminder and proficiency on the supplied scales. Do not add an exposure offset to this binary model.

**3(a) Formulate the dependence — 6 points.** State the observational and clustering units. Write (i) a naive ordinary logistic model and (ii) a logistic random-intercept model with b_i~N(0,sigma_b^2). State conditional independence and the independent-subject assumption. Write the observed-data likelihood for the random-intercept model, showing a product over a participant's weeks **inside one integral over that participant's random effect**.

**3(b) Fit and check — 7 points.** Fit the naive model and the random-intercept model by maximum likelihood. The reference mixed fit is `lme4::glmer` with one random intercept, nAGQ=9 and the supplied tested control settings. Report fixed-effect estimates/SEs, random-intercept SD, convergence warnings and singularity status. Use the supplied helper to simulate 200 complete panels from each fitted model with seed **50602027**: the naive model uses independent Bernoulli draws; the mixed model draws one new random intercept per participant. Plot the observed number of participants with 0,1,2,3,4 active weeks against each model's simulated mean and 5th–95th percentile envelope. Interpret a feature of this check. These plug-in envelopes do not include parameter-estimation uncertainty and are not formal confidence bands.

**3(c) Predict for a new participant — 8 points.** At proficiency=0, consider four profiles: reminder/week=(0,0),(0,3),(1,0),(1,3). In one table report the naive-model probability; the mixed-model probability conditional on b=0; and the mixed-model probability for a new participant after integrating over b~N(0,sigma_hat_b^2). Use the supplied integration helper rather than writing quadrature. Explain why setting b=0 is not the same as averaging over the random-effect distribution. Interpret exp(beta_A) from the mixed model as a conditional odds ratio, not as a population risk ratio.

**3(d) Compare responsibly — 4 points.** Discuss why the naive and mixed-model reminder coefficients need not agree. Explain why their difference alone does not establish a bias comparison for an identical parameter. Identify one remaining modeling assumption or limitation relevant to the weekly data and say what evidence would make you reconsider it.

## Question 4 — Can a larger sample repair misspecified uncertainty? (22 points)

This simulation asks a focused statistical question: a Poisson regression has the correct mean form but the wrong conditional variance. Does increasing n alone make its conventional model-based confidence interval reliable, and how does a fitted NB2 model compare?

For each n in **{100,400}**, fix x_i to n equally spaced points from -1 to 1. Generate independent observations with

mu_i=exp(0.5+0.5*x_i), Y_i~NB2(mu_i,kappa=1.5).

The true slope is beta1=0.5. There is no exposure offset, missingness or random effect in this simulation. Perform **B=500 attempted replications per n**. For n=100 use seed **5060401**; for n=400 use seed **5060402**. In R use Mersenne-Twister/Inversion/Rejection and set the seed once per scenario. In Python use a NumPy Generator with PCG64 and set it once per scenario. At every replication fit both methods to the **same generated response vector**. Use an intercept and x in both models. Estimate NB2 shape rather than supplying its true value to the fit.

For both fits construct a 95% model-based Wald interval beta1_hat±1.95996398454 SE_hat. Do not substitute sandwich SEs, bootstrap intervals, known-shape NB or Bayesian credible intervals for this specified comparison. Such methods can be discussed as possible extensions, but they do not replace the experiment.

**4(a) State the experiment — 4 points.** Identify the aim, data-generating mechanism, target parameter, methods and performance measures. State a reasoned expectation for bias, uncertainty and coverage, and distinguish increasing n from increasing B. Assess the statistical expectation, not whether your first guess happened to match every realized number.

**4(b) Implement fairly — 5 points.** Use the supplied annotated loop structure, completing the model calls and required summaries. Keep one record per attempted replication per method. Record convergence warnings, any bounded refit on the **same data**, and final validity. A valid fit has converged and has finite coefficient and positive finite SE; NB shape must also be positive and finite. Do not silently drop failures or generate replacement datasets until a method succeeds. Report attempted and valid counts. A warning that is resolved by a documented same-data refit is not automatically a final failed replication.

**4(c) Measure performance — 7 points.** For each n/method report bias, RMSE, empirical SE, RMS reported SE, empirical coverage and the Monte Carlo SE of coverage, together with valid-fit counts. Use the following definitions over B_v valid fits:

- Bias = mean(beta1_hat)-0.5.
- RMSE = sqrt(mean((beta1_hat-0.5)^2)).
- Empirical SE = sample SD of beta1_hat, using denominator B_v-1.
- RMS reported SE = sqrt(mean(SE_hat^2)).
- Coverage = mean[lower<=0.5<=upper].
- Coverage MCSE = sqrt(coverage*(1-coverage)/B_v).

If final failures occur, clearly state that this coverage is conditional on a valid fit and also report `number of valid-and-covering fits / 500`. Explain why B=500 gives a more informative calibration assessment than B=10; a calculation near nominal 0.95 coverage is sufficient.

**4(d) Answer the question — 6 points.** Plot coverage against n for both methods, include a 0.95 reference, and display approximate Monte Carlo error bars of ±1.96 MCSE (bounded to [0,1]). Interpret bias/RMSE jointly with empirical versus reported SE and coverage. Does larger n alone fix the Poisson variance misspecification? Distinguish a meaningful calibration failure from a small Monte Carlo fluctuation. Do not claim that NB must have smaller realized RMSE in every scenario or exactly 95% realized coverage.

## Reproducibility, communication and disclosure (5 points)

Two points concern a runnable end-to-end analysis; one concerns unchanged data, seeds, session/dependency information and warnings; one concerns clear, labeled and appropriately concise tables/figures/report; one concerns the required AI-use statement. Statistical interpretation is mainly marked within Questions 1–4, not reduced to these five process points.

### Output checklist

Your report should contain the data/model audit; count-model coefficient/diagnostic table, two residual plots and exposure sensitivity/profile predictions; nominal coefficients, profile probabilities, probability curves and reference-invariance check; mixed-model comparison, convergence/model-check evidence and the four-profile prediction table; simulation performance table, failure counts, coverage plot and an evidence-based conclusion. Label every response, reference category, interval type and relevant unit.

Your source submission should reproduce these outputs, preserve the supplied CSVs, record its seed/environment and show where AI/external code was used and verified. You are not required to submit an implementation of a sampler, quadrature algorithm or numerical optimizer.
