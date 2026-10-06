# 059 Candidate Plugin Replay 共享隔离恢复 — Kickoff Draft v0.1

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-06

只有独立 Critic 对下列同版执行包给出 execution-ready PASS，并逐字批准本 Kickoff 后，用户实际发送这份批准正文，才形成执行授权：

- Proposal：
  `docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_PROPOSAL_V0_2_2026-10-06.md`
  @ `f479efb4e2ad31eaafe6ec56b9fc0ba3f284c569`
- Architecture Critic PASS：
  `docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_CRITIC_REVIEW_V0_2_2026-10-06.md`
  @ `307904418e42b704e8bf6e0f1f27aa93c1368a87`
- Implementation Plan：
  `docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md`
  @ `8dbe6b4ee0d359436b231d21632963b4b40346f1`
- Canonical Goal：
  `docs/goals/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_GOAL_V0_1.md`
  @ `c2eac9aa677fbeffed5114269dfac93c2bd03590`

## Kickoff 正文

继续同一 059 task，只实现已批准的 shared `candidate_plugin_replay` consumer-isolation recovery。

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

这个 product commit 不得修改。

开始前：

1. 在 exact worktree 核实 repo/origin/branch/dirty ownership，并 `git fetch origin main`；
2. 读取 current `AGENTS.md`、approved Proposal v0.2、Critic PASS、Implementation Plan v0.1、Canonical Goal v0.1；
3. 核实从 `ac501d98...` 到当前 branch HEAD 的 Research Authoring candidate-owned production files没有未经批准的变化；
4. 不创建 successor task、第二套 replay framework、watcher、daemon、database 或 state machine。

只允许修改：

```text
scripts/candidate_plugin_replay.py
tests/test_candidate_plugin_replay.py
docs/workflows/CANDIDATE_PLUGIN_REPLAY.md
```

以及 task-local evidence：

`results/research-authoring--formal-production-authoring/g4_c1_c2_replay_infrastructure_recovery/**`

## 我明确批准的短暂用户级本地状态副作用

我明确批准本任务在当前用户的 `candidate_plugin_replay` lock 内，为了测试未发布 candidate，执行下面这个**短暂、可恢复、限定范围**的本地 plugin-cache mutation：

1. 只处理 helper 自动检测出的、与 candidate 存在 exact top-level Skill `name` overlap 的 conflicting local cached Plugin package；
2. suppression 前必须先做最小只读并发检查；
3. 如果明确发现其他活跃 Codex consumer 正在共享同一个有效 `CODEX_HOME`，立即 fail closed，不移动任何 Plugin，不 kill/pause/接管其他进程；
4. quarantine 必须位于 plugin discovery/cache root **之外**；
5. quarantine parent 必须和 original package 在同一 filesystem，并在 mutation 前验证：
   `original.st_dev == quarantine_parent.st_dev`；
6. 只允许 same-filesystem atomic rename；
7. 不允许 copy + delete、cross-filesystem move、cache 内隐藏 quarantine、CLI uninstall/reinstall fallback；
8. 不调用 Plugin Creator，不修改 remote Plugin，不永久 uninstall live Plugin，不修改用户 config/auth/credential；
9. temporary quarantine期间，该冲突 live Plugin 对共享同一 `CODEX_HOME` 的其他本地 Codex进程可能暂时不可用；这个影响只允许存在于已通过并发 preflight后的最短 replay窗口；
10. 成功、child FAIL、ReplayError、timeout、ordinary exception、SIGINT、catchable SIGTERM 都必须先 exact restore，再返回；
11. SIGKILL/power-loss 后，下一次 helper入口必须先按 recovery manifest恢复或 fail closed；
12. ambiguous recovery 必须返回 `RESTORATION_AMBIGUOUS`，不得覆盖、删除或继续 child replay；
13. 如果无法找到 discovery root之外且同 filesystem 的安全 quarantine位置，返回 `SAFE_QUARANTINE_UNAVAILABLE`，不得降级；
14. ordinary non-force push只允许当前 exact task branch。

这段授权不延伸到其他用户级或远端状态。

## 实现合同

按 Plan/Goal实现：

- exact Skill-name overlap generic conflict detection；
- out-of-discovery quarantine；
- same-`st_dev` gate；
- durable recovery manifest + fsync；
- atomic rename；
- exact restore；
- stale recovery；
- before/after equality；
- candidate/original/quarantine three-way consumption proof；
- account-backed rehydration/read -> FAIL；
- bounded concurrency preflight。

Replay PASS必须满足：

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
```

candidate也被读到不能掩盖 conflict path读取。

## Deterministic validation

运行 approved focused/full helper tests，至少覆盖 Goal §10 的全部风险面。

Existing candidate replay behavior必须保持：
- candidate staging；
- actual-consumption parser；
- cleanup；
- timeout child-tree kill；
- multi-candidate；
- repo-relative input/writable boundaries。

## Risk-matched real replay

只执行三类：

1. 一个既有 public-safe single-plugin candidate replay；
2. 一个 `web-development + writing-style` public-safe multi-plugin replay；
3. 059 exact development replay against：
   `ac501d988f00cb6672fec105ae5fd51a0679cae0`。

059 replay不得用更强 prompt blacklist追 PASS。

必须证明：

```text
candidate reads > 0
original live-wrapper reads = 0
quarantine reads = 0
no PDF/render mechanics
before/after persistent state equality = PASS
```

如果 helper修复后 059仍读取 live wrapper、发生 rehydration、无法安全 quarantine、或 candidate仍未真实消费，停止回 Planner/Critic；不要修改 Research Authoring绕过。

## Commit identity

先形成 helper-only：

```text
REPLAY_INFRASTRUCTURE_COMMIT=<I>
```

后续 replay/evidence可形成：

```text
EVIDENCE_PACKET_HEAD=<E>
```

但 Research Authoring product identity保持：

```text
REPAIRED_PRODUCT_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

不要把 `I` 或 `E` 称为 Research Authoring C2。

即使 exact 059 replay PASS，本轮也只停止给 Planner：

```text
SHARED_REPLAY_INFRASTRUCTURE_READY=YES
REPLAY_INFRASTRUCTURE_COMMIT=<I>
REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
059_DEVELOPMENT_REPLAY=PASS
C2_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

Planner后续再决定把 unchanged `ac501d98...` 提升为 C2，并冻结新的 final packet。

## 明确不授权

本 Kickoff不授权：

- Research Authoring production change；
- `ac501d98...` 变化；
- live `research-authoring` Plugin update；
- Plugin Creator；
- remote Plugin mutation；
- permanent uninstall；
- kill/pause/takeover其他 Codex进程；
- Bridge Kit / Host Policy change；
- profiles / Marketplace production payload change；
- version / README change；
- G1-G4 final Gate；
- G4 ChatGPT；
- PDF production；
- paid API；
- private/sensitive external upload；
- main/release/tag/GitHub Release；
- force push/destructive Git；
- background automation。

README 与版本保持不变。

完成 approved helper implementation、tests、三类 replay和 evidence 后立即停止，不继续 final Gates。
