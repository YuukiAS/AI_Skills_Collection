# Planner–Critic 1.8 实施准备计划 v0.10：同版决策说明与接收方验收

日期：2026-10-22
同版 Proposal：`docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_10_2026-10-22.md`
任务：`chatgpt-web--pass-integrity`；分支：`design/chatgpt-web--pass-integrity-v0-4`
设计审查阶段，只允许 `PROCEED/REVISE`。所有文件按交接入口给出的同一准确 PACKAGE_COMMIT 读取。
正式 main 的 Planner/Critic 仍是 1.7；本计划不是现在允许 Codex 执行的冻结包。

## 一、实施目标与已经做过的事情的区别

v0.9 只是改变“写说明的时间和位置”，没有接收方义务；错误 v1.0 假设需要 Mica 与平台呈现工程，本次撤回。v0.10 新增的是**双向交付责任**与**最终 PASS 多一次原 Planner 接收**：不合格的 Critic 回答不能仅凭机器状态继续进入 Codex；技术上真实合格但文字糟糕时由接收 Planner 从已审全文恢复说明，不再让同一 Critic反复原地 PASS。

这一改变不是增加日常质量审查员：原本 `REVISE/PROCEED` 就必须交 Planner，直接在这个既有接收步骤核对；只有最终执行就绪 PASS 从原“直交 Codex”变成“交原 Planner 核对一次再给 Codex”，增加一次用户纯复制粘贴。是否值得额外跳转为本轮独立 Critic 必审取舍，不得隐藏成本。

## 二、计划修改的真正角色职责和精确落点

### Planner Role Contract 1.7 → 1.8

**§2 / §2.1：准确版本与历史锚点。** 新实质轮次以最新正式 main 的角色合同、当前同任务的完整 Proposal/上轮 Critic review 为实际依据；不能只依赖历史聊天、消息摘要或任务专属 prompt。记录 current stage、当前 source/ref、前轮实际结论与仍开放的关键问题。未变源不无谓反复全文读。

**§6：提案含同版用户决策说明。** 用户一开始就能看懂选了什么真实技术、重要替代、代表性动作、失败路径、风险与当前已证明范围。技术决策实质改变则同版更新说明；未变只写有用的当轮变化，不机械重打印全文。此内容在既有 Proposal 前部，不另建通用报告文件。

**§7：双对象送审。** 独立 Critic 同时审完整技术包和用户真正会阅读的说明全文；这与第 6 节现有的“关键决定摘要”区别在于它是明确、可比对的交付对象，必须随方案版本变化而改变，不能当成可选解释片段。

**§10 / §10.1：接收 Critic 结果先验收交付。** 收到 `PROCEED/REVISE/PASS`，先从准确来源判断 Critic 的技术依据/结论是否完整、它有没有让用户理解本轮决定、是否与当前 Proposal 身份一致。源证据充分而表述差，由 Planner 忠实修正读者解释并继续；技术源/对象/结论不完整，返回同 Critic 补审，不推进 Codex。当前 Planner 能做的后续不转嫁用户。普通实现 bug 不开新治理任务。

**§11：最终 PASS 后由 Planner 做用户交付核对。** 独立 Critic 给技术 PASS 但此时只能 `COPY TO PLANNER`；原 Planner接收后，不得重新审批技术，不得扩大授权；核对受审完整说明、独立裁定、当前包与原用户承诺，展示正确的用户架构全貌及 Critic 关闭的关键问题，再生成现有短 `COPY TO CODEX`。若发现不一致不放行。既有短 Kickoff、Goal/Plan 同版、权限最小化规则原样保留。

### Critic Role Contract 1.7 → 1.8

**§2 / §4：独立来源与反证。** Critic 先确认用户原要求和真实 source，再对照 Planner 当前用户决策说明；实际机制可替换而说明不变、正文误称 Hook/Wrapper、无法解释一个真实成功/失败链、隐瞒未验证接口，按实质缺陷处理。不能因为作者提供了“用户说明”就自动认可其专业内容。

**§6：每个 verdict 都有用户能理解的真实理由。** `REVISE` 必须说失败如何损害使用、保留哪些正确部分、最小修复；`PROCEED` 必须说哪些设计已足以继续和为什么还不是可以执行；最终 `PASS` 需要解释确切批准的架构、关键历史阻塞关闭、当前可执行与未验证范围。读者正文不堆 status/commit/finding 编号。

