# STAT5060 Canonical Knowledge V1

- Status: FROZEN_CONTENT_FOR_CODEX; not a claim that PDFs or clean-environment builds have passed.
- Date: 2026-09-28.
- Source authority: Chapter1–9.pdf, Chapter3_Supplement.pdf and the old assessment/tutorial corpus inventoried in `STAT5060_SOURCE_INVENTORY_V1.md`; roadmap commit `9d1923d2002c529352ad6464599e7da08eb6787c`.
- Relation: this file owns statistical meaning, notation, source corrections and the complete internal review-note content. Software choices are owned by `STAT5060_SOFTWARE_WORKFLOW_POLICY_V1.md`; assessed scope by the Tutorial/HW1 specifications. Codex may typeset and cross-link this content, not replace its teaching decisions.

## 0. How to read and render this note

The course connects three questions: what distribution describes an outcome; what unobserved structure makes observations dependent or heterogeneous; and what can actually be learned when outcomes, membership or mechanisms are partly unobserved. Chapters 1–3 supply estimation and outcome-model foundations. Chapters 4–7 extend these foundations to multilevel structure, mixtures, missingness and changing latent states. Chapters 8–9 join measurement, longitudinal processes and event times. A more elaborate likelihood does not automatically identify its scientific interpretation.

This is newly written review content, not a transcription of lecture slides. Source page references below mean **physical, one-based PDF pages**, not slide-footer numbers. Do not insert original slide images, copied textbook paragraphs or patient data into the derived note.

Three explicit labels must survive PDF rendering:

- **SOURCE COURSE CONTENT (S):** a method or problem actually present in the supplied course.
- **MODERNIZATION / EXTERNAL BEST PRACTICE (M):** present-day diagnostics, implementation and qualifications added here; primary documentation is catalogued in the software policy.
- **OUR PEDAGOGICAL REORGANIZATION (P):** this note's explanatory order, examples and selected Tutorial/HW scope.

Corrections have a fourth label, **CORRECTION (C)**: the original expression remains locatable in the errata table, while the corrected expression is used in teaching. A correction is not silently attributed to the original lecturer.

### Model-card coverage contract

Each card below supplies these 16 fields, grouped to avoid an unreadable 16-column table: (1) data problem, (2) intuition, (3) mathematical form, (4) parameters; (5) assumptions and (6) identification; (7) estimation/inference and (8) computational mechanism; (9) diagnostics; (10) interpretation and (11) failure modes; (12) R and (13) Python routes; (14) chapter connections; (15) aging/source limitations and (16) additions. Chapter-level shared qualifications apply to each card in that chapter. Do not interpret an inherited computational route as a claim that every special model has a turnkey package.

### Polished PDF contract

Render a Chinese instructor-facing review, retaining English method names and code identifiers. Title: **STAT5060：从观测模型到潜在结构——整门课复习笔记**. Target 28–36 A4 pages, with legible mathematics taking precedence over exact page count. Use 11-point body text, approximately 1.15–1.25 line spacing, 20–22 mm margins, bookmarks, page numbers and a linked contents page. No dense landscape mega-tables. Short equations inline; display only the models and identities needed for comparison. Use the same nine reader-facing section labels within each chapter: 为什么需要；场景；模型与参数；估计；诊断；解释；容易出错的地方；现代实现；与其他章节的关系. The cards below are the complete content source for those sections: rearranging their labeled paragraphs is allowed; inventing extra models or deleting qualifications to save space is not. Put notation and corrections in two short appendices. Software catalogue details remain in a separate implementation appendix, not in every chapter's main narrative.

## 1. Common notation and reconciliation

Use subject/cluster `i=1,...,N`, occasion `t`, outcome/channel `k`, category `j`, component/state `s`, Monte Carlo replication `r=1,...,B`, posterior draw `m=1,...,M`. `n` denotes an independent sample size when there are no clusters; never confuse it with B or M. X is n-by-p, and a row predictor is x_i^T beta. Include an intercept in x only when the model does not already absorb it into cutpoints.

| Original reuse or conflict | Frozen notation and conversion |
|---|---|
| A chapter uses p-by-n X | This note uses n-by-p X; transpose consistently, not only in the first equation. |
| Normal second argument in BUGS | `dnorm(mu,tau)` uses precision tau=1/sigma^2. R/Python normal generators generally take standard deviation; this note writes N(mu,sigma^2). |
| Poisson/NB dispersion named theta, phi or alpha | NB2 shape is kappa: Var(Y|x)=mu+mu^2/kappa. MASS theta and PyMC alpha equal kappa; statsmodels NB2 alpha equals 1/kappa. |
| Ordinal signs differ across chapters/examples | Canonical logit P(Y<=j|x)=a_j-x^T beta, a_1<...<a_(J-1). Chapter 3 insomnia's plus-sign coefficient must be negated to compare with this convention. |
| Nominal last-category baseline vs nnet first factor level | Write the reference category explicitly, set its entire coefficient vector to zero, and explicitly order the factor. |
| Random effect variance, SD and precision reused | D is covariance; scalar sigma_b is SD; sigma_b^2 is variance. |
| HW2 uses R=1 for missing | This note uses R=1 for observed. Convert to R_miss=1-R_obs before comparing selection-model signs. |
| Latent class, HMM state and membership weights confused | S_i is one class; S_it is a state at a time; g_i is a simplex of simultaneous membership weights. |
| Threshold vs regression intercept | Use free thresholds OR a latent-location intercept constraint, not an unidentified free shift in both. |
| Mixture likelihood vs product of weighted component densities | A class mixture sums component densities. Chapter 9 instead places a weighted trajectory in a conditional mean; neither is a product-of-densities replacement. |
| Inverse-gamma conventions | IG(a,b) has density proportional to v^(-a-1) exp(-b/v), v>0. b is a scale in this stated convention, not a rate for v. |

Shared identification checks: full-rank observed design; specified response ordering/baseline; positive variances; constraints on factor location, scale and rotation; permutation invariance in latent classes; sufficient within-cluster/within-state information; missingness or causal assumptions beyond observed-data fit. An optimizer returning numbers is not an identification test.

## 2. Chapter 1 — Estimation is part of the model

