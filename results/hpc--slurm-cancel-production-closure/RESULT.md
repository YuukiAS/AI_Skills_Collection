# Slurm protected-cancel production closure candidate

Task: `hpc--slurm-cancel-production-closure`

Result: `READY_FOR_INDEPENDENT_REVIEW`

Phase: 3 candidate handoff; production deployment is forbidden until an independent Reviewer returns PASS for the exact three product commits below.

## Exact identities

- Approved package base: `798415474f909fedd385b86086e576e2e9d40128`
- AI Skills product candidate: `b4815a35f708078184bff27b34f185fea6938cc3`
- DII consumer candidate: `e04f6a8da729c05a9e286b38c2c14cfd9ab13d31`
- CARE consumer candidate: `74d2948def67502070c06336866638f0869d9481`
- Branch in all three repositories: `work/hpc--slurm-cancel-production-closure`

Repository and standalone versions remain unchanged in this pre-deployment candidate:

- Repository: `5.4.4`
- `slurm-workflows`: `0.4`
- Central Marketplace Plugins: `NO_BUMP`
- Bridge Kit: `NO_CHANGE`

## Product behavior

The central `slurm_routing.py safe-cancel` entry resolves the live cluster, effective-UID scheduler owner, exact JobId records, current state, partition and accelerator facts, and the private site policy. It accepts an exact current-run ownership set from the consumer.

- `ALLOW_OWNED_UNPROTECTED`: evaluation remains non-mutating unless `--execute` is present. The execute path obtains a second complete snapshot, requires the same binding digest, resolves an absolute `scancel`, executes only then, and reads target state back.
- `REQUIRE_FRESH_HUMAN`: executes nothing, retains the target, and emits the exact short human request.
- `DENY_UNKNOWN_OR_FORBIDDEN`: executes nothing.

There is no CLI input that turns chat text, an old race opt-in, `auto_review`, Hook output, or a model-created receipt into protected cancellation authority.

## Consumer inventory

DII:

- Repo-local `slurm-workflows` is copied from central product candidate `b4815a35f708078184bff27b34f185fea6938cc3`.
- The manifest binds that exact collection commit.
- The two standing H100/A100 race policy paragraphs now require central `safe-cancel`; protected/unknown/non-current targets are retained.
- No training, model, data, evaluation, GPU eligibility, budget, or route compatibility contract changed.

CARE authority surfaces:

- `AGENTS.md`
- `.agents/skills/slurm-routing-partition/SKILL.md`
- `prompts/tasks/20260801_care_target_domain_race_gap_closure_controller.md`
- `prompts/blueprints/CARE_target_domain_race_gap_closure_20260801.md`

CARE reachable consumers:

- `scripts/route_B_round04/watch_B1_race.py`
- `scripts/evaluation/watch_care_srr_cascade_formal_race.py`
- `scripts/evaluation/watch_srr_v3_m7_routing.py`
- `scripts/evaluation/watch_srr_v3_m8_myops_race.py`
- `scripts/target_domain_gap_closure/monitor_interactive_takeover.py`

All use `scripts/ops/slurm_safe_cancel.py`; none has a direct `scancel` fallback. The adapter treats an executed result as true only when the central decision is also `ALLOW_OWNED_UNPROTECTED`. Missing entry, timeout, malformed output, unknown decision, and nonzero failure retain the target.

`results/20260711_srr_v3_m10_complete_mechanism_repair/wave2_partition_race_watcher.py` is historical/non-entry. Current authority and reachable watcher paths do not route to it. Remaining references identify historical result inputs in old plans/evaluators; the historical artifact was not mechanically rewritten.

## Deterministic validation

AI Skills candidate:

- targeted protected-cancel tests: PASS, 5 tests
- `python -m unittest tests.test_slurm_workflows`: PASS, 21 tests
- `python -m unittest tests.test_skill_update`: PASS, 11 tests
- `python scripts/skills.py validate`: PASS, 155 active skills and 18 profiles
- `python scripts/skills.py audit --all`: PASS
- `python -m unittest discover -s tests`: PASS, 344 tests
- Python compilation and `git diff --check`: PASS

