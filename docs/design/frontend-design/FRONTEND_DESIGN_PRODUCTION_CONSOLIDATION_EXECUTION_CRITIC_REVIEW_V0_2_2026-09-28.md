# Frontend Design Production Consolidation — Execution-Ready Critic Review v0.2

Review date: 2026-09-28  
Repository: `YuukiAS/AI_Skills_Collection`  
Review stage: recovery execution-ready review  
Reviewed package commit: `3d8669f52680f63f76ce537335fbee6019e4d5a9`  
Latest main checked before review: `547073b6b5120059239a5daf550eef1c47051c12`  
Bridge authority checked: `YuukiAS/GPT_Codex_AI_Bridge_Kit` latest main `9d15247d5cec5472a0f3c280a6bdd9d194a193fc`

REVIEWED_OBJECT = Frontend Design Production Consolidation execution package  
REVIEWED_PACKAGE_VERSION = v0.2  
RESULT = REVISE  
READY_FOR_CODEX = NO  
REVIEWED_PACKAGE_COMMIT = 3d8669f52680f63f76ce537335fbee6019e4d5a9  
APPROVED_TASK_KEY = web-development--frontend-design-production-consolidation  
REVIEWED_BRANCH = reviewed/web-development--frontend-design-production-consolidation  
REVIEWED_WORKTREE = /home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation  
ARCHITECTURE_AUTHORITY = docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md @ effa02b4e7e02f012ea24bda1683857609a09fe1

## 结论

v0.2 的恢复方向基本正确，Frontend Design Proposal v0.3 architecture 不需要重开。

三个 recovery 问题中：

1. Bridge first bootstrap 的真实 sibling worktree 已被正确识别；旧 `/tmp` locator 已明确废弃，Kickoff 的正常恢复路径也明确禁止 second bootstrap。
2. `external approved package -> GPT Planner task-local AI_BRIDGE_REVIEWED_PLAN_V2 -> PLAN_REQUESTED -> PLAN_FROZEN -> Executor` 的角色与状态合同已经与当前 Bridge source 对齐。
3. 固定的 repo 内 durable Critic review locator 设计正确，本文件即为该 locator；但因为本轮仍有两个 execution-package 一致性 blocker，所以当前必须记录 `REVISE / READY_FOR_CODEX=NO`，不能写 PASS。

剩余问题都不是 Frontend 产品架构问题，而是 v0.2 文档中仍残留会让 Executor 读到旧 authority 或重新获得创建 task/worktree 权限的 v0.1 文案。

## 已核实的 Bridge 事实

当前 Bridge main 的真实实现与规范支持 Planner 的主要 recovery 判断：

- `task bootstrap` 固定派生 `reviewed/<task_key>`。
- first-bootstrap worktree 由 `_repo_local_bootstrap_worktree()` 固定生成 `<repo-parent>/<repo-dir>-<task_key>`。
- bootstrap 创建 `REQUEST.md` / `CURRENT.json`，初态为 `PLAN_REQUESTED`、`next_action=RUN_GPT_PLANNER`。
- 新 freeze 必须使用 `AI_BRIDGE_REVIEWED_PLAN_V2`。
- `PLAN_REQUESTED -> PLAN_FROZEN` 需要合法 `PLAN.md`；只有从 `NEEDS_GPT_PLANNER` re-freeze 才增加 `plan_revision`，因此首次 freeze 不消耗 revision budget。
- `PLAN_FROZEN` 的下一执行动作是 `RUN_CODEX_EXECUTOR`。
- 已有 task 的 worktree 恢复使用 artifact-bound `materialize-worktree --mode resume`，并核对 REQUEST 冻结的 worktree locator。
- 当前 Bridge template 明确要求 Planner 写 V2 PLAN；Executor 不拥有 Planner 的 freeze authority。

