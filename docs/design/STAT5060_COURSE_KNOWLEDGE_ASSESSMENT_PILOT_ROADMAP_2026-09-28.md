# STAT5060 Course-Knowledge / Assessment Pilot Roadmap

Status: ACTIVE — two-day delivery sprint  
Date: 2026-09-28  
Canonical repo for reusable knowledge/plugin work: `YuukiAS/AI_Skills_Collection`

## 1. Purpose

Use STAT5060 as the first real course-scale pilot for upgrading the Statistical Modeling and Scientific Visualization knowledge layers.

The immediate objective is **not** to redesign a plugin first. The urgent objective is to produce course materials that are pedagogically useful, statistically correct, current, reproducible, and independently reviewed. Durable knowledge is extracted into reusable Skills/plugins only after the course deliverables have frozen.

The two student-facing deliverables are:

1. a usable 90-minute Tutorial covering the material needed before HW1;
2. a publishable HW1 package: assignment, reference solution, runnable code, and explicit rubric.

An internal polished whole-course PDF is a required Day-1 intermediate artifact for knowledge freeze and instructor review, but is not a third student-facing deliverable.

## 2. Current assessment architecture

Current course weights supplied for 2026/27:

- Attendance: 20%
- Assignment 1: 20%
- Assignment 2: 20%
- Final Project: 40%

Working assessment-role split:

### Homework

Homework is primarily a **guided learning + transfer + feedback** instrument.

It should test whether students can:

- translate a scientific/data question into an appropriate statistical model;
- implement the model reproducibly;
- diagnose assumptions and model failures;
- compare plausible alternatives;
- interpret estimates, uncertainty, predictions, and diagnostics;
- explain why a method is appropriate rather than merely call a package.

Homework should not be designed mainly as an AI-detection mechanism. AI-assisted coding/debugging/explanation may be allowed under an explicit disclosure rule, subject to the instructor's final course policy.

### Final Project

The Final Project is the main integrative assessment. The current working design is:

- written/data-analysis project: 25 percentage points;
- oral defense: 15 percentage points.

The oral-defense design remains governed by the separate SeminarArc STAT5060 roadmap. The intended role of the defense is to test ownership and understanding of the submitted analysis, not to detect whether AI was used.

Working defense structure:

- 60–90 second project introduction;
- Q1: project/results understanding;
- Q2: course-method/statistical understanding;
- Q3: integrative reasoning, perturbation, limitation, or alternative-model reasoning;
- follow-ups immediately after the related main question;
- no AI assistance during the defense;
- examiner-controlled evidence display and continuous audio/markers.

The exact 25/15 split remains a course-design working decision until formally approved by the instructor.

## 3. Source authority and repository boundary

Course source material currently lives in the configured Google Drive STAT5060 folder and includes:

- syllabus / assessment material;
- Chapter 1–9 lecture notes;
- prior Tutorial materials;
- prior HW1/HW2;
- Final Project instructions;
- legacy R / WinBUGS examples.

The Google Drive source files are authoritative course inputs. Do **not** copy source PDFs wholesale into this public repository unless licensing and publication are explicitly approved.

This repository may contain:

- derived knowledge maps;
- rewritten notes;
- software/workflow mappings;
- executable examples that are newly authored;
- assessment-design artifacts;
- critic reports;
- reusable Skill/plugin knowledge extracted after freeze.

SeminarArc separately owns the oral-defense application/runtime and its course-pack implementation.

## 4. Core teaching philosophy for the pilot

The Tutorial and HW1 should be case-driven rather than package-driven.

Default explanatory order:

1. scientific or data-analysis question;
2. data-generating/data-structure issue;
3. model choice and assumptions;
4. estimation/computation;
5. diagnostics and failure modes;
6. interpretation;
7. alternative model / sensitivity question;
8. reproducible implementation.

Do not replace WinBUGS with a different package tutorial and call that modernization.

Modernization means teaching a current analysis workflow while preserving the statistical ideas behind the course.

## 5. Provisional software policy to validate and freeze on Day 1

R remains the primary teaching environment for models where its statistical ecosystem is strongest. Python is used as a deliberate secondary implementation where it helps students transfer the modeling workflow.

Provisional map:

