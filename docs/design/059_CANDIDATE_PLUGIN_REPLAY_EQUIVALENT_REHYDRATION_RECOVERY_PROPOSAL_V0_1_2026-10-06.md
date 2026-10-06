# 059 Candidate Plugin Replay 等价再水化恢复 — Planner Proposal v0.1

日期：2026-10-06  
状态：DRAFT_FOR_CRITIC_REVIEW / NOT_IMPLEMENTATION_AUTHORIZATION  
Repository：`YuukiAS/AI_Skills_Collection`  
Branch：`work/research-authoring--formal-production-authoring`  
Triggering task：`research-authoring--formal-production-authoring`

## 0. Authority and current state

Approved shared-isolation design remains：

- `docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_PROPOSAL_V0_2_2026-10-06.md`
- Proposal commit：`f479efb4e2ad31eaafe6ec56b9fc0ba3f284c569`
- Critic PASS：`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_CRITIC_REVIEW_V0_2_2026-10-06.md`
- Critic commit：`307904418e42b704e8bf6e0f1f27aa93c1368a87`

Current shared helper implementation/evidence：

```text
REPLAY_INFRASTRUCTURE_COMMIT=
b61c46957709030bee3735c77d21701871f0480b

EVIDENCE_PACKET_HEAD=
dcf9381eacc6c56f954fc3ca60f3ab8e351d1fb1

REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

DETERMINISTIC_VALIDATION=PASS
SINGLE_PLUGIN_REPLAY=PASS
MULTI_PLUGIN_REPLAY=FAIL
FAILURE_CLASS=RESTORATION_AMBIGUOUS
059_DEVELOPMENT_REPLAY=NOT_STARTED
FINAL_GATES_NOT_STARTED=YES
```

This is not a new Research Authoring product failure. Research Authoring production remains frozen at `ac501d98...`.

## 1. New direct evidence

The approved multi-plugin replay correctly isolated the candidate consumer during the child run.

Tracked child JSONL：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/replays/multi_web_writing_failed_ambiguous/child.stdout.jsonl`

blob SHA：

`c16d967a7cfbbe571bc4a7128bfbb0b5677f1bdd`

Planner re-read the complete tracked JSONL and directly counted path mentions：

```text
web-development candidate path mentions = 4
writing-style candidate path mentions = 2
created-by-me-remote/research-authoring original path mentions = 0
research-authoring quarantine path mentions = 0
```

The existing STATUS and recovery manifest show that during the quarantine window the account-backed `created-by-me-remote/research-authoring/0.3.0` package reappeared at the original cache path, while the transaction-owned quarantined copy still existed outside the discovery root.

Current preserved state：

```text
RA_ORIGINAL_PRESENT
RA_QUARANTINE_PRESENT
```

The current helper then followed its approved v0.2 contract and stopped：

`RESTORATION_AMBIGUOUS`

No overwrite/delete was attempted.

## 2. Failure attribution

```text
ISOLATION=WORKED
ROOT_CAUSE=
RESTORATION_RECONCILIATION_TOO_STRICT_FOR_ACCOUNT_REHYDRATION

MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO
MODIFY_SHARED_REPLAY_RESTORATION=YES
```

The prior design intentionally treated：

```text
original exists
AND quarantine exists
```

as unconditional ambiguity.

Real runtime evidence now shows one additional state that design did not model：

> the account-backed plugin may rehydrate an exact content-equivalent copy back to its original cache path during the replay, without the child consuming either the rehydrated original or the quarantined copy.

Existence alone is therefore not sufficient to classify consumer-isolation failure or unsafe restoration.

The restoration layer needs one new narrow classification：

`VERIFIED_EQUIVALENT_REHYDRATION`

without weakening the existing true-ambiguity fail-closed boundary.

## 3. Two restoration classes

### 3.1 VERIFIED_EQUIVALENT_REHYDRATION

When original and quarantine both exist, the helper may classify the state as verified equivalent rehydration **only if every condition below passes read-only verification**：

```text
original tree hash
=
quarantine tree hash
=
recorded pre-quarantine tree hash

AND

original plugin-manifest hash
=
quarantine plugin-manifest hash
=
recorded pre-quarantine plugin-manifest hash

AND

original exact path
=
recorded expected original path

AND

marketplace/plugin/version identity
=
recorded pre-run identity

