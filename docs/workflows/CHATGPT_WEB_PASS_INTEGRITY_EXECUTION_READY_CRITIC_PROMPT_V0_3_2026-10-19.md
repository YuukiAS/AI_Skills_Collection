# Execution-ready Critic prompt v0.3 — chatgpt-web--pass-integrity

你现在担任 AI Research Stack 的独立 Critic，对 ChatGPT Web PASS 可信度与用户控制修复做唯一一次 execution-ready 最终审查。

## Active Review Context

target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=ChatGPT Web collaboration governance / Planner-Critic / Capability Gate
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=work/chatgpt-web--pass-integrity
package_commit=ce8bc133987547e354af5e5c1213a7984a9ad3db
package_design_base=main@9740a593c1622bce61401c8215c621f8cdb7d93a
review_stage=EXECUTION_READY_REVIEW_V0_3

审查对象必须全部从 exact package commit
`ce8bc133987547e354af5e5c1213a7984a9ad3db`
读取：

- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_3_2026-10-19.md`
- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_EXECUTION_PLAN_V0_3_2026-10-19.md`
- `docs/goals/chatgpt-web--pass-integrity-goal-v0.3.md`
- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_KICKOFF_DRAFT_V0_3_2026-10-19.md`
- `docs/project-settings/AI_RESEARCH_STACK_PASS_INTEGRITY_PROJECT_SETTING_DELTA_V0_3_2026-10-19.md`
- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_REGRESSION_CLOSURE_PLAN_V0_3_2026-10-19.md`

先读取最新 main 的 AGENTS、Planner/Critic Role Contract、Plugin Capability Gate Policy、AI Skills Maintenance Board、当前已生效 Project setting 快照，再读取上述完整 package。若 main 已前进，只把真正会改变本执行包正确性的新增事实带入审查，不因无关 main 提交机械失效。

## 本轮唯一允许的 Critic verdict

- `PASS`：只在所有 execution-ready 条件完整闭合时允许；必须同时 `READY_FOR_CODEX=YES` 并生成短 Codex handoff。
- `REVISE`：任一会改变用户承诺、架构、配置归属、调用关系、权限、验收、恢复或执行语义的空白仍存在。

本轮禁止 `PROCEED`。这是本设计—执行闭环唯一可能出现 Critic PASS 的位置。

## 必须重新完整审查，不得只看上一轮 blocker

逐项检查 Proposal v0.3 的完整用户承诺是否都被 Execution Plan / Goal / Kickoff 覆盖：

1. 中间设计审查只有 PROCEED / REVISE。
2. 唯一 PASS 与 READY_FOR_CODEX=YES 绑定。
3. PASS 后 Codex 不需要自行决定任何产品/架构/权限/验收/恢复语义。
4. 实现后最终评估前独立安全门仍存在，但 verdict 为 PROCEED_TO_FINAL_EVALUATION / REVISE。
5. PASS 后冻结语义若实质改变，旧 package/PASS 不再覆盖修改后的语义，同 task 回 Planner。
6. 普通实现 bug、漏接、配置 scope、runtime/loader、测试/CI/冻结 Gate failure 默认 RETURN_TO_CODEX。
7. Capability Gate 同时覆盖正向能力、跨组件成功链、风险匹配关键失败链。
8. 每轮 Planner/Critic 先有可独立阅读的一屏中文用户摘要，再有机器交接。
9. Clear Writing 只检查用户摘要的最终表达，不改写机器 handoff。
10. 不新增第三人工角色、数据库、watcher、daemon、ledger、状态机或产品层修改。

## 用两个真实事故问穿执行包

### Bridge

必须能够从合同直接判断以下 execution-ready package 不得 PASS：

- 把机器级共享 Notifier 改成每 repo 配邮箱；
- Persistent Run 与 Notifier 各自有实现但没有完整调用链；
- ETA 只规定 UNKNOWN fallback，却没有任何正常场景要求 ETA 真正出现。

### Slurm

必须能够从合同直接判断以下 execution-ready package 不得 PASS：

- Hook checker 单独可用；
- 正常 Codex Hook runtime 启动失败；
- Gate 没有直接证明此时危险底层 scancel 不执行。

若上述任一仍可能获得 PASS，则 REVISE。

## 用户可读输出

回复先给一屏自然中文摘要，必须说明：

- 这次是否已经真正达到“可以交 Codex”的唯一 PASS；
- 相比 v0.3 设计阶段，本执行包新增冻结了什么；
- 这套规则以后怎样避免 Bridge/Slurm 类问题；
- 用户现在是否需要做任何事；
- 若 PASS，Codex 将修改哪些文件、明确不会碰哪些产品。

正式 Clear Writing 可调用时只对该摘要调用；不可用不得伪称调用。机器 handoff 保持原文。

## PASS 后短 Codex handoff

若且仅若 PASS，必须使用 exact locators：

```text
APPROVED_PROPOSAL_PATH=docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_3_2026-10-19.md
APPROVED_PLAN_PATH=docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_EXECUTION_PLAN_V0_3_2026-10-19.md
APPROVED_GOAL_PATH=docs/goals/chatgpt-web--pass-integrity-goal-v0.3.md
APPROVED_KICKOFF_PATH=docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_KICKOFF_DRAFT_V0_3_2026-10-19.md
APPROVED_COMMIT=ce8bc133987547e354af5e5c1213a7984a9ad3db
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
=== COPY TO CODEX BEGIN ===
执行同一任务 chatgpt-web--pass-integrity。严格读取上述 approved package commit，并按 Goal/Plan 修改三份中央合同、生成 Project setting clean candidate、追加 regression closure。允许 task-owned add/commit 和普通 non-force push；禁止修改 live Project setting、Bridge/Slurm/Delivery Assurance/workflow-core/Clear Writing 产品代码、正式 release 或 force/destructive Git。普通实现失败在同一 Codex task 内修复；只有冻结用户承诺、架构、权限、验收或恢复语义必须变化时才停止并回 Planner。
=== COPY TO CODEX END ===
```

若 REVISE，只给真实 blocker 和最小关闭条件，并自动生成下一 Planner prompt。
