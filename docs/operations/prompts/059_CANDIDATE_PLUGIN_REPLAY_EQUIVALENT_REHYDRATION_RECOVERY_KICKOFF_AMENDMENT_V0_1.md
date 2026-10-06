# 059 Candidate Plugin Replay 等价再水化恢复 — Kickoff Draft Amendment v0.1

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-06

只有独立 Critic 对以下 amended execution package 给出 execution-ready PASS，并逐字批准本 Kickoff 后，用户实际发送这份批准正文，才形成执行授权。

Approved recovery design：

- `docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_PROPOSAL_V0_1_2026-10-06.md`
  @ `b0b9fc8c50251789fe97f21395637f7060cd7d89`
- `docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_AMENDMENT_V0_1_2026-10-06.md`
  @ `3b2d747f07a69f808d092fc2c24daf22a4687780`
- Critic PASS：
  `docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_CRITIC_REVIEW_V0_1_2026-10-06.md`
  @ `7a3dd5b19db779d17d224cec1dd8cba0a4a9f182`
- Goal amendment：
  `docs/goals/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_GOAL_AMENDMENT_V0_1.md`
  @ `eae4bd36c52965406fc6d35a7f852b1cf52e4939`

## Kickoff 正文

继续同一 059 task，只实现已批准的 equivalent-rehydration recovery amendment。

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

这个 product commit不得修改。

Prior shared replay helper commit：

`b61c46957709030bee3735c77d21701871f0480b`

Current evidence head：

`dcf9381eacc6c56f954fc3ca60f3ab8e351d1fb1`

开始前：

1. 核实 exact worktree/repo/origin/branch/dirty ownership，并 `git fetch origin main`；
2. 读取 approved recovery Proposal、Plan amendment、Critic PASS、Goal amendment；
3. 不重新设计 isolation、quarantine、Skill-overlap detection 或 Route A/B/C/D；
4. 不修改 Research Authoring production；
5. 不启动 final Gates。

只允许修改：

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
```

以及 task-local evidence：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/**`

## 我明确批准的新增 bounded local-cache side effect

我明确批准本任务在**完整 VERIFIED_EQUIVALENT_REHYDRATION 条件成立时**，执行一次严格受限的本地恢复操作：

只有当当前或未来 transaction 同时满足：

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

quarantine exact path is owned by the current transaction/run

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

才允许：

1. 保留 rehydrated original 不动；
2. 只删除 exact current-transaction-owned quarantine duplicate；
3. 不删除、不覆盖 original；
4. fsync quarantine parent / relevant parent；
5. 重新读取 original tree/manifest；
6. 重新验证 config 和 normalized non-candidate plugin state；
7. 只有当：
   `FINAL_PERSISTENT_STATE_EQUIVALENT_TO_BEFORE=YES`
   时，才删除 recovery manifest。

任何 proof缺失、不一致、不可读、identity不匹配、hash不匹配、read evidence不满足，必须返回：

`RESTORATION_AMBIGUOUS`

并：

- 不删除任一 side；
- 不覆盖任一 side；
- 不继续 candidate replay；
- 保存 evidence；
- 返回 Planner/Critic。

这段授权只允许删除本次 transaction 自己创建、且已证明与 pre-state 完全等价的 quarantine duplicate，不授权删除任何其他用户文件或 Plugin cache。

## Stage 0 — 先处理当前 preserved dual-copy transaction

在修改 helper或启动新 replay之前，先处理：

```text
run_id=
20261006T071703Z-3410223
```

Recovery manifest：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/replays/multi_web_writing_failed_ambiguous/recovery-manifest.json`

Tracked child evidence：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/replays/multi_web_writing_failed_ambiguous/child.stdout.jsonl`

Stage 0 必须现场重新只读验证：

- current original tree hash；
- current quarantine tree hash；
- original/quarantine manifest hash；
- path/marketplace/plugin/version；
- transaction ownership；
- config hash；
- normalized plugin state；
- candidate/original/quarantine read evidence。

Tracked child evidence只能证明历史 read side，不能单独授权 cleanup。

Stage 0不通过：
- 不删除；
- 不修改 helper；
- 不启动 replay；
- 直接返回 `RESTORATION_AMBIGUOUS` / Planner。

## Helper amendment

按 approved Plan amendment实现：

- 加入 `VERIFIED_EQUIVALENT_REHYDRATION` classification；
- passive original reappearance不再单独构成 isolation FAIL；
- actual conflict-path consumption仍是 hard FAIL；
- cleanup前 durable保存 post-child evidence；
- only transaction-owned equivalent quarantine duplicate可以删除；
- cleanup后重新做 persistent-state equality。

Replay PASS必须仍满足：

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
FINAL_PERSISTENT_STATE_EQUIVALENT_TO_BEFORE=YES
```

candidate也被读到不能掩盖 conflict consumption。

## Validation sequence

如果 Stage 0安全完成并形成 helper amendment：

1. deterministic helper tests；
2. 形成新的 helper-only：
   `REPLAY_INFRASTRUCTURE_COMMIT=<I2>`；
3. 在 I2 下重新跑 representative single-plugin replay；
4. 在 I2 下重新跑 `web-development + writing-style` multi-plugin replay；
5. 只有 multi-plugin PASS 后，才运行 exact 059 development replay against：
   `ac501d988f00cb6672fec105ae5fd51a0679cae0`。

旧 multi replay永久保持：

`FAIL / RESTORATION_AMBIGUOUS`

旧 `b61c...` single-plugin PASS仅作历史 evidence，不能拼进 I2 PASS。

059 replay仍然只是 development regression，不是 final Gate。

不得通过增强 replay prompt、添加 isolation/render blacklist或换任务追 PASS。

## Identity

保持：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

形成：

```text
REPLAY_INFRASTRUCTURE_COMMIT=<I2>
EVIDENCE_PACKET_HEAD=<E2>
```

I2/E2 不得算作 Research Authoring product candidate。

即使全部 replay PASS，Executor仍只能停在：

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

Planner后续才决定 C2 identity和新的 final packet。

## 其余原 Kickoff 授权继续受限

仍只允许：

- existing candidate_plugin_replay lock内操作；
- exact Skill-overlap conflict suppression；
- plugin discovery root外、same-filesystem quarantine；
- bounded read-only concurrency preflight；
- success/failure/timeout exact restore；
- stale recovery；
- helper source/test/docs；
- risk-matched replays；
- task-local evidence；
- helper/evidence commits；
- ordinary non-force push exact branch。

## 明确不授权

- 删除任何未证明 transaction-owned equivalent 的 path；
- 修改/删除 rehydrated original；
- Plugin Creator；
- remote Plugin mutation；
- permanent uninstall；
- kill/pause/take over其他 Codex进程；
- Research Authoring production change；
- live Research Authoring Plugin update；
- G1-G4 final Gate；
- G4 ChatGPT；
- PDF production；
- paid API；
- private/sensitive external upload；
- Bridge/Host Policy change；
- main/release/tag/GitHub Release；
- force push/destructive Git；
- daemon/watcher/global state machine。

完成后立即停给 Planner，不继续 final Gates。
