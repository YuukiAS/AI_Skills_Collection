# STAT5060 Tutorial 01 Frozen Specification V1

- Status: FROZEN_90_MINUTE_CONTENT_FOR_MATERIALIZATION.
- Date: 2026-09-28.
- Source authority: supplied Chapters 1–3, old Tutorial/HW1, the canonical knowledge corrections and current official software audit. The cases below are newly authored synthetic teaching cases, not original lecture datasets.
- Relation: owns timing, instructional content, slide/note sequence, case files and classroom execution. `STAT5060_HW1_STUDENT_SPEC_V1.md` owns assessed tasks; the alignment file maps every task. Bayesian model details and implementation constraints are owned by the software policy.

## 1. Frozen teaching decision

Title: **From a fitted model to a defensible analysis: a campus equipment reliability case**.

Audience: students who have encountered basic GLMs and likelihood; the repeated-measures block explicitly introduces the scalar random-intercept formulation rather than assuming familiarity with a new package. Deliver Tutorial 1 before HW1 work is due, and provide the two-page random-intercept bridge described below if Chapter 3 has not yet been lectured. The 20-minute repeated-measures block plus its worksheet is the actual explanatory bridge; no separately produced video is required. Do not infer this year's lecture progress from last year's PDF timestamps.

One narrative, three questions. Facilities staff ask: how frequently does a device generate faults at equal operating exposure; which type of issue is found at a separate inspection; and how do repeated weekly alarms vary within the same device? The inspection is a separate observation, so 'none' is not mechanically derived from the fault count. Service status is observational in this teaching story; do not call its fitted association a randomized causal effect.

### Case selection decision

Crab counts are valuable for Poisson/NB intuition; alligator choices demonstrate relative logits versus absolute probabilities; wheeze and insomnia illustrate repeated outcomes. Keep those examples in the whole-course review, not as four disconnected datasets in 90 minutes. The old wheeze table has a pattern-label problem, insomnia requires an additional ordinal API/sign lesson, and neither solves the data-distribution/rights problem as neatly as newly authored fixtures. The frozen replacement is a connected synthetic case with controlled complexity, explicit provenance and no external download during class. Do not claim synthetic results describe real CUHK equipment.

### Data and roles

`tutorial_devices.csv`: 240 devices, columns device_id, load (dimensionless, -1 to 1), service (0/1), exposure_100h (>0), faults (nonnegative integer), inspection (none/mechanical/electronic). `tutorial_alarms.csv`: 960 records, four weeks 0–3 per device, columns device_id, week, load, service, alarm (0/1).

Use the byte-frozen fixture files in the private execution handoff. Their source is original synthetic teaching design; redistribution of these CSVs is permitted under CC0. Do not regenerate them from a similar RNG seed. Hashes are in the source inventory/release manifest.

R is live/reference. Python frequentist counterparts are runnable take-home files. PyMC appears only in the ten-minute instructor Bayesian workflow demo. No mandatory brms/Stan/JAGS installation and no ordinal live coding.

## 2. Minute-by-minute plan and exact slide sequence

This table is the complete 90-minute schedule. Durations sum to 90; transitions and questions are included, not added afterwards. Use 24 content slides, with any title/contents incorporated into slide 01. The slide titles below are the required student-facing section titles. No appendix is presented live unless a later block finishes early; do not displace HW1 preparation to show another package.

