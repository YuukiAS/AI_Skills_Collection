# STAT5060 Mathematical Details and Clarifications V1

- Status: FROZEN_MATHEMATICAL_APPENDIX.
- Date: 2026-09-28.
- Source authority: supplied Chapters 1–9, the source-correction register, and explicitly labeled standard derivations below.
- Relation: mandatory mathematical appendix to `STAT5060_CANONICAL_KNOWLEDGE_V1.md`. This file supplies exact definitions behind compressed model-card descriptions; it does not add assessed HW1 tasks. Render the relevant definitions with their chapter, with remaining detail in the internal note's appendix.

## 1. Bayesian computation and model comparison

**S, with C for unambiguous parameterization.** Let v denote a variance. N(mu,v) has density (2*pi*v)^(-n/2) exp[-sum_i(y_i-mu)^2/(2v)] for n independent observations sharing mu,v. Writing v=sigma^2 gives a factor sigma^(-n), not sigma^(-n/2). BUGS normal precision is 1/v, whereas an ordinary normal RNG receives sqrt(v) as its scale/SD.

For y|beta,v~N(X beta,vI), beta~N(m0,V0), with known v and a prior independent of v, beta|y,v~N(mn,Vn), where Vn=(V0^(-1)+X^T X/v)^(-1) and mn=Vn[V0^(-1)m0+X^T y/v]. These expressions do not apply unchanged to a GLM merely because its coefficient prior is normal.

With IG(a,b) density b^a/Gamma(a) v^(-a-1) exp(-b/v), the conditional variance update given a mean predictor adds n/2 to shape and residual sum of squares/2 to b. For D of dimension q, IW(nu,S) uses density proportional to |D|^[-(nu+q+1)/2] exp[-tr(S D^(-1))/2], with S positive definite and nu>q-1. Given independent b_i~N(0,D), the covariance conditional is IW(nu+N,S+sum_i b_i b_i^T). A different covariance/precision prior needs its own update.

**S.** D(theta)=-2 log p(Y|theta)+C, where the chosen likelihood and constant convention are explicit. One common DIC definition is p_D=E[D(theta)|Y]-D(E[theta|Y]), DIC=E[D(theta)|Y]+p_D. Latent-variable DIC variants use different likelihoods/complexity definitions; do not compare a complete-data variant with ordinary observed-likelihood AIC as if they were the same statistic. AIC=-2ell(theta_hat)+2d; BIC=-2ell(theta_hat)+d log n.

For a differentiable unnormalized path q_t(theta) with C_t=integral q_t(theta)dtheta and p_t=q_t/C_t, log(C_1/C_0)=integral_0^1 E_t[partial log q_t(theta)/partial t]dt, under conditions permitting differentiation/integration. Power-posterior path q_t=p(Y|theta)^t p(theta) has derivative log p(Y|theta). A comparison between models of different dimensions requires a valid common construction/bridge, not interpolation of incompatible parameter vectors. Numerical path integration and MCMC both contribute error; old fixed grid/iteration examples are not accuracy guarantees.

**S/M.** A Laplace prior proportional to exp(-lambda|beta_j|) corresponds to an L1 penalty at the MAP under the matching likelihood/scale convention. One normal-scale-mixture construction is beta_j|tau_j^2,sigma^2~N(0,sigma^2 tau_j^2), tau_j^2~Exponential(lambda^2/2). Integrating tau gives a Laplace distribution with scale sigma/lambda. State which coefficients are penalized and how predictors are scaled; continuous posterior means do not in general equal exact zeros.

## 2. GLMs and the misspecified-variance simulation

**S/M.** For the specified Poisson log-mean model, U(beta)=sum_i x_i(y_i-mu_i). If the conditional mean is correct, E[U(beta_true)|X]=0 even when the conditional variance is not Poisson. Let A=sum_i mu_i x_i x_i^T and B=sum_i Var(Y_i|x_i)x_i x_i^T. Under standard independent-data regularity conditions, the sampling covariance is approximated by A^(-1) B A^(-1); the conventional Poisson model covariance is A^(-1). Under NB2 truth B uses mu_i+mu_i^2/kappa. Increasing n reduces both scales but does not generally make B equal A. This is instructor reasoning behind HW1, not an additional required sandwich-matrix derivation.

