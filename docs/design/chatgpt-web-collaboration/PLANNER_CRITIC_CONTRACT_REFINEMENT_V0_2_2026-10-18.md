# Planner / Critic 合同完善方案 v0.2

日期：2026-10-18  
状态：修订后待独立 Critic 复核  
目标：只完善 ChatGPT Web 长期 Planner / Critic 协作合同，不修改 `workflow-core`、具体 Plugin/Skill 或 Bridge Kit 运行实现。  
前版：`docs/design/chatgpt-web-collaboration/PLANNER_CRITIC_CONTRACT_REFINEMENT_V0_1_2026-10-17.md`  
修订依据：用户转交的独立 Critic 结论为 `REVISE`，仅包含 B1、B2 两个 blocker；本版只关闭这两项及其直接文字回归，其他设计保持不动。

## 0. v0.2 相比 v0.1 的唯一实质修订

### B1 — 用户侧角色模型修正

ChatGPT Web 的人工协作角色只有两个：

- Planner：负责方案、范围、恢复路线与职责判断；
- Critic：负责独立审查和批准。

Codex 是批准后的执行入口，不是第三个 ChatGPT Web 人工角色。

Reviewer、Verifier、Terra 等身份不属于普通 AI Research Stack 的网页端人工角色。它们只在某个既有 Bridge Kit / Reviewed Handoff / Control 或其他明确重型工作流本来就要求时，继续按照那个既有机器、自动审查或仓库协议工作。本次合同完善：

- 不新增 Reviewer；
- 不要求用户手工选择 Reviewer / Terra；
- 不把 Codex 写成第三个人工角色；
- 不修改既有 Reviewer / Verifier / Terra 机器协议；
- 不改变 Bridge Kit / Reviewed Handoff 的既有内部角色图。

因此，本版把 v0.1 中“Planner / Critic / Codex 三个人工接收方”统一修正为：

> ChatGPT Web 只有 Planner 与 Critic 两个人工协作角色；Codex 是 execution-ready 后的执行入口。既有重型工作流中的 Reviewer / Verifier / Terra 等内部角色按原协议运行，不成为普通网页端人工路由选择。

### B2 — Codex 交接真实性收紧，但不误伤后置 Reviewer

v0.1 的“第一个尚未完成动作属于 Codex”判据不够精确。本版改为：

> 只有在 Codex 开始当前批准的实质执行之前，不再存在任何尚未完成的 Planner 决策、Critic 审查或用户必要产品/授权选择时，才允许给出 Codex kickoff / `READY_FOR_CODEX=YES`。

Codex 收到 kickoff 后必须能够直接进入当前批准范围内的实质执行。允许它先做正常的任务内读取、环境确认或安全预检，但这些步骤只能服务于已经批准的执行，不能用于发现一个其实应该在 kickoff 之前由 Planner、Critic 或用户决定的关键事项。

因此以下情况不允许称为 execution-ready：

- Codex 只能先读一批文件，然后才决定是否仍需 Planner；
- Codex 只能先做 probe，再决定是否仍需 Critic；
- Codex 只能先检查权限，再让用户补一个本应在 kickoff 前明确的必要授权；
- Codex 进入任务后才发现核心产品、架构、恢复或权限语义尚未冻结。

但**实现完成后的后置审查不属于上述前置依赖**。如果某个既有 Bridge Kit / Reviewed Handoff / Control 重型工作流本来就规定 Executor/Codex 实现后由 Reviewer、Terra、Verifier 等继续审查，则该后置审查按既有协议保留，不因为尚未发生而阻止 Codex kickoff。本版不新增 execution segment、review protocol、角色或状态机。

除 B1、B2 外，v0.1 的设计原则、九类问题覆盖、正常使用六问、PASS 范围说明、非终态下一跳、比例化 PASS 解释、有限同因果机制检查、owner-first 与简单人类版本规则均保持不变。

## 1. 背景与目标

本方案直接处理：

- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md` 记录的九类真实问题；
- 当前 AI Research Stack Project setting 备份：
  `docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-17.md`；
- 当前 `PLANNER_ROLE_CONTRACT.md` 与 `CRITIC_ROLE_CONTRACT.md`。

目标不是增加新的工作流、角色、状态机、插件或自动化，而是让已有 Planner / Critic 在 ChatGPT Web 中真正承担四件事：

1. 审查必须经得起普通用户沿正常路径追问；
2. 用户只需要理解 Planner 与 Critic 两个人工协作角色，执行阶段直接进入 Codex；
3. 非终态必须自动给出唯一下一入口，不让用户承担内部角色路由；
4. PASS 必须让用户理解自己到底批准了什么。

## 2. 当前规则为什么仍不足

现有合同已经有多项正确原则，例如：

- PASS 绑定对象、版本和阶段；
- Critic 检查过重、过简与实际入口；
- REVISE 后应自动给 Planner prompt；
- execution-ready PASS 必须审 Proposal / Goal / Kickoff；
- 曾经 REVISE 后的最终 PASS 应给用户可读闭环说明。

但九类真实失败说明仍有四个结构性缺口。

第一，现有 Critic 规则偏重“审查材料是否充分”，没有把“普通用户会怎样连续使用和追问”变成 PASS 前必须实际回答的反证面。因此一个文档很完整的方案仍可能在启动、配置、进度可见、权限拦截、恢复或接手路径上留下大洞。

第二，现有“下一角色 prompt”只覆盖部分 Critic / Planner 路径。仓库内部的 Reviewer / Verifier / Terra 等身份仍会泄漏到 ChatGPT Web，导致某些结果绕过 Planner/Critic 的用户交接合同。Clear Writing 第二轮自动 Reviewer 耗尽后只报 REVISE、不告诉用户下一步给谁，就是这一缺口。需要修的是用户侧人工协作模型，而不是修改既有 Reviewer / Verifier / Terra 协议。

第三，当前 execution-ready 主要检查执行包完整与授权边界，但仍可能把尚未完成的 Planner 决策、Critic 审查或必要用户选择推迟到 Codex 启动之后才发现。需要检查的是**Codex 开始实质执行之前的所有前置依赖是否已经关闭**，而不是要求整个后续工作流都已经完成。既有重型工作流中的实现后 Reviewer / Terra / Verifier 继续保留为后置审查。

第四，用户可读 PASS 说明当前只在“同一对象曾经 REVISE”时强制要求较完整闭环。首次就 PASS 的复杂设计反而可能只得到 PASS + 路径 + Kickoff，使用户不知道通知接口、逐任务配置、危险动作拦截层、失败恢复等关键机制到底怎样设计。

## 3. 设计原则

### 3.1 不新建角色和工作流

ChatGPT Web 的人工协作角色只有：

- Planner：方案、范围、恢复路线或职责需要判断或修改时负责；
- Critic：需要独立审查、批准、复核或争议裁定时负责。

Codex 是 execution-ready 后的执行入口，不属于 ChatGPT Web 人工协作角色。

现有仓库协议中的 Reviewer、Verifier、Terra 等精确身份不删除、不重命名，也不重新定义。它们只在既有 Bridge Kit / Reviewed Handoff / Control 或其他明确重型工作流本来就要求时，继续作为自动任务、机器角色、证据生产者或仓库内部审查者运行。

普通 AI Research Stack 任务不得因为本次合同完善而新增 Reviewer，不得要求用户自行决定“找 Reviewer 还是 Critic”。若一个既有自动 Reviewer / Verifier / Terra 已真实绑定当前重型工作流，则按原协议自动或机器化继续；若该自动路径已耗尽、不可用或结果要求重新做方案判断，则用户侧回到 Planner；若需要新的独立方案审查，则交 Critic。

### 3.2 不新建 PASS 状态枚举

不增加 `DESIGN_PASS`、`PRODUCT_PASS` 等新状态机字段。继续使用现有 review stage / 对象定位，但用户正文必须明确：

- 本次批准了什么；
- 只证明到哪一层；
- 还没有证明什么。

### 3.3 正常使用路径优先于文档完整

Critic 不因为 Proposal / Goal / Kickoff / Gate Matrix 齐全就默认可执行。对会改变用户实际工作方式的设计，必须能回答当前范围内真正重要的正常使用问题。

### 3.4 解释关键机制，而不是重讲整份 Plan

PASS 的用户说明不是第二份 Proposal。只解释会改变用户体验、权限、安全、自动化、费用、通知、恢复或后续操作的关键决定。内部结构、哈希、测试编号和不影响用户判断的细节留在仓库。

## 4. 对 Planner 合同的拟修改

### P1. 在 Active Design Context 增加人类版本与机器定位分离

保留现有 task key、路径和 commit 作为机器定位。

新增规则：

- 新的人类方案版本默认使用简单连续形式，如 `v0.1`、`v0.2`、`v1`、`v2`；
- 只有存在真实成熟度语义时才使用 alpha / beta / rc；
- 历史 `C11`、`R0`、批次号、Gate 编号等可继续作为精确 locator，但不得作为新的用户主版本体系；
- 不新造 `C'` 一类临时版本语法。

