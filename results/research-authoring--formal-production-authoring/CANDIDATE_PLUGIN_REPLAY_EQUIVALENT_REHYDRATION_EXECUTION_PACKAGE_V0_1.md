# 059 Candidate Plugin Replay 等价再水化恢复 — Amended Execution Package v0.1

状态：READY_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-06

## Approved recovery authority

Recovery Proposal：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_PROPOSAL_V0_1_2026-10-06.md`  
commit：`b0b9fc8c50251789fe97f21395637f7060cd7d89`

Plan amendment：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_AMENDMENT_V0_1_2026-10-06.md`  
commit：`3b2d747f07a69f808d092fc2c24daf22a4687780`

Critic PASS：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_CRITIC_REVIEW_V0_1_2026-10-06.md`  
commit：`7a3dd5b19db779d17d224cec1dd8cba0a4a9f182`

## Same-version amended execution objects

1. Canonical Goal Amendment v0.1  
   `docs/goals/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_GOAL_AMENDMENT_V0_1.md`  
   commit：`eae4bd36c52965406fc6d35a7f852b1cf52e4939`

2. Kickoff Draft Amendment v0.1  
   `docs/operations/prompts/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_KICKOFF_AMENDMENT_V0_1.md`  
   commit：`4b5edec8df8773ce97702404fa87d7b8a8e658f9`

The amended Goal and Kickoff bind the already-approved recovery Proposal and Plan amendment. No new architecture is introduced.

## Existing task identity

```text
task_key=research-authoring--formal-production-authoring
branch=work/research-authoring--formal-production-authoring
worktree=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring
```

## Current identities

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

PRIOR_REPLAY_INFRASTRUCTURE_COMMIT=
b61c46957709030bee3735c77d21701871f0480b

CURRENT_EVIDENCE_PACKET_HEAD=
dcf9381eacc6c56f954fc3ca60f3ab8e351d1fb1

NEW_REPLAY_INFRASTRUCTURE_COMMIT=
NOT_CREATED

C2_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
```

## Stage 0 frozen requirement

Before helper amendment or any new replay, the current preserved dual-copy transaction must be reconciled first.

Run：

`20261006T071703Z-3410223`

Cleanup is allowed only when the full `VERIFIED_EQUIVALENT_REHYDRATION` contract passes.

If it passes：

- keep rehydrated original untouched;
- delete only the exact transaction-owned equivalent quarantine duplicate;
- fsync;
- re-verify persistent state;
- remove recovery manifest only after final equality.

If any proof fails：

`RESTORATION_AMBIGUOUS`

and do not delete, overwrite, modify helper, or launch replay.

## Frozen implementation scope

Only：

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
```

plus task-local evidence.

No Research Authoring production change.

## Frozen validation sequence

After safe Stage 0 recovery and helper amendment：

1. deterministic helper tests;
2. form `REPLAY_INFRASTRUCTURE_COMMIT=<I2>`;
3. rerun representative single-plugin replay under I2;
4. rerun `web-development + writing-style` multi-plugin replay under I2;
5. only after multi-plugin PASS, run exact 059 development replay using `ac501d98...`.

Old multi replay remains permanently FAIL.
Old `b61c...` single-plugin PASS is historical only.

## User-level mutation authorization represented by the Kickoff

The Kickoff explicitly requests bounded user authorization for：

- previously approved temporary local conflicting-plugin quarantine/restoration;
- conditional deletion of only the transaction-owned quarantine duplicate under complete `VERIFIED_EQUIVALENT_REHYDRATION`;
- retaining the rehydrated original untouched;
- fsync and final persistent-state verification;
- no deletion under any ambiguity.

It does not authorize Plugin Creator, remote Plugin mutation, permanent uninstall, Research Authoring production changes, final Gates, paid API, PDF production, main/release, or destructive Git.

## Required stop state

If amended infrastructure execution succeeds：

```text
SHARED_REPLAY_INFRASTRUCTURE_READY=YES
REPLAY_INFRASTRUCTURE_COMMIT=<I2>
REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
EVIDENCE_PACKET_HEAD=<E2>
059_DEVELOPMENT_REPLAY=PASS
C2_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

This package itself authorizes no implementation, cleanup, or replay.
Only an independent execution-ready Critic PASS followed by the user actually sending the approved amended Kickoff may authorize execution.