DII candidate:

- installed skill file parity with central product candidate: PASS
- manifest `collection_commit`: PASS, exact `b4815a35f708078184bff27b34f185fea6938cc3`
- installed `slurm-workflows` version: PASS, `0.4`
- installed normal-entry CLI discovery: PASS; `safe-cancel` and its bounded arguments are present
- `git diff --check`: PASS

CARE candidate:

- `python -m unittest tests.ops.test_slurm_safe_cancel`: PASS, 3 tests
- reachable-watcher direct-call scan: PASS
- authority-surface central-entry scan: PASS
- six changed Python files compile: PASS
- `git diff --check`: PASS
- no watcher or Slurm command was executed during validation

## G1-G6

- G1: `PARTIAL_PHASE4`. Generic exact-target, protection-union, protected-partition, protected-accelerator, cross-cluster and unknown-fact behavior passes deterministic tests. Real Longleaf `htzhulab` plus H100 private-policy installation/readback is intentionally deferred until Reviewer PASS.
- G2: `PASS_CANDIDATE`. Protected normal entry returns `REQUIRE_FRESH_HUMAN`, executes nothing, and produces a target-bound retain-by-default request. Model/chat representations remain non-authorizing.
- G3: `BLOCKED_BY_ISOLATION`. Consumer no-direct-fallback evidence passes. Dangerous fake cancellation, absolute-path, Python/shell, array/batch, and holder-equivalent replay was not run because this Longleaf process cannot prove ER-02 isolation. Host Policy rules are candidate-only and not deployed. No hard same-UID isolation claim is made.
- G4: `PASS_IMPLEMENTATION / EXECUTION_REPLAY_DEFERRED`. Source requires a second live snapshot and identical binding before mutation; decision-level state/target/policy changes fail closed. The mutation-bearing replay remains blocked by ER-02.
- G5: `PASS_CANDIDATE`. Central routing/race/sticky/persistent/doctor regressions pass. DII and CARE changes are limited to cancellation routing. Actual unprotected cancellation is not claimed tested on Longleaf.
- G6: `PARTIAL_PHASE3`. Exact product and consumer commits are frozen. Production install identity, private-policy readback, active Host Policy readback, independent Reviewer PASS, integration, and release remain pending.

## Safety and stop point

- `REAL_SLURM_MUTATION = NO`
- No `sbatch`, `salloc`, `srun`, `scancel`, mutating `scontrol`, holder signal, requeue, release, or suspend was run.
- No Longleaf private config or active Host Policy was modified.
- No main branch was integrated.
- No version was bumped and no release was advanced.
- Phase 4 remains forbidden until the user returns an independent Reviewer PASS bound to the three exact product/consumer commits.

## Maintenance tracking

- Existing Issue search found no tracking Issue for this protected-cancellation item; closed #96 belongs to the completed race-policy task and was not reused.
- `CLEAR_WRITING_UNAVAILABLE`: the installed skill file is readable, but the only available auditable replay path would start a new model call, which the frozen Kickoff forbids. Reading the skill file alone was not treated as a Clear Writing invocation.
- No reader-facing Issue or Project mutation was made, and `docs/skill-todos/slurm-workflows.md` truthfully remains `PENDING_CLEAR_WRITING`.
- Exact pending mutation: a later Clear Writing-capable, authorized maintainer must review the title `防止 AI 未经本人确认取消受保护 Slurm 作业` and the required Issue body fields, create a new `maintenance-track` Issue with `kind:regression`, `scope:cross-repo`, and Area `standalone-skill`, write its real `tracking: #N` backlink, and set lifecycle `DOING` with these three exact candidate branches as the current anchor. Do not reuse #96 and do not mark ADAPTING or DONE at this phase.
