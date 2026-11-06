# Presentations 下一版本研究

建议继续审查现有 0.5 v0.2 双端提案。最需要确认的是，用户从任一端开始，系统是否都能先决定受众、页面职责和证据，再完成可投影或可编辑的成品。下一版本需要同时解决教学模板分叉和返修改坏已接受页面的问题。独立审查应评价产物，并用来发现生产机制的遗漏。它发现的一批明显旧缺陷，应当作为生产机制的失败处理。

## 现状和证据

- **0.4 已发布。** 主线 `ff5be718` 有 `research-presentations` 和 `business-presentations` 源入口，已有确切 CUHK Beamer、明确可编辑请求的官方 Presentation/Slides 路线、版式与证据合同、已有文稿锁和候选身份验证。0.4 固定了 TeX Gyre Termes 字体身份，增强了返修时对来源、逐页渲染与独立审查记录的验证。现行路由对未指定格式的教学任务默认可编辑，中央模板目录只打包 CUHK。课程项目使用的本地 Beamer 和共享字体规则，不能代替 #98 所需的中央 course-standard 模板实装。 [发布记录](../../../plugin-changelogs/presentations.md) · [研究入口](../../../../skills/tools/documents-media/presentations/research-presentations/SKILL.md) · [商务入口](../../../../skills/tools/documents-media/presentations/business-presentations/SKILL.md) · [模板路由](../../../../skills/tools/documents-media/presentations/shared/template-routing.md) · [#98](https://github.com/YuukiAS/AI_Skills_Collection/issues/98)
- **0.5 v0.2 处于中间设计审查。** 独立设计分支读取到 `15781777a4dba50122d17ce7697e595920798b3c`。提案记录 `PROPOSED_FOR_CRITIC`、`ready_for_codex = NO`。教学默认的 course-standard Beamer、一个作者合同的两端发布，以及两个时点的 Clear Writing 调用均属候选能力。旧双模板 V1.1 的架构审查和 Stage 1 v1.3 的 execution-ready 审查各有独立对象，其结论只可作为迁移依据。 [0.5 v0.2 原提案](https://github.com/YuukiAS/AI_Skills_Collection/blob/15781777a4dba50122d17ce7697e595920798b3c/docs/design/presentations/PRESENTATIONS_0_5_DUAL_SURFACE_AUTHORING_AND_PRODUCTION_ARCHITECTURE_V0_2_2026-10-20.md) · [旧 V1.1 审查](../../../../results/presentations--two-template-production-redesign/CRITIC_REVIEW_V2.md) · [旧 Stage 1 审查](../../../../results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V5.md)
- **缺少渲染依赖是独立的兼容修复。** `bb74e18f` 是当前主线的祖先。对应远端任务有 CI 与 Reviewer PASS，`CURRENT` 为 `AWAIT_HUMAN_DECISION`。它验证缺 TeX 引擎和缺规范字体时的状态及显式容许边界，真实投影和 0.5 产品承诺需要另外取证。 [修复结果](../../../../results/presentations--ci-missing-render-contract-repair/RESULT.md) · [远端 CURRENT](https://github.com/YuukiAS/AI_Skills_Collection/blob/02886fdbd19464df4a5265057e12163d4a4b8609/automation/reviewed_handoff/tasks/presentations--ci-missing-render-contract-repair/CURRENT.json)
- **四论文冻结批次失败是有效证据。** 041 的真实入口有两篇无法选出可用构图，两篇虽按 exact CUHK 渲染，却没过冻结视觉门，且现有自动返修无法把审查意见安全映射到允许动作。四篇均已消耗。后续可用公开安全开发样本重现相同语义选择、投影可读性及安全返修问题。原论文、图像与像素保留作历史验收证据。 [041 最终报告](../../../../results/041_research_presentation_frozen_four_paper_generalization_batch/FINAL_REPORT.md)

## 把分散反馈归到用户能力

| 失败族及来源 | 当前判断与回归归属 |
| --- | --- |
| **受众不知道该看什么。** CAT-TRACE v13/v14 的首用、跨页过渡、讨论问题、图文层次与模型闭合。#29–35、#38–43、#45–48 等处重复记录。 | 合并到作者阶段和全套读者努力。证据不足的讨论页保留开放问题。成熟结果页说明可核对的结论及证据。版式应反映比较或顺序关系，逐页语言检查无法证明跨页理解。语言调用归 Clear Writing，故事和证据选择归 Presentations。 |
| **课程样式或教学语义分叉。** STAT5060 真实批注的章节导航、Question/Terminology/Caption、页脚、比例、代码可复制，以及课程讲解与教师伴随材料。 | #98 只追踪共享 Beamer core 与两个 skin。教学目标、学生可见内容、独立教师材料、考核不泄露各归教学路线。课程自有的题目、符号与行政决定留在项目。 |
| **上一轮接受的东西被返修改坏。** 课程反馈锁、共享组件锁、已接受图形退化。CAT-TRACE 多轮补丁也有同类风险。 | 0.4 已有分层锁、稳定 PageID、视觉继承和独立审查合同。先用正常已有文稿入口核实实际消费，少量修改用相同格式与作用域。持续复发时查共享部件、内容权威或检测器，同类页面共用修复。 |
| **已有合同仍允许劣质成品被送审。** 38 页教学 deck 编译成功，仍有小对象、大空白、诊断图与数值可能不一致、候选被过早展示。#36 自证、#37 漏检及多项 reviewer 模型/图像能力反馈同类。 | 生产侧保留逐页实际渲染、全套节奏、身份和定量视觉自查，独立 reviewer 读取对应候选图像并做领域判断。图像能力不足保留未验证，缺资源只允许合法轻量分支停在其可证实范围。0.5 可用现有独立审查。后续通用运行时、盲校准和 verdict 聚合另行论证。 |
| **交付形态偏离意图。** 公式、引用和代码可复制、学生/教师文件可打开、明确 editable 仍需保留对象。 | 由演示路线提供对象与成品证据，再用实际文件入口验证交付。技术渲染、可编辑性、教学充分性、用户能下载是不同证据。跨领域 Delivery Assurance 只消费领域判定和用户可用的交付物。 |

案例定位见 [主 TODO](../../../plugin-todos/presentations.md)、[教学模板 parity](../../../design/PRESENTATIONS_STAT5060_RICH_V1_TEMPLATE_PARITY_AND_DELIVERY_QA_TODO_2026-10-04.md)、[历史锁](../../../plugin-todos/presentations-core-history-lock.md)、[独立审查合同](../../../../skills/tools/documents-media/presentations/shared/independent-review-contract.md) 与 [真实渲染事故](../../../design/PRESENTATIONS_RENDER_REGRESSION_POSTMORTEM_AND_HARDENING_2026-10-07.md)。本轮核对公开事故记录和契约，未重跑生成流程，也未复核私有原始 slide 像素。

跟踪方面，公开 #29、#35、#36、#39、#43、#44、#98 仍 open。TODO 中历史的 `PROMOTED_BY_045` 保留为来源记录，后续以当前包内合同、实际正常入口及独立成品证据区分已覆盖、复发和缺实现。若同号已指向别的维护事项，候选动作是按标题、描述和消费者逐条核对后修 backlink。例如教学模板/教师伴随材料段落中的 #49/#50，当前公开 Issue 分别是科学可视化的文案交接和交互示意图。不要因旧编号自动关闭 Issue，或把通用审查分支的事项一起归到 #98。 [#49](https://github.com/YuukiAS/AI_Skills_Collection/issues/49) · [#50](https://github.com/YuukiAS/AI_Skills_Collection/issues/50) · [#98](https://github.com/YuukiAS/AI_Skills_Collection/issues/98)

## 外部方案

均于 2026-11-06 查阅。保留现有引擎与官方工具路线，外部证据用来区分模板接口、读者理解和编辑安全三类问题。

| 资源与许可 | 查到什么、适合借鉴什么 | 采用判断 |
| --- | --- | --- |
| Beamer 3.78，CTAN 列 LPPL 1.3c、GPL v2 或更新版和文档 FDL。 | 看了原生 miniframe、section/subsection/frame 的组织与维护者对 #456 的讨论。缺层级或例外帧会改变导航，证实 #98 需要可点击导航和例外页的实际渲染回归。Beamer 不定义课程品牌、语义角色或源权限。 [CTAN](https://ctan.org/pkg/beamer) · [原生主题文档](https://github.com/josephwright/beamer/blob/main/doc/beamerug-elements.tex) · [#456](https://github.com/josephwright/beamer/issues/456) | `RUNTIME_DEPENDENCY`（沿用现有 Beamer 路线） |
| Quarto CLI，MIT，随附组件另见 COPYRIGHT。 | 看了 PPTX `reference-doc` 布局名匹配、缺布局告警后回到默认，以及 #8312 中母版定制未被实际布局拾取的用户案例。值得借鉴其显式布局合同，并把 canonical 模板静默降级作为负例。多格式输出不能证明指定模板精确复现或已有 deck 的对象完整性。 [PowerPoint 指南](https://quarto.org/docs/presentations/powerpoint.html) · [#8312](https://github.com/quarto-dev/quarto-cli/issues/8312) · [许可](https://github.com/quarto-dev/quarto-cli/blob/main/COPYRIGHT) | `REFERENCE_ONLY` |
| Microsoft PresentationML / Open XML SDK，SDK MIT。 | 看了 slide master、layout 和 slide part 的引用及继承。适合检验局部修改是否触及共用母版或其他页面。包结构有效只证明对象关系，不证明原生打开、重排后的观感或视觉语义。 [微软文档](https://learn.microsoft.com/en-us/office/open-xml/presentation/working-with-slide-masters) · [SDK 许可](https://github.com/dotnet/Open-XML-SDK/blob/main/LICENSE) | `REFERENCE_ONLY` |
| PPTArena，arXiv:2512.03042v3（2026-07-02）。数据卡标 MIT，代码仓未见明确许可文件。 | 看了真实 PPTX 的成对精确修改设计，结构差异与图像并评。适合启发“改到且保住”的用例。基准和 VLM 判定无法替代本产品的课程、科学和原生交付门槛。未下载 deck 或引入代码。 [原论文](https://arxiv.org/abs/2512.03042v3) · [数据卡](https://huggingface.co/datasets/mofengenden/PPTArena/blob/main/README.md) · [代码仓](https://github.com/michaelofengenden/PPTArena) | `REFERENCE_ONLY` |
| Garner 等，ASEE 2011，© ASEE，未见开放复用许可。 | 读了同一录音、两种 slide 结构的比较。复杂概念的理解和回忆支持以信息明确的标题与证据组织页面。研究条件有限，提问、负结果、推导和教学练习可用适合其任务的标题。 [会议论文](https://peer.asee.org/assertion-evidence-slides-appear-to-lead-to-better-comprehension-and-recall-of-more-complex-concepts.pdf) | `REFERENCE_ONLY` |
| Anthropic PPTX Skill，`fa0fa64bdc967915dc8399e803be67759e1e62b8`，专有许可。 | 对比了新建、现有模板编辑和读取三种入口，以及真实渲染与包结构验证的分工。它针对 Office 文件操作，未覆盖科学叙事、精确 Beamer、冻结权限或独立审查。只记录设计对照，不复制其脚本、提示或资产。 [Skill](https://github.com/anthropics/skills/blob/fa0fa64bdc967915dc8399e803be67759e1e62b8/skills/pptx/SKILL.md) · [许可](https://github.com/anthropics/skills/blob/fa0fa64bdc967915dc8399e803be67759e1e62b8/skills/pptx/LICENSE.txt) | `REVIEWED_NOT_ADOPTED` |

## 初步产品构想

用户照常说“用这些材料做组会”“按上轮接受版本只改标出的页”或“做一套可编辑教学文稿”。现有 0.5 提案值得优先检验以下四种能力。

1. **从来源做作者判断。** 明确受众和目标，锁住页面职责、首次出现和证据，在含义稳定后交 Clear Writing。GPT 负责来源可见范围内的作者对话和可审阅交接。Codex 可直接走同一作者路径，也可消费已冻结的交接。
2. **按请求生产真实成品。** Codex 使用实际资源、模板和引擎。研究与教学共享 Beamer 角色和原生控件，分别呈现视觉身份。明确要求可编辑或指定模板时应保留格式、原生对象和可操作入口。GPT 端可交讲稿或逐页计划，能否生成文件取决于所处实际工具和授权。
3. **有界返修。** 两端读用户已接受的结果、历史和改动范围。Codex 用源文件和像素差异证明保护区，修正同时保持可编辑性、语义、格式和分工。单页文字修正走轻路径，系统性回归在根因层处理。
4. **先由生产侧读完候选，再独立审查和交付。** 实际成品、逐页图像、整套视图和身份供审查方判断。领域作者和外部审查各有职责，既有 GPT Work/独立 reviewer 方式可先提供证据，通用验收器以后独立定界。

这四类能力可继续在 Presentations 内演进。更换渲染器只处理输出形式。若先建设通用评审运行时，容易延续“首次生产留给 reviewer 补课”的返工。设计是否具备可实施条件由 Design Assurance 研究，交付是否到达消费者由 Delivery Assurance 研究。两者复用演示自己的专业判断。课程题目、科研结论和统计正确性仍交领域方，通用流程与证据传输仍沿 Workflow Core 和 Bridge Kit。

## 建议复验与交由 Planner 决定

| 真实任务入口 | 通过证据 | 反例和应保持行为 |
| --- | --- | --- |
| 同一个研究任务分别从 GPT 作者包和 Codex 直接开始 | 受众、主张与来源、首用和页面职责可对应，冻结后的文案实际经 Clear Writing，最终真实 deck 在普通投影尺度可读。 | 省掉作者阶段、串错证据、论文图缩贴、科学结论被改写均应查出。允许合法探索性问句和用户只要提纲。 |
| #98 课程模板和 CUHK，4:3/16:9 | 两种皮肤实载同一 core。全名章节、可点 miniframe、页脚、语义角色和整套页面都过独立观察。学生版和教师伴随材料各自检查。 | 长标题、无章节的开场页和课程目录例外各有预期行为。禁止 host 字体替代、误继承学校品牌或教师内容泄露。 |
| 已有 deck 单页修改和失败版本恢复 | 只改获准位置，原生源和整套成品可追溯，历史批注逐条在最终渲染上有观察。 | 混入旧 render、用整套重生成假装局部修改、用删除当修复或跳过锁验证，应拦截。 |
| 可编辑商务 deck 与审查证据缺失 | 最终文件可打开、对象可编辑且用户能取到，实际可用的审查记录可绑定此候选。 | 验证器或独立 reviewer 看不到像素、文本或对象时保留未验证。正常的低风险局部改动不升级成全套评审。 |

Planner 需要裁决三个问题。第一，未明确格式的教学请求由当前 0.4 的 editable 改为 course-standard Beamer，哪些工作会受影响，怎么保障显式请求和既有模板不变。第二，#98 可否先用既有独立运行入口拿双皮肤消费证据，并明确两个 ChatGPT/Codex 实际入口、Clear Writing 和评审工具可用性。第三，v0.2 的广范围应如何分包，确保同一最终候选保留科学构图、教师隔离、锁、原生投影和首交，且没有用 041 已消耗论文调门槛。建议按风险先做确定性回归，再进入独立整套审查和新样本验收。研究稿不改变提案已定的产品承诺或权限。