**S:** likelihood and Bayesian inference, latent-data augmentation, Gibbs/MH, EM/Monte Carlo EM, information criteria, Bayes factors/path sampling and regularization. **P:** start by separating uncertainty about a parameter from error in its numerical approximation.

### 1A. Likelihood and Bayesian updating

**Problem, intuition, form, parameters.** Observed data Y inform an unknown theta through L(theta)=p(Y|theta). A prior adds explicit information: p(theta|Y) is proportional to p(Y|theta)p(theta). A concrete scene is estimating a mean with a small sample: the same sampling model can yield an MLE or a posterior, but these are not the same inferential object. For a normal variance v with known mean and the stated IG(a0,b0) prior, v|Y is IG(a0+n/2,b0+sum_i(y_i-mu)^2/2).

**Assumptions/identification.** The likelihood must match the observation and sampling structure. Priors must be proper when required for a proper posterior or a Bayes factor. A proper prior can regularize weak identification but does not make the data intrinsically informative.

**Estimation/computation.** Maximize log likelihood, or integrate/sample a posterior. Conjugate blocks permit direct draws; general GLM coefficients do not become conjugate merely because their prior is normal. Posterior means, medians and credible intervals are summaries of a stated posterior, not software-independent universal answers.

**Diagnostics.** Check likelihood coding, scaling, optimization gradients/Hessian and prior sensitivity. For simulation-based posterior summaries distinguish posterior SD from Monte Carlo SE. A very small Monte Carlo SE cannot repair a wrong likelihood.

**Interpretation/failures.** A frequentist confidence interval concerns repeated-sample performance of a procedure; a Bayesian credible interval concerns posterior probability under the model/prior. Do not swap those explanations. BUGS precision-to-SD mistakes can change a prior by orders of magnitude.

**R/Python; links; aging/additions.** R `stats`/model packages for ML; `brms`/Stan for appropriate Bayesian models. Python `statsmodels` for ML, PyMC for Bayesian models. This card underlies every chapter. Fixed diffuse priors and fixed iteration counts in old examples are not universal defaults (M).

### 1B. Missing variables in computation: EM, Gibbs and MH

