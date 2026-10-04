# RESULT — hpc--slurm-race-policy-bounded-opt-in

RESULT = READY_FOR_FINAL_CRITIC

## Candidate

Repository: `YuukiAS/AI_Skills_Collection`
Reviewed branch: `reviewed/hpc--slurm-race-policy-bounded-opt-in`
Worktree: `/tmp/ai-skills-hpc-slurm-race-policy-bounded-opt-in`

PRODUCT_CANDIDATE = `cf9bfe16d526811525395d66e05035736e6ecc23`

Formal release baseline:
- `origin/release` = `03b0281b1f7fbd29621faa6298cd1db2578a0ffc`
- Repository `VERSION` on release = `5.4.3`
- `slurm-workflows` on release = `0.3`

Target versions:
- Repository = `5.4.4`
- `slurm-workflows` = `0.4`
- Central Plugins = `NO_BUMP`
- Bridge Kit = `NO_CHANGE`

Maintenance tracking:
- Issue: `#96`
- Project Status: `DOING`
- Resolution commit: empty
- Canonical TODO backlink: `docs/skill-todos/slurm-workflows.md`

REAL_SLURM_MUTATION = NO

## Implementation Summary

`slurm-workflows 0.4` changes duplicate race from "site must explicitly allow"
to a bounded opt-in policy:

- race remains off by default;
- user/local explicit opt-in is required;
- explicit site prohibition blocks race;
- `missing`, `UNKNOWN`, `disabled_by_default`, and `explicit_user_opt_in`
  site policy can proceed only when no prohibition is known and the bounded
  two-route contract is satisfied;
- race is limited to exactly two candidate routes;
- both routes must preserve the same workload/scientific contract;
- both routes must satisfy hard resource requirements;
- winner/loser cancellation and near-simultaneous RUNNING behavior must be
  frozen before submission.

No site profile was changed to `allowed`. Longleaf and CUHK remain
`race_execution = disabled_by_default`.

## Validation Evidence

All evidence below was rerun after reconciling latest compatible `origin/main`
and is bound to product candidate
`cf9bfe16d526811525395d66e05035736e6ecc23`.

- Race-policy targeted tests: PASS
  - `python -m unittest tests.test_slurm_workflows.SlurmWorkflowsRoutingTests.test_g3_g4_job_identity_and_duplicate_race_fail_closed tests.test_slurm_workflows.SlurmWorkflowsRoutingTests.test_duplicate_race_policy_opt_in_truth_table_and_bounded_contract`
- Complete Slurm workflow tests / G1-G8 surface: PASS
  - `python -m unittest tests.test_slurm_workflows`
- `tests.test_skill_update`: PASS
  - `python -m unittest tests.test_skill_update`
- Version-dependent tests: PASS
  - `python -m unittest tests.test_standalone_skill_baselines tests.test_central_plugin_icon_assets tests.test_codex_marketplace`
- Skill validation: PASS
  - `python scripts/skills.py validate`
- Skill audit: PASS
  - `python scripts/skills.py audit --all`
  - Existing context-budget guidance emitted; command exit status was 0.
- Marketplace write/validate/check/path-report: PASS
  - `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
- Normal-entry smoke: PASS
  - Covered by `tests.test_slurm_workflows` G6 tests and `tests.test_skill_update`.
- Full suite: PASS
  - `python -m unittest discover -s tests`
  - Result: `Ran 330 tests ... OK`
- GitHub CI: PASS
  - Workflow: `codex-marketplace.yml`
  - Run: `37185949083`
  - `head_sha`: `cf9bfe16d526811525395d66e05035736e6ecc23`
  - Jobs PASS: `windows-sparse-checkout`, `codex-marketplace`,
    `editable-install-smoke (ubuntu-latest)`,
    `editable-install-smoke (windows-latest)`

Clear Writing evidence:
- README pre-update replay: `20261004T065819Z-f5dde8434832` = PASS.
- Issue creation replay: `20261004T070137Z-8b94f123a40f` = PASS.
- README merge-resolution replay: `20261004T071933Z-7a80b26c6bc1` = PASS.
- Issue #96 update replay: `20261004T073131Z-adb53522fae6` = PASS.
- Issue #96 update comment:
  `https://github.com/YuukiAS/AI_Skills_Collection/issues/96#issuecomment-5977736691`.

