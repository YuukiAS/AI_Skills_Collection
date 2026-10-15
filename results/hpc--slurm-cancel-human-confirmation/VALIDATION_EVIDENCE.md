# Stage A validation evidence

Date: 2026-10-15

## Passed checks

- `python -m unittest tests.test_slurm_workflows`
  - PASS: 19 tests.
  - Covers the cancellation truth table, exact target expansion, private/site protection union, protected accelerator/partition matching, same-named partitions on distinct clusters, verified current-run ownership, old jobs, PENDING/RUNNING binding, policy/target/state invalidation, untrusted confirmation sources, installed normal entry, generated privacy, and all existing Slurm G1-G8 regression tests.
- `python -m unittest tests.test_skill_update`
  - PASS: 11 tests.
- `python scripts/skills.py validate`
  - PASS: 155 active skills, 18 profiles, templates, and trigger evaluation scaffolds.
- `python scripts/skills.py audit --all`
  - PASS.
- `git diff --check`
  - PASS.
- Task-local Reviewed Handoff preflight
  - PASS for task key, `AI_BRIDGE_REVIEWED_CURRENT_V1`, `AI_BRIDGE_REVIEWED_PLAN_V2`, `PLAN_FROZEN`, `RUN_CODEX_EXECUTOR`, base commit, and plan revision.

All Python runs used `PYTHONDONTWRITEBYTECODE=1` because the task worktree is mounted read-only for ordinary process writes. The successful targeted runs wrote only to their temporary directories; two unrelated full-suite tests that write tracked presentation/palette outputs failed as recorded below.

## G1-G6 result

- G1: PASS for deterministic offline classification and existing read-only/normal-entry regression coverage.
- G2: PASS for the target-bound representation. A valid representation still returns `execution_authorized=false`; no trusted human channel or executor is claimed.
- G3: `BLOCKED_BY_ISOLATION` for dangerous replay. See `ER_02_ISOLATION_EVIDENCE.md`. No mutation or signal path was run.
- G4: PASS for pure revalidation and existing replacement fail-closed behavior. Target, state, policy, dependency and ownership facts are included in the binding.
- G5: PASS for central offline regressions and read-only consumer inventory. DII/CARE remain explicitly unadapted.
- G6: PASS for claim scoping: this is an offline central candidate only, with no release, deployment, trusted cancellation executor, Hook install or consumer adaptation.

## Repository-wide baseline failures

`python -m unittest discover -s tests` ran 342 tests and finished with 6 failures and 1 error. None is in the Slurm module:

- repository `VERSION` is 5.4.4 while `test_central_plugin_icon_assets` expects 5.5.0;
- Marketplace/TODO/generated parity has pre-existing presentations and research-writing differences;
- presentation and palette tests attempt to write tracked outputs, but this task worktree is read-only to ordinary processes;
- presentation source/mirror content is already divergent.

`python scripts/build_codex_marketplace.py --validate --check --path-report` likewise reports 16 pre-existing presentations/research-writing publication differences. `git diff 58ee18cd3e68df77c35b314c5cf9b0e83a985423` is empty for `VERSION`, Marketplace payloads, plugin TODOs, presentations sources, palette sources, and all failing test modules. Those unrelated baselines were not regenerated or changed.

The formal `ai-bridge reviewed-handoff validate` command scans every historical task and remains nonzero on pre-existing legacy task-key and missing historical artifact errors; it reports no error for `hpc--slurm-cancel-human-confirmation`. The task-local preflight above passes.

## Maintenance preflight limitation

The bounded `ai-bridge plugin-replay` preflight failed closed before child execution with `WRITE_ISOLATION_NOT_ENFORCEABLE` (run `20261015T173809Z-2d5a41e43488`). No raw nested Codex fallback was used. The installed/enabled AI Skills Maintainer contract was applied in the current session; this limitation does not expand Stage A's claims.

## Version and mutation truth

- Repository bump decision: `NONE`.
- `slurm-workflows`: `NO_BUMP` (remains 0.4).
- Central plugins: `NO_BUMP`.
- Bridge Kit: unchanged.
- Real Slurm mutation: `NO`.