| Slide | Minutes | Student-facing title | Teaching action / intended output |
|---|---:|---|---|
| 01 | 0–2 | Three questions, one analysis workflow | State fault rate, inspection choice and repeated alarm questions; show question→data→model→fit→check→interpret→revise. |
| 02 | 2–5 | What does one row represent? | Display six device rows and one device's four weekly rows; identify units, exposure and response type. |
| 03 | 5–8 | Counts are not rates | Plot faults versus exposure and load; ask why a large raw variance does not settle conditional overdispersion. |
| 04 | 8–12 | A Poisson rate model | Write log(mu)=log(exposure)+beta0+betaS service+betaL load; one manual equal-exposure prediction and the offset's fixed coefficient. |
| 05 | 12–16 | Fit, then check the variance | Live Poisson fit; display beta/SE and Pearson residuals; calculate descriptive Pearson dispersion. |
| 06 | 16–20 | Negative binomial: same mean, more variation | Introduce NB2 variance mu+mu^2/kappa; live glm.nb; explain the inverse-dispersion parameter. |
| 07 | 20–24 | Use evidence, not a package preference | Compare residual pattern, observed/fitted zeros and AIC on identical rows; discuss what NB does not establish. |
| 08 | 24–28 | A rate ratio is not a probability or a cause | Equal-exposure predictions and rate-ratio interval; two-minute student explanation: coefficients can look similar while uncertainty changes. Transition to a different response type. |
| 09 | 28–31 | Inspection categories have no order | Show category frequencies and name 'none' as the reference; explain why ordinal scoring is inappropriate. |
| 10 | 31–35 | Reference logits and predicted probabilities | Write two reference logits and the three-category softmax; manually calculate one profile's probabilities. |
| 11 | 35–39 | Plot the probabilities people actually ask for | Run multinom and display probability curves over load for service 0 and 1. Discuss changing denominator terms. |
| 12 | 39–43 | Changing the reference does not change the model | Relevel to mechanical, refit, reorder probability columns and verify invariance. One student explains why coefficients change. |
| 13 | 43–46 | Four rows are still one device | Show weekly panel and device totals; ask why independent rows are not independent devices. |
| 14 | 46–50 | A shared random intercept | Contrast naive logit and logit(p_it|b_i)=beta0+betaS service_i+betaW week+betaL load_i+b_i, b_i~N(0,sigma_b^2). |
| 15 | 50–54 | Integrate shared variation when fitting | Show product-over-visits inside one integral per device; run or load the pretested scalar-RI glmer fit; display convergence and SD. |
| 16 | 54–59 | A typical random effect is not an average probability | Compare b=0 prediction with integral expit(eta+b)phi(b)db at four profiles; use supplied integration helper. |
| 17 | 59–63 | Does the model reproduce device patterns? | Display observed 0–4 alarm totals against plug-in simulated panels from naive and RI models; explain envelope limitations. One-minute exit question about conditional versus marginal interpretation. |
| 18 | 63–66 | Simulation asks a repeated-sample question | Define the tutorial's correct-variance versus wrong-variance experiment; distinguish n observations from B replications. |
| 19 | 66–70 | One dataset, one fit, then repetition | Run one iteration and show saved estimates/SE/CI flags; expand the same operation to B=500 without waiting live. |
| 20 | 70–74 | Bias, precision and coverage are different | Define bias, RMSE, empirical SE, RMS reported SE, coverage and coverage MCSE. Display precomputed summary and interval-coverage plot. |
| 21 | 74–77 | More data do not automatically fix a wrong variance | Interpret Poisson-true versus NB-true calibration; ask students to predict what increasing n or fitting NB might change in HW1. |
| 22 | 77–79 | The same count model, with explicit priors | Show compact PyMC model declaration for the same NB2 device case and named priors. |
| 23 | 79–84 | Sampling is not the end of analysis | Two minutes on prior predictive output and posterior sampling; three minutes on four-chain R-hat, bulk/tail ESS, MCSE and divergences using cached checked output. |
| 24 | 84–90 | Check predictions; prepare a reproducible submission | 84–87: posterior predictive zeros/tails and brms→Stan/PyMC architecture mapping. 87–89: HW1 outputs, seeds, R/Python route and reproducibility. 89–90: AI policy and final one-sentence evidence-based conclusion. |

The last slide has explicitly timed subpanels so the Bayesian workflow ends at 87 minutes and the final three minutes remain protected. Place the full assignment/policy instructions in the handout; do not try to read them aloud in three minutes.

## 3. Count block: complete content contract (0–28)

**Learning objective:** distinguish a conditional count mean from its variance and exposure; justify Poisson versus NB using evidence; interpret rates at a fixed exposure.

