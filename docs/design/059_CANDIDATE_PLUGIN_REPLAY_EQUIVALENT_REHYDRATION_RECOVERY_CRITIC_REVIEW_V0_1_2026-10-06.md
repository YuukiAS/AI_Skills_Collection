# 059 Candidate Plugin Replay 等价再水化恢复 — Critic Review v0.1

日期：2026-10-06  
角色：独立 Critic  
审查阶段：SHARED_REPLAY_INFRASTRUCTURE_EQUIVALENT_REHYDRATION_RECOVERY_REVIEW

## 审查对象

Recovery Proposal：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_PROPOSAL_V0_1_2026-10-06.md`  
commit：`b0b9fc8c50251789fe97f21395637f7060cd7d89`

Plan amendment：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_AMENDMENT_V0_1_2026-10-06.md`  
commit：`3b2d747f07a69f808d092fc2c24daf22a4687780`

## Result

```text
RESULT=PASS

ISOLATION=WORKED

ROOT_CAUSE=
RESTORATION_RECONCILIATION_TOO_STRICT_FOR_ACCOUNT_REHYDRATION

VERIFIED_EQUIVALENT_REHYDRATION=APPROVED

TRUE_AMBIGUITY_REMAINS_FAIL_CLOSED=YES

PASSIVE_ORIGINAL_REAPPEARANCE_ALONE_IS_NOT_ISOLATION_FAIL=YES

CANDIDATE_PATH_READS_GT_0=REQUIRED
ORIGINAL_CONFLICT_PATH_READS_0=REQUIRED
QUARANTINE_PATH_READS_0=REQUIRED
FINAL_PERSISTENT_STATE_EQUIVALENT_TO_BEFORE=REQUIRED

MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO

REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

PRIOR_REPLAY_INFRASTRUCTURE_COMMIT=
b61c46957709030bee3735c77d21701871f0480b

NEW_REPLAY_INFRASTRUCTURE_COMMIT=
NOT_CREATED

CURRENT_EVIDENCE_PACKET_HEAD=
dcf9381eacc6c56f954fc3ca60f3ab8e351d1fb1

FINAL_GATES_MAY_START=NO
```

This PASS approves only the equivalent-rehydration recovery design and Plan amendment. It does not authorize helper implementation, current quarantine cleanup, new candidate replay, Research Authoring modification, final Gates, paid API, merge, or release.

## Direct evidence

The failed multi-plugin replay remains permanently `FAIL / RESTORATION_AMBIGUOUS`.

Independent re-read of the tracked child JSONL confirms command-execution reads:

```text
web-development candidate path reads = 4
writing-style candidate path reads = 2
created-by-me-remote/research-authoring original path reads = 0
research-authoring quarantine path reads = 0
```

Therefore the isolation mechanism itself worked during the child run. The failure happened later in restoration, when the account-backed Research Authoring cache package reappeared at the original path while the transaction-owned quarantine copy still existed.

The current recovery manifest records the original Research Authoring package identity, original path, quarantine path, pre-run tree hash, plugin-manifest hash, Skill overlap set, marketplace/plugin/version identity, config hash and before-plugin-list snapshot. This is enough to support the proposed read-only equivalence proof at execution time.

## Attribution ruling

The new attribution is accepted:

`RESTORATION_RECONCILIATION_TOO_STRICT_FOR_ACCOUNT_REHYDRATION`

The evidence does not justify reopening the previously approved isolation architecture.

A path reappearing on disk is not the same event as a child consuming that path. The old helper intentionally collapsed those two states into one fail-closed outcome. The amendment correctly separates:

- consumer isolation;
- post-run persistent-state reconciliation.

## VERIFIED_EQUIVALENT_REHYDRATION

The new restoration class is sufficiently strict.

It requires all of the following before any duplicate cleanup:

- original tree hash == quarantine tree hash == recorded pre-run tree hash;
- original plugin-manifest hash == quarantine plugin-manifest hash == recorded pre-run hash;
- exact original path == recorded original path;
- marketplace/plugin/version identity == recorded pre-run identity;
- current config hash == recorded pre-run config hash;
- normalized non-candidate plugin-state invariants == recorded pre-run invariants;
- candidate actual consumption proven;
- original conflict path reads == 0;
- quarantine path reads == 0;
- quarantine path is exactly transaction-owned by the current recovery manifest/run.

