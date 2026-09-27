# STAT5060 Source Inventory and Provenance V1

- Status: SOURCE_READING_COMPLETE_FOR_FROZEN_SCOPE; original files remain outside this repository.
- Date: 2026-09-28.
- Source authority: connected Google Drive STAT5060 folder and the two specified GitHub roadmap files, read directly rather than reconstructed from memory.
- Relation: this file owns locators, reading scope, provenance and fixed data identity. The knowledge file owns statistical interpretation/corrections; the software/AI files own external-source conclusions.

## 1. Authority order

1. Current user instructions establish the 2026 assessment weights and this sprint's scope.
2. The supplied course PDFs establish what the original course actually contains. Their historical dates/weights do not override current instructions.
3. `docs/design/STAT5060_COURSE_KNOWLEDGE_ASSESSMENT_PILOT_ROADMAP_2026-09-28.md` at `9d1923d2002c529352ad6464599e7da08eb6787c` establishes the existing pilot roadmap.
4. `YuukiAS/SeminarArc/docs/plans/stat5060-oral-defense-pc-roadmap.md`, file blob `a380e0fdfc84a1acc3c60306629f507ab877bbcc`, establishes the previously designed oral structure. Read the full file, including privacy/difficulty/recording sections; do not redesign the PC product here.
5. Current primary official documentation supplies explicitly labeled modernization, not retroactive claims about what the lecturer taught.

Repository governance read: `AGENTS.md` relevant planner/executor/reviewer, source/generated, privacy, branch/worktree, release and artifact-review sections; root `TODO.md`; `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`. This is course-content planning, not a plugin maintenance implementation task; it creates no new plugin, maintenance issue, watcher or control plane. Repository/plugin version decisions: **NO_BUMP**, documentation-only.

## 2. Drive structure actually inspected

Root: https://drive.google.com/drive/folders/1oWbzJErw8x08FWnzkx98n_qh1IMSeGYt

- Lecture Notes folder: `1_jQY4fmknPmLfSERk-75DlSOLoKaBoUn` — Chapter1 through Chapter9 and Chapter3_Supplement.
- Tutorial folder: `1MpGQ_4TnBoGZ7zG4Z0-2v_S1wdk1JPhf` — old tutorial, MH supplement, Bayesian SEM/WinBUGS material, examples and installation/background files.
- Tutorial/examples: `1D3zkqnPAQvltXpvQ4f-vUxxig55v8KH2` — count/ordinal/linear/multilevel/mixture R scripts, BUGS linear model, GLMM and ordinal documentation.
- Tutorial WinBUGS background folder: `1lc1Pxgv50lOJUflPC0DN8Zx5ePBjuq6y` — appendix and legacy installer archive.
- Interactive model subfolder: `1QFN5zAaxJ872xScpwKBfDMxtAOgcYFXN` — model.odc, inventoried as obsolete GUI material.
- Assignments folder: `1CZJypbNebi-msraGE-X3zyNrW8Hhbpwf` — HW1 and HW2 folders, current old-assignment copies and auxiliary materials.
- Root Final Project.pdf and Syllabus.pdf.

`.DS_Store`, the WinBUGS installer ZIP and the obsolete interactive ODC file were inventoried but not executed. An older HW2 machine-named duplicate and score data were not treated as a new 2026 assignment authority. No broad unrelated repository traversal was performed.

## 3. Core PDFs: actual reading and exact identity

Drive URLs for individual files use `https://drive.google.com/file/d/<ID>/view`. All page references in the knowledge file are physical one-based PDF pages.