- GLM: R `stats` / `MASS`; Python `statsmodels`
- nominal / ordinal models: R `nnet`, `ordinal`; Python `statsmodels` where mature
- GLMM / multilevel: R `lme4`, `glmmTMB`; Python only when the implementation is sufficiently mature and pedagogically clean
- modern Bayesian high-level R: `brms`
- modern Bayesian computational layer: Stan / `CmdStanR`
- modern Bayesian Python: PyMC + ArviZ
- finite mixtures: R `mclust` / `flexmix`; Python mixture tooling where appropriate
- missing-data workflow: R `mice` plus explicit discussion of missingness assumptions
- HMM: current R/Python HMM implementations selected after Day-1 verification

Legacy/software-development positioning:

- WinBUGS: historical context only; no GUI-operation teaching
- JAGS / `R2jags`: mention as a maintained BUGS-family continuation when relevant; not the primary 2026 teaching path
- `Rcpp`: explain only as a performance/development layer; not a Tutorial requirement
- TMB / automatic differentiation: optional "under the hood" context for advanced computation; not required student syntax

### PyMC scope in Tutorial

Target: approximately 8–12 minutes, not a full PyMC lesson.

Students should see:

- model declaration;
- prior meaning;
- posterior sampling;
- `R-hat` / effective sample size / divergence as basic diagnostics;
- posterior predictive checking.

Do not teach HMC/NUTS derivations, PyTensor internals, custom samplers, or backend engineering in Tutorial 1.

## 6. Day 1 — whole-course knowledge freeze + Tutorial build

Day 1 must end with the whole-course knowledge base frozen enough to support Tutorial/HW1 authoring.

### 6.1 Whole-course knowledge extraction

Read Chapter 1–9 and reconcile them into one canonical internal structure:

For each model family, record:

- motivating data structure / scientific problem;
- formal model;
- notation and parameter meaning;
- assumptions;
- identifiability constraints;
- frequentist and/or Bayesian estimation route;
- computational mechanism;
- diagnostics;
- interpretation;
- common failure modes;
- modern R/Python implementation;
- links to adjacent chapters.

Do not silently "correct" course content. Distinguish:

- what the existing course explicitly teaches;
- what is being modernized or added;
- what is a current external best-practice recommendation.

### 6.2 Internal polished course PDF

Generate an instructor-facing review PDF covering the complete course.

The PDF is not a slide dump. It should be usable for rapid course refresh and later plugin extraction.

Target chapter template:

- intuition / use case;
- model and notation;
- estimation;
- diagnostics;
- implementation;
- interpretation;
- failure modes;
- modern workflow note.

### 6.3 Tutorial 1

Tutorial covers material needed before HW1 and should be case-study-first.

Current candidate structure, subject to source/software verification:

1. count-data case: Poisson model, overdispersion, negative-binomial alternative;
2. nominal/categorical case: reference category, predicted probabilities, interpretation;
3. repeated-measures case: why within-subject correlation requires a mixed model;
4. Monte Carlo simulation: bias, RMSE, empirical coverage, model misspecification;
5. short modern Bayesian workflow demonstration with PyMC/ArviZ;
6. HW1 expectations, reproducibility, interpretation, and AI-use policy.

R is the main executable spine. Python examples are included when they clarify transfer across ecosystems rather than duplicating syntax.

### 6.4 Day-1 gate

Day 1 is not complete until:

- Chapter 1–9 knowledge matrix exists;
- notation conflicts/gaps are recorded;
- current software claims have been verified against current official documentation;
- internal PDF renders correctly;
- Tutorial has runnable source, not only slides;
- estimated live duration is approximately 90 minutes;
- a critic has checked statistical accuracy and tutorial-to-HW readiness.

## 7. Day 2 — HW1 + final Tutorial convergence

### 7.1 HW1 design

HW1 must not be a parameter-swapped copy of prior HW1.

Preferred structure: a small number of connected case-based tasks that require model choice, computation, diagnostics, and interpretation.

The assignment should include meaningful transfer beyond the exact Tutorial examples.

Candidate abilities to assess:

- distinguish Poisson vs overdispersed count behavior;
- interpret nominal-model probabilities and reference-category changes;
- recognize dependence in repeated/clustered data;
- compare naive GLM vs mixed model;
- conduct a genuine simulation-calibration study using more than a token number of replications;
- report bias, RMSE, uncertainty/coverage and diagnostic evidence;
- explain model failure and a defensible alternative.

A full Bayesian programming task is not automatically required in HW1. It should be included only if Tutorial exposure, software setup, time burden, and assessment value justify it. Otherwise reserve deeper Bayesian implementation for HW2 / Project.

