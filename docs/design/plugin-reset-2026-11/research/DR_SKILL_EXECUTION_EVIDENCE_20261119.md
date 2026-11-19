# 怎样让 ChatGPT 网页端插件 / Skills 的实际读取、流程执行和结果影响可核查，同时不污染正常回答

## 结论

当前候选方向里，“**正常答案保持干净，验证证据与正文分离**”是正确的；“**普通任务每次都额外生成一份 Markdown 审计附件**”则不建议作为默认行为。原因不是附件本身不好，而是只要附件仍由同一个模型在任务结束后自由生成，它与末尾一句“我已经执行了插件”在证据性质上没有本质跨越：两者都可以在流程根本没有执行时事后补写。自我清单、规则映射和漂亮的审计格式主要提升**可检查性与发现错误的概率**，不能单独构成执行证明。关于模型自我验证，系统综述和多项实验都发现：在缺乏可靠外部反馈时，模型对自身错误的发现与纠正并不稳定，而外部反馈明显更可靠。citeturn210084search0turn210084search1turn210084search3

更合理的体系不是“每次回答生成越来越重的证明”，而是把验证拆成两条正交轴。第一条是**单次任务证据强度**，建议分为轻、中、重三级；第二条是**插件版本级能力认证**，用 fresh-context、未见样本、随机抽样、哨兵约束和故障用例周期性检验整个 Skill 是否真的会被加载并稳定执行。这样普通聊天几乎没有额外阅读负担，正式产物留下与结果绑定的证据，重任务再保存机器回执和不可轻易重写的外部状态。长指令、多约束和多层指令本身确实更容易出现遗漏、位置效应和冲突，因此“每轮把整份 Skill 重新复述一遍”不是好的补救；更有效的是缩短常驻规则、按需加载细节、把验收要求靠近相应生成步骤，并用独立检查器或第二上下文复核。citeturn769999search1turn756885search0turn756885search3turn756885search5

具体建议是：

| 层级 | 默认使用场景 | 用户正常看到什么 | 后台或按需证据 | 主要证明对象 |
|---|---|---|---|---|
| **轻量级** | 普通问答、低风险插件调用 | 只有正常答案；必要时一个极短“已使用某 Skill”状态 | 显式 `@插件` 调用、稳定规则编号、可选按需展开的规则→结果定位 | 弱读取证据、结果一致性 |
| **产物级** | 正式文档、研究报告、复杂分析、改写 | 正常产物；审计内容独立于正文 | 规则版本、相关规则集合、规则→产物位置、修改前后差异、产物回读检查、确定性检查器或独立 Reviewer | 执行证据与结果影响 |
| **可追溯级** | 固定仓库、长任务、高影响任务 | 正文只报告结论和验证结果 | 版本化证据文件、工具回执、输入/输出摘要或哈希、验证器结果、最终产物哈希或提交、独立复核 | 较强外部可验证执行证据 |

与此同时，另设**版本级认证**，不要把它混入上述三级：插件发布、规则重大修改、模型或平台行为显著变化后，以及固定周期，运行 fresh-context 回归、未见样本、随机规则组合、故障路径、哨兵规则和多轮漂移测试。单次聊天不应该重新证明插件的所有能力。

这一判断尤其适合当前 ChatGPT 网页端。OpenAI 现行文档说明，Skills 可以包含指令、示例、支持文件和代码，并可在相关时被 ChatGPT 自动选择；插件则把 Skills、连接应用等组合起来。官方同时提供工作区层面的 Skill 调用统计，并在符合条件的 Enterprise / Edu 环境中提供部分 Skill、会话和应用活动的合规记录；连接应用的调用可以进入合规日志。官方文档目前**没有描述一个面向普通最终用户、每一轮都提供、不可由模型伪造的 Skill 指令读取与执行回执**。因此不能把网页端尚不存在的底层轨迹能力当作现成基础设施。citeturn858005search0turn858005search2turn122088search0turn122088search4turn822142search1

## “读取、执行、结果影响”是三种不同的证据

