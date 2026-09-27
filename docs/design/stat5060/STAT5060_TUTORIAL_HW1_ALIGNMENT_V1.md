# STAT5060 Tutorial–HW1 Alignment V1

- Status: FROZEN_ALIGNMENT_GATE.
- Date: 2026-09-28.
- Source authority: `STAT5060_TUTORIAL_01_FROZEN_SPEC_V1.md`, `STAT5060_HW1_STUDENT_SPEC_V1.md`, original Chapters 1–3 and the derived canonical knowledge.
- Relation: this file owns the preparation/transfer audit. It cannot add a new assessed prerequisite or change a question's marks. Rubric dimensions below refer to `STAT5060_HW1_RUBRIC_V1.md`.

## 1. Complete alignment matrix

| Tutorial concept/skill | Tutorial case/slide | HW1 task | Expected transfer, not merely copied output | Rubric dimension / fairness |
|---|---|---|---|---|
| Observation, cluster and response units | Device/weekly rows, 02,13 | 1(a),3(a) | Distinguish participant requests from participant-weeks; do not use ID as a slope or count exposure as binary offset | Model formulation; explicitly prepared |
| Data checks, units, missingness | Device audit, 02–04 | 1(a), global submission | Verify a new frozen CSV rather than silently deleting rows | Correct implementation/reproducibility; prepared |
| Conditional mean/variance versus raw summaries | Faults, 03,05–07 | 1(a),1(c) | Reject raw variance>mean as a conclusive conditional Poisson test | Statistical reasoning; prepared |
| Exposure offset with coefficient one | Fault rate, 04,08 | 1(a),1(b),1(e) | Model requests per week; predict at an eight-week exposure | Model formulation/interpretation; prepared |
| Poisson versus NB2, shape conversion | Faults, 05–07 | 1(b),1(c) | Estimate dispersion and compare supported models on identical rows | Implementation/diagnostics; prepared |
| Pearson residuals, approximate D, zero probabilities, AIC | Faults, 05–07 | 1(c) | Use several diagnostics as evidence, not a package label or isolated p-value | Diagnostics/reasoning; prepared |
| What an offset changes | Fault rates and equal-exposure comparison, 04,08 | 1(d) | Deliberately omit offset when exposure differs by group; explain resulting distortion | **Intentional transfer** of a taught principle, not an unfair new method |
| Rate ratio, expected count and causal restraint | Faults, 08 | 1(b),1(e),2(d) | Separate count/rate association from learning benefit or causal effect | Interpretation; prepared |
| Nominal versus ordered categories | Inspection, 09 | 2(a) | Treat service channels as unordered | Model formulation; prepared |
| Baseline logits and softmax | Inspection, 10–11 | 2(a),2(b) | Manual probabilities for a new profile; interpret probability curves, not coefficient signs alone | Formulation/calculation/interpretation; prepared |
| Reference change as reparameterization | Inspection, 12 | 2(c) | New baseline workshop, subtract coefficient vectors and align labels before testing | Model understanding/correct execution; prepared |
| Different denominators mean different effects | Count→inspection transition, 08–10 | 2(d) | Explain rate ratio versus odds of one channel relative to another | **Intentional integration** across two taught cases |
| Conditional independence and a shared random intercept | Weekly alarms, 13–15 and bridge | 3(a),3(b) | Formulate participant-level variation, not independent visit effects | Formulation/likelihood; prepared explicitly even if Chapter3 lecture is later |
| Integrated likelihood | Weekly alarms, 15 | 3(a) | One integral per participant, product over weeks inside | Statistical correctness; prepared |
| ML, numerical approximation, convergence and singularity | Weekly alarms, 15,17 | 3(b) | Use the supplied scalar-RI R route and report diagnostics honestly | Correct implementation/computational diagnosis; prepared |
| Whole-panel plug-in predictive check | Alarm totals, 17 | 3(b) | Interpret 0–4 active-week frequencies under two dependence structures | Model diagnosis; helper supplied, no unintroduced simulation algorithm |
| b=0 versus integrating a nonlinear link | Weekly alarm profiles, 16 | 3(c) | Predict four new-participant profiles; explain the target difference | Interpretation/correct calculation; helper supplied |
| Conditional OR versus naive/marginal association | Weekly alarms, 14,16–17 | 3(c),3(d) | Avoid labeling coefficient differences an automatic same-target bias comparison | **Intentional transfer** of a taught target distinction |
| A limitation supported by diagnostics | End of each case, 07,12,17 | 1(d),3(d),4(d) | Name a testable concern or design limit rather than generic 'more data needed' | Reasoning; prepared |
| Simulation aim/DGP/target/method/performance | 18–19 | 4(a),4(b) | Change from correct/wrong variance at fixed n to whether larger n or NB fitting repairs inference | **Intentional transfer**, not a new estimator |
| Fair method comparison on identical responses | One iteration and saved records, 19 | 4(b) | Fit Poisson/NB to the same realization; preserve failed attempts | Execution/fairness; loop supplied |
| Bias/RMSE/empirical SE/RMS reported SE | 20 | 4(c),4(d) | Judge accuracy and reported uncertainty separately | Calculation/reasoning; prepared |
| Coverage, MCSE and B versus n | 18,20–21 | 4(a),4(c),4(d) | Explain why B=500 improves Monte Carlo precision but n=400 does not repair a wrong variance assumption by itself | Interpretation/calibration; prepared |
| Reproducible paths, seeds, warnings and disclosure | Scripts, handout, 24 | Process 5 points | Submit a runnable evidence-linked report in one supported language route | Reproducibility/communication; prepared |
| Bayesian workflow and diagnostics | 22–24 | No compulsory HW1 coding/task | Awareness transfers to later course work; no unannounced PyMC/Stan installation | **Deliberately not assessed in HW1** |

