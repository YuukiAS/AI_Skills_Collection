# D7 冷读报告

## 1. 拟开工顺序

本次判断只依据 `blueprint.json`。蓝图当前保留 `versions: []`，实施状态为 `not-implemented`。以下顺序包含实施前的既定关卡，以及完成冻结交接后的实现工作。

1. **先完成本稿的冻结准备。** D1 收敛本轮关卡反馈，明确同一受审快照，准备固定格式的冻结说明。D5 使用草稿档，D6 逐组件追问并检查说明，D7 判断开工缺口，D8 按每轮新 GPT 对话合批复述，由 D1 逐单位判断。依据 `role-D1`、`gates`、`role-D6`、`role-D7`、`role-D8`、`freeze`。
2. **取得批准，按五步顺序冻结并交接。** 四关卡对受审快照有效后取得用户批准，追加首个版本，对完整输出运行 D5 冻结档，确认获批快照保持一致，再写冻结记录。X1 在独立长期线程实际读取并接收，D1 最后一次状态提交切换阶段和写权，X1 回读确认。依据 `freeze`、`q-checker`、`writer`、`role-X1`。本插件自身的 X1 使用蓝图明确指定的 GPT Work 极高，Claude 承担机械启动 Codex 的运输。
3. **先实现共用文件协议。** 按唯一规则源建立状态、事件、任务书、派发及结果等结构与模板，实现只读记录检查、身份计算、单写者与冲突恢复约定。加入 JCS 字节与哈希对照例。依据 `minimum`、`source-layout`、`state`、`writer`、`record-check`、`dispatch`、`prompts`。
4. **接入设计端完整流程。** 实现澄清分类、独立设计任务书、设计角色资源、四关卡组织、九项合同定位、冻结说明及冻结交接。Blueprint 检查器按固定提交接入。依据 `clarify`、`design-roles`、`contract`、`gates`、`freeze`、`q-checker`。
5. **接入交付端完整流程。** 实现候选提案与选定、验收资产审定、三类校准、三态证据、偏离申报、五类设计退回、修订继承、十三项签发检查和签发后复核撤回，接上三项衡量。依据 `delivery-roles`、`acceptance`、`calibration`、`candidate`、`evidence`、`deviation`、`revision`、`q-inheritance`、`sign`、`metrics`。
6. **生成并安装同源插件包。** 建立两个规划入口和两个执行入口，用现有生成器复制共用资源与规划资料，落实 12 插件、32 技能预算，保留原有能力。网页端打包先定位并复用 thread handoff、thread instruction 的既有方法。依据 `source-layout`、`planning-entry`、`execution-package`、`q-capacity`、`web-later`。
7. **在最终候选上完成真实验收，由 X1 签发。** 先做便宜的结构检查和已知回归，再完成 Claude Code、GPT Work、已安装 Codex 入口及真实 ChatGPT 网页端的规定观察。按条件取得 X3、X4、X5 的结果，X1 亲读最终对象与原始证据，逐项签发。依据 `capability-check`、`contract-fidelity`、`contract-regression`、`web-later`、`sign`。

## 2. 已经明确的接缝