**§6.1 / §6.2：改变最终 PASS 的唯一下一入口。** `PROCEED/REVISE` 仍 `COPY TO PLANNER`；唯一技术 `PASS + READY_FOR_CODEX=YES` 仍只能由 Critic 产生，但此时仍用现有 `NEXT_HANDOFF=PLANNER` 及短 `COPY TO PLANNER`，正文注明此步只为最终读者交付接收；不发明新的机器状态/枚举，而不是直接给最终 `COPY TO CODEX`。这不是新增长期机器状态，仅是一次明确的人工接收目的。原 Planner核对后才发正式 Codex 入口；用户不能把 Critic 的临场独立回复直接误当已检查的执行提示词。

**§6.3：批准内容必须能逐轮对照。** 包含本任务所有影响决定的技术及代表性流程；有前轮 `REVISE` 时说明真实关闭情况、未变范围与剩余风险。可直接引用经过专业审查的同版用户机制正文，但 Critic 必须有独立结论，不能粘贴 Planner 正文代替判断。少量内部元数据与可复制机器交接分层。

**§9：先检查谁没有实际消费旧规则。** 发现上游/下游没做接收检查，修当前接收机制，不再增加同义“应说人话”。

### 不修改的合同

`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` 1.2：本任务不添加固定 Gate 个数，仍按实际专业质量/真实性/正常入口验收。
AI Research Stack Project setting：现有条款已触发两份角色合同和自然中文，无需用户再次替换。
`AGENTS.md`/Bridge：本轮不新增平台安全工具、网关、机器批准状态。完整执行授权仍由 user 和目标仓库规则限定。

## 三、单轮交付与跨轮接收的实际合同

**Planner 提交前**：完成现有 Proposal 的“用户决策说明”和对应技术方案、Goal/Kickoff（如该阶段需要），推送后用 GitHub 重新读取相同 ref，确认最新内容属于正确任务。对用户先讲本轮真实变动、最重要技术选择、为什么、剩余问题和送审目的，再附自动生成的短 `COPY TO CRITIC`。

**Critic 审查后**：给自然中文判断和独立证据；在中间阶段给可转发原 Planner 的 prompt，最终技术 PASS 也回原 Planner作一次交付接收。若缺真实完整 review 文件、Critic 不具有 repo write 权限，就让原 Planner接收完整原始审查文本并忠实归档；不让用户手工写 review 文件或查询 GitHub。

**Planner 接收时**：判断三种原因，避免无谓多轮：
1. 已核实完整技术判断且用户正文完整 → 正常推进下一轮 / 最终交付；
2. 技术判断源证据完整但文字只像审计流水 → 从已审 Proposal 原文与 Critic 现有 finding 直接补正用户说明；不要求 Critic 再“第四次 PASS”；
3. 缺实际独立技术依据、权限/执行接口未验证、版本/用户承诺冲突 → 不冒充纯文案问题；退回 Critic 做真正的技术补审或回 Planner 修 Proposal，禁止 Codex。

上述分类不是新持久 status 字段；由原接收者在原任务的正常回复中判断。

**交给 Codex 之前**：由原 Planner 核对精确批准 Proposal/Plan/Goal/Kickoff、真实 Critic 原结论、已向用户展示的架构说明和用户授权。只引用冻结包并短交接。Codex 后续依目标 repo AGENTS 和正常工具再核实际身份；这不能冒充不可绕过的 ChatGPT Web 发送前 Hook。

## 四、关键流程实例：从 Slurm Wrapper 风险到最后批准

第一轮 Planner 选择 Wrapper，却在用户正文只写“危险操作会被安全拦截”。Critic 对照实际命令覆盖发现绝对路径/子进程可能绕过，在 `REVISE` 说明真实失败和要求明确保护边界。

第二轮 Planner 换成全局 `PreToolUse` 并行 MCP 确认，必须同步用户说明，交代 `Bash` 命令运行之前发生什么、`scontrol` 查分区、原 `scancel` 为什么不执行、当前聊天怎么获得本人确认、失败时哪个执行路径不放行、为什么不再采用 Wrapper。Critic 复核方案与说明的一致性；仅“增加 Hook”不算用户已经理解。

