# ChatGPT Web 协作回归记录：2026-10 十类问题

日期：2026-10-17  
状态：原十类历史问题保留；Planner/Critic 1.7、Capability Gate Policy 1.2 与 2026-10-19 Project setting 已生效；两项复杂真实回归已完成，PASS integrity 治理候选已接受
主要适用层：AI Research Stack Project setting、Planner 角色合同、Critic 角色合同  
非默认 owner：`workflow-core`、具体领域 Plugin/Skill、Bridge Kit

## 定位

本文件记录的是 2026 年 10 月以来 AI Research Stack 在 ChatGPT Web 长期协作中暴露出的用户侧问题。它们首先属于网页端项目设置与 Planner/Critic 合同，而不是 Codex 侧 `workflow-core` 的生产行为。

具体项目与组件只作为真实证据：Bridge Kit / Persistent Run、Longleaf / Slurm、Clear Writing、Research Authoring、Reviewed Handoff、Codex handoff、DII 文稿及相关审查轮次。后续只有当某一问题被证明属于具体运行实现时，才回到对应 canonical owner 修复；不得因为这些例子出现过，就把本文件整体下沉到某个 Plugin/Skill。

## 九类真实问题

### 1. Critic PASS 缺少正常用户路径的反证强度

若一个方案已经 PASS，但用户随后只需追问“怎么启动、运行中怎么看、断线后怎么办、哪些自动环节真实存在、失败后谁接手”，就能快速发现关键缺口，那么问题不只是某个实现字段没写全，而是 Critic 的 PASS 本身不够可信。

审查不能只证明文档、字段、权限、状态、恢复说明、测试或执行包存在；必须判断普通用户沿正常路径真正使用时，核心承诺是否闭合。

### 2. PASS 对象和结论范围会发生语义膨胀

“某份 Proposal / Plan 在当前阶段可接受”不能逐渐被解释成“机制已经设计完整”“工作流已经可用”或“产品能力已经成立”。

每次 PASS 必须让用户知道它只证明到哪一层，以及明确没有证明什么。设计可行、可交 Codex、实现完成、正常入口可用、正式发布完成是不同结论。

### 3. 内部角色体系泄漏给用户，用户被迫成为角色路由器

当前不同流程同时出现 Planner、Critic、Reviewer、Verifier、Terra、Executor 等角色。仓库内部可以保留必要的机器身份，但 ChatGPT Web 不应要求用户自己理解这些差异并判断“下一段到底发给谁”。

用户侧人工接收方应尽量稳定、少而清楚。内部自动角色若真实存在，应由系统自己承担路由，不把角色选择转嫁给用户。

### 4. 非终态回复只报告“不能继续”，没有负责把任务送到下一入口

真实失败包括：REVISE、BLOCKED、自动审查轮次耗尽或等待外部角色后，回复只解释为什么不能继续，却没有确定唯一下一接收方、没有说明为什么是该角色、没有直接生成完整可复制提示词，也没有证明自动接手机制真实存在。

用户不应在每次失败后再额外追问“那下一步给谁、发什么”。

### 5. 所谓 Codex handoff 实际并不 execution-ready

当回复明确说“给 Codex”“Kickoff”或“开始执行”时，用户合理预期 Codex 收到后能开始完成当前批准范围。

但近期多次交接在 Codex 端才发现仍缺 Planner / Critic / Reviewer 前置步骤、未冻结的产品/架构决定、未验证的自动任务或其他人工判断。此时问题不是 Codex 执行失败，而是 handoff 在发出前就不真实。

### 6. 单点修复后缺少有限同簇检查，导致连续地鼠式回归

一个真实失败若已经证明某个职责、状态转换、授权边界、恢复路径或交接入口存在设计缺口，关闭当前 blocker 前应检查同一机制簇的相邻路径。

这不是要求每次做全系统审计，而是避免只修当前显式症状，随后让用户通过自然追问继续发现结构相同的问题。

### 7. 职责 owner 判断和复杂度约束不够有效

同一根类问题有两种表现：

- 某个能力发现相邻 Plugin/Skill 的问题后，容易越过 owner 边界去修改或承担对方职责；
- 运行、调度、持久化、监控等问题一出现，就容易新增路由器、watcher、状态机、长期服务或控制层，即使已有调度器、平台原生机制或明确 owner 可以承担职责。

默认顺序应是先找当前真实 owner，再判断已有机制能否适配；新增控制层必须有具体不可由现有 owner 轻量解决的缺口。