| 组件之间 | 输入与输出，以及采纳条件 |
|---|---|
| 两个插件与共用状态 | 同一任务绑定同一任务目录和 `STATE.json`，默认路径为 `docs/assurance/<task_id>/STATE.json`。输入包含任务、仓库、分支和实际目录，输出为有修订号的唯一当前状态。设计阶段 D1 写状态，交付阶段 X1 写状态。依据 `state`、`writer`。 |
| 澄清与独立设计、现实核查 | D1 输出不可变 `design/briefs/<brief_version>.json`，包含带出处的需求、用户决定、事实、开放事项与读限。D2、D3、D4 绑定 `brief_sha256`。D2 与 D3 读取同一任务书，独立交回完整候选。任务书换版后旧结果标为 `stale`，由 D1 判断仍可支持的范围。依据 `clarify`、`dispatch`、`role-D2`、`role-D3`、`role-D4`。 |
| 调度、提示词与角色返回 | 调度按七级优先顺序选首个成立条件，可并行角色组成明确批次。提示词展开角色、档次、线程、准确定位、读写范围、绑定身份和返回位置。派发区分 `prepared/sent/returned/accepted/stale/cancelled`。返回包含 `dispatch_id`、`based_on`、实际读写、产物定位、发现和未运行项，负责人核对后采纳。依据 `dispatch`、`prompts`、`writer` 及角色卡。 |
| 记录与只读检查入口 | `check_records.py` 接收 `--task-root`、`--schema`、`--record`、`--format json`，使用包内预注册结构。输出包含 `assessment,errors,unresolved,checked_files`，退出值 0、1、2 分别表示结构及可检查引用合规、确定错误、无法完成检查。依据 `record-check`。 |
| 受审设计与四关卡 | D5–D8 绑定 `snapshot_sha256`。D7 只读 Blueprint，D8 每轮一个新 GPT 对话合批，记录 `reader_isolation: "single-thread-batch"`，D1 逐单位判断。结构检查使用已指定的 Blueprint 检查器提交 `c05edcf51bc93f8be82180fd4ad28a250937f195`。依据 `gates`、`q-checker`、`role-D7`、`role-D8`。 |
| 冻结说明、用户批准与冻结记录 | 说明为独立文件，原始字节计算 `explanation_sha256`。D6 结果、D1 批准请求、用户批准及 `freeze.json` 绑定同一说明身份。批准和冻结记录同时记录 `snapshot_sha256` 与 `explanation_sha256`。说明改动后重新做说明四项检查，Blueprint 未变时可保留逐组件追问的有效结果。依据 `freeze`、`role-D6`、`record-check`。 |
| 冻结包与 X1 接收 | `snapshot_sha256` 标识获批内容快照，`semantic_hash` 用于定义内容及批准继承核验，`bundle_sha256` 标识冻结输出文件。内容哈希使用 JCS，完整文件与说明使用原始字节哈希。X1 实际读取并写接收记录，D1 核对后提交写权切换。依据 `state`、`freeze`、`writer`。 |
| 修订与正在进行的交付 | 小修须同时满足六项条件，包括至多两个既有节点的范围限制。继承记录保留前后语义哈希、字段差异、逐项等价理由及新 D5 结果。交付派发绑定获批语义哈希或沿完整合格继承链可达的值。暂停范围覆盖受影响节点及依赖工作，其他获准工作可继续。依据 `revision`、`q-inheritance`、`dispatch`。 |
| 实现、验收资产与当前候选 | X2 交候选提案及验收资产，触发条件成立时由 X3 独立完成相关验收实现。关键验收器实际运行正、坏、缺证三类控制例。X1 审定验收资产版本并选定当前候选，候选记录覆盖源码集合、最终对象、构建安装映射、运行器与环境。依据 `role-X2`、`role-X3`、`acceptance`、`calibration`、`candidate`。 |
| 当前候选、原始证据与签发 | 证据绑定候选、冻结合同、判据、验收资产及实际观察对象，记录 `passed/failed/unknown` 和有效性。X1 亲读最终对象与关键原始证据，核对十三项条件，对整个冻结范围签发。签发后有新事实时先进入复核，维持或撤回均留不可变记录，返修后的新签发关联旧签发。依据 `evidence`、`sign`。 |
| 中断恢复与重新派发 | 从最后有效历史状态出发，用事件与不可变记录核对补登。普通冲突固定按变化未发生处理，相关派发记 `stale` 并保留原始材料，重派列出已有提交和文件。涉及冻结、批准、签发、撤回或保守处置做不了的冲突交用户，相关范围暂停。恢复记录检查并远端回读后恢复未暂停范围。依据 `state`、`writer`、`record-check`、`dispatch`。 |
| 源层、生成包与各宿主 | 两个市场插件各暴露一个唯一命名的执行技能，规划正文放包内 `planning/`，共用资源放 `shared/assurance/`。规划读取绑定源仓库固定提交或经确认可读的完整包根。网页端 X4 实测读取资源、生成完整下一步提示词、按权限写回或给出内容，保存原始对话交 X1。依据 `source-layout`、`planning-entry`、`execution-package`、`web-later`。 |