若下一轮 Critic `PROCEED`：说清架构选择已比较，但执行入口/故障测试还未关闭；由 Planner继续冻结 Plan。若某轮 `REVISE`：说明真实断点并保持正确部分。只有独立完整执行前审查 `PASS` 时，才允许原 Planner 读回该准确受审说明和 Critic 的具体理由，向用户交付可以理解的机制与短 Codex 入口。**不允许“已设计 Hook”替代真实运行环境的 fail-closed 实测**；真正的发布需后续正式用户正常入口验证。

换成 Bridge Notifier、科研模型、幻灯片布局引擎时使用相同的用户决策/因果/接收原理，例子和技术身份按领域重新选，不形成 Slurm 专项模板。

## 五、验证方法和通过界线

**已见错误回归**：从用户提供的真实坏 Critic PASS、Slurm Wrapper/Hook/MCP 实施更迭、Bridge 机器共享通知错误设计、Phase C 无实际下一入口中抽取相应场景。检查用户能否理解原问题与新技术、每一 verdict 是否解释理由、下一接收方是否发现并修正坏交付；不单凭关键词或字数判分。

**受控连续返修**：在真实或隔离安全方案中进行不少于一轮实质技术变化的 `Planner → Critic REVISE → Planner 修订 → Critic 复核`，期间下一轮仅传准确版本和自然任务，不附“请说人话/要有 Hook 名”的提示。核对用户决策说明随技术修改、独立审查没有缩成旧 finding、正常回复仍能说清当前总体架构。

**最终 PASS 交接**：冻结真实可形成 execution-ready PASS 的方案；Critic 独立作正确判定后必须先回 Planner，Planner 分类检查、必要时补正常解释，再给 Codex 入口。若 Critic 实际 REVISE 不可造假 PASS 或换样本。额外一次机械转发的真实耗时/用户可读结果需记录，若增加明显无意义往返则 Critic 应要求更轻的等价设计。

**当前普通 Web 入口**：候选试用首次有一次必要的候选合同绑定，后续回合不反复注入写作标准；正式 1.8 合入 main 后，还须在提前选定的真实新任务中，普通用户要求不增加额外提醒，亲自验证 Planner/Critic 确实读取正式合同、可读说明/每轮结论与接收方检查生效。不能把测试线程看到验收答案、历史样本或配置存在称为正常使用稳定通过。

**判分责任**：Critic 独立读原始方案与全文；Planner 在本来就必须接收 Critic 的下一回合核对其交付。不是同线程自查，也不增加第三人工角色；中文专业质量必须由真实完整产物及用户反馈检验，来源身份只支持来源真实性。若 Planner自己最终交付的说明仍缺必要技术，视为未通过正常入口质量，不用一条虚假的机器 PASS 覆盖。

## 六、原 1.8 正确机制保留、范围与授权

原 v0.7 已正确的任务 prompt 兼容、关键现实接口证据、非终态交接、PASS 后解释/新矛盾分流、最终候选同版身份、实现后 Critic 安全门（`PROCEED_TO_FINAL_EVALUATION/REVISE`）、真实 Web 回归和安全合入 main/远端回读继续保留，不新增第三 Reviewer、长期服务或付费模型。

设计阶段只写原 `design/chatgpt-web--pass-integrity-v0-4` 分支的 v0.10 文档与稳定需求记录，不修改 `main`、正式角色合同、`AGENTS.md`、Project setting、Capability Gate Policy、Clear Writing、Slurm、Mica、Bridge Kit、Plugin Creator 和正式发行物。

**额外的 Planner 最终 PASS 接收是改变原 1.7 审查后直接 Codex 的工作流程。** 本轮独立 Critic 要具体判断它的用户收益能否抵消一次机械交接的成本；只有设计阶段 `PROCEED` 后 Planner 才准备最终可执行定位与实施包，最终唯一 `PASS` 和用户授权前不可实施。若用户明确不接受额外交接，需重新设计可真实工作的等效接收方式，不得静默退回旧无检查路径。

本轮不生成软件发行版本 1.0，不发布任何能力，不创建新 Issue 作为另一套控制面；看板/Issue 同源事实由以后实际有权限的维护轮次处理，不能让用户手工维护。README 仍按最终修改的真实范围再核。
