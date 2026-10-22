# PIE 0.3：仓库 AGENTS 的建立、维护与真实消费——架构提案 v0.2

状态：待独立架构 Critic；不授权实现或修改消费者仓库  
设计归属：`YuukiAS/AI_Skills_Collection`，独立技能 `project-instructions-editor`  
任务键：`project-instructions-editor--0.3-agents-authority-maintenance`  
当前基线：PIE 0.2；Issue：[#108](https://github.com/YuukiAS/AI_Skills_Collection/issues/108)  
本轮用户反馈：v0.1 只有职责和抽象规则，没有解释模板、完整操作、真实样例及自动入口；因此修订为可逐步检验的设计。  
受审前来源：AI_Skills_Collection `main`，Bridge Kit `main`，AI Research Toolkit `main`，真实 SeminarArc 文件。

## 1. 用户到底得到什么

以后用户在 Codex 里说「整理这个仓库的 AGENTS，去掉重复内容，但别丢安全规则」，或一个已批准的项目任务确实要求更新长期指令时，PIE 应从**真实仓库当前文件**出发，核对适用目录、现行权威和版本，整理出更容易被未来任务正确读取的指令。用户能审查实际删改、看到完整结果；Codex 在合法写入后读回验证，不能靠“更短了”宣布通过。

这和只把 `AGENTS.md` 里的句子润色不同：目标是「后续真实任务在行动前可以找到正确约束，而且旧约束没有被删弱」。内容正确不等于运行时已加载，二者分别负责。

PIE 0.2 对 ChatGPT Project setting 的完整当前基线门、受保护缺失、局部修改、改动预览与完整干净结果全部维持原样。0.3 仅新增独立的仓库指令模式。

## 2. 真实现状：模板已经存在，不能挪走

Bridge Kit 的 `templates/repo/AGENTS_TEMPLATE.md` 是一次性**初始文件骨架**。当前 `ai_bridge_kit/cli.py::projected_agents_snippet` 在没有根 `AGENTS.md` 时确实读取模板并追加 Bridge 自管区块；已有文件则只追加/按要求更新受管区，保留项目自有正文。Bridge 的 `readiness.py` 只对相关受管写入检查合并后的真实指令容量，不会替用户压缩自有规则。

同时，AI Skills 安装器可能通过 `shared/templates/AGENTS.md.template` 写入独立的技能索引受管区。这与 Bridge 受管区是**两个 owner**。

据此冻结唯一模板归属：

- **Bridge 保留现有物理初始模板**及 `ai-bridge init`，不迁到 PIE，不需要先安装 PIE 才能初始化。
- **PIE 拥有长期指令如何组织、保留、压缩、迁移的编辑合同**，不是第二份可自动覆盖项目的通用模板。
- **项目仓库拥有实际完成的 `AGENTS.md` 正文**；Bridge/AI Skills 受管区分别归各自安装器。
- **没有 Bridge 的仓库**：PIE 按相同编辑原则从真实项目来源构造简短项目指令，不伪造 Bridge 区块，也不依赖运行时下载 Bridge 模板。
- Bridge 模板以后更新，影响后续 `ai-bridge init` 的新项目；**不自动迁移旧仓库**。除非有真实失效或项目 owner 发起维护，PIE 不为追求统一重写老仓库。

Bridge 新建的模板骨架不是「已经写好了这个项目的规则」。其中 `Define the product...` 一类占位引导仍需要后续合法项目任务根据真实 README/TODO/合同填写，且不能虚构项目事实。

## 3. AGENTS 的目标信息架构

根文件不是百科全书，也不是必须填满的固定六节表。建议从下列六个问题决定是否需要章节：

1. **项目是什么、哪份文档具有当前权威**：项目目标、版本/阶段边界、不可替代的专业原则。
2. **从哪里开始**：当前任务入口、必须在行动前读取的稳定定位、计划和权限来源。
3. **什么绝不能违反**：授权、安全、隐私、数据、证据强度、用户已经接受的不可退化约束。
4. **什么类型的任务读什么规则**：软件子系统、设备、科研、用户界面、发布各自的条件触发与真实定位。
5. **何时才算完成**：最少的专业验收入口与最终消费对象；详细检查矩阵不全文复制。
6. **详细资料和受管区域在何处**：较长操作说明在项目文档；Bridge 和 AI Skills 受管区禁止人工改写。

根 `AGENTS.md` 放全仓且必须在查阅更深文档前生效的边界。只有子树有真正不同的规则时才添加子目录 `AGENTS.md`；不用为每个目录建立文件。同目录 `AGENTS.override.md` 会遮蔽 `AGENTS.md`，不能把两者误算成共同生效。具体规则由实际 Codex 发现路径、`CODEX_HOME`、`project_doc_fallback_filenames` 与 `project_doc_max_bytes` 决定；默认 32 KiB 是官方缺省值，不是允许 PIE 擅自提升的预算。

原则：全仓最低安全要求不能因为更深一层文件后加载就被无权削弱；合法的局部专用测试命令可以覆盖普通测试入口。哪个例外真的合法，取决于项目/领域正式合同，不取决于文件层数。

## 4. 一个真实仓库的具体例子：SeminarArc

**以下素材来自真实当前文件，但整理结果是设计示范，不是已实施的 Git 修改。**

已读取：
- `YuukiAS/SeminarArc/AGENTS.md`：设备测试安全摘要、项目技能、早期版本范围、产品不变量、Bridge 区块；
- `YuukiAS/SeminarArc/docs/DEVICE_TESTING.md`：真机操作禁令、模拟器与 WSL 环境、实际设备核对和详细命令；
- `YuukiAS/SeminarArc/TODO.md`：当前产品路线图及历史 `0.1.x` 合同的适用范围；
- `YuukiAS/SeminarArc/prompts/AGENT_RULES.md`：目前仓库继续使用的 `prompts/tasks/<id>_task.md` 入口。

建议 root 的项目自有正文组织如下（保留真实原则，非整文件覆盖文本）：

~~~markdown
# SeminarArc — 仓库指令

## 目标与当前权威
这是本地优先的学术报告记录应用。当前产品规划与阶段范围以 TODO.md
为准；0.1.x 的详细实现合同见 docs/plans/0.1.x-mvp-implementation-plan.md。
历史阶段限制只适用于对应阶段，不自动覆盖后来已批准的能力。

## 正常任务入口
执行前读取 prompts/AGENT_RULES.md 和本次实际任务文件。
当前仓库仍有 <id>_task.md 形式的有效交接约定；
未经专门批准，不因为 Bridge 新模板采用另一种 task_key 就全仓迁移。

## 行动前必须遵守
Android 测试优先使用模拟器；受保护物理真机只接受本次明确授权的专项检查。
禁止为测试便利自动重置或恢复 ADB、USB、usbipd、WSL 及设备传输。
真机操作必须复核设备身份，并在获准写入前后执行检查。
物理设备通道阻塞不代表其它开发和模拟器测试被阻塞。
不得在仓库、日志或发布物中保存 PIN、密码、私钥等秘密。
不得以假数据、静态按钮、未完成的音频片段冒充产品完成。

## 专业规则按需读取
设备操作：docs/DEVICE_TESTING.md。
Android 架构：.agents/skills/android-lead/SKILL.md。
Compose：.agents/skills/compose-expert/SKILL.md。
产品阶段、实施合同和验收：TODO.md 及它指向的已批准文档。

## 项目级数据与验收不变量
素材必须归属于明确的 seminarId；同一时间最多一场 ACTIVE seminar。
录音状态使用持久来源；片段只有 READY 才能被当作可播放。
测试应匹配真实目标；仅凭构建或模拟通过不得宣称真实设备验收完成。

## 受管内容
既有 Bridge 和 AI Skills 生成区块必须保留原有字节；
需更新时分别使用对应正式安装器。
~~~

示例中的文字必须逐条与现行合同对应；真正写入时仍须完整保留当前 root 其它独有规则，比如 internal dogfood 权限、单模块 Android 限制、界面/可访问性要求及原有 Git/发布边界，除非能证明它们有准确、会被读取的下沉权威。不能照抄示例而删掉未展示的约束。

三种具体场景：

- **正向整理**：root 有一段环境路径和设备命令长手册，同时 `docs/DEVICE_TESTING.md` 已有完整现行正文。PIE 把可在获准操作后再读的细节保留在深层文档，root 保留不能错过的设备禁令与强制读取条件，核对所有原有安全含义仍可发现。
- **不能修改的场景**：root 约束真机不可自动恢复传输。即使简化会少数行，也绝不把它改成「必要时可自动恢复」。同样不能把 `0.1.x` 的局部限制误用到所有后续版本。
- **应当停止的场景**：root 和当前正式产品计划对发布权威存在未解决冲突，无法找到合法替代关系。PIE 显示冲突，不自行选较新文件或更方便的一方；可继续修改与冲突无关的文字。

## 5. 用户要求「整理这个 AGENTS」时的完整正常路径

以用户在一个已安装 PIE 的 Codex 环境里提出「整理 SeminarArc 的 AGENTS，去掉重复、保留所有真机保护规则」为例：

1. **入口识别**：现有 Codex 技能发现读取 PIE `name/description`，应把创建/编辑 `AGENTS.md` 归入仓库指令模式；读取当前技能 `SKILL.md` 及其仓库编辑合同。若不能证明实际读取，只能称应当调用，不能报告已调用。
2. **绑定真实输入**：当前用户要求 + Git 根目录 + 当前选中分支/工作树/HEAD；读取根、相关 nested/override、当前配置的 fallback、同目录被遮蔽的文件，以及直接关联的项目权威文件。不能从旧聊天、模型记忆或历史示例重建当前基线。
3. **诊断而非立刻改字**：区分真正重复、旧但仍适用、过期定位、没有权威的临时规则、深层条件阅读和真正需要根文件保留的硬保护。若问题是「根文件内容正确但实际 session 未加载」，交给入口/Delivery Assurance，不通过再写一遍相同规则修复。
4. **决定最小修改**：先尝试局部修正；只有广泛重复、严重矛盾、预算无解或项目 owner 明确请求时才整体整理。受管区和本次授权之外的文件绝不写。
5. **先产生完整候选**：同一基线 `B` → 可用的每个目标文件候选 `C` → 在真实候选基础上生成带删除线/粗体的可读修改预览；所有删除、移动和新增必须能在预览里追踪。至少保存真正有改动的完整新文件。
6. **写入与读回**：ChatGPT 没有合法写入能力时只交审阅包；Codex 只能在当前任务授权的文件范围写入，写前防止来源版本变化，写后重新读取实际文件、检查受管区字节及 Git 差异。多文件中途失败，不得宣称整套成功或清理掉用户工作。
7. **检验真实消费范围**：新 `AGENTS.md` 被当前任务写入不代表此 Codex 运行中的指令链已刷新；官方说明通常在新运行/新会话构建。若这次任务声称解决了「读取不到」，必须使用目标环境实际新鲜入口确认加载路径、遮蔽、预算和行为。PIE 不能替 Bridge/Delivery Assurance 声称这个复验 PASS。
8. **交付给用户**：简明回答「改了哪几类内容、哪几条安全规则保留、是否仍有未解决权威冲突、有没有实际验证新会话加载」。小修改不制造三份报告；完整跨文件整理才在任务结果目录保存预览、权威定位与覆盖证据。

## 6. 谁在什么时候负责

| 组件 | 真正发生的动作 | 具体交付或接收 | 不负责 |
|---|---|---|---|
| Bridge Kit | `ai-bridge init` 创建根模板；更新自己标记的受管区；保护写入容量 | 新 repo 初始文件、有效 Bridge 区块 | 压缩项目正文、决定项目专业规则 |
| 项目 owner / 已批准合同 | 决定科研、产品、权限、设备和验收的真实约束 | 项目正式文档、当前任务授权 | 每次手工提醒模型润色 |
| PIE 模式入口 | 区分「Project setting」和「仓库 AGENTS」；选择对应合同 | 正确的输入读取范围 | 凭空重建用户设置或 Git 内容 |
| PIE 仓库发现与诊断 | 找生效、遮蔽、嵌套、受管区；分辨内容问题与加载问题 | 此次真实基线及诊断结果 | 启动/恢复 Codex 或更改宿主配置 |
| PIE 权威编辑 | 按来源决定留在 root、nested、深层文档或任务；保真、去重和最小改动 | 完整候选与可读修改预览 | 修改未获授权的项目标准 |
| 当前 Codex Executor | 在获准范围内写入、读回、检查真实 Git diff | 项目仓库实际文件与结果 | 自己削弱标准制造 PASS |
| AI Skills 安装器/Maintainer | 安装/升级技能、维护技能索引受管区 | 被目标环境真实加载的技能版本 | 项目内容和 Bridge 的受管块 |
| `workflow-core`（适用时） | 判断当前复杂交付任务是否需要更新长期指令 | 当前任务明确维护义务 | 编辑 AGENTS 正文 |
| Bridge/Delivery Assurance（适用时） | 验实际加载的指令身份、必读文件和下游验收消费 | 运行时身份与有效证据 | 编写/决定 AGENTS 内容 |

这些是**职责和拟议接线**，不是八个必须新建的软件模块。PIE 内部只有「模式入口 → 真实文件发现 → 语义编辑 → 预览/交付」四个逻辑步骤，不增加守护进程、数据库或独立执行服务。

## 7. Codex 自动调用：现有事实与 0.3 必须兑现的范围

现行 `project-instructions-editor` 是独立技能；AI Skills 安装器能把 `SKILL.md` 安装到 repo 或 user scope，`--write-agents-md` 可写技能索引受管区，且 metadata `allow_implicit_invocation: true`。但是这个布尔值**只允许隐式选择，不等于模型一定调用**。安装来源、实际所选 `CODEX_HOME`、技能索引/描述和新鲜会话都必须实际核实。

当前 PIE 0.2 的 `evals/trigger_queries.json` 甚至把「Add a rule to AGENTS.md」列为近似但不应调用的任务；0.3 需要改为正例。这是真实需要修改的路由逻辑，不是另建插件的理由。

冻结两类触发：

- **直接 AGENTS 任务**：用户自然要求创建、改、整理或压缩 `AGENTS.md`，不用输入 `$project-instructions-editor`。已安装 PIE 的 Codex 应从技能名称/描述和已有技能索引直接调用。在新鲜真实会话用非特制的正例、反例及不同仓库测试；如果只靠手动 `$` 才成功，0.3 的 Codex 正常入口不能声称通过。
- **普通任务伴随长期权威变化**：项目正式入口/`workflow-core` 只有在真实触发条件出现时才要求本任务调用 PIE；不因普通代码改动而全仓重写。Delivery Assurance 如果尚未正式实现/安装，不能称这条跨组件自动路径已生效；0.3 仍须可被直接调用独立使用。

未来若要把「永远不会漏调用」提升为硬阻断，必须由真正已加载的宿主/任务生命周期机制观察到文件修改与技能执行，凭一条 `AGENTS` 自我要求或模型口头 `PIE_CALLED=YES` 均不足以证明。可在既有 Bridge/Delivery Assurance 的后续审查中评估**最小**调用保障，但不让 PIE 0.3 无授权修改全局 Host Policy、加新 Hook、后台 watcher 或新的完成状态机。普通任务看见文件未变时不制造一个 PIE 运行回合。

如果实际 normal-entry Gate 证明 Skill 发现不足以满足用户高频自动维护诉求，0.3 必须返回 Planner 修入口，不得降低验收为「手动能调用」后称 Codex 自动目标完成。

## 8. 修改判定与越权防护

每一条长期指令，PIE 同时判断**语义归属**和**行动前有效放置**。具体结论可为：根文件直接保留；根文件短触发加定位；子目录增量；深层正式文档；仅当次任务；历史资料；确认失效删除；无法决定而停止。输出保留精确文档定位，不建立第二份权威数据库。

严禁未经正式权威改变：强制/可选、安全/隐私、人工授权、实验/产品最低标准、验收门、受保护设备、数据来源、正式版本、最终结果语义、项目已接受的不应改变事项。之前明确删掉的规则，不得从旧历史擅自恢复。多源冲突时不能以「哪个更新」「哪个更严格」代替项目 owner 决策。

Bridge `<!-- ai-bridge-kit:start -->...<!-- ai-bridge-kit:end -->` 和 AI Skills `<!-- AI_SKILLS_COLLECTION_START -->...<!-- AI_SKILLS_COLLECTION_END -->` 区域均必须保留字节。对新增未知管理区，先定位真实 owner；确认前不擅自编辑。

文件内容变化不允许隐式改写同一任务的原始完成条件。当前 Executor 删掉真实验收入口、把 MUST 改成 SHOULD、降低硬件/数据要求，不能拿删改后的文件自证工作合格；任务冻结的验收和外部权威仍独立有效。被移动的规则必须在新的可读位置确实存在并被相关入口触发。

## 9. Skill 文件结构：不另建插件

保留唯一生产技能 `skills/core/codex-system/project-instructions-editor/`：

~~~text
SKILL.md                         两模式入口、共享不变量、加载对应详细合同
agents/openai.yaml               名称、自然请求触发描述及现有隐式策略
references/editor-contract.md    原 PIE 0.2 Project-setting 编辑合同
references/repository-agents-contract.md    新 repo-AGENTS 编辑合同
evals/trigger_queries.json       两模式正常触发、近似误触发、不应触发
assets/app-facing.svg            已有身份
~~~

核心是同一 `SKILL.md` + 两份 reference，没有新的长期进程。`writes_files` 应与 repo 模式能否合法写入相匹配；写入能力声明不是权限授予。实际文件编辑/比对优先使用 Codex 已有文件和 Git 工具，不急着造专属脚本；如果多文件完整一致性在真实任务中失败，应依据失败证据再评估成熟确定性工具，不能为坚持“纯文字”牺牲正确性。

ChatGPT 使用已有私人 Plugin wrapper 包装同一个源码快照；Codex 使用独立技能的真实安装/加载。各端版本必须与同一个最终源候选相符，不得以安装清单代替真实执行。

## 10. 反证与发布前证据

沿用 PIE 现有四个 Gate 家族，不再复制 Delivery Assurance 的另一套 Gate：

| Gate | 真正需要证明什么 | 正例 | 必须拒绝的错误或兼容性反例 |
|---|---|---|---|
| G1 入口与基线 | 两端调用正确模式，Codex 自然改 AGENTS 会真正读取 PIE；获取当前生效文件 | 不提 `$skill` 的真实 Codex 文件编辑，准确读取工作树和技能版本 | PIE 0.2 仍要求用户给完整 Project setting；AGENTS 不得被误判为 Project setting；非指令任务不误触发 |
| G2 组织与编辑 | 真正减少过期/重复/错误放置，同时保持查阅触发 | 从真实 SeminarArc/Asteria 的 root + 深层文档得出可读候选和完整结果 | 只缩字数、错误迁移历史阶段约束、漏掉遮蔽文件、仅输出口号 |
| G3 权限与保真 | 保留项目硬约束和受管区，不能删 Gate 换 PASS | 正确保留真机/权限/验收等不可弱化规则并正确处理合法局部覆盖 | 管理区字节变化、MUST 降级、丢真机保护、过期证据冒充有效 |
| G4 完整真实任务 | 同一最终候选从真实入口完成跨文件审阅和合法写入/回读；实际用户可审查 | 冻结真实 repo 隔离工作树、完整编辑产物，ChatGPT 私人 wrapper 与 Codex 均有正常入口证据 | 仅 fixture PASS、读了错误版本、混合不同候选、PIE 0.2 已有能力回归 |

反事实检查：删掉 PIE 编辑合同将再次由项目 Executor 临场随意删改；删掉 Bridge 初始化模板则新 Bridge 仓库不能独立初始化；删掉实际加载/消费复验，文件正确但 Codex 未读到的问题仍会被误判修好。任何组件如果移除后无真实损失，不再新增。

完整真实候选至少要在两个差异明显的仓库中验证（计划以 SeminarArc 的设备保护、Asteria 的网页/可视化入口为例）；使用冻结真实源、隔离工作树，不向消费仓库正式分支擅自推送。保留 0.2 Project setting 的端到端正例及必要回归。先运行便宜的历史回归，最后用同一候选做正常入口与独立完整产物评审，不反复换样本挑赢家。

## 10.1 与 Delivery Assurance 输入合同的明确关系

Delivery Assurance 的原需求输入把三份报告和权威摘要列为**每次受管 AGENTS 修改**所需的证据。本提案为了避免普通一行编辑也变成三份报告，采用**按消费合同区分**，而不是悄悄废除原要求：

- 普通用户直接要求编辑 AGENTS、且没有接入 Delivery Assurance 的任务：最小交付为本次真实修改预览、完整干净目标文件以及必要的权威/不变量说明。
- **明确属于 Delivery Assurance 受管任务、其当前获批合同要求三份证据的情况**：保留 `AGENTS_CHANGE_PREVIEW.md`、`AGENTS_AUTHORITY_MAP.md`、`AGENTS_COVERAGE_REPORT.md` 及其要求的准确定位/摘要。PIE 生成内容，原任务执行者保存，DA 负责消费和判定；不能以“PIE 小任务轻量”为理由跳过。
- 若后续 DA 正式设计改变了这项要求，先由其合法 owner 完成独立审查及权威变更；PIE 不能自行替 DA 下调完成条件。

这保持了普通 PIE 的低摩擦使用和 DA 的现有明确承诺，不创造两个同时有效的同一任务验收标准。

## 11. 这次 v0.2 相对 v0.1 真正修了什么

1. 明确模板**保留 Bridge**，PIE 是长期编辑主体，二者没有模板复制或版本联动迁移。
2. 解释了两个受管区域和真实 `ai-bridge init` / AI Skills 安装器消费位置，不再只有“模块负责”。
3. 给出实际 `SeminarArc` 文件对应的根文件结构和正向、错误、不变三条故事；避免用编造例子冒充现有结果。
4. 给出完整用户任务的八步真实路径，特别区分已经写入文件、当前会话仍旧读取，以及下一会话的真实消费。
5. 纠正「implicit=true 就一定自动调用」的错误暗示，识别 0.2 触发测试将 AGENTS 请求判成近似负例，并把真正正常入口验收设为前置条件。
6. 明确项目自有合同与两个 managed block 的保护，避免“整理”意外覆盖 Bridge 或 AI Skills 安装内容。
7. 把证据产物按任务规模收敛；轻量修改不强制产生三件套，复杂整理才需要读者可追溯的覆盖表。

## 12. 当前状态与下一步

这是**设计草案**，不是生产功能。现在能验证的是现有 Bridge 模板初始化源码、现有 SeminarArc 文件内容、现有 PIE 0.2 源码和官方 Codex 的发现规则；尚未证明 PIE 0.3 已被安装、自然触发、正确编辑或被新会话消费。

下一入口仅是**独立架构 Critic**，本阶段只给 `PROCEED` 或 `REVISE`。只有该阶段允许继续后 Planner 才准备完整 Plan/Goal/Kickoff 和最终执行前审查；唯一正式 `PASS` 及用户批准以前，不修改 PIE 生产源、Bridge、项目 AGENTS 或启动付费测试。

配套来源：
- [复杂架构的可信解释标准](https://github.com/YuukiAS/AI_Research_Toolkit/blob/main/COMPLEX_ARCHITECTURE_EXPLANATION_STANDARD.md)
- [复杂系统设计与交付标准](https://github.com/YuukiAS/AI_Research_Toolkit/blob/main/COMPLEX_SYSTEM_DESIGN_GUIDE.md)
- [Codex 指令发现官方规则](https://developers.openai.com/codex/agent-configuration/agents-md)
- [OpenAI 技能构建](https://developers.openai.com/plugins/build/skills)
- [Bridge Kit 模板](https://github.com/YuukiAS/GPT_Codex_AI_Bridge_Kit/blob/main/templates/repo/AGENTS_TEMPLATE.md)
- [SeminarArc 当前 AGENTS](https://github.com/YuukiAS/SeminarArc/blob/main/AGENTS.md)
- [SeminarArc 设备规范](https://github.com/YuukiAS/SeminarArc/blob/main/docs/DEVICE_TESTING.md)
- [Delivery Assurance 对 PIE 0.3 的需求输入](https://github.com/YuukiAS/AI_Research_Toolkit/blob/research/software-production-decision-20261013/docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_AGENTS_LIFECYCLE_AND_PIE_0_3_REQUIREMENTS_V0_1_20261019.md)

提案版本：`v0.2`；设计任务键：`project-instructions-editor--0.3-agents-authority-maintenance`；生产实现授权：否。
