---
name: bayesian-ppl-diagnostics
description: Executable guidance for Bayesian workflows using Stan/CmdStanPy, brms, PyMC, and ArviZ, with legacy JAGS/OpenBUGS paths and Rcpp acceleration patterns.
status: active
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-05-14
profile_tags:
recommended_scope: project
license: Apache-2.0
metadata:
  skill-author: CardiacNexus maintainers
allowed-tools:
---
# Bayesian PPL and diagnostics

## Overview

This skill defines a **default HMC/NUTS-first** Bayesian stack (Stan family, PyMC) with **ArviZ** (Python) or **posterior / bayesplot / brms** utilities (R) for diagnostics. **Gibbs samplers** (JAGS, OpenBUGS/WinBUGS) are **legacy / reproduction-only** unless there is a documented reason to stay in BUGS language.

**Rcpp** is for **data wrangling, performance bottlenecks outside the sampler, and custom family math**—not for replacing Stan’s autodiff + NUTS as the main inference engine.

Primary references: [references/reference.md](references/reference.md).

## When to Use This Skill

Use when you:

- Fit or review **hierarchical / multilevel** models on tabular or imaging-derived phenotypes.
- Must **prove convergence and sampling quality** before interpreting posteriors.
- Choose between **Stan/CmdStanPy**, **brms**, **PyMC**, or **JAGS/OpenBUGS** for a given task.
- Integrate **prior/posterior predictive checks** and **simulation-based calibration** into a reproducible pipeline.

Do **not** treat “posterior means look reasonable” as sufficient evidence of a valid fit.

## Core Tooling / Preferred Stack

| Layer | Preferred tools | Role |
|-------|------------------|------|
| Language-first PPL | **Stan** + **CmdStanPy** (Python) or **rstan** / **cmdstanr** (R) | Custom models, stable NUTS, fine-grained control of sampling and diagnostics |
| R formula interface | **brms** | Standard GLMMs / multilevel models without hand-written Stan for common structures |
| Python PPL | **PyMC** | Notebook-centric workflows, tight coupling with NumPy/SciPy/xarray stacks |
| Diagnostics (Python) | **ArviZ** | `InferenceData`, R-hat, ESS, BFMI, PPC plots, LOO hooks |
| Legacy Gibbs | **JAGS** + **R2jags**; **OpenBUGS** / **WinBUGS** | Reproduce historical BUGS models; teaching; interoperability |
| Acceleration (R) | **Rcpp** (+ Armadillo/Eigen as needed) | Fast pre/post processing, custom brms families, not the main sampler |

**CmdStanPy** is documented primarily via **Stan documentation and the CmdStanPy manual**—treat the official docs as the canonical citation surface, not a single “CmdStanPy paper.”

## Workflow / Decision Rules

### Route selection (which engine first?)

- **Prefer Stan / CmdStanPy** when:
  - The model is **mostly custom** (non-standard likelihoods, ODEs, complex constraints, heavy control of generated quantities).
  - You need **stable HMC/NUTS** with explicit control of adaptation, treedepth, and metric.
  - You need **fine-grained diagnostics** and reproducible Stan programs versioned in git.

- **Prefer brms** when:
  - The task is a **standard hierarchical / GLMM** structure and a formula interface reduces error.
  - You want **fast iteration** without maintaining `.stan` files, and the model maps cleanly to brms’ supported families.

- **Prefer PyMC** when:
  - The workflow is **Python-native** (Jupyter, PyTensor graphs, tight integration with ArviZ and scientific Python).
  - You need flexible **model composition** in Python without a separate Stan file.

- **Fall back to JAGS / OpenBUGS / WinBUGS** only when:
  - You must **replicate an old paper** or run a **legacy BUGS/JAGS** codebase.
  - Historical **discrete-parameter** Gibbs formulations are the explicit target (still consider rewriting in Stan with marginalization when possible).

**New project default:** Stan/brms/PyMC — not JAGS.

