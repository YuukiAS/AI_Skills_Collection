# 059 Candidate Plugin Replay 共享隔离恢复 — Implementation Plan v0.1

日期：2026-10-06  
状态：READY_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
Repository：`YuukiAS/AI_Skills_Collection`  
Task key：`research-authoring--formal-production-authoring`  
Execution branch：`work/research-authoring--formal-production-authoring`  
Existing worktree：`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

## 0. Authority

Approved recovery design：

- Proposal：`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_PROPOSAL_V0_2_2026-10-06.md`
- Proposal commit：`f479efb4e2ad31eaafe6ec56b9fc0ba3f284c569`
- Critic PASS：`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_CRITIC_REVIEW_V0_2_2026-10-06.md`
- Critic commit：`307904418e42b704e8bf6e0f1f27aa93c1368a87`

Approved conclusion：

```text
ROOT_CAUSE=SHARED_CANDIDATE_REPLAY_CONSUMER_ISOLATION_GAP
APPROVED_ROUTE=B_TEMPORARY_LOCAL_CACHE_SUPPRESSION_WITH_EXACT_RESTORE
CPR1=CLOSED
MODIFY_SHARED_CANDIDATE_PLUGIN_REPLAY=YES
MODIFY_RESEARCH_AUTHORING_PRODUCTION=NO
FINAL_GATES_MAY_START=NO
```

Research Authoring product identity remains：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

This Plan only repairs shared replay infrastructure. It does not modify or re-authorize Research Authoring production.

## 1. Positive completion

This bounded infrastructure task is complete only when the existing `candidate_plugin_replay` can safely isolate an exact candidate from an overlapping live local cache consumer and restore user state exactly.

Required positive outcome：

1. exact top-level Skill `name` overlap is detected generically across candidate and live cached Plugin packages;
2. only conflicting live cached packages are temporarily suppressed;
3. suppression moves them outside the plugin discovery/cache root;
4. move is same-filesystem atomic rename only;
5. child consumes the candidate;
6. child reads neither the original conflict path nor quarantine path;
7. account-backed rehydration or conflicting-path read causes FAIL;
8. success/failure/timeout/exception restoration returns persistent state exactly to the before snapshot;
9. stale transaction recovery is fail-closed;
10. existing no-conflict, single-plugin and multi-plugin replay behavior does not regress;
11. the exact 059 replay against `ac501d98...` proves candidate consumption and closes the current development-replay infrastructure blocker;
12. no Research Authoring production file changes.

This task does not make Research Authoring final Gates pass. It only restores a valid development-replay evidence path.

## 2. Allowed tracked implementation scope

Only these shared infrastructure files may change：

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
```

Task evidence may be added under：

```text
results/research-authoring--formal-production-authoring/
  g4_c1_c2_replay_infrastructure_recovery/**
```

Private/runtime replay material remains under existing ignored/task-local runtime/private paths.

Explicit ZERO WRITE：

- Research Authoring production source/config/tests/generated payload;
- `ac501d988f00cb6672fec105ae5fd51a0679cae0`;
- live `research-authoring` Plugin;
- Plugin Creator remote object;
- Bridge Kit;
- Host Policy;
- profiles;
- Marketplace product payload;
- root/plugin versions;
- README;
- main/release;
- G1-G4 frozen task/rubric semantics.

No second replay framework may be created.

## 3. Generic conflict detection

### Candidate identities

After staging exact committed candidate payloads, parse each top-level：

`skills/*/SKILL.md`

and read exact frontmatter `name`.

For multi-plugin replay, form the union of candidate Skill names.

If two candidate packages themselves expose the same top-level public Skill name and the helper cannot deterministically prove they are intended duplicates, fail closed before any live mutation.

### Live cached identities

Discover the current effective plugin discovery/cache root used by the current Codex identity. Inspect installed local cache packages under the resolved discovery root, excluding this run's `ai-skills-candidate` packages.

For each package, parse top-level `skills/*/SKILL.md` frontmatter `name`.