对应问题：8。

### P2. 在“五遍预检 / 提案内容”中加入正常使用六问

对于工作流、架构、长期任务、权限/恢复或自动化设计，Planner 在送 Critic 前按适用范围回答：

1. 用户怎样开始；
2. 正常运行时实际发生什么、用户能看到什么；
3. 哪些重要行为有默认值，哪些能逐任务配置；
4. 高影响或危险动作由哪一个真实层负责拦截或审批；
5. 失败、断线、等待或自动轮次耗尽后怎样恢复；
6. 当前阶段结束后，用户侧下一入口是什么；若既有重型工作流会自动进入内部 Reviewer / Verifier / Terra 等后置环节，也应说明该自动路径，而不是让用户手工选角色。

不是每个小任务都机械写六个标题；但任何与核心能力直接相关的问题若仍只能回答“以后再设计”“理论上可以”，不得提交 execution-ready package。

对应问题：1、5、9，并强化 2。

### P3. 强化 owner-first 和反过度设计

跨组件设计必须先回答：

- 当前职责的 canonical owner 是谁；
- 已有 owner 为什么不能直接承担或轻量适配；
- 若要新增层，它具体阻止哪个真实失败；
- 为什么这个收益值得新增维护面和故障面。

发现相邻 Plugin/Skill 或平台问题时，默认记录证据并交给 owner；当前任务只有在职责调整本身已经进入审查范围时才能修改别的 owner。

已有调度器、平台原生机制、服务管理器、领域能力或 Bridge 正常入口能承担职责时，优先复用或适配，不因“统一”而复制第二套路由器、watcher、状态机或长期服务。

对应问题：7。

### P4. 把“非终态续航责任”从 Critic 特例提升为 Planner 通用职责

Planner 处理任何外部审查结果、既有自动 Reviewer / Verifier / Terra 结果、执行中断或恢复结果时，只要当前任务不是终态，就必须确定一个唯一的**下一用户入口**，而不是要求用户自行理解内部角色图。

用户侧规则：

- 需要改变设计、范围、职责或恢复语义 → Planner；
- 需要新的独立方案审查或复核 → Critic；
- 设计与所需前置审查已经完成，可以开始批准范围内的实质执行 → Codex 执行入口；
- 真正只有用户才能完成的产品选择、私有上传或必要授权 → 先提出最小用户动作，完成后继续生成对应 Planner / Critic / Codex 入口。

既有重型工作流中的 Reviewer / Verifier / Terra 若已经由原协议真实绑定并负责后置自动审查，可以直接说明“后续由该既有工作流自动继续”，不把它们变成普通 ChatGPT Web 人工角色。若该自动路径不存在、已耗尽或不能继续，则不得假装会自动接手，应回到 Planner 或 Critic。

对应问题：3、4。

### P5. Codex handoff 增加“前置依赖已经关闭”硬门

任何准备称为 Codex handoff / Kickoff / execution-ready 的包，在送 Critic 前必须确认：

> 在 Codex 开始当前批准的实质执行之前，不再存在任何尚未完成的 Planner 决策、Critic 审查或用户必要产品/授权选择。

Codex 收到后必须能够直接进入当前批准范围内的实质执行。它可以执行正常的任务内 source read、环境确认、安全 preflight 或实现前检查，但这些只能验证已经冻结的执行条件，不能把本应在 kickoff 前解决的关键设计、范围、恢复、权限或产品问题推迟到运行时发现。

因此，若预期 Codex 只能先 inspect / probe，然后才判断是否还需要 Planner、Critic 或用户决定核心事项，就不能生成面向用户的 Codex handoff。

用户发送已审过的 kickoff 可以形成其中明确列出的 bounded authorization；但不能借 kickoff 替代尚未作出的产品选择或尚未完成的独立审查。

**后置 Reviewer 不属于该前置门。** 如果当前任务已经选择某个既有 Bridge Kit / Reviewed Handoff / Control 重型工作流，且其原协议规定 Codex/Executor 完成实现后再由 Reviewer、Terra、Verifier 等进行后置审查，则这些后置环节继续按原协议运行，不要求在 Codex kickoff 前完成，也不因为它们尚未发生而阻止 execution-ready。

