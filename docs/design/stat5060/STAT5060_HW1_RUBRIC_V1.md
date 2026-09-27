# STAT5060 HW1 Rubric V1

- Status: FROZEN_100_POINT_RUBRIC_FOR_CODEX.
- Date: 2026-09-28.
- Source authority: the complete HW1 student spec and frozen assessment philosophy.
- Relation: this file owns point allocations and consistent marking rules. The student spec owns requested work; the private solution owns worked results. No code style, software brand or AI-use preference may create an extra criterion.

## 1. Point ledger

Use integer or half-point marks consistently. Each row's component marks sum exactly to its stated maximum. Full marks require the requested evidence and its statistical meaning, not a pasted package output. Assign partial credit at component level; do not apply an additional global penalty for the same error.

| Part | Maximum | Exact components for full credit |
|---|---:|---|
| 1(a) | 6 | Data/ID/missingness/count/exposure audit 2; correct log-rate equation and offset units 2; conditional independence/mean assumptions 1; conditional versus raw variance distinction 1. |
| 1(b) | 6 | Both requested fits on identical rows/predictors/offset, estimated NB shape and labeled coefficient/SE/AIC table 4; rate ratio and correctly transformed 95% Wald interval 2. |
| 1(c) | 8 | Correct residual construction and informative labeled residual plots 3; D calculation with stated divisor/approximate interpretation 1; observed and fitted zero proportions 2; integrated diagnostic/AIC reasoning, including limits, 2. |
| 1(d) | 6 | Correct no-offset sensitivity refit/comparison 2; explanation of exposure/group distortion rather than 'NB fixes everything' 2; defensible recommended analysis and a relevant limitation 2. |
| 1(e) | 4 | Correct two eight-week predictions plus difference/ratio 2; expected-count/rate/causal interpretation 2. |
| **Q1** | **30** | |
| 2(a) | 5 | Correct two nominal reference equations, online baseline and parameter identities 3; correct unpenalized fit/table with category mapping and SEs 2. |
| 2(b) | 7 | Two profiles and one explicit softmax calculation 3; complete labeled probability curves for both groups 2; probability contrast and relative-logit interpretation 2. |
| 2(c) | 4 | Correct reference-transformation algebra 2; aligned-label probability invariance check, numerical difference and explanation 2. |
| 2(d) | 2 | Correct distinction between request rate ratio and channel-versus-reference odds ratio, with the actual denominators 2. |
| **Q2** | **18** | |
| 3(a) | 6 | Observation/cluster units 2; both mean models and distribution/independence assumptions 2; correct integrated likelihood with visit product inside subject integral 2. |
| 3(b) | 7 | Requested ML fits, fixed-effect/SE and RI-SD results 3; convergence and singularity evidence 1; correctly generated/labeled observed-versus-plug-in panel diagnostic 1; interpretation of pattern and envelope limitations 2. |
| 3(c) | 8 | Four-profile table containing all three requested probabilities 3; correct conditional-versus-integrated target explanation and use of helper 3; conditional OR interpretation, not population risk ratio, 2. |
| 3(d) | 4 | Responsible coefficient comparison recognizing different targets/nonlinear averaging 2; a specific remaining assumption/limitation and relevant evidence 2. |
| **Q3** | **25** | |
| 4(a) | 4 | Aim/DGP/target/method/performance description 2; n versus B distinction 1; defensible expected pattern with reasoning 1. |
| 4(b) | 5 | Paired same-data method fits over all specified attempts/scenarios 2; correct unknown-shape NB and model-based Wald comparison 1; complete warnings/refits/validity/failure accounting without replacement datasets 2. |
| 4(c) | 7 | Complete correctly calculated performance table 3; correct bias/RMSE/empirical-SE/RMS-SE definitions 2; coverage/MCSE and valid-denominator treatment, including B=500 versus 10 explanation, 2. |
| 4(d) | 6 | Correct coverage plot with nominal line and labeled Monte Carlo error bars 2; conclusion jointly using bias, SE comparison and coverage 3; distinction between substantial failure and Monte Carlo fluctuation 1. |
| **Q4** | **22** | |
| Process | 5 | End-to-end runnable source/README 2; unchanged data, stated seeds, environment and warning record 1; clear labeled concise communication 1; AI-use statement/no-AI statement 1. |
| **TOTAL** | **100** | **30+18+25+22+5=100; assignment course contribution = score/100 × 20%.** |

## 2. Stable partial-credit anchors

For a two-point conceptual component: 2 for correct reasoning tied to the task; 1 for the right idea with an important ambiguity or incomplete application; 0 for a contradictory/missing explanation. A one-point component can receive 0.5 for a meaningful partial demonstration. For a three/four-point implementation component, distinguish a correct model with a local repairable extraction mistake from fitting the wrong response, likelihood or dependence structure.

A correct numeric table with no requested interpretation receives only the numeric/implementation component marks. A persuasive paragraph contradicted by its own model/code does not receive full statistical credit. Conversely, a local arithmetic typo need not erase an otherwise correct model explanation.

### Error examples and maximum scope of deduction

