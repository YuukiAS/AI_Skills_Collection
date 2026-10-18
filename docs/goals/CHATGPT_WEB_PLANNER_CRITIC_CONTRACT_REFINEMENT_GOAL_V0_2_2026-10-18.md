# ChatGPT Web Planner / Critic 合同完善 Goal v0.2

日期：2026-10-18  
任务：`chatgpt-web--planner-critic-contract-refinement`  
设计依据：`docs/design/chatgpt-web-collaboration/PLANNER_CRITIC_CONTRACT_REFINEMENT_V0_2_2026-10-18.md`  
实施计划：`docs/design/chatgpt-web-collaboration/PLANNER_CRITIC_CONTRACT_REFINEMENT_EXECUTION_PLAN_V0_2_2026-10-18.md`

## 目标

将已通过独立 Critic 设计复核的 v0.2 规则忠实整合进两份现有角色合同，使 ChatGPT Web 的 Planner / Critic 协作直接覆盖 2026-10 记录的九类问题，同时不新增工作流、角色、状态机或运行实现。

## 必须修改

只允许修改：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`

两份合同版本从 1.4 升到 1.5，日期更新为 2026-10-18。

## 必须实现的语义

### Planner 合同

忠实实现批准方案 P1–P7：

- 简单连续的人类版本与机器 locator 分离；
- 会改变工作方式的设计在送审前能回答正常使用六问；
- owner-first 和反过度设计；
- ChatGPT Web 人工角色只有 Planner / Critic，Codex 是批准后的执行入口；
- 非终态必须给唯一下一用户入口；
- Codex kickoff 前关闭 Planner / Critic / 必要用户选择等前置依赖；
- 正常 task-local read / 环境确认 / 安全 preflight 仍允许；
- 既有重型工作流的实现后 Reviewer / Terra / Verifier 后置审查不阻止 kickoff；
- 机制级真实失败做有限的一跳同因果邻域检查；
- 复杂设计送 Critic 时给短的用户关键决定摘要。

### Critic 合同

忠实实现批准方案 C1–C9：

- Critic 是 ChatGPT Web 唯一人工独立审查角色，Codex 不是第三个人工角色；
- Reviewer / Verifier / Terra 只按既有重型工作流协议工作，不要求普通用户手工选择；
- 增加正常用户路径反证；
- PASS 明确“本次批准什么 / 不代表什么”；
- 所有实质 PASS 都给比例化的用户关键机制说明；
- REVISE / 非终态给唯一下一用户入口和完整可复制 prompt；
- `READY_FOR_CODEX=YES` 前关闭 Codex 实质执行所需的 Planner / Critic / 必要用户前置依赖；
- 正常 task-local read / preflight 允许，既有后置 Reviewer 不构成前置 blocker；
- 机制 blocker 关闭前做有限一跳同因果检查；
- 新控制层或跨 owner 修改必须有正面必要性证明；
- 审查新的人类版本是否使用简单连续形式。

## 不得修改

不得修改：

- `workflow-core`；
- 任何 Plugin / Skill；
- Bridge Kit；
- Reviewed Handoff / Control；
- Reviewer / Verifier / Terra 机器协议；
- AI Research Stack Project setting；
- GitHub Project schema；
- AGENTS / README；
- 任何其他运行实现。

不得新增：

- 新的 ChatGPT Web 人工角色；
- 新的 PASS 状态枚举；
- execution segment；
- review protocol；
- watcher / daemon / database / state machine / controller。

## 执行真实性

在用户发送经 Critic 批准的 kickoff 时，本 Goal 不再保留需要 Planner / Critic 决定的设计问题。Codex 应能够在现有 canonical checkout 的 `main` 上直接开始批准范围内的合同编辑。

Codex 可以先读取 source、确认环境和做安全 preflight，但不得以这些步骤为由重新打开设计，或先 probe 后才发现本应在 kickoff 前解决的核心范围、角色、权限或产品选择。

如果实施过程中发现批准的 v0.2 本身存在无法无歧义实现的缺口，或必须修改第三个文件，停止并返回 Planner。

## Git 与授权边界

用户发送 approved kickoff 后授权：

- 修改上述两份合同；
- 运行相称的本地/只读 deterministic 验证；
- 提交仅包含两份合同的 commit；
- 验证后普通非强制 push 当前 `main` 到 `origin/main`。

不授权 branch/worktree 创建或切换、force push、rebase/autostash、reset/clean/restore、remote mutation、PR/release/deploy、付费调用、私有数据传输或 scope expansion。

## 验收

最终必须证明：

1. 两份合同均为 1.5；
2. v0.2 的九类问题覆盖语义均进入正式合同；
3. B1：只有 Planner / Critic 是 ChatGPT Web 人工角色，Codex 是执行入口；Reviewer / Verifier / Terra 仍仅为既有重型流程内部角色；
4. B2：Codex kickoff 前置依赖门成立；正常 read/preflight 不被禁；既有实现后 Reviewer 不误伤；
5. 所有实质 PASS 均需比例化解释用户真正批准的关键机制；
6. 非终态不会只报状态而不给下一入口；
7. owner-first、有限同因果检查、简单版本规则均进入现有合同；
8. implementation commit 只修改两份合同；
9. 没有新增角色、状态机、自动化或运行机制；
10. `git diff --check` 与相称文档检查通过。

完成后，最终回复先用自然中文说明用户实际获得了什么变化，再给必要 commit / 验证信息。