Git 官方 `git worktree` 文档也确认 linked worktree 是 repository 管理的登记对象，已有 linked worktree 不应因为旧 locator 偏好而随意移动或重建。这个外部核查只支持 recovery mechanics，不改变 Frontend architecture。

## Recovery R1 — sibling worktree

主要机制：PASS。

Plan / Goal / Kickoff 都已经把 canonical recovery target 改为：

`/home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation`

Kickoff 还正确要求：

- 先检查 `git worktree list --porcelain`、REQUEST/CURRENT、base lineage 和 dirty ownership；
- 收养现有 sibling worktree；
- 不 second bootstrap；
- 不 raw `git worktree add`；
- 不 move/remove/recreate；
- future rematerialization 走 `materialize-worktree --mode resume`。

但 Goal/Plan 仍残留与上述 recovery 相冲突的“创建 branch/worktree”授权，见 blocker `FD-ER-R01`。

## Recovery R2 — task-local V2 PLAN

PASS。

v0.2 已把 task-local PLAN 定义为 approved Proposal / Execution Plan / Goal 的运行时翻译，而不是第二套 architecture。冻结顺序与 Bridge 当前合同一致：

`approved package + durable Critic result -> GPT Planner writes V2 PLAN -> self-check -> CURRENT last: PLAN_REQUESTED -> PLAN_FROZEN -> Executor`

同时：

- V2 PLAN 必须保留 Positive completion、Non-substitutable semantics、G1–G7、replay、scope、version 和 out-of-scope；
- task-local PLAN 无权覆盖 canonical execution package；
- Executor 不得自己创建/编辑 PLAN 给自己授权；
- 初次 freeze 不增加 `plan_revision`；
- 若 metadata 尚未远端发布，只允许先发布 REQUEST/CURRENT control metadata，然后等待 Planner。

没有发现需要修改 Bridge Kit 的缺口。

## Recovery R3 — durable Critic PASS locator

机制设计：PASS；当前 verdict：REVISE。