## 3. 阻塞问题

**本次发现 0 个需要设计方新增决定的阻塞问题。**

以下事项已有处理规则，可以按蓝图推进。

- **已有网页端打包方法的具体位置须在实施时查明。** `web-later.terminal.mechanism` 已指定由 X2 在仓库和实际包中定位、记录来源并复用。找不到或无法复现时，按 `fail-web-method` 交 X1 处理偏离。查找结果尚未取得，已有方法选择和失败接收方均已明确。
- **跨宿主读取、安装与真实验收尚待执行。** `planning-entry`、`execution-package`、`capability-check`、`web-later` 已明确观察对象、必需动作、原始证据及接收者。实际失败或证据不足时，按既定返修、补证或设计退回规则处理。
- **依赖大小尚未记录时的处理已确定。** `freeze`、`role-D6`、`contract-authorization` 要求说明如实写“大小未记录”，首次下载或安装前记录实际大小，单项超过 100 MB 时先取得用户授权。
- **恢复冲突的处置边界已确定。** `state`、`writer`、`record-check` 已限定普通冲突的保守处置、必须交用户的情形、原始写入披露和暂停范围。执行者可据此实现恢复流程。
- **当前稿仍须完成冻结与交接。** `gates`、`freeze`、`writer` 已给出关卡、批准、冻结档复验、冻结记录及写权交接的先后关系。这些是开始插件实现前应完成的流程工作。

## 4. 实现自由度

- **代码组织。** 在已定入口、字段语义和写权内，自定函数拆分、变量名、内部模块与错误收集方式。依据 `role-D7` 对普通代码细节的明确许可，以及 `minimum` 的四个内部工作包。
- **结构定义的代码表达。** 将蓝图已有字段、枚举、空值、路径和引用规则落实为 JSON Schema，选择内部复用方式、错误信息排序与展示形式。记录检查的命令参数、退出语义及只读边界已固定。依据 `state`、`record-check` 和各记录节点。
- **JCS 依赖的具体版本与调用封装。** Python 使用 `rfc8785`，JavaScript 使用 `canonicalize`，版本在实施时固定。可自行组织覆盖中文、嵌套键排序和整数的字节对照例。依据 `state`、`gates`、`freeze`。
- **派发和回读的内部接线。** 可在已有授权及蓝图允许的提交、文件接口等方式中落实预期修订核对、幂等去重和回读。写入结果不明时先回读、机械网络失败最多自动重新读写一次的行为已固定。依据 `writer`。
- **模板和资源的内部组织。** 在保持已定目录映射、唯一技能名称、同源字节一致及角色读限的前提下，安排 Markdown 段落、模板实现和资源加载代码。依据 `source-layout`、`planning-entry`、`execution-package`。
- **具体控制例和回归实现。** 围绕冻结能力选择输入、构造真实坏例与缺证例，按覆盖需要确定数量和执行组织。预期结果来源、三态含义、关键验收器的三类校准及专业角色触发条件已有规定。依据 `contract-controls`、`calibration`、`capability-check`。
- **D8 合批的随机排列实现。** 可自行选择排列算法及记录方式，同时满足每轮新对话、逐单位只依据自身文字、记录文本身份、保留原样复述和受影响单位重读的要求。依据 `dispatch`、`role-D8`、`gates`。
- **衡量计算与展示。** 可自行组织事件读取、去重及汇总输出，遵循三项既定指标，保留未知归因和原始来源。依据 `metrics`。

这些自由度均限于合同允许的实现范围。角色职责、接口字段含义、判定标准、必需证据、不可替换方法或资源边界发生变化时，按 `revision`、`acceptance`、`deviation` 的既定规则处理。

## 5. 结论

从设计决定的完整性看，可以按蓝图既定语义推进。开工阻塞问题共 **0 个**。

插件实现应在本稿完成规定关卡、用户批准、冻结档复验和 X1 接收交接后开始。本次结论来自文件冷读，蓝图中的来源、宿主能力、依赖与验收计划仍待各自规定的实际检查。