判断插件是否“真的执行过”，首先要避免一个常见错误：把“能复述规则”当成“执行了规则”，再把“产物恰好符合规则”当成“流程造成了这个结果”。

**读取证据**只回答：模型本轮是否获得了某个规则或 Skill 的内容。最弱的例子是模型说“我读过”；稍强的是它能准确给出没有出现在用户提示中的规则编号、独特措辞或文件位置；再强一些，是外部系统留下检索、文件读取或应用调用记录。即使存在真实读取日志，它仍然只证明“内容进入过模型可用上下文或工具结果”，不证明后续步骤真的按它执行。OpenAI 的 Agents SDK 把模型生成、工具调用、交接和守卫等作为独立 trace/span 记录，这正体现了“观察到一次输入或工具事件”与“最终任务正确”是不同概念。citeturn923240search0turn923240search8

**执行证据**回答：要求的步骤是否真的发生。比如规则要求“先读取 A，再运行检查器 B，之后重新读取最终文件”，那么可信度较高的证据不是模型写三行“✓ 已完成”，而是三个具有顺序、参数和返回值的外部事件，或者至少是可以独立重放的状态变化。工具型 Agent 的研究越来越重视轨迹而不仅是最终答案；例如 τ-bench 除了对话，还通过最终数据库状态判断工具代理是否真正完成目标，后续轨迹型评测则进一步检查工具选择、参数与调用顺序。citeturn410963academia9turn410963academia10

**结果影响证据**要求更高：不仅步骤发生过，而且步骤对最终产物产生了可识别影响。对于改写任务，“原文→修改后文本→触发该修改的规则”是很有价值的证据；对于代码或结构化产物，则可以把规则绑定到具体 diff、文件位置、测试结果或检查器输出。但这仍可能被事后解释。要进一步提高因果可信度，需要让证据绑定到**不能在最终答案出来后任意改写的对象**，例如早先保存的原始输入、工具返回值、版本化 diff、最终文件哈希、提交对象或独立验证结果。最高成本的验证是反事实测试：同一类任务在 Skill 开启/关闭或不同版本下比较结果；它非常适合版本认证，不适合每次普通聊天。

因此可以把证据强度概括成：

\[
\text{模型自由生成的叙述}
<
\text{产物绑定的结构化证据}
<
\text{独立验证}
<
\text{外部不可随意重写的执行状态}
\]

这里的“不易重写”不必等同于密码学不可否认性。对于日常科研和工程流程，一个已经提交到 Git 的文件、工具服务器产生的调用标识、独立检查器的输出、含产物哈希的审查记录，通常已经显著强于同一回答中的自我陈述。哈希本身却只能证明“这是同一个字节序列”，**不能证明模型读过它或受它影响**；它必须与事件、输入和验证结果组合起来才有意义。

## 主要验证机制：哪些有用，哪些容易沦为“合规表演”

下面的比较中，“可伪造”指模型在没有真正完成相应流程时，是否仍可仅根据最终产物生成看起来一样的证据。