**Problem/intuition/form.** Latent Z can simplify a complete-data model even when p(Y|theta)=integral p(Y,Z|theta)dZ is awkward. EM uses Q(theta|theta_old)=E[log p(Y,Z|theta)|Y,theta_old], then maximizes with respect to the candidate theta. Gibbs draws blocks from their full conditionals. MH proposes theta' from q(theta'|theta) and accepts with probability min{1, p(theta'|Y)q(theta|theta')/[p(theta|Y)q(theta'|theta)]}.

**Assumptions/identification.** EM needs a legitimate conditional expectation and well-defined maximization; MH requires suitable support and an ergodic chain. A symmetric proposal cancels its ratio, but an arbitrary asymmetric proposal does not. Latent-parameter constraints still apply.

**Estimation/computation.** EM is optimization, not posterior sampling. MCEM approximates its E-step and requires control of simulation noise. Gibbs/MH target distributions, not a deterministic sequence of improving likelihood values. The nonlinear latent-SEM MH supplement illustrates why some coefficient blocks have no standard full conditional; it is not a mandate to hand-code a sampler in Tutorial 1.

**Diagnostics.** Multiple starts and likelihood progression for EM; Monte Carlo precision for MCEM; multiple chains, rank-normalized split R-hat, bulk/tail ESS, trace/rank behavior and MCSE for MCMC. With HMC/NUTS, inspect divergences and geometry, not only trace plots.

**Interpretation/failures.** EM can find a local optimum. Posterior draws may remain in one mixture labeling or mode. More iterations do not fix an invalid transition kernel. An acceptance-rate example such as 0.25 is not a universal target.

**R/Python; links; aging/additions.** R mixture/HMM packages implement EM; Stan/PyMC handle many posterior computations. Python mixture tools implement EM; PyMC handles posterior sampling. Link to mixtures (5), missingness (6), HMMs (7), joint latent models (8–9). Replace old R-hat≈1.2 comfort thresholds and automatic thinning with current diagnostics (M); preserve algorithmic intuition (S).

### 1C. Comparison and regularization

**Problem/intuition/form.** Fit is not the only objective: compare predictive adequacy, scientific usefulness and complexity on compatible likelihoods. With d free parameters, AIC=-2 ell(theta_hat)+2d; BIC=-2 ell(theta_hat)+d log n. DIC uses a posterior deviance summary and an effective complexity term; latent-variable definitions depend on which likelihood is being summarized. Posterior model odds equal prior model odds times a Bayes factor. Path sampling represents a log normalizing-constant ratio by an integral of expectations along a specified path. Penalized estimation solves -ell(beta)+lambda sum_j w_j|beta_j|; ordinary Lasso uses w_j=1.

**Assumptions/identification.** Count the same free parameters and use the same response, rows, exposure and likelihood convention. Regular AIC/BIC heuristics and ordinary likelihood-ratio asymptotics can fail for boundary/singular mixture problems. Bayes factors require comparable proper prior specifications. Lasso requires scale-aware penalization and a tuning rule.

**Computation/diagnostics.** Calculate criteria from the intended marginal or conditional likelihood, not whatever a package happens to print. Check multi-start stability, out-of-sample performance and sensitivity to priors/tuning. Path discretization error and Monte Carlo error both matter. Predictive validation must respect subjects and time.

**Interpretation/failures.** A smaller criterion is not proof that the data-generating mechanism or a causal story is true. A continuous shrinkage posterior mean is generally not an exact variable-selection rule; a Lasso MAP estimate can have zeros. Quasi-likelihood does not supply an ordinary full-likelihood AIC.

**R/Python; links; aging/additions.** Model-specific `logLik`/AIC/BIC in R; corresponding likelihood-aware results in Python; Stan/PyMC posterior tools where needed. S includes DIC and Bayes-factor methods; M adds stronger predictive validation and cautions against automatically treating modified DIC/AIC as ordinary AIC. C: Chapter 1 p26's doubled BIC penalty is not retained. Applies to Chapters 2–9.

## 3. Chapter 2 — Choose the observation model before choosing the package

**S:** exponential-family GLMs, binary, count, ordinal and nominal outcomes. General form f(y|theta,phi)=exp{[y theta-b(theta)]/a(phi)+c(y,phi)}, E(Y)=b'(theta), Var(Y)=a(phi)b''(theta), g(mu)=x^T beta. The link is a modeling choice and need not be canonical. ML uses score/Hessian iterations, often IRLS. Independence here is conditional on the stated covariates and sampling design, not guaranteed by having one spreadsheet row per measurement.

### 2A. Binary logit and probit

**Problem/intuition/form/parameters.** A yes/no event requires a probability in [0,1]. Bernoulli(p_i), logit(p_i)=x_i^T beta, or probit(p_i)=x_i^T beta. A latent-threshold representation uses logistic noise for logit and N(0,1) noise for probit.

**Assumptions/identification.** Full-rank X, correct event coding and enough outcome overlap. Fix latent noise scale; coefficients and an unconstrained latent scale cannot both be identified. Complete/quasi separation can make an unpenalized logistic MLE infinite.

**Estimation/computation.** ML/IRLS or a stated Bayesian posterior; normal priors on logit coefficients do not yield generic normal full conditionals. **Diagnostics:** separation, leverage, predicted probabilities, calibration, sensitivity to functional form; residuals need not look Gaussian.

**Interpretation/failures.** exp(beta) is a conditional odds ratio in a logit model, not a risk ratio or an absolute probability change. A sign on the linear predictor does not specify a constant probability difference. Probit coefficients have no direct odds-ratio interpretation.

**R/Python; links; aging/additions.** `stats::glm(binomial(...))`; statsmodels GLM/Logit/Probit. M: emphasize calibration, coding and separation rather than only a significant coefficient. Ch3 adds dependence; Ch6 missingness affects observed samples. C: a normal latent-error construction must be labeled probit, even where an old slide calls it a cumulative logit.

### 2B. Poisson and negative-binomial counts

**Problem/intuition/form/parameters.** Counted events occur over an exposure e_i>0. Use log(mu_i)=log(e_i)+x_i^T beta. Poisson has Var(Y_i|x_i,e_i)=mu_i. NB2 adds shape kappa>0 and Var=mu_i+mu_i^2/kappa; its pmf is Gamma(y+kappa)/[Gamma(kappa)y!] times [kappa/(kappa+mu)]^kappa [mu/(kappa+mu)]^y. Larger kappa approaches Poisson. The offset has coefficient exactly one and models a rate, not a freely estimated exposure association.

**Assumptions/identification.** Independent observations conditional on predictors; integer nonnegative counts; a meaningful exposure denominator; correct mean/link. Covariates varying across observations can make the raw variance exceed the raw mean even under a valid conditional Poisson model. Zero inflation is a separate structural hypothesis, not a synonym for overdispersion.

**Estimation/computation.** Poisson IRLS; NB2 joint or alternating estimation of beta and kappa. Check that software estimates dispersion rather than holding a default value fixed. A Poisson score can consistently estimate a correctly specified log mean despite a wrong variance, while its model-based SE is wrong.

**Diagnostics.** Pearson sum divided by residual degrees of freedom as a descriptive dispersion check, residuals versus fitted rate and covariates, observed versus fitted zero frequencies, tails, convergence and exposure sensitivity. Pearson dispersion is approximate, not a universal binary pass/fail test. Compare ordinary AIC only on the same rows/response with full likelihoods.

**Interpretation/failures.** exp(beta_j) is a conditional rate ratio at equal exposure, not a causal effect absent design assumptions. More sampling does not automatically repair variance misspecification. Dropping an offset can confound exposure with group differences. More event counts need not mean a better service outcome.

**R/Python; links; aging/additions.** `glm(...,poisson,offset)` then `MASS::glm.nb`; glmmTMB later. Python statsmodels **discrete** NegativeBinomial(loglike_method='nb2') estimates alpha; GLM's NegativeBinomial family uses a supplied alpha. Tutorial's modern diagnostic/offset sequence is P/M. S: horseshoe-crab satellite counts contrast Poisson and NB, with different uncertainty; do not reproduce old tables wholesale. Ch3 can induce extra count variation through shared random effects; Ch5/6 offer different mechanisms that NB alone does not identify.

### 2C. Ordered categories

**Problem/intuition/form/parameters.** Severity categories preserve order without assuming equal spacing. Define F_ij=P(Y_i<=j)=F(a_j-x_i^T beta), j=1,...,J-1, with ordered a_j, F logistic or standard normal. Category probability is F_ij-F_i,j-1, using endpoints 0 and 1. A positive beta moves probability toward higher categories in this convention.

**Assumptions/identification.** Correct order; common slope across cutpoints for proportional odds/probit; constrained latent location and scale. Free cutpoints plus a redundant intercept are unidentified. Nonparallel cumulative predictors can cross and generate negative category probabilities.

**Estimation/computation.** Constrained ML or Bayesian latent-threshold inference. Estimate cutpoints, do not treat arbitrary scores 1,2,3 as an automatically valid continuous response. **Diagnostics:** cutpoint ordering, sparse categories, predicted category probabilities, plausibility of parallel effects and sensitivity to a carefully specified alternative.

**Interpretation/failures.** Under logit, exp(beta) multiplies odds of being above rather than at/below any threshold. An alternative plus-sign cumulative equation reverses that coefficient. Software output must be interpreted from its equation, not from a familiar variable name.

**R/Python; links; aging/additions.** `ordinal::clm`, `MASS::polr` for ordinary models; statsmodels OrderedModel for ordinary ordered outcomes. Repeated ordinal responses require `ordinal::clmm` or a suitable Bayesian multilevel model, not ordinary OrderedModel. S contains latent ordinal constructions; C reconciles Chapter2's sign with Chapter3 insomnia and the old R script. P: retain fully in this review but do not require ordinal coding in HW1.

### 2D. Unordered categories and latent utilities

**Problem/intuition/form/parameters.** Food choice or a service channel has categories but no ranking. With reference J, beta_J=0 and P(Y=j)=exp(x^T beta_j)/sum_l exp(x^T beta_l). Thus log(p_j/p_J)=x^T beta_j. A multinomial-probit alternative compares correlated latent utilities after fixing utility location and scale.

**Assumptions/identification.** Explicit reference, category ordering, rank and overlap; multinomial logit imposes its particular odds structure, including IIA in a choice interpretation. Utility models need a reference contrast and scale constraint; multiplying utilities and means by c requires covariance multiplication by c^2.

**Estimation/computation.** Multinomial ML with stable log-sum-exp, or latent-normal integration/simulation for multinomial probit. Re-referencing to category r gives beta_j(new)=beta_j(old)-beta_r(old), including the previous reference. Probabilities are unchanged.

**Diagnostics.** Category frequency/sparsity, convergence, calibration of predicted probabilities, sensitivity to predictors and reference-invariance tests. **Interpretation/failures:** a negative coefficient for log(p_j/p_J) does not require p_j itself to decrease; all denominator terms change. The alligator example makes this distinction especially useful. Do not label ordinary softmax output as ordinal or causal preference effects.

**R/Python; links; aging/additions.** `nnet::multinom` (first factor level baseline, explicitly relevel); statsmodels MNLogit with verified label mapping. Multinomial probit is not an equivalent nnet option. M: probability curves and reference invariance as executable tests. Ch3 adds subject effects; Ch5's class probabilities may themselves use a multinomial regression.

## 4. Chapter 3 — Correlation changes both uncertainty and interpretation

**S:** GLMMs for repeated count, binary, ordinal and nominal responses, latent-normal constructions and Bayesian computation. **P:** explain one scalar random intercept before presenting richer random-effect matrices.

### 3A. General GLMM, binary and count versions

**Problem/intuition/form/parameters.** Repeated measurements share a person's propensity. Conditional on b_i~N(0,D), responses are independent with g(mu_it)=x_it^T beta+z_it^T b_i. The observed likelihood is product_i integral [product_t f(y_it|b_i,beta)] phi(b_i;0,D) db_i. For binary responses use Bernoulli and logit; for counts use Poisson/NB with an exposure offset.

**Assumptions/identification.** Independent subjects, appropriate conditional family, specified random-effect distribution and conditional independence, usually b independent of included covariates. Repeated observations supply information about variation among subjects. Adding an independent latent variance to every single Bernoulli observation is not automatically well identified. Too few clusters or overly rich D gives singular or weakly identified fits.

**Estimation/computation.** Integrate random effects for ML, using Laplace or adaptive quadrature where supported; alternatively sample the joint posterior under declared priors. Laplace approximation to a marginal likelihood and Laplace approximation to a Bayesian posterior are different procedures. General normal coefficient priors do not imply a conjugate GLMM update.

**Diagnostics.** Convergence/gradient, singularity, sensitivity to quadrature and optimizer, subject-level fitted checks, conditional family and unexplained time patterns. A near-zero estimated random-effect variance is a boundary issue; an ordinary chi-square LRT is not automatically justified. Use diagnostic evidence rather than a single variance-component p-value in HW1.

**Interpretation/failures.** A logistic fixed effect is conditional on b. A new-subject probability is integral expit(x^T beta+b) phi(b)db, not expit(x^T beta). Setting b=0 is a conditional prediction, not integration. Naive logistic coefficients and conditional GLMM coefficients can differ even without a simple 'omitted correlation causes coefficient bias' story. For a Poisson random intercept, marginal covariance at two occasions is exp(x_t^T beta+x_s^T beta+sigma_b^2)[exp(sigma_b^2)-1]; random slopes can yield other covariance patterns.

**R/Python; links; aging/additions.** `lme4::glmer`, scalar random-intercept nAGQ=9 in HW1; glmmTMB for broader response/dispersions. Python statsmodels BinomialBayesMixedGLM is NOT the same ML estimator; use the supplied R runner for HW1's mixed fit. PyMC is an explicit Bayesian alternative later, not a covert replacement. Ch4 develops multilevel interpretations; Ch6 shares random effects with missingness; Ch7 lets latent states change over time. M: distinguish conditional, b=0 and genuinely marginalized predictions. The old Monte Carlo-likelihood `glmm` manuals describe a different numerical route and are not modern lme4 authority.

### 3B. Ordinal and nominal repeated responses

**Problem/intuition/form/parameters.** Repeated severity or repeated choices need both the outcome scale and within-person dependence. Ordinal: logit P(Y_it<=j|b_i)=a_j-x_it^T beta-b_i. Nominal: log[p_itj(b)/p_itJ(b)]=x_it^T beta_j+z_it^T b_ij with reference effects fixed to zero. A multivariate-probit utility model uses reference utility differences and constrained covariance.

**Assumptions/identification.** Ordered cutpoints and scale constraints remain necessary; for nominal random effects identify only relative utilities, not an arbitrary shared additive utility. Enough repeated data must support category-specific D. Conditional proportional-odds assumptions are not identical to marginal proportional odds.

**Estimation/computation.** Integrate random effects or augment latent utilities in a valid posterior algorithm. For normal random-effect covariance with IW(nu,S) parameterization, a standard conditional covariance update adds sum_i b_i b_i^T to S and N to nu; do not mix covariance and precision conventions.

**Diagnostics.** Cutpoint/category sparsity, random-effect singularity, fitted category probabilities over time, convergence and prior sensitivity. **Interpretation/failures:** Chapter3's insomnia example uses a **plus** cumulative-logit sign; increasing its predictor raises the probability of lower severity. Negate those slopes before comparing with the canonical minus convention. Keep the cutpoints in the equation; omitting them does not define an ordinal model.

**R/Python; links; aging/additions.** `ordinal::clmm`; brms for supported cumulative/categorical multilevel formulations. Ordinary Python ordered or multinomial ML routines do not add the required random effects. Ch2 supplies category semantics, Ch4 multilevel extensions. C corrects cutpoint/sign/latent-scale issues; P postpones hands-on repeated ordinal coding beyond HW1 to avoid an unfair package prerequisite.

## 5. Chapter 4 — Multilevel models represent structured heterogeneity

**S:** nested and multilevel models, varying coefficients, heterogeneous residual variance, small-area count applications and growth models.

### 4A. Gaussian multilevel models and varying slopes

**Problem/intuition/form/parameters.** Pupils share schools; repeated measurements share people. Partial pooling estimates group departures without giving every small group an unrelated estimate. y_it=x_it^T beta+z_it^T b_i+epsilon_it, b_i~N(0,D), epsilon_it~N(0,sigma_it^2). With random intercept and slope at covariate x, marginal variance is sigma_it^2+tau_0^2+2x tau_01+x^2 tau_1^2.

**Assumptions/identification.** Conditional mean, random-effect distribution, independent groups, residual covariance and predictor/random-effect relationships must be justified. Centering changes intercepts and intercept-slope covariance. Separate within-group and between-group associations where they answer different questions. A predictor constant within groups cannot identify a within-group slope.

**Estimation/computation.** Gaussian marginal likelihood has mean X beta and covariance ZDZ^T+R. ML or REML with their proper comparison restrictions; integrate or sample hierarchically for Bayes. Models with different fixed-effect structures should not be compared using unqualified REML likelihood differences.

**Diagnostics.** Random-effect and residual plots, influence of groups, singular D, residual variance versus covariates, contextual effects and out-of-group prediction. **Interpretation/failures:** pooling strength depends on information and heterogeneity, not a universal averaging coefficient. A random slope is not justified merely because it is available. Independence of b and x is a substantive assumption.

**R/Python; links; aging/additions.** `lme4::lmer`, `nlme` for suitable residual structures, brms for Bayesian variants; statsmodels MixedLM for Gaussian mixed effects. S includes the language/IQ/SES school example. M adds explicit centering/within-between interpretation and grouped validation. Connects GLMMs (3), latent classes (5) and trajectories (9).

### 4B. Dispersion, multilevel counts and growth

**Problem/intuition/form/parameters.** Groups may differ in variability as well as average level; repeated outcomes may change smoothly with time. A positive modern variance model is log(sigma_it^2)=d_it^T gamma. A source model linear in IQ, sigma_it^2=theta_1+theta_2 IQ_it, instead needs positivity over its domain: the log-variance replacement is a different model, not merely another API. For area counts, log(mu_i)=log(expected_i)+x_i^T beta+b_i. For growth, time basis B(t) enters fixed and random coefficients; residual serial correlation is an additional choice, not automatically absorbed by a random intercept.

**Assumptions/identification.** Positive residual variance and covariance matrices; sufficient occasions/time coverage for random slopes; appropriate exposure; distinguish nested from crossed grouping. Do not fit a rich trajectory and a rich serial covariance with inadequate repeats.

**Estimation/computation.** ML/REML for suitable Gaussian models; Laplace/quadrature for non-Gaussian models; Bayesian computation for declared structures. **Diagnostics:** variance and residual time patterns, extrapolation, group influence, exposure and prediction target.

**Interpretation/failures.** A positive variance credible interval under a continuous positive prior is not equivalent to a frequentist test rejecting zero. A relative rate is not an absolute count. Predicting a known cluster with its estimated b differs from predicting a new cluster after integration.

**R/Python; links; aging/additions.** glmmTMB dispersion models, nlme correlation/variance structures and brms supported multilevel models; MixedLM covers only part of this landscape. Python need not duplicate unsupported heterogeneous GLMM syntax. M: present positivity and prediction targets explicitly. Ch6 adds informative dropout; Ch9 links trajectories to event times. C: latent-noise realizations should not replace the deterministic linear predictor in an ordinal probability equation.

## 6. Chapter 5 — Mixtures describe unobserved subpopulations, not certain labels

### 5A. Gaussian and regression mixtures

**S problem/intuition/form/parameters.** A single population distribution may hide groups. With one latent class S_i per subject, P(S_i=s)=pi_s and f(y_i|x_i)=sum_s pi_s f_s(y_i|x_i,theta_s). Gaussian components use mu_s and positive-definite Sigma_s; regression components use x_i^T beta_s. Concomitant-variable models let pi_is=softmax(w_i^T gamma_s). Repeated-response class models allocate an entire subject rather than every visit independently unless the model explicitly says otherwise.

**Assumptions/identification.** Finite chosen K, within-component model adequacy, positive weights summing to one, distinct enough components, constraints for regression and covariance. Labels are identified only up to permutation. Tiny components and collapsing Gaussian covariance can produce singular likelihoods. More components can absorb skewness rather than reveal scientific groups.

**Estimation/computation.** EM responsibilities are tau_is=pi_is f_s(y_i)/sum_l pi_il f_l(y_i). Weighted parameter updates follow; use multiple starts. Bayesian allocation sampling requires correct full conditionals and label-aware summaries. Under a Dirichlet(alpha) prior, density is proportional to product pi_s^(alpha_s-1), and posterior shapes add class counts. For normal means with known component covariance, V_post=(V0^-1+n_s Sigma_s^-1)^-1 and m_post=V_post[V0^-1 m0+Sigma_s^-1 sum_{i:S_i=s} y_i]. Conditional covariance updates use centered scatter, not uncentered y_i y_i^T by default.

**Diagnostics.** Multi-start likelihood agreement, component occupancy, covariance eigenvalues, allocation uncertainty, posterior label behavior and sensitivity to K. Classification accuracy without true labels is not a diagnostic. Holdout observations must be appropriate to the subject structure.

**Interpretation/failures.** A 0.55 membership probability is not a certain diagnosis. Relabel all linked means, variances, regression coefficients and weights consistently before component-level bias/RMSE or posterior averaging. Standard chi-square tests for K versus K+1 are nonregular. Do not treat `BayesianGaussianMixture` variational output as a fully sampled posterior.

**R/Python; links; aging/additions.** mclust for Gaussian model-based clustering; flexmix for finite mixtures of regressions and supported concomitant models. scikit-learn GaussianMixture and BayesianGaussianMixture cover a narrower Gaussian-mixture problem; neither implements the whole course's regression/multilevel/joint models. S includes richer Bayesian mixture computations and model comparison; M emphasizes stability and uncertainty rather than automatic class naming. Ch7 changes a subject's state over time; Ch9 replaces a single class with simultaneous membership weights. C: Chapter5 pp13–15 conjugate-update expressions require the corrections listed in Appendix A.

## 7. Chapter 6 — Missingness assumptions determine what can be learned

### 6A. Ignorable and nonignorable missingness

**S problem/intuition/form/parameters.** An absent measurement may be related to the very outcome being studied. With R=1 meaning observed, a selection factorization is p(Y|theta)p(R|Y,psi); a pattern-mixture factorization is p(Y|R,eta)p(R|rho). A shared-parameter model integrates p(Y|b,theta)p(R|b,psi)p(b). The observed-data likelihood integrates the missing Y and any latent b.

**Assumptions/identification.** MCAR: missingness independent of the complete data. MAR: conditional on observed data, missingness does not additionally depend on missing values. MNAR: that conditional restriction fails. Ignoring the missingness mechanism also requires appropriate parameter distinctness; Bayesian ignorability uses compatible factorization of priors. MAR versus MNAR is generally not determined from observed-data fit alone. Pattern-mixture extrapolation and MNAR parameters need identifying restrictions, external information or sensitivity ranges.

**Estimation/computation.** Observed-likelihood integration, data augmentation, joint/selection models, or multiple imputation under a justified model. In a shared-parameter model, conditional independence given b is an assumption, not an empirical consequence of adding random effects.

**Diagnostics.** Missingness patterns over groups/time, which observed variables predict missingness, imputation/observed distribution comparisons, convergence, sensitivity to MNAR departures. An insignificant correlation involving latent factors is not evidence proving MAR.

**Interpretation/failures.** Complete-case estimates can target a changed population or be biased for the desired target. 'We used an imputer' is not an argument for ignorability. Switching R's coding reverses selection-model coefficient interpretations. This directly matters for old HW2, which codes R=1 as missing.

**R/Python; links; aging/additions.** mice for appropriate MAR-based chained equations; model-specific Stan/PyMC for explicitly nonignorable/shared models. statsmodels MICE provides a limited Python route; scikit-learn IterativeImputer alone is not a full inferential MI/pooling workflow. Connects multilevel structure (4), dropout/state processes (7) and joint models (9). M: require sensitivity analysis rather than claiming that diagnostics validate MAR.

### 6B. Multiple-imputation inference

**Problem/intuition/form/parameters.** One completed dataset hides uncertainty about unobserved values. For m valid imputations, combine estimates Q_l and their variances U_l: Qbar=mean(Q_l), Ubar=mean(U_l), B_MI=sum_l(Q_l-Qbar)^2/(m-1), T=Ubar+(1+1/m)B_MI. Use appropriate finite-degree-of-freedom inference rather than blindly applying an infinite-sample normal approximation.

**Assumptions/identification.** Proper imputations must represent relevant uncertainty and be compatible enough with the analysis: preserve outcome types, interactions, important predictors, outcomes and clustering. Include useful auxiliary variables. Twenty or more imputations can be a starting point, with more and an MCSE check when missing information is large; no fixed small number guarantees precision.

**Estimation/computation.** Fit the analysis separately in each imputation and pool estimates/variances. Do not average completed datasets and then pretend the averages were observed. Consecutive MCMC draws are not automatically independent, adequate imputations.

**Diagnostics.** Chain behavior, plausible completed values, between-imputation variation and stability as m increases; examine scientific conclusions over sensitivity settings. **Interpretation/failures:** between-imputation variability contributes to uncertainty. Deterministic imputation or ignoring B_MI overstates precision.

**R/Python; links; aging/additions.** mice plus its model-appropriate pooling functions; statsmodels MICE where supported. Multilevel imputation needs compatible two-level/joint options, not a flat default. S includes multiple imputation; M replaces 'five draws suffice' habits with uncertainty-driven precision checks. Supports HW2/Project, not another HW1 programming prerequisite.

## 8. Chapter 7 — A latent state can change over time

### 7A. Hidden Markov models

**S problem/intuition/form/parameters.** A sequence may alternate between unobserved regimes. S_i1~rho and P(S_it=s|S_i,t-1=r)=Q_rs; each row of Q sums to one. Conditional emissions f_s(y_it|x_it) link states to data. The subject likelihood sums over state paths: sum_{s_1:T} rho_s1 product_{t>1}Q_{s_(t-1),s_t} product_t f_st(y_it).

**Assumptions/identification.** First-order state dynamics, conditional emission independence, adequately distinct emissions and state occupancy, label constraints for interpretation. Unequal time gaps require an appropriate transition model; a constant discrete-time transition matrix does not silently become a continuous-time model.

**Estimation/computation.** Forward recursion computes likelihood in O(T K^2), with scaling or log-sum-exp. Forward-backward gives state probabilities; EM/Baum-Welch or Bayesian methods estimate parameters. Viterbi returns one most likely joint path, not the vector of most probable marginal states. These computational explanations are M/P additions to the supplied treatment, not claims that every recursion was taught in the original slides.

**Diagnostics.** Multiple starts, transition row sums, posterior state uncertainty, occupancy, residual serial dependence, dwell-time plausibility and heldout whole sequences. Ordinary homogeneous HMMs imply geometric dwell times. **Interpretation/failures:** a state label is a model-dependent summary, not an observed diagnosis. Hard labels conceal uncertainty and can propagate errors into later analyses.

**R/Python; links; aging/additions.** depmixS4 is the ordinary course implementation; Python hmmlearn for supported emissions/basic HMMs. M includes scaled recursions and state-uncertainty plots. Ch5 is the static-class analogue; Ch3 random effects represent persistent heterogeneity rather than a changing discrete state.

### 7B. Mixed HMMs and hidden Markov latent-variable models

**S problem/intuition/form/parameters.** State transitions and multivariate emissions may themselves vary by subject. Conditional on b_i, transition predictors can depend on x_it and b_i. The source's ordered transition specification uses a continuation-ratio logit log[P(S_it=s|previous)/P(S_it>s|previous)]=a_rs+x_it^T beta+v_it^T b_i. If h_s is its inverse-logit hazard, category probabilities are h_s product_{l<s}(1-h_l), with the final state taking the remaining probability. This is NOT an ordinary cumulative proportional-odds model.

A latent measurement layer can use y_it|S_it=s,omega_it ~ N(mu_s+Lambda_s omega_it,Psi_s), with diagonal measurement-error Psi_s and a structural relation eta_it=Gamma_s xi_it+delta_it inside omega=(eta,xi).

**Assumptions/identification.** Fix factor location, scale and rotation as well as state labels. Verify that item/state information supports the proposed structure. Conditional Markov behavior given b does not imply first-order Markov behavior after b is integrated out.

**Estimation/computation.** Integrate continuous latent effects as well as summing states, or use valid augmentation and MH-within-EM/MCMC. Computation is substantially richer than fitting a basic HMM to one outcome.

**Diagnostics.** The basic HMM checks plus measurement-model residuals, factor constraints, weak state separation, random-effect sensitivity and posterior geometry. **Interpretation/failures:** transition associations are not causal effects; a flexible latent layer can absorb misspecification without validating its interpretation.

**R/Python; links; aging/additions.** hmmTMB is an optional advanced R route for supported covariate/random-effect HMMs. Neither it nor hmmlearn automatically reproduces every hidden-Markov latent measurement model in the slides. Use custom Stan/PyMC/model-specific code for genuinely unsupported joint structures; discretely latent states in Stan generally require marginalization. Ch8 builds on latent measurement; Ch9 combines longitudinal summaries with events. M: explicitly label package capability limits.

## 9. Chapter 8 — Measurement models do not, by themselves, establish mediation

### 8A. Latent mediation with an event-time outcome

**S problem/intuition/form/parameters.** A treatment/exposure S may affect an event through imperfectly measured intermediate variables. A schematic model matching the source's roles is W=a0+A_Z Z+a_S S+e_W; M=b0+B_Z Z+b_S S+B_W W+e_M; observed indicators V=mu+Lambda M+zeta; and h(t|S,Z,W,M)=h0(t)exp(gamma_S S+gamma_Z^T Z+gamma_W^T W+gamma_M^T M). Loadings describe measurement, a/B coefficients intermediate regressions, and gamma coefficients conditional hazard associations.

**Assumptions/identification.** Measurement location/scale/rotation restrictions, adequate indicators, measurement invariance where assumed, positive hazard and conditionally appropriate censoring. Causal mediation additionally needs consistency, positivity and appropriate treatment/mediator-outcome confounding and cross-world assumptions. A good fitted latent model does not establish those assumptions; exposure randomization alone need not remove mediator-outcome confounding.

**Estimation/computation.** Joint likelihood includes measurements and survival. For a piecewise-constant baseline with hazard lambda_h and constant subject predictor eta_i, an event contributes delta_i[log lambda_h(T_i)+eta_i]-exp(eta_i)sum_h lambda_h exposure_ih. With time-varying eta_i(t), integrate lambda_h exp(eta_i(t)) over time instead. Bayesian latent augmentation contains some conjugate and some nonstandard blocks; use proper priors and a correctly coded joint likelihood.

**Diagnostics.** Measurement residuals and loading constraints, posterior sampling diagnostics, survival calibration/censoring-aware prediction, proportional-hazards or time-effect adequacy, prior sensitivity, and causal sensitivity assumptions. Observational fit cannot certify absence of confounding.

**Interpretation/failures.** On a defined counterfactual contrast scale, TE=NDE(0)+NIE(1)=NDE(1)+NIE(0); same-reference decompositions need additional conditions. Under the source's **rare-outcome/low-cumulative-hazard approximation**, path contributions include gamma_S Delta S, gamma_M^T b_S Delta S, and (gamma_W^T+gamma_M^T B_W)a_S Delta S. The last term already includes the W-to-M-to-event path: do not count it again. These path products are not unrestricted exact hazard-ratio decompositions.

**R/Python; links; aging/additions.** Custom Stan via CmdStanR, or an explicitly validated PyMC joint model, is the research-tier implementation; a single ordinary brms formula is not an exact reproduction of this complete latent mediation model. S uses a biomedical illustration, which does not license redistributing patient data. Ch3/4 supply conditional models, the supplement supplies measurement identification, and Ch9 develops joint trajectory/event modeling. M adds a stronger separation of statistical fit from causal identification.

## 10. Chapter 9 — Joint trajectories and events with mixed membership

### 9A. Mixed-membership longitudinal-survival model

**S problem/intuition/form/parameters.** A subject may resemble several extreme trajectory profiles rather than belong wholly to one class. Let g_i lie on an M-component simplex, with g_i~Dirichlet(delta0 xi), sum xi_m=1. For outcome k, profile h_km(t)=sum_p b_kmp B_p(t), and mu_ik(t)=sum_m g_im h_km(t). Observations follow y_ik(t)|g_i ~ N(mu_ik(t),psi_k), where psi_k is explicitly a variance. This is a weighted conditional mean, not a class-mixture likelihood sum or a product of component densities.

The joint event model is h_i(t)=h0(t)exp(beta^T z_i+sum_k alpha_k mu_ik(t)). Its likelihood uses the time integral of h_i(t). When mu_ik(t) varies with time, H_i(t) is not generally H0(t) times exp of the predictor evaluated only at t.

**Assumptions/identification.** Conditional measurement distribution, observation schedule and censoring assumptions, adequate trajectory coverage, constrained labels/profile interpretation and positive variances/hazards. Extreme profiles and membership weights can be weakly identified when profiles overlap or observation times are sparse. An ordering constraint removes label symmetry but does not by itself prove full identification.

**Estimation/computation.** Joint posterior or a carefully validated numerical likelihood integrates/samples subject memberships and trajectory coefficients and evaluates cumulative hazards, often numerically. Dirichlet concentration controls dispersion around xi; behavior also depends on individual delta0 xi_m, so 'small concentration means exactly one class' is not a literal statement. Put each parameter prior in the joint density once, not once per subject unless it is genuinely a subject-specific parameter.

**Diagnostics.** Joint longitudinal and event predictive checks, uncertainty in memberships, prior/profile sensitivity, trajectories in observed ranges, likelihood quadrature accuracy, posterior convergence and heldout-subject prediction. For dynamic prediction, condition only on data available by the landmark time; do not leak future measurements. Assess calibration and appropriate censoring-aware accuracy, not only an AUC.

**Interpretation/failures.** A membership vector describes resemblance under the fitted profile system; labels such as CN/MCI/AD require external clinical justification before diagnostic use. Dependence between a trajectory and event time is not automatically a causal trajectory effect. The source's posterior/complete-data modified-AIC construction is not ordinary maximized-likelihood AIC.

**R/Python; links; aging/additions.** This is a custom joint-model task for Stan/CmdStanR or PyMC, not mclust, scikit-learn LDA or a generic HMM one-liner. Rcpp/TMB may accelerate a developer's likelihood implementation but are not necessary student syntax. Links: multilevel trajectories (4), classes (5), informative dropout/missingness (6), measurement/causal limits (8). M adds explicit dynamic-prediction and numerical-integration checks. C corrects the weighted-mean expression and repeated-prior issue in the source.

## 11. Chapter 3 supplement — Latent measurement and shrinkage bridge

**S:** latent structural models combine binary, ordinal, count and continuous measurements, illustrated with happiness/job/home and behavioral outcomes; shrinkage priors regularize paths. **P:** keep this as a short bridge after the main nine chapters, not an extra Tutorial 1 prerequisite.

A generic measurement equation is z_ij=nu_j+lambda_j^T f_i+epsilon_ij; observed ordinal categories are thresholded z, binary outcomes use one threshold, and count channels use their own conditional count likelihood. Structural equations relate latent factors or predictors. Fix a factor scale/loading and appropriate location/rotation; two indicators do not automatically identify a factor without additional restrictions. Fix probit residual variance at one for categorical latent scales.

Estimate the stated joint model by ML/integration or posterior augmentation. Inspect loading constraints, measurement residuals, outcome coding, posterior geometry and shrinkage sensitivity. Gaussian-exponential scale-mixture representations can induce Laplace shrinkage; continuous shrinkage does not automatically yield exact zero posterior means. Measurement-error problems can bias naive regressions, but 'all direct regression is biased' is too broad without specifying the target and misspecification.

R/Python: an appropriate SEM package for the exact supported structure, or a declared custom Stan/PyMC model; brms is not a general-purpose latent SEM compiler. Old WinBUGS demonstrations preserve useful conditional-model ideas, not a mandatory GUI workflow. Connects Chapters 3, 7, 8 and 9.

## Appendix A. Source correction and qualification register

These entries are explicit derived corrections, not replacement source documents. Preserve source locators and explain the mathematical reason in the internal note.

| Source locator | Issue | Frozen treatment |
|---|---|---|
| Chapter1 p26 | BIC complexity term doubled | Use d log n, not 2d log n, with -2 log likelihood convention. |
| Chapter1 normal/conjugate discussion; legacy `linear.R`/`model_linear.txt` | Variance/SD/precision notation can be read inconsistently | State N(mu,sigma^2), generator SD, BUGS precision and IG convention explicitly; verify normalizing powers. |
| Chapter2 p38 | Normal latent construction described with logit wording | Normal latent error gives probit; logistic error gives logit. |
| Chapter2 p48 | Latent-utility scaling written with covariance multiplied by c | Scaling a random variable by c scales covariance by c^2. |
| Chapter2 crab color interpretation | Coding and verbal light/dark direction conflict | Do not reuse its directional claim without recoding; Tutorial uses newly authored data. |
| Chapter3 p3 | Predictor/covariance expression omits regression multiplication | Use x^T beta consistently in the marginal Poisson covariance. |
| Chapter3 p14 | Wheeze pattern table duplicates a pattern label | Do not reconstruct individual records from that table. |
| Chapter3 p18 | Ordinal expression lacks cutpoints | Restore a_j and state ordered thresholds. |
| Chapter3 p20 vs Chapter2 / `glm_ordinal.R` | Plus/minus cumulative-logit conventions differ | Convert coefficient signs; explain the event 'Y<=j' versus 'Y>j'. |
| Chapter3 multinomial-probit scaling | Covariance and SD scaling conflated | Normalize covariance by the square of the chosen scale. |
| Chapter4 ordinal construction | A realized latent noise term appears where the deterministic predictor is needed | Probability uses the mean/linear predictor before integrating noise. |
| Chapter5 p13 | Dirichlet exponent omits -1 | Product pi_s^(alpha_s-1). |
| Chapter5 p14 | Normal posterior-mean update uses an inappropriate centered/candidate-mean expression | Use V_post[V0^-1 m0+Sigma^-1 sum y]. |
| Chapter5 p15 | Gaussian covariance density/update has determinant/scatter problems | Normal likelihood contributes |Sigma|^(-n_s/2); covariance update uses the appropriate centered scatter. |
| Chapter6 p27 | Insignificant latent association overinterpreted as evidence for MAR | Treat MAR as an assumption; require sensitivity, not a non-significance proof. |
| Chapter8 p14 | Path-product interpretation can lose its approximation conditions | Retain rare-outcome/low-hazard approximation and avoid double counting paths. |
| Chapter8 piecewise-hazard likelihood | Bracketing/accumulated hazard can be misread | Use event log-hazard minus integrated hazard. |
| Chapter9 p5 | Product notation conflicts with the weighted-mean construction | Use mu_ik(t)=sum_m g_im h_km(t). |
| Chapter9 p14 | A common coefficient prior appears repeated in a subject product | A common parameter prior enters the joint posterior once. |
| Old HW1 all simulation tasks | B=10 inadequate for precise calibration claims | New HW1 B=500 per scenario, with MCSE and failure accounting. |
| Old R/BUGS examples | Hard-coded local paths, no reproducible seed, old GUI and incomplete package setup | Replace with fixed fixtures, explicit seeds, lockfiles and script-based outputs. |

## Appendix B. What is deliberately not added to Tutorial 1

No latent mediation derivation, HMM fitting, mixed-membership programming, ordinal mixed-model coding, mixture label-switching exercise, Rcpp/TMB syntax, custom MH sampler or full Stan API. These remain meaningful whole-course content or later-course tools. Their omission from a 90-minute pre-HW1 tutorial is a pacing decision, not a claim that they are unimportant.

The progression prerequisite is explicit: HW1's mixed-model section is released only after Chapter 3's conditional random-intercept concept has been covered, or after students receive the frozen bridge note and recorded explanation. Do not infer 2026 teaching progress from 2025 PDF modification dates. No original 2025 due date is reused.
