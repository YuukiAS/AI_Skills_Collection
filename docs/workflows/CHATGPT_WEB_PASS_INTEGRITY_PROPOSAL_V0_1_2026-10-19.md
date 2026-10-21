# ChatGPT Web PASS 可信度与用户控制修复 — Proposal v0.1

日期：2026-10-19  
任务键：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`work/chatgpt-web--pass-integrity`  
设计基线：`main@8b060627ee51f89c179436ea3e96b34ff58c594b`  
阶段：DESIGN_PROPOSAL / CRITIC_REQUIRED / NO_IMPLEMENTATION

## 1. 目标

修复当前 Planner–Critic 协作中一个已经被 Bridge Kit 与 Slurm Workflows 反复证明的系统性问题：

- Planner/Critic 多轮返修后，审查容易逐渐退化为“只检查上一轮 blocker”；
- Critic 可以对 Proposal 或 execution package 给 PASS，但用户最关心的完整产品路径仍可能没有被问穿；
- Codex 实现后才暴露核心连接、配置归属、正向能力或运行时链路根本没做；
- 用户必须靠自然追问继续承担架构审计；
- PASS 对用户而言缺少明确阶段含义，且大量内部 finding / locator / 状态字段增加阅读负担。

本轮只修 ChatGPT Web 项目协作合同与正式 Plugin Capability Gate 规则，不新建 Plugin、Skill、Reviewer、状态机、数据库、watcher、daemon 或中央控制层，不修改 Bridge Kit、Slurm Workflows 或 Delivery Assurance 产品代码。

## 2. 本轮用户承诺基线

这组承诺是本任务后续 Proposal / Plan / Critic prompt 不得静默弱化的稳定基线。除非用户明确改变要求，否则后续版本必须保持这些语义。

1. **最终设计 PASS 不能只复核上一轮 blocker。** 中间返修可以窄审，但任何最终设计通过或 execution-ready 通过，都必须重新对照本任务的完整用户承诺和正常用户路径。
2. **用户不再负责二次架构审计。** 如果一句自然追问“到底怎么工作、谁调用谁、配置在哪里、失败后怎么办”就能发现核心缺口，则前一个 PASS 视为审查失败。
3. **PASS 必须让用户知道实际架构。** 不能只给 PASS、commit、路径和下一段 prompt；必须用一屏内的自然中文说明主要机制、默认值、逐任务配置、关键调用关系、失败恢复、尚未实现项。
4. **核心能力必须有正向发生证据。** `UNKNOWN`、fallback、未配置、失败关闭只能证明安全退化，不能单独证明用户要求的能力已经实现。产品声称会产生 ETA，就必须有代表性正常任务真的出现 ETA；产品声称 Persistent Run 会通知，就必须真实走通 Persistent Run → Notifier。
5. **跨组件用户承诺必须做端到端验证。** 若用户要求本身跨多个组件，不能把每个组件分别 PASS 后假定中间连接存在。
6. **实现缺陷默认留在同一 Codex 任务修复。** 漏接调用、配置层级错误、运行时启动失败、普通测试/Gate failure 不自动退回 Planner。只有修复需要改变本基线、架构 owner、验收语义、权限/数据/费用/恢复边界，或证明平台假设根本不可行时，才回 Planner–Critic。
7. **用户不读内部审查流水账。** Critic 可以保留稳定 finding ID 和完整技术依据，但面向用户先给消化后的结论；不能要求用户逐条读几十个 blocker 才理解问题。
8. **阶段必须显式。** 面向用户不得裸用“PASS”表示所有层次。至少区分“设计方案通过”“执行包通过”“最终候选通过”“正式发布完成”；机器字段可继续保留 `CRITIC_RESULT=PASS`。

## 3. 已核实的当前缺口

当前 Planner/Critic 1.6 已经包含五遍预检、正常使用六问、Critic 的“正常用户路径能否问穿方案”、execution-ready 完整包、PASS 后用户说明等正确要求；Project setting 也已经强调真实能力、正常入口和用户阅读层。

问题不是完全没有规则，而是四个缺口仍允许真实事故发生：

### A. 最终复核责任可以被 handoff prompt 事实上收窄

当前合同要求后续轮次“优先处理旧 finding 与新改动影响”，但没有明确规定：**最终设计 PASS / execution-ready PASS 的责任范围不能被 Planner 生成的窄 prompt 缩成旧 finding closure。**

因此返修几轮后，最初用户承诺可能退出 Critic 的工作集。

### B. “用户路径问穿”没有绑定稳定的用户承诺源

Critic 被要求问正常入口，但没有一个在多轮 Proposal 之间保持稳定的最小用户承诺基线。结果 Critic 很容易拿当前 Proposal 自己定义的产品范围去验证当前 Proposal，形成局部自洽。

### C. Gate Policy 缺少“正向义务”和“跨组件承诺”规则

当前 Gate Policy 已要求 normal entry、正例、负例、should-not-change、最终候选一致性，但仍允许把一个跨组件用户承诺拆散成几个分别可 PASS 的 Gate，或者让安全 fallback 长期替代本应出现的正向能力。