| 方法 | 主要支持哪一层 | 单独证据强度 | 可否事后伪造 | 正常阅读干扰 | 适合的用途 |
|---|---|---:|---|---:|---|
| “已执行某插件”声明 | 几乎没有 | 很弱 | 极易 | 很低 | 仅状态提示，不能验收 |
| 自我打勾清单 | 执行意图 | 很弱 | 极易 | 中 | 帮助模型不漏项，不作为证明 |
| 引用规则编号/独特内容 | 读取 | 弱至中 | 若规则已知则容易 | 低 | 快速检查是否接触到相关规则 |
| 规则→产物位置映射 | 结果影响 | 中 | 可以事后构造 | 中 | 人工审查非常实用 |
| 改写前→后→规则 | 结果影响 | 中至较强 | 可构造，但容易被人工反驳 | 中 | 改写、编辑、规范化任务 |
| 独立 Markdown 审计附件 | 取决于内容 | 本身不增加 | 可以 | 正文低、附件高 | 作为证据容器，而不是证据本身 |
| 生成后回读完整产物 | 执行/质量 | 中 | “声称回读”可伪造 | 正文无干扰 | 配合真实文件读取或检查器使用 |
| 第二模型/独立 Reviewer | 执行/结果 | 中至较强 | 比同一模型自审难 | 低 | 正式产物和高价值任务 |
| 确定性检查器 | 执行/结果 | 强，限可机器判定规则 | 难伪造真实输出 | 低 | 格式、引用、schema、测试、文件约束 |
| 工具调用记录/receipt | 读取/执行 | 较强 | 若由外部运行时产生则较难 | 很低 | 工具型流程 |
| 文件回读 + 哈希 | 执行对象身份 | 较强辅助证据 | 不能伪造已有对象，但不证明因果 | 很低 | 重任务、仓库 |
| 独立外部状态变化 | 执行 | 强 | 较难 | 很低 | API、数据库、仓库等 |
| 随机/隐藏/未见测试 | 能力可靠性 | 强于自证 | 难针对性迎合 | 用户无负担 | 发布与周期认证 |
| fresh-context 回归 | 是否依赖偶然聊天上下文 | 中至强 | 难由单次任务迎合 | 无 | 版本认证 |
| 仓库持久化证据 | 可追溯性 | 取决于所存内容 | 只存自述则仍弱 | 正文无 | 重任务 |

自我清单并非没有价值。FollowBench、InFoBench 等工作说明，把复杂指令拆解成可分别检查的要求能提高诊断粒度；DeCRIM 也通过“分解约束→批评→修订”提高了多约束任务表现。它们支持的是“**分解要求有助于执行和发现遗漏**”，而不是“模型勾选的清单是真实执行日志”。citeturn756885search0turn756885search1turn756885search2

同理，“输出后再检查一次”值得采用，但应把它定位为质量控制，不要冒充不可伪造证明。TACL 对自我纠错文献的系统分析指出，在没有可靠外部反馈的普通 prompting 条件下，并没有一般性的证据证明模型能够稳定自我纠正；逻辑推理实验也发现模型经常找不到自己的错误。外部反馈、已知错误位置或可验证条件显著更有效。citeturn210084search0turn210084search1turn210084search5

第二模型或“Reviewer”优于同一个上下文里的自审，主要因为它减少了共享生成轨迹和自我偏好，而不是因为第二个模型自动变成了事实裁判。已有研究发现模型会偏好自己的输出，自我修订可能放大这种偏差；因此 Reviewer 最好拿到**原始任务、适用规则和最终完整产物**，而不要只看生成器给出的“执行摘要”。citeturn210084search3

最强的一类证据来自模型无法单方面生成的外部事件。例如 OpenAI Agents SDK 的 trace 会记录模型调用、工具调用、交接和守卫；LangGraph 的 checkpoint 保存工作流状态；Claude Code 的 hooks 可以在工具使用前后真实运行脚本，例如修改后自动跑测试。这些机制不能原样搬到纯 ChatGPT Skill 上，但它们给出了共同的工程原则：**流程关键边界应该由运行时或外部验证器留下状态，而不是让生成模型在结尾描述自己做过什么。** citeturn923240search0turn410963search4turn410963search0

这也解释了为什么“证据越重越可靠”是错误命题。一个五页、全部由同一模型填写的审计报告，可能比一行真实的测试器返回值更弱。可靠性取决于**证据来源的独立性和绑定程度**，不是文本长度。

## 为什么长 Skill 容易漏执行，以及什么缓解措施有依据

长 Skill 的风险首先来自模型并非均匀使用长上下文。Liu 等人的 *Lost in the Middle* 在多文档问答和键值检索中观察到明显位置效应：相关信息位于上下文中部时性能可显著下降，而开头和结尾往往更好。这不是对所有现代模型、所有任务都必然成立的定律，但足以反驳“只要规则仍在上下文里，模型就一定同等可靠地使用它”的假设。**证据等级：同行评审研究。** citeturn769999search1

