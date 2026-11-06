# GPT 与 Codex 各负责什么

双端产品应围绕一条实际任务分工。能够访问事实、读懂真实产物或执行安全动作的一端持有对应证据。两端共用可复核的输入和交接条件，各自报告自己实际观察到的行为。独立 Critic 仍需独立上下文和候选身份。

## 六条研究线

| 方向 | GPT 侧 | Codex 侧 | 共享材料和入口判断 |
| --- | --- | --- | --- |
| Reasoned Decision | 澄清完整目标，调查现实选项，比较与裁决，说明停止条件及何时改判。 | 对依赖仓库、设置或宿主状态的证据做限定探查，回传结果及可推翻假设，再执行已授权路线。 | 共用任务状态、候选、适用条件、关键未知与改判理由。双端角色互补，Codex 无需复制一套对话裁决。 [研究](WORKSTREAMS/REASONED_DECISION.md) |
| Clear Writing | 普通回复、解释、多源综合和可直接阅读的成品。 | 实际处理文件、做候选保真核对、把语言检查接到文档或界面 copy freeze 前。 | 共享读者任务、保真约束与语言能力。两端都需要正常入口，账号和仓库的入口形态可不同。 [研究](WORKSTREAMS/CLEAR_WRITING.md) |
| Design Assurance | 识别会改变结果的设计决定，提出澄清，收敛验收情景，给用户可审阅的变化。 | 核对现有源码、约束、外部接口、实现可行性和取证办法，必要时做授权探针。 | 双端复用设计源、约束、证据和未知。只在复杂设计或高返工代价场景引入准备审查，继续沿正式 Planner–Critic。 [研究](WORKSTREAMS/DESIGN_ASSURANCE.md) |
| Delivery Assurance | 澄清交付承诺、从实际对象独立审查、解释当前能交付到哪一步。 | 从正常入口运行领域验收，核对同一候选、目标环境及用户能否实际使用，把失败送回原任务。 | Codex 主入口。GPT 在能直接观察产物且需要独立判断时参与。共享确切候选与证据，不设对称的完成按钮。 [研究](WORKSTREAMS/DELIVERY_ASSURANCE.md) |
| Presentations | 冻结页任务、专业叙述、受众和新建/返修范围。 | 消费精确模板与已接受页锁，制作、完整渲染并提交真实像素给独立评审。 | 双端有价值，共享源到页、锁、模板和完整成品契约。懂科研叙述与实际生成分别取证。 [研究](WORKSTREAMS/PRESENTATIONS.md) |
| Research Authoring | 负责论点、科学证据关系、受众、文档叙述和需要作者裁定的问题。 | 负责源材料和产物身份、文献/引用核验、专业工具、排版渲染及真实交付。 | 双端消费同一文档合同，论文、报告、课程各自有可观察产物。保存批准的语义和变更范围。 [研究](WORKSTREAMS/RESEARCH_AUTHORING.md) |

## 其余主要入口

| 产品 | 分工与下一步 |
| --- | --- |
| Workflow Core | GPT 已有 Planner/Critic 合同。Codex 用执行入口、权限分类、恢复与适当验收。桥接由 Bridge Kit 负责，当前无需另加对称 GPT 产品入口。 |
| AI Skills Maintainer | Codex 当前机器或当前任务维护，实际取证发布、安装、消费和回归。GPT 可做设计审查与优先级判断，经现有角色接口接入。 |
| Frontend Design | GPT/设计端做任务、内容和视觉意图。Codex/Figma 或原生可用环境核对实现、动效、实际交互与屏幕效果。页面规则与证据可以共享，浏览器替代与实际设备分开。 |
| Scientific Visualization | GPT 和领域专家决定科学问题、图该证明什么和阅读目标。Codex 保持数据与视觉编码，生成并核查真实成品。仅当产品声称支持上述任务时评估双端，不另开一个解释图的插件。 |
| Statistical Modeling | 共享 estimand、假设、算法、诊断和数值容差。GPT 负责证据和方案判断，Codex 负责真实分析与复现，实际科研决定由有权的领域方裁定。 |
| Bioinformatics / Medical Imaging | 按数据和工具可用性分工。领域设计与权威核对可以在 GPT，参考库、格式/影像几何、pipeline 或真实病例观察通常在 Codex。是否需要双入口等待取证，不扩大到项目架构。 |
| 独立 Skill | PDF 和 Slurm 以实际运行环境为主。PIE 的用户指令理解和真实文件核验可分别在两端，用可审阅差异交接。课程候选走 Research Authoring 领域路线，Artifact Content Design 先做可共享的准备能力。 |

三条可靠性产品线的交接应尽量短。Reasoned Decision 给出选路依据和仍能改变选择的未知，Design Assurance 交出被证明可落实的设计约束和验收情景，Delivery Assurance 核对交到用户手里的实际结果。任一步遇到会改变前提的新事实，可以把差异退回原负责人。Workflow Core 继续处理阶段、授权与恢复，Bridge Kit 继续提供运行和传输能力。
