# STAT5060 Codex Execution Goal V1

- Status: FROZEN_EXECUTION_CONTRACT; READY_FOR_CODEX=YES when accompanied by the private handoff attachment.
- Date: 2026-09-28.
- Source authority: current user authorization, roadmap commit `9d1923d2002c529352ad6464599e7da08eb6787c`, and the complete frozen specifications indexed below.
- Relation: this file owns execution scope, deliverable paths and acceptance gates. It does not supersede statistical, teaching, assessment or rubric meaning. `STAT5060_CRITIC_RELEASE_MANIFEST_V1.md` records the completed planner reviews and remaining administrative approvals.

## 1. Goal and authorization envelope

Materialize, execute, validate and render the already-designed STAT5060 course review, Tutorial 1 and HW1 package. Do not redesign the course, substitute easier datasets, choose a new assessment policy or convert this into a plugin project.

Canonical repository: `YuukiAS/AI_Skills_Collection`.
Task key: `stat5060--materialize-frozen-v1`.
Authorized task branch: `reviewed/stat5060--materialize-frozen-v1`.
Authorized worktree: `.worktrees/stat5060--materialize-frozen-v1` under the existing long-lived canonical checkout. Resolve and record its absolute path before creation. Reuse it only if it belongs to this exact task and is safe; do not overwrite another worktree or uncommitted user work. The final user kickoff should explicitly authorize this exact branch/worktree and ordinary non-force push. Do not infer authorization for arbitrary branches, a force push, destructive cleanup, global installation changes or an automatic merge into main.

Allowed changes: newly derived course sources, task-local environments, scripts, tests, original synthetic fixtures, rendered artifacts and evidence described here. Public source root is `courses/STAT5060/2026/`. Task execution evidence is `results/stat5060--materialize-frozen-v1/`, with confidential evidence stored privately as below. Frozen specifications are read-only inputs; ordinary formatting/API fixes go into the implementation, not silent edits of the frozen teaching contract.

Read `AGENTS.md`, root `TODO.md` and relevant existing planner/executor/critic/artifact-review/privacy rules before implementation. Read the maintenance-board policy to understand the boundary, but do not create plugin maintenance work merely because the course lives in this repository. No repository/plugin version bump. No Skill/plugin implementation, generated marketplace changes, new watcher/control plane, paid model API call, credential copying, SeminarArc implementation or upload of original course PDFs is authorized by this Goal.

Use `git fetch origin main`, verify the frozen release commit supplied in the kickoff, and create the task from a compatible clean main containing that release. Keep the exact frozen input commit in evidence. Preserve unrelated new main changes. If an existing formal Reviewed Handoff transport is available and applicable, use it according to governance; do not fabricate its state or replace a missing independent review with an executor summary. Do not invent a new scheduled or paid-review dependency for this bounded course build.

## 2. Read all canonical inputs, not just this Goal

All paths below are exact repository paths:

1. `docs/design/STAT5060_COURSE_KNOWLEDGE_ASSESSMENT_PILOT_ROADMAP_2026-09-28.md`
2. `docs/design/stat5060/STAT5060_SOURCE_INVENTORY_V1.md`
3. `docs/design/stat5060/STAT5060_CANONICAL_KNOWLEDGE_V1.md`
4. `docs/design/stat5060/STAT5060_MATHEMATICAL_DETAILS_V1.md`
5. `docs/design/stat5060/STAT5060_SOFTWARE_WORKFLOW_POLICY_V1.md`
6. `docs/design/stat5060/STAT5060_ASSESSMENT_AI_POLICY_V1.md`
7. `docs/design/stat5060/STAT5060_TUTORIAL_01_FROZEN_SPEC_V1.md`
8. `docs/design/stat5060/STAT5060_TUTORIAL_HW1_ALIGNMENT_V1.md`
9. `docs/design/stat5060/STAT5060_HW1_STUDENT_SPEC_V1.md`
10. `docs/design/stat5060/STAT5060_HW1_SOLUTION_SPEC_V1.md`
11. `docs/design/stat5060/STAT5060_HW1_RUBRIC_V1.md`
12. `docs/design/stat5060/STAT5060_CRITIC_RELEASE_MANIFEST_V1.md`
13. `docs/design/stat5060/STAT5060_PLANNER_VALIDATION_V1.json`
14. `docs/design/stat5060/STAT5060_CODEX_EXECUTION_GOAL_V1.md`

Authenticated instructor payload: `docs/design/stat5060/STAT5060_HW1_SOLUTION_V1.aesgcm`.

