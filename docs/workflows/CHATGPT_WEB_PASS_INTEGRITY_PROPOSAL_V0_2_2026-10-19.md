# ChatGPT Web PASS 可信度与用户控制修复 — Proposal v0.2

日期：2026-10-19  
任务键：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`work/chatgpt-web--pass-integrity`  
设计基线：`main@8b060627ee51f89c179436ea3e96b34ff58c594b`  
上一版：`docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_1_2026-10-19.md`  
阶段：DESIGN_PROPOSAL / CRITIC_REQUIRED / NO_IMPLEMENTATION

## 1. 目标

修复当前 Planner–Critic 协作中已经被 Bridge Kit 与 Slurm Workflows 反复证明的系统性问题：

- 多轮返修后，审查容易逐渐退化成只检查上一轮 blocker；
- Critic 可以对 Proposal 或执行包给出 PASS，但用户最关心的完整产品路径仍可能没有闭合；
- Codex 实现后才暴露关键调用没接、配置层级写错、正向能力没有真正发生或正式运行入口根本不能工作；
- 用户必须靠自然追问继续承担架构审计；
- “PASS”被用于多个阶段，用户无法仅凭该词判断到底只是设计方向可以继续，还是已经真的可以交 Codex。

v0.2 在 v0.1 基础上接受用户新的明确决定：**Critic 级别的 PASS 在一个设计执行闭环中只允许出现一次，而且只允许出现在最终 execution-ready 审查。**

本轮只修改 ChatGPT Web 项目协作合同与正式 Plugin Capability Gate 规则，不新建 Plugin、Skill、Reviewer、状态机、数据库、watcher、daemon 或中央控制层，不修改 Bridge Kit、Slurm Workflows 或 Delivery Assurance 产品代码。

## 2. 本轮用户承诺基线

这组承诺是后续 Proposal / Plan / Critic prompt 不得静默弱化的稳定基线。除非用户明确改变要求，否则后续版本必须保持这些语义。

1. **Critic 级 PASS 只允许出现一次。** 只有最终 execution-ready 审查可以给 PASS；它必须与 `READY_FOR_CODEX=YES` 同时成立，并直接给出最终可发送的 Codex kickoff/handoff。
2. **设计中间轮次只能给 PROCEED 或 REVISE。** PROCEED 只表示当前对象足以进入下一设计阶段，不表示整体架构已经闭合，不授权 Codex。
3. **最终 PASS 不能只复核上一轮 blocker。** 中间返修可以窄审，但最终 execution-ready 审查必须重新对照完整用户承诺、当前 Proposal/Plan/Goal/Kickoff 和正常用户路径。
4. **最终 PASS 的语义必须足够强。** 它表示：用户要求已经被充分翻译成冻结的产品行为、架构边界、配置归属、关键调用关系、验收和恢复语义；不存在需要 Codex 自己决定的产品、架构、权限或验收空白。Codex 仍可在这些冻结约束内自行选择普通实现细节。
5. **用户不再负责二次架构审计。** 如果最终 PASS 后，用户一句自然追问“到底怎么工作、谁调用谁、配置在哪里、失败后怎么办”就能发现核心设计缺口，则这次 PASS 本身不合格。
6. **最终 PASS 必须让用户知道实际架构。** 不能只给 commit、路径和 prompt；必须先用一屏内自然中文说明主要机制、默认值、逐任务配置、关键调用关系、失败恢复和仍需未来授权的外部动作。
7. **核心能力必须有正向发生要求。** `UNKNOWN`、fallback、未配置、失败关闭只能证明安全退化，不能单独证明用户要求的能力已经实现。
8. **跨组件用户承诺必须做端到端验证。** 若用户要求本身跨多个组件，不能把每个组件分别验证后假定中间连接存在。
9. **实现缺陷默认留在同一 Codex 任务修复。** 漏接调用、配置层级错误、运行时启动失败、普通测试/Gate failure 不自动退回 Planner。
10. **用户不读内部审查流水账。** Critic 可保留 finding ID 和完整技术依据，但用户可见正文必须先说明真正的问题和实际影响。

