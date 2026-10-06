# 059 Candidate Plugin Replay 共享隔离恢复 — Implementation Plan Amendment v0.1

日期：2026-10-06  
状态：DRAFT_FOR_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
Repository：`YuukiAS/AI_Skills_Collection`  
Branch：`work/research-authoring--formal-production-authoring`

## 0. Binding

Base approved Implementation Plan：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md`

Base Plan commit：

`8dbe6b4ee0d359436b231d21632963b4b40346f1`

New recovery Proposal：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_PROPOSAL_V0_1_2026-10-06.md`

Proposal commit：

`b0b9fc8c50251789fe97f21395637f7060cd7d89`

Current infrastructure/evidence：

```text
PRIOR_REPLAY_INFRASTRUCTURE_COMMIT=
b61c46957709030bee3735c77d21701871f0480b

CURRENT_EVIDENCE_PACKET_HEAD=
dcf9381eacc6c56f954fc3ca60f3ab8e351d1fb1

REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

This amendment changes only restoration reconciliation and replay acceptance around verified account-backed rehydration. All other approved Plan v0.1 mechanisms remain in force.

## 1. Superseded clauses

The following Base Plan semantics are amended：

1. “original conflict path reappears” is no longer by itself a consumer-isolation FAIL;
2. “original and quarantine both exist” is no longer unconditionally `RESTORATION_AMBIGUOUS`;
3. restoration may delete a quarantine duplicate only after full `VERIFIED_EQUIVALENT_REHYDRATION` proof;
4. final replay success now explicitly requires persistent-state equivalence after rehydration reconciliation.

No other architecture/routing/identity/authorization clause is relaxed.

## 2. Implementation scope

Allowed source remains exactly：

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
```

