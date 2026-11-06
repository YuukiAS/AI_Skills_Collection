# Clear Writing 下一版本研究

建议沿 [#13](https://github.com/YuukiAS/AI_Skills_Collection/issues/13) 继续 0.6 的原 Phase C。下一阶段要验证的是，用户用正常入口提出问题时，能否在第一次收到的完整回答或文档里直接得到所需判断、解释和行动，而无须自己拼合多份来源或反复追问。近期案例给这项验收带来了更强的反例，暂时没有证据支持重开插件架构。

## 当前实现与候选

- 主线 `ff5be718` 发布包标为 `writing-style 0.5`，已有普通回答、保真、中文文稿、英文科研、结构重写和 UI 文案六条路线。普通回答已有“读者先理解对象”“用必要证据回答问题后停止”“多源共识、分歧与证据缺口分开”规则。主线还有标为 `Unreleased` 的补充示例，不能据此推断已安装 0.5 自动取得这些更新。0.5 发布记录的四个真实 Web 回答也没有证明后台每轮加载。 [0.5 包声明](../../../../plugins/codex/plugins/writing-style/.codex-plugin/plugin.json) · [现行源码](../../../../skills/writing/core/response-clarity/SKILL.md) · [版本记录](../../../plugin-changelogs/writing-style.md)
- 0.6 已有一个冻结候选。远端研究分支 `design/clear-writing--single-entry-artifact-finalization` 回读为 `9832a590`，最终候选源为 `cee207d3`。v0.4 执行包已安排写前选材、完整候选终审和混合请求的聊天/文档分别交付，保留六条路线。22 份首次产品答案来自 `157725b9`，包括 18 项已知回归、4 项保护对照。最终提交只改回放 helper。受影响的结构重写链用原输入、原阶段包和原首稿在实际安装的最终候选中复验。397 项本地测试、四项 CI 和独立实施审查有记录。纯精确 JSON 的 wrapper exit 1 与两项文稿读取日志空正文均留有边界，不能泛称所有结果都由最终提交重新生成并逐字回读。 [v0.4 计划](https://github.com/YuukiAS/AI_Skills_Collection/blob/9832a590896a6769842b89eaf863e251ef6d62e8/docs/design/clear-writing/CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md) · [候选身份](https://github.com/YuukiAS/AI_Skills_Collection/blob/9832a590896a6769842b89eaf863e251ef6d62e8/results/clear-writing--single-entry-artifact-finalization/candidate/FINAL_CANDIDATE.json) · [CI](https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/39743659101)
- 当前交接要求先核实真实账户、备份原插件、用真实导出验证恢复，然后按原合同检验 Web 正常入口。旧 Phase C 曾遇到 tar.gz 与 fresh Web actor 的前置问题。新版候选提供安全恢复读取，真实账户恢复和 Web 验收仍缺证据。个人正式插件保持 0.5，Web G1–G3、G6 与正式发布仍待后续，候选 `release_eligible=false`。#13 仍 open。统计和可视化消费方的 #73/#49 单列，0.6 本身发布也不会代替它们的验证。 [新版 Phase C 交接](https://github.com/YuukiAS/AI_Skills_Collection/blob/9832a590896a6769842b89eaf863e251ef6d62e8/results/clear-writing--single-entry-artifact-finalization/v0.4/PHASE_C_HANDOFF.md) · [旧 Phase C 状态](https://github.com/YuukiAS/AI_Skills_Collection/blob/9832a590896a6769842b89eaf863e251ef6d62e8/results/clear-writing--single-entry-artifact-finalization/phase-c/STATUS.json) · [#73](https://github.com/YuukiAS/AI_Skills_Collection/issues/73) · [#49](https://github.com/YuukiAS/AI_Skills_Collection/issues/49)

## 真实案例归并

| 问题簇 | 证据支持的判断 | 归属和回放方向 |
| --- | --- | --- |
| 双路 Pro 汇报、Bridge 0.11.1 完成汇报、STAT5060 缺陷编号、简单下一步被写成依赖说明 | 双路汇报技术裁决基本正确，逐份复述却把比较留给读者。用户最终接受的答复完整交代目标、覆盖、如何开发和验证、将收到什么以及还差哪一步。Bridge 案例有 Skill 正文进入上下文的记录，整篇仍失控，排除了该例的“完全未加载”。其他案例有用户所见结果，部分缺独立运行轨迹。 | `response-clarity` 的内容选择和全文执行回归。保留一份复杂长答与一份短动作答，分别核查完整交付和回答比例。内部定位码按是否影响操作选用，真实提交文件名仍须准确。 |
| CAT-TRACE 校准图与热图、DII 术语、必要长数学解释 | 有科学材料却先写限制或公式，导致读者不知道数据、坐标和颜色指什么。只写趋势的缩短版仍无法读图。当前规则已经要求先用来源支持的信息建立对象。DII 文稿有用户批评和版本对照，未证明安装插件的入口和全文终审确实执行。 | 普通图解归 `response-clarity`，正式全文归中文文稿或结构改写。把热图和校准图作为同一读图能力的两种例子，长推导作为保护性对照。统计量、图中编码、模型边界由领域 owner 给出。 |
| BetterDisplay 连续说“没懂”、Reasoned Decision 架构总结漏答、Atlas 路线讨论反复复述 | 既有“遵从最新指令”和完整论证规则覆盖明显失败。现有证据还提示一个跨轮缺口：需要识别前轮解释没有交付的具体理解，并换例子或解释路径。上一轮已确定的事实和用户目标应随续问保留。平台是否每轮加载仍需独立区分。 | 先增加连续追问样本验证候选，要求下一轮直接补答、演算或提供新解释路径。用户要求原来的多项任务时应继续做完，单纯分析上一轮的写法也算未完成。 |
| DII 中文长稿和科研幻灯片全文、课程双语材料冻结后才发现机器文案 | 前者是整件产物的实际阅读体验和第一处术语说明。后者有明确的调用拓扑和时序风险。0.5 的 `chinese-prose` 在其自身适用面要求终审，但另一个插件缺少已安装依赖或冻结前交接时，规则声明不足以证明实际发生。 | 文稿用完整首稿与源文成对验收。课程材料是否必须在冻结前调用 Clear Writing，由 Research Authoring 与 writing-style 另审接口。已冻结原样渲染必须保持内容不动。 |
| UI 短文案与展示形式 | #17、#90 的文案案例已有 `product-ui-copy` 正式路线，剩余问题应区分语言、页面内容选择、产品状态与宿主生成的卡片。 | 文案留在专门入口。普通回复的可视形式只在带来额外解释价值时使用。根据成品区分真实图证据和占屏的形式包装。Frontend Design 仍负责界面信息架构，插件不能承诺控制宿主自动渲染。 |

主来源是 [writing-style TODO](../../../plugin-todos/writing-style.md)。Reasoned Decision 的多部分摘要有 [独立负例说明](../../../../skills/writing/core/response-clarity/references/reasoned-decision-summary-architecture-negative-example-2026-11-05.md)。上述合并保留两类证据区别：用户可见的真实失败，以及正常入口已确认实际载入插件后发生的回归。

## 初步产品构想

用户照常说“讲清楚”“按这两份研究给出交付说明”“把这篇写成读者能用的稿子”，也可显式选择 Clear Writing。GPT 上由现有 0.6 方案的一处入口识别任务，Codex 保持现有六条直接入口。两端共享语义、受众和写作规则，结果与对应入口实际表现分别核对。

1. **先决定读者需要知道什么。** 普通答复把行动、结论和直接理由放在读者用得到的位置。复杂综合保留会改变判断的分歧、证据强弱与未决项。主张来自上游领域推理时，保留归属和确定性，作者建议与来源结论分开。
2. **给读者理解所需的深度。** 图解释先建立坐标、编码及生成过程，模型解释用来源支持的对象和单位。续问表明原解释失败时，提供能改变理解的例子、比较或具体数值关系，随后把仍未完成的原请求做完。
3. **独立通读实际交付物。** 短答仍按短答结束。需完整成稿时，从头到尾核对用户任务、事实和阅读顺序，发现实际障碍就修正文。混合请求分别核对用户看到的说明与保存的完整文档。有写入权限时，Codex 可读写本地成品并回读，GPT 侧只有具备实际能力和授权才做外部写入。
4. **保住原意和精确交付。** 复用 `writing-fidelity`、结构重写、长文和 UI 路线。保护数据、公式、条件、出处、授权、完成状态与精确字段。按用户任务调整呈现位置。纯精确输出、已冻结原样渲染等对照继续保持原文。

词表和标题数量可以筛查局部问题，无法解释“事实已齐却仍要读者比较”。固定短答会漏掉复杂任务的条件与步骤。现有 0.6 结构已经给内容选择和完整候选留出位置，先用新旧对照检验它。Reasoned Decision 负责判断是否可靠，Design Assurance 负责方案约束是否足以执行，Delivery Assurance 负责产物身份和实际交付。Clear Writing 负责在各自已确认的事实边界内让读者理解和行动。 [插件职责边界](../../../design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md)

## 外部参考

以下资源核对于 2026-11-06。仅提取评审和回放思路。

| 来源与许可 | 实际检查及对本项目的用途 | 局限与采用判断 |
| --- | --- | --- |
| CDC Clear Communication Index，官网使用指南。CDC 自有美国政府材料通常属公有领域，个别资源、图和第三方内容例外。 [指南](https://www.cdc.gov/ccindex/tool/how-to-use.html) · [使用条款](https://www.cdc.gov/Other/imagereuse.html) | 查看了受众、主要信息、行动以及独立读者审查的做法。可以把“读者能否复述结果、下一步与限制”变成独立验收提问。 | 健康传播二元评分和公共受众假设无法覆盖专业技术长答。保留验收问题的思路，`REFERENCE_ONLY`。 |
| DeYoung 等，《Do Multi-Document Summarization Models Synthesize?》，TACL 2024，论文 CC BY 4.0。 [论文](https://aclanthology.org/2024.tacl-1.58/) | 阅读研究问题、输入顺序和组成扰动结论。其模型对来源顺序过敏、对组成变化不足的观察启发两个对照：换 A/B 顺序时，同一证据裁决应稳定。实质分歧变化时，回答应准确反映。 | 论文任务是观点和证据综合，无法直接证明技术负责人应采纳哪份报告，也无须把生成多个候选的方法移入产品。 `REFERENCE_ONLY`。 |
| Fabbri 等，SummEval，TACL 2021，论文 CC BY 4.0，代码 MIT。 [论文](https://aclanthology.org/2021.tacl-1.24/) · [代码与数据说明](https://github.com/Yale-LILY/SummEval) | 检查人工审阅维度和自动指标对照。用“事实一致、推理顺、内容相关、表达流畅”独立定位问题，允许第一项通过而读者任务失败。 | 研究语料为英文新闻摘要，分数和数据版权不能直接外推到中文科研完整文稿。 `REFERENCE_ONLY`。 |
| Vale，官方仓库 README 与规则范围，MIT。 [项目](https://github.com/vale-cli/vale) · [Scopes](https://vale.sh/docs/scopes/) | 查看真实 markup 解析、代码段豁免和可配置术语规则。可作为精确输出不误伤的实现对照。 | 现有回放已有保真检查，增加 linter 也无法判断证据去留或讲解顺序。本轮 `REVIEWED_NOT_ADOPTED`。 |

## 下一轮应怎样验收

- **先继续既有候选。** 原 Planner 先核实 Phase C 的真实账户、恢复与 Web 能力。新案例可提交给正式 Planner/Critic 作为额外已知开发回归，沿既有 G2/G4 验收口径。原 G6 的新鲜样本与标准保持独立，不能用这些已知案例顶替。
- **在完整首答上做正反对照。** 双路 Pro 案例先保留用户确认稿和原失败稿，观察回答能否一次完成所需裁决和完整交付说明。补一个无实质冲突与一个会改变决定的真实冲突，分别测试来源顺序和冲突保真。科研图读者须能准确解释轴、点/颜色和判断范围，保护一例确需完整公式的长答。对“还是没懂”，下一轮应解决具体卡点并保留用户未获回答的事项。精确 JSON、命令、原样引文、已冻结文案和真正影响行动的 ID 作为对照。
- **把入口、内容和证据分开判。** 观察同一个候选的实际加载或豁免、原输入和第一次完整产物。独立评审逐项说明原有事实、用户能从哪里读到关键结论、实际遗漏，以及是否有额外阅读工作。没有完整成稿、源文或真实用户表面时，只保留相应证据缺口。若候选正常入口仍失败，再区分该修路由、应有的跨轮重答行为，还是领域插件在冻结前漏接入。

正式 Planner 还需决定哪些入口承诺应覆盖连续追问、何种宿主证据能证明实际消费，以及是否先用两个真实上游成品验证写作交接再扩大适配。纯编辑工作不改变领域判断和已审批发布条件。研究范围限于公开记录与可读候选证据，本轮没有重新运行产品回放、访问个人账户或实施插件改动。
