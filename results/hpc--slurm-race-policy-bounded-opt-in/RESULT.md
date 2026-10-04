# RESULT — hpc--slurm-race-policy-bounded-opt-in

RESULT = READY_FOR_FINAL_CRITIC

## Candidate

Repository: `YuukiAS/AI_Skills_Collection`
Reviewed branch: `reviewed/hpc--slurm-race-policy-bounded-opt-in`
Worktree: `/tmp/ai-skills-hpc-slurm-race-policy-bounded-opt-in`

PRODUCT_CANDIDATE = `5a3dc447da2ea429ba2d229b0301c378be9e8018`

Final Critic repair input:
- Prior reviewed candidate: `cf9bfe16d526811525395d66e05035736e6ecc23`
- Final Critic review: `results/hpc--slurm-race-policy-bounded-opt-in/FINAL_CRITIC_REVIEW_2026-10-04.md`
- Critic conclusion: `REVISE`
- Closed blocker: `RACE-B1_COMPLETE_BOUNDED_GATE`

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

This bounded repair keeps the frozen `slurm-workflows 0.4` race policy and
closes only `RACE-B1_COMPLETE_BOUNDED_GATE`.

Changes in product/test candidate `5a3dc447da2ea429ba2d229b0301c378be9e8018`:

- `duplicate_race_decision()` is now an eligibility helper for site policy plus
  user/local opt-in. It no longer returns a final-looking race authorization.
- Final duplicate-race authorization comes only from
  `bounded_duplicate_race_decision()`.
- Bounded race requires exactly two distinct route identities.
- Candidate workload contracts are compared as full deterministic contracts,
  excluding only route-only fields. Unenumerated scientific fields such as
  augmentation, loss variant, checkpoint selection, and preprocessing fail
  closed when they differ.
- `workload_scope_digest` mismatch fails closed.
- Hard resource requirements are validated for GPU count/type, memory, CPU,
  walltime, and any explicit hard resource fields carried in the frozen
  workload contract.
- The cancellation contract is closed to supported safe semantics:
  `winner_rule = first_running_job`,
  `running_tie_policy = keep_lowest_job_id_cancel_other`, and
  `cancel_loser = true`.
- Unsupported winner/tie policies such as `keep_both`, `do_nothing`, and
  arbitrary strings fail closed.
- Installed normal-entry race smoke now loads the installed
  `slurm-workflows/scripts/slurm_routing.py` helper and verifies the full
  bounded gate, including safe ALLOW and unsafe cancellation DENY cases.

No site profile was changed to `allowed`. Longleaf and CUHK remain
`race_execution = disabled_by_default`.

No Bridge Kit or DII files were modified.

## Validation Evidence

All evidence below was rerun after the RACE-B1 repair and is bound to product
candidate `5a3dc447da2ea429ba2d229b0301c378be9e8018`.

- Race-policy targeted tests: PASS
  - `python -m unittest tests.test_slurm_workflows.SlurmWorkflowsRoutingTests.test_g3_g4_job_identity_and_duplicate_race_fail_closed tests.test_slurm_workflows.SlurmWorkflowsRoutingTests.test_duplicate_race_policy_opt_in_truth_table_and_bounded_contract tests.test_slurm_workflows.SlurmWorkflowsRoutingTests.test_g6_installed_normal_entry_duplicate_race_bounded_gate`
- Complete Slurm workflow tests / G1-G8 surface: PASS
  - `python -m unittest tests.test_slurm_workflows`
  - Result: `Ran 15 tests ... OK`
- `tests.test_skill_update`: PASS
  - `python -m unittest tests.test_skill_update`
  - Result: `Ran 11 tests ... OK`
- Version-dependent tests: PASS
  - `python -m unittest tests.test_standalone_skill_baselines tests.test_codex_marketplace tests.test_central_plugin_icon_assets`
  - Result: `Ran 53 tests ... OK`
- Skill validation: PASS
  - `python scripts/skills.py validate`
  - Result: `validated 154 active skills, 18 profiles, templates, and trigger eval scaffolds`
- Skill audit: PASS
  - `python scripts/skills.py audit --all`
  - Existing context-budget guidance emitted; command exit status was 0.
- Marketplace write/validate/check/path-report: PASS
  - `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
  - Result: marketplace generated/validated/checked; Windows path budget `over_budget=0`.
- Installed normal-entry race smoke: PASS
  - Covered by
    `tests.test_slurm_workflows.SlurmWorkflowsRoutingTests.test_g6_installed_normal_entry_duplicate_race_bounded_gate`.
  - The test installs `slurm-workflows`, loads the installed helper from
    `slurm-workflows/scripts/slurm_routing.py`, proves
    `disabled_by_default + explicit opt-in + safe two-route contract => ALLOW`,
    and proves unsafe cancellation `running_tie_policy = keep_both => DENY`.
- Full suite: PASS
  - `python -m unittest discover -s tests`
  - Result: `Ran 331 tests in 74.342s ... OK`
- GitHub CI: PASS
  - Workflow: `codex-marketplace.yml`
  - Run: `37187784359`
  - URL: `https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/37187784359`
  - `head_sha`: `5a3dc447da2ea429ba2d229b0301c378be9e8018`
  - Jobs PASS: `windows-sparse-checkout`, `codex-marketplace`,
    `editable-install-smoke (ubuntu-latest)`,
    `editable-install-smoke (windows-latest)`

Stale evidence explicitly not reused:
- Prior GitHub CI run `37185949083` belongs to
  `cf9bfe16d526811525395d66e05035736e6ecc23` and is stale for this repair.

Clear Writing evidence:
- README pre-update replay: `20261004T065819Z-f5dde8434832` = PASS.
- Issue creation replay: `20261004T070137Z-8b94f123a40f` = PASS.
- README merge-resolution replay: `20261004T071933Z-7a80b26c6bc1` = PASS.
- Issue #96 earlier update replay: `20261004T073131Z-adb53522fae6` = PASS.
- Issue #96 RACE-B1 update replay: `20261004T080847Z-6a802c1a4efb` = PASS.
- Issue #96 RACE-B1 update comment:
  `https://github.com/YuukiAS/AI_Skills_Collection/issues/96#issuecomment-5977986373`.