AND

current config hash
=
recorded pre-run config hash

AND

normalized non-candidate plugin-state invariants
=
recorded pre-run invariants

AND

CANDIDATE_PATH_READS > 0

AND

ORIGINAL_CONFLICT_PATH_READS = 0

AND

QUARANTINE_PATH_READS = 0
```

The transaction must also prove that the quarantine path is exactly the path owned by the current recovery manifest/run, not an unrelated user directory.

If all conditions pass：

- treat the rehydrated original as the already-restored live cache state;
- keep original untouched;
- delete only the transaction-owned, content-equivalent quarantine duplicate;
- fsync the quarantine parent and relevant ancestor;
- re-read original tree/manifest identity;
- re-check config and normalized plugin-state invariants;
- remove the recovery manifest only after final equality passes.

This is reconciliation of an equivalent duplicate, not acceptance of live-plugin consumption.

### 3.2 TRUE_AMBIGUITY

Any mismatch or missing proof remains：

`RESTORATION_AMBIGUOUS`

including：

- original tree hash differs from quarantine or recorded pre-state;
- plugin manifest hash differs;
- marketplace/plugin/version identity differs;
- original path differs from recorded path;
- config/plugin-state invariant differs materially;
- candidate actual consumption was not proven;
- original conflict path was read;
- quarantine path was read;
- quarantine is not provably transaction-owned;
- required source evidence is missing or unreadable.

TRUE_AMBIGUITY keeps the existing behavior：

- no overwrite;
- no deletion;
- no further replay;
- preserve both sides and recovery evidence;
- return Planner/Critic.

## 4. Replay acceptance semantics amendment

The previous helper currently treats “original path reappeared” itself as a consumer-isolation failure.

v0.1 amendment changes that narrowly.

A rehydrated original **existing on disk** is not by itself a replay FAIL.

The actual consumer-isolation conditions remain：

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
```

Final infrastructure replay PASS additionally requires：

`FINAL_PERSISTENT_STATE_EQUIVALENT_TO_BEFORE=YES`

Therefore replay FAIL remains mandatory if：

- candidate was not actually consumed;
- original conflict path was consumed;
- quarantine path was consumed;
- rehydrated original is not byte/content equivalent to recorded pre-state;
- plugin/config identity is not equivalent to pre-state;
- persistent state cannot be reconciled exactly/equivalently.

Candidate consumption can never excuse conflict consumption.

## 5. Why this does not weaken isolation

The amendment changes only the meaning of **passive reappearance**.

It does not allow the live plugin to participate in the child run.

The child evidence from the failed multi replay already demonstrates the distinction：

- candidate paths were read;
- original conflict path was not read;
- quarantine path was not read;
- restoration stopped only because both copies existed afterward.

So the new logic answers：

> Are two post-run copies actually the same pre-run package, with no live-package consumption?

It does not answer：

> Is it acceptable for the live package to be consumed too?

The latter remains unequivocally NO.

## 6. Current preserved-cache recovery

Until a new execution package receives Critic PASS and explicit user authorization：

- do not delete original;
- do not delete quarantine;
- do not start another candidate replay.

The current stale transaction may be conditionally reconciled later only through the new `VERIFIED_EQUIVALENT_REHYDRATION` path.

For this exact historical transaction, the future recovery must use：

- the existing recovery manifest;
- the preserved child JSONL bound to the failed replay;
- current read-only hashes/identity of original and quarantine at cleanup time.

The tracked child evidence already establishes：

```text
candidate path reads > 0
original conflict path reads = 0
quarantine path reads = 0
```

but **does not by itself authorize cleanup**. Current original/quarantine hashes, manifest identity and persistent-state invariants must still be verified at execution time.

Only if the full equivalent-rehydration condition passes may the next approved execution remove the transaction-owned quarantine duplicate.

Otherwise retain both sides and return `RESTORATION_AMBIGUOUS`.

## 7. Shared helper amendment scope

