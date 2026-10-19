# ChatGPT Web PASS 可信度与用户控制修复 — Execution Plan v0.3

日期：2026-10-19  
任务键：`chatgpt-web--pass-integrity`  
设计 authority：`docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_3_2026-10-19.md`  
设计分支：`work/chatgpt-web--pass-integrity`  
执行包基线：最新 main 已同步至本分支，当前共同基线包含 `main@9740a593c1622bce61401c8215c621f8cdb7d93a`。  
阶段：EXECUTION_PACKAGE / FINAL_CRITIC_REQUIRED / NO_IMPLEMENTATION

## 1. 本轮实施目标

只修改 ChatGPT Web Planner–Critic 与能力验收的中央合同，使以下语义成为默认行为：

- 中间设计审查只使用 `PROCEED / REVISE`；
- Critic 级 `PASS` 只在最终 execution-ready 审查出现一次，并与 `READY_FOR_CODEX=YES` 同时成立；
- 唯一 PASS 前必须重新检查完整用户承诺、完整执行包和正常用户路径；
- 实现后保留独立最终评估前安全门，但使用 `PROCEED_TO_FINAL_EVALUATION / REVISE`；
- 核心能力必须有正向发生、跨组件成功链和风险匹配的关键失败链证据；
- 普通实现失败默认回同一 Codex 任务，不重新启动 Planner–Critic；
- 每个 Planner/Critic 人工轮次先给用户可独立阅读的一屏中文摘要，再给机器交接；
- Clear Writing 只做用户摘要的最后表达检查，不改写机器 handoff。

不修改 Bridge Kit、Slurm Workflows、Delivery Assurance、workflow-core 或 Clear Writing 产品实现。

## 2. 允许修改的正式文件

实施只允许修改下列既有文件并新增一份 Project setting 完整候选：

1. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
2. `docs/workflows/CRITIC_ROLE_CONTRACT.md`
3. `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
4. `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`
5. `docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_REVISION_PASS_INTEGRITY_V0_3_2026-10-19.md`

Proposal、Execution Plan、Goal、Kickoff 和本轮 Project setting delta 作为冻结设计依据，不由 Executor 重写。

根 README、插件代码、Skill runtime、Marketplace、VERSION、根 CHANGELOG 默认 NO CHANGE。若实现者认为必须修改上述范围，停止并返回 Planner，不得自行扩大。

## 3. Planner Role Contract 1.7

从 1.6 做最小修改，保持其他职责不变。

必须加入：

1. **用户承诺基线**：首个正式 Proposal 冻结少量稳定用户承诺；后续版本不能静默弱化。用户明确改变要求时才记录变更。
2. **设计阶段 verdict**：Planner 送 Critic 的中间 Proposal/revision 预期结论只能是 `PROCEED / REVISE`，不能把 `PROCEED` 描述为最终批准。
3. **最终审查不可缩窄**：Planner 自动生成的 Critic prompt 可以让中间轮次优先复核旧 blocker，但 execution-ready 最终审查必须要求重新对照完整用户承诺、Proposal/Plan/Goal/Kickoff 和正常用户路径。
4. **失败分流**：批准范围内的漏实现、调用未接通、配置 scope、runtime/PATH/loader、测试/CI/已批准 Gate failure 默认 `RETURN_TO_CODEX`；只有用户承诺、架构 owner、权限、验收或 recovery semantics 需要改变时才回 Planner。
5. **用户摘要**：每个 Planner 人工轮次先给一屏自然中文摘要，必须说明本轮结论、相对上一轮的实际变化、产品影响、剩余真实问题、用户是否需要动作、下一接收方和原因；然后再给机器 handoff。
6. **Clear Writing**：正式 writing-style 可调用时，对用户摘要做一次最终表达检查；不可用时不得假称调用。机器 handoff 不经 Clear Writing 改写。

不得新增新的 persistent state/schema/role。

## 4. Critic Role Contract 1.7

从 1.6 做最小修改，保留独立性、最终评估前检查和现有高成本任务保护。

必须修改：

1. **设计阶段**：只允许 `PROCEED / REVISE`。Proposal 合理但尚未形成完整执行包时必须 `PROCEED`，不得 PASS。
2. **唯一 PASS**：只有 execution-ready 最终审查可给 `PASS`，且必须同时 `READY_FOR_CODEX=YES` 并直接生成最终短 Codex handoff。
3. **PASS 强语义**：所有用户承诺、配置归属、关键调用、默认值、逐任务覆盖、正常成功、关键失败/恢复、Gate 和高影响授权边界都已冻结；Codex 只剩普通实现细节。
4. **最终审查全量回看**：不得被 task-specific prompt 缩成只审上一轮 finding。读取范围只覆盖当前用户承诺及其一跳实现链，不做无边界全仓审计。
5. **PASS 失效**：PASS 后如果必须改变用户承诺、架构/canonical owner、权限、Gate 成功定义或 recovery semantics，原 package/PASS 对修改后的语义失效；保持同一 task_key 回 Planner，新闭环仍只有一次 PASS。
6. **实现后安全门**：不可继续调优的最终评估前仍由独立 Critic 检查完整产物、正常入口、同一最终候选、评估标准、预算和恢复；结论只能 `PROCEED_TO_FINAL_EVALUATION / REVISE`。
7. **实现后用户级结论**：`RETURN_TO_CODEX / CANDIDATE_ACCEPTED / RELEASE_READY / RELEASED` 只是用户层表达，不创建持久状态。
8. **用户摘要**：所有实质轮次先给一屏中文摘要；REVISE 先解释问题实质，不能把 finding 列表当用户说明；PROCEED 说明稳定项与未闭合项；唯一 PASS 给一屏真实架构说明。
9. **Clear Writing**：与 Planner 同样只用于用户摘要，机器交接保持精确原文。

## 5. Plugin Capability Gate Policy 1.2

在现有 normal-entry / positive / negative / should-not-change / same-final-candidate 要求上增加三条，不增加固定 Gate 数：

1. **正向能力义务**：产品明确声称会发生的核心能力，至少一个 final-candidate normal-entry case 必须实际观察到该正向行为；`UNKNOWN`、fallback、未配置或 fail-closed 不能成为唯一证明。
2. **跨组件成功链义务**：若一个用户承诺跨多个组件，至少一个 Gate 场景必须从正常入口覆盖完整链路，不能用各组件分别 PASS 推断集成存在。
3. **风险匹配失败链义务**：若承诺包含 fail-closed、安全阻断或恢复语义，选择风险最高且能代表真实事故的关键边界失败，从正常入口直接证明危险下游动作不发生或恢复语义成立。数量由风险决定，不构造全故障矩阵。

Bridge 和 Slurm 仅作为规则解释中的回归例，不把产品专属逻辑硬编码到中央 policy。

## 6. Project setting 最小增量

本执行包冻结的 exact 最小增量见：

`docs/project-settings/AI_RESEARCH_STACK_PASS_INTEGRITY_PROJECT_SETTING_DELTA_V0_3_2026-10-19.md`

Executor 必须以实施时最新、用户已确认生效的完整 Project setting 快照为基线，生成一份完整 clean candidate，不允许直接覆盖 ChatGPT Web 设置。

只有用户本人实际替换并确认后，才可把新快照记为“已生效”。

## 7. 协作回归记录收口

对 `CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md` 只做追加式收口：

- 保留原十类历史问题，不改写旧事实；
- 追加 Bridge/Slurm 新事故：设计/执行包获批后仍靠用户追问发现核心链路缺失；
- 记录本轮修复的四条长期边界：唯一 PASS、稳定用户承诺、正向/端到端/失败链、用户摘要双层输出；
- 明确这些是中央 Planner/Critic/Gate owner 的修复，不把责任下沉到 Bridge 或 workflow-core。

具体修改语义见 closure plan。

## 8. 实施与验证顺序

1. 从 execution-ready PASS 指定的 exact package commit 继续同一 task branch。
2. 修改 Planner/Critic/Gate 三份中央合同及内部版本号：Planner 1.7、Critic 1.7、Gate Policy 1.2。
3. 生成完整 Project setting candidate，但不修改 ChatGPT Web live setting。
4. 更新 collaboration regressions。
5. 做静态一致性检查：
   - 设计中间审查不得允许 Critic PASS；
   - execution-ready PASS 必须与 `READY_FOR_CODEX=YES` 绑定；
   - 实现后最终评估安全门仍存在；
   - 机器 handoff 不受 Clear Writing 改写；
   - 不引入第三角色、数据库、watcher、daemon、ledger 或新状态机。
6. 做三组语义回放：
   - Bridge：repo-local Notifier / Persistent 未接 Notifier / ETA 永久 UNKNOWN 的执行包不得获得唯一 PASS；
   - Slurm：Hook runtime 启动失败而危险底层动作未被明确验证的执行包不得获得唯一 PASS；
   - 普通 implementation bug：冻结架构未变时应 `RETURN_TO_CODEX`，不能机械回 Planner。
7. 做一个用户摘要回放：REVISE/PROCEED 回复在机器 handoff 前必须能独立说明本轮变化和下一步。
8. 核对 Git diff 只涉及批准范围。

这些回放可以是确定性的合同场景检查与独立 Critic 阅读，不要求新增自动评测框架。

## 9. 实现后独立检查与最终评估

实现完成后仍保留 Proposal v0.3 冻结的安全门：

- 独立 Critic 读取实际修改后的完整三份合同、Project setting candidate、回归记录和语义回放；
- 检查是否来自同一候选；
- 结论只能 `PROCEED_TO_FINAL_EVALUATION / REVISE`；
- 若可继续，最终评估使用一个新鲜、未用于改合同的短场景验证唯一 PASS/用户摘要行为；
- 最终候选通过后使用 `CANDIDATE_ACCEPTED`，不再产生第二个 Critic PASS。

## 10. 权限和停止条件

本任务是文档/治理实现，不授权：

- Bridge Kit、Slurm、Delivery Assurance、workflow-core 或 Clear Writing 产品代码修改；
- live ChatGPT Project setting 修改；
- 真实 Slurm、Gmail、模型付费 Gate；
- force/destructive Git；
- main/release 合并或发布。

若实施过程中发现必须改变 Proposal v0.3 的用户承诺、架构 owner、权限、Gate 成功定义或恢复语义，停止，原 execution-ready PASS 对修改后的语义失效，回同一 task Planner。

README checked: no update required。
