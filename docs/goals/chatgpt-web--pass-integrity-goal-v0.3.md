# Canonical Goal v0.3 — chatgpt-web--pass-integrity

## 目标

在 `YuukiAS/AI_Skills_Collection` 中按已批准 Proposal v0.3 和 Execution Plan v0.3，实现 ChatGPT Web Planner–Critic 的 PASS 可信度修复。

最终结果必须使：

1. 中间设计审查只有 `PROCEED / REVISE`；
2. Critic 级 `PASS` 只在 execution-ready 最终审查出现一次，并与 `READY_FOR_CODEX=YES` 同时成立；
3. 唯一 PASS 前重新对照完整用户承诺、Proposal/Plan/Goal/Kickoff 和正常用户路径；
4. 唯一 PASS 后若冻结语义需要实质改变，原批准对修改后的语义失效，同一 task 回 Planner；
5. 普通实现缺陷默认 `RETURN_TO_CODEX`；
6. 实现后最终评估前独立安全门继续存在，使用 `PROCEED_TO_FINAL_EVALUATION / REVISE`；
7. Capability Gate 同时要求正向能力、跨组件完整成功链和风险匹配关键失败链；
8. Planner/Critic 每轮先给可独立阅读的一屏中文摘要，再给机器 handoff；
9. Clear Writing 可用时只检查用户摘要的最终表达，绝不改写机器交接。

## 必须修改

- `docs/workflows/PLANNER_ROLE_CONTRACT.md` → 1.7
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` → 1.7
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` → 1.2
- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`
- 新增完整 Project setting clean candidate，依据冻结 delta 和实施时最新已生效快照生成

## 不得修改

- Bridge Kit / Slurm Workflows / Delivery Assurance / workflow-core / Clear Writing 产品实现
- 根 README、Marketplace、Plugin/Skill runtime、VERSION、正式 release
- live ChatGPT Project setting

## 必须验证

- Bridge 错误链：机器级 Notifier 不能被 repo-local 配置替代；Persistent→Notifier 必须作为跨组件承诺被端到端要求；ETA 不能只靠 UNKNOWN 获得能力成立。
- Slurm 错误链：若 Hook runtime 无法启动，安全承诺必须要求正常入口直接证明危险底层动作没有执行。
- 普通实现错误仍回同一 Codex task，不因失败本身重新设计。
- 用户摘要无需阅读 finding/locator/handoff 即可理解本轮结论、变化、产品影响、剩余问题、是否需动作和下一入口。

## 完成边界

实现提交后不得自报 Critic PASS。下一步进入实现后独立安全门；只有其 `PROCEED_TO_FINAL_EVALUATION` 后才做最终新鲜场景评估。最终成功使用 `CANDIDATE_ACCEPTED`，不是第二次 Critic PASS。