A live package is a conflict iff：

```text
candidate_top_level_skill_names
INTERSECT
live_package_top_level_skill_names
!= empty
```

No hard-coded `research-authoring`, `research-writing`, marketplace or 059 path is allowed.

This first version deliberately does not add description similarity, embedding/LLM matching, or heuristic semantic conflict detection.

## 4. Quarantine root selection

Temporary suppression is allowed only by same-filesystem atomic rename to a location outside plugin discovery.

For each replay：

1. resolve the effective plugin discovery/cache root;
2. resolve each conflict package original path;
3. choose a task-local quarantine parent outside the discovery root, with the preferred shape：
   `$CODEX_HOME/.candidate-plugin-replay-quarantine/<run-id>/`;
4. resolve the quarantine parent and candidate destination;
5. verify quarantine parent is not inside, equal to, or symlink-resolved back under plugin discovery/cache root;
6. verify：
   `original.st_dev == quarantine_parent.st_dev`;
7. verify the quarantine destination does not collide with pre-existing user data.

If any package lacks a safe out-of-discovery same-filesystem destination：

```text
SAFE_QUARANTINE_UNAVAILABLE
```

Fail closed before mutation.

Forbidden fallback：

- any `plugins/cache/**` hidden quarantine directory;
- copy + delete;
- cross-filesystem move;
- CLI uninstall/reinstall;
- Plugin Creator mutation;
- prompt blacklist;
- changing candidate identity.

## 5. Concurrency preflight

The existing replay lock protects only `candidate_plugin_replay` invocations. It does not protect unrelated local Codex processes sharing the same user-level `CODEX_HOME`.

Before any quarantine mutation：

1. run a bounded read-only process inspection;
2. exclude the current helper/Executor process tree;
3. identify obvious other active Codex consumers that can be directly associated with the same effective `CODEX_HOME`;
4. if such a consumer is positively identified：
   `CONCURRENT_SHARED_CODEX_HOME_CONSUMER`
   -> fail closed;
   -> do not quarantine;
   -> do not kill, pause, signal or take over that process.

The implementation may use current Linux process metadata/read-only diagnostics to prove obvious concurrency. It must not create a daemon, watcher, global lock service or process supervisor.

The preflight is intentionally bounded: it detects directly observable conflicting consumers; it does not claim universal proof that no same-user process can ever touch the cache.

## 6. Durable recovery manifest

Before the first rename, write a durable manifest containing at least：

- replay run id;
- resolved plugin discovery/cache root;
- resolved quarantine parent;
- original `st_dev`;
- quarantine-parent `st_dev`;
- each conflict package exact original path;
- each conflict package exact quarantine path;
- complete package tree SHA256 manifest/hash;
- plugin manifest hash;
- overlapping Skill names;
- original marketplace/plugin/version identity;
- normalized before `codex plugin list --json`;
- `$CODEX_HOME/config.toml` hash if present;
- candidate installed identity/path;
- transaction phase sufficient for entry-time crash recovery.

Write + fsync the manifest and parent before mutation.

This is a bounded crash-recovery journal, not a persistent workflow state machine.

## 7. Transaction and restoration

Frozen order：

```text
acquire replay lock
-> recover stale transaction if present
-> install/stage exact candidate
-> detect Skill-overlap conflicts
-> concurrency preflight
-> resolve/validate out-of-discovery quarantine
-> same-filesystem st_dev gate
-> durable recovery manifest + fsync
-> atomic rename original conflict packages -> quarantine
-> fsync affected parents where supported
-> fresh child replay
-> collect consumption/runtime evidence
-> exact restore quarantine -> original
-> verify hashes / plugin state / config state
-> remove candidate
-> final before/after equality
-> release replay lock
```

### Normal failures

For：

- child non-zero;
- `ReplayError`;
- timeout;
- ordinary exception;
- `KeyboardInterrupt` / SIGINT;
- catchable SIGTERM;

restoration is attempted before the failure returns.

### SIGKILL / power loss