| ID | File / physical pages | Drive file ID | Reading scope |
|---|---|---|---|
| C1 | Chapter1.pdf / 50 | 1U4Wv1yA0xIiroyaNY6Rl7RL1IwymxapT | Full text; likelihood/Bayes, augmentation, computation, criteria and shrinkage. Critical equations visually checked. |
| C2 | Chapter2.pdf / 50 | 1QUfZtvnIHkf6mJa_GUBHQuX-2j_hvlIu | Full text; GLM response families, cases, links, ordinal and utility constraints. Critical equations visually checked. |
| C3 | Chapter3.pdf / 33 | 1svWMsHSsCrLcKL-UApoAQe1aumNCa1d0 | Full text; repeated count/binary/ordinal/nominal models. Wheeze table and insomnia sign/cutpoint pages visually checked. |
| C4 | Chapter4.pdf / 32 | 1cJ9j5mudhdOZFhlvM7_iG-AV0jMFQXNt | Full text; multilevel, varying coefficients, residual heterogeneity, area counts and growth. |
| C5 | Chapter5.pdf / 35 | 1J9W2cQXn-zHAX5nR_wrKcSohypaEgkyc | Full text; mixture models, estimation and comparison. Conjugate-update pages visually checked. |
| C6 | Chapter6.pdf / 32 | 1xzLcgJMuYD-TGh_W2inL1K30C_1Hh04Q | Full text; MCAR/MAR/MNAR, selection/pattern/shared models and multiple imputation. |
| C7 | Chapter7.pdf / 32 | 1xEoZ1o4lRnT_w0lolNv0SRHfe3w0d8D5 | Full text; HMM, mixed HMM and latent measurement/state models. |
| C8 | Chapter8.pdf / 29 | 1AwhHT-zINpjSsU1Fzr-viFH_ngfUdTeA | Full text; latent mediation and event-time model, identification and approximation conditions. Path page visually checked. |
| C9 | Chapter9.pdf / 40 | 1AC2_9q76uAHgekb7Y8J7APytQyTbIMfu | Full text; mixed-membership trajectories and survival. Weighted-mean/prior pages visually checked. |
| CS | Chapter3_Supplement.pdf / 37 | 1UGwdoS8yRa0mevcLQDISBX7FNqzrLWFv | Full text; latent measurement/structural/shrinkage material, used to delimit rather than expand HW1. Footer numbering differs from physical pages. |
| H1 | HW1.pdf / 2 | 1ZeUMz2iAmDBqNmQQCemDTgNQZ1W0DjIO | Complete questions, generation parameters, B=10 instructions and repeated ordinal task. |
| H2 | HW2.pdf / 1 | 1LtgsQSBqWX50kiqVQnr2HzulLyLp0u9z | Complete tasks: multilevel score example, Gaussian mixture and missing longitudinal binary data. |
| FP | Final Project.pdf / 1 | 1om_Sr0i69-zW7eVXZC8dMX-dRPO8dmZ7 | Complete requirements and structure; source page visually checked. |
| SY | Syllabus.pdf / 11 | 1ka6SUslgJUNE99MhuwEG2CY7JzPOMDX9 | Full course/assessment/policy text, with historical/current conflicts recorded. |
| T0 | tutorial.pdf / 30 | 1D7prKzofDRakfhowLE6AMMaPWtJrsX0h | Full tutorial text, including package simulation examples and legacy GUI orientation. |
| MH | MH-algorithm.pdf / 15 | 1YkLqiQCAT01lmp8C_YtYo-VVY_HkDaJ9 | All pages inspected, including nonlinear latent-model full conditionals, proposal ratio and sampling discussion. |

Critical visual checks used locally rendered source pages; original slide screenshots/contact sheets are not exported to this public repository. Text extraction was used for systematic reading; no OCR-derived equation was accepted without mathematical/visual checking of ambiguous expressions.

### SHA-256 of core original PDFs

```text
Chapter1.pdf ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
Chapter2.pdf 6809d424f9fd8096f578b54873b035a257d67da38cd31195d68d5f70e30e1826
Chapter3.pdf cfe7b2c76da9a715dab0bc919319643330959bfe5e1d891061a84794588baa82
Chapter4.pdf 12049140b5e70048403fc8d7b1ed5090f24128288405bcad29a1c426d3bc2232
Chapter5.pdf 0b8ec6ecc62cd834a58e5032c6b9dba7e02e6ad694f0bb9e8b14adab0fd05996
Chapter6.pdf e1f4aa25813d98caa45472a2a6ce7360cec670b38720abd384c929137e203c43
Chapter7.pdf 82accad40c3dc1edad3bb43f9d90ece6e841ecc9b73daef1f1c7333d98fd4a97
Chapter8.pdf 75f36213e4c09bf149335f6150a580c66d2601da908003dc9e4c4febbb46104c
Chapter9.pdf 3038c746d8c145c03f49ff5eacc529f48ddad930e2399106067db5ebe5606e23
Chapter3_Supplement.pdf 854ad4eecdb677785cdc11b48da428db89563dcaf36b91355dd667ef476c70a4
HW1.pdf cc2a847ef901b628b32b7572707eb01447aefd0b19617f48ca463c0671d6fc01
HW2.pdf b91be11684970f900091c59e67dcf9812e558e4d6d264a68def758f6429c6a8c
Final Project.pdf 694dd01df008aff76eb96abe7173027312b4824d8b8bd0c64fec4c49654b03ca
Syllabus.pdf 3732fdc78bd5699c0c8107dd9a2e838b74567c47b5e986e0fe410cd9ff3f63b7
tutorial.pdf b02ca58cbd075a499ce6fc0b0dc42eaabe4a2d1d338d36f2c2eebc24227a3514
MH-algorithm.pdf 1d526037536457f88703321974f65246156fbf87f02b9c4f22e4ec3a9e3c3d7c
```

## 4. Old scripts and supplementary manuals

Read all five relevant R scripts and the BUGS linear-model text in full:

