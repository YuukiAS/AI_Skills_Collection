# 059 Candidate Plugin Replay Stage 0 config drift — Goal amendment v0.1

状态：DRAFT_FOR_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
日期：2026-10-06  
Repository：`YuukiAS/AI_Skills_Collection`  
Task key：`research-authoring--formal-production-authoring`

## Binding

Base Goal：

`docs/goals/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_GOAL_AMENDMENT_V0_1.md`

Stage 0 evidence：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/stage0_equivalent_rehydration_recovery/STAGE0_EQUIVALENT_REHYDRATION_RECOVERY.json`

Stage 0 evidence commit：

`a76d7c36d45e52eaf6b771fd604b691c7b67244c`

Config drift Critic review：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_CRITIC_REVIEW_V0_1_2026-10-06.md`

Critic commit：

`1a39dd916eebdc45ecd4f73b84833fe736c52cb4`

Recovery amendment：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_RECOVERY_AMENDMENT_V0_1_2026-10-06.md`

## Amended goal

Close the last Stage 0 blocker by narrowing the equivalent-rehydration cleanup invariant:

- continue recording full `$CODEX_HOME/config.toml` hash drift as diagnostic provenance;
- do not use full config-file hash equality as a hard cleanup gate;
- require all package/cache identity, ownership, read-evidence and normalized plugin-state invariants before cleanup;
- after cleanup, re-prove original package identity and normalized plugin-state equality before deleting the recovery manifest.

## Required cleanup gates

Cleanup may proceed only when all are true:

```text
original tree hash == quarantine tree hash == recorded pre-run tree hash
original plugin manifest hash == quarantine plugin manifest hash == recorded pre-run plugin manifest hash
marketplace/plugin/version/path identity unchanged
quarantine exact path is transaction-owned by the run
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
normalized non-candidate plugin state == recorded pre-run normalized plugin state
```

The full config hash must not decide cleanup for the current historical transaction.

## Required final proof

After deleting only the exact equivalent quarantine duplicate:

```text
rehydrated original tree/manifest/identity remain correct
normalized plugin state equals the cleanup-precondition state
quarantine duplicate is absent
recovery manifest is removed only after final proof
```

Any missing or mismatched proof means:

```text
RESTORATION_AMBIGUOUS
```

with no deletion, overwrite, replay, or PASS claim.

## Validation sequence

After implementation creates `REPLAY_INFRASTRUCTURE_COMMIT=<I2>`, rerun in order:

1. deterministic tests;
2. representative single-plugin replay under I2;
3. `web-development + writing-style` multi-plugin replay under I2;
4. only after multi-plugin PASS, exact 059 development replay against:
   `ac501d988f00cb6672fec105ae5fd51a0679cae0`.

The old multi replay remains permanently `FAIL / RESTORATION_AMBIGUOUS`.

## Boundaries

```text
MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO
MODIFY_BRIDGE_OR_HOST=NO
FINAL_GATES_MAY_START=NO
PLUGIN_CREATOR_MUTATION=NO
LIVE_PLUGIN_UPDATE=NO
MAIN_MERGE_RELEASE=NO
```

Even after successful I2 validation:

```text
C2_CANDIDATE_READY=NO
NEXT_HANDOFF=PLANNER
```
