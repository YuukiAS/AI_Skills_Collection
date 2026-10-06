# 059 Candidate Plugin Replay 等价再水化恢复 — Canonical Goal Amendment v0.1

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
日期：2026-10-06  
Repository：`YuukiAS/AI_Skills_Collection`  
Task key：`research-authoring--formal-production-authoring`

## 0. Binding

Base Goal：

`docs/goals/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_GOAL_V0_1.md`

Approved recovery Proposal：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_PROPOSAL_V0_1_2026-10-06.md`  
commit：`b0b9fc8c50251789fe97f21395637f7060cd7d89`

Approved Plan amendment：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_AMENDMENT_V0_1_2026-10-06.md`  
commit：`3b2d747f07a69f808d092fc2c24daf22a4687780`

Critic PASS：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_CRITIC_REVIEW_V0_1_2026-10-06.md`  
commit：`7a3dd5b19db779d17d224cec1dd8cba0a4a9f182`

Current identities：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

PRIOR_REPLAY_INFRASTRUCTURE_COMMIT=
b61c46957709030bee3735c77d21701871f0480b

CURRENT_EVIDENCE_PACKET_HEAD=
dcf9381eacc6c56f954fc3ca60f3ab8e351d1fb1
```

This amendment changes only equivalent-rehydration restoration semantics. All unchanged clauses of the base Goal remain in force.

## 1. Amended goal

Extend the existing shared `candidate_plugin_replay` helper so that:

- consumer isolation remains strict;
- passive account-backed rehydration of an identical live cache package is not mistaken for consumer participation;
- a transaction-owned duplicate quarantine may be deleted only after complete, read-only equivalence proof;
- true ambiguity remains fail closed.

No Research Authoring production change is allowed.

## 2. Stage 0 — current preserved transaction must be handled first

Before any helper source amendment validation replay, first address the currently preserved dual-copy transaction:

```text
run_id=
20261006T071703Z-3410223

manifest=
results/research-authoring--formal-production-authoring/
g4_c1_c2_replay_infrastructure_recovery/
replays/multi_web_writing_failed_ambiguous/recovery-manifest.json

child evidence=
results/research-authoring--formal-production-authoring/
g4_c1_c2_replay_infrastructure_recovery/
replays/multi_web_writing_failed_ambiguous/child.stdout.jsonl
```

Current historical replay result remains permanently:

`FAIL / RESTORATION_AMBIGUOUS`

Stage 0 may perform only read-only equivalence checks until all requirements below pass.

If Stage 0 does not prove `VERIFIED_EQUIVALENT_REHYDRATION`, stop immediately. Do not delete either side and do not start any new candidate replay.

## 3. VERIFIED_EQUIVALENT_REHYDRATION contract

Classification is allowed only when all are true:

```text
original tree hash
=
quarantine tree hash
=
recorded pre-run tree hash

AND

original plugin manifest hash
=
quarantine plugin manifest hash
=
recorded pre-run plugin manifest hash

AND

marketplace/plugin/version identity unchanged

AND

original exact path == recorded expected original path

AND

quarantine exact path is transaction-owned by this run

AND

config hash == recorded pre-run config hash

AND

normalized non-candidate plugin-state invariants
== recorded pre-run invariants

AND

CANDIDATE_PATH_READS > 0

AND

ORIGINAL_CONFLICT_PATH_READS = 0

AND

QUARANTINE_PATH_READS = 0
```

Any missing or mismatched proof means:

`RESTORATION_AMBIGUOUS`

with no deletion, overwrite, or new replay.

## 4. Conditional cleanup contract

Only for `VERIFIED_EQUIVALENT_REHYDRATION`:

1. keep the rehydrated original untouched;
2. delete only the exact transaction-owned quarantine duplicate;
3. fsync the quarantine parent and relevant parent directory;
4. re-read/re-hash the original package;
5. re-check plugin manifest identity;
6. re-check config hash and normalized non-candidate plugin state;
7. require:
   `FINAL_PERSISTENT_STATE_EQUIVALENT_TO_BEFORE=YES`;