**Model/equations:** Y_i~Poisson(mu_i), log(mu_i)=log(e_i)+beta0+betaS S_i+betaL L_i. NB2 retains this mean and replaces variance by mu_i+mu_i^2/kappa. Pearson residual r_i=(y_i-mu_hat_i)/sqrt(V_hat_i); descriptive dispersion D=sum r_i^2/(n-p), with p the number of mean coefficients (3 here). It is approximate and not presented as a formal p-value.

**Figures/tables:** F01 faults versus exposure with load shown or a separate load plot; F02 Pearson residual versus fitted mean, one clearly labeled plot per model; F03 observed zero proportion versus each fitted mean zero probability and a simple count-frequency/tail comparison. Table T01 has model, betaS, betaL, SEs, rate-ratio intervals, shape, AIC and D. No screenshot of an entire console summary.

**Live code intent:** validate integer counts and positive exposure; `glm(faults ~ service + load + offset(log(exposure_100h)), poisson, data=d)`; `MASS::glm.nb` with identical formula/rows; compute fitted zero probabilities using dpois/dnbinom; plot residuals; predict at exposure_100h=1, load=0, service 0/1. Derive 95% Wald rate-ratio intervals as exp(beta±1.959964 SE), explicitly labeled Wald.

**Instructor expected behavior, already checked in a Python design pilot:** observed zero proportion about .379; Poisson predicts .216 and NB .396. Poisson D about 3.02 versus NB about 1.11. AIC about 992.57 versus 831.20. NB shape about .995. NB service coefficient about -.324, load .278; point estimates need not equal generator parameters in one sample. R output is to be run and verified, not invented from this pilot.

**Talking points:** the offset's units set the rate unit; NB changes variance, not the scientific question; more zeros than a Poisson fit predicts does not by itself identify a structural zero class; a substantially better descriptive fit still needs a scientifically plausible mean.

**Expected confusion:** raw variance>raw mean as a decisive test; interpreting kappa as a variance increasing with kappa; treating exp(beta) as a risk ratio; removing the offset because it is not 'significant'; inferring causality from service status.

**Transition:** an inspection label is neither an event count nor an ordered score. The question stays practical, but the response distribution must change.

**HW1 transfer:** Q1 uses a different context and exposure associated with the group variable, so students must diagnose omission of exposure rather than copy a preferred model choice.

## 4. Nominal block: complete content contract (28–43)

**Objective/case:** model inspection=none/mechanical/electronic and explain reference logits through absolute probabilities.

**Equations:** with none as baseline, eta_M=beta_M0+beta_MS S+beta_ML L and eta_E analogously; p_none=1/(1+exp eta_M+exp eta_E), p_M=exp eta_M*p_none, p_E=exp eta_E*p_none. Re-reference to mechanical by subtracting beta_M from every old coefficient vector, treating beta_none=0.

**Figures/tables:** F04 three probability curves over load at each service level (separate plots, common axes); T02 one row per category at load=0/service=0 and 1; a tiny reference-change check with maximum absolute probability difference. Do not show a coefficient forest without stating its reference.

**Code intent:** factor levels explicitly none, mechanical, electronic; `nnet::multinom(...,Hess=TRUE,trace=FALSE,decay=0,maxit=1000)`; predict(type='probs'); relevel to mechanical and refit; align category columns before maximum difference. Equivalent statsmodels example goes in the take-home file.

**Talking points/expected results:** at load=0, service=0, pilot probabilities are approximately (.236,.460,.303), and at service=1 (.266,.464,.270), in none/mechanical/electronic order. A category's absolute probability depends on every logit. Reference change alters coordinates, not fitted probabilities.

**Confusions:** first factor level versus last category in the lecture; interpreting a coefficient as a probability change; sorting category labels before comparing without preserving identities.

**Transition:** the inspection model used one row per device. Weekly alarms reuse a device; the independence assumption must now be reconsidered.

**HW1 transfer:** Q2 requires a new substantive reference category, manual probabilities, a reference-change identity and comparison with a different response's coefficient meaning.

## 5. Repeated binary block: complete content contract (43–63)

**Objective:** identify clustering, formulate the integrated likelihood, fit one RI GLMM, separate conditional and new-subject predictions and examine within-device outcome patterns.

