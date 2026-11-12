# D7 冷读

本次判断依据为当前目录的 `blueprint.json`，按接手实现两个 Assurance 插件的执行者视角阅读。结论针对设计是否足以指导开工。蓝图中的实现状态、验收状态和空的 `versions` 表明，当前仍处于待审设计阶段。

## 1. 拟开工顺序

| 顺序 | 准备完成的工作 | 蓝图依据 |
|---|---|---|
| 1 | 由 D1 收敛当前设计，完成同一受审快照的 D5 草稿检查、D6、D7、D8，关闭阻塞问题，再取得用户对该快照的批准。D8 每轮在一个新 GPT 对话中合批处理，保留逐单位文字身份和判断。 | `role-D1`、`gates`、`role-D8`、`freeze` 的 `terminal.mechanism` |
| 2 | 按首次冻结五步追加版本历史，运行 D5 冻结档并核对获批快照，写入三个身份哈希和冻结记录。新 X1 线程实际读取并接收，D1 最后一次状态提交同时切换阶段与写权，X1 回读确认。实际执行授权按任务范围核对。 | `freeze` 第 6.4–6.5 节、`writer` 第 1.3 节、`contract-authorization` |
| 3 | 开始共享文件协议工作包。建立状态、任务书、派发、结果等结构和模板，完成只读记录检查入口、身份计算、基线核对、幂等采纳、冲突与状态恢复规则。先把跨组件使用的文件合同落实。 | `minimum` 第 10.1 节、`state`、`writer`、`record-check`、`dispatch`、`prompts` |
| 4 | 完成设计端工作包。将澄清、独立设计、角色读限、四关卡、九项合同、小修继承和冻结交接接到规划入口及设计执行入口。Blueprint 检查器使用蓝图指定的固定提交。 | `clarify`、`design-roles` 及 `role-D1`–`role-D8`、`contract` 及九个子节点、`gates`、`q-checker`、`q-inheritance`、`freeze` |
| 5 | 完成交付端工作包。接入候选提案与选择、验收资产审查、三类校准、条件角色、原始证据、偏离申报、返修与设计退回、整份签发及撤回复核，同时接入实际告知与衡量记录。 | `delivery-roles` 及 `role-X1`–`role-X5`、`acceptance`、`calibration`、`candidate`、`evidence`、`deviation`、`sign`、`revision`、`metrics` |
| 6 | 用现有生成器生成两个自包含包，将预算改为 12 个插件、32 个技能，同步相关断言和回归。在同一最终规则版本上完成 Claude Code、GPT Work 的规划读取，以及安装后 Codex 执行入口的真实任务验收。X3 承担安全相关验收，X5 承担开放专业判断，X1 亲读后核对签发条件。 | `source-layout`、`planning-entry`、`execution-package`、`q-capacity`、`capability-check`、`contract-regression`、`sign` |

第 3–6 步沿用 `minimum` 已规定的四个内部工作包顺序。当前先推进第 1–2 步的设计、冻结与交接工作。

## 2. 已经明确的接缝

### 2.1 任务定位、写入与角色返回

| 接缝 | 输入 | 输出及接收方式 |
|---|---|---|
| `state` → `writer` | 已绑定的任务目录、`STATE.revision`、文件身份、目标分支头、写者身份 | 带预期基线的状态提交和同分支回读。设计阶段由 D1 写状态，交接后由 X1 写状态。 |
| `writer` → `dispatch` → `prompts` | 当前有效状态、采纳结果、暂停范围、角色条件、来源身份和读写范围 | 按七级优先顺序确定下一动作，展开完整提示词并保存派发记录。允许并行时明确给出批次，各角色保留独立提示词和写回位置。 |
| 被派角色 → 负责人 | `dispatch_id`、读取的状态修订号、角色绑定对象、适用的候选身份、实际读写清单 | 各自派发目录中的 `RESULT.json`、`RESULT.md` 和实际产物。负责人核对身份后采纳，同一结果重复返回按幂等处理。 |
| 任务记录 → `record-check` | `--task-root`、`--schema`、`--record`、`--format` 及包内预注册结构 | `assessment/errors/unresolved/checked_files`。退出值 0 表示结构与可检查引用合规，1 表示确定记录错误，2 表示无法完成检查。 |

`state.terminal.mechanism` 给出了默认任务目录、状态字段、空值规则和事件字段。`writer.terminal.mechanism` 给出了冲突、一次机械重试及回读规则。`record-check.terminal.mechanism` 固定了 Python 环境要求、依赖、记录种类和检查边界。

### 2.2 设计任务书、受审快照与冻结对象