第二类风险是约束数量和冲突。FollowBench、ManyIFEval 和 MOSAIC 均观察到，随着指令数量增加，约束遵循会下降，并受到约束类别和位置影响；IHEval 则发现当不同优先级指令发生冲突时，模型表现明显恶化。多轮纠缠指令研究进一步显示，即使模型能回忆规则，也不意味着它能在交叉和冲突场景下正确整合这些规则。**证据等级：同行评审研究。** citeturn756885search0turn756885search5turn756885search7turn756885search3turn756885search4

OpenAI 当前也把不同来源指令的优先级冲突视为独立的可靠性问题，并针对 instruction hierarchy 进行专门训练；这说明“系统里存在规则”和“模型稳定按照正确优先级执行规则”本身就是两件事。**证据等级：官方技术说明。** citeturn756885search8

社区经验与研究结论方向一致，但不能用来估计故障率。2025–2026 年 OpenAI 社区和 Reddit 中持续有用户报告长对话中 Project / 自定义 GPT 指令漂移、迁移到 Skills 后部分工作流程不再稳定等现象；这些案例缺乏控制变量，可能混入模型版本、上下文、配置和产品故障，因此只能作为“真实使用中存在重复投诉”的证据。**证据等级：社区重复经验，不是受控实验。** citeturn604222search0turn604222search4turn604222reddit8

基于这些证据，以下缓解方法值得采用：

1. **常驻规则应短而稳定，详细流程按需加载。** 入口规则负责触发条件、不可违背边界和“去哪里取详细步骤”，不要把所有领域知识、所有例外和所有验收条款长期堆在一个 Skill 主体中。OpenAI 对 GPT 指令的官方建议同样强调多步骤流程应明确分段、规则和知识分离；Skills 本身也被设计为可自动选择的复用工作流。**证据等级：官方能力说明 + 同行评审研究的设计推论。** citeturn949686search2turn858005search2

2. **把关键验收条件重新放到它所约束的生成或验证阶段附近。** 这是针对位置与多约束干扰的工程缓解，并不能保证执行，但比“在长提示最前面写一次然后希望模型始终记住”更合理。**证据等级：同行评审研究支持的工程推论。** citeturn769999search1turn756885search7

3. **只核查本任务实际相关的规则集合。** 一次问答若只触发 7 条规则，就审这 7 条，不要让模型重新证明 80 条插件能力。这同时降低上下文竞争和“审计文本越长越像真的”的风险。

4. **产物完成后重新读取完整产物，但让验证尽可能外部化。** 对文档可重新打开最终文件，对代码重新运行测试，对引用重新解析参考文献，对结构约束使用确定性检查器；第二模型则负责难以机械判断的语义质量。**证据等级：多方工程实践 + 自我纠错研究。** citeturn210084search0turn410963search0turn923240search0

5. **稳定规则编号非常值得引入。** 编号不提高规则本身的执行概率，却能让“哪条规则→哪个产物位置→哪个验证结果”稳定绑定，也让插件升级后能够精确知道某次任务验的是哪个版本。

## ChatGPT 网页端的推荐落地方案

### 普通聊天：默认不要生成独立 Markdown 审计附件

普通聊天若每次调用插件都创建附件，会增加生成成本、上下文长度和用户界面噪声，却没有自动提升证据可信度。更好的默认是：**用户只看到正常答案；插件内部维护可检查结构，但不主动展开。** 如果产品表面允许显式调用，重要任务可以让用户通过 `@插件` 指定插件，这至少消除了“是否打算调用哪个插件”的歧义。OpenAI 当前文档说明，安装后的插件可自动使用，也可以通过 `@` 或工具菜单明确选择。**证据等级：官方能力说明。** citeturn122088search2

轻量任务若需要一个最低证据单元，建议只保留三项，而且仅在用户展开“核查”时显示：**本轮使用的 Skill 身份/可获得的版本标识、实际适用规则编号、规则对应的最终答案位置**。第三项尤其重要，因为它迫使证据落到可检查的输出，而不是停留在“我做过”。但这三项仍属于软证据：它们可以被同一模型事后构造，因此不能作为高风险任务的唯一验收条件。