对应问题：5，并减少 3、4。

### P6. 真实失败触发有限同簇检查

当一个真实失败证明某个机制本身有洞，而不是单个数据/环境偶发问题时，Planner 在提出修复前检查同一机制的一跳相邻路径，例如：

- 正常成功 / 失败 / 恢复；
- 首轮 / 轮次耗尽；
- 既有自动接手存在 / 不存在；
- 权限允许 / 拒绝；
- 同一 owner 的主要入口 / 邻近入口。

只检查与已证实失败共享同一因果机制的邻域，不升级成全仓或全系统审计。

对应问题：6。

### P7. Planner 给 Critic 的包加入“用户关键决定摘要”

复杂设计送 Critic 时，附一个短摘要，最多聚焦真正会影响用户理解的关键决定，例如：

- 机制到底怎么工作；
- 默认开启什么；
- 哪些可以逐任务配置；
- 危险动作在哪里拦；
- 通知/费用/外部副作用怎样触发；
- 失败后如何恢复。

这不是最终 PASS 说明，而是让 Critic 能检查“用户是否会真正知道自己批准了什么”。

对应问题：9。

## 5. 对 Critic 合同的拟修改

### C1. 明确 Critic 是 ChatGPT Web 唯一人工独立审查角色

ChatGPT Web 的人工协作角色只有 Planner 与 Critic。Critic 是用户需要手工切换到独立审查线程时的唯一审查角色。

Codex 是批准后的执行入口，不是第三个人工角色。

Reviewer、Verifier、Terra 等若属于某个既有 Bridge Kit / Reviewed Handoff / Control 或其他明确重型工作流，继续按那个既有机器/自动审查协议运行并产出证据；本合同不重命名、不删除，也不修改其协议。

不得因为既有自动 Reviewer 不存在、已耗尽或不能继续，就要求用户自己新开一个“Reviewer”或“Terra”线程。此时若需要重新判断方案、恢复路线或下一步，交 Planner；若需要新的独立方案审查，交 Critic。

Critic 可以读取内部 Reviewer / Verifier / Terra 的现有结果作为证据，但不把这些内部角色重新变成普通用户的人工路由责任。

对应问题：3、4。

### C2. 将“六个核心判断”完善为包含正常使用反证的七个判断

新增一项“正常用户路径能否问穿方案”。

Critic 在当前审查阶段按适用项独立回答：

1. 怎么开始；
2. 正常运行中真实发生什么；
3. 用户看到什么、可配置什么；
4. 关键权限/危险操作在哪里由真实机制阻断；
5. 失败、断线、等待、轮次耗尽后怎么恢复；
6. 当前阶段结束后，用户侧下一入口是什么；若既有重型工作流包含后置自动 Reviewer / Verifier / Terra，该自动路径是否真实存在且属于原协议。

若其中任何一个属于核心承诺，却没有明确 owner、机制或阶段边界，则 REVISE。不能用“实现时再补”掩盖会改变架构、权限或用户体验的核心未知。

对应问题：1、9。

### C3. 强化 PASS 范围陈述，防止语义膨胀

每次实质 PASS 的自然中文结论必须显式包含：

- “本次批准的是……”；
- “这不代表……”或等价边界说明。

不得让设计 PASS 自然演变成实现 PASS、产品可用或正式发布结论。后续引用旧 PASS 时必须保留原阶段和边界。

不新增新的 PASS 枚举。

对应问题：2。

### C4. Execution-ready PASS 增加“Codex 前置依赖已关闭”检查

现有 Proposal / Goal / Kickoff 三件套检查继续保留。

Critic 必须确认：

> 在 Codex 开始当前批准的实质执行之前，不再存在任何尚未完成的 Planner 决策、Critic 审查或用户必要产品/授权选择。

只有满足这一条件，才可以 `READY_FOR_CODEX=YES`。

Critic 需要检查的不是“整个未来工作流是否已经结束”，而是“Codex 开始实质执行所需的前置决策是否全部关闭”。因此：

- 若仍需 Planner 改设计、范围、职责或恢复语义 → 不可 READY_FOR_CODEX；
- 若仍需 Critic 完成必要独立审查 → 不可 READY_FOR_CODEX；
- 若仍需用户作必要产品选择或当前任务必需授权 → 不可 READY_FOR_CODEX；
- 若 kickoff 预计让 Codex 只做 read / inspect / preflight / probe，随后才能发现或决定上述关键事项 → 不可 READY_FOR_CODEX。