If Critic approves, the next bounded execution may modify only the existing shared infrastructure：

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
```

plus task-local evidence.

Expected helper semantics to amend：

1. restoration/recovery logic distinguishes equivalent rehydration from true ambiguity;
2. run acceptance no longer fails merely because original path exists;
3. original/quarantine/candidate read evidence remains mandatory;
4. final persistent-state equality is checked after duplicate cleanup;
5. current stale transaction gets a separately authorized conditional cleanup path.

No Research Authoring source/config/generated payload changes.

## 8. Required deterministic amendments

At minimum add/adjust tests for：

1. both original + quarantine, exact tree/manifest/identity match, candidate consumed, zero original/quarantine reads -> `VERIFIED_EQUIVALENT_REHYDRATION`;
2. equivalent state keeps original and deletes only transaction-owned quarantine duplicate;
3. final state equality after duplicate cleanup;
4. original tree mismatch -> `RESTORATION_AMBIGUOUS`;
5. quarantine tree mismatch -> ambiguity;
6. manifest hash mismatch -> ambiguity;
7. identity/version/path mismatch -> ambiguity;
8. config/plugin-state invariant mismatch -> ambiguity;
9. candidate not consumed -> no equivalent-rehydration classification;
10. original read > 0 -> replay FAIL;
11. quarantine read > 0 -> replay FAIL;
12. transaction-ownership mismatch -> no deletion;
13. cleanup fsync/final verification failure -> replay FAIL;
14. stale recovery can reconcile verified equivalent rehydration;
15. current old ambiguous semantics remain fail-closed for non-equivalent cases.

All existing isolation, concurrency, path, timeout, SIGTERM, crash-recovery and no-remote-mutation tests remain green.

## 9. Risk-matched replay after amendment

The current multi replay remains permanently：

```text
FAIL / RESTORATION_AMBIGUOUS
```

Do not retroactively change it.

After a new helper infrastructure commit `I2` is formed：

1. rerun deterministic helper tests;
2. rerun one representative single-plugin replay under `I2`;
3. rerun the approved `web-development + writing-style` multi-plugin replay under `I2`;
4. only after multi replay passes, run exact 059 `ac501d98...` development replay.

The prior single-plugin PASS remains historical evidence for `b61c...`, but it cannot be stitched into `I2` infrastructure PASS without a risk-matched rerun.

No G1-G4 final Gate starts in this recovery.

## 10. Identity separation

Research Authoring remains：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

Old helper identity：

```text
PRIOR_REPLAY_INFRASTRUCTURE_COMMIT=
b61c46957709030bee3735c77d21701871f0480b
```

If this amendment changes helper source：

```text
REPLAY_INFRASTRUCTURE_COMMIT=
<I2>
```

After new replay evidence：

```text
EVIDENCE_PACKET_HEAD=
<E2>
```

`I2` and `E2` are validation-infrastructure/evidence identities, not Research Authoring product commits.

Until the amended infrastructure and exact 059 development replay pass：

`C2_CANDIDATE_READY=NO`

## 11. Authorization boundary for the next execution package

This Proposal does not authorize cleanup or implementation.

A later execution-ready Kickoff must explicitly authorize one new bounded side effect in addition to the already-approved quarantine/restoration scope：

> If and only if the preserved original and transaction-owned quarantine copy satisfy the full `VERIFIED_EQUIVALENT_REHYDRATION` condition, keep the original and delete the transaction-owned quarantine duplicate, fsync, and re-verify persistent state.

That authorization must apply both to：

- the currently preserved ambiguous transaction;
- future equivalent account-rehydration cases.

It must not authorize deleting any non-transaction-owned path or resolving mismatched copies by choosing one.

## 12. Planner decision

```text
ROOT_CAUSE=
RESTORATION_RECONCILIATION_TOO_STRICT_FOR_ACCOUNT_REHYDRATION

ISOLATION=WORKED

ADD_RESTORATION_CLASS=
VERIFIED_EQUIVALENT_REHYDRATION

TRUE_AMBIGUITY_REMAINS_FAIL_CLOSED=YES

MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO

REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

PRIOR_REPLAY_INFRASTRUCTURE_COMMIT=
b61c46957709030bee3735c77d21701871f0480b

NEW_REPLAY_INFRASTRUCTURE_COMMIT=
NOT_CREATED

CURRENT_EVIDENCE_PACKET_HEAD=
dcf9381eacc6c56f954fc3ca60f3ab8e351d1fb1

059_DEVELOPMENT_REPLAY=NOT_STARTED
FINAL_GATES_NOT_STARTED=YES
READY_FOR_AMENDMENT_IMPLEMENTATION=NO
NEXT_HANDOFF=CRITIC
```
