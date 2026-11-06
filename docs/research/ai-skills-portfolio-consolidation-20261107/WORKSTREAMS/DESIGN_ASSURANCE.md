# Design Assurance：复杂设计何时可以开工

建议下一轮为 Design Assurance 起草独立 Plugin 的正式 Proposal。它应能指出一份设计中哪些决定已落实到执行约束，哪些关键假设需要先试证，实施者拿到哪些材料就能开工。首轮设计应同时用 Asteria 的执行包和一项非 UI 任务验证。Asteria 可以继续裁决视觉和交互候选。它与 Plugin 的接口等正式设计冻结后再接。

本报告依据 AI_Skills_Collection `origin/main@c83ee4b5ab41d0cd4955916e4c81f71de954cbfd` 及 2026-11-06 读取的公开 Issue 和外部资料。Asteria Blueprint 和 Project Atlas 案例取自中央库已公开的记录。报告中的能力和回放均为研究建议，等待 Planner 提案和独立 Critic 审查。

## 仓库目前已有的能力

- **独立 Plugin 仍处于规划。** 基线 Marketplace 和生产 manifest 中未见 `design-assurance`。现有中央记录包括 workflow-core 中的 Asteria 执行包可审阅性条目，以及 Reasoned Decision 架构草案中的多路研究、盲区检查、设计冻结和可实施性分工。前一条保留 `NEW`，未见公开 tracking backlink。 [工作流待办](../../../plugin-todos/workflow-core.md) · [Reasoned Decision 架构](../../../design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md)
- **流程和领域能力已有归属。** `workflow-core 0.5` 已发布，提供分级、角色、正常入口、授权和交接等能力。Planner/Critic 合同已定义执行包、独立审查、范围和权限边界。前端已有 `web-development 0.4`，其中 0.3 发布了设计权威、真实界面证据与统一入口，0.4 补上界面文案交接。Bobbio 的 [#57](https://github.com/YuukiAS/AI_Skills_Collection/issues/57)、[#58](https://github.com/YuukiAS/AI_Skills_Collection/issues/58)、[#59](https://github.com/YuukiAS/AI_Skills_Collection/issues/59) 已关闭，当前工作可复用这些领域能力。 [工作流发布记录](../../../../results/workflow-core--normal-entry-reliability/RELEASE_CLOSURE.md) · [Planner 合同](../../../workflows/PLANNER_ROLE_CONTRACT.md) · [Critic 合同](../../../workflows/CRITIC_ROLE_CONTRACT.md) · [前端版本记录](../../../plugin-changelogs/web-development.md)
- **课程和研究文档已有专项实践。** `research-writing 0.2` 为基线发布版。包内已有课程文档的预执行手册和语义分页补充规定，课程侧也有完整读者正文批准、课程来源优先级、师生材料分层、页面可行性预证等候选实践。文件存在能证明已有方法可借鉴。其正式泛化验收与正常入口消费仍需另查。[#99](https://github.com/YuukiAS/AI_Skills_Collection/issues/99) 跟踪 Research Authoring 正式收口。 [版本记录](../../../plugin-changelogs/research-writing.md) · [课程发布候选实践](../../../plugin-todos/research-authoring-student-assessment-workflow.md) · [包内预执行手册](../../../../plugins/codex/plugins/research-writing/shared/student-assessment-end-to-end-pre-execution-runbook.md)
- **内容准入仍值得独立考察。** `artifact-content-design` 是候选能力，中央 TODO 中保存了不同产物的真实反馈，尚需选定稳定的消费方式。它解决的是“哪些信息值得出现在这件作品上”。Project Atlas 的后续复审在先前 PASS 后仍发现问题，说明完整成品要重新核对。稿件足够供领域审查和成品可交付是两个时点。 [内容设计待办](../../../skill-todos/artifact-content-design.md) · [Atlas 逐项复审记录](../../../design/product-ui-copy/evidence/PROJECT_ATLAS_COPY_REVIEW_HISTORY_2026-11-03.md)

## 四类应进入回放的失败

| 失效点 | 已有真实案例 | 下一轮应查的因果关系 |
| --- | --- | --- |
| 做了研究，但执行者可以忽略它 | Asteria 的三份独立研究各找到 20 多个相关参考。早期候选仍出现默认组件外观、机器状态泄漏和动效不足。后续执行包把真实参考、上一版负例、视觉目标、文案准入、动效和并排验收写成明确要求，用户才有材料判断包是否值得运行。当前证据支持执行包更可审阅，仍需在回放中验证约束是否真的被下一执行者消费。 [Asteria 执行包案例](../../../plugin-todos/workflow-core.md) | 从同一条旧失败跟到实际执行条款、使用入口和可观察的判断依据。只列研究标题、成熟产品截图或“加强 QA”时，该项仍待落实。 |
| 设计源不完整或被误当参考图 | Bobbio 有批准的设计基线，实现仍直接在代码里补不存在的状态，功能过关后原生界面继续偏离。前端已有 canonical design/state coverage 规则。 [Bobbio #58](https://github.com/YuukiAS/AI_Skills_Collection/issues/58) · [前端待办](../../../plugin-todos/web-development.md) | 对齐当前权威设计、主路径与关键异常状态，给出实现者将读取的具体位置。缺失的生产状态先由前端设计决定。这个案例可用于复用前端规则的回归，避免重复设门。 |
| 把冲突或不可行性留到制作阶段 | STAT5060 的旧时间表、未批准安排、计分分区和题号关系曾发生冲突。页面数先定死，后来才发现合法断页不易实现，局部换页命令还能造成与禁止硬分页相同的结果。 [课程复盘](../../../design/research-authoring/STUDENT_ASSESSMENT_HW1_FINAL_PROJECT_POSTMORTEM_AND_NONRECURRENCE_V1_2026-10-07.md) · [语义分页补充规定](../../../../plugins/codex/plugins/research-writing/shared/student-assessment-semantic-pagination-amendment-v1.md) | 开工前锁定权威内容和必要关系。由领域方用最小测量稿证明硬页面约束可实现，或把不可行性退给决策者。教师审批、计分、页面语义和交付分层继续由课程文档承担。 |
| 已有信息被当作应展示的信息 | Project Atlas 的两套候选和 CAT-TRACE 数值 Atlas 在内容成立时仍出现首屏堆叠、重复解释和操作时机错误。课程材料也曾把阅卷方信息当作学生正文。科学图案例还提供了反向检验，冗余免责声明应去掉，会改变专业判断的研究状态应保留。 [内容设计案例](../../../skill-todos/artifact-content-design.md) · [学生读者与审批](../../../skill-todos/course-assessment-authoring-student-audience-gate.md) | 在设计中明确读者、任务和必须出现的内容。用 Artifact Content Design 候选实践区分保留、压缩、移到次级页面和删除，领域方判断内容后果，写作能力修订保留项。一次判断同一个语义单位，渲染后再检查各界面出现位置。 |

可合并的是失效模式和复用证据。前端原生体验、科学图的结论、课程的计分和读者边界各有不同的证据要求。Asteria 的具体技术栈、颜色、字体、动效和视图属于项目设计。清晰说明本轮变化的文字由 Clear Writing 协助，Asteria 反馈记录中的长段否定式开头和重复说明可进入它的回归集。 [Clear Writing 待办](../../../plugin-todos/writing-style.md)

## 可借鉴的外部方法

以下是研究采用建议。代码、模板和运行依赖均处于原样参考阶段。访问日期为 2026-11-06。

| 来源、版本与许可 | 实际检查 | 可借鉴的部分和边界 |
| --- | --- | --- |
| Matt Pocock `grill-me` 和 `grilling`，`4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`，[MIT](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/LICENSE) | 入口为显式调用，访谈核心按已满足前提的问题分轮推进。Agent 自行查事实，用户裁定偏好和有权决定的取舍。读了上游 [#1123](https://github.com/mattpocock/skills/issues/1123) 的 Codex 工具兼容报告和 [#686](https://github.com/mattpocock/skills/issues/686) 的结束范围讨论。 | `REFERENCE_ONLY`。复用“只问阻断决策的问题并给出建议”这一思想。访谈共识仍需连接到可执行条款和可行性证据。薄入口调用的 `Skill` 工具在各环境中的可用性需单独证明。 [grill-me](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grill-me/SKILL.md) · [grilling](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grilling/SKILL.md) |
| Matt Pocock `grill-with-docs` 和 `domain-modeling`，同一提交与 MIT 许可 | 核对了薄入口、词汇即时落盘及仅在难反转、有真实取舍且需补上下文时提议 ADR 的规则。上游 [#341](https://github.com/mattpocock/skills/issues/341) 有决定只留聊天、交接后被重复询问的用户案例。 | `REFERENCE_ONLY`。借鉴及时把会改变后续行为的决定写到可引用的既有文档。Glossary 和 ADR 只能承载部分决定，执行包仍须明确每条关键约束的消费位置。 [grill-with-docs](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/grill-with-docs/SKILL.md) · [domain-modeling](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/domain-modeling/SKILL.md) |
| GitHub Spec Kit，`573b1cf7ac1a45f85594a83c47467f90e230380f`，[MIT](https://github.com/github/spec-kit/blob/573b1cf7ac1a45f85594a83c47467f90e230380f/LICENSE) | 核对 `clarify`、`checklist`、`analyze` 文档。分析操作只读检查规格、计划和任务之间的覆盖、冲突及模糊点，把问题退回对应文档。检查表由审查者判定，通过仅表示要求质量达标。 | `REFERENCE_ONLY`。借鉴从要求追到任务、反向发现无来源任务的做法，用本库既有文件即可。跨文档内部一致仍可能共同引用了错误来源，也无法证明真实环境可行性。整套脚手架与现有 Planner/Critic、Reviewed Handoff 重叠。 [固定版本原文](https://raw.githubusercontent.com/github/spec-kit/573b1cf7ac1a45f85594a83c47467f90e230380f/docs/reference/agentic-sdd.md) |
| CMU/SEI Architecture Tradeoff Analysis Method，CMU/SEI-2000-TR-004，2000 年 8 月。报告版权归 CMU，复制或派生权限按原文 | 核对官方九步说明和报告第 5、7、8 节所列场景、风险、敏感点、权衡和评审步骤。高优先级场景用来检验架构，另由利益相关者补充场景。 | `REFERENCE_ONLY`。借鉴用成功、关键失败和恢复场景压测重大取舍，按风险选取数量。完整工作坊规模偏大，适合复杂架构专题。场景评估仍需接入仓库事实、授权和后续执行包。 [官方方法说明](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/) · [原始报告及权利声明](https://sei.cmu.edu/documents/629/2000_005_001_13706.pdf) |
| NASA Software Engineering Handbook，Ver D §7.09。公开政府资料，页面未列软件许可，第三方素材另有使用边界 | 核对 PDR/CDR 的入审条件、所看对象和出审条件。详细设计通过审查前需覆盖需求与设计双向追溯、接口、约束、测试计划、风险及已知未决事项。 | `REFERENCE_ONLY`。借鉴将“材料齐备”“审查足以开工”“实施后已证实”分开。航天项目专用阈值、完整评审节奏和法定签署条件不进入通用 Plugin。 [NASA 软件手册 §7.09](https://swehb.nasa.gov/pages/viewpage.action?pageId=198771067) · [NASA 使用指南](https://www.nasa.gov/nasa-brand-center/images-and-media/) |
| Michael Nygard 的 ADR 原文，2011-11-15，公开文章，页面未标明开放许可 | 核对决策记录的上下文、选择、状态和后果，及被新决定取代的记录如何保留。 | `REFERENCE_ONLY`。已有 ADR 可以记录设计变化的来由和被替代条件。ADR 只证明做过决定，开工判断还要检查接口和方案如何被实施者消费。 [原文](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) |

## 首版产品构想

正常入口可以是“检查这个设计能不能交给实现”，或“根据上一轮失败判断现在还缺哪几条”。用户给出当前 Proposal、设计稿或源码入口、计划投入和不可更改的边界。最终得到一份可以独立复核的实施前判断，说明哪些已具备、哪些阻断开工、谁能补上、允许在什么范围内继续。简单可逆的局部调整沿用原领域入口。涉及多边界、高返工代价、已经严重失败过，或用户明确要求独立设计审查时，单独入口才有收益。

1. **核对设计权威与关键选择。** 绑定当前设计、相关实现、用户确认、领域规则和反例。挑出会影响接口、权限、目标或可验证性的冲突。能查到的事实自行解决，只有真实取舍回到用户或决定者。若证据推翻已确认的产品路线，转 Reasoned Decision 重新裁定。
2. **在关键场景中查盲区和做最小试证。** 用正常使用、最严重且相关的失败、必要的恢复、必须保持的既有行为走一遍设计，按风险选场景。需要实证时由 Codex 或领域方核对一跳源码、实际数据形状、代表性原型或测量稿。没有可接触的证据时，指出待核条件和开工范围。
3. **核对研究和反馈能否被执行。** 将少量会改变结果的发现映射到实际 Proposal、设计稿、执行限制或验收场景。区分仅参考、已绑定要求、负对照、以及实际执行依赖。独立审查者应能根据定位自行读到条款。“关键变化与落实点”在要求用户运行下一执行者前出现，每条交代旧问题、落实位置和可验证效果。没有实质变化时省去这一步。
4. **把可实施的设计交给既有流程。** 在现有 Proposal/Plan/ADR 中明确当前版本、关键约束、领域验收要求、证据负责人、必要授权和重新审查条件。剩余项若都属于可逆实现细节，现有 Critic 可继续判断执行就绪。局部范围能独立开工时说明其边界。正式冻结、授权和独立通过依现有角色合同办理。 [Capability Gate 政策](../../../workflows/PLUGIN_CAPABILITY_GATE_POLICY.md) · [Planner 合同](../../../workflows/PLANNER_ROLE_CONTRACT.md)

仅加一个追问 Skill 能改善访谈，无法证明执行合同消费研究、覆盖边界和能在实际条件下实现。把检查拆给各领域可保持专业判断，但跨越设计、前端、文档和执行的遗漏仍需要统一可调用的复核入口。独立 Plugin 的新增价值应由同一小套判断在不同领域的实际使用证明。它可以复用仓库中已有的审查组织、源定位和领域试证，无需引入看板、生命周期、状态、审查角色或文档系统。

## GPT、Codex 与相邻产品的交接

**GPT 优先承担设计梳理。** 适合整合多路研究、辨别不同领域的冲突、提出可证伪场景，和用户处理需要他决定的取舍，再把少量关键选择写入现有设计文档。对无仓库依赖的概念设计，GPT 可以独立给出设计评审。依赖实际接口或材料时，应把未核验事实明示为条件。

**Codex 优先承担事实核查。** 适合按版本读取源码和配置、定位一个调用链、比对当前执行包实际引用、核验验收方法可用，并在授权范围内做窄试证。已有完整设计时可以直接进入 Codex 的实施前复核，实质产品决策送回 GPT 或用户确认。两端共享设计决定、权威版本、关键约束与观察方式。用仓库中同一份材料交接即可。是否做两个独立命令应由正常入口试用决定。

| 相邻能力 | 接缝 |
| --- | --- |
| Reasoned Decision | 它给当前选择、依据与推翻条件。Design Assurance 把选定方向细化并检验可实施性。发现新证据触发推翻条件时将证据退回给决策方。 |
| workflow-core | 它负责规划执行流程、角色、权限、交接、等待与恢复。Design Assurance 给出供现有 Planner/Critic 使用的设计就绪证据。用户仍沿既有入口授予执行权限。 |
| Asteria / Asteria Blueprint | Asteria 产品可以把获批决策和约束连接到自身长期系统模型、源码、证据及漂移。Design Assurance 只需能输出可引用的设计决定和重审条件。原型模型、图谱、浏览、交互和长期维护由项目负责。 |
| Delivery Assurance 与 Bridge Kit | Design Assurance 交出哪些承诺需要如何验收。Delivery Assurance 在真实候选出现后查对应证据、正常入口、防降级、防回归和可交付声明。Bridge Kit 承担受权运行、传输、身份与恢复的机制。公开 [#107](https://github.com/YuukiAS/AI_Skills_Collection/issues/107) 的 `da/1` 冻结和生产验证仍有各自门槛。 |
| 领域 Plugin 与 Clear Writing | 各领域拥有试证和最终质量判断，例如原生动效、科学论断、学术页流、图像真实性。Clear Writing 负责把变化与结论写清。Design Assurance 检查这些判断由谁完成、怎样观察以及遗漏会怎样改变能否开工。 |

## 交给正式 Planner 的验证问题

建议先用以下成对案例比较现有 Planner/Critic 路线和加入专门设计复核后的路线。观测点应是同一输入能否识别实际阻断点、是否保住原有约束、接手者能否开始获准的工作。案例的改良版本可作为正例设计，最终效果仍须通过正常入口实测。

- **Asteria 成对执行包。** 旧包包含研究，却允许从默认组件出发制作，缺真实参考消费、动效证据和明确的负对照。正向包应能从旧失败追到实际的视觉目标、已绑定的比较对象、一个主要界面范围和可观察的验收方法。另移除任一关键约束，要求独立审查指出缺失并定位。原型阶段的视觉或交互裁决不因产品接口未冻结而停摆。
- **非 UI 正反例。** 取课程复盘中的权威冲突和语义分页。允许开工的一侧应绑定获批正文和当前来源，并由领域方法证明至少一种合法排法。另一侧输入完整的格式清单和测试绿灯，但保留过期来源、失效的题号引用或未试证的硬页数，期待给出具体退回对象及理由。受保护的教师内容继续留在相应层。
- **复用与不过度触发。** 使用已有 Bobbio 类设计规则，审查应识别前端负责的缺失状态和原生证据，直接引用现有质量门。再用一个有明确验收的小范围修订，预期普通路径直接推进。
- **失效与复审。** 冻结后发现实质接口变化或用户撤回关键限制，应只重开受影响的决定和场景。文案笔误等可逆细节沿原路处理。设计就绪时仍保留实际交付验收，后续只出现截图或组件测试时不给真实成品通过。

Planner 应先确定独立调用阈值、最低设计证据、谁有权判定通过、哪种变化触发复审，以及 Asteria 首批消费哪些字段。优先用既有 Proposal、Plan、ADR 和验收证据承载这些内容。采用外部 Skill、定义固定数据接口和把内容设计升级成独立产品，均可等首轮证明具体需要后再裁定。