正常 source read、环境确认、安全 preflight 可以是执行开始的一部分，但它们必须服务于已经批准的范围，不能承担“发现尚未完成的规划/审查/用户决策”的职责。

**既有后置审查不构成前置 blocker。** 如果任务已经采用某个既有 Bridge Kit / Reviewed Handoff / Control 重型工作流，且其原协议规定实现完成后由 Reviewer、Terra、Verifier 等继续后置审查，则该审查无需在 Codex kickoff 前完成，不妨碍 `READY_FOR_CODEX=YES`。Critic 只需确认该后置角色属于既有协议，而不是本次新造的普通网页端人工角色。

本条不新增 execution segment、状态、角色或 review protocol。

对应问题：5，并强化 4。

### C5. 所有实质 PASS 都要给用户关键机制说明，不再只限“曾经 REVISE”

把当前 §6.3 从“曾经 REVISE 后的最终 PASS”扩展为所有实质设计 / execution-ready PASS 的比例化用户说明。

至少按当前对象真正相关的部分说明：

- 这次批准了什么；
- 最重要的机制怎样工作；
- 用户正常使用时会看到什么；
- 默认行为与逐任务可配置项；
- 权限、安全或危险动作由哪一真实层执行；
- 通知、费用、外部副作用何时发生；
- 失败、断线或自动轮次耗尽后如何恢复；
- 哪些能力仍未实现、未验证或不在本次 PASS 内；
- 下一步唯一用户入口：Planner、Critic、Codex 执行入口，或一个确实只能由用户完成的最小动作；既有重型工作流中的内部自动 Reviewer / Verifier / Terra 可作为后续自动环节说明，但不作为普通人工角色让用户选择。

复杂方案可以有 5–10 个关键决定；简单方案保持简短。禁止复制整份 Plan、堆路径/字段/测试名或用术语替代解释。

对应问题：9，也增强 1、2、4。

### C6. REVISE / 非终态必须保证下一入口，不只生成状态

保留当前 §6.2 的自动 prompt，但强化为：

- 所有正式非终态，只要下一步需要另一个人工 ChatGPT Web 线程，就必须在 Planner 与 Critic 两个人工角色中给出唯一接收方，并附完整可复制 prompt；
- 若设计和必要前置审查均已完成，下一步是执行，则给 Codex execution entry / kickoff；Codex 不作为“第三个人工角色”描述；
- 若既有重型工作流中的 Reviewer / Verifier / Terra 将按原协议自动接手，说明该已验证自动入口，不要求用户手工转发；
- 若内部自动路径不存在、已耗尽或不能继续，则不得让用户自己决定“再找哪个 Reviewer”，而应按语义回 Planner 或 Critic；
- 如果无法确定下一入口，这本身是工作流缺口，不能把状态写成“已交接”。

对应问题：3、4。

### C7. Critic 关闭真实机制 blocker 前做有限同簇反证

对于已经暴露“机制级”而非单例级失败的 blocker，Critic 在关闭前检查 Planner 是否覆盖共享同一因果机制的一跳邻域。

Critic 不得借此无限增加新 blocker；只有同一机制直接可推导的相邻失败才能要求补齐。

对应问题：6。

### C8. 过重设计和跨 owner 修改必须有正面证明

在现有“是否过重或过简”中增加：

- 新增路由器、watcher、状态机、长期服务、控制层前，必须明确已有 owner 为什么不能满足；
- 跨 owner 修改必须证明职责调整本身已被批准；
- “为了统一”“更保险”“以后可能有用”不是充分理由；
- 若成熟平台/现有 owner 能解决，Critic 应要求删除多余层，而不是仅记为非阻塞优化建议。

对应问题：7。

### C9. 人类版本命名也进入 Critic 检查

若新提案使用临时、不可预测的人类版本体系，Critic 要求改为简单连续版本；历史机器 locator 不需重命名。

对应问题：8。

## 6. 九类问题覆盖映射