### 8. 内部版本、候选、轮次和定位符侵入用户阅读层

`C'`、`C11`、`R0` 等内部标识可以保留作历史或机器定位，但不应成为用户理解方案的主要版本体系。

面向用户的新方案和版本应采用稳定、简单、可预测的命名；内部定位符只作为附属信息。用户不应为了理解“现在是哪一版”而先学习一套临时编号体系。

### 9. PASS 缺少“我到底批准了什么”的用户级解释

用户通常不会逐轮重读长 Proposal / Plan / Critic 文档。一次重要 PASS 不能只给 PASS、commit、路径和 Codex kickoff，还必须把已经批准的关键机制用自然中文讲清楚。

用户至少应理解会影响实际使用的内容：主要机制怎样工作、默认行为是什么、哪些事项可以逐任务配置、危险动作究竟在哪一层被拦截、失败和恢复如何发生、用户运行时会看到什么，以及哪些能力仍未实现。

真实例子包括：

- ETA / 进度通知方案通过时，用户需要知道邮件或通知接口实际在哪里、默认是否启用、每个任务能否分别配置完成后是否发送邮件、阶段进度和最终完成通知如何区分；
- Slurm / routing 方案通过时，用户需要知道 `scancel` 等危险动作究竟由什么真实机制阻断，例如 Host Policy、hook、wrapper、审批入口或其他实现，而不是只看到“有安全边界”。

这些例子不意味着所有任务都必须有邮件、Slurm hook 或固定实现。通用要求是：PASS 必须让用户真正理解重要批准内容，而不是要求用户重新阅读大量内部材料。

### 10. 批准前 Kickoff 控制面泄漏到批准后 Codex handoff

真实失败表明，execution-ready PASS 之后如果仍机械全文复制 frozen Kickoff artifact，会把 `DRAFT ONLY`、`NOT_AUTHORIZED`、"仅在 Critic PASS 后执行"、审查历史、blocker closure 和其他批准前控制面文本重新塞回用户真正要发给 Codex 的提示词。即使 Project setting 已要求 Codex handoff 简短、只指向当前批准任务，只要中央 Critic 合同仍要求 verbatim Kickoff，这个失败就可以在全新 thread 中复现。

正确职责边界是：

- Kickoff Draft 是 execution-ready 审查的冻结执行范围与授权来源，可以保留内部生命周期元数据；
- execution-ready PASS 后的用户 Codex handoff 是该冻结包的**用户阅读层渲染**，不是 artifact 全文；
- handoff 只保留任务、approved locators、必要执行定位/当前授权和停止条件；
- 历史 task-specific prompt 中的"逐字输出 approved Kickoff"只能解释为 scope 不得漂移，不能覆盖中央用户侧 handoff 规则；
- 如果无法在不猜测、不遗漏必要授权、不改变 scope 的情况下生成短 handoff，应在 PASS 前 REVISE，而不是把内部 artifact 整份交给用户。

本问题的 canonical owner 是 Planner / Critic Role Contract；Project setting 已经有正确的短 handoff 顶层原则，不应继续堆同义规则。具体 Kickoff artifact 只负责保存其任务自己的冻结执行语义，Bridge Kit 不是默认 owner。

## 用户侧影响

这些问题共同造成四类直接损失：

1. 用户看到 PASS 后仍需亲自继续追问，等于再做一遍架构审计；
2. 用户承担本应由工作流处理的角色路由、恢复和下一步选择；
3. 一个任务在非终态处经常突然断裂，需要额外对话才能继续；
4. 用户可能已经准备授权执行，却并不清楚最终机制实际会怎样工作。

## 后续设计边界

本文件记录问题与已经形成的长期行为边界，不要求每个历史任务重写冻结 artifact。

当前角色合同已经推进到 1.6：在 1.5 的用户侧角色模型与 Codex 前置依赖语义基础上，新增批准后短 Codex handoff 规则，明确禁止把批准前 Kickoff 控制面全文泄漏到用户执行入口。

后续应优先检查和修改：

- 当前 AI Research Stack Project setting；
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`；
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`。

只有当进一步取证证明某个问题属于具体运行实现，才进入 Bridge Kit、某个领域 Plugin/Skill 或其他 canonical owner。

当前不计划为了这九类问题新增顶级 Plugin、Skill、工作流、数据库、watcher、daemon、状态机或统一控制层；也不默认要求 `workflow-core` 承担 ChatGPT Web 项目协作规则。

## 2026-10-19：PASS 可信度新增事故与中央合同收口

