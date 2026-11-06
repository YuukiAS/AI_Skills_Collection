# 维护问题怎么合并

同类问题应共用一个维护入口、保留不同真实样本。一个样本可以检验多个能力，但是否要改规则、改实现还是修调用，取决于原有能力承诺和真实入口是否消费。下表是研究分流。原有 maturity 和 Issue 生命周期由各自来源维护。

| 归并结论 | 证据与处理 |
| --- | --- |
| **规则已存在，先查正常入口** | Clear Writing 的直接作答、按读者任务组织、保真和受众语体已在 0.5 多条 route 中。对近例先复现实际加载与成品行为。Presentations 多项完整 render、独立 reviewer 和锁保护已有包内合同。若候选仍失效，应排查调用、artifact 身份和真实视觉检查。PDF renderer 的原始路线、数学保真、首次下载也已有发布，复发按已发布行为验收。 |
| **合并证据** | iTerm2 原生设置、UU 社区线索和 Tailscale 权威状态都是寻找真实解空间的一条链。Clear Writing 的连续纠偏与双路汇报分属重答和跨源综合两类，沿现有入口追加样本。课件的 reviewer 自证、没读像素、审批与候选错位共用独立视觉验收。页锁、共享组件锁和历史反馈保留分为同一返修能力的不同反例。 |
| **新能力候选** | Reasoned Decision 的证据调查与选路，Design Assurance 的执行前设计可行性，Delivery Assurance 的实际消费者准入各有独立用户问题。Artifact Content Design 的跨载体内容准入先做共享候选，科研学习笔记先在 Research Authoring 中试。 |
| **项目内保留** | Asteria 的参考产品、配色、图谱布局与动效选择，STAT5060 的具体题目、判分与学生规则，CardiacNexus 的架构、病例细节和数据约定，科研统计项目的算法参数都由原项目持有。中央只提取可复验的通用失败。 |
| **证据不足** | 生信、医学影像、统计和可视化的课程驱动方向仍缺真实正常入口的前后对比。Asteria 交互科学图需另一个科学图任务或可核实严重单例。PIE 私有 locator 需真实来源与权限边界。编排配置只能作为用户提供的输入候选。 |
| **值得研究下一版本** | Clear Writing 用单入口检验选择信息和纠偏行为。Presentations 沿现有 0.5 设计审双端、模板、冻结返修和视觉评审。Research Authoring 优先继续 #99 的已有 release 路径，课程领域能力与学习笔记各自取证。 |
| **已有实现或更强规则** | AI Skills Maintainer 的版本发布、当前机器更新和回归处理已有机制。Bobbio 的 Figma canonical source、全屏和原生交互等多条旧候选已发布或被更强路线覆盖。Slurm #95/#96/#109、PIE #93/#102、PDF #80–82/#101 留回归。只有 exact 能力、消费者和当前 Issue 对上后才考虑压缩记录。 |

## 逐入口覆盖

以下范围按基线文件行号和独立问题族列出。连续范围涵盖中间所有带状态的段落，补充设计中没有结构化状态行的内容按整篇归属。Presentations 的示例模板不计入真实问题。附加材料用于解释具体问题，不新增待办入口。