如果插件调用了连接应用，网页端可利用现有平台留下的应用活动作为更强证据。在符合条件的 Enterprise / Edu 环境中，官方文档称支持的应用请求及相关响应可以进入合规平台，连接应用调用可被记录；但覆盖范围取决于产品、应用和工作区配置，因此必须逐项确认。Skill 本身则有工作区级 invocation 指标，不能据此推断“这条规则在这一轮被完整执行”。**证据等级：官方能力说明。** citeturn822142search0turn822142search1turn122088search4

### 正式文档、复杂分析和插件驱动改写：升级为“产物绑定证据”

这一层适合独立 Markdown 审计附件，但附件应被重新定义为**证据容器**，而不是“模型自述日志”。建议最少包含：

- 任务输入或来源对象的明确标识；
- Skill / 规则集版本及本任务触发的规则编号；
- 每条关键规则对应的产物位置；
- 若是改写任务，保留具有实质意义的“修改前→修改后→规则”差异；
- 最终产物回读后的检查结果；
- 能确定性检查的项目直接附检查器结果；
- 难以机器判断的项目由独立 Reviewer 给出结论和失败位置。

不需要写逐步思维过程，也不应该要求隐藏推理。过程证据应是**可观察动作和产物**，如读取文件、运行检查器、生成 diff、调用外部工具、验证引用、打开最终文件等。

“重新读取最终完整产物”应该作为正式产物的默认步骤，但要区分两种情况：如果只是同一模型说“我重新读过了”，证据仍弱；如果系统真的重新打开最终 PDF、Markdown、代码文件或数据输出，再基于其内容验证，证据就与实际消费对象绑定。这与成熟 Agent 系统把执行轨迹、状态和工具输出分开记录的做法一致。citeturn923240search0turn410963search4

### 固定仓库的重任务：持久化证据合理，但只保存有复核价值的对象

将重任务证据保存到 repo 是合理的，而且比把长审计塞进聊天更好，因为 Git 天然提供版本、diff、时间线和不可无痕覆盖的历史。但**不要把模型全部对话、思维摘要和每条“✓ 已完成”清单长期提交进去**。这些会快速变成噪音。

值得持久化的内容主要是：任务/规则版本标识、真实工具调用或外部操作回执、验证器和测试结果、最终产物路径与哈希、关键 diff、独立审查结果，以及足够重现失败的输入标识。若有提交或发布对象，应把证据绑定到对应 commit，而不是只写“最终版本已验证”。

一个典型的重任务证据对象可以是：

```text
task-id
skill-id / skill-version
applicable-rule-ids
input-artifact identifiers
external/tool receipts
validator results
review result
final-artifact hashes
git commit
```

其中 `hash` 解决的是“审的是不是这个产物”，测试/检查器解决“这个产物满足了什么客观条件”，Reviewer 解决难以机械判断的质量问题；三者职责不同。

对于 ChatGPT 网页端需要特别注意产品边界。官方迁移说明明确指出，标准 Chat 当前并不支持直接运行安装插件 ZIP 中附带的脚本；因此不能设计一个依赖“Skill 自己静默执行本地脚本并生成不可伪造 receipt”的通用网页方案。若需要真实机器回执，应通过平台支持的应用/MCP/外部服务或在仓库的实际执行环境中产生，而不是假定 Skill-only Chat 已具备这种运行时。**证据等级：官方能力说明。** citeturn858005search6

## 每次任务验证与版本级能力认证应该分开

最容易导致体系失控的做法，是试图让每一轮普通聊天重新证明“整个插件是可靠的”。单次任务最多能回答“这次结果有没有足够证据”，不能高效回答“这个 Skill 在各种场景下是否可靠”。

**每次任务应该验证**的是与这次产物直接相关的条件：当前适用规则、关键外部工具是否真实完成、最终产物是否重新读取、确定性约束是否通过，以及高风险任务是否完成独立复核。普通聊天没有外部动作且风险低时，甚至可以不展示任何验证文本。

