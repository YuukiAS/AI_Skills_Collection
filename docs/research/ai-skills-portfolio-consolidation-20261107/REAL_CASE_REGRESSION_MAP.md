# 真实案例如何进入回归

表中的“观察”引用仓库公开记录。部分原始成品只在项目侧留存，本次只核实中央可读摘要、相关源码和已公开的结果，保持各自的证据强度。回放列是下一轮要验证的行为。这些回放尚未在本轮执行。

| 已记录的真实案例 | 失败类别及主要 owner | 后续回放与应保持的行为 |
| --- | --- | --- |
| Edge/Windows 过早宣布路线，Tailscale 未定位持久状态，iTerm2 漏查原生设置，UU 远程漏查社区和客户端机制 | **Reasoned Decision**。来源调查、可行路线、状态权威和停止标准。四个证据对应同一决策链的不同断点。 [公开案例](../../design/reasoned-decision/evidence/) | 同一原问题下先明确成功所需条件，调查准确版本和原生开关，按证据降级，缺失条件影响排序时做最小探针。已经排除原生路径时，给可执行的替代建议。遇到高影响操作，单独核对授权。 |
| 人工接受的多选一决策样本给出首选、备选与停止条件 | **Reasoned Decision** 正控制。其价值在判断结构与来源强度，具体服务流程会变化。 [历史 seed](../../skill-todos/reasoned-decision.md) | 换任务时仍能说明哪些证据决定选择和何时停止。验证旧样本结构时避免复用旧产品事实。 |
| 近期“先做什么”、技术关系、热图轴、连续纠偏、Reasoned Decision 架构解释。回答有信息却没按读者问题组织 | **Clear Writing**。普通解释的直接回答、解释对象和失败后重组。已有相近规则，需要查是否实际消费。 [TODO](../../plugin-todos/writing-style.md) | 短答首段交付动作。解释图先说坐标、数据、视觉含义。连续纠偏时重建用户问题和解释模型。保持必要限定、公式、关系完整，复测该保留的完整技术回答。 |
| 044 完整中文稿仍留下内部术语且审查没读成稿。DII 长文、跨源 Pro 汇报事实正确但给读者留下比较工作 | **Clear Writing** 的文档与综合。审查证据缺失由 Workflow Core / 对应 review 机制承担。 [044 记录](../../workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md#101-artifact-aware-review-与-044-回归) · [近期案例](../../plugin-todos/writing-style.md) | 在完整首稿上分别验事实保真、读者信息选取和成稿可读性。保留各来源不同意见和仍未解决项，完整成稿须实际可读且被对应审查消费。 |
| Asteria 的成熟参考研究未落实到 Figma、执行合同和真实评审，旧负例被自评盖过 | **Design Assurance**。把研究、失败与设计决定变成可核对的执行约束。Frontend Design 保持专业视觉与动效 owner。 [公开记录](../../plugin-todos/workflow-core.md) | 证明下一位执行者能在目标设计和候选上逐条定位高风险改动。拿掉一条实际约束后，审查能指出执行包缺口。复用失败场景时把具体 UI 约定留原项目。 |
| Atlas 已有精炼文案，首交仍遗漏读者需要的可执行内容。专家科研图含过度解释 | **Artifact Content Design 候选**，Design Assurance 负责准备阶段交接。领域决定信息是否必须、优先和摆放位置。 [公开记录](../../skill-todos/artifact-content-design.md) | 同时保留“缺关键操作信息”和“加入多余说明”的反例，避免把内容准入变成删词。 |
| CAT-TRACE v13/v14 有页间理解、首用、图文层次问题，STAT5060 教学返修改坏已接受页或共享组件 | **Presentations**。分别测试科学叙述与教学任务、冻结页和模板、完整渲染。 [主 TODO](../../plugin-todos/presentations.md) · [锁保护](../../plugin-todos/presentations-core-history-lock.md) | 至少保留新建和既有 deck 各自入口。真实投影比例检查，候选页与整套 render 可追溯。允许经授权解锁，受锁范围回归需拒绝。 |
| 教学 deck 的 reviewer 缺渲染能力仍判通过、审批与候选没绑定 | **Presentations** 验视觉和教学，review transport 负责能力与证据身份。 [审查案例](../../plugin-todos/presentations.md) · [CI 合同修复](../../../results/presentations--ci-missing-render-contract-repair/RESULT.md) | 先证明 reviewer 能看真实像素，再接完整 artifact。负例覆盖错 candidate、旧意见和像素无法读取。普通单页小修保留合适的轻量流程。 |
| STAT5060 HW1 与 Final Project 经多轮有效编译仍不合读者任务、信息预算或语义分组，冻结内容在返修中漂移 | **Research Authoring / 课程文档**。先冻结学生与教师的内容权限，再查实际 PDF 页面和语义边界。 [事后复盘](../../design/research-authoring/STUDENT_ASSESSMENT_HW1_FINAL_PROJECT_POSTMORTEM_AND_NONRECURRENCE_V1_2026-10-07.md) | Homework 和 Project 分别检验语义锁、正反版面、教师保护字段、原生 renderer 与最终文件入口。课程具体题目和权威由课程方决定。 |
| 正式 PDF 名义调用时走错误 renderer，或渲染完首次回复只有路径 | **render-chinese-math-pdf** 正常渲染。**Delivery Assurance** 只消费真实首交事件。 [#80](https://github.com/YuukiAS/AI_Skills_Collection/issues/80) · [#101 结果](../../../results/documents-media--pdf-save-as-delivery/FINAL_REPORT.md) | 分别验证实际 Pandoc/XeLaTeX、数学/字体、首条面向用户的可下载文件。上游生成成功、内部路径和机械检查各有用途，交付宣称需确证文件入口。 |
| Lucerna 源码测试与独立审查已通过，但目标分支和本机安装结果不能由此推定。Producer 遗漏已有截图可见问题 | **Delivery Assurance** 的目标与消费证据。产品 owner 核实安装归属、Frontend Design 核实原生交互，Bridge 负责安全操作。 [公开记录](../../plugin-todos/workflow-core.md) · [#107](https://github.com/YuukiAS/AI_Skills_Collection/issues/107) | 用冻结候选分别检查已审查、远端落点、可安装产物、真实用户表面，按任务承诺声明。重复启动项只能以真实归属取证。 |
| ChatGPT Web 独立 Critic 指出交付设计仍有产品缺口。已发布 056 含工作流与权限边界 | **Delivery Assurance** 的先前候选，和 **Workflow Core / Bridge Kit** 的已发底座分开。 [fresh Critic 回归](../../../results/chatgpt-web--pass-integrity/DELIVERY_ASSURANCE_FRESH_CRITIC_REGRESSION_2026-10-20.md) · [056](../../../results/056_product_delivery_discipline/RESULT.md) | 独立拒绝保留原 verdict。候选变化后重绑证据。正常可执行的小改走其轻量路径，授权缺失时控制受影响动作。 |
| Bobbio/Figma 设计源曾被实现绕开。Asteria 科学图连接线触错语义，浏览器表现也不能代替原生交互 | **Frontend Design** 的产品表面与 **Scientific Visualization** 的图语义分开。 [前端 TODO](../../plugin-todos/web-development.md) · [图语义 TODO](../../plugin-todos/scientific-visualization.md) | 复验已发的设计源和原生能力，检验真实语义与浏览器到原生的边界。科学图第二案例确认后再推进通用规则。 |
| 统计方案把算法选择留给执行者。误差、seed 和长运行进度没有对齐统计目标 | **Statistical Modeling**，前置设计缺口。公开记录来自方案审阅，未观察到本插件的生产失败。 [#75–78 入口](../../plugin-todos/statistical-modeling.md) | 用同一实际统计任务核对可执行算法、独立数值参照、随机性来源和日志能否区分问题。集群生命周期由原工具层管理。 |
| Project instructions 追加一项时挤坏整体预算、未正确反映共享设置。Slurm 受保护作业需要本人当次确认 | 各自保持 **Project Instructions Editor / Slurm Workflows** 独立。 [PIE 记录](../../skill-todos/project-instructions-editor.md) · [Slurm 记录](../../skill-todos/slurm-workflows.md) | 回放真实基线和可审阅差异。危险 Slurm 操作只在合法授权与安全环境取证。既有豁免及 live 未运行边界照录。 |

已知失败适合开发回归，独立泛化另冻结新样本。回放结果要绑定最后一个实际候选、正常调用和完整产物。应保持行为包括短任务轻量路径、已批准范围、原专业语义、已接受页面和安全授权。