**Equations:** naive logit(p_it)=x_it^T beta; conditional logit(p_it|b_i)=x_it^T beta+b_i, b_i~N(0,sigma_b^2). L(beta,sigma_b)=product_i integral product_t Bern(y_it;expit(x_it^T beta+b))phi(b;0,sigma_b^2)db. Shared b appears once per device in an entire visit product.

**Figures/tables:** F05 a four-visit panel diagram/data snippet; T03 naive and GLMM coefficients/SE, RI SD and convergence; F06 four-profile b=0 versus integrated probability comparison; F07 observed device alarm totals 0–4 versus plug-in predictive panel summaries from each model.

**Code intent:** naive `glm(alarm ~ service + week + load,binomial)`; RI `lme4::glmer(alarm ~ service + week + load + (1|device_id),binomial,nAGQ=9,control=glmerControl(optimizer='bobyqa',optCtrl=list(maxfun=200000)))`. Device ID is a grouping factor, not a numeric slope. Inspect fit warnings, gradient information and `isSingular`. No variance-component chi-square significance test is required.

Provide a base-R helper for a new device: when sd>0, numerically integrate `plogis(eta+b)*dnorm(b,0,sd)` over the real line with relative tolerance 1e-9; when sd=0 return plogis(eta). Students do not write quadrature. State explicitly that `predict(...,re.form=NA)` gives b=0, not the integral.

Provide a panel-check helper: conditional on fitted parameters, simulate 200 complete panels using the observed design; naive model draws independent Bernoulli outcomes, RI model draws one new b per device and then all its Bernoulli outcomes. For each simulated panel count devices with 0,1,2,3,4 alarms. Show mean simulated frequency and 5th–95th percentile envelope, with observed frequencies. Label this a **plug-in model check**, not a parameter-uncertainty confidence band or a formal test.

**Expected behavior:** scalar-RE design pilot gave SD about 1.138 and conditional service coefficient about -.675; naive service coefficient about -.551. At service=0/week=0/load=0, b=0 probability about .319 versus integrated .354. These differences illustrate averaging through a nonlinear link, not a proof that the naive coefficient estimates the same target with bias. Observed alarm totals are 74,65,52,37,12 for 0–4 alarms.

**Confusions:** four visits as four independent subjects; RI variance as variance of a probability; sigma versus sigma squared; b=0 called population average; posterior/VB mixed fits called identical to ML.

**Transition/HW1:** once one dataset yields different uncertainties or targets, ask how procedures behave across many newly generated datasets. Q3 preserves the RI structure but changes the scientific context, profile questions and diagnosis.

### Two-page bridge handout (fixed content)

Page 1: one person/device with four rows; naive and RI equations; verbal meaning of shared b; conditional independence versus marginal dependence; integrated likelihood with one integral per subject. Page 2: conditional OR, b=0 probability, new-subject integral, numerical helper call and the warning that different targets should not be compared as if they were the same coefficient. Include one worked tutorial profile and one blank HW-style profile. No new theory beyond this block.

## 6. Simulation block: complete content contract (63–77)

**Objective:** evaluate a confidence-interval procedure, not merely reproduce a parameter estimate. Explain Monte Carlo precision and distinguish a data sample size from a simulation replication count.

**Tutorial experiment:** n=100, x_i equally spaced from -1 to 1, mu_i=exp(.5+.5*x_i), true beta1=.5. Scenario T-P: independent Poisson(mu_i). Scenario T-NB: independent NB2(mu_i,kappa=1.5). Fit only a Poisson log-link model in this tutorial experiment. B=500 per scenario, R seeds 5060301 and 5060302, respectively. The class runs one iteration; all repeated results are cached. This compares a correct versus incorrect variance assumption. HW1 intentionally extends it by estimating NB and varying n, rather than rerunning the same comparison with a new seed.

For B_v valid estimates, bias=mean(beta_hat)-beta1; RMSE=sqrt(mean((beta_hat-beta1)^2)); empirical SE is sample SD with denominator B_v-1; RMS reported SE=sqrt(mean(SE_hat^2)); coverage=mean[lower<=beta1<=upper], with model-based Wald interval beta_hat±1.959964 SE_hat; coverage MCSE=sqrt(c_hat(1-c_hat)/B_v). Bias MCSE is empirical SE/sqrt(B_v). Explain that Monte Carlo randomness affects the estimated coverage too.