## Required Final Status Fields

RESULT = READY_FOR_FINAL_CRITIC
PRODUCT_CANDIDATE = `5a3dc447da2ea429ba2d229b0301c378be9e8018`
FORMAL_RELEASE_BASELINE = repository `5.4.3`, `slurm-workflows 0.3`,
`origin/release` `03b0281b1f7fbd29621faa6298cd1db2578a0ffc`
TARGET_REPOSITORY_VERSION = `5.4.4`
SLURM_WORKFLOWS_VERSION = `0.4`
RACE_POLICY_TRUTH_TABLE = PASS
FULL_SCIENTIFIC_CONTRACT_IDENTITY = PASS
HARD_RESOURCE_CONTRACT = PASS
CANCELLATION_POLICY_VALIDATION = PASS
INSTALLED_NORMAL_ENTRY_RACE = PASS
FULL_SUITE = PASS
GITHUB_CI = PASS (`37187784359`, `head_sha` `5a3dc447da2ea429ba2d229b0301c378be9e8018`)
REAL_SLURM_MUTATION = NO
BRIDGE_KIT = NO_CHANGE

## Independent Final Critic Prompt

You are the independent Final Critic for
`YuukiAS/AI_Skills_Collection` task
`hpc--slurm-race-policy-bounded-opt-in`.

Review exact product candidate:

`5a3dc447da2ea429ba2d229b0301c378be9e8018`

Reviewed branch:

`reviewed/hpc--slurm-race-policy-bounded-opt-in`

This is a bounded repair after Final Critic `REVISE` for exactly one blocker:

`RACE-B1_COMPLETE_BOUNDED_GATE`

Do not approve based on this RESULT alone. Check the repository at the exact
candidate and verify:

1. The task remains a bounded Slurm Workflows race-policy repair only.
2. It does not create a successor task, alternate branch/worktree, daemon,
   watcher, queue service, registry, database, state machine, or background
   race controller.
3. It does not modify Bridge Kit or DII consumer repositories.
4. It does not execute or authorize real `sbatch`, `salloc`, `scancel`,
   duplicate GPU race, or weekly GPU enrollment.
5. Formal release baseline is repository `5.4.3` and `slurm-workflows 0.3`;
   target versions remain repository `5.4.4` and `slurm-workflows 0.4`.
6. Central Marketplace plugin versions remain unchanged.
7. `duplicate_race_decision()` is only a site-policy plus user/local opt-in
   eligibility helper. A normal consumer must not treat it as final
   duplicate-race authorization.
8. Final duplicate-race authorization comes only from the full bounded gate.
9. The race-policy truth table is correct:
   - explicit prohibition + opt-in => DENY;
   - missing/`UNKNOWN` + no opt-in => DENY;
   - missing/`UNKNOWN` + opt-in => eligible only, then ALLOW only through the
     complete bounded gate;
   - `disabled_by_default` + opt-in => eligible only, then ALLOW only through
     the complete bounded gate;
   - `explicit_user_opt_in` + opt-in => eligible only, then ALLOW only through
     the complete bounded gate;
   - `allowed` + opt-in => eligible only, then ALLOW only through the complete
     bounded gate;
   - `allowed` + no opt-in => DENY.
10. The bounded helper proves the full contract, not just policy text:
    - exactly two candidates;
    - two candidates have distinct route identities;
    - full workload/scientific contract identity is checked, and unenumerated
      scientific field mismatch fails closed;
    - `workload_scope_digest` mismatch fails closed;
    - hard GPU/resource requirements cannot be downgraded;
    - memory and CPU hard requirements are checked;
    - cancellation contract is required before race;
    - only supported winner/tie policies are accepted;
    - `keep_both`, `do_nothing`, unknown arbitrary strings, and missing rules
      fail closed;
    - explicit prohibition has priority over local opt-in.
11. A valid H100/H100 bounded race is allowed only when the full bounded gate
    passes.
12. A valid H100/A100 race is allowed only when the frozen workload explicitly
    permits both GPU types for the same scientific result.
13. Longleaf and CUHK profiles remain `disabled_by_default`; neither is
    changed to `allowed`.
14. README, CHANGELOG, VERSION, `SKILL.md`, registry/catalog/generated surfaces
    and tests are consistent with repository `5.4.4` and `slurm-workflows 0.4`.
15. Clear Writing was actually invoked for reader-facing README/Issue
    mutations.
16. Issue #96 remains open / DOING, with Resolution commit empty and canonical
    TODO backlink present.
17. Local validation evidence is current for the candidate:
    - race-policy targeted tests PASS;
    - complete `tests.test_slurm_workflows` PASS;
    - `tests.test_skill_update` PASS;
    - version-dependent tests PASS;
    - `scripts/skills.py validate` PASS;
    - `scripts/skills.py audit --all` PASS;
    - Marketplace write/validate/check/path-report PASS;
    - installed normal-entry race smoke PASS;
    - `python -m unittest discover -s tests` PASS.
18. GitHub CI run `37187784359` has `head_sha`
    `5a3dc447da2ea429ba2d229b0301c378be9e8018` and all required jobs PASS.
19. `REAL_SLURM_MUTATION = NO`.

Return `PASS` only if the candidate is ready for final human integration
consideration. Otherwise return `REVISE` with exact file/line findings and the
smallest bounded repair required.
