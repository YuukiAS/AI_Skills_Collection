# STAT5060 Critic and Release Manifest V1

- Status: FROZEN_DESIGN_RELEASE; READY_FOR_CODEX=YES with the private handoff attachment.
- Date: 2026-09-28.
- Source authority: the current user request, original source reading, current primary-document research, completed Python design pilots and the frozen specifications below.
- Relation: this is the release index, authority-resolution record and four-perspective planner critic report. The execution Goal owns subsequent build/run/render gates; no future execution PASS is implied by this design release.

## 1. Release meaning and unique authorities

`READY_FOR_CODEX=YES` means teaching content, statistical models, case fixtures, questions, worked reasoning, marks, software roles and execution acceptance criteria are sufficiently frozen for implementation. It does not mean the materials have already been officially issued to students, every language/environment has been run, or the final PDFs exist.

`READY_FOR_STUDENT_PUBLICATION=NO_UNTIL_BUILD_AND_ADMIN_GATES` is deliberate. Formal course-policy approvals and the due date remain outside the planner's authority. They do not require Codex to decide the pedagogy or prevent building the draft release package.

All filenames below are under `docs/design/stat5060/`:

| File | Unique authority |
|---|---|
| STAT5060_SOURCE_INVENTORY_V1.md | Original source locators, reading scope, historical conflicts, hashes and new-data provenance. |
| STAT5060_CANONICAL_KNOWLEDGE_V1.md | Chapter1–9 plus supplement model cards, unified notation, source/modernization boundaries and review-note content. |
| STAT5060_MATHEMATICAL_DETAILS_V1.md | Mandatory exact mathematical definitions/qualifications supporting the compressed model cards. |
| STAT5060_SOFTWARE_WORKFLOW_POLICY_V1.md | Current primary-source software audit, roles, model equivalence, Bayesian demo and environment/runtime rules. |
| STAT5060_ASSESSMENT_AI_POLICY_V1.md | Homework/Project boundary, working Project split, institutional versus selectable policy, exact AI text and approval register. |
| STAT5060_TUTORIAL_01_FROZEN_SPEC_V1.md | Complete 90-minute/24-slide teaching script, cases, equations, outputs, code intent and bridge materials. |
| STAT5060_TUTORIAL_HW1_ALIGNMENT_V1.md | Every assessed skill's preparation or intentional-transfer justification; explicit exclusions. |
| STAT5060_HW1_STUDENT_SPEC_V1.md | Complete publishable question content and required outputs, with explicit administrative fields. |
| STAT5060_HW1_SOLUTION_SPEC_V1.md | Public authenticated-payload locator and instructor-only build contract. |
| STAT5060_HW1_SOLUTION_V1.aesgcm | Complete encrypted instructor solution; decryption yields the full frozen reasoning/numeric/alternative/tolerance document. |
| STAT5060_HW1_RUBRIC_V1.md | Exact 100-point ledger, stable partial credit, error handling and marking safeguards. |
| STAT5060_CODEX_EXECUTION_GOAL_V1.md | Exact implementation/output paths, authorized boundaries, clean execution/render/privacy/critic/commit requirements. |
| STAT5060_PLANNER_VALIDATION_V1.json | Machine-readable summary of completed local checks and explicitly unperformed execution gates. |
| STAT5060_CRITIC_RELEASE_MANIFEST_V1.md | This release index, critic findings and remaining approvals. |

The older top-level roadmap remains intact at `docs/design/STAT5060_COURSE_KNOWLEDGE_ASSESSMENT_PILOT_ROADMAP_2026-09-28.md`, initial commit `9d1923d2002c529352ad6464599e7da08eb6787c`. New detailed specifications resolve its open design questions; they do not mutate unrelated Skill/plugin implementations.

### Cross-file clarification frozen during the final audit

The Tutorial specification owns the Chapter3 preparation gate. Its actual 20-minute RI block plus two-page bridge/worksheet are the explanatory preparation; no separately produced video is a mandatory sprint deliverable. The earlier knowledge-file mention of a 'recorded explanation' is satisfied by the delivered explanation/bridge and does not create an extra production prerequisite. The mathematical appendix likewise makes the Chapter8 additive counterfactual contrast explicit; do not reinterpret that identity as an unrestricted additive hazard-ratio decomposition.

The student-spec AI inclusion directive is a source-build instruction, not publishable student prose. The complete canonical policy block must appear in the actual PDF after instructor adoption, with draft approval status otherwise evident. This is mechanical inclusion, not a missing policy decision.

## 2. Critic method and independence boundary

Four distinct adversarial roles were applied to the complete design, each with its own failure criteria and recheck. These are **four role-separated reviews within this planning session**, not four independently instantiated external models or paid reviewer calls. Mathematical calculations, independent numerical formulations and actual test executions provide additional evidence where stated. The executor must still obtain artifact-aware post-build review and label the review provenance honestly.

