# AI Research Stack Project setting 验收方案 v0.2

日期：2026-10-18  
状态：修订后待独立 Critic 复核  
对象：用户已在 ChatGPT Web 实际替换并确认的 AI Research Stack Project setting  
当前设置快照：`docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-18.md`  
前版：`docs/project-settings/AI_RESEARCH_STACK_PROJECT_SETTING_ACCEPTANCE_PLAN_V0_1_2026-10-18.md`  
修订范围：只关闭验收设计 blocker B1、B2；不重新设计 Project setting，不重新打开 Planner / Critic 1.5，不增加九项 synthetic 测试。

## 1. 验收目标

本轮不重新测试 Planner / Critic 1.5 已经独立审查并正式实现的全部九类行为，也不为每个历史问题各造一个新测试。

Project setting 本身是薄触发层，因此本轮验收只证明两件事：

1. 当前真实 Web Project setting 能把需要正式治理的任务路由到最新 Planner / Critic 1.5、按需 Capability Gate 政策、必要的 Bridge 规范和目标仓库规则；
2. 本轮 Project setting 新修改的角色、Capability Gate 和 branch/worktree 边界没有在真实 Web 入口重新退化。

九类问题中属于角色合同内部行为的部分，继续由 1.5 合同和后续真实任务回归证明；本轮不复制一套 synthetic contract test。

## 2. 静态收口

上一轮 Critic 已确认静态部分通过，本版不重新设计：