### 7.2 HW1 package

Required release package:

- student-facing HW1;
- supplied data / deterministic data-generation instructions;
- runnable R solution;
- Python solution where Python is officially supported for that task;
- reference numerical/graphical outputs;
- instructor solution with reasoning;
- explicit scoring rubric;
- AI-use statement template / course policy text;
- environment/package requirements.

### 7.3 Rubric principle

The rubric should reward statistical reasoning rather than code volume.

Provisional dimensions:

- model formulation / choice;
- correct and reproducible implementation;
- diagnostics / model comparison;
- interpretation / statistical reasoning;
- communication, reproducibility, and required AI disclosure.

Exact points are frozen only after the final task set is known.

### 7.4 Day-2 gate

No release until four independent checks pass:

1. **Statistical critic** — equations, parameterization, assumptions, identifiability, inference, interpretation.
2. **Pedagogy/alignment critic** — Tutorial genuinely prepares students for HW1 without making HW1 a copy exercise.
3. **Assessment/AI-resilience critic** — questions require understanding and transfer even when AI assistance is allowed.
4. **Execution critic** — clean-environment rerun regenerates all required outputs.

## 8. Tool/agent responsibility — freeze this before execution

### ChatGPT Pro / strategic planner

Use for:

- reading and synthesizing the Drive course corpus;
- deciding course-wide notation and knowledge structure;
- current web research on statistical practice/software;
- pedagogy and assessment design;
- resolving tradeoffs such as R vs Python, PyMC depth, AI policy, and rubric;
- reviewing rendered PDF/slides/HW;
- final critic and revision decisions.

ChatGPT is the authority for **what should be taught and assessed** during this sprint.

### Codex / repository executor

Use after the plan and current source set are sufficiently frozen.

Codex owns:

- repository organization;
- Quarto/Markdown/LaTeX source construction;
- R/Python notebooks/scripts;
- package/environment setup;
- running all examples;
- generating plots/tables;
- building PDFs;
- tests/reproducibility checks;
- mechanical consistency fixes;
- implementing critic-approved revisions.

Codex should not independently redefine course pedagogy, assessment philosophy, or software-policy decisions.

### Skills/plugins

**Do not make the plugin the dependency for these two-day deliverables.**

Plugin/Skill work starts only after the course knowledge and Tutorial/HW1 are stable.

Then extract durable reusable knowledge into:

- Statistical Modeling: model choice, assumptions, estimation, diagnostics, interpretation, simulation design, failure modes;
- Scientific Visualization: statistical graphics that support diagnosis, uncertainty, calibration, model comparison, and communication.

Course-specific wording, deadlines, marks, or answer keys must not leak into a general-purpose plugin.

## 9. Execution order

The required sequence is:

1. Planner freezes source inventory and software-research questions.
2. Planner performs current external research.
3. Planner freezes Chapter 1–9 canonical knowledge map.
4. Codex materializes the internal polished PDF and executable examples.
5. Critic reviews Day-1 knowledge/PDF/Tutorial.
6. Planner resolves critic decisions.
7. Codex builds HW1, solution, rubric, and release package.
8. Critics review statistics, alignment, AI resilience, and reproducibility.
9. Codex applies bounded fixes.
10. Planner performs final release decision.
11. Only after release freeze, extract generalized knowledge into Skills/plugins.

## 10. Explicit non-goals for the two-day sprint

Do not:

- rebuild Statistical Modeling as a prerequisite;
- bulk-import textbook content into a plugin;
- teach WinBUGS GUI operation;
- turn Tutorial into an R/Python package catalogue;
- force equal R/Python coverage;
- teach Rcpp merely because it is modern infrastructure;
- use AI detection as the principal assessment mechanism;
- publish HW1 before solution/rubric/reproducibility are simultaneously ready;
- let an executor silently change the assessment philosophy.

## 11. Success condition

At the end of Day 2, success means:

- the instructor can teach the Tutorial for ~90 minutes from the released materials;
- the Tutorial materially prepares students for HW1;
- HW1 is meaningfully different from the prior generate-fit-repeat template;
- the solution and rubric make grading predictable and defensible;
- all code runs;
- AI policy is explicit;
- Project and Homework have distinct assessment roles;
- the reusable course knowledge is structured well enough for a later Statistical Modeling / Scientific Visualization plugin upgrade without blocking the immediate course delivery.