An initial REVISE below names a substantive risk addressed before this release; the final PASS is **PASS_DESIGN**, not a claim that a clean R/PyMC run or rendered artifact already passed.

## 3. Critic A — Statistical correctness

**Initial verdict: REVISE.** Blockers examined: NB shape/dispersion inversion across packages; an ordinary Python Bayesian mixed-model routine being mislabeled as the same estimator as glmer; b=0 prediction being called population averaging; source ordinal sign/cutpoint conflicts; latent-utility covariance scaling; mixture conjugacy errors; vague survival/mediation contrast scales; simulation equating low bias with valid uncertainty.

**Repairs frozen:** one NB2 kappa convention and explicit MASS/PyMC/statsmodels mapping; scalar-RI ML through the R runner; integrated new-subject probabilities with a supplied tested helper; explicit source correction/notation tables; positive utility rescaling with covariance multiplied by c^2; exact Gaussian/IG/IW and mixture formulas in the mathematical appendix; additive counterfactual definitions and rare-outcome path-product qualifications; time-varying integrated hazard; complete bias/RMSE/SE/coverage/MCSE definitions and failure denominators.

**Recheck evidence:** actual nominal re-reference/refit with aligned probability columns; independently evaluated new-subject probability integration, including zero SD and symmetry; high-order scalar-RI likelihood pilot with convergence/Hessian/quadrature checks; two 500-replication HW scenarios preserving same-data method comparisons. Review retained the fact that the NB pilot did not have smaller realized RMSE in every scenario and that a correct mean can coexist with Poisson undercoverage. No universal Jensen argument or same-target interpretation of naive versus conditional logit coefficients remains.

**Final verdict: PASS_DESIGN. Remaining content blockers: none.** Actual canonical R fits and current Bayesian diagnostics are execution gates, not completed planner evidence.

## 4. Critic B — Pedagogy and alignment

**Initial verdict: REVISE.** Risks: four unrelated historical datasets in 90 minutes; a catalogue of Bayesian/C++ packages; a repeated-ordinal or unsupported Python mixed-model prerequisite; a simulation merely repeating an old loop; a tutorial whose quoted durations omit transitions and end-of-class instructions.

**Repairs frozen:** one connected equipment narrative with three different response questions; R as the main language, Python as a limited transferable route; 28 minutes counts, 15 nominal, 20 repeated binary, 14 calibration, 10 Bayesian workflow, 3 HW/reproducibility/policy. Exactly 24 slides cover 0–90 with transitions and student checks included. Complete MCMC and simulation are cached. Ordinal mixed coding and Bayesian HW1 coding are excluded. A two-page RI bridge, integration helper, panel helper, annotated simulation starter and Python-to-R runner remove unassessed engineering burdens.

HW1 transfers to a different learning-support context: exposure sensitivity, a new reference category, nonlinear marginalization and sample-size/estimator calibration. Tutorial simulation instead contrasts correct versus wrong variance for Poisson at fixed n; HW simulation asks whether larger n or estimated NB repairs the uncertainty. The distinction is intentional transfer, not a hidden new model. The alignment matrix covers every marked core skill. Eight main report pages and supplied infrastructure yield a planning workload of 11–15 hours rather than four full open-ended projects.

**Recheck evidence:** all 24 time intervals sum to exactly 90 without gaps/overlap; all question subparts sum to 30/18/25/22 plus5 process points; explicit mapping from every question to teaching/helper evidence; no additional video or installation workshop added by implication. A human classroom delivery has not yet occurred, so timing is a realistic design allocation, not an observed teaching trial.

**Final verdict: PASS_DESIGN. Remaining content blockers: none.** Codex must check the actual slide/handout material contains the allocated content without shrinking it into unreadable text.

## 5. Critic C — AI resilience and assessment validity

**Initial verdict: REVISE.** A strong AI can write the entire homework, including plausible interpretation. Neither changing parameters nor adding perturbation prose proves student ownership. A detector or a full prompt history would not repair that construct-validity problem. An answer key in a public repository would weaken assessment and violate its intended instructor-only boundary.

**Repairs frozen:** homework explicitly assesses guided statistical workflow, transfer and evidence, not purported AI detection. Numeric output alone leaves interpretation/model-choice/diagnostic marks unavailable. The written Project assesses autonomous integration with real data and a substantive justified Chapter4–9 method; its published oral defense is the main supervised verification of ownership and understanding. Preserve the existing three-question SeminarArc structure, immediate follow-ups and human scoring. No complex-model bonus, live AI, automatic grading or hidden language-fluency criterion.

AI use is allowed with concise task-level disclosure as a frozen instructor-adoption recommendation. Students retain responsibility, references/claims must be checked, no paid tool is required, no full prompt log is required and detector scores are not sole evidence of misconduct. Official institutional declarations remain separate. The restricted full CUHK AI guide was inaccessible and is not falsely quoted; public current official guidance supports only the claims actually made. The complete instructor answer is encrypted, not published in plaintext.