At every helper entry, stale recovery is processed before candidate install or new replay.

Automatic restore is allowed only if：

```text
original path missing
AND quarantine path exists
AND quarantine tree/manifest hash matches recorded before hash
AND recorded provenance is valid
AND current discovery/filesystem assumptions remain valid
```

Any ambiguous condition returns：

`RESTORATION_AMBIGUOUS`

and must：

- not overwrite;
- not delete either side;
- not start child;
- preserve manifest/evidence for manual Planner/Critic recovery.

If original and quarantine both exist, even if one appears rehydrated, do not silently delete either side.

## 8. Replay PASS evidence

A replay cannot PASS merely because candidate was also read.

Required：

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
```

Also required：

- candidate actual-consumption event remains bound to exact installed candidate path;
- no conflict package reappears/gets read during child execution;
- all conflict packages are restored to exact original paths;
- tree hashes match before snapshot;
- plugin-manifest hashes match;
- marketplace/plugin/version identity matches;
- normalized plugin-list state matches;
- config hash matches;
- candidate is removed;
- no stale quarantine/recovery entry remains.

If account-backed state rehydrates the original path during the run, or child reads original/quarantine, replay FAILs even if candidate is consumed.

Restoration/equality verification still runs after such a failure.

## 9. Deterministic tests

`tests/test_candidate_plugin_replay.py` must cover at least：

1. different plugin name / same exact Skill name conflict;
2. no-conflict path;
3. same-name production conflict;
4. multi-candidate union and candidate-candidate conflict;
5. quarantine outside discovery root;
6. same-`st_dev` success;
7. cross-filesystem fail closed;
8. no cache-hidden fallback;
9. symlink resolve-back / escape rejection;
10. success restoration;
11. child non-zero restoration;
12. timeout restoration;
13. ordinary exception restoration;
14. stale quarantine recovery;
15. ambiguous recovery fail closed;
16. account-backed original-path rehydration/read -> FAIL;
17. three-way candidate/original/quarantine read proof;
18. concurrency preflight positive -> fail closed;
19. concurrency preflight no-conflict -> no regression;
20. remote Plugin/config not mutated.

Existing helper tests must continue to pass：

- actual-consumption parser;
- candidate cleanup;
- timeout child-tree kill;
- multiple candidate plugins;
- repo-relative input/writable scope;
- candidate marketplace staging.

Unit tests may use filesystem/process fixtures. They do not authorize real user-cache mutation.

## 10. Risk-matched real replay

After deterministic tests pass, run only these representative real replays：

### A. Existing single-plugin replay

Reuse one public-safe existing successful candidate replay, preferably workflow-core or ai-skills-core.

Purpose：
prove no-conflict/single-plugin path still loads exact candidate and restores state.

### B. Existing multi-plugin replay

Reuse the public-safe `web-development + writing-style` same-session candidate replay.

Purpose：
prove multi-plugin replay remains functional and conflict union logic does not break legitimate multi-candidate operation.

### C. Exact 059 blocking replay

Replay exact：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

using the already-prepared 059 development replay task/input.

Required：

```text
candidate reads > 0
original live-wrapper reads = 0
quarantine reads = 0
no PDF/render mechanics
before/after persistent state equality = PASS
```

This is development regression only. It does not start G1-G4 final Gates.

Do not strengthen the task prompt with test-specific isolation/render blacklists to manufacture PASS.

If exact 059 replay still consumes the live wrapper, rehydrates conflict state, or cannot safely isolate the cache, stop and return Planner/Critic. Do not modify Research Authoring production.

## 11. Infrastructure and product identity

Three identities remain separate.

### Research Authoring product

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

This task must not change it.

### Shared replay infrastructure

After helper source/tests/docs are complete and deterministic validation passes, create：

```text
REPLAY_INFRASTRUCTURE_COMMIT=<helper-only commit>
```

This commit may contain only approved shared helper source/test/docs plus no Research Authoring product change.

### Evidence head

After representative replay evidence is written：

```text
EVIDENCE_PACKET_HEAD=<latest evidence commit>
```

Evidence commits must not alter Research Authoring product or helper source after the infrastructure commit unless a new infrastructure candidate is explicitly formed.

## 12. 059 recovery state

Even after helper implementation commit exists：

`C2_CANDIDATE_READY=NO`

until exact 059 replay validly passes.

If helper tests + representative replays + exact 059 replay all pass, Executor stops with：

```text
SHARED_REPLAY_INFRASTRUCTURE_READY=YES
REPLAY_INFRASTRUCTURE_COMMIT=<I>
REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
059_DEVELOPMENT_REPLAY=PASS
C2_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