**Figure/table:** F08 coverage and approximate Monte Carlo uncertainty for T-P/T-NB, 0.95 reference; T04 bias/RMSE/empirical SE/RMS SE/coverage/MCSE/valid counts. No claim of exactly 95% coverage in a finite simulation. Emphasize that NB-truth/Poisson-fit can retain a sensible mean estimate while the reported SE is too small.

**Code intent:** an annotated `simulate_one` function returns beta, SE, interval, covered, convergence and warning record; a supplied loop preserves every attempted replication and never resamples a failed dataset. Stop on code bugs, do not hide failed fits as missing rows. Use the same stored responses for language equivalence checks.

**Confusions:** B=500 makes each dataset larger; RMSE and SE are identical; empirical coverage should equal exactly .95; a small bias implies valid intervals; retrying new data until a method converges is harmless.

**Transition:** simulation investigates a procedure across datasets. Bayesian diagnostics instead investigate computational quality and model predictions for a posterior conditional on the observed dataset.

## 7. Bayesian workflow block: complete content contract (77–87)

The exact NB2 device model, priors, seeds, chains, draws and diagnostic targets are frozen in the software policy. Display no more than a compact model-declaration snippet plus a sampling call. Interpret the output rather than reading library arguments.

**Required visuals:** a prior predictive count/zero summary; a small posterior table with means/SD/95% credible intervals and unrounded diagnostics used for checking; posterior-predictive zero and tail checks. Trace/rank plots are included in the appendix and shown only if needed to explain a warning. Four-chain R-hat close to one and adequate ESS do not prove the likelihood fits; zero divergences does not establish scientific validity. Posterior predictive checks concern model-data discrepancies, not sampler convergence.

**Language mapping:** PyMC declares a model directly. brms supplies a higher-level R formula interface to Stan. CmdStanR connects R to CmdStan. These are different interface layers, not three competing distributions. The brms counterpart is an appendix, not another live lesson.

**Take-home:** declare assumptions and priors, compute, check computation, check replicated data, then interpret. **No Bayesian coding is required in HW1.**

## 8. Final three minutes and student materials

87–89 minutes: show the four HW tasks and one-page output checklist; R-only versus Python-plus-R-runner option; fixed datasets/seeds; code/output paths and session information. 89–90: allowed-with-disclosure AI rule after instructor adoption, no full prompt log and personal responsibility; ask: 'What evidence would make you revise your first fitted model?'

Required deliverables: 24-slide 16:9 PDF and editable Quarto source; student notes with the exact section order/equations/plot interpretations above; two-page RI bridge; R scripts; optional Python ordinary-model/simulation scripts; instructor-only PyMC run and cached reproducible outputs; data dictionary; dependency/setup page; AI policy inclusion and HW1 link. Student notes target 10–14 A4 pages, not a dump of slide bullets. Each section ends with the take-home message already stated in this spec.

### File-level code contract

- `R/01_count.R`: data checks, Poisson/NB, diagnostics, profile predictions and saved tables/figures.
- `R/02_nominal.R`: explicit categories, multinom, probability profiles/curves and reference-invariance assertion.
- `R/03_repeated_binary.R`: naive/RI fits, convergence, integrated predictions and 200-panel diagnostic; seed 5060105 for panel simulations.
- `R/04_simulation.R`: the two n=100 tutorial scenarios, B=500, complete attempt/warning records.
- `python/01_count_nominal.py`: same frozen rows/designs for optional ML equivalence.
- `python/02_simulation.py`: same experiment, independently seeded for learning; read shared response matrices for strict equivalence tests.
- `python/03_bayesian_demo.py`: the frozen PyMC model, cached draws/diagnostics/PPC, no external API.
- `R/helpers.R`: base-R new-subject probability integration and panel-check helper, with tests; not an assessed programming trick.

Full execution budgets, lockfile rules and installation fallback are in the software policy. Any live call exceeding its tested budget is replaced by its validated cached result, not by a different model. The original CSVs and all generated output provenance must remain visible in the classroom package.