This is enough to establish that the rehydrated original is content/identity-equivalent to the pre-run live cache package and that neither live copy participated in the child run.

The existing `tree_sha256()` also includes directory/file relative paths, file bytes, and symlink targets, so the proposed tree equality is materially stronger than a shallow file-count check.

## Equivalent cleanup

For verified equivalent rehydration, the cleanup rule is the minimum safe reconciliation:

1. keep the rehydrated original untouched;
2. delete only the exact transaction-owned quarantine duplicate;
3. fsync relevant parent directories;
4. re-read/re-hash the original;
5. re-check config and normalized plugin state;
6. delete the recovery manifest only after final persistent-state equality passes.

No “choose the better copy” behavior is introduced.

If any proof is missing or mismatched, `RESTORATION_AMBIGUOUS` remains unchanged: no overwrite, no deletion, no new replay.

## Replay acceptance

The amended acceptance semantics are correct:

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
FINAL_PERSISTENT_STATE_EQUIVALENT_TO_BEFORE = YES
```

Passive original-path reappearance alone is no longer an isolation failure.

Actual original/quarantine consumption remains a hard failure, and candidate consumption can never mask it.

## Current preserved transaction

The current dual-copy Research Authoring cache state must remain untouched until a new execution-ready package and explicit user authorization exist.

The tracked child evidence proves only the read/consumption side. Stage 0 must still re-check the current original/quarantine tree hashes, manifest hashes, identity/path, transaction ownership, config hash and normalized plugin state before any cleanup.

Only a complete `VERIFIED_EQUIVALENT_REHYDRATION` proof may authorize deletion of the transaction-owned quarantine duplicate.

## Durable evidence

Persisting the post-child evidence before duplicate cleanup is justified and necessary because the cleanup decision is destructive to the transaction-owned quarantine copy.

This is still a bounded crash-recovery journal, not a new workflow state machine. It stores only the evidence needed to decide whether duplicate cleanup is safe after interruption.

## Tests and replay sequence

The proposed amendment tests are risk-matched.

After helper source changes form `I2`, the following sequence is required:

1. deterministic helper tests;
2. representative single-plugin replay under `I2`;
3. `web-development + writing-style` multi-plugin replay under `I2`;
4. only after multi-plugin PASS, exact 059 `ac501d98...` development replay.

The old multi replay remains permanently FAIL, and the old single-plugin PASS under `b61c...` cannot be stitched into the new infrastructure candidate's final PASS.

No additional historical replay sweep is required.

## Identity separation

The amendment preserves the existing identity split:

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

PRIOR_REPLAY_INFRASTRUCTURE_COMMIT=
b61c46957709030bee3735c77d21701871f0480b

NEW_REPLAY_INFRASTRUCTURE_COMMIT=
<I2>

EVIDENCE_PACKET_HEAD=
<E2>
```

The helper amendment does not change Research Authoring product identity.

Until `I2` validation and the exact 059 development replay both pass:

`C2_CANDIDATE_READY=NO`

## External implementation sanity check

Python's documented `os.replace` semantics support the previously approved same-filesystem atomic-rename premise: successful replacement/rename is atomic, while cross-filesystem movement may fail. The amendment does not weaken that already-approved quarantine mechanism; it changes only post-run duplicate reconciliation.

## Approved bindings

```text
APPROVED_RECOVERY_PROPOSAL_PATH=
docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_PROPOSAL_V0_1_2026-10-06.md

APPROVED_RECOVERY_PROPOSAL_COMMIT=
b0b9fc8c50251789fe97f21395637f7060cd7d89

APPROVED_PLAN_AMENDMENT_PATH=
docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_AMENDMENT_V0_1_2026-10-06.md

APPROVED_PLAN_AMENDMENT_COMMIT=
3b2d747f07a69f808d092fc2c24daf22a4687780
```

## Authorization boundary

```text
HELPER_IMPLEMENTATION_AUTHORIZED=NO
CURRENT_QUARANTINE_CLEANUP_AUTHORIZED=NO
NEW_CANDIDATE_REPLAY_AUTHORIZED=NO
MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO
FINAL_GATES_MAY_START=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```

The next owner is Planner. Planner should prepare a small amended execution package whose Kickoff explicitly authorizes conditional deletion of the current/future transaction-owned quarantine duplicate only after full `VERIFIED_EQUIVALENT_REHYDRATION` proof.