## 3. 为什么只保留一次 PASS

当前合同虽然已经要求“PASS 只对当前阶段有效”，但用户仍然会自然把 PASS 理解成“这个东西已经审清楚了”。把同一个词用于“设计方向可继续”“执行包可交 Codex”“最终候选可接受”等不同语义，本身就是持续制造误解。

因此本轮把 Critic 级结论简化为：

### 设计阶段

- `PROCEED`：当前设计对象足以进入下一步，但仍未完成 execution-ready 闭合。
- `REVISE`：存在必须关闭的真实 blocker。

设计 Proposal 本身即使完全合理，也只能得到 `PROCEED`，下一步仍由 Planner 把它整理成完整执行包。

### 最终 execution-ready 审查

- `PASS`：唯一一次。必须同时满足 `READY_FOR_CODEX=YES`，并直接生成最终 Codex kickoff/handoff。
- `REVISE`：任一用户承诺、关键调用关系、配置归属、验收、恢复、权限或执行语义仍存在空白。

禁止 `PASS BUT...`、`PASS_WITH_CONDITIONS`、先 PASS 再让 Codex 探索关键架构等模糊状态。

### Codex 实现以后

不再给第二次 Critic 级 PASS。使用与真实阶段一致的结论，例如：

- `RETURN_TO_CODEX`：批准范围内的实现缺陷，回同一 Codex 任务修；
- `CANDIDATE_ACCEPTED`：最终候选的 required Gate 与正常入口证据成立；
- `RELEASE_READY`：发布前条件已经闭合；
- `RELEASED`：正式发布/安装身份已核实。

现有 Gate/schema 内部若已有机器值 `PASS`，可以保持兼容；但它不能作为 ChatGPT Web Critic 的用户级结论，也不能被写成“Critic PASS”。

## 4. 已核实的当前缺口

当前 Planner/Critic 1.6 已经包含五遍预检、正常使用六问、Critic 的“正常用户路径能否问穿方案”、execution-ready 完整包和 PASS 后用户说明。Project setting 也已经强调真实能力与正常入口。

仍有四个结构缺口：

### A. 最终审查责任可以被 handoff prompt 事实上收窄

返修轮次里“优先复核旧 finding”是合理的，但 Planner 生成的窄 Critic prompt 不能缩小最终 execution-ready 审查责任。否则最初用户承诺会逐轮退出工作集。

### B. 正常用户路径没有绑定稳定用户承诺源

Critic 如果只对照当前 Proposal，就可能形成“Proposal 自己定义范围、Critic 再按这个范围判它正确”的局部自洽。必须有一个稳定的用户承诺基线贯穿所有版本。

### C. Gate Policy 缺少正向义务和跨组件承诺

当前 Gate Policy 已经要求 normal entry、正例、负例、should-not-change 和最终候选一致性，但仍可能把跨组件用户要求拆散后分别通过，或者让安全 fallback 永久替代本应出现的正向能力。

### D. PASS 用户说明还不等于真实产品说明

用户真正需要知道的是配置在哪里、谁调用谁、默认行为是什么、成功时发生什么、失败后怎么办，而不是 finding 编号、commit 和内部状态。

## 5. 方案

### 5.1 首个正式 Proposal 内冻结简短用户承诺基线

每个需要 Planner–Critic 的 major round / 实质产品设计，首个正式 Proposal 必须包含少量稳定用户承诺。

默认不新增独立需求账本。后续版本必须保持这些语义；只有用户明确改变要求时，才能记录变更。

小设计通常 3–5 项，复杂设计通常 5–12 项，不机械追求数量。

### 5.2 中间审查可窄，最终 PASS 必须完整回看

Critic 合同新增不可被 task-specific prompt 覆盖的规则：