| Error | Stable treatment |
|---|---|
| Reports exp(beta) correctly but transforms SE instead of CI endpoints | Deduct the affected interval portion of 1(b), normally 1 point; retain correct model/rate interpretation credit. |
| Omits the offset unintentionally throughout Q1 | Lose the offset-formulation and affected fitting/comparison components. Award follow-through for correctly computed predictions/ratios under the displayed fit and any valid diagnostic reasoning. Do not automatically assign zero to all Q1. Deliberate no-offset fit in 1(d) is required, not an error. |
| Treats raw variance>mean as conclusive proof | Lose 1(a)'s conditional-variance point and only independently incorrect diagnostic reasoning in 1(c); do not deduct again merely because the raw summary appears in a table. |
| Uses statsmodels GLM NB with fixed default alpha while claiming shape was estimated | Lose the estimated-shape/correct-NB portions of the relevant fit; retain correct Poisson and general NB reasoning. Flag the parameterization issue in feedback. |
| Converts MASS theta to PyMC alpha by inversion | This is conceptual parameterization failure; deduct the affected NB/variance interpretation components. Correct unrelated results remain credited. |
| Reference labels differ but probabilities and transformation are correct | No deduction after reconciling explicit labels; software's default ordering is not a grading rule. |
| Compares probability columns without aligning labels | Lose the executable invariance-check portion of 2(c); retain correct algebra if present. |
| Fits an ordinal model to preferred channel | Lose nominal formulation/fit components; assess remaining transferable explanations separately rather than pretending the requested model was fit. |
| Calls b=0 a population-averaged probability | Lose the target distinction in 3(c); do not penalize correctly computed b=0 numbers as arithmetic errors. A correct independent integral elsewhere can earn its own credit. |
| Uses a Bayesian/VB mixed fit as if it were glmer ML | Lose the requested-estimator implementation component; assess any correct conditional likelihood/interpretation independently. No undisclosed substitution earns full equivalence credit. |
| Says any difference between naive and conditional coefficients proves bias for one common parameter | Lose the target-comparison component of 3(d). |
| A same-data NB refit resolves a warning, with full logs | No penalty for the existence of the warning. Validity depends on the final fit and transparent record. |
| Deletes failed replications without reporting denominator | Lose failure-accounting and affected coverage-denominator credit; do not demand replacement datasets. |
| Labels mean reported SE as RMS reported SE | Deduct the affected summary-definition/calculation component; both are meaningful summaries, but the requested statistic must be correctly labeled and computed. |
| Coverage is .93 rather than exactly .95 in a finite simulation | No automatic deduction. Evaluate MCSE, estimator validity and interpretation. |
| Honest alternative model recommendation supported by diagnostics | Do not penalize the recommendation merely for differing from the answer key, provided the requested candidate fits and comparisons were performed correctly. |
| Uses base R, tidyverse or a different readable plotting style | No deduction for style/API preference; assess labels, units, readability and evidence. |
| Report over eight pages | Address only the explicit communication component, at most 1 point, for unnecessary overlength; do not silently discard statistical evidence or create an unannounced grade cap. |
| Missing AI statement | At most the stated 1 process point initially; seek clarification/correction under the course process. Suspected dishonesty is a separate institutional procedure, not detector-based extra deductions. |

## 3. Numerical tolerance and alternative software

Case data are fixed; student results should be reproducible from their code. Use full-precision results to check and sensible rounded numbers in reports. Ordinary deterministic R/Python comparisons use the software policy's tolerances: Poisson/nominal coefficient tolerance 1e-4, NB2 coefficients 1e-3, probabilities 1e-5, compatible log likelihoods 1e-3. A student's reporting to three decimals is acceptable and is not tested against an unrounded 1e-5 bound.

NB2 reported SEs may differ slightly with information conventions; up to approximately 5% relative difference, with the same mean model and a documented reasonable estimator, is normally numerical rather than conceptual. Near zero, use an absolute tolerance and inspect the implementation. Scalar GLMM comparisons must account for quadrature/optimizer tolerance; the frozen high-order Python design pilot is corroborating evidence, not a claim that R output has already been run. Codex produces the actual R reference and checks it against the pilot.

For simulation, identical R and NumPy integer seeds do not imply identical response draws. Grade correct design, saved records, definitions, reasonable numerical behavior and MCSE-aware interpretation. Do not insist on the private pilot's exact coverage or RMSE. Strict cross-language testing uses a common stored response matrix; students are not required to reproduce another language's RNG. Unusual but correctly documented simulation results prompt code/data review, not an automatic deduction for failing a preferred narrative.

No marks are allocated to building an optimizer, implementing quadrature or writing an interoperability wrapper; supplied helpers must be available. An equivalent legitimate implementation can earn full credit when it preserves the requested likelihood, estimation objective, data coding and prediction target.

## 4. Marker procedure

Before marking the class, two markers or the instructor/TA jointly review three anonymized mock solutions: (i) correct but terse; (ii) one local coding mistake with good reasoning; (iii) clean package output with conceptual target errors. Apply this ledger and record any disagreement at the component level. This calibration is not a new scoring model.

For each submission, keep part scores, a short root-error description and any follow-through credit. Verify at least a targeted code/output consistency sample. Do not automatically run untrusted submitted code with broad filesystem/network access; use a bounded teaching execution environment. AI disclosure is checked for completeness, not for how many prompts were used. Human graders determine marks; no AI automatic grade is a frozen requirement.

The private solution may supply acceptable alternative reasoning and numeric checks, but cannot introduce hidden questions, extra negative marks or a penalty for choosing an evidence-supported conclusion.