| 基线入口 | 问题族、范围和建议 |
| --- | --- |
| [ai-skills-core](../../plugin-todos/ai-skills-core.md) | L7–29 已有“先查实际消费再去重”。L31–89 更新、陪同维护、产物审查和分发均保留为既有能力与回归。 |
| [bioinformatics](../../plugin-todos/bioinformatics.md) | L7 #84 取真实数据库/组学任务与版本、格式、复现记录后再设计。 |
| [medical-imaging](../../plugin-todos/medical-imaging.md) | L7 #85 与 L20 #79 分开。课程方向缺证。困难病例先验证可复用发现与归因及成熟组件。 |
| [presentations](../../plugin-todos/presentations.md) | L11–107 最近 CAT-TRACE 样本、读者导航、审查真实性和版式。L115–183 045 已标推广的能力与同类返修。L190–227、L266、L291–336、L434–577、L590、L642 教学、模板和可读性。L238–257、L273–282、L347–392、L410、L462、L603–630 独立审查和候选证据。L401 模板与图分工。L421 文件首交。L669–709 旧开放候选归回上述类。L719–730 历史锁和控制器候选归既有返修工作流。L657 是示例。 |
| [Presentations 制作流程](../../plugin-todos/presentations-authoring-production-workflow.md) 与 [历史锁](../../plugin-todos/presentations-core-history-lock.md) | 已有共享运行合同。主线契约和分支实际消费分别核对。禁止把可运行文档推定成正常入口成功。 |
| [reasoned-decision](../../plugin-todos/reasoned-decision.md) | L5–34 四条案例入口共用原生可用性、真实解空间、状态权威和停手回归。具体危险操作与权限的接口交 Critic。 |
| [research-writing](../../plugin-todos/research-writing.md) | L8–147 学习笔记单家族取证。L148–394 文档身份、结构改写、受众与证据位置，收敛到报告领域。L412 文件交付消费已有 renderer/交付入口。L428–553 课程材料信息预算、排版和语义、题库适用性、renderer 委托及冻结返修。 |
| [Research Authoring 制作流程](../../plugin-todos/research-authoring-production-workflow.md)、[课程流程](../../plugin-todos/research-authoring-student-assessment-workflow.md)、[排版收敛](../../plugin-todos/research-authoring-layout-convergence-and-human-review-budget.md)、[文档构成](../../plugin-todos/reader-facing-document-composition-protocol.md)、[学生受众](../../plugin-todos/research-writing-student-audience-and-pre-render-approval.md) | 同一领域产品的准备、语义批准、排版、渲染和返修。跨文档候选需用真实报告反证。布局反例留领域，不转化为通用审批。 |
| [scientific-visualization](../../plugin-todos/scientific-visualization.md) | L7 语言交接核对 #49。L16 专家图结果优先验证。L52 #50 交互图语义与真实渲染。L68 #51 取证。 |
| [statistical-modeling](../../plugin-todos/statistical-modeling.md) | L7 #73 语言适配仍需证明不改统计结论。L16 #74 先验预测 pilot 缺真实对照。L39–68 #75–78 放一个可实施统计方案，四种证据不能互相替代。 |
| [web-development](../../plugin-todos/web-development.md) | L7–215 现有发布/被替代的视觉准入、Figma、动效、原生验证。L232–326 界面可读语义和敏感表单，同类案例留原设计合同。L360 #89 对接内容与文案。L399 专业任务迁移需要第二个样本。 |
| [workflow-core](../../plugin-todos/workflow-core.md) | L9–167 正常入口、运行时归属、真实批次、授权恢复和作用域。L175–240 比对包与领域 QA 等交付问题归 #10/#107，通用流程只负责路由与消费。L263 exact worktree 执行失配留 Host/Bridge。L288 Asteria 的执行前可审阅差异交 Design Assurance。 |
| [writing-style](../../plugin-todos/writing-style.md) | L8–380 近期真实对话与长文，分别收敛成直接回答、解释顺序、纠偏与跨源成品。L549 README 已执行要求。L567–708 通用语言层、英文、科研长文与 UI copy 的现有/候选能力，词汇规则不再扩。L749–772 复杂路线和结构丢失回到读者任务、事实/覆盖保真。 |
| [artifact-content-design](../../skill-todos/artifact-content-design.md) | L7、L28、L57 的三种真实载体检验内容准入、信息密度和操作信息。后续概念保留共享候选。 |
| [course-assessment-authoring](../../skill-todos/course-assessment-authoring.md)、[学生受众](../../skill-todos/course-assessment-authoring-student-audience-gate.md)、[领域工作流推进](../../skill-todos/course-assessment-authoring-canonical-workflow-promotion.md) | 一个领域入口。按 Homework、Project 和受保护教师材料验证，区分已接受的首屏/提交流程、候选协议和实际 runner。 |
| [project-instructions-editor](../../skill-todos/project-instructions-editor.md) | L15–66 #93 已有正式对应。L83 #108 仓库 AGENTS 权威投影是当前窄候选。L788 #102 0.2 已发布。L809 私有 locator 另取证。 |
| [reasoned-decision 历史 seed](../../skill-todos/reasoned-decision.md) | 历史条目和接受样本引用到专属插件 TODO，避免双重维护。 |
| [render-chinese-math-pdf](../../skill-todos/render-chinese-math-pdf.md) | L9–41 #80–82 与 L89 #101 已发布。L52 #83 部分解决，L70 上游自动交接候选需由实际领域正常入口验证。 |
| [slurm-workflows](../../skill-todos/slurm-workflows.md) | L13、L27、L40 是三个已推广的安全/兼容证据族。保留各自 live、test 和豁免边界。 |

## 横向归属

- **同一成品的层次**。领域 owner 决定意义和验收，Clear Writing 按冻结含义组织读者可见文本，Delivery Assurance 判断既有证据是否支持实际交付。课程与演示的签收门槛不同，避免一个通用的“看过成品”检查覆盖两者。
- **同一流程的层次**。Workflow Core 决定正常入口、合法权限与恢复，Bridge Kit 负责跨端传输与工具运行。Design Assurance 处理设计是否具备可执行约束，Reasoned Decision 处理选择什么路线。根据事故最先失效的用户承诺确定单一主入口。
- **看板核对**。看板可读。#13、#90、#98、#99、#107、#108 这些公开 Issue 都仍 open。现有 released/closed 的条目不承诺未来使用自动成功。同号跨文件绑定也需查内容匹配。候选对账见 [CANDIDATE_CANONICAL_EDITS.md](CANDIDATE_CANONICAL_EDITS.md)。
