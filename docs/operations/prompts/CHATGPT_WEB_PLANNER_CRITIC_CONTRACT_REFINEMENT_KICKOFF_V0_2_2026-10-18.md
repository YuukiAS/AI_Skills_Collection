# Codex Kickoff Draft — ChatGPT Web Planner / Critic 合同完善 v0.2

在独立 Critic 对本执行包给出 execution-ready PASS 后，将下面正文逐字发送给 Codex。

---

执行 `YuukiAS/AI_Skills_Collection` 的 ChatGPT Web Planner / Critic 角色合同完善任务。

任务：
`chatgpt-web--planner-critic-contract-refinement`

批准设计：
`docs/design/chatgpt-web-collaboration/PLANNER_CRITIC_CONTRACT_REFINEMENT_V0_2_2026-10-18.md`

实施计划：
`docs/design/chatgpt-web-collaboration/PLANNER_CRITIC_CONTRACT_REFINEMENT_EXECUTION_PLAN_V0_2_2026-10-18.md`

Canonical Goal：
`docs/goals/CHATGPT_WEB_PLANNER_CRITIC_CONTRACT_REFINEMENT_GOAL_V0_2_2026-10-18.md`

只修改：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`

把两份合同从 1.4 升到 1.5，并忠实实现已经批准的 v0.2；不要重新设计。

执行前先读取当前 `main` 的 AGENTS、上述批准设计、实施计划、Goal 和两份现行合同。使用机器上现有的 `YuukiAS/AI_Skills_Collection` canonical checkout；确认当前分支为 `main`、remote 正确、工作区状态允许安全修改。不要创建或切换 branch / worktree。

本次 kickoff 已授权你直接开始当前批准范围内的实质编辑。不要只做 read / inspect / probe 后再把已批准的设计问题退回 Planner/Critic。正常 source read、环境确认和安全 preflight 可以做，但只用于执行已经冻结的合同修改。

必须保持以下边界：

- ChatGPT Web 人工协作角色只有 Planner 与 Critic；
- Codex 是批准后的执行入口，不是第三个人工角色；
- Reviewer / Verifier / Terra 只在既有 Bridge Kit / Reviewed Handoff / Control 等明确重型工作流中按原协议工作；
- 不新增 Reviewer，不要求普通用户手工选择 Reviewer / Terra，不修改其机器协议；
- Codex kickoff 前所需 Planner 决策、Critic 审查和必要用户产品/授权选择已经完成；
- 实现后的既有 Reviewer / Terra / Verifier 后置审查不是 kickoff 前置 blocker；
- 保留正常使用六问、PASS 范围与未证明边界、非终态唯一下一入口、所有实质 PASS 的比例化用户机制说明、有限同因果一跳检查、owner-first / 反过度设计、简单连续的人类版本规则；
- 不新增角色、PASS 状态枚举、execution segment、review protocol、watcher、daemon、数据库、状态机或控制层。

明确禁止修改：

- `workflow-core`；
- 任何 Plugin / Skill；
- Bridge Kit；
- Reviewed Handoff / Control；
- Reviewer / Verifier / Terra 机器协议；
- AI Research Stack Project setting；
- GitHub Project schema；
- AGENTS / README；
- 任何其他运行实现。

验证至少包括：

1. 完整重读两份修改后的合同；
2. 确认版本均为 1.5、日期为 2026-10-18；
3. `git diff --check`；
4. 对照批准设计检查 P1–P7、C1–C9 均有唯一合同落点；
5. 专门验证 B1、B2；
6. 确认没有新增角色/状态机/审查协议；
7. 确认 implementation diff 只包含两份合同；
8. 对新增中文做读者可读性检查，不用内部术语堆砌代替含义。

这是 Markdown 合同修改，不要求无关全仓重型 CI；若存在直接适用的轻量 deterministic 文档检查可以运行。

验证通过后提交只包含两份合同的 commit，并普通非强制 push 当前 `main` 到 `origin/main`。本 kickoff 不授权 force push、rebase/autostash、reset/clean/restore、remote mutation、branch/worktree 操作、PR/release/deploy、付费调用、私有数据传输或 scope expansion。

如果实施过程中发现 v0.2 无法无歧义落入现有合同，或必须修改第三个文件，停止并返回 Planner，不自行扩项。

完成后用自然中文说明：两份合同具体怎样完善、九类问题分别由什么规则解决、B1/B2 如何保持、哪些层明确没有修改，并给出 implementation commit 和验证结果。