## 2. Explicit decisions for all proposed HW1 capabilities

| Capability | HW1 decision | Reason |
|---|---|---|
| Poisson with overdispersed count data | YES | Core conditional-variance reasoning. |
| Poisson versus NB2 | YES | Meaningful likelihood/uncertainty comparison, not a parameter swap. |
| Multinomial/nominal response | YES | Different outcome scale and transferable probability interpretation. |
| Reference category versus probabilities | YES | Algebra plus executable invariance check. |
| Longitudinal/clustered binary response | YES | Core dependence structure from Chapter3. |
| Naive GLM versus RI GLMM | YES | Different uncertainty and conditional/marginal targets. |
| Ordinal repeated data | NO, defer | Adds cutpoint/sign/model API burden beyond this 90-minute preparation; remains in the canonical course review. |
| Simulation calibration | YES | Evaluates a statistical procedure, not merely a loop. |
| Bias | YES | Required but not treated as sufficient evidence. |
| RMSE | YES | Joint precision/bias measure. |
| Empirical versus reported SE | YES | Direct explanation for miscalibrated intervals. |
| Empirical coverage | YES | Primary simulation question, with MCSE. |
| Model misspecification | YES | Variance, omitted exposure and dependence/target distinctions. |
| Visualization as diagnostic evidence | YES | Residuals, category probabilities, subject-total checks and coverage. |
| Bayesian workflow | Tutorial awareness YES; compulsory HW1 Bayesian coding NO | Ten minutes is insufficient preparation for a fair new Bayesian programming requirement; avoid environment burden. |

## 3. Prerequisites deliberately removed or supplied

No student must derive adaptive quadrature, implement GH nodes, construct a latent posterior sampler, repair an unfamiliar Python mixed-model package, solve label switching, write a C++ extension or reverse-engineer old WinBUGS input. Provide the RI probability integrator and panel-check helper with tests and a transparent explanation. The simulation starter provides data generation, attempt records and loop structure but leaves students to complete fits, summaries and reasoning; do not distribute filled HW1 answers in the starter.

R users are not required to learn Python. Python users are told in advance that the shared maximum-likelihood mixed-model fit uses R; the provided runner turns this into a documented command/output interface, not an assessed interoperability exercise. No hidden 'pure Python' solution based on a statistically different posterior approximation is presented as equivalent.

## 4. Pacing/workload decision and release gate

The 90-minute tutorial is an instructor-led case study with short student checks, not a hands-on installation workshop. Full MCMC and repeated simulations are cached. The eight-page HW1 report target and supplied helpers keep the estimated work at 11–15 hours; 100 marks are allocated across reasoning, implementation and diagnostics rather than four equally large coding projects.

A prerequisite gate before release checks that students have the Tutorial notes, fixture dictionary, setup path, RI bridge/helpers and simulation starter. Missing one of these is an **execution/materials defect to repair**, not an invitation to delete the corresponding learning objective. Administrative due-date and AI-policy adoption are separately recorded; no original 2025 date is inferred.

**Final alignment verdict: PASS_DESIGN.** Every assessed core skill is explicitly taught, intentionally transferred from a stated taught principle, or accompanied by a transparent supplied numerical helper. Actual material/code inclusion is a Codex validation gate.