- 中间 blocker closure / rebuttal 可以围绕旧 finding；
- 这些轮次只能给 `PROCEED` 或 `REVISE`；
- 最终 execution-ready 审查必须重新读取当前完整 Proposal/Plan/Goal/Kickoff、用户承诺基线和必要原始用户证据；
- 必须重新问穿完整正常路径及跨组件连接；
- 只有该轮能够给唯一一次 `PASS`。

这不是全仓审计。读取范围仍服从 AGENTS 的上下文预算，只覆盖当前承诺及其一跳实现链。

### 5.3 唯一 PASS 的强语义

最终 PASS 必须同时证明：

- 所有用户承诺均有明确 owner；
- 配置层级已经冻结；
- 跨组件调用关系已经冻结；
- 默认值和逐任务覆盖已经冻结；
- 正常成功行为已经定义；
- 必要失败/恢复行为已经定义；
- Capability Gate 能验证这些行为；
- 需要用户另行授权的外部动作已经明确隔离；
- Codex 不需要再做产品/架构/权限/验收选择。

允许留给 Codex 的只有不改变上述语义的普通实现细节，例如具体 helper 拆分、局部库选择、临时文件命名和等价代码结构。

### 5.4 最终 PASS 前必须给一屏真实架构说明

最终 Critic 在输出 PASS 和 Codex handoff 前，必须直接用自然中文说明：

- 用户怎样触发；
- 关键配置属于机器 / repo / task / run 哪一层；
- 谁调用谁；
- 默认行为和可配置项；
- 正常成功时必须发生什么；
- 失败后怎样退化或恢复；
- 哪些真实外部动作仍需后续授权。

如果 Critic 无法准确写出这段说明，则不得 PASS。

### 5.5 Gate Policy 增加两条硬规则

**正向能力义务：** 对产品明确声称会发生的核心能力，至少一个 final-candidate normal-entry case 必须实际观察到该正向行为。安全 fallback / UNKNOWN 不能成为唯一证据。

**跨组件承诺义务：** 如果用户承诺本身是端到端链路，则至少一个 Gate 或同一 Gate 的完整场景必须覆盖整条链，不能只靠各组件分别通过来推断集成成立。

这直接覆盖：

- ETA 永远 UNKNOWN 却声称支持 ETA；
- Notifier 自己会发邮件、Persistent Run 自己会运行，但 Persistent Run 从未调用 Notifier；
- Hook 检查器自身测试通过，但 Codex 正常入口因运行时启动失败而绕过保护。

### 5.6 实现失败默认留在同一 Codex 任务

留在原 Codex 任务修复：

- approved 行为漏实现；
- 调用没有接通；
- 配置 scope 写错；
- runtime / PATH / loader /依赖启动错误；
- deterministic test / CI /已批准 Gate failure；
- 同一因果的一跳回归。

只有以下情况回 Planner：

- 用户承诺需要改变；
- canonical owner / 架构边界需要改变；
- Gate 的成功定义需要改变；
- 新 provider / 数据 / 凭据 / 费用 / live-global / destructive 权限；
- recovery semantics 需要改变；
- 已批准平台机制经证据证明不可实现。

### 5.7 REVISE 与 PROCEED 的用户层保持短

完整 finding ID、路径、证据和关闭条件继续保存在审查文档和下一角色 prompt 中。

用户可见正文优先说明：

- 当前阶段能不能继续；
- 真正卡在哪里；
- 为什么影响实际使用；
- 是否需要重做架构；
- 用户现在是否需要做任何事情；
- 下一步唯一入口。

## 6. 拟修改的 canonical owner

Critic 对本 Proposal 给出 `PROCEED` 后，Planner 才可以形成执行包，计划修改：

1. `docs/workflows/PLANNER_ROLE_CONTRACT.md`：加入稳定用户承诺基线、`PROCEED/REVISE` 设计阶段语义、实现失败分流。
2. `docs/workflows/CRITIC_ROLE_CONTRACT.md`：改为 Critic 级 PASS 只在 execution-ready 审查出现一次；加入最终完整回看、一屏真实架构说明和后实现结论命名。
3. `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`：加入正向能力义务与跨组件端到端承诺。
4. AI Research Stack Project setting：只准备短增量，不复制中央合同全文；实际 Web setting 仍需用户最终替换/确认。
5. `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`：追加 Bridge/Slurm 新证据与本轮 closure，不改写历史。

