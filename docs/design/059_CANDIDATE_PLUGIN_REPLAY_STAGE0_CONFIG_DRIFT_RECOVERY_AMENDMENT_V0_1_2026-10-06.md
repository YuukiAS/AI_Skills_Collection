# 059 Candidate Plugin Replay Stage 0 config drift recovery amendment v0.1

日期：2026-10-06  
状态：DRAFT_FOR_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
Repository：`YuukiAS/AI_Skills_Collection`  
Task：`research-authoring--formal-production-authoring`

## Binding

Critic review：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_STAGE0_CONFIG_DRIFT_CRITIC_REVIEW_V0_1_2026-10-06.md`

Critic commit：

`1a39dd916eebdc45ecd4f73b84833fe736c52cb4`

Current identities：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

CURRENT_REPLAY_INFRASTRUCTURE_HEAD=
3ec2714e5f7ea386833ee54c365e923235603819

STAGE0_EVIDENCE_COMMIT=
a76d7c36d45e52eaf6b771fd604b691c7b67244c
```

This amendment changes only the equivalent-rehydration cleanup invariant for the preserved Stage 0 transaction and future transactions using the same restoration contract.

No Research Authoring production file, Bridge/Host policy, live Plugin, final Gate, or release path is in scope.

## Finding

Stage 0 proved every package/cache/consumer invariant required for equivalent rehydration except the full `$CODEX_HOME/config.toml` file hash:

```text
PACKAGE_EQUIVALENCE=PROVEN
NORMALIZED_PLUGIN_STATE_EQUIVALENT=YES
CANDIDATE_ACTUAL_CONSUMPTION=YES
ORIGINAL_CONFLICT_PATH_READS=0
QUARANTINE_PATH_READS=0
ONLY_BLOCKER=FULL_CONFIG_FILE_HASH_DRIFT
```

The full config hash is too broad for this recovery decision. The helper neither owns nor restores the entire user config file, and the historical transaction did not snapshot config contents or a plugin-relevant projection. The drift remains useful diagnostic provenance, but it must not by itself block deletion of a transaction-owned duplicate quarantine package when all real plugin/cache invariants are proven.

## Amended cleanup gate

`VERIFIED_EQUIVALENT_REHYDRATION` cleanup no longer requires:

```text
current full config.toml hash == recorded pre-run full config.toml hash
```

The helper must still record both hashes as diagnostic/provenance evidence.

Cleanup remains allowed only when all hard gates below pass:

```text
original tree hash == quarantine tree hash == recorded pre-run tree hash
original plugin manifest hash == quarantine plugin manifest hash == recorded pre-run manifest hash
marketplace/plugin/version/path identity unchanged
quarantine path is owned by the current transaction/run
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
normalized non-candidate plugin state == recorded pre-run normalized state
```

Candidate consumption can never mask conflict consumption.

## Final verification

After deleting only the exact transaction-owned quarantine duplicate, the helper must prove:

```text
rehydrated original tree hash == recorded pre-run tree hash
rehydrated original plugin manifest hash == recorded pre-run manifest hash
rehydrated original marketplace/plugin/version/path identity is unchanged
normalized non-candidate plugin state equals the cleanup-precondition state
quarantine duplicate no longer exists
```

The recovery manifest may be removed only after final verification passes.

If any hard gate or final verification is missing, unreadable, or mismatched:

```text
RESTORATION_AMBIGUOUS
```

and the helper must not delete either side, overwrite either side, start replay, or claim PASS.

## Future config handling

If future evidence shows a real plugin-relevant config invariant is required, a new transaction must snapshot an explicit minimal plugin-relevant config projection before mutation.

Do not use the full `config.toml` file hash as a substitute for such a projection.

For the current historical transaction, no config content snapshot exists. Do not infer or reconstruct a config diff after the fact.

## Replay identity

The old multi-plugin replay remains permanently:

```text
FAIL / RESTORATION_AMBIGUOUS
```

After this amendment is implemented, create a new helper candidate:

```text
REPLAY_INFRASTRUCTURE_COMMIT=<I2>
```

Then rerun:

1. deterministic tests;
2. representative single-plugin replay;
3. `web-development + writing-style` multi-plugin replay;
4. only after multi-plugin PASS, exact 059 development replay against `ac501d988f00cb6672fec105ae5fd51a0679cae0`.

Even if all replay evidence passes:

```text
C2_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```
