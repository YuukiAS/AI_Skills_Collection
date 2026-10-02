# Slurm Workflows Routing Refactor Post-Integration Repair Result

RESULT = READY_FOR_FINAL_CRITIC
TASK = hpc--slurm-workflows-routing-refactor
BRANCH = reviewed/hpc--slurm-workflows-routing-refactor
WORKTREE = /tmp/ai-skills-hpc-slurm-workflows-routing-refactor
START_MAIN = f1b35d04e5bd63d0f974c0080e937e9c7f919cc9
FORMAL_RELEASE_BASELINE = a7028195f3e97d32d51c32ef8c87f658f92048e5
PRE_REPAIR_REVIEWED_REMOTE = b1889c9364c98deae4928a5e60192f1a147dea88
RECONCILED_MAIN_MERGE = e0c09d633f226f7c7a6d1644f071665f272ac9fb
FINAL_CANDIDATE = a2b511ebaca3abebb0515cd9acec8c35b58ec1d6

## Scope And Drift

- Existing worktree was recoverable at `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`.
- `origin/main` was fetched and had advanced to `f1b35d04e5bd63d0f974c0080e937e9c7f919cc9`.
- `origin/release` remained `a7028195f3e97d32d51c32ef8c87f658f92048e5`.
- Diff from task merge base `1c39f45c5a6e564c0abc71c3f612e90b6f710189` to latest `origin/main` showed no new Slurm production source/test semantic drift.
- `origin/main` was merged into the existing reviewed branch with ordinary non-force merge commit `e0c09d633f226f7c7a6d1644f071665f272ac9fb`.
- No rebase, force-push, main integration, release advancement, or new task/branch occurred.

## Required Fields

STICKY_STATE_PERSISTENCE = PASS
- Candidate keeps the `~/.config/ai-skills/slurm-workflows.toml` state contract for accepted workload contracts, capacity families, enrollments, and optional evidence locators.
- `tests.test_slurm_workflows.test_g7_sticky_contract_and_right_sizing_hysteresis` proves save/load/reload reuse across independent loads.

CALENDAR_CAPACITY_COVERAGE = PASS
- `capacity_reconcile` computes target windows from recurrence/target occurrence, `target_ready_by`, `successor_lead_time`, `minimum_useful_duration`, and latest useful end/cutoff.
- Running allocations and lifecycle successors must cover the next target window; multiple lifecycle-owned matching successors fail closed.
- Calendar-bound successor mutation remains gated on verified calendar-submit capability.

ENROLLMENT_DIGEST_FAIL_CLOSED = PASS
- Mutation-capable enrollment requires exact valid `scope_digest`.
- Missing, stale, or mismatched digest remains a read-only proposal.
- `tests.test_slurm_workflows.test_g8_modes_capacity_reuse_successor_and_enrollment` covers missing digest, wrong digest, unverified calendar submit, and exact digest success.

LEGACY_CONFIG_CLEANUP = PASS
- Fresh generated local override sections emit blank `race_after_minutes` and blank `race_cancel_policy`.
- Legacy fields remain readable for compatibility.
- `tests.test_slurm_workflows.test_legacy_race_defaults_and_site_aware_doctor` covers the cleanup.

DOCTOR_SITE_AWARE = PASS
- `environment doctor` derives requiredness from public profile constraints and local/live facts instead of universal account/partition/qos/scratch/module assumptions.
- Current public Slurm profiles require account only.

G6_TRUE_NORMAL_ENTRY = PASS
- `environment detect` consumes bounded live Slurm discovery when no public profile matches.
- `tests.test_slurm_workflows.test_g6_true_normal_entry_detect_plan_apply_doctor_installed_live_route` runs fake Slurm CLI on PATH through detect -> plan -> apply -> doctor -> installed `slurm-workflows` -> installed live discovery -> local preference -> routing plan.
- Covered installed scenarios: no-profile arbitrary third-party, known overlay + distinct local id, no-profile + optional overlay, hidden detail/unavailable association -> `UNKNOWN`.

PUBLIC_SAFE_GENERATED_REFERENCE = PASS
- Repo-targeted generated site references and manifests use public-safe locators/aliases for local overrides and managed paths.
- Regression test uses fake private ClusterName/controller/local paths and asserts raw private values are not written.

G1 = PASS
- `tests.test_slurm_workflows.test_g1_live_discovery_no_profile_and_unknown_facts`
- `tests.test_slurm_workflows.test_g1_generic_source_has_no_deployment_routing_constants`

G2 = PASS
- `tests.test_slurm_workflows.test_g2_local_preference_orders_legal_routes_without_resource_change`

G3 = PASS
- `tests.test_slurm_workflows.test_g3_g4_job_identity_and_duplicate_race_fail_closed`

G4 = PASS
- `tests.test_slurm_workflows.test_g3_g4_job_identity_and_duplicate_race_fail_closed`

G5 = PASS
- `tests.test_slurm_workflows.test_g5_bounded_monitoring_replacement`

G6 = PASS
- `tests.test_slurm_workflows.test_g6_no_profile_environment_apply_installed_normal_entry`
- `tests.test_slurm_workflows.test_g6_true_normal_entry_detect_plan_apply_doctor_installed_live_route`
- `tests.test_slurm_workflows.test_g6_known_profile_keeps_distinct_local_site_id`
- `tests.test_slurm_workflows.test_g6_no_profile_can_attach_optional_public_overlay`