### Rcpp: allowed roles

- **Do:** vectorized data prep, expensive covariate construction, lookup tables, custom **un-normalized** log-likelihood pieces exposed to **brms** custom families, or post-processing of posterior draws.
- **Do not:** reimplement HMC or expect Rcpp to fix a misspecified hierarchical geometry; **reparameterize the model** instead.

### Diagnostic workflow (mandatory gates)

Treat the following as **blocking** before scientific conclusions. Use ArviZ (`az.summary`, `az.plot_trace`, `az.plot_rank`, energy plots) or equivalent R tooling.

1. **Divergent transitions (HMC/NUTS)**  
   - **Meaning:** numerical instability or **geometry too difficult** for current parameterization / step size.  
   - **First response:** increase `adapt_delta` / `target_accept` (Stan/PyMC), then **non-centered** reparameterization for hierarchical scales, then **rescale** covariates / outcomes.  
   - **If still present:** treat as **model misspecification** or **prior/data conflict** until proven otherwise.

2. **Max treedepth hits**  
   - **Meaning:** trajectories hitting the cap; often **strong posterior correlation** or **funnel** geometry.  
   - **Action:** reparameterize (non-centered), simplify model, or allow deeper trees **only after** ruling out misspecification.

3. **E-BFMI (Bayesian fraction of missing information)**  
   - **Meaning:** low values suggest **difficult global exploration** (often funnels).  
   - **Pair with:** divergences and energy Bayesian bootstrap checks; fix geometry before “more iterations.”

4. **R-hat**  
   - Use **split R-hat**; flag **> 1.01** (stricter thresholds for publication-critical parameters).  
   - **High R-hat** is not fixed by wishful thinning—**run longer**, **more chains**, or fix parameterization/multimodality.

5. **Bulk vs tail ESS**  
   - Report **both** when using ArviZ defaults.  
   - Tail ESS matters for **extreme quantiles** and **tail statements** (e.g. odds ratios far from 0).

6. **Posterior predictive checks (PPC)**  
   - Test **systematic discrepancies** between replicated and observed data (not just overlap).  
   - Failure suggests **wrong likelihood**, **missing structure**, or **wrong link**, not “tweak priors only.”

7. **Prior predictive checks**  
   - Run **before** or alongside early fits to ensure priors imply **plausible observables**.  
   - If observables are impossible under the prior, the problem is usually **prior / scale**, not the MCMC run.

8. **Simulation-based calibration (SBC)**  
   - When feasible, use **SBC** to check **entire inference pipeline** (model + sampler settings) over simulated datasets. Flag **systematic coverage errors**.

9. **Non-centered parameterization**  
   - Default for **hierarchical scales and group effects** when centered parameterization shows divergences / low BFMI.  
   - If non-centered is worse (rare), document **why** and show diagnostics for both.

### Disentangling failure modes

| Symptom cluster | Likely cause | What to change first |
|-----------------|--------------|----------------------|
| PPC fails on **location/scale** of data | Likelihood / link / missing covariates | Model structure |
| PPC OK but **prior predictive** absurd | Priors off by orders of magnitude | Priors + measurement scales |
| Divergences + low BFMI, bad funnel plots | Geometry / parameterization | Non-center, rescaling |
| R-hat high, chains stuck in modes | Multimodality / label switching | Model constraints, stronger priors, different likelihood |

## Common Pitfalls / Validation Notes

- **No saved seeds, chain count, thinning policy, and package versions** → results are not auditable.
- **Ignoring divergences** because trace plots “look mixed.”
- **Flat or overly wide priors** on scales → funnel geometry; fix with weakly informative priors and **standardization**.
- **Mixing Stan and JAGS** in one pipeline without documentation and version pins.
- Publishing **posterior means** without **uncertainty intervals** and diagnostic summary tables.

## References

Canonical papers and documentation URLs are maintained in [references/reference.md](references/reference.md).
