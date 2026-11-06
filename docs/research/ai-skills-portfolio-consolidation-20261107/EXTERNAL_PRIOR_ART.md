# 外部方案取舍

2026-11-06 查阅。每份研究报告保留来源、版本或访问日、许可、实际检查的对象与适用边界。采用判断只针对所列用途。

| 问题 | 核对的外部方法及取舍 |
| --- | --- |
| 查到可能改变选择的已有方案 | KCS v6 的边解决边复用、Google SRE 的可证伪排障、τ-bench 的多轮工具轨迹均为 `REFERENCE_ONLY`。配合上游文档、维护者 Issue、同语境社区报告发现真实候选。Superpowers 的排障纪律和 ADR Tools 作为直接移植方案为 `REVIEWED_NOT_ADOPTED`。[出处与许可](WORKSTREAMS/REASONED_DECISION.md#外部研究) |
| 判断设计能否开工 | Matt Pocock 的 grill-me / grill-with-docs、Spec Kit 的规格/计划/任务检查、ATAM 的优先场景、NASA 的审查出入口和 ADR 的决策记录均为 `REFERENCE_ONLY`。借鉴检索事实后再提问、用高优先级场景逼出实现约束，沿原 Planner–Critic 工作。[出处与许可](WORKSTREAMS/DESIGN_ASSURANCE.md#可借鉴的外部方法) |
| 证明用户拿到了已经验收的结果 | in-toto / SLSA 的对象身份、SRE PRR 的交接责任、Pact 的消费合同、Playwright 的下载事件与保存失败、GitHub Release 的资产核验均为 `REFERENCE_ONLY`。签名、合同测试、下载事件和真实消费分别取证。[出处与许可](WORKSTREAMS/DELIVERY_ASSURANCE.md#外部方案) |
| 帮读者完成比较和理解 | CDC Clear Communication Index、DeYoung 等人的多文档综合研究和 SummEval 为 `REFERENCE_ONLY`，用来区分读者任务、顺序/取舍、来源保真。Vale 对表面词汇有用，作为该产品能力的方案为 `REVIEWED_NOT_ADOPTED`。[出处与许可](WORKSTREAMS/CLEAR_WRITING.md) |
| 演示模板与真实渲染 | Beamer 是已有 `RUNTIME_DEPENDENCY`。Quarto、Open XML SDK、PPTArena 和演示理解实验为 `REFERENCE_ONLY`，Anthropic PPTX Skill 为 `REVIEWED_NOT_ADOPTED`。编译、可编辑对象、页面视觉与独立判断各自取证。[出处与许可](WORKSTREAMS/PRESENTATIONS.md) |
| 保持文档语义，生成正式产物 | Quarto Manuscripts、The Turing Way、CMU Eberly、LaTeX needspace、Typst 和自我解释研究均为 `REFERENCE_ONLY`。文档结构与渲染问题可以借鉴成熟做法，科研论证和课程信息仍由领域判断。[出处与许可](WORKSTREAMS/RESEARCH_AUTHORING.md) |

## 领域与客户端补充取证

| 公开来源与许可 | 实际检查、适用与局限 | 采用建议 |
| --- | --- | --- |
| UUyc-companion，`f5e45dc6d8c5f5fcae2011774d5c735d25ab8fa1`，MIT。 [源码树](https://github.com/aoyamashou/UUyc-companion/tree/f5e45dc6d8c5f5fcae2011774d5c735d25ab8fa1/Sources/UUDisplay) · [许可](https://github.com/aoyamashou/UUyc-companion/blob/f5e45dc6d8c5f5fcae2011774d5c735d25ab8fa1/LICENSE) | 读了 `UUMonitor`、`UUReader`、`UUConnectionState`。覆盖窗口、辅助功能读取控制端和短防抖可形成会话信号候选。会话信号不能恢复键盘事件物理来源，实际宿主权限和完整体验需要现场证据。 | `REFERENCE_ONLY`。作为 Reasoned Decision 的解空间反例。原项目是否复用，由项目验证和授权。 |
| Stan User's Guide 2.36，文字/图像 CC BY-ND 4.0，代码 BSD 3-Clause。 [预测检查](https://mc-stan.org/docs/2_36/stan-users-guide/posterior-predictive-checks.html) · [许可](https://github.com/stan-dev/docs) | 查了先验参数抽样、生成数据及其与后验预测的区别，以及独立随机数取样示例。可给 #74 做方案基线，合理观测范围与近似误差另有研究判断。 | `REFERENCE_ONLY`。冻结一个真实模型和容易误选的对照后再看现有统计入口。 |
| nf-core Pipeline Specifications 在线版，规定管线采用 MIT，文档只作引用。 [规范](https://nf-co.re/docs/specifications/pipelines/overview) · [复用说明](https://nf-co.re/docs/developing/external-use) | 看了单命令、版本标签、特定版本容器、最小输入和测试。适合给 #84 选真实对照。参考库版本、样本结构与生物学语义仍需按任务核对。 | `REFERENCE_ONLY`。有真实项目任务时再选择管线，核对该工具的版本和许可。 |
| MONAI、ANTsPy，访问日源码，均 Apache-2.0。 [MONAI](https://github.com/Project-MONAI/MONAI) · [教程](https://project-monai.github.io/tutorials.html) · [ANTsPy](https://github.com/ANTsX/ANTsPy) | 核对 MONAI 的教程覆盖及 ANTsPy 配准、变换、分割使用入口。是现有影像工作流的成熟候选。保留物理空间、标签及病例归因需要真实证据。 | `REFERENCE_ONLY`。#79 用困难病例验证一个适配点，再决定实际依赖。 |
| WCAG 2.2 的 3.3.2 解释页与 W3C 文档许可。 [Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions) · [许可](https://www.w3.org/copyright/document-license-2023/) | 查了可见说明、程序化关系和 accessible name 的区别。适合给 #89 表单信息准入一个可观察对照。原生路径、专业任务和真实视觉分别取证。 | `REFERENCE_ONLY`。用于 Frontend Design 与 Product UI Copy 的已有路线。 |

新增采用状态需有实际消费证据。正式设计可先对照既有资源归档，再决定是否适配依赖。 [AI Resources Intake](../../provenance/AI_RESOURCES_INTAKE_V3_6.md)
