# 059 Candidate Plugin Replay 共享隔离恢复 — Critic Review v0.2

日期：2026-10-06  
角色：独立 Critic  
审查阶段：SHARED_REPLAY_INFRASTRUCTURE_RECOVERY_ARCHITECTURE_REVIEW  
Proposal：
`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_PROPOSAL_V0_2_2026-10-06.md`  
Proposal commit：
`f479efb4e2ad31eaafe6ec56b9fc0ba3f284c569`

## 结论

```text
RESULT=PASS

ROOT_CAUSE=
SHARED_CANDIDATE_REPLAY_CONSUMER_ISOLATION_GAP

APPROVED_ROUTE=
B_TEMPORARY_LOCAL_CACHE_SUPPRESSION_WITH_EXACT_RESTORE

CPR1=CLOSED

QUARANTINE_OUTSIDE_PLUGIN_DISCOVERY_ROOT=REQUIRED
SAME_FILESYSTEM_ST_DEV_GATE=REQUIRED

CANDIDATE_PATH_READS_GT_0=REQUIRED
ORIGINAL_CONFLICT_PATH_READS_0=REQUIRED
QUARANTINE_PATH_READS_0=REQUIRED

CONCURRENT_SHARED_CODEX_HOME_PREFLIGHT=REQUIRED

MODIFY_SHARED_CANDIDATE_PLUGIN_REPLAY=YES
MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO

REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

REPLAY_INFRASTRUCTURE_COMMIT=
NOT_CREATED

FINAL_GATES_MAY_START=
NO
```

This PASS approves the v0.2 recovery design only. It does not authorize helper implementation, cache suppression, live Plugin mutation, final Gates, paid API, merge, or release.

## CPR1 closure

The prior blocker was that v0.1 placed the quarantine inside `$CODEX_HOME/plugins/cache/**`, the same discovery/cache tree from which the current runtime had already consumed a supposedly disabled live wrapper.

v0.2 closes that failure path.

It now requires the quarantine root to be outside the plugin discovery/cache root, forbids a hidden cache-subdirectory fallback, and requires the original package and quarantine parent to share `st_dev` before any atomic rename.

If a safe out-of-discovery same-filesystem location cannot be established, the route fails closed as `SAFE_QUARANTINE_UNAVAILABLE`; it does not downgrade to copy/delete, cross-filesystem movement, CLI uninstall/reinstall, or prompt manipulation.

That directly satisfies CPR1's minimum closure.

## Recovery manifest and atomic restoration

The proposed recovery manifest now records enough information to recover after interruption:

- resolved discovery root;
- resolved quarantine parent;
- exact original/quarantine paths;
- original and quarantine-parent `st_dev`;
- package tree hash and plugin-manifest hash;
- overlapping top-level Skill identities;
- marketplace/plugin/version identity;
- config hash;
- candidate installed identity.

The transaction order is also correct:

```text
validate discovery/quarantine roots
-> same-filesystem check
-> durable manifest + fsync
-> atomic rename out of discovery tree
-> child
-> consumption evidence
-> exact restore
-> hash/state verification
-> candidate cleanup
-> final equality
```

Normal child failure, timeout, ordinary exception, SIGINT and catchable SIGTERM must restore before returning failure. SIGKILL/power-loss recovery remains entry-time, fail-closed recovery from the durable manifest. Ambiguous state never overwrites or deletes either side.

This is a bounded crash-recovery journal, not a new daemon, database, watcher, or long-lived state machine.

## Consumer-isolation evidence

v0.2 also closes the false-PASS route identified in the prior review.

A replay may pass only when all three conditions are true:

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
```

If the account-backed Plugin rehydrates at the original path, if that original path is read, or if the quarantined package is read from its new path, the replay fails even if the candidate is also consumed.

This is the right fail-closed behavior for the current evidence model.

## Shared-CODEX_HOME concurrency

The v0.2 concurrency boundary is sufficient at architecture level.

The helper lock only serializes helper invocations; it cannot protect unrelated local Codex processes sharing the same user-level plugin cache. v0.2 now requires a minimal preflight and fail-closed behavior when an obvious concurrent consumer of the same CODEX_HOME exists.

The later execution package must make that preflight concrete enough to implement and test, but there is no need for a global lock service, daemon, process controller, or watcher.

## Tests

The proposed deterministic coverage is risk-matched and sufficient:

- out-of-discovery quarantine;
- same-filesystem gate and cross-filesystem failure;
- no cache-hidden fallback;
- symlink safety;
- candidate/original/quarantine three-way read checks;
- rehydration failure;
- concurrency preflight;
- no-conflict behavior;
- success/failure/timeout/exception restoration;
- stale and ambiguous recovery;
- no remote-object mutation.

Representative runtime coverage remains appropriately bounded to:

1. one existing single-plugin candidate replay;
2. one existing multi-plugin replay;
3. the exact 059 `ac501d98...` blocking replay.

No broad historical replay sweep is required.

## Identity separation

The v0.2 proposal preserves the required three-layer identity:

```text
REPAIRED_PRODUCT_COMMIT =
ac501d988f00cb6672fec105ae5fd51a0679cae0

REPLAY_INFRASTRUCTURE_COMMIT =
<future helper-only commit>

EVIDENCE_PACKET_HEAD =
<future evidence head>
```

The shared replay-helper repair does not become part of the Research Authoring product candidate.

Until the helper implementation passes and the 059 development replay is validly executed, `ac501d98...` remains only `REPAIRED_PRODUCT_COMMIT`, not ready C2.

## Scope and next stage

The approved design allows a later execution package to modify only:

- `scripts/candidate_plugin_replay.py`;
- `tests/test_candidate_plugin_replay.py`;
- `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md`;
- task-local recovery evidence.

It does not authorize changes to Research Authoring production, live Plugin state, Bridge Kit, Host Policy, profiles, Marketplace product payload, versions, README, main, or release.

The next owner is Planner. Planner may now prepare a same-version bounded infrastructure Implementation Plan, Canonical Goal, and Kickoff Draft. The Kickoff must explicitly request user authorization for the short-lived local cache quarantine + exact restoration side effect before any suppression is executed.
