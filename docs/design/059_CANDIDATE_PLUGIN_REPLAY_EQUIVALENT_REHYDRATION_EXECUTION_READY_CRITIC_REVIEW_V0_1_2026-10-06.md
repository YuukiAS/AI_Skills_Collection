# 059 Candidate Plugin Replay 等价再水化恢复 — Execution-Ready Critic Review v0.1

日期：2026-10-06  
角色：独立 Critic  
审查阶段：EXECUTION_READY_REVIEW  
Task：`research-authoring--formal-production-authoring`

## 结论

```text
RESULT=PASS
READY_FOR_CODEX=YES
```

本 PASS 只批准 equivalent-rehydration recovery amendment 的 bounded implementation、Stage 0 conditional cleanup、后续 I2 验证与三类 risk-matched replay。

真正的本地 quarantine duplicate 删除权限，只有在用户实际发送本审查逐字批准的 amended Kickoff 后才成立。

不批准 Research Authoring production change、live Plugin update、G1-G4 final Gates、G4 ChatGPT、PDF production、paid API、Bridge/Host mutation、main merge 或 release。

## 批准绑定

Recovery Proposal：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_PROPOSAL_V0_1_2026-10-06.md`  
commit：`b0b9fc8c50251789fe97f21395637f7060cd7d89`

Recovery Critic PASS：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_CRITIC_REVIEW_V0_1_2026-10-06.md`  
commit：`7a3dd5b19db779d17d224cec1dd8cba0a4a9f182`

Plan amendment：

`docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_AMENDMENT_V0_1_2026-10-06.md`  
commit：`3b2d747f07a69f808d092fc2c24daf22a4687780`

Goal amendment：

`docs/goals/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_GOAL_AMENDMENT_V0_1.md`  
commit：`eae4bd36c52965406fc6d35a7f852b1cf52e4939`

Kickoff amendment：

`docs/operations/prompts/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_KICKOFF_AMENDMENT_V0_1.md`  
commit：`4b5edec8df8773ce97702404fa87d7b8a8e658f9`

Package index：

`results/research-authoring--formal-production-authoring/CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_EXECUTION_PACKAGE_V0_1.md`  
commit：`dbd34886327000808f1c461015aee03a80a3e0f7`

Goal、Kickoff、package index 在当前 task branch 的内容与声明 commit byte-for-byte 一致。

从 recovery Critic PASS `7a3dd5b...` 到 package head `dbd3488...` 只新增 amended Goal、Kickoff 和 package index，没有 helper source、Research Authoring production 或 live Plugin mutation提前发生。

## 当前 policy / execution context

审查时核对：

- AI_Skills_Collection main：`5f20e0482a686ab249c47566c312c8c94214a3cc`
- task branch：`dbd34886327000808f1c461015aee03a80a3e0f7`
- Bridge Kit main：按最新 main AGENTS 读取，未发现要求修改 Bridge/Host 的新事实。

继续复用：