Retain the existing oral authority `YuukiAS/SeminarArc/docs/plans/stat5060-oral-defense-pc-roadmap.md`, whose reviewed file blob is `a380e0fdfc84a1acc3c60306629f507ab877bbcc`. The assessment spec already freezes the course-facing use of that design; do not implement/redesign SeminarArc.

Read the complete private solution before producing instructor materials. It is not a request to derive a new answer key. The statistical notation/likelihood/identification corrections in the mathematical appendix are mandatory. The Tutorial specification is the scheduling authority: its 20-minute RI block and two-page bridge provide the prerequisite explanation; no separately produced video is required by this sprint.

## 3. Private input and durable storage

The user supplies `STAT5060_PRIVATE_HANDOFF_V1.zip` with the kickoff.
SHA-256: `dd4823f973f386be378aba2e5d3db71dcf566e6a7e26fba0bbf3d0dc623b6ac0`.
It contains the complete plaintext answer, recovery key, original fixed fixtures, pilot results and instructor scripts. It contains no original lecture PDFs.

Before extraction, create and verify an ignored durable directory in the long-lived checkout:
`private/exports/stat5060--materialize-frozen-v1/`.
Use `git check-ignore`; if necessary add a checkout-local exclude through `git rev-parse --git-path info/exclude`, never a global configuration change. Task worktree caches are not the only durable copy. Locate the supplied attachment through the current attachment/input surface or the mounted file, not by inventing an old sandbox path on the user's machine. Verify the ZIP hash before extraction and prevent path traversal.

Read the recovery key from its private file without printing it. Authenticate/decrypt the repository ciphertext using the algorithm, nonce and AAD in the solution wrapper, decompress and verify plaintext SHA-256 `1a9c870646fe52f17b2daca7de3303a8ac480498a491ac2b8969b57c01ed8fd1`. Verify that the supplied plaintext has the same hash. A failed check is an input-integrity blocker, not permission to reconstruct answers from guesses.

Keep keys, full solution source, case-generating mechanisms, HW1 expected outputs, worked reference code and instructor PDFs out of Git, public logs and student bundles. The four synthetic case CSVs alone are expressly approved for public course materialization under CC0. Copy their exact bytes and verify the four hashes in the source inventory; do not regenerate case data. Existing pilot scripts contain planning-sandbox paths: adapt paths only, never distribute those absolute paths or instructor generating mechanisms as student code.

## 4. Frozen deliverable tree

### Public editable sources and student-accessible code

Under `courses/STAT5060/2026/` create:

- `README.md`, `_quarto.yml`, `build.py`: audience/entrypoints, input/output boundaries and one-command build orchestration. A small script is sufficient; do not build a new framework.
- `data/tutorial_devices.csv`, `data/tutorial_alarms.csv`, `data/hw1_participants.csv`, `data/hw1_weekly.csv`, `data/README.md`, `data/manifest.json`, `data/LICENSE-CC0.txt`.
- `tutorial01/slides.qmd`, `tutorial01/notes.qmd`, `tutorial01/random_intercept_bridge.qmd`.
- `tutorial01/R/01_count.R`, `02_nominal.R`, `03_repeated_binary.R`, `04_simulation.R`, `helpers.R`.
- `tutorial01/python/01_count_nominal.py`, `02_simulation.py`, `03_bayesian_demo.py`.
- `hw1/student.qmd`, `hw1/rubric.qmd`, `hw1/starter/README.md`, transparent starter files for R and Python, the supplied R mixed-model runner and tested probability/panel helpers. The starter may contain the instructed model-fitting scaffolding/helper, but not filled answer tables, interpretation paragraphs or the completed simulation summaries.
- `environments/R/renv.lock` plus restoration instructions; `environments/python/requirements-core.lock`, `requirements-bayes.lock` with reproducible resolution/hashes where supported. Use two isolated Python environments if dependency compatibility requires it. Do not require every audited package for HW1.
- `tests/` covering the gates below; public tests must not disclose private HW1 answer tables through fixtures, expected literals or logs.

Public source may include complete worked Tutorial code and Tutorial outputs; it must not include the private HW1 solution. Keep unapproved course policy/deadline fields clearly marked in draft student materials. Do not upload to the LMS or announce release without instructor authorization.

### Generated student artifacts

