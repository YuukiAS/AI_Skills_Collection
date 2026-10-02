# Dependent execution blocker review

Date: 2026-10-02  
Critic result: `RECOVERY_REQUIRES_PLANNER`

Observed identities:

```text
origin/main = 4ce1946ba047ea200c4ab41ae824de999ef535ed
task branch = 94e3ecae9764c00bbeb8d5965f14cb0af695b0c3
merge base = 98721a202bc557c0b9c0800e66e50cab466bfba2
```

The Executor stopped correctly. The blocker is real, but its current form is no longer the original R3 condition alone: current `main` has moved materially since the approved implementation package and now changes both the shared replay test baseline and repository release identity.

## D1 — shared replay timeout drift

Current `main` sets the relevant `tests/test_candidate_plugin_replay.py` timeout to `3`, introduced by commit `2b260f1e81cc736333c92705e45bde13ca51993f` as part of workflow-core candidate replay qualification.

The task branch currently has `0.5` after the bounded R3 repair.

Therefore the branch still differs from current main on a shared test that is outside the Project Instructions Editor scope.

The correct recovery is not to choose a new timeout inside this task. The task branch should inherit the current-main value through a bounded main synchronization, so the Project Instructions Editor task no longer owns that shared-test difference.

## D2 — repository VERSION drift

Current `main:VERSION` is now `5.4.1`, not `5.4.0`.

The approved implementation package explicitly requires `VERSION_DRIFT` to return to Planner before release-candidate metadata is continued.

The previously approved release type remains `MINOR`; if current main remains `5.4.1`, the resulting candidate target is still `5.5.0`.

However the candidate must now preserve the current-main `5.4.1` release history and current central-plugin state, including workflow-core `0.5`, rather than carrying forward stale `5.4.0` / workflow-core `0.4` assumptions.

## Required recovery shape

Return to Planner for a minimal execution-package amendment. Do not reopen product design.

The bounded recovery should:

1. explicitly authorize synchronization of current `origin/main` into the exact task branch using a non-force history-preserving route;
2. avoid rebasing/pushing rewritten history because force push is outside the approved authorization;
3. resolve any merge conflicts by preserving current-main shared behavior and the already-approved Project Instructions Editor candidate additions;
4. inherit `timeout_seconds=3` from current main without task-specific timeout redesign;
5. update release-candidate parity so the candidate is based on `5.4.1`, while keeping the approved MINOR target `5.5.0` if main remains `5.4.1`;
6. preserve current-main workflow-core `0.5` and other unrelated main changes;
7. create a new exact final candidate commit only after the synchronization and candidate-owned reconciliation are complete;
8. rerun deterministic/full validation and G1-G4 evidence under the existing same-final-candidate contract.

The existing R1/R2 evidence requirements remain open. R3 is superseded by this current-main synchronization requirement rather than closed by forcing the branch back to an obsolete `0.5` timeout.

```text
DEPENDENT_EXECUTION_BLOCKED=YES
RECOVERY_REQUIRES_PLANNER=YES
PRODUCT_DESIGN_REOPEN=NO
R1=OPEN
R2=OPEN
R3=SUPERSEDED_BY_CURRENT_MAIN_SYNC
VERSION_DRIFT=YES
READY_FOR_GATES=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
NEXT_HANDOFF=PLANNER
```