Bridge Kit 的用户追问暴露出三个相连缺口：机器级共享 Notifier 被退成每仓库邮箱配置；Persistent Run 与 Notifier 虽分别存在，关键调用却未接通；预计完成时间可以长期保持 `UNKNOWN`，以保守输出掩盖正向能力没有发生。问题不是缺少一个字段，而是批准前没有把完整用户承诺、正常入口的跨组件成功链和正向结果一起审透。

Slurm Workflows 的事故表明，受保护取消的判断逻辑存在，不等于正式 Codex Hook 的 Python/runtime 启动失败时危险底层动作已被阻断。安全承诺必须从正常入口直接验证最关键的失败链，不能用组件单测或“设计为 fail-closed”代替实际阻断证据。

本轮长期边界归属中央 Planner、Critic 与 Capability Gate 合同，而不把这两起事故的治理责任下沉给 Bridge Kit、Slurm 或 `workflow-core`：

1. 首个正式 Proposal 保留稳定用户承诺；中间设计审查只给 `PROCEED / REVISE`，唯一 Critic 级 `PASS` 只能在完整 execution-ready 审查并与 `READY_FOR_CODEX=YES` 同时出现。最终审查重新看完整承诺和执行包，不被旧 blocker 清单缩窄。
2. Gate 要从正常入口看到核心正向行为、跨组件完整成功链和按风险选择的关键失败链；`UNKNOWN`、fallback、未配置、fail-closed 或各组件单独通过不能冒充整体能力。检查数量由承诺和风险决定，不造全故障矩阵。
3. 每轮 Planner/Critic 先给一屏独立可读的自然中文摘要，再给精确机器交接；Clear Writing 只检查用户摘要的表达，不改写机器块。
4. 冻结范围内的漏接、配置、runtime/loader、测试/CI 和 Gate 失败默认 `RETURN_TO_CODEX`，继续同一任务；只有用户承诺、架构 owner、权限、验收或恢复语义必须变化才回 Planner，旧批准不覆盖新语义。
5. 实现后最终评估前的独立安全门仍在，但结论为 `PROCEED_TO_FINAL_EVALUATION / REVISE`，不再产生第二个 Critic 级 `PASS`；最终候选接受与正式发布分别如实说明，不造新持久状态。

本文件只记录历史事故和合同层的防复发边界，不声称 Bridge/Slurm 产品运行实现已经修复。2026-10-19 Project setting 已由用户手动替换并记录为当前生效快照。本轮不新增第三个人工角色、数据库、watcher、daemon、ledger 或状态机。

## 2026-10-20：两项复杂真实回归完成

最终新鲜回归选择了两个用户明确不信任其既有“冻结/通过”结论的复杂任务：

1. Delivery Assurance 七仓架构；
2. STAT5060 Validator Architecture 与后续 GPT Work 实施提示词。

两个独立 Critic 均返回 `REVISE`，并分别发现了此前未充分闭合的真实问题。Delivery Assurance 审查发现七仓正式覆盖不足、adapter 可遗漏降级、authority locator 漂移、DA-G10–DA-G15 仍过粗，以及逐仓声明上限未冻结；STAT5060 审查发现“有 owner”不等于语义强制链完整、现有 handoff 不是安全 GPT Work 执行包、历史三页 Guide 实际可恢复，以及若干关键正反控制仍未物化。

这两个结果支持本治理任务的目标：复杂设计不能因为历史 PASS、文件存在、映射数量完整、测试通过或“DESIGN FROZEN”就被批准；Critic 应重新读取当前事实、完整用户承诺、正常成功链、跨组件连接、风险匹配失败链与实际执行入口，并把可恢复缺口转换为具体 closure/recovery 工作。用户不应再靠自然追问承担第二次架构审计。

详细记录：
- `results/chatgpt-web--pass-integrity/DELIVERY_ASSURANCE_FRESH_CRITIC_REGRESSION_2026-10-20.md`
- `results/chatgpt-web--pass-integrity/STAT5060_VALIDATOR_FRESH_CRITIC_REGRESSION_2026-10-20.md`
- `results/chatgpt-web--pass-integrity/FINAL_CLOSURE_2026-10-20.md`

本治理候选据此记为 `CANDIDATE_ACCEPTED`。未来若 Critic 又退化为只复述方案、只关旧 blocker、只看 schema/测试/映射数量，或仍需用户追问才能暴露核心空白，应视为治理回归并重新执行审查，而不是接受其结论。