**Recheck:** the point ledger rewards exact evidence and interpretation without pretending to guarantee unassisted work; disclosure omissions have an explicit limited process treatment; ownership verification is located in the Project, not improvised homework interrogations. Project25/15 and policy adoption remain clearly pending rather than being represented as instructor-approved.

**Final verdict: PASS_DESIGN. Remaining content blockers: none.** Residual limitation acknowledged: homework alone cannot establish independent unaided understanding under permitted strong AI assistance. That is the reason for the assessment boundary, not an undisclosed failure of the design.

## 6. Critic D — Reproducibility, execution and disclosure safety

**Initial verdict: REVISE.** Risks: public-repo instructor answers; fragile external data links; recreating 'the same' case with a different RNG; stale PyMC/ArviZ APIs; treating a Python posterior approximation as R ML equivalence; Poisson-boundary NB fits dominating a calibration exercise; hiding failed replications; live installation or MCMC; private artifacts stranded in a disposable worktree.

**Repairs frozen:** authenticated AES-GCM answer payload and private handoff with key/complete answer; four original CC0 CSVs frozen by SHA; no external case download required. Current software roles/API boundaries are explicit, and actual released dependency versions are locked after resolution. A small R/core-Python environment is separate from the instructor-only Bayesian environment. HW simulation uses NB truth at two sample sizes; Tutorial's Poisson-truth contrast fits Poisson only, avoiding an unnecessary NB boundary-estimation prerequisite. Same-data recovery and complete attempt records are required. Full simulations/MCMC are precomputed for class; actual runs still mandatory before release. Durable private storage and student/public artifact separation are explicit.

**Recheck evidence actually obtained:** fixed-file hashes/row/domain checks; both ordinary model and scalar-RI design pilots; 500-attempt simulations per scenario; 200-panel checks; reference-change and independent-integration tests; authenticated encryption/decryption round-trip; ciphertext tamper rejection; ZIP integrity/path/content checks; local ciphertext Git blob SHA matching the SHA returned by the connected GitHub blob upload. The handoff contains no original PDF. See the validation JSON for actual completed versus unperformed gates.

**Final verdict: PASS_DESIGN. Remaining content blockers: none.** Clean R/lme4 execution, the locked current PyMC/ArviZ run, hardware-specific runtime ceilings and all final PDF/slide renders remain explicit Codex acceptance gates. No installation/runtime/render certification is claimed in this design release.

## 7. Completed evidence versus next execution

Completed in this planner session: source reading and current official research; canonical knowledge/software/assessment content; complete Tutorial/HW1/solution/rubric; synthetic fixture generation and numeric design pilots; the four reviews and corrections above; local numeric/packaging checks. The review content records provenance and uncertainties rather than calling every test 'independent'.

Required next: actual R and Python reference scripts, current Bayesian run, complete clean-environment restoration/execution, all plots/tables/PDFs, every-page/slide render inspection, artifact-aware four-perspective review, privacy leak checks, normal commit/push and remote SHA verification. This split follows the user's ChatGPT-versus-Codex boundary.

Private handoff: `STAT5060_PRIVATE_HANDOFF_V1.zip`, SHA-256 `dd4823f973f386be378aba2e5d3db71dcf566e6a7e26fba0bbf3d0dc623b6ac0`; complete plaintext solution SHA-256 `1a9c870646fe52f17b2daca7de3303a8ac480498a491ac2b8969b57c01ed8fd1`. It must accompany the final Goal. Keys are not printed in the Goal or committed. Public wrapper/ciphertext are durable repo authority; the attachment supplies authorized private recovery and execution inputs.

## 8. Remaining instructor approvals and administrative fields

- Formal Project25 written/15 oral split within the confirmed40% total and publication of the updated Project course-depth brief.
- Formal adoption/publication of the allowed-with-disclosure homework/written-Project AI rule and no-AI oral rule.
- Recording notice/access/storage/retention/deletion and any transcription/export permissions.
- HW1 due date/time/timezone and official submission/declaration details.

These are `INSTRUCTOR_APPROVAL_REQUIRED` or explicit administrative placeholders. Ordinary model, teaching, software and marking choices are not left undecided. The known course weights remain20/20/20/40.

## 9. Release boundaries

This commit adds derived planning/content/evidence files only. Repository bump: NONE. All plugins: NO_BUMP. Original Google Drive PDFs and legacy installers remain outside Git. No raw restricted teaching content, original slides or patient records are republished.

Future extraction may begin only after Tutorial+HW1 are actually executed, reviewed and release-validated: reusable statistical knowledge to Statistical Modeling; reusable diagnostic-visualization guidance to Scientific Visualization. No extraction implementation is part of this Goal. Course points, deadlines, answer keys, dataset-specific expected answers and course-specific wording never become generic plugin knowledge.
