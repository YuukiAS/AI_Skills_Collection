# Kickoff Draft v0.3 — chatgpt-web--pass-integrity

状态：仅供 execution-ready Critic 审查；当前未授权实施。

## Authority

- Proposal:
  `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_3_2026-10-19.md`
- Execution Plan:
  `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_EXECUTION_PLAN_V0_3_2026-10-19.md`
- Goal:
  `docs/goals/chatgpt-web--pass-integrity-goal-v0.3.md`
- Project setting delta:
  `docs/project-settings/AI_RESEARCH_STACK_PASS_INTEGRITY_PROJECT_SETTING_DELTA_V0_3_2026-10-19.md`
- Regression closure plan:
  `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_REGRESSION_CLOSURE_PLAN_V0_3_2026-10-19.md`

## 执行范围

用户在 Critic 唯一 execution-ready PASS 后实际发送短 handoff 时，授权 Codex 在同一任务分支完成以下 bounded 文档/治理实现：

- 修改 Planner Role Contract 至 1.7；
- 修改 Critic Role Contract 至 1.7；
- 修改 Plugin Capability Gate Policy 至 1.2；
- 追加 ChatGPT Web collaboration regression closure；
- 依据实施时最新已生效 Project setting 快照和冻结 delta 生成完整 clean candidate；
- 做 Execution Plan 中的静态一致性检查和三组合同语义回放；
- task-owned add/commit 与普通 non-force push。

## 明确禁止

- 不修改任何 Bridge Kit、Slurm、Delivery Assurance、workflow-core、Clear Writing 产品代码；
- 不修改 Marketplace、Plugin/Skill runtime、VERSION 或 release；
- 不修改 live ChatGPT Project setting；
- 不运行真实 Slurm、Gmail、付费模型 Gate；
- 不 force/destructive Git；
- 不自行合并 main/release；
- 不新建第三人工角色、数据库、watcher、daemon、requirements ledger 或新状态机。

## 停止条件

若实现只暴露普通文档 bug、一致性问题或冻结范围内回归，自己修复后继续。

只有发现必须改变 Proposal v0.3 的用户承诺、架构/canonical owner、权限、Gate 成功定义或 recovery semantics 时停止，并报告：原 execution-ready PASS 对修改后的语义失效，保持同一 task_key 回 Planner。