- D1 在澄清结束时写不可变任务书 `design/briefs/<brief_version>.json`。D2、D3 读取同一份任务书，D4 也绑定相应任务书，派发使用 `based_on.brief_sha256`。提前核查时先形成问题任务书。任务书换版后，旧结果标为 `stale`，D1 判断仍可支持的范围。依据为 `clarify`、`dispatch`、`role-D2`、`role-D3`、`role-D4`。
- D5–D8 的输入为受审设计，结果共同绑定 `snapshot_sha256`。D7 的材料限于 Blueprint 和最小运输封套。D8 接收本轮复述单位，逐单位仅依据自身文字作答，记录 `reader_isolation: "single-thread-batch"`，由 D1 逐项判断。依据为 `gates`、`role-D7`、`role-D8`。
- `freeze` 接收九项合同定位、有效关卡结果、用户批准和授权引用，输出不可变 Blueprint 与 `freeze.json`。内容哈希使用 JCS 规范化后的 UTF-8 字节。`snapshot_sha256` 绑定受审与批准对象，`semantic_hash` 绑定定义内容及批准继承，`bundle_sha256` 绑定完整冻结文件的原始字节。字段范围、排除清单和首次冻结顺序均已给定。
- X1 接收冻结包、批准与授权，核对 `bundle_sha256`，写实际接收记录。D1 据此切换写权。后续交付派发绑定获批 `semantic_hash` 或完整合格小修继承链可达的值。交付期间 D1 继续负责设计决定及设计记录，由 X1 原样登记到当前状态。依据为 `freeze`、`writer`、`revision`、`q-inheritance`。

蓝图第 2.1a 节和 `e-merge` 已明确 D8 的最终修订及其替代范围，可据此生成当前规则。

### 2.3 实现、验收、证据与签发

- X2 提交实现、候选提案、验收资产提案、校准结果和偏离表。X1 选择当前候选，并审定正式验收资产引用。科研数值、统计、安全相关验收及需要换人重写的弱验收按条件交 X3。依据为 `role-X2`、`role-X3`、`candidate`、`acceptance`、`calibration`。
- 每个关键验收器实际处理正例、危险坏例和缺证例，分别预期 `passed/failed/unknown`。校准记录包含独立预期来源、实际观察及原始结果。正式证据另绑定当前候选、冻结条款、资产版本、观察对象、正常入口和原始证据定位。依据为 `calibration`、`evidence`。
- 普通实现、环境或证据问题由 X1 安排同任务处理。命中五类设计退回条件时，X1 交原 D1 决定并暂停影响闭包，其余获准工作继续。小修和大改的权限、条件、关卡影响及告知要求已由 `deviation`、`revision`、`q-inheritance` 给出。
- `sign` 接收当前最终候选、有效证据、必要角色结果和适用的用户验收，X1 亲读后逐项核对十三项条件，对整个冻结范围签发。签发后出现新事实时先进入 `X1-review-release`，再由 X1 维持或撤回整份签发。原签发保留，新签发通过 `supersedes` 关联。

### 2.4 源规则、生成包与实际宿主

`source-layout` 明确四个源入口、一份共用规则源和 13 张角色卡。现有生成器将每个执行技能复制到对应包的 `skills/execute/`，将规划正文复制到 `planning/`，将共用资源复制到 `shared/assurance/`。两个可调用技能分别命名为 `design-assurance-execute`、`delivery-assurance-execute`。

`planning-entry` 接收固定源仓库提交，或宿主已确认可读的完整包根。`execution-package` 接收有效派发，安装后通过显式入口执行角色工作。`capability-check` 要求分别取得各宿主的实际读取、运行和写回证据，`q-capacity` 已确定容量及旧能力保护边界。

## 3. 阻塞问题

**阻塞问题共 0 项。**

就蓝图覆盖的 0.1 范围，未发现必须由设计方追加裁决的产品行为、科研或验收语义、接口、权限或资源边界选择。

开工所需的冻结、批准、授权核对和 X1 接收已有明确顺序与责任人。实际任务中的 D3、D4、X3、X4、X5 启用也有条件和决定责任。缺入口、缺材料、缺原始证据或状态异常时，蓝图给出了停止、补证、恢复或退回路线，执行者可以沿这些规则处理。

## 4. 实现自由度

- 模块、函数和类怎样拆分，内部变量与文件内符号怎样命名，以及重复规则怎样在源层组织。对外字段、角色责任和生成后内容仍按各节点合同落实。依据为 `minimum`、`source-layout`、`role-X2`。
- 在蓝图允许的 Git 或 GitHub 接口内安排读写代码、基线比较和提交组织，落实预期身份核对、幂等采纳、受限重试和远端回读。依据为 `writer`。
- 将已列出的字段、枚举、空值和引用约束表达为 JSON Schema Draft 2020-12，组织本地结构注册、错误收集和诊断输出代码。依据为 `state`、`record-check`。
- 实施时固定 `rfc8785` 或 `canonicalize` 的具体版本，编写规定覆盖范围内的规范化对照例。规范化算法和参与哈希的字段范围已由蓝图确定。依据为 `state`、`freeze`。
- 为任务内唯一编号选择具体生成方式，组织模板渲染和材料清单的代码，保证编号唯一、引用可核对、正式提示词完整。依据为 `state`、`dispatch`、`prompts`、`record-check`。
- 按关键能力覆盖需要组织控制例和回归用例，选择具体样例文件与测试代码结构。每个关键验收器的三类校准、独立预期、当前最终对象验证及专业角色条件按既定要求执行。依据为 `contract-controls`、`calibration`、`capability-check`。
- 在五级验收变更规则内提交日志、选择器、解析器、运行器等实现维修提案，由 X1 审定正式使用并按影响重验。依据为 `acceptance`、`role-X2`。

## 5. 结论

设计语义足以指导实现。完成蓝图规定的四关卡、用户批准、冻结、实际授权核对和 X1 接收后，可以按既定语义开工。

**阻塞问题数量为 0。** 本结论来自 Blueprint 冷读，实际实现与验收进展按蓝图所记录的阶段继续推进。
