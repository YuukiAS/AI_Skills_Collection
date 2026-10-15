---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: hpc--slurm-cancel-human-confirmation
implementation_commit: acf8bf29681b404a3c107d25ade527ad1dfe0b89
---

# Codex Result

## Implemented

- Added a deterministic, side-effect-free cancellation classifier with the frozen outcomes `ALLOW_OWNED_UNPROTECTED`, `REQUIRE_FRESH_HUMAN`, and `DENY_UNKNOWN_OR_FORBIDDEN`.
- Required verified cluster identity, verified exact target facts, fully expanded JobIds, PENDING/RUNNING state, partition/accelerator facts, verified current-run ownership, a versioned user-confirmed private policy, and explicit target-set completeness.
- Applied site prohibition, site protection, private `protected_partitions`, and private `protected_accelerators` as a fail-closed union without public site-specific constants.
- Added short target-bound confirmation requests and short-lived single-use confirmation-representation validation. Long Goals, race opt-in, `auto_review`, Hook output, model receipts, `scancel --interactive`, silence, expired receipts, changed state, changed policy, or changed target sets do not validate.
- Kept policy results separate from execution authority. Every result and even a structurally valid human representation has `execution_authorized=false`; Stage A installs no cancellation executor or Hook.
- Extended the existing private local-override mechanism with cancellation policy fields while excluding those values from generated public site summaries.
- Added deterministic G1/G2/G4 tests and an installed normal-entry test. Existing routing, race, sticky-resource, capacity, doctor, and read-only behavior remains covered.
- Recorded ER-02 evidence and a read-only DII/CARE cancellation-consumer inventory. No consumer was changed or run.

## Verification

- `python -m unittest tests.test_slurm_workflows`: PASS, 19 tests.
- `python -m unittest tests.test_skill_update`: PASS, 11 tests.
- `python scripts/skills.py validate`: PASS, 155 active skills and 18 profiles.
- `python scripts/skills.py audit --all`: PASS.
- `git diff --check`: PASS.
- Task-local Reviewed Handoff schema/state preflight: PASS.
- G1 exact identification/private protection union: PASS.
- G2 target-bound human representation: PASS, with no execution authority.
- G3 dangerous replay: `BLOCKED_BY_ISOLATION`; skipped exactly as required by ER-02.
- G4 target/state/policy/ownership revalidation: PASS for pure deterministic coverage.
- G5 existing Slurm capability regression and read-only consumer inventory: PASS.
- G6 claim and release truth: PASS.

Detailed evidence is in `VALIDATION_EVIDENCE.md`, `ER_02_ISOLATION_EVIDENCE.md`, and `CONSUMER_INVENTORY.md` in this result directory.

## Deviations / blockers

- ER-02 could not be proven: the process can see real `/usr/bin/scancel`, `/usr/bin/salloc`, and `ssh`, and shares the host PID namespace. Therefore no fake or real cancellation, API, Python/shell/SSH cancellation, array/batch cancellation, signal, tmux, or allocation-holder simulation was run.
- Full unittest discovery ran 342 tests and ended with 6 failures and 1 error in pre-existing VERSION/Marketplace/presentations/palette baselines. None is a Slurm test, and all affected source/test/generated paths are unchanged from base commit `58ee18cd3e68df77c35b314c5cf9b0e83a985423`.
- Marketplace check remains nonzero on 16 pre-existing presentations/research-writing publication differences. Those unrelated generated surfaces were not rewritten.
- Repository-wide Reviewed Handoff validation remains nonzero on historical task-key/artifact errors and reports no error for this task. The task-local preflight passes.
- Bounded AI Skills Maintainer plugin replay failed closed before child execution with `WRITE_ISOLATION_NOT_ENFORCEABLE`; no raw fallback was used.

## Claim boundary

This commit is a central offline Stage A candidate awaiting independent Reviewer assessment. It does not establish a trusted human approval channel, an unbypassable cancellation executor, a production Hook, Longleaf/H100 deployment, DII/CARE adaptation, formal `slurm-workflows` 0.5, repository release, or real Slurm mutation.

Repository bump decision: `NONE`.

Affected plugins and standalone skills:

- `slurm-workflows`: `NO_BUMP` (remains 0.4).
- Central plugins: `NO_BUMP`.
- Bridge Kit: `NO_CHANGE`.

`REAL_SLURM_MUTATION = NO`