G7 = PASS
- `tests.test_slurm_workflows.test_g7_sticky_contract_and_right_sizing_hysteresis`

G8 = PASS
- `tests.test_slurm_workflows.test_g8_modes_capacity_reuse_successor_and_enrollment`

REAL_SLURM_MUTATION = NO
- No `sbatch`, `salloc`, `scancel`, mutating `scontrol`, or real enrollment was run.
- Live-path proof used deterministic fake Slurm commands on PATH.

REPOSITORY_VERSION = 5.4.1
SLURM_WORKFLOWS_VERSION = 0.3

FULL_TEST_SUITE = PASS
- `python -m unittest discover -s tests` -> PASS, 319 tests, 76.988s.
- Current venv was missing test dependencies `setuptools` and `python-pptx`; `python -m ensurepip --upgrade` and `python -m pip install setuptools python-pptx` were used to restore the test environment.
- One unrelated timeout-preservation test in `tests/test_candidate_plugin_replay.py` was made timing-robust by increasing the artificial timeout window from `0.5s` to `2.0s`; it still exercises the timeout branch and passed before full-suite rerun.

TRACKING_ISSUE = #95
- URL: https://github.com/YuukiAS/AI_Skills_Collection/issues/95
- Created after Clear Writing replay with installed `writing-style@yuukias-ai-skills`.
- Labels: `maintenance-track`, `kind:regression`, `scope:standalone-skill`, `area:standalone-skill`.
- Canonical source backlink: `docs/skill-todos/slurm-workflows.md` contains `tracking: #95`.

PROJECT_STATUS = DOING
- Project: `YuukiAS` / `AI Skills Maintenance` #5.
- Project item id: `PVTI_lAHOA0Lgf84BkjCUzg-C1-s`.
- Status field set to `DOING`.
- Area field set to `standalone-skill`.
- Resolution commit intentionally remains empty before final Critic and integration/release closure.

FINAL_CRITIC = PENDING
INTEGRATED_TO_MAIN = NO
FORMAL_RELEASE_ADVANCED = NO

## Validation Commands

- `python -m unittest tests.test_slurm_workflows` -> PASS, 12 tests, 1.909s.
- `python -m unittest tests.test_skill_update` -> PASS, 11 tests, 3.927s.
- `python scripts/skills.py validate` -> PASS, 154 active skills, 18 profiles.
- `python scripts/skills.py audit --all` -> PASS.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS, `over_budget=0`.
- `python -m unittest discover -s tests` -> PASS, 319 tests, 76.988s.

## Version Decision

Repository bump decision: PATCH
Reason: this release improves existing standalone `slurm-workflows` behavior within the current collection contract after the formal release line advanced to `5.4.0`; it does not add a new repository-level user capability.

Affected standalone skills:
- `slurm-workflows`: `0.2` -> `0.3`
  Reason: the repaired candidate changes user-facing Slurm routing/capacity behavior and passes original repair replay coverage, G1-G8, generated parity, and full regression testing.

Affected central plugins:
- all central plugins: NO_BUMP
  Reason: no central Marketplace plugin production behavior changed.

Bridge Kit: NO CHANGE
Reason: this task did not modify Bridge Kit source, distribution, runtime, or release state.

## Independent Final Critic Prompt

Review `YuukiAS/AI_Skills_Collection` task `hpc--slurm-workflows-routing-refactor` on branch `reviewed/hpc--slurm-workflows-routing-refactor`.

Use product candidate:

```text
a2b511ebaca3abebb0515cd9acec8c35b58ec1d6
```

Read:

- `results/hpc--slurm-workflows-routing-refactor/CODEX_POST_INTEGRATION_REPAIR_PROMPT.md`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md`
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_6_2026-09-24.md`
- changed source, tests, version metadata, generated registry/catalog, tracking evidence, and canonical standalone-skill TODO in candidate `a2b511ebaca3abebb0515cd9acec8c35b58ec1d6`

Independently verify whether the post-integration repair contract is satisfied:

- latest compatible `origin/main` was merged into the existing reviewed branch without rebase/force-push and without relevant Slurm semantic conflict;
- sticky state persists workload/capacity/enrollment/evidence state without creating a history DB;
- capacity lifecycle is calendar-aware and fail-closed for uncovered target windows, multiple successors, and unverified calendar submit options;
- enrollment mutation requires exact valid digest;
- fresh config no longer emits obsolete race defaults while legacy fields stay readable;
- doctor requiredness is site-aware, not generic;
- G6 is true installed normal-entry coverage using fake Slurm on PATH through detect -> plan -> apply -> doctor -> installed helper -> live discovery -> local preference -> route;
- generated references/manifests are public-safe and do not leak fake private raw values;
- repository version closure is correct for the current release line: repository `5.4.0 -> 5.4.1`, standalone `slurm-workflows 0.2 -> 0.3`, central Plugins `NO_BUMP`, Bridge Kit `NO CHANGE`;
- GitHub maintenance tracking is one top-level issue, uses Clear Writing before reader-facing Issue creation, binds `docs/skill-todos/slurm-workflows.md` to `tracking: #95`, and keeps Project lifecycle at `DOING` pending review;
- G1-G8 and required validation commands are credible and bound to the exact candidate;
- no real Slurm mutation, main integration, release advancement, or self-approval occurred.

Return `PASS` only if the product candidate can proceed to integration/release closure. Otherwise return `REVISE` with concrete file/line findings.