**插件发布或周期性认证应该验证**的是能力本身：规则是否会在 fresh context 中触发；长对话后是否漂移；多 Skill 同时存在是否冲突；关键规则放在不同位置时是否仍被执行；随机组合约束是否遗漏；工具失败时是否会错误宣称成功；不同模型/模式下性能是否显著改变。ManyIFEval、FollowBench、IHEval 等结果都说明这类组合与冲突测试比只测试单一 happy path 更有价值。citeturn756885search0turn756885search3turn756885search5

认证集应包含**未见样本**。用于修改 Skill 的失败例子不应再次被算作独立验证，因为模型和规则已经针对它们适配。可以维护固定回归集，再额外保留一批直到最终验证才揭开的 holdout；还可以每次从规则库中随机抽取组合。所谓哨兵规则也应主要用于认证：例如在 Skill 中放入一个低自然发生率但无害的约束，用未向执行模型透露预期答案的测试来判断规则是否实际被加载。它能提升“未加载被发现”的概率，但并不能证明其它流程全都执行过。

这里可以借鉴 τ-bench 的 `pass^k` 思路：代理一次做对并不代表稳定；同一任务或同类任务跨多次 fresh-context 运行，能暴露偶然成功。τ-bench 在工具代理上专门强调多次试验的可靠性，而不是只看最佳一次。**证据等级：同行评审前的原始论文 / 工程基准研究。** citeturn410963academia9

最终可以把验收规则压缩成一句话：

> **单次任务靠与产物和外部状态绑定的证据，插件整体可靠性靠独立、未见、重复的版本级认证；任何完全由生成模型在最终回答中自由写出的“执行证明”，都只能作为辅助说明，不能单独通过验收。**

这同时满足四个目标：普通用户平时几乎感觉不到验证；怀疑时能从规则编号和产物位置快速展开；正式与重任务留下真实可追溯对象；而“我执行过插件”无论写得多完整，都不能取代真实证据。

## 对当前候选方案的具体修改

当前“正文干净 + 独立证据”的方向应保留，但需要做三处关键调整。

第一，把“**普通任务默认生成 Markdown 证据**”改为“**普通任务默认零展开证据，按需提供证据视图**”。原因是普通任务最缺的不是审计篇幅，而是外部绑定；把同一模型的自述从正文搬到 Markdown，并不会提升可信度。

第二，把正式任务的 Markdown 从“执行日志”改为“**产物绑定的核查记录**”。凡是模型无法独立证明的内容都不要写成确定事实。例如不要写“已读取 Skill 全文”，除非存在外部可观察事件；可写“审计中引用了规则 R12、R17，并在产物 §3.2 和表 4 找到对应实现”。如果真实读取行为不可观测，就应诚实保持这个证据边界。

第三，仓库中的证据文件只用于保存**未来重新检查仍有价值的信息**。最优先保存的是版本身份、真实外部回执、验证结果、产物身份和独立审查；最不值得保存的是自然语言过程叙述、模板化打勾和聊天中已经存在的冗长总结。

若未来允许增加一个工程扩展，最值得投入的不是“更复杂的审计 Markdown 生成器”，而是一个非常窄的**证据收集层**：当 Skill 调用真正的外部工具、读写正式产物或运行检查时，由该工具返回结构化 receipt，例如 `call_id`、操作、对象标识、结果、时间、输入/输出摘要或哈希。模型只能引用 receipt，不能自己创建一个等价“成功”事件。Claude Code hooks、OpenAI Agents tracing、LangGraph checkpoints 等成熟系统的共同经验正是把可验证状态移出自由文本生成。**证据等级：多方工程实践。** citeturn410963search0turn923240search0turn410963search4

因此，后续插件设计可以采用下面四条作为稳定原则：

1. **验证证据不等于解释文本；优先相信外部状态和可重放产物。**
2. **规则必须可单独寻址，证据必须尽量绑定到具体产物位置。**
3. **运行时验证只覆盖本任务相关风险，插件整体可靠性由独立版本认证承担。**
4. **默认界面为正常答案，验证采用渐进展开；风险越高，证据越外部化，而不是越啰嗦。**