| 问题 | 主要关闭机制 |
|---|---|
| 1. 一问就露洞仍能 PASS | P2 + C2：正常使用六问 / 用户路径反证 |
| 2. PASS 范围膨胀 | C3 + C5：明确批准层级与未证明边界 |
| 3. Reviewer / Critic 等角色混乱 | P4 + C1 + C6：网页端人工角色仅 Planner / Critic；Codex 是执行入口；既有内部 Reviewer 等不成为普通人工角色 |
| 4. REVISE/BLOCKED 后不知道给谁 | P4 + C6：所有非终态唯一下一入口 + 完整 prompt / kickoff |
| 5. Codex handoff 进去后还找 Planner/Critic | P5 + C4：Codex 开始实质执行前，Planner / Critic / 必要用户选择全部关闭；后置 Reviewer 不误伤 |
| 6. 修一个又冒一个 | P6 + C7：同因果机制的一跳邻域检查 |
| 7. 越界改 owner / 过重路由 | P3 + C8：owner-first + 新控制层正面举证 |
| 8. `C'` / `C11` / `R0` 等命名 | P1 + C9：简单人类版本 + 机器 locator 分离 |
| 9. PASS 后仍不知道具体设计 | P7 + C5：用户关键决定摘要 + 所有实质 PASS 的机制说明 |

## 7. 不修改什么

本轮不修改：

- `workflow-core`；
- 任何领域 Plugin / Skill；
- Bridge Kit runtime、Host Policy、Reviewed Handoff / Control 状态机或 Persistent Run；
- GitHub Project schema；
- 既有 Reviewer / Verifier / Terra 的机器或自动审查协议；
- 当前 AI Research Stack Project setting 本体。

Project setting 会在角色合同方案稳定后单独做一次有边界的同步修订，避免合同与设置同时变化导致难以判断哪一层负责。

## 8. 外部核查

本轮 B1、B2 是内部角色语义和交接边界修正，没有引入新的外部产品假设。v0.1 已做的外部核查继续有效，本轮不重新打开已通过设计点。

与本次修订直接相关的当前仓库事实已重新核对：

- Bridge Kit Review 的既有内部角色仍是 `Planner -> Executor -> Reviewer`，属于该重型工作流自己的协议；
- Review 中的 Scheduled GPT Reviewer 是既有自动/机器审查环节，不是本次新建的 ChatGPT Web 人工角色；
- Bridge Kit 明确要求 Executor 在冻结 Plan 后执行，产品/科学/架构取舍不得留给 Executor 自行决定；
- 实现完成后的 Reviewer 审查属于后置阶段，因此不能被误判成 Codex kickoff 前必须已经完成的前置依赖。

这正是 B1、B2 修订的边界：网页端人工协作模型收敛，但不重写 Bridge 的内部 Review 协议。

## 9. 验收标准

下一轮 Critic **优先只复核 B1、B2 及其直接回归**，不重新打开已通过的其他设计点。

B1 最小关闭条件：

1. 文档不再把 Codex 称为第三个 ChatGPT Web 人工角色；
2. Planner 与 Critic 是普通网页端仅有的两个人工协作角色；
3. Reviewer / Verifier / Terra 只作为既有重型工作流的内部或自动角色存在；
4. 不要求用户手工选择 Reviewer / Terra；
5. 不修改这些既有机器协议。

B2 最小关闭条件：

1. `READY_FOR_CODEX=YES` 前，Codex 开始实质执行所需的 Planner 决策、Critic 审查、必要用户产品/授权选择全部完成；
2. Codex 收到 kickoff 后可以进入已批准范围的实质执行，而不是只 probe 后才发现前置决策；
3. 正常 task-local read / preflight 不被机械禁止；
4. 实现完成后的既有 Reviewer / Terra / Verifier 后置审查不会因此阻止 kickoff；
5. 没有新增 execution segment、角色、状态机或 review protocol。

原 v0.1 的以下点保持冻结，不要求下一轮重新审：

- 正常使用六问；
- PASS 范围与未证明边界；
- 非终态唯一下一跳；
- 所有实质 PASS 的比例化用户机制说明；
- 有限同因果机制一跳检查；
- owner-first / 反过度设计；
- 简单连续的人类版本规则。

## 10. 实施边界

本 v0.2 只有在独立 Critic 对 B1、B2 及其直接回归复核 PASS 后，才能修改正式合同。

若 PASS，实施仍只修改：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`

合同版本仍建议从 1.4 升到 1.5，表示同一角色体系内的兼容行为完善，不改变 Planner / Critic 的基本职责分工。

不需要 Codex 工作流插件改版，不需要 Bridge 发布，不需要新增自动化。