- branch：`work/research-authoring--formal-production-authoring`
- worktree：`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

无需 successor task、branch、watcher、daemon、database 或 state machine。

## 上一轮 blocker 的闭环

真实 multi-plugin replay 已证明 candidate isolation 工作，但 account-backed live wrapper 在 quarantine 窗口内被重新水化回 original path，导致旧恢复合同看到 original + quarantine 双副本后正确 fail closed。

本 amended package 没有削弱隔离，而是把“路径重新出现”和“child 实际消费 live path”分开。

只有完整 `VERIFIED_EQUIVALENT_REHYDRATION` 成立时，才允许保留 rehydrated original 并删除 current transaction-owned identical quarantine duplicate。

任何 hash、manifest、identity、config、plugin-state、transaction ownership 或 read-evidence 缺失/不一致，继续 `RESTORATION_AMBIGUOUS`。

## Stage 0

Stage 0 顺序正确：

- 先读取当前 preserved manifest / child evidence；
- 现场只读核验 original/quarantine tree hash、manifest、identity、config、normalized plugin state、transaction ownership；
- 不满足完整等价条件即停止；
- 满足后才允许 conditional duplicate cleanup；
- cleanup 后 fsync、重新读取 original、再次验证 persistent-state equality；
- final equality 成立后才移除 recovery manifest。

Stage 0 未通过时不得修改 helper或启动新 candidate replay。

## Kickoff authorization review

Kickoff 对新的 destructive local side effect 说明充分：

只允许删除**当前 transaction 自己创建、并已证明与 pre-state / rehydrated original完全等价的 quarantine duplicate**。

它明确禁止：

- 删除/覆盖 rehydrated original；
- proof不完整时删除任一 side；
- Plugin Creator / remote Plugin mutation；
- permanent uninstall；
- Research Authoring production change；
- final Gates；
- paid API；
- main/release；
- destructive Git；
- unrelated user file deletion。

因此，用户实际发送该 Kickoff 后，形成的是可判定、限定对象、可恢复的本地 cache cleanup授权，而不是泛化删除权限。

## Implementation scope

允许 source 仍严格只有：

- `scripts/candidate_plugin_replay.py`
- `tests/test_candidate_plugin_replay.py`
- `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md`

以及 task-local evidence。

如果实际实现需要 Research Authoring、Bridge、Host Policy、Marketplace product payload 或其他 source，Executor必须停止回 Planner/Critic。

## Validation / identity

任何 helper source change 都形成新的：

`REPLAY_INFRASTRUCTURE_COMMIT=<I2>`

旧 `b61c469...` 不得 relabel 为新 PASS。

I2 必须依次重新通过：

1. deterministic tests；
2. representative single-plugin replay；
3. web-development + writing-style multi-plugin replay；
4. multi PASS后 exact 059 `ac501d98...` development replay。

旧 multi永久保持 FAIL；旧 single PASS只能做历史 evidence，不能跨 helper candidate拼 I2 PASS。

Research Authoring product identity继续：

`ac501d988f00cb6672fec105ae5fd51a0679cae0`

即使 amended infrastructure全部通过，Executor仍不得自行宣称 C2 ready；必须停止给 Planner。

## 外部实现核对

Python官方 `os.replace` 文档确认：同文件系统成功 rename/replace 时操作是原子的，跨文件系统可能失败；`os.fsync` 用于强制把文件描述符对应内容写入磁盘。当前 amended package 没有改变此前批准的 same-filesystem atomic quarantine基础，只增加严格的 post-run equivalent-duplicate reconciliation。

## Approved fields

```text
APPROVED_RECOVERY_PROPOSAL_PATH=docs/design/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_PROPOSAL_V0_1_2026-10-06.md
APPROVED_RECOVERY_PROPOSAL_COMMIT=b0b9fc8c50251789fe97f21395637f7060cd7d89

APPROVED_PLAN_AMENDMENT_PATH=docs/design/059_CANDIDATE_PLUGIN_REPLAY_SHARED_ISOLATION_RECOVERY_IMPLEMENTATION_PLAN_AMENDMENT_V0_1_2026-10-06.md
APPROVED_PLAN_AMENDMENT_COMMIT=3b2d747f07a69f808d092fc2c24daf22a4687780

APPROVED_GOAL_AMENDMENT_PATH=docs/goals/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_GOAL_AMENDMENT_V0_1.md
APPROVED_GOAL_AMENDMENT_COMMIT=eae4bd36c52965406fc6d35a7f852b1cf52e4939

APPROVED_KICKOFF_AMENDMENT_PATH=docs/operations/prompts/059_CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_RECOVERY_KICKOFF_AMENDMENT_V0_1.md
APPROVED_KICKOFF_AMENDMENT_COMMIT=4b5edec8df8773ce97702404fa87d7b8a8e658f9

APPROVED_PACKAGE_PATH=results/research-authoring--formal-production-authoring/CANDIDATE_PLUGIN_REPLAY_EQUIVALENT_REHYDRATION_EXECUTION_PACKAGE_V0_1.md
APPROVED_PACKAGE_COMMIT=dbd34886327000808f1c461015aee03a80a3e0f7

READY_FOR_CODEX=YES
```
