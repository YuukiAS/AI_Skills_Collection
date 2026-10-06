# 059 Candidate Plugin Replay 共享隔离恢复 — Canonical Goal v0.1

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
日期：2026-10-06  
Repository：`YuukiAS/AI_Skills_Collection`  
Task key：`research-authoring--formal-production-authoring`

## Authority

Approved Proposal：

- `docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_PROPOSAL_V0_2_2026-10-06.md`
- commit：`f479efb4e2ad31eaafe6ec56b9fc0ba3f284c569`

Critic PASS：

- `docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_CRITIC_REVIEW_V0_2_2026-10-06.md`
- commit：`307904418e42b704e8bf6e0f1f27aa93c1368a87`

Implementation Plan：

- `docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md`
- commit：`8dbe6b4ee0d359436b231d21632963b4b40346f1`

本 Goal 只修 shared candidate replay infrastructure，不修改 Research Authoring production。

## 1. Goal

使现有：

`scripts/candidate_plugin_replay.py`

在 candidate 与已安装 live Plugin 暴露相同顶层 Skill identity 时，能够：

```text
detect conflict
-> safely suppress only conflicting local cache package
-> run exact candidate replay
-> prove candidate-only consumption
-> exactly restore user plugin-cache state
```

而不是继续让 live Plugin 抢 candidate。

不得创建第二套 replay framework。

## 2. Product identity boundary

Research Authoring：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

本 Goal不得修改该 product tree。

Shared infrastructure later forms：

```text
REPLAY_INFRASTRUCTURE_COMMIT=<helper-only commit>
EVIDENCE_PACKET_HEAD=<evidence-only/latest packet head>
```

helper commit不得被称为 Research Authoring C2。

在 exact 059 development replay有效 PASS 前：

`C2_CANDIDATE_READY=NO`

## 3. Allowed source

Only：

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
```

Evidence only：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/**`

禁止修改 Research Authoring、Bridge、Host Policy、profiles、Marketplace production payload、versions、README、main/release。

## 4. Conflict contract

Conflict signal：

exact top-level Skill frontmatter `name` overlap.

Candidate and live cached packages must be inspected generically; do not hard-code plugin names.

Candidate-candidate ambiguous duplicate Skill identity -> fail closed.

Do not add semantic similarity/LLM conflict detection.

## 5. Quarantine contract

Quarantine must：

- resolve outside plugin discovery/cache root;
- remain on same filesystem as original package;
- satisfy：
  `original.st_dev == quarantine_parent.st_dev`;
- not symlink-resolve into discovery root;
- not collide with existing user data.

No safe location：

`SAFE_QUARANTINE_UNAVAILABLE`

and no mutation.

Forbidden fallback：

- cache-hidden quarantine;
- copy + delete;
- cross-filesystem move;
- CLI uninstall/reinstall;
- Plugin Creator;
- prompt blacklist.

## 6. User-cache concurrency contract

Replay lock does not protect other local Codex consumers.

Before suppression：

- run bounded read-only process preflight;
- exclude current helper/Executor process tree;
- positively identify obvious other active Codex consumers sharing the same effective `CODEX_HOME`;
- if found：
  `CONCURRENT_SHARED_CODEX_HOME_CONSUMER`
  -> no quarantine.

Do not kill, pause, signal, or take over other processes.

Do not add daemon/watcher/global lock/state machine.

## 7. Recovery manifest

Before mutation save at least：

- discovery/cache resolved root;
- quarantine parent;
- both `st_dev`;
- exact original path;
- exact quarantine path;
- package tree hash;
- plugin manifest hash;
- overlapping Skill names;
- marketplace/plugin/version identity;
- normalized plugin list;
- config hash;
- candidate installed identity/path;
- transaction phase.

Manifest + parent must be fsynced before rename.

## 8. Restoration

Frozen order：

```text
manifest/fsync
-> atomic rename original -> quarantine
-> child
-> consumption evidence
-> exact restore
-> hash/state verification
-> candidate cleanup
-> final equality
```

Must restore on：

- child non-zero;
- ReplayError;
- timeout;
- ordinary exception;
- KeyboardInterrupt/SIGINT;
- catchable SIGTERM.

For SIGKILL/power loss, next helper entry performs stale recovery first.

Automatic restore only when：

```text
original missing
quarantine exists
hash matches
provenance valid
filesystem/discovery assumptions still valid
```

Otherwise：

`RESTORATION_AMBIGUOUS`

and do not overwrite/delete/start child.

## 9. Consumption proof

PASS requires：

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
```

If original conflict path reappears/gets read or quarantine gets read：

FAIL even if candidate was also read.

Restoration still runs.

## 10. Tests

Deterministic suite must cover the approved Proposal/Plan list, including：

- cross-plugin exact Skill conflict;
- no conflict;
- same-name conflict;
- multi-candidate;
- discovery-root exclusion;
- same-filesystem success;
- cross-filesystem fail;
- no cache-hidden fallback;
- symlink rejection;
- success/non-zero/timeout/exception/SIGTERM restore;
- stale recovery;
- ambiguous recovery;
- account rehydration/read failure;
- candidate/original/quarantine three-way proof;
- concurrency preflight;
- no remote/config mutation.

Existing helper tests remain green.

## 11. Risk-matched real replay

Only：

1. one existing single-plugin candidate replay;
2. one `web-development + writing-style` multi-plugin replay;
3. exact 059 replay against：
   `ac501d988f00cb6672fec105ae5fd51a0679cae0`.

059 must show：

```text
candidate reads > 0
original live-wrapper reads = 0
quarantine reads = 0
no PDF/render mechanics
before/after persistent state equality = PASS
```

Do not alter the natural task prompt with isolation/render blacklists.

## 12. Stop state

If all helper checks and the exact 059 development replay pass：

```text
SHARED_REPLAY_INFRASTRUCTURE_READY=YES
REPLAY_INFRASTRUCTURE_COMMIT=<I>
REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
059_DEVELOPMENT_REPLAY=PASS
C2_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

Planner then decides/promotes unchanged Research Authoring product identity to C2 and freezes new final tasks.

Executor does not start final Gates.

## 13. Version / release

```text
Repository bump decision: NONE
Affected plugins: NO_BUMP
Research Authoring: unchanged 0.3 candidate
README: no update
main/release: no mutation
```

## 14. Authorization ceiling

A future approved Kickoff may authorize only：

- exact branch/worktree;
- three shared helper files;
- deterministic tests;
- bounded concurrency preflight;
- temporary conflicting local cache quarantine inside replay lock;
- same-filesystem out-of-discovery atomic rename;
- exact restoration;
- stale recovery;
- the three risk-matched replays;
- evidence;
- helper-only/evidence commits;
- ordinary non-force push exact task branch.

It does not authorize：

- remote Plugin/Plugin Creator;
- permanent uninstall;
- killing other processes;
- Research Authoring production changes;
- G1-G4 final Gates;
- G4 ChatGPT;
- PDF production;
- paid API;
- Bridge/Host Policy;
- main/release;
- destructive Git;
- new daemon/state system.

## 15. Positive terminal condition

This bounded Goal succeeds only as shared validation infrastructure：

```text
SHARED_REPLAY_INFRASTRUCTURE_READY=YES
059_DEVELOPMENT_REPLAY=PASS
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

It does not mean Research Authoring 0.3 is complete or released.
