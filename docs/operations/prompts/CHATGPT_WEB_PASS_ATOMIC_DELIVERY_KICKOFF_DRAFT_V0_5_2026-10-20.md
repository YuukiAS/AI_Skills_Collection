# Kickoff Draft v0.5 — chatgpt-web--pass-integrity

状态：DRAFT ONLY；当前未授权实施。

## Authority

- Proposal:
  `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_5_2026-10-20.md`
- Execution Plan:
  `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_EXECUTION_PLAN_V0_5_2026-10-20.md`
- Canonical Goal:
  `docs/goals/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_GOAL_V0_5.md`
- Critic review authority:
  `results/chatgpt-web--pass-integrity/PASS_ATOMIC_DELIVERY_V0_4_CRITIC_REVIEW_2026-10-20.md`

只有同一独立 Critic 对完整 v0.5 execution package 给出唯一 execution-ready `PASS` 与 `READY_FOR_CODEX=YES`，并由用户实际发送批准后的短 handoff，才允许启动。

## 执行任务

在 `YuukiAS/AI_Skills_Collection` 中实现 Planner/Critic 1.8 的最小治理修复：

1. Planner Role Contract 1.7 → 1.8；
2. Critic Role Contract 1.7 → 1.8；
3. 更新 ChatGPT Web collaboration regression 记录；
4. 仅在真实正向回归成功后，把该 PASS 案例补入优质 Critic 示例；
5. 保存 `results/chatgpt-web--pass-integrity/**` 回放与回归证据。

## 1.8 必须实现的语义

Planner：
- execution-ready task-specific Critic prompt 必须通过中央 compatibility preflight；
- Planner 必须能从冻结 Goal/Kickoff/授权边界生成短 Codex handoff，否则 package 不可送最终审查。

Critic：
- execution-ready 审查先做 task-prompt compatibility hard gate；
- 有冲突时不得 PASS，但继续检查其余可检查内容；
- PASS 必须同一回复一次交齐架构说明、approved locators、`READY_FOR_CODEX=YES`、`NEXT_HANDOFF=CODEX`、短 `COPY TO CODEX`；
- 缺任一项不得先 PASS 后补；
- PASS 后 follow-up 区分解释请求、矛盾证据、新要求。

## 回放与最终真实回归

先运行 deterministic compatibility replay。

第一阶段：
- exact old Clear Writing package：
  `d7b810d194ead881303aaca9c2e4f1d59a97c1f1`
- 作为兼容性负控；
- 必须因旧 task-specific prompt 与中央合同冲突而 REVISE。

第二阶段只在第一阶段通过后准备：
- Clear Writing branch：
  `design/clear-writing--single-entry-artifact-finalization`
- 只允许最小修正 task-specific execution-ready Critic prompt 和必要 locator/package identity；
- 产品 Proposal/Plan/Goal/Runbook/Kickoff 产品语义、G1-G6、生产代码均不得改变；
- 必须形成新的 exact package commit；
- 独立 Critic 对新 package 做完整 execution-ready review；
- 不预设 PASS；发现产品 blocker 就正常 REVISE。

若新 package 真正 PASS，再用自然问题：

`写入 repo 的文件怎么保证确实走了 Clear Writing？`

验证只解释 approved G3，不临场新增 `create_blob`、MCP、App、网关或新 Gate。

## 允许修改

中央治理：
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`
- `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md`
- `results/chatgpt-web--pass-integrity/**`

正向回归准备：
- Clear Writing 设计分支上的 task-specific execution-ready Critic prompt；
- 必要的机械 locator/package identity 更新。

## 禁止

- 不修改当前 Project setting；
- 不修改 `PLUGIN_CAPABILITY_GATE_POLICY.md`；
- 不修改 Clear Writing 产品架构、生产代码或 G1-G6 产品语义；
- 不修改 Bridge Kit / Plugin Creator；
- 不创建新角色、schema、状态机、数据库、服务、watcher、daemon 或统一 prompt compiler；
- 不运行 Clear Writing G1-G6 产品 Gate；
- 不修改 Personal Plugin；
- 不调用付费模型；
- 不合并 main/release；
- 不 force/destructive Git。

## 停止条件

以下任一出现立即停止并回 Planner：

- 1.8 必须修改 Project setting 或 Capability Gate Policy 才能成立；
- 需要新的治理运行系统；
- 正向回归 package 需要改变 Clear Writing 产品语义；
- 无法从批准包生成短 Codex handoff而不猜测或扩权；
- compatibility replay 对旧冲突 prompt 不能稳定拒绝。

普通文档实现错误留在同一 Codex task 修复。

README checked: no update required。