这比“每条回答都附一份审计报告”更轻，也比“相信模型说自己执行过”可靠得多。

## 参考文献

以下文献均为本报告实际使用的主要来源，已去重。社区材料单列并明确作为经验性材料，不与官方文档和同行评审研究等价。

**OpenAI 官方文档与技术资料**

OpenAI. 2026. *Skills in ChatGPT*. OpenAI Help Center.  
https://help.openai.com/en/articles/20001066-skills-in-chatgpt

OpenAI. 2026. *Plugins in ChatGPT*. OpenAI Help Center.  
https://help.openai.com/en/articles/20001256-plugins-in-chatgpt

OpenAI. 2026. *Projects in ChatGPT*. OpenAI Help Center.  
https://help.openai.com/en/articles/10169521-projects-in-chatgpt

OpenAI. 2026. *GPTs in ChatGPT*. OpenAI Help Center.  
https://help.openai.com/en/articles/8554407-gpts-in-chatgpt

OpenAI. 2026. *Creating and editing GPTs*. OpenAI Help Center.  
https://help.openai.com/en/articles/8554397-creating-and-editing-gpts

OpenAI. 2026. *Custom GPT retirement and migration FAQ*. OpenAI Help Center.  
https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq

OpenAI. 2026. *Admin controls, security, and compliance for plugins and apps*. OpenAI Help Center.  
https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps

OpenAI. 2026. *OpenAI Compliance Platform for Enterprise and Edu Customers*. OpenAI Help Center.  
https://help.openai.com/en/articles/9261474-compliance-apis-for

OpenAI. 2026. *Workspace analytics for ChatGPT Enterprise and Edu*. OpenAI Help Center.  
https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu

OpenAI. 2026. *Improving instruction hierarchy in frontier LLMs*.  
https://openai.com/index/instruction-hierarchy-challenge/

OpenAI. 2026. *OpenAI Agents SDK — Tracing*.  
https://openai.github.io/openai-agents-python/tracing/

OpenAI. 2026. *OpenAI Agents SDK*.  
https://openai.github.io/openai-agents-python/

**同行评审与原始研究**

Liu, Nelson F., Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024. “Lost in the Middle: How Language Models Use Long Contexts.” *Transactions of the Association for Computational Linguistics*.  
https://aclanthology.org/2024.tacl-1.9/  
arXiv: https://arxiv.org/abs/2307.03172

Jiang, Yuxin, Yufei Wang, Xingshan Zeng, et al. 2024. “FollowBench: A Multi-level Fine-grained Constraints Following Benchmark for Large Language Models.” *Proceedings of ACL 2024*. DOI: 10.18653/v1/2024.acl-long.257.  
https://aclanthology.org/2024.acl-long.257/

Qin, Yiwei, Kaiqiang Song, Yebowen Hu, et al. 2024. “InFoBench: Evaluating Instruction Following Ability in Large Language Models.” *Findings of ACL 2024*. DOI: 10.18653/v1/2024.findings-acl.772.  
https://aclanthology.org/2024.findings-acl.772/

Ferraz, Thomas Palmeira, Kartik Mehta, Yu-Hsiang Lin, et al. 2024. “LLM Self-Correction with DeCRIM: Decompose, Critique, and Refine for Enhanced Following of Instructions with Multiple Constraints.” *Findings of EMNLP 2024*.  
https://aclanthology.org/2024.findings-emnlp.458/

Zhang, Zhihan, Shiyang Li, Zixuan Zhang, et al. 2025. “IHEval: Evaluating Language Models on Following the Instruction Hierarchy.” *NAACL 2025*. DOI: 10.18653/v1/2025.naacl-long.425.  
https://aclanthology.org/2025.naacl-long.425/