| File | Drive ID | Main finding / treatment |
|---|---|---|
| glm_count.R | 1kqCVbUZwMpsP4rEjmPhqOz93TCScMTSp | Minimal Poisson simulation; no reproducibility seed/diagnostic narrative. Replace organization, not merely parameters. |
| glm_ordinal.R | 1PTzpEiZcV8RwnuxdNagntceaVgFrqm7l | Threshold and slope-sign reconciliation needed for canonical clm interpretation. |
| linear.R | 11K_CsBTb-tdJgj2sROPt8Z4EDZzZpsW8 | R2WinBUGS/local Windows paths and SD/precision conventions; do not reuse as modern setup authority. |
| multilevel.R | 1-odmcar6Gxgoy1v2a1S8EHf2CVTFsW1U | Useful lme4 random-coefficient structure; old dependency/setup and sample-size choices are not current Tutorial constraints. |
| mixture.R | 1I0FVqAkkO2g-nDCnSErngnCxZ5YlG7WM | Mixture simulation/MH logic; label matching and reproducibility need explicit handling. |
| model_linear.txt | 1hb0SqXdp_XKFMiMtJKNTo5LJagLSbg5i | BUGS normal precision/Wishart conventions; historical model evidence. |

Additional PDFs were downloaded and inspected for the relevant model/implementation sections, not treated as current package authority:

- `Bayesian Analysis for SEMs using WinBUGS.pdf` (45 pages), ID `1uxdtDmRJqPwT2XWiL4UqC78kBSM77i86`: SEM declaration, priors/precision, GUI workflow, Bayesian computation and R2WinBUGS/path-sampling context. No full-text republication.
- `Winbugs_AppendixB.pdf` (28 pages), ID `1VWScIj__Uh77KFed0K3ndBcAl8xiGvhb`: background/model/distribution/GUI sections; remaining installer details have no modern instructional authority.
- `glmm_operate.pdf` (17 pages), ID `11sJT6lahpiEzcMdk9bx1ZFgteoLvSf_-`; `glmm_Rdocument.pdf` (24 pages), ID `1dEWKwkBKlw6WUPFCm_VdS67pDSmnwzIq`; `glmm.pdf` (24 pages), ID `1k0OEqU1O8yyrKJ6rWCJnQLd_FdUBuPUb`: scoped reading of the Monte Carlo-likelihood `glmm` route and relevant controls/uncertainty. Do not confuse it with lme4's likelihood approximations.
- `ordinal_R.pdf` (61 pages), ID `1TidVKHMpWFnZf2Dl3yDxXHZ2gz3mRtEp`: relevant clm/clmm model/cutpoint/mixed-model documentation, not every unrelated help-index entry. Current official ordinal documentation replaces this old manual for implementation.

## 5. Historical conflicts resolved

- Old Syllabus weights 10/20/20/50 are superseded by the user's confirmed 20/20/20/40.
- Old HW1's 2025 deadline and B=10 repetitions are not reused; the new assignment has a date placeholder, case diagnosis and B=500 with MCSE.
- Old HW2's missingness indicator uses 1=missing; the canonical knowledge convention uses 1=observed and explicitly converts signs.
- The old syllabus outline does not by itself establish exclusion of Chapter9: Chapter9.pdf exists, was read, and the user explicitly requires Chapters1–9. Keep all nine in the review.
- The original Project's real-data, research-question-to-conclusion narrative and Chapter4–9 emphasis are retained as a working design; its old date/page annotations/weight are not copied mechanically.
- The SeminarArc roadmap's oral design is retained; 25/15 scoring and recording governance require formal course approval as listed in the assessment policy.

## 6. New fixed fixtures and licensing

The four files below were created in this planning session from newly authored synthetic mechanisms. They contain no actual student, patient or equipment records and no reconstructed original course table. They are distributed under CC0 as teaching fixtures. Freeze the bytes below; the attached instructor handoff supplies these exact bytes for Codex to materialize publicly into the course data directory.

| File | Rows | SHA-256 |
|---|---:|---|
| tutorial_devices.csv | 240 | ac5bed1c9e6abb1641986f9187e819f91589edb2cf85289b26b3f22b72ca74ad |
| tutorial_alarms.csv | 960 | b7582a5ba8f4ef0a4569a26a364dc6e4034341fbc9ff2dddb6020747a6c8e4f2 |
| hw1_participants.csv | 600 | 239773577bc8e4a621f0355f289af0b81f33434b236f492a4392a898d2d87600 |
| hw1_weekly.csv | 2400 | ec41524844d348f09cd7566d0e710c3cc1a47b83c262b759e52f91b0ace8a6cc |

The instructor-only data-generating details, worked answers and pilot reference outputs are in the private handoff, not the public student starter. Publicly providing the synthetic case data is allowed; publicly revealing a confidential answer key is not implied by that permission.

## 7. Research and implementation evidence boundaries

The software policy's W01–W29 register records primary software/method sources. The assessment policy's A01–A05 register records current official CUHK sources and explicitly reports the authentication barrier to the full restricted AI guide. Do not replace that barrier with an invented quotation or claim to have read the restricted guide.

Actual completed execution in this session: frozen-case generation, ordinary Python ML models, high-order scalar random-intercept ML cross-check, HW simulation n100/n400 with 500 attempts each, Tutorial calibration with 500 attempts per variance scenario, and 200-panel plug-in checks. Numerical pilot outputs are private. R/PyMC/ArviZ installation, clean-environment validation and final PDF/slide rendering remain mandatory Codex execution gates; they are not evidence already obtained by the planner.
