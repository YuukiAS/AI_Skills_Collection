# Slurm Workflows Routing Refactor Result

RESULT = READY_FOR_FINAL_CRITIC
TASK = hpc--slurm-workflows-routing-refactor
BRANCH = reviewed/hpc--slurm-workflows-routing-refactor
WORKTREE = /tmp/ai-skills-hpc-slurm-workflows-routing-refactor
START_MAIN = 29095e580a9b149e2b39931f4518d9d0651cb780
FINAL_PREFLIGHT_MAIN = 29095e580a9b149e2b39931f4518d9d0651cb780
FINAL_CANDIDATE = 223b8806a7a94f328da9325ee77d53c7d7b6dbdd

## Gate Evidence

G1 = PASS
- `tests.test_slurm_workflows.test_g1_live_discovery_no_profile_and_unknown_facts`
- `tests.test_slurm_workflows.test_g1_generic_source_has_no_deployment_routing_constants`

G2 = PASS
- `tests.test_slurm_workflows.test_g2_local_preference_orders_legal_routes_without_resource_change`

G3 = PASS
- `tests.test_slurm_workflows.test_g3_g4_job_identity_and_duplicate_race_fail_closed`

G4 = PASS
- `tests.test_slurm_workflows.test_g3_g4_job_identity_and_duplicate_race_fail_closed`
- Duplicate race remains disabled unless site policy explicitly allows it and user/local config opts in.

G5 = PASS
- `tests.test_slurm_workflows.test_g5_bounded_monitoring_replacement`

G6 = PASS
- `tests.test_slurm_workflows.test_g6_no_profile_environment_apply_installed_normal_entry`
- `tests.test_slurm_workflows.test_g6_known_profile_keeps_distinct_local_site_id`
- `tests.test_slurm_workflows.test_g6_no_profile_can_attach_optional_public_overlay`
- These exercise `environment plan/apply`, the installed `slurm-workflows/scripts/slurm_routing.py`, generated public-safe site context, no-profile local site id, distinct local id with known public overlay, optional overlay from no-profile local config, and normal routing helper behavior.

G7 = PASS
- `tests.test_slurm_workflows.test_g7_sticky_contract_and_right_sizing_hysteresis`

G8 = PASS
- `tests.test_slurm_workflows.test_g8_modes_capacity_reuse_successor_and_enrollment`

NO_PROFILE_SITE_NORMAL_ENTRY = PASS
RESOURCE_CONTRACT_STABILITY = PASS
PERSISTENT_CAPACITY_LIFECYCLE = PASS
ENROLLMENT_AUTHORITY = PASS

REAL_PROBE_A = NOT_NEEDED
REAL_PROBE_B = NOT_NEEDED
PROBE_CLEANUP = NOT_APPLICABLE

SLURM_WORKFLOWS_VERSION = 0.2
REPOSITORY_RELEASE_CLASS = MINOR
REPOSITORY_VERSION = 5.3.0
CENTRAL_PLUGIN_BUMPS = NONE
BRIDGE_CHANGE = NO

README_CHECK = PASS
CHANGELOG_CHECK = PASS
FULL_TEST_SUITE = PASS
FINAL_CRITIC = PENDING
INTEGRATED_TO_MAIN = NO
REMOTE_MAIN = 29095e580a9b149e2b39931f4518d9d0651cb780

## Validation Commands

- `python -m unittest tests.test_slurm_workflows` -> PASS, 10 tests.
- `python -m unittest tests.test_skill_update` -> PASS, 11 tests.
- `python -m unittest tests.test_standalone_skill_baselines tests.test_central_plugin_icon_assets tests.test_codex_marketplace tests.test_slurm_workflows tests.test_skill_update` -> PASS, 68 tests.
- `python scripts/skills.py registry --write` -> PASS.
- `python scripts/skills.py catalog --write` -> PASS.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS.
- `python scripts/skills.py validate` -> PASS.
- `python scripts/skills.py audit --all` -> PASS.
- `python -m unittest discover -s tests` -> PASS, 288 tests.

## Critic Revise Closure

Initial final Critic on `6a089c924ba4fe9f128af96b481e8c861c1c324c` returned REVISE because:

- `local_site_id` and `policy_overlay_id` were folded together in environment plan/apply;
- G6 lacked installed-path coverage for distinct local id plus known public overlay, and no-profile local id plus optional public overlay;
- `FINAL_CANDIDATE` was not bound to an exact SHA.

Closure in `223b8806a7a94f328da9325ee77d53c7d7b6dbdd`:

- `requested_site_id`, `local_site_id`, and `policy_overlay_id` are tracked separately through plan/apply/manifest;
- G6 includes installed-path tests for no-profile/no-overlay, known-profile/distinct-local-id, and no-profile/optional-public-overlay;
- this result file binds gate evidence to the exact product candidate SHA above.

## Version Decision

Repository bump decision: MINOR
Reason: no-profile Slurm environment materialization and installed normal use are a new repository-level environment/install capability.

Affected plugins:
- all central plugins: NO_BUMP
  Reason: central Marketplace plugin production behavior and versions are unchanged.

Affected standalone skills:
- slurm-workflows: 0.1 -> 0.2
  Reason: the standalone Skill now ships user-facing live discovery, optional policy overlay, sticky resource contract, routing safety, and persistent-capacity lifecycle behavior.