Harada, Keno, Yudai Yamazaki, Masachika Taniguchi, et al. 2025. “When Instructions Multiply: Measuring and Estimating LLM Capabilities of Multiple Instructions Following.” *Findings of EMNLP 2025*.  
https://aclanthology.org/2025.findings-emnlp.896/

Han, Chi, Xin Liu, Haodong Wang, et al. 2025. “Can Language Models Follow Multiple Turns of Entangled Instructions?” *Findings of EMNLP 2025*.  
https://aclanthology.org/2025.findings-emnlp.1387/

Purpura, Alberto, Li Wang, Sahil Badyal, Gene Beaufrand, and Adam Faulkner. 2026. “Deconstructing Instruction-Following: A New Benchmark for Granular Evaluation of Large Language Model Instruction Compliance Abilities.” *EACL 2026*.  
https://aclanthology.org/2026.eacl-long.62/

Kamoi, Ryo, Yusen Zhang, Nan Zhang, Jiawei Han, and Rui Zhang. 2024. “When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs.” *Transactions of the Association for Computational Linguistics*, 12:1417–1440. DOI: 10.1162/tacl_a_00713.  
https://aclanthology.org/2024.tacl-1.78/

Hong, Ruixin, Hongming Zhang, Xinyu Pang, Dong Yu, and Changshui Zhang. 2024. “A Closer Look at the Self-Verification Abilities of Large Language Models in Logical Reasoning.” *NAACL 2024*. DOI: 10.18653/v1/2024.naacl-long.52.  
https://aclanthology.org/2024.naacl-long.52/

Xu, Wenda, Guanglei Zhu, Xuandong Zhao, et al. 2024. “Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement.” *ACL 2024*.  
https://aclanthology.org/2024.acl-long.826/

Tyen, Gladys, Hassan Mansoor, Victor Carbune, Peter Chen, and Tony Mak. 2024. “LLMs Cannot Find Reasoning Errors, but Can Correct Them Given the Error Location.” *Findings of ACL 2024*.  
https://aclanthology.org/2024.findings-acl.826/

Lightman, Hunter, Vineet Kosaraju, Yura Burda, et al. 2023. “Let’s Verify Step by Step.” OpenAI. arXiv:2305.20050.  
https://arxiv.org/abs/2305.20050

Yao, Shunyu, Noah Shinn, Pedram Razavi, and Karthik Narasimhan. 2024. “τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains.” arXiv:2406.12045.  
https://arxiv.org/abs/2406.12045

He, Pengfei, Zhenwei Dai, Bing He, et al. 2025. “TRAJECT-Bench: A Trajectory-Aware Benchmark for Evaluating Agentic Tool Use.” arXiv:2510.04550.  
https://arxiv.org/abs/2510.04550

**工程实践资料**

Anthropic. 2025. *Claude Code: Best practices for agentic coding*.  
https://www.anthropic.com/engineering/claude-code-best-practices

Anthropic. 2025. *Enabling Claude Code to work more autonomously*.  
https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously

LangChain / LangGraph. 2026. *LangGraph Checkpoint*.  
https://github.com/langchain-ai/langgraph/blob/main/libs/checkpoint/README.md

OpenAI. 2026. *Codex default instructions / AGENTS.md specification*.  
https://github.com/openai/codex/blob/main/codex-rs/protocol/src/prompts/base_instructions/default.md

**社区经验材料，仅用于说明重复出现的实际使用反馈**

OpenAI Developer Community. 2025. *Custom GPTs not following instructions + no way to report it*.  
https://community.openai.com/t/custom-gpts-not-following-instructions-no-way-to-report-it/1280359

OpenAI Developer Community. 2026. *Custom instructions and memory preferences repeatedly drift in long ChatGPT conversations*.  
https://community.openai.com/t/custom-instructions-and-memory-preferences-repeatedly-drift-in-long-chatgpt-conversations/1406547

Reddit, r/ChatGPT. 2026. *Migrated your Custom GPT’s to Skills yet?*  
https://www.reddit.com/r/ChatGPT/comments/1wtm2pl/migrated_your_custom_gpts_to_skills_yet/