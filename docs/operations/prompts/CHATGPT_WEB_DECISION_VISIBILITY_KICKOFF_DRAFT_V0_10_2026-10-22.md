# Planner–Critic 1.8 v0.10：启动范围草案（尚未授权）

任务：`chatgpt-web--pass-integrity`；日期：2026-10-22。
现阶段仅设计审查；下文不是用户的 Codex 执行消息，没有任何现成 `PASS`。
目标仓库：`YuukiAS/AI_Skills_Collection`。
当前设计分支：`design/chatgpt-web--pass-integrity-v0-4`。
正式 main 合同仍为 Planner/Critic 1.7；目标待审升级仍叫 1.8（不是新发行 1.0）。

## 唯一当前设计包

全部从用户在 Critic 入口提供的同一准确 PACKAGE_COMMIT 读取：
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_10_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PLAN_V0_10_2026-10-22.md`
- `docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_10.md`
- 本草案。
还必须查看独立设计审查结论，之后由 Planner 准备完整 execution-ready 包。不得拿旧 v0.7/v0.9 或错误扩项 v1.0 文件充当当前 approved source。

## 若之后通过完整执行就绪审查，预定最小修改

- `docs/workflows/PLANNER_ROLE_CONTRACT.md`：落实当前用户决策说明、每轮变更与上轮审查接收职责；最终 Critic 技术 PASS 后同一 Planner 完成用户交付核对和短 Codex prompt。
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`：独立对照用户说明和真实机制；每轮明确 PROCEED/REVISE/PASS 的原因、保留与待证事项；唯一 PASS 仍由 Critic 审技术但下一入口变为现有 `NEXT_HANDOFF=PLANNER` 以进行交付核对；无需第三个角色或新机器状态。
- 既有 `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`：补充真实用户交付失败和跨轮说明被遗忘的原始证据。
- 既有 `results/chatgpt-web--pass-integrity/**`：实际用户/机器输出及正常使用回归；不添加与现有证据重复的状态存储。

保留原 1.8 的 Prompt兼容、关键真实接口核验、非终态唯一下一入口、同候选与最终版本证据、实现后 Critic 安全门、正式 main 集成/readback。需求本身的可读性不是判断技术准确性的唯一依据。

## 必须真实核对的效果

模型面对不含逐条“说人话”提醒的正常真实设计，主动形成可审的用户方案说明；Critic 能发现与真实技术不一致的重要选择；下一 Planner在接收质量差的 Critic 回复时，能够从已经受审的 source 和独立事实进行有界补正，不能机械把 status 直接交给 Codex；缺少有效独立技术证据时则确实停止推进。

一次完成完整 `Planner → Critic REVISE → Planner修订 → Critic复审` 的连续试用；另有一次能真实到达独立技术 PASS 的批准案例（不能强迫任何有缺陷案例 PASS）。用户摘要有无信息价值必须独立看全文，不以关键词、字数、prompt token、机器状态或读过 Clear Writing 代替。正式源安装之后仍需真实新任务默认入口验证。测试必要范围和次数由最终 Critic 按风险冻结，不无限调参。

## 权限、边界与失败路由

本轮不能实施。之后任何已批准 Codex 入口均不得修改 AI Research Stack Project setting、Capability Gate Policy、Bridge Kit、Mica、Slurm、Clear Writing 产品、Plugin Creator 或其他生产代码；不得启动付费模型、生产服务器/Slurm mutation、账户/浏览器扩展或增加新的审核引擎。README 只按最终实际文件变化检查。

本方案相对 1.7 的正式执行就绪 PASS 用户交接语义有实质变化，**必须由独立 Critic 最终审完全同版提案/计划/Goal/本 Kickoff**，不能把这一决定留给 Codex。用户是否接受多一次最终机械转发的成本，也属于此次独立设计 Critic 需直接评价的问题。未独立通过前，不要求用户执行，也不得宣布 1.8 可用。

普通实现错误：同一 Codex 修；独立专业审查材料本身不足：返回原 Critic 真正补审；架构/权限/验收/恢复语义变化：回 Planner 并重新走独立审查；当前 Planner 可以自己完成的归档、说明整理、包更新不能丢回用户。
