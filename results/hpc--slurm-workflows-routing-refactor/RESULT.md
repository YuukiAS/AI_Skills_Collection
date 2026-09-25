# Slurm Workflows Routing Refactor Post-Integration Repair Result

RESULT = READY_FOR_FINAL_CRITIC
TASK = hpc--slurm-workflows-routing-refactor
BRANCH = reviewed/hpc--slurm-workflows-routing-refactor
WORKTREE = /tmp/ai-skills-hpc-slurm-workflows-routing-refactor
START_MAIN = 1c39f45c5a6e564c0abc71c3f612e90b6f710189
FORMAL_RELEASE_BASELINE = 29095e580a9b149e2b39931f4518d9d0651cb780
PRE_REPAIR_REVIEWED_REMOTE = 72690e43664367e95fcca83bb1c72c6fadd8f77f
FINAL_CANDIDATE = 20c47de1c2569b32f2b3aff2181fbc55bd179d94

## Required Fields

STICKY_STATE_PERSISTENCE = PASS
- `slurm_routing.py` now persists accepted workload contracts, capacity families, enrollments, and optional evidence locators in `~/.config/ai-skills/slurm-workflows.toml`.
- `tests.test_slurm_workflows.test_g7_sticky_contract_and_right_sizing_hysteresis` proves save/load/reload reuse across independent loads.

CALENDAR_CAPACITY_COVERAGE = PASS
- `capacity_reconcile` now computes the next target window from recurrence/target occurrence, `target_ready_by`, `successor_lead_time`, `minimum_useful_duration`, and latest useful end/cutoff.
- Running allocations and lifecycle successors must cover that target window; more than one lifecycle-owned matching successor fails closed.
- Calendar-bound successor mutation requires verified calendar-submit capability.

ENROLLMENT_DIGEST_FAIL_CLOSED = PASS
- Mutation-capable enrollment now requires exact `scope_digest`; missing, stale, or mismatched digest remains read-only proposal.
- `tests.test_slurm_workflows.test_g8_modes_capacity_reuse_successor_and_enrollment` covers missing digest, wrong digest, unverified calendar submit, and exact digest success.

LEGACY_CONFIG_CLEANUP = PASS
- Fresh generated local override sections now emit blank `race_after_minutes` and blank `race_cancel_policy`; legacy fields remain readable for compatibility.
- `tests.test_slurm_workflows.test_legacy_race_defaults_and_site_aware_doctor` covers the cleanup.

DOCTOR_SITE_AWARE = PASS
- `environment doctor` no longer treats account/partition/qos/scratch/module as universal requirements.
- Missing required fields are derived from public profile constraints; current public Slurm profiles require account only.

G6_TRUE_NORMAL_ENTRY = PASS
- `environment detect` now consumes bounded live Slurm discovery when no public profile matches.
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

REPOSITORY_VERSION = 5.3.0
SLURM_WORKFLOWS_VERSION = 0.2
FULL_TEST_SUITE = PASS
- `python -m unittest discover -s tests` -> PASS, 290 tests, 197.729s.

TRACKING_ISSUE = PENDING_CREATE_OR_BIND
- Search found no existing Slurm Workflows maintenance backlink in `docs/plugin-todos/` or `docs/skill-todos/`.
- Current surface has no GitHub Project mutation tool.
- Pending mutation: create or bind one top-level `maintenance-track` Issue titled `完善 Slurm Workflows 路由与容量维护闭环`; set Area = `slurm-workflows`; Status = `DOING`; current anchor = branch `reviewed/hpc--slurm-workflows-routing-refactor`, candidate `20c47de1c2569b32f2b3aff2181fbc55bd179d94`; next action = independent final Critic review.

PROJECT_STATUS = PENDING_PROJECT_MUTATION_NO_TOOL_SURFACE
FINAL_CRITIC = PENDING
INTEGRATED_TO_MAIN = NO
FORMAL_RELEASE_ADVANCED = NO

## Validation Commands

- `python -m unittest tests.test_slurm_workflows` -> PASS, 12 tests.
- `python -m unittest tests.test_skill_update` -> PASS, 11 tests.
- `python scripts/skills.py validate` -> PASS, 153 active skills, 18 profiles.
- `python scripts/skills.py audit --all` -> PASS.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS, `over_budget=0`.
- `python -m unittest discover -s tests` -> PASS, 290 tests.

## Version Decision

Repository bump decision: NONE
Reason: this is a post-integration repair of the already-integrated `5.3.0` / `slurm-workflows 0.2` candidate; no new release version is introduced and formal `release` remains untouched pending final Critic.

Affected standalone skills:
- slurm-workflows: NO_BUMP, remains 0.2
  Reason: the repair completes the frozen 0.2 behavior rather than creating a new independent release batch.

Affected central plugins:
- all central plugins: NO_BUMP
  Reason: no central Marketplace plugin version changed.

## Independent Final Critic Prompt

Review `YuukiAS/AI_Skills_Collection` task `hpc--slurm-workflows-routing-refactor` on branch `reviewed/hpc--slurm-workflows-routing-refactor`.

Use product candidate:

```text
20c47de1c2569b32f2b3aff2181fbc55bd179d94
```

Read:

- `results/hpc--slurm-workflows-routing-refactor/CODEX_POST_INTEGRATION_REPAIR_PROMPT.md`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md`
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_6_2026-09-24.md`
- changed source and tests in candidate `20c47de1c2569b32f2b3aff2181fbc55bd179d94`

Independently verify whether the post-integration repair contract is satisfied:

- sticky state persists workload/capacity/enrollment/evidence state without creating a history DB;
- capacity lifecycle is calendar-aware and fail-closed for uncovered target windows, multiple successors, and unverified calendar submit options;
- enrollment mutation requires exact valid digest;
- fresh config no longer emits obsolete race defaults while legacy fields stay readable;
- doctor requiredness is site-aware, not generic;
- G6 is true installed normal-entry coverage using fake Slurm on PATH through detect -> plan -> apply -> doctor -> installed helper -> live discovery -> local preference -> route;
- generated references/manifests are public-safe and do not leak fake private raw values;
- G1-G8 and required validation commands are credible and bound to the exact candidate;
- no real Slurm mutation, main integration, release advancement, or self-approval occurred.

Return `PASS` only if the product candidate can proceed to integration/release closure. Otherwise return `REVISE` with concrete file/line findings.