The unconditional raw variance identity Var(Y)=E[Var(Y|X)]+Var[E(Y|X)] explains why heterogeneous means alone can make raw variance exceed raw mean. The offset is part of X's mean context; omitted exposure can change the conditional mean itself, unlike a pure variance misspecification.

For a binary RI model, E(Y_it|X)=integral expit(eta_it+b)phi(b)db and Cov(Y_it,Y_is|X)=E_b[p_it(b)p_is(b)]-E_b[p_it(b)]E_b[p_is(b)] for distinct occasions under conditional independence. The integral is not evaluation at b=0. Logistic curvature changes sign, so a casual global Jensen inequality is not a valid proof for all random-effect distributions. A time-invariant subject-level predictor's conditional coefficient should not be described as an observed within-person exposure switch.

## 3. Mixture, Markov and membership likelihoods

**S/C.** A single-class mixture is sum_s pi_s product_t f_s(y_it), when one class applies to an entire subject. It is not product_t sum_s pi_s f_s(y_it), which reallocates independently at each occasion. An HMM instead sums over state sequences with transition factors. Chapter9's mixed-membership conditional Gaussian mean sum_m g_im h_km(t) is a third construction; it cannot be replaced with either mixture expression.

**M/P computational detail.** For an ordinary HMM, forward alpha_1(s)=rho_s f_s(y_1), alpha_t(s)=f_s(y_t) sum_r alpha_(t-1)(r)Q_rs, and L=sum_s alpha_T(s). Rescale each step or use log-sum-exp to avoid numerical underflow. Forward-backward marginal probabilities and a Viterbi most-likely joint path answer different questions. Integrating a persistent random effect out of a conditionally Markov model can induce longer memory.

For a multinomial-probit utility construction, a common additive utility location cancels from choices. Multiplication by **positive** c preserves the utility ordering and requires mean multiplication by c and covariance multiplication by c^2. Negative scaling reverses order and is not the same invariance. Fix reference differences and a positive scale to identify the model.

## 4. Mediation identities: specify the contrast scale

**M/C clarification of the Chapter8 compressed description.** The additive decomposition is for an additive counterfactual outcome contrast, not an unqualified hazard ratio. For a binary exposure, potential mediator M(a) and outcome Y(a,m), define

TE=E[Y(1,M(1))-Y(0,M(0))],
NDE(a)=E[Y(1,M(a))-Y(0,M(a))],
NIE(a)=E[Y(a,M(1))-Y(a,M(0))].

Then TE=NDE(0)+NIE(1)=NDE(1)+NIE(0) algebraically. A ratio-scale definition would require a corresponding multiplicative decomposition instead. Identification of these counterfactual expectations from observed data is an additional question and needs the relevant consistency, positivity and confounding/cross-world conditions. Exposure-induced mediator–outcome confounders complicate natural-effect identification; ordinary regression path products do not solve that problem.

In the source's multiple-intermediate-variable survival model, the regression path expressions retained in the knowledge file are explicitly **rare-outcome/low-cumulative-hazard approximations under the stated joint model and assumptions**. They are not a blanket exact natural-effect formula. A path through W and then M is already included in (gamma_W^T+gamma_M^T B_W)a_S and must not be counted twice.

For a right-censored subject with hazard h_i(t), log-likelihood contribution is delta_i log h_i(T_i)-integral_0^(T_i) h_i(s)ds. With piecewise-constant baseline lambda_h and a time-constant eta_i, the integral reduces to exp(eta_i)sum_h lambda_h exposure_ih. With Chapter9's time-varying trajectory predictor eta_i(s), it must remain sum_h integral_in_interval lambda_h exp(eta_i(s))ds. Numerical integration accuracy is part of validation, not an optional plotting refinement.

## 5. No new assessment burden

These definitions make the instructor review mathematically explicit. HW1 students are not asked to derive path sampling, conjugate matrix updates, a sandwich covariance, HMM recursions or natural-effect identification. The exact HW1 question/rubric scope remains unchanged. Codex must preserve the distinction between a whole-course reference and a 90-minute tutorial/assignment prerequisite.