Build under `courses/STAT5060/2026/dist/`:
`STAT5060_Tutorial01_Slides.pdf`, `STAT5060_Tutorial01_Notes.pdf`, `STAT5060_Random_Intercept_Bridge.pdf`, `STAT5060_HW1_Student.pdf`, `STAT5060_HW1_Rubric.pdf`, and a student-code/data ZIP. Include editable sources separately. Build an HTML teaching fallback with checked cached outputs. Follow repository policy on storing generated binary artifacts; when binaries are not tracked, keep durable copies and return exact local/downloadable locations and hashes rather than claim they were pushed.

### Instructor-only outputs

In the durable private directory create:

- `course_review/STAT5060_Course_Review.qmd` and `.pdf`: complete Chinese polished review of Chapters1–9 plus the mathematical/notation/corrections appendices, 28–36 A4 pages targeted. Faithful translation/reorganization into the frozen nine section headings is permitted; adding new claims or omitting caveats is not. This is explanatory prose, not slide bullets.
- `hw1/STAT5060_HW1_Solution.qmd` and `.pdf`: English worked instructor solution, with an optional concise Chinese TA marking commentary; all questions, reasoning, actual results, acceptable alternatives and tolerances included.
- `hw1/reference/R/`, `hw1/reference/python/`, `hw1/outputs/`, common simulation-response matrices and complete attempt/warning records.
- `tutorial01/outputs/`: cached fits, actual MCMC draws/diagnostics and plot/table inputs. Tutorial non-confidential outputs may be copied to the teaching bundle; posterior draws need not inflate the student package.
- `review/`: private full-resolution page/slide renders, annotated critic evidence and private numeric consistency checks.
- `release/`: instructor ZIP, artifact hash manifest and a handoff README. Verify no key or answer accidentally entered the student ZIP.

The original course PDFs, screenshots and textbook prose are not copied into these derived deliverables or public Git.

## 5. Implement and run the frozen analysis

R is the teaching/reference route. Execute the actual Poisson/NB2, nominal reference-change and scalar-RI `glmer(nAGQ=9)` analyses. Run the Python ordinary-model equivalents on the same fixed rows/designs. Preserve factor/event/reference conventions, offsets, unpenalized likelihood, NB2 shape conversion and conditional versus marginalized targets. A Bayesian/VB mixed-model fit is not an equivalent fallback for the required ML fit.

Run the complete Tutorial simulation and the HW1 simulation: 500 attempted replications per frozen scenario, all specified seeds and same-response pairing of methods. Do not reduce B to meet a runtime budget. Preserve every warning, same-data recovery and final validity record; never replace a failed response vector with new data. Compute bias, RMSE, sample empirical SE, RMS reported SE, coverage, MCSE and correct denominators exactly as specified. If reference fits have more than 2% final invalid attempts, investigate numerical causes while preserving the experiment and report honestly; do not tune the DGP to eliminate failures.

Run both sets of 200-panel plug-in checks. Draw all 200 naive panels, then all 200 RI panels from the specified seeded stream; each RI panel uses one random intercept per subject shared across its visits. The seed need not yield identical R/Python realizations. Label envelopes as plug-in model checks, not parameter-uncertainty intervals. Validate the integration helper independently, including zero SD, eta=0 symmetry and actual profile checks.

The Bayesian instructor demo is a mandatory execution deliverable, though optional for students: run the exact priors/NB2 model, four chains, explicit sampler, warmup/draws and seeds in the software policy. Current PyMC/ArviZ APIs must match the versions actually installed; preserve the model when adapting API syntax. Check unrounded R-hat, bulk/tail ESS, MCSE and divergence count, then prior/posterior predictive outputs. Only the frozen bounded numerical recovery is allowed; do not drop problematic draws/chains or change priors for a prettier demonstration.

Use the planner's actual Python results as corroboration, not fabricated R output. Record discrepancies with their model/numerical explanation. Do not force legitimate simulations to equal one pilot's realized coverage or claim universal NB RMSE superiority. Exact numeric tolerances are in the software policy and rubric.

## 6. Clean environment and classroom execution gates

Actually restore/install released dependencies into clean task-local environments and run from the documented entrypoint with no undeclared interactive/global state. Do not pin R-devel merely because official reference help was served under R-devel. Record OS, hardware, R/Python/package versions, commands, runtime, peak resource observations where available and lockfile hashes.