- `docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-18.md` 正文与获批 v0.2 完整候选逐字一致；
- Planner / Critic 正式合同均为 1.5；
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` 的适用范围覆盖中央 Plugin / Skill / Profile；
- 当前 main 与上一轮 acceptance plan 审查基线一致。

静态核对只能证明文本与来源一致，不代替真实 Web 入口。

## 3. Live Web 验收总量

用户只需要：

- 新开 **一个** AI Research Stack Project chat；
- 共发送 **两条**消息；
- 不需要 Codex 真执行；
- 不需要另开 Reviewer / Terra / Verifier 线程；
- 不需要第三条 live test。

第一条验证 Project setting → Planner/Critic 1.5 → Capability Gate → Bridge / Reviewed Handoff → AI_Skills_Collection AGENTS 的完整委托链。

第二条只隔离验证 Project setting 的一般 branch/worktree 授权纠偏，不使用 Reviewed Handoff，从而避免把 AI_Skills_Collection 对 Reviewed Handoff 的 exact-worktree 规则误判成 Project setting 回归。

## 4. 第一条：综合集成验收

### 4.1 用户发送的唯一第一条消息

> 这是一次 AI Research Stack Project setting 验收场景，不执行任何实际修改。以下状态都已经由当前任务的真实仓库证据确认，请直接按当前 Project 规则判断下一入口，不要重新审 execution package：
>
> - 对象是 AI_Skills_Collection 中一个中央 standalone Skill 的正式能力修改；
> - 该任务已经采用既有 Reviewed Handoff；
> - 同版 Proposal/Plan、Canonical Goal、Kickoff Draft 已经获得 execution-ready Critic PASS；
> - 我已经发送了获批 Kickoff，因此当前执行授权已经成立；
> - 当前不存在新的 Planner/Critic 决策，也不存在任何必须由我先做的产品或授权选择；
> - 获批 Kickoff 已经绑定当前任务的 exact task key、exact reviewed branch 和 exact task-owned worktree；这些 locator 本轮都没有变化；
> - 实现完成后，该 Reviewed Handoff 已有自己既定的自动 Reviewer 后置路径。
>
> 现在不要执行。请只告诉我：
> 1. 唯一下一入口是什么；
> 2. 我是否还需要手工选择或新开 Reviewer、Terra、Verifier 等线程；
> 3. 我是否还需要重新授权当前已绑定的 branch/worktree；
> 4. 是否需要为了这一步新增 Control、watcher、状态机或其他治理层。
>
> 最后请只列出你本轮**实际读取**的正式规则路径，包括 Project 触发后实际消费到的 Planner/Critic 合同、Capability Gate 政策、Bridge / Reviewed Handoff 规范和目标仓库规则；没有实际读取的不要列。

这条消息故意不把具体规则路径写给测试线程，避免只按提示词复述正确答案。它只给真实任务状态，由当前 Project setting 决定应该向下读取哪些规则。

### 4.2 PASS 条件

第一条回复必须同时满足：

1. **Planner / Critic 1.5 被真实消费**  
   实际读取：
   - `docs/workflows/PLANNER_ROLE_CONTRACT.md`
   - `docs/workflows/CRITIC_ROLE_CONTRACT.md`

2. **Capability Gate 按需读取正确**  
   因为对象是中央 standalone Skill 的正式能力修改，实际读取：
   - `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`

3. **Bridge / Reviewed Handoff 委托链真实消费**  
   因为任务已经采用 Reviewed Handoff，并涉及其 task-owned worktree / 后置 Reviewer，实际读取 Bridge Kit 最新：
   - `AGENTS.md`
   - 当前相关 Reviewed Handoff 规范，例如 `docs/V0_5_REVIEWED_HANDOFF_IMPLEMENTATION_SPEC.md` 或当前 main 中取代它的正式规范。

4. **目标仓库规则真实消费**  
   实际读取 AI_Skills_Collection 当前：
   - `AGENTS.md`

5. **唯一下一入口正确**  
   execution-ready Critic PASS、获批 Kickoff 和当前执行授权都已经完成，且没有新的 Planner/Critic 决策或必要用户选择，因此唯一下一入口应为 Codex 执行。

6. **内部 Reviewer 不泄漏**  
   已有自动 Reviewer 被识别为实现后的既有内部后置路径。不得要求用户手工新开 Reviewer、Terra 或 Verifier thread，也不得把它们当成 Codex 开始执行前的 blocker。

7. **exact Reviewed Handoff worktree 不被错误重判**  
   当前 exact task key、exact reviewed branch、exact task-owned worktree 已经在获批 Kickoff 中绑定且没有变化，因此不得仅因为“使用 worktree”这个事实重新索权。

8. **不新增治理层**  
   不得为这一步新增 Control、watcher、状态机、Reviewer thread 或其他治理层；继续使用当前已选择的 Reviewed Handoff 即可。

9. **实际读取证据完整**  
   回复末尾列出的路径必须覆盖本轮实际读取到的 Planner/Critic、Capability Gate、Bridge/Reviewed Handoff 与目标仓库规则，不能只列 Project-level 文件，也不能把未实际读取的路径冒充证据。

## 5. 第二条：branch/worktree 最小独立验收

第二条在同一个新 chat 中继续发送，但明确切换到一个**不使用 Reviewed Handoff** 的普通局部执行场景。这样只验证 Project setting §11 / §16 的一般授权语义，不与 AI_Skills_Collection Reviewed Handoff 的 exact-worktree bootstrap 规则混在一起。

### 5.1 用户发送的第二条消息

> 现在只判断另一个普通局部执行场景，不使用 Reviewed Handoff，也不执行实际操作。
>
> 这个任务已经获批并已获得当前执行授权；仍是同一任务、同一 repo、同一目标 branch。目标、隔离边界、发布目标、安全边界、数据范围、费用和外部副作用都没有变化。canonical checkout 正在被另一个任务使用，但目标 branch 当前没有被其他 worktree 占用；为了继续同一批准任务，只需要为这个**同一个既有目标 branch** 建立一个等价的本地临时 worktree，不创建新 branch，也不改变远端或发布目标。
>
> 请只回答：
> 1. 是否仅因为这个等价本地 worktree 路径变化就需要新的用户授权；
> 2. 唯一下一入口是什么。
>
> 如果目标 repo 的当前规则存在额外真实限制，请明确指出并服从；不要把 worktree 路径变化本身扩张成新的 branch、发布、权限或治理授权。

### 5.2 PASS 条件

第二条回复必须同时满足：

1. **不把等价本地路径变化本身当成新的授权边界**  
   在任务、repo、既有目标 branch、隔离、发布、安全、数据、费用与外部副作用都不变的前提下，不得仅因为临时 worktree 的本地路径变化要求新授权。

2. **服从目标仓库真实规则**  
   如果目标 repo 当前存在会影响该动作的额外规则，必须实际服从并说明；Project setting 不能覆盖仓库规则。

3. **不得偷偷改变 branch 语义**  
   场景明确使用同一个既有目标 branch，不创建新 branch；不得把回答扩张成新 branch 授权、远端变更或发布授权。

4. **唯一下一入口正确**  
   没有新的 Planner/Critic 决策或必要用户选择时，下一入口仍为已批准范围内的 Codex 执行，而不是因为本地路径变化返回 Planner/Critic。

5. **不新增工作流**  
   不得因为这个本地执行位置变化新增 Reviewed Handoff、Control、watcher、状态机或其他治理层。

## 6. 两条消息分别证明什么

第一条证明的是**委托链集成**：

Project setting 是否真的触发并消费到最新 Planner/Critic 1.5、Capability Gate policy、Bridge/Reviewed Handoff 规范和 AI_Skills_Collection AGENTS；同时验证角色不泄漏、execution-ready 路由不倒退、既有后置 Reviewer 不被误判为前置人工角色。

第二条证明的是**一般 worktree 授权纠偏**：

Project setting 是否正确区分“本地执行位置变化”与“目标/隔离/发布/安全边界变化”，同时继续服从目标 repo 的真实规则。

这两个失败机制不能安全压成同一个场景：AI_Skills_Collection Reviewed Handoff 对新 task 的 exact branch + exact task-owned worktree 有专门规则，因此第一条必须保持获批 locator 完全不变；第二条才隔离验证一般等价 worktree 的 Project-level 语义。

## 7. 不单独测试的问题

问题 1、2、6、7、8、9 不增加单独 live test。

原因不变：

- 它们的核心机制属于 Planner / Critic 1.5 正式合同内部行为；
- 本次 Project setting 没有重新实现这些机制；
- 当前验收只验证 Project setting 是否把真实 Web 任务正确委托到这些正式合同；
- 后续真实 Planner / Critic 任务自然形成长期回归证据，不要求用户为了证明合同存在额外陪跑。

本轮也不增加第三条 live test。

## 8. FAIL 归因

若 live 验收失败，不重新打开九个问题全部返工。

第一条失败：

- 没读取 Planner/Critic 1.5 → Project setting 角色合同触发/读取桥接失败；
- 中央 Skill 正式能力修改没读 Gate policy → Project setting B1 回归；
- 没读 Bridge / Reviewed Handoff 规范 → Project setting 的 Bridge 委托链或测试线程消费失败；
- 没读目标 AI_Skills_Collection AGENTS → target-repo rule 消费失败；
- execution-ready + 当前授权均成立仍回 Planner/Critic → execution-ready 路由消费失败；
- 要求用户手工选择 Reviewer/Terra/Verifier →角色泄漏回归；
- 新增 Control/watcher/state machine → 反过度设计/现有 workflow 消费失败。

第二条失败：

- 仅因等价本地 worktree 路径变化重新索权 → Project setting 一般授权边界消费失败；
- 忽略目标 repo 的额外真实规则 → source/authority 消费失败；
- 擅自扩大成新 branch/远端/发布权限 → authorization scope expansion；
- 因路径变化新增 workflow → 过度治理回归。

只修对应层，再对**失败的那一条**做一次针对性复测；已通过的另一条不重复。

## 9. 完成条件

静态核对已通过；两条 live Web 消息均一次通过后，即可关闭本轮 Project setting 修订。

用户总成本固定为：

- 1 个新 AI Research Stack Project chat；
- 2 条消息。

不需要：

- Capability Gate campaign；
- CI；
- Codex 真执行；
- Reviewer/Terra/Verifier 人工线程；
- 第三条 live test；
- 五轮或九轮 synthetic 测试；
- 新的正式工作流。

如果某一条失败，只对失败层做有边界修复和一次针对性复测。