Evidence remains under：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/**`

No Research Authoring production change.

## 3. New restoration classification

Implement two explicit outcomes when both original and quarantine exist：

### A. VERIFIED_EQUIVALENT_REHYDRATION

Allowed only when all read-only checks pass：

- original exact path equals recovery-manifest original path;
- quarantine exact path equals recovery-manifest quarantine path;
- quarantine is provably owned by this transaction/run;
- original tree hash == quarantine tree hash == recorded pre-run tree hash;
- original plugin manifest hash == quarantine plugin manifest hash == recorded pre-run manifest hash;
- original parsed marketplace/plugin/version == recorded identity;
- quarantine path identity corresponds exactly to the recorded marketplace/plugin/version;
- current config hash == recorded pre-run config hash;
- normalized non-candidate plugin state satisfies the recorded pre-run invariants;
- candidate actual consumption is proven;
- original conflict path reads == 0;
- quarantine path reads == 0.

### B. RESTORATION_AMBIGUOUS

Any missing/mismatched proof keeps the existing fail-closed behavior.

No “best copy” selection is permitted.

## 4. Equivalent-rehydration cleanup

For `VERIFIED_EQUIVALENT_REHYDRATION` only：

1. do not modify the rehydrated original;
2. re-check quarantine is inside the exact transaction-owned quarantine parent;
3. delete only the exact quarantine package duplicate recorded by the manifest;
4. do not delete the original;
5. fsync quarantine parent and relevant parent directories;
6. re-hash/re-read original package;
7. re-run normalized non-candidate plugin-state/config verification;
8. only after all final checks pass, mark restoration complete and remove the recovery manifest.

If cleanup/final verification fails：

- replay remains FAIL;
- preserve remaining evidence;
- do not invent an alternative recovery;
- return Planner/Critic.

## 5. Current preserved ambiguous transaction — Stage 0 recovery

Before any new candidate replay, the future amended execution must first address the currently preserved transaction：

Run id：

`20261006T071703Z-3410223`

Tracked recovery manifest：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/replays/multi_web_writing_failed_ambiguous/recovery-manifest.json`

Tracked child stdout：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/replays/multi_web_writing_failed_ambiguous/child.stdout.jsonl`

Tracked child stdout blob SHA：

`c16d967a7cfbbe571bc4a7128bfbb0b5677f1bdd`

Planner directly verified from the complete tracked JSONL：

```text
web-development candidate path mentions > 0
writing-style candidate path mentions > 0
research-authoring original conflict path mentions = 0
research-authoring quarantine path mentions = 0
```

This child evidence satisfies only the read/consumption side of the conditional recovery.

At execution time Stage 0 must still read-only verify current local：

- original tree hash;
- quarantine tree hash;
- both manifest hashes;
- original identity/path;
- quarantine transaction ownership;
- config hash;
- normalized plugin-state invariants.

Only if all equivalent-rehydration conditions pass may Stage 0 keep original and delete the transaction-owned quarantine duplicate.

If any condition fails：

`RESTORATION_AMBIGUOUS`

and the amended execution stops before changing helper source or launching replay unless Critic-approved execution sequencing explicitly allows source edit before unresolved cleanup. Preferred order is to restore the user's state first.

No new replay may start while both sides remain unresolved.

## 6. Replay acceptance logic

After amendment, child execution evaluation must separate：

### Consumer isolation

FAIL if：

- candidate actual consumption is absent;
- original conflict path read count > 0;
- quarantine read count > 0.

### Passive rehydration

Original path existence alone does not fail isolation.

If original reappears without conflict reads, restoration classifies the post-run state：

- verified identical -> reconcile;
- not proven identical -> ambiguity.

### Final replay PASS

Requires all：

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
FINAL_PERSISTENT_STATE_EQUIVALENT_TO_BEFORE=YES
```

No candidate/conflict mixed consumption is accepted.

## 7. Durable evidence amendment

Before restoration reconciliation, durable evidence must bind：

- child stdout/stderr identity/hash;
- candidate installed paths;
- candidate read events/count;
- original conflict read events/count;
- quarantine read events/count;
- post-child original-presence observation;
- recovery manifest identity.

For future runs, write sufficient post-child evidence before mutating/deleting a duplicate so a crash during reconciliation can still distinguish：

- candidate consumed/no conflict read;
- unknown/incomplete evidence.

Do not rely only on in-memory variables for a cleanup decision that deletes the transaction-owned quarantine duplicate.

## 8. Deterministic amendment tests

Add/modify focused tests covering：

1. equivalent rehydration classification with exact hashes/identity and valid read proof;
2. equivalent cleanup keeps original unchanged;
3. equivalent cleanup removes only transaction-owned quarantine duplicate;
4. final persistent-state equality;
5. original content mismatch -> ambiguity;
6. quarantine content mismatch -> ambiguity;
7. plugin manifest mismatch -> ambiguity;
8. marketplace/plugin/version mismatch -> ambiguity;
9. expected-original-path mismatch -> ambiguity;
10. config mismatch -> ambiguity;
11. normalized plugin-state invariant mismatch -> ambiguity;
12. missing candidate consumption -> no reconciliation;
13. original conflict read -> replay FAIL;
14. quarantine read -> replay FAIL;
15. unowned quarantine path -> no delete;
16. cleanup failure -> replay FAIL;
17. final verification failure -> replay FAIL;
18. stale recovery with verified equivalent rehydration;
19. stale recovery with non-equivalent dual copies remains ambiguous;
20. existing single-copy stale restore behavior remains unchanged.

All pre-existing isolation, quarantine-location, same-`st_dev`, concurrency, timeout, exception, SIGTERM, path safety and remote-state tests remain required.

## 9. Infrastructure candidate I2

Any helper source change after：

`b61c46957709030bee3735c77d21701871f0480b`

creates a new shared-infrastructure candidate：

```text
REPLAY_INFRASTRUCTURE_COMMIT=<I2>
```

Do not amend or relabel `b61c...` as PASS.

The old multi replay remains：

`FAIL / RESTORATION_AMBIGUOUS`

permanently.

## 10. Required validation after I2

After Stage 0 cleanup is safely resolved and I2 is formed：

1. deterministic helper tests;
2. representative single-plugin replay under I2;
3. approved `web-development + writing-style` multi-plugin replay under I2;
4. only after multi-plugin PASS, exact 059 development replay using：
   `REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0`.

The old single-plugin PASS under `b61c...` remains historical evidence only.

059 exact replay remains development regression, not final Gate evidence.

No prompt blacklist may be added.

## 11. Evidence identity

After I2 validation：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

REPLAY_INFRASTRUCTURE_COMMIT=
<I2>

EVIDENCE_PACKET_HEAD=
<E2>
```

Research Authoring product identity remains unchanged.

Only if：

- deterministic tests PASS;
- single-plugin I2 replay PASS;
- multi-plugin I2 replay PASS;
- exact 059 replay PASS;
- state restoration/equivalence PASS;

may Planner later promote the unchanged product commit to C2 identity.

Executor must not do that promotion.

## 12. User authorization required in the next execution package

This amendment itself authorizes no mutation.

The next Kickoff must explicitly request/contain bounded user authorization for：

1. the previously approved temporary cache quarantine/restoration behavior;
2. **conditional deletion of the current/future transaction-owned quarantine duplicate only under `VERIFIED_EQUIVALENT_REHYDRATION`;**
3. retaining the rehydrated original untouched;
4. fsync + final state verification;
5. no deletion if any proof is missing/mismatched.

This is a user-level local cache deletion, even though it deletes only a transaction-created duplicate; it must not be inferred from the prior Proposal PASS.

## 13. Failure semantics

- current dual-copy state not equivalent -> `RESTORATION_AMBIGUOUS`, no deletion/replay;
- equivalent proof passes but duplicate cleanup fails -> infrastructure FAIL, preserve evidence;
- candidate missing -> replay FAIL;
- original/quarantine conflict read -> replay FAIL;
- post-cleanup state mismatch -> infrastructure FAIL;
- I2 implementation requires Research Authoring/Bridge/Host changes -> stop Planner/Critic;
- final Gates remain prohibited.

## 14. Stop state after amended implementation

If the future amended execution succeeds：

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

This amendment does not authorize implementation, cleanup, replay, final Gates, Plugin mutation, paid API, merge or release.