### D. PASS 用户说明仍然偏“解释审查结果”，而不是“复述实际产品”

Critic 1.6 已要求比例化用户说明，但没有强制它以真实调用关系和配置归属回答“这个东西到底怎么工作”。因此仍可能出现用户看到 PASS，却不知道 Hook、Notifier、Persistent Run、ETA 等核心机制实际怎样连接。

## 4. 方案

### 4.1 不新增默认 artifact：在首个正式 Proposal 内冻结“用户承诺基线”

每个需要 Planner–Critic 的新 major round / 实质产品设计，首个正式 Proposal 必须有一段简短的“用户承诺基线”。

默认不新增独立需求账本或矩阵文件。后续 Proposal 版本必须：

- 逐项保持基线语义；
- 用户明确改变要求时，单独记录哪一项改变、为什么改变；
- Critic 发现 Proposal 与基线冲突时，以用户当前要求为准，给 REVISE；
- Planner 不能通过改写 Critic prompt 静默缩小这组承诺。

小设计可只有 3–5 项，复杂设计通常 5–12 项；不机械追求数量。

### 4.2 中间复核可窄，最终 PASS 必须全量回看

Critic 合同新增一条不可被 task prompt 覆盖的规则：

- blocker closure / rebuttal 中间轮次可以主要审旧 finding；
- 但任何 **DESIGN PASS** 或 **READY_FOR_CODEX=YES** 前，Critic 必须重新读取当前完整 Proposal/执行包、用户承诺基线和必要原始用户证据；
- 必须重新问穿完整正常用户路径和跨组件连接；
- Planner prompt 中的“只审 F01–F04”只能限制中间轮次，不得缩小最终 PASS 责任；
- 新 blocker 仍只允许来自真实遗漏、新改动回归、安全/执行不可行，不允许用“还能更好”移动终点。

这不是全仓审计。读取范围仍服从 AGENTS 的上下文预算，只要求覆盖当前用户承诺及其一跳实现链。

### 4.3 PASS 改为阶段化用户结论

机器状态不变，但用户可见首句必须说明具体阶段：

- 设计通过：架构和验收设计足以进入执行包；功能尚未实现。
- 执行包通过：可以交 Codex 开始批准范围内实现；功能尚未通过最终验收。
- 最终候选通过：同一候选已经通过要求的正常入口 Gate；仍未自动代表正式发布。
- 发布完成：正式安装/发布身份已经核实。

禁止只写“PASS，可以做了”而让用户自行推断是哪一层。

### 4.4 每次实质 PASS 必须给“一屏真实架构说明”

复杂任务的 PASS 用户说明必须直接回答当前对象真正相关的内容：

- 用户怎样触发；
- 关键配置属于机器 / repo / task / run 哪一层；
- 谁调用谁；
- 正常成功时必须实际发生什么；
- 失败时怎样退化或恢复；
- 当前仍有什么没实现、没验证或需用户授权。

不要求固定标题，不要求重复 Plan。目标是用户看完无需再追问“所以到底怎么工作”。

例如 Bridge 类问题应能直接说清：
`Persistent Run → shared Notifier → one-shot Clear Writing → transport`，以及邮箱配置属于机器级还是 repo 级。

Slurm 类问题应能直接说清：
`Codex tool call → user-level Hook → protected scancel detection → current-chat confirmation → exactly-once execution`，以及 Hook/runtime 损坏时是否 fail closed。

### 4.5 Gate Policy 增加两条硬规则

**正向能力义务：** 对产品明确声称会发生的核心能力，至少一个 final-candidate normal-entry case 必须实际观察到该正向行为。安全 fallback / UNKNOWN 不能成为唯一通过证据。

**跨组件承诺义务：** 如果用户承诺本身是端到端链路，则至少一个 Gate 或同一 Gate 的完整场景必须覆盖整条链，不能只靠各组件分别通过来推断集成成立。

这两条直接覆盖：
- ETA 永远 UNKNOWN 却声称支持 ETA；
- Notifier 自己能发邮件、Persistent Run 自己能运行，但 Persistent Run 从未调用 Notifier；
- Hook 检查器本身测试通过，但 Codex 正常入口因运行时启动失败而绕过保护。

### 4.6 实现失败默认不升级为新设计轮次

Planner/Critic 合同共同冻结失败分流：

留在同一 Codex 任务修复：
- approved 行为漏实现；
- 调用没有接通；
- 配置 scope 错；
- runtime / PATH / loader /依赖启动错误；
- deterministic test / CI /已批准 Gate failure；
- 同一因果的一跳回归。

只有以下情况回 Planner：
- 用户承诺需要变化；
- canonical owner / 架构边界需要变化；
- Gate 的成功定义需要变化；
- 新 provider / 数据 / 凭据 / 费用 / live-global / destructive 权限；
- recovery semantics 需要变化；
- 已批准平台机制经证据证明不可实现。