Required runtime targets are in the software policy: ordinary fits around 5 seconds; scalar GLMM around 30 seconds; core HW pipeline target 10 minutes, validation ceiling 15 minutes excluding installation/rendering; offline Bayesian demonstration target 15 minutes and 8 GB RAM. Record measured results and optimize implementation within the frozen model, not the pedagogy. Classroom mode uses cached simulation/MCMC and any slow fit. Verify fallback without network/package installation during the session. An installation failure is not permission to substitute a different estimator.

Run student starter/runner smoke tests and a complete instructor reference run. Common stored response matrices provide strict R/Python method equivalence; identical integers passed to different RNGs are not a bitwise test. Full rebuild from raw fixed CSVs must work. Render-from-cache may be separate for classroom use, but cannot substitute for the required actual analysis run.

## 7. Content, render and privacy acceptance gates

- Source/notation: all nine chapters and the mathematical appendix present; source content, modernization, pedagogical reorganization and corrections distinguishable; references/page locators retained; no copied original slides.
- Alignment: every HW1 requested output and rubric item maps to the frozen Tutorial or explicit supplied helper; no added ordinal/Bayesian programming burden.
- Arithmetic: exactly 90 instructional minutes, 24 content slides; points 30/18/25/22/5=100; course weights 20/20/20/40. The working Project25/15 split remains labeled pending approval.
- AI policy: include the entire canonical English student-facing block, not the source-file build directive. Keep official declaration procedures distinct. No invented deadline, retention period or approval.
- Statistics: NB2 conversion, exposure offset, multinomial probability sums/reference invariance, GLMM grouping/likelihood/integration, uncertainty labels, simulation definitions/failure accounting, Bayesian diagnostics and prior correspondence tested.
- Rendering: build every required PDF; inspect every PDF page and all 24 slides visually, not only successful exit codes. Check clipping/overlap, missing glyphs, broken math, cutpoints/signs, legends, units, category colors/labels and table readability. Use the installed artifact/PDF/slides skills for building/QA. No font-file redistribution. Record page counts, render hashes and specific issue/fix evidence.
- Privacy: inspect `git diff --cached`, public logs, all output manifests and student ZIP contents for private answer text, reference tables, generating mechanisms, keys and original course PDFs. Encryption wrapper/ciphertext and public synthetic CSVs are allowed; instructor artifacts stay private and durable.

## 8. Critics, bounded repairs and completion

Produce four separately structured post-execution reviews: A statistical correctness, B pedagogy/alignment, C assessment/AI validity, D reproducibility/render/privacy. Use actual outputs, code and rendered artifacts, not only this plan or an executor summary. Distinguish local deterministic tests, host role-based review and genuinely independent reviewer evidence. Never claim four independent external model runs when only one host reviewed four perspectives. Consume existing authorized independent review capability when available without adding paid calls or new services. An unavailable required independent-review transport must be reported, not faked as PASS.

Local implementation errors, plot labels, layout, dependency resolution and compatible API repairs can be fixed and retested. Changes to questions, marks, cases, model families, priors, target parameters, AI policy, teaching scope or simulation design require returning the exact conflict for planner resolution; do not silently rewrite the frozen specs. Ordinary execution problems are not grounds to abandon the rest of the build.

Administrative approval is separate from artifact quality. Finish all executable/renderable work with clear draft fields even if the instructor has not supplied the due date, approved25/15 or adopted recording/AI rules. Report `READY_FOR_INSTRUCTOR_RELEASE` only after artifact gates pass; report student publication as pending those explicit approvals. No LMS publishing is requested here.

Commit only safe authorized source/evidence changes, push the exact task branch normally, verify the remote tip equals the intended local HEAD, and preserve durable private outputs before cleaning any temporary worktree. Do not auto-merge into main. Return the final SHA, branch, public source paths, private durable artifact paths, artifact hashes, actual R/Python/Bayesian and clean-run results, render/page checks, four critic verdicts/evidence locators and the remaining instructor approvals. Do not call the Goal achieved while a required build/run/render/review gate is unperformed.

## 9. Execution order

First implementation pass: verify frozen inputs/private handoff, establish clean environments and fixtures, implement/run the core R/Python analyses and compose the internal review/Tutorial/HW sources. Second pass: finish full simulations/Bayesian run, render all artifacts, perform the four reviews, repair within scope, rerun clean checks and push verified evidence. This ordering is the two-day sprint's execution structure, not a reason to stop at an intermediate plan or a promise of asynchronous work.

Reusable Statistical Modeling/Scientific Visualization knowledge extraction is explicitly deferred until the real Tutorial/HW release has been validated. Course deadlines, points, answer keys and course-specific wording are never promoted into generic plugins by this Goal.
