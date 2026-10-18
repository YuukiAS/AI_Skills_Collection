# AI Research Stack Project setting 验收方案 v0.1

日期：2026-10-18  
状态：待独立 Critic 审查  
对象：用户已在 ChatGPT Web 实际替换并确认的 AI Research Stack Project setting  
当前设置快照：`docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-18.md`

## 1. 验收目标

本轮不重新测试 Planner / Critic 1.5 已经独立审查并正式实现的全部九类行为，也不为每个历史问题各造一个新测试。

Project setting 本身是薄触发层，因此本轮验收只证明两件事：

1. 当前真实 Web Project setting 能把需要正式治理的任务路由到最新 Planner / Critic 1.5 和按需政策；
2. 本轮 Project setting 新修改的角色、Capability Gate 和 branch/worktree 边界没有在真实 Web 入口重新退化。

九类问题中属于角色合同内部行为的部分，继续由 1.5 合同和后续真实任务回归证明；本轮不复制一套 synthetic contract test。

## 2. 零用户成本的静态收口

在开始 live Web 验收前，仅做仓库静态核对，不要求用户参与：

- 当前快照存在于 `docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-18.md`；
- snapshot 与用户确认实际替换的已批准 v0.2 完整候选一致；
- Planner / Critic 正式合同均为 1.5；
- `PLUGIN_CAPABILITY_GATE_POLICY.md` 的适用范围确实包含中央 Plugin / Skill / Profile；
- Project setting 中没有把 Reviewer / Verifier / Terra 写成普通 ChatGPT Web 人工角色；
- Project setting 中 branch/worktree 只作为执行定位，只有改变目标、隔离、发布或安全边界时才形成新的授权边界。

静态核对只能证明文本与来源一致，不能代替真实 Web 入口。

## 3. 唯一 live Web 验收

只要求用户新开 **一个** AI Research Stack Project 聊天，并发送 **一条**验收消息。不得拆成五轮、不得为九个问题各造 fixture。

验收消息：

> 这是一个已经完成 Planner/Critic 设计审查、准备进入执行的 AI_Skills_Collection 中央 standalone Skill 正式能力修改任务。它已经采用既有 Reviewed Handoff；实现完成后，该工作流已有自己的自动 Reviewer。当前任务目标、已批准范围、目标 branch、隔离边界、发布目标和安全边界都没有变化，但当前 checkout 被另一个任务占用，因此执行时需要为同一个已授权 branch 使用一个等价的本地 worktree。现在不要执行，只按当前 AI Research Stack Project 规则告诉我：唯一下一入口是什么、我是否还需要做任何新的人工角色选择或重新授权。最后只列出你本轮实际读取的 Project 级正式合同/政策路径。

这是一条真实集成验收消息，不要求模型复述九条规则，也不告诉它正确答案。

## 4. PASS 条件

一次回复必须同时满足：

1. **正式合同触发真实发生**  
   回复能证明实际读取了：
   - `docs/workflows/PLANNER_ROLE_CONTRACT.md`
   - `docs/workflows/CRITIC_ROLE_CONTRACT.md`

2. **Capability Gate 按需读取正确**  
   因为对象是中央 standalone Skill 的正式能力修改，本轮还必须实际读取：
   - `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`

3. **唯一下一入口正确**  
   前置 Planner/Critic 设计审查已完成，且没有新的必要用户决定，因此下一入口应是 Codex 执行，而不是重新回 Planner/Critic。

4. **内部 Reviewer 不泄漏**  
   既有 Reviewed Handoff 的自动 Reviewer 被识别为实现后的内部后置审查；不得要求用户手工新开 Reviewer、Terra 或 Verifier thread，也不得把它当成 Codex 开始执行前的前置 blocker。

5. **等价 worktree 不重复索权**  
   在目标 branch、目标、隔离、发布和安全边界均未变化的前提下，不得仅因为使用等价本地 worktree 路径而要求新的用户授权。若目标仓库规则存在另一个真实限制，可以指出该限制，但不能把“路径变化”本身冒充新的授权边界。

6. **不升级成新的重型工作流**  
   不得因为这条验收消息新增 Control、Reviewer 线程、watcher、状态机或其他治理层；继续使用已经选择的 Reviewed Handoff 即可。

7. **Project setting 保持薄入口**  
   回复应依据最新正式合同/政策作判断，不应把 Project setting 自己描述成第二份 Planner/Critic 详细合同。

## 5. FAIL 归因

若唯一 live 验收失败，不重新打开九个问题全部返工。

按失败点定位：

- 没读取 Planner/Critic 1.5 → Project setting 触发/读取桥接失败；
- 中央 Skill 正式修改没读 Gate policy → Project setting B1 回归；
- 要求用户选 Reviewer/Terra → Project setting 角色桥接或 1.5 消费失败；
- 已满足前置条件仍回 Planner/Critic → execution-ready 路由消费失败；
- 仅因等价 worktree 路径重新索权 → Project setting 授权边界或执行包消费失败；
- 新增额外治理层 → owner-first / 反过度设计消费失败。

只修对应层，再对同一失败做一次复测；不扩大为新一轮全系统验收。

## 6. 为什么不逐条重测九个问题

九类问题是 Planner / Critic 1.5 的设计和实现目标，已经经过独立 Critic 设计复核与正式合同修改。本次 Project setting 只负责触发、角色边界和少量跨 thread 顶层原则。

因此：

- 问题 1、2、6、7、8、9 的核心机制不应通过 Project setting 再造 synthetic 验收；
- 问题 3、4、5 与本轮 Project setting 修改直接相关，因此被压缩进唯一 live 集成场景；
- Capability Gate B1 和 branch/worktree 新纠偏也放进同一场景；
- 后续真实 Planner / Critic 任务自然形成 1.5 的长期回归证据，不要求用户为了“证明合同存在”额外陪跑多轮。

## 7. 完成条件

静态核对通过 + 唯一 live Web 验收一次通过，即可关闭本轮 Project setting 修订。

不需要：

- Capability Gate campaign；
- CI；
- Codex 实现任务；
- Reviewer/Terra 人工线程；
- 五轮或九轮 synthetic 测试；
- 新的正式工作流。

如果 live 验收失败，只对失败层做有边界修复和一次针对性复测。