固定路径：

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md`

足以成为 repo 内可达的 durable review locator，而且不需要新增 schema、ledger、database 或 Bridge workflow。

本轮实际结论必须保留为：

`RESULT = REVISE`  
`READY_FOR_CODEX = NO`

只有 Planner 修完下面两个 blocker、形成新的明确 package commit，并由独立 Critic 重新审核后，才能把该 durable locator 更新为 PASS。

## Blockers

### FINDING_ID = FD-ER-R01 EXISTING_TASK_RECOVERY_STILL_AUTHORIZES_CREATION

**requirement**

v0.2 是 existing-task recovery。所有 normative execution authority 都必须只允许收养/继续现有 exact reviewed branch + sibling worktree；不得在后续 Executor phase 重新授权创建 branch/worktree，也不得留下可能被理解为 second bootstrap / raw worktree recreation 的合同。

**direct evidence**

- Execution Plan v0.2 开头仍写：只有 Critic PASS + 用户发送 Kickoff 后，才允许“创建上述分支/工作树并启动 Executor”。
- Canonical Goal v0.2 的 Executor phase 仍明确列出：
  - “创建 exact branch: reviewed/web-development--frontend-design-production-consolidation”
  - “创建 exact worktree: /home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation”
- 同一 Goal / Kickoff 其它 recovery 段又明确说明该 branch/worktree 已由 first bootstrap 创建，并禁止 second bootstrap、move/remove/recreate。

**causal risk**

这给 Executor 两套相反 authority：一套要求收养现有 task，另一套又明确授权“创建” exact branch/worktree。Codex 在 worktree 缺失、metadata 不完整或 resume 失败时可能据此尝试第二次创建，而不是 fail closed / `materialize-worktree --mode resume`，重新制造本轮正要消除的控制面事故。

**minimal closure condition**

只修 execution contract wording，不改 Frontend architecture：

1. Plan 开头把“允许创建上述分支/工作树”改成“允许按 recovery contract 收养/继续现有 reviewed branch/worktree，并在 PLAN_FROZEN 后启动 Executor”。
2. Goal Executor phase 删除“创建 exact branch/worktree”，改为“继续使用 recovery preflight 已收养的 exact branch/worktree”。
3. 若 existing worktree 以后确实丢失，只允许当前 Bridge artifact-bound `materialize-worktree --mode resume`；不得 second bootstrap/raw add。
4. 与版本判断有关的“创建 execution branch 时”改为不会暗示重新建 branch 的当前 release-baseline表述即可。

**owner**

Planner.

### FINDING_ID = FD-ER-R02 V02_PACKAGE_STILL_POINTS_TO_SUPERSEDED_V01_PLAN

**requirement**

Plan / Goal / Kickoff 必须是同版 execution authority。v0.2 recovery 后，任何 normative implementation / Gate / validation locator 必须指向 Execution Plan v0.2；v0.1 只能作为历史事故说明，不能继续作为执行依据。

**direct evidence**

- Canonical Goal v0.2 的 Capability Gates 仍写：
  “同一 final candidate 必须直接通过 Execution Plan v0.1 的 G1–G7”。
- Kickoff v0.2 Generator contract 仍写：
  “按 Plan v0.1 实现”。
- Kickoff v0.2 broad regression 仍写：
  “最低 broad commands 见 Plan v0.1 Phase D”。

v0.1 恰好是本轮已经判定存在旧 `/tmp` worktree、task-local PLAN handoff 缺口和无 durable Critic locator 的 superseded execution package。

**causal risk**

Executor 或后续 task-local Planner 被正式 Kickoff 导向 v0.1，会出现两个 execution authority。即使 G1–G7 产品语义本身没变化，读取 v0.1 的其它段落仍可能重新带回已经废弃的 worktree/control-plane 语义，并破坏“v0.2 exact package + durable Critic PASS”这一恢复目标。

**minimal closure condition**

- Goal v0.2 的 G1–G7 locator 改为 Execution Plan v0.2。
- Kickoff v0.2 的 Generator contract 和 Phase D locator 都改为 Plan v0.2。
- 对 Plan/Goal/Kickoff 做一次 targeted search：规范性 `Plan v0.1` / `Execution Plan v0.1` 引用清零；只保留明确标注为历史事故说明的 v0.1 文本。
- 不改变 G1–G7、coordinator-first、replay、maturity 或版本方向。

**owner**

Planner.

## Non-blocking notes

1. Package commit `3d8669f52680f63f76ce537335fbee6019e4d5a9` 之后 latest main 只新增了本轮 Critic prompt；未发现 Frontend recovery package 的后续 semantic drift。
2. 当前 main 版本仍是 repository `5.3.0`、`web-development 0.2`。v0.2 recovery docs 自身不 bump；若最终 production implementation 完成且 release gates PASS，当前基线下仍是 repository `5.3.1`、`web-development 0.3`、其它 central plugins NO_BUMP、maturity 保持 `unclassified`。
3. 远端当前仍未发现 `reviewed/web-development--frontend-design-production-consolidation` branch；这与“first-bootstrap metadata 尚未发布”的 recovery 场景兼容，不是单独 blocker。真实 machine-local branch/worktree clean/base 仍必须由 Kickoff recovery preflight 核实，Critic 不伪称从 GitHub surface 已验证本机状态。
4. Maintenance Board 不因本次 Critic REVISE 自动改变状态；本 review artifact 不是 Project 状态同步。

## Scope preserved

本轮没有重新打开，也没有修改：

- Frontend Design Proposal v0.3；
- coordinator-first；
- P0–P4；
- F-A/F-B/F-C/F-D；
- G1–G7 产品语义；
- Bobbio/Lucerna/Asteria replay；
- maturity attribution；
- Product UI Copy / Clear Writing deferred scope；
- final version direction；
- Bridge Kit source。

只有 execution package 的 recovery/control-plane parity 仍需最小返修。