不得用“实现失败”本身作为重新开启大设计的理由。

### 4.7 REVISE 的用户层与机器层分开

Critic 仍可在审查文档和 handoff prompt 中保留完整 finding ID、路径、证据和关闭条件。

但用户可见正文先用自然中文只回答：
- 现在真正卡在哪里；
- 为什么会影响实际使用；
- 是否需要重做架构；
- 用户现在需不需要做任何事情；
- 下一步唯一入口。

用户不需要逐条消费内部 finding 才能继续。

## 5. 拟修改的 canonical owner

Critic PASS 后，Implementation Plan 只允许修改：

1. `docs/workflows/PLANNER_ROLE_CONTRACT.md`：升级为下一版，加入用户承诺基线、最终复核不可被 handoff prompt 缩窄、实现失败分流。
2. `docs/workflows/CRITIC_ROLE_CONTRACT.md`：升级为下一版，加入最终 PASS 全量回看、阶段化 PASS、真实架构说明、用户层简化。
3. `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`：升级为下一版，加入正向能力义务和跨组件端到端承诺。
4. 当前 AI Research Stack Project setting：只准备一个短增量，不复制上述合同全文。实际 ChatGPT Web setting 仍需用户最终替换/确认。
5. `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`：追加本次 Bridge/Slurm 新证据与 closure 说明，不重写历史。

不修改 Bridge Kit、Slurm Workflows、Delivery Assurance、workflow-core 或 Clear Writing 的生产行为。

## 6. 正常用户工作流

修改后，复杂设计的主线应变成：

```text
用户给目标
→ Planner 在 Proposal 冻结少量用户承诺
→ Critic 独立审完整用户路径
→ 中间 REVISE 可围绕稳定 blocker 快速收敛
→ 最终设计 PASS 时重新对照全部用户承诺
→ Critic 用一屏中文讲清实际架构
→ execution-ready PASS 后交 Codex
→ Codex 普通实现失败留在原任务修
→ 最终候选用正向 normal-entry + 跨组件端到端证据验收
→ 再发布
```

用户仍只需要在真正的产品选择、高影响授权或无法推导的科学/业务决定上介入。

## 7. 反证检查

本方案故意不采用以下更重路线：

- 不新建“Requirements Manager”角色；
- 不新增独立 requirements database / ledger / matrix service；
- 不让 Bridge Kit 管 ChatGPT Web Planner/Critic；
- 不要求每轮都重新全量读取所有历史聊天；
- 不要求每个 Gate 增加新的编号；
- 不把 Delivery Assurance 前移成 ChatGPT Web 控制层。

原因是当前根因主要是现有 Planner/Critic/Gate 合同的批准责任没有绑定稳定用户承诺和完整正向链路；在现有 owner 内修正即可。

## 8. 外部现实核查

NASA 的软件需求验证实践要求需求贯穿设计、实现和测试保持可追踪，并验证软件在用户/客户环境中按预期工作；其端到端验证强调完整运行场景和外部接口，而不是只证明各个配置项各自可用。

本方案只采用其中两个成熟原则：
- 用户要求不能在多轮设计中失去追踪；
- 跨组件承诺必须通过完整运行场景验证。

不引入其重型文档体系或完整需求矩阵。

## 9. 本轮设计验收

Critic 必须独立回答：

1. 这套修改是否直接覆盖 Bridge 的“机器级 Notifier 被改成 repo 级、Persistent Run 未接 Notifier、ETA 可永久不出现”这类漏审？
2. 是否直接覆盖 Slurm 的“Hook 逻辑存在但正式运行时启动失败，底层命令仍执行”这类集成漏审？
3. 用户承诺基线是否足够稳定，又没有变成新的大型需求账本？
4. 最终 PASS 全量回看是否会重新制造每轮全仓审计，还是保持在当前承诺的一跳范围内？
5. 正向能力与跨组件端到端 Gate 是否会增加真实证明，而不是机械增加 Gate 数？
6. 实现失败分流是否能显著减少“Codex 一失败就退回 Planner”，同时不绕过真正的架构/权限变更审查？
7. 阶段化 PASS 和一屏架构说明是否足以让用户在执行前理解“到底会怎么工作”？
8. 是否存在更简单、仍能关闭上述真实事故的方案？

若这些问题均成立，下一阶段才允许写 Implementation Plan / Goal / Kickoff 并修改三份中央合同与 Project setting 候选。

## 10. 当前权限与下一步

本轮只提交 Proposal，不修改上述正式合同、不修改当前 ChatGPT Web Project setting、不实施任何产品代码。

AI Skills Maintenance tracking 需要 reader-facing Issue + Project mutation；当前 surface 未暴露可实际调用的 installed Clear Writing，因此按维护看板规则暂不创建 tracking Issue。后续具备 Clear Writing + Project mutation 的合法入口必须为同一任务创建/绑定 tracking Issue，Status=DOING，并把真实 issue number 回写到 canonical source。

下一入口：独立 Critic 做 DESIGN_PROPOSAL_REVIEW_V0_1。