8. only then remove the recovery manifest.

If cleanup, fsync, re-read, or final equality fails, infrastructure result is FAIL and evidence is preserved.

## 5. Replay acceptance amendment

Original path existence alone is not an isolation failure.

Replay PASS still requires:

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
FINAL_PERSISTENT_STATE_EQUIVALENT_TO_BEFORE=YES
```

Hard FAIL remains:

- candidate not consumed;
- original conflict path consumed;
- quarantine path consumed;
- rehydrated original not equivalent to pre-state;
- persistent state cannot be reconciled.

Candidate consumption never masks conflict consumption.

## 6. Allowed implementation scope

Exactly:

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
```

Evidence only under:

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/**`

No Research Authoring product file may change.

## 7. Durable post-child evidence

Before any duplicate deletion decision, persist enough evidence to survive interruption:

- child stdout/stderr identity/hash;
- candidate installed path(s);
- candidate read events/count;
- original conflict read events/count;
- quarantine read events/count;
- post-child original presence;
- recovery-manifest identity.

Cleanup must never rely only on in-memory state.

## 8. Required deterministic validation

In addition to the existing isolation suite, cover at least:

- exact equivalent dual-copy classification;
- keep original unchanged;
- delete only transaction-owned duplicate;
- final persistent-state equality;
- original/quarantine tree mismatch;
- plugin manifest mismatch;
- marketplace/plugin/version/path mismatch;
- config mismatch;
- normalized plugin-state mismatch;
- candidate missing;
- original read;
- quarantine read;
- unowned quarantine path;
- cleanup/fsync/final verification failure;
- stale recovery with equivalent dual copies;
- stale recovery with non-equivalent dual copies;
- unchanged single-copy stale recovery.

All previous isolation/quarantine/concurrency/timeout/SIGTERM/path-safety/no-remote-mutation tests remain required.

## 9. I2 validation sequence

Any helper source change creates:

```text
REPLAY_INFRASTRUCTURE_COMMIT=<I2>
```

Then run, in order:

1. deterministic tests;
2. representative single-plugin replay under I2;
3. `web-development + writing-style` multi-plugin replay under I2;
4. only after multi-plugin PASS, exact 059 development replay against:
   `ac501d988f00cb6672fec105ae5fd51a0679cae0`.

The old multi replay remains FAIL.
The old single-plugin PASS under `b61c...` is historical evidence only and cannot be stitched into I2 PASS.

## 10. Identity boundary

Research Authoring remains:

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

Helper amendment:

```text
REPLAY_INFRASTRUCTURE_COMMIT=<I2>
```

New evidence:

```text
EVIDENCE_PACKET_HEAD=<E2>
```

Until I2 validation and exact 059 development replay both pass:

`C2_CANDIDATE_READY=NO`

Executor must not promote C2.

## 11. Authorization ceiling

A future approved Kickoff may authorize:

- Stage 0 read-only equivalence verification;
- conditional deletion of only the exact transaction-owned quarantine duplicate when the full verified-equivalent contract passes;
- keeping the rehydrated original unchanged;
- fsync + final persistent-state verification;
- the three existing helper source/test/docs files;
- deterministic tests;
- single/multi/059 development replays;
- helper-only/evidence commits;
- ordinary non-force push exact task branch.

It does not authorize:

- deletion when any proof is missing;
- deleting/modifying the rehydrated original;
- Plugin Creator or remote Plugin mutation;
- permanent uninstall;
- Research Authoring production modification;
- final G1-G4;
- G4 ChatGPT;
- PDF production;
- paid API;
- Bridge/Host changes;
- main/release;
- destructive Git;
- automation.

## 12. Positive terminal condition

Only:

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

This does not mean Research Authoring 0.3 is complete.
