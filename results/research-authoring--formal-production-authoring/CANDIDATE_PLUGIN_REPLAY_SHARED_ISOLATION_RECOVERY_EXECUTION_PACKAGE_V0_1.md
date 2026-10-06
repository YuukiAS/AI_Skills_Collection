# 059 Candidate Plugin Replay 共享隔离恢复 — Execution Package v0.1

状态：READY_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-06

## Design authority

Approved Proposal：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_PROPOSAL_V0_2_2026-10-06.md`

commit：

`f479efb4e2ad31eaafe6ec56b9fc0ba3f284c569`

Critic PASS：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_CRITIC_REVIEW_V0_2_2026-10-06.md`

commit：

`307904418e42b704e8bf6e0f1f27aa93c1368a87`

## Same-version execution package

1. Implementation Plan v0.1  
   `docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md`  
   commit：`8dbe6b4ee0d359436b231d21632963b4b40346f1`

2. Canonical Goal v0.1  
   `docs/goals/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_GOAL_V0_1.md`  
   commit：`c2eac9aa677fbeffed5114269dfac93c2bd03590`

3. Kickoff Draft v0.1  
   `docs/operations/prompts/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_KICKOFF_V0_1.md`  
   commit：`32eae60e7edbd704a9a49df823cd029ce9a831f2`

All three bind the same existing task：

```text
task_key=research-authoring--formal-production-authoring
branch=work/research-authoring--formal-production-authoring
worktree=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring
REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
```

## Frozen implementation scope

Only：

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
```

plus task-local evidence.

No Research Authoring production change.

## Frozen user-level side effect

The Kickoff explicitly requests bounded user authorization for：

- temporary local cached conflicting-plugin quarantine;
- only inside the existing replay lock;
- exact Skill-name conflict auto-detection;
- quarantine outside plugin discovery root;
- same-filesystem atomic rename only;
- read-only concurrency preflight;
- exact restoration after success/failure/timeout;
- stale recovery on next helper entry;
- fail-closed ambiguous recovery.

It explicitly does not authorize Plugin Creator, remote Plugin mutation, permanent uninstall, other-process control, final Gates, paid API, PDF production, main/release or destructive Git.

## Required stop state

If implementation/tests/replays succeed：

```text
SHARED_REPLAY_INFRASTRUCTURE_READY=YES
REPLAY_INFRASTRUCTURE_COMMIT=<I>
REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
059_DEVELOPMENT_REPLAY=PASS
C2_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

This package itself authorizes no implementation or cache mutation.

Only an independent execution-ready Critic PASS followed by the user actually sending the approved Kickoff can authorize execution.