Planner, not Executor, then promotes the unchanged `ac501d98...` product tree to the C2 product candidate identity, freezes new C2 G1/G2/G3 final tasks, and submits C2 + infrastructure + evidence identities to pre-final Critic.

## 13. Version / README / release

This is validation infrastructure repair, not a user-facing plugin release.

```text
Repository bump decision: NONE
Affected plugins: NO_BUMP
Research Authoring version: unchanged 0.3 candidate
root VERSION: unchanged
README: no update
formal release: NO
```

`docs/workflows/CANDIDATE_PLUGIN_REPLAY.md` changes because it is the helper contract.

No root/plugin changelog or Marketplace product payload changes are expected.

## 14. Authorization boundary

The future approved Kickoff must explicitly authorize the short-lived user-level local cache mutation.

Authorized only after the user actually sends that approved Kickoff：

- exact existing branch/worktree;
- edits to the three shared replay infrastructure files;
- deterministic tests;
- read-only concurrency preflight;
- inside the helper replay lock, temporary atomic quarantine of only automatically detected exact-Skill-overlap local cached packages;
- quarantine only outside plugin discovery root and on same filesystem;
- exact restoration after success/failure/timeout;
- entry-time stale recovery;
- task-owned evidence files;
- three risk-matched real replays;
- helper-only commit(s) and evidence commit(s);
- ordinary non-force push exact task branch.

Not authorized：

- Plugin Creator;
- remote Plugin mutation;
- permanent uninstall;
- killing/pausing/taking over other Codex processes;
- cross-filesystem copy/delete;
- Research Authoring production change;
- live Research Authoring update;
- final G1-G4;
- PDF production;
- paid API;
- Bridge/Host Policy change;
- main/release/tag;
- force/destructive Git;
- daemon/watcher/global lock/state machine.

## 15. Failure semantics

- `SAFE_QUARANTINE_UNAVAILABLE` -> stop, no mutation.
- `CONCURRENT_SHARED_CODEX_HOME_CONSUMER` -> stop, no mutation.
- `RESTORATION_AMBIGUOUS` -> stop, preserve both sides + manifest; do not start another replay.
- conflict path read / rehydration -> replay FAIL, restore/equality first, then stop.
- candidate not consumed -> replay FAIL; no prompt escalation.
- deterministic/helper regression -> repair only within approved helper scope, rerun risk-matched checks.
- fix requires Bridge/Host Policy/Research Authoring/product config -> stop to Planner/Critic.
- helper source changes after `REPLAY_INFRASTRUCTURE_COMMIT` -> form new infrastructure commit identity; old replay evidence becomes stale.

## 16. Execution-ready Critic review

Critic must review this Plan together with same-version Goal and Kickoff and confirm：

1. only existing helper is modified;
2. exact Skill-name conflict signal matches approved Proposal;
3. out-of-discovery + same-`st_dev` quarantine is executable and fail-closed;
4. concurrency preflight is bounded;
5. restoration covers ordinary failure and stale crash recovery;
6. three-way read proof closes false PASS;
7. tests are risk-matched;
8. representative real replay set is sufficient;
9. product/infrastructure/evidence identities remain distinct;
10. Kickoff makes the user-level cache mutation explicit and does not silently authorize other user/global changes.

Only execution-ready Critic PASS may produce：

`READY_FOR_CODEX=YES`

This Plan itself authorizes no mutation.