不修改 Bridge Kit、Slurm Workflows、Delivery Assurance、workflow-core 或 Clear Writing 的生产行为。

## 7. 修改后的正常工作流

```text
用户给目标
→ Planner 冻结用户承诺基线
→ Critic 审设计
   ├─ REVISE：回 Planner 修
   └─ PROCEED：允许 Planner 形成完整执行包
→ Critic 对完整 Proposal + Plan + Goal + Kickoff 做最终 execution-ready 审查
   ├─ REVISE：回 Planner
   └─ PASS：唯一一次；READY_FOR_CODEX=YES；直接给最终 Codex kickoff
→ Codex 实现
   ├─ 普通实现/Gate failure：RETURN_TO_CODEX，同一任务修
   └─ 只有架构/用户承诺/权限等实质变化才回 Planner
→ 最终候选：CANDIDATE_ACCEPTED
→ 发布前：RELEASE_READY
→ 发布完成：RELEASED
```

这样用户看到 PASS 时，含义永远只有一个：**架构和执行包已经彻底闭合，可以把当前 handoff 发给 Codex；不再有需要 Codex 自己猜的产品/架构决定。**

## 8. 反证检查

本方案不新增：

- 第三个人工角色；
- requirements database / ledger / matrix service；
- 新顶级工作流；
- 新状态机；
- Bridge Kit 控制面；
- 每轮全仓重新审计。

它只收紧现有 Planner / Critic / Capability Gate 的 verdict 语义和最终批准责任。

## 9. 外部现实核查

成熟软件验证实践强调用户要求贯穿设计、实现和测试，并用端到端运行场景验证接口与完整链路。

本方案只采用两个原则：

- 用户要求不能在多轮设计中失去追踪；
- 跨组件承诺必须由完整运行场景证明。

不引入重型需求矩阵体系。

## 10. Critic 本轮必须回答的问题

本轮 Critic **不得给 PASS**，因为现在只是 Proposal 设计审查。结论只能是 `PROCEED` 或 `REVISE`。

必须独立回答：

1. Critic 级 PASS 只保留给最后 execution-ready 审查，是否比当前多阶段 PASS 更清楚、更符合用户理解？
2. `PROCEED` 是否足以表达“这个设计阶段可以继续”，又不会让用户误以为功能或整个执行合同已经完成？
3. 唯一 PASS 的强语义是否真正保证：所有会改变产品、架构、权限、验收的空白都已在 Codex 前关闭，同时仍允许 Codex 决定普通实现细节？
4. 最终 PASS 前重新对照完整用户承诺，是否能防止多轮返修后只剩局部 blocker 审查？
5. Bridge 与 Slurm 的真实事故是否会被新的正向能力 + 跨组件完整路径要求提前拦住？
6. 实现失败默认回同一 Codex task，是否能减少无意义 Planner 往返，又不会绕过真正的重新设计？
7. 后实现阶段改用 `RETURN_TO_CODEX / CANDIDATE_ACCEPTED / RELEASE_READY / RELEASED` 是否比再次使用 Critic PASS 更清晰？
8. 是否存在更简单但同样能关闭这些事故的方案？

## 11. 当前权限与下一步

本轮只提交 Proposal v0.2，不修改正式合同、不修改当前 ChatGPT Web Project setting、不实施产品代码。

AI Skills Maintenance tracking 仍受当前维护看板约束；当前 surface 没有真实 Clear Writing + GitHub Project mutation 的组合入口，因此暂不创建 reader-facing tracking Issue，不要求用户手工维护。

下一入口：独立 Critic 做 Proposal v0.2 设计审查；其结论只能是 `PROCEED` 或 `REVISE`。
