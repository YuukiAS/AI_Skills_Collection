# 059 Candidate Plugin Replay Stage 0 config drift — Kickoff amendment v0.1

继续同一 059 task，只实现已批准的 Stage 0 config-drift recovery amendment。

Repository：

`YuukiAS/AI_Skills_Collection`

Task：

`research-authoring--formal-production-authoring`

Branch：

`work/research-authoring--formal-production-authoring`

Worktree：

`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

Research Authoring repaired product commit：

`ac501d988f00cb6672fec105ae5fd51a0679cae0`

这个 product commit 不得修改。

Current replay infrastructure head：

`3ec2714e5f7ea386833ee54c365e923235603819`

Stage 0 evidence commit：

`a76d7c36d45e52eaf6b771fd604b691c7b67244c`

Config drift Critic review：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_CRITIC_REVIEW_V0_1_2026-10-06.md`

Critic commit：

`1a39dd916eebdc45ecd4f73b84833fe736c52cb4`

Approved amendment：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_RECOVERY_AMENDMENT_V0_1_2026-10-06.md`

Goal amendment：

`docs/goals/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_GOAL_AMENDMENT_V0_1.md`

## Authorization

I explicitly authorize the exact task worktree and branch above for this bounded execution.

I explicitly authorize the following local-cache side effect only:

When all true plugin/cache invariants are proven:

```text
original tree hash == quarantine tree hash == recorded pre-run tree hash
original plugin manifest hash == quarantine plugin manifest hash == recorded pre-run plugin manifest hash
marketplace/plugin/version/path identity unchanged
quarantine exact path is transaction-owned by this run
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
normalized non-candidate plugin state == recorded pre-run normalized plugin state
```

then, even if the full `$CODEX_HOME/config.toml` hash has drifted, the Executor may:

1. keep the rehydrated original untouched;
2. delete only the exact transaction-owned equivalent quarantine duplicate;
3. fsync the quarantine parent and relevant parent directory;
4. re-read/re-hash the rehydrated original tree and plugin manifest;
5. re-check marketplace/plugin/version/path identity;
6. re-check normalized plugin state against the cleanup-precondition state;
7. remove the recovery manifest only after final verification passes.

The full config hash must still be recorded as diagnostic/provenance evidence, but full config-file drift alone must not block cleanup.

If future work needs plugin-relevant config validation, a future transaction must snapshot an explicit minimal plugin-relevant config projection before mutation. Do not infer the historical config diff after the fact.

## Stage 0

First process the preserved transaction:

```text
run_id=20261006T071703Z-3410223
recovery_manifest=results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/replays/multi_web_writing_failed_ambiguous/recovery-manifest.json
child_stdout=results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/replays/multi_web_writing_failed_ambiguous/child.stdout.jsonl
```

If any hard plugin/cache invariant is missing or mismatched:

```text
RESTORATION_AMBIGUOUS
```

and do not delete, overwrite, continue replay, or claim PASS.

## Implementation scope

Only modify:

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/**
```

## Validation sequence

After Stage 0 and helper amendment form `REPLAY_INFRASTRUCTURE_COMMIT=<I2>`, run:

1. deterministic tests;
2. representative single-plugin replay;
3. `web-development + writing-style` multi-plugin replay;
4. only after multi-plugin PASS, exact 059 development replay against:
   `ac501d988f00cb6672fec105ae5fd51a0679cae0`.

Old evidence rules:

```text
OLD_MULTI_REPLAY=FAIL / RESTORATION_AMBIGUOUS
OLD_SINGLE_PLUGIN_PASS=HISTORICAL_ONLY
NO_RETROACTIVE_PASS=YES
```

## Not authorized

- Research Authoring production change;
- Bridge/Host policy change;
- Plugin Creator;
- live Plugin update;
- permanent uninstall;
- G1-G4 final Gates;
- G4 ChatGPT;
- PDF production;
- paid API;
- private/sensitive external upload;
- main merge, release, tag, GitHub Release;
- force push or destructive Git;
- daemon, watcher, database, or new global state machine.

## Stop condition

After authorized implementation and replay evidence complete, stop with:

```text
SHARED_REPLAY_INFRASTRUCTURE_READY=<YES|NO>
REPLAY_INFRASTRUCTURE_COMMIT=<I2 if created>
REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
EVIDENCE_PACKET_HEAD=<E2 if created>
059_DEVELOPMENT_REPLAY=<PASS|NOT_STARTED|FAIL>
C2_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```