## Required Final Status Fields

RESULT = READY_FOR_FINAL_CRITIC
PRODUCT_CANDIDATE = `cf9bfe16d526811525395d66e05035736e6ecc23`
FORMAL_RELEASE_BASELINE = repository `5.4.3`, `slurm-workflows 0.3`,
`origin/release` `03b0281b1f7fbd29621faa6298cd1db2578a0ffc`
TARGET_REPOSITORY_VERSION = `5.4.4`
SLURM_WORKFLOWS_VERSION = `0.4`
RACE_POLICY_TRUTH_TABLE = PASS
BOUNDED_TWO_ROUTE_CONTRACT = PASS
HARD_RESOURCE_REQUIREMENT = PASS
LOSER_CANCELLATION_CONTRACT = PASS
NORMAL_ENTRY_SMOKE = PASS
FULL_SUITE = PASS
GITHUB_CI = PASS (`37185949083`)
REAL_SLURM_MUTATION = NO
BRIDGE_KIT = NO_CHANGE

## Independent Final Critic Prompt

You are the independent Final Critic for
`YuukiAS/AI_Skills_Collection` task
`hpc--slurm-race-policy-bounded-opt-in`.

Review exact product candidate:

`cf9bfe16d526811525395d66e05035736e6ecc23`

Reviewed branch:

`reviewed/hpc--slurm-race-policy-bounded-opt-in`

Do not approve based on this RESULT alone. Check the repository at the exact
candidate and verify:

1. The task is a bounded Slurm Workflows race-policy repair only.
2. It does not create a successor task, alternate branch/worktree, daemon,
   watcher, queue service, registry, database, state machine, or background
   race controller.
3. It does not modify Bridge Kit or DII consumer repositories.
4. It does not execute or authorize real `sbatch`, `salloc`, `scancel`,
   duplicate GPU race, or weekly GPU enrollment.
5. Formal release baseline is repository `5.4.3` and `slurm-workflows 0.3`;
   target versions are repository `5.4.4` and `slurm-workflows 0.4`.
6. Central Marketplace plugin versions remain unchanged.
7. The race-policy truth table is correct:
   - explicit prohibition + opt-in => DENY;
   - missing/`UNKNOWN` + no opt-in => DENY;
   - missing/`UNKNOWN` + opt-in => ALLOW only through bounded contract;
   - `disabled_by_default` + opt-in => ALLOW only through bounded contract;
   - `explicit_user_opt_in` + opt-in => ALLOW only through bounded contract;
   - `allowed` + opt-in => ALLOW only through bounded contract;
   - `allowed` + no opt-in => DENY.
8. The bounded helper proves the full contract, not just policy text:
   - exactly two candidates;
   - matching workload/scientific contract;
   - hard GPU/resource requirements cannot be downgraded;
   - cancellation contract is required before race;
   - explicit prohibition has priority over opt-in.
9. Longleaf and CUHK profiles remain `disabled_by_default`; neither is changed
   to `allowed`.
10. README, CHANGELOG, VERSION, `SKILL.md`, registry/catalog/generated surfaces
    and tests are consistent with repository `5.4.4` and
    `slurm-workflows 0.4`.
11. Clear Writing was actually invoked for README and Issue mutations.
12. Issue #96 remains open / DOING, with Resolution commit empty and canonical
    TODO backlink present.
13. Local validation evidence is current for the candidate:
    - race-policy targeted tests PASS;
    - complete `tests.test_slurm_workflows` PASS;
    - `tests.test_skill_update` PASS;
    - version-dependent tests PASS;
    - `scripts/skills.py validate` PASS;
    - `scripts/skills.py audit --all` PASS;
    - Marketplace write/validate/check/path-report PASS;
    - `python -m unittest discover -s tests` PASS.
14. GitHub CI run `37185949083` has `head_sha`
    `cf9bfe16d526811525395d66e05035736e6ecc23` and all required jobs PASS.

Return `PASS` only if the candidate is ready for final human integration
consideration. Otherwise return `REVISE` with exact file/line findings and the
smallest bounded repair required.
