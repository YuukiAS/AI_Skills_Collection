# Project Instructions Editor 0.3：仓库 AGENTS 权威维护架构提案

状态：`DRAFT_FOR_ARCHITECTURE_CRITIC_REVIEW`  
日期：2026-10-20  
Tracking：#108  
Planner 依据：`AI_Skills_Collection main@ba86b75cc561ebc3faf1d46b7695f45a9c20b2cc`  
角色合同：Planner/Critic 1.7；Capability Gate Policy 1.2  

## Active Design Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = standalone Skill / project-instructions-editor
design_topic_or_task_key = project-instructions-editor--0.3-agents-authority-maintenance
source_branch_or_ref = main
proposal_path_and_version = docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_3_AGENTS_ARCHITECTURE_PROPOSAL_V0_1_2026-10-20.md / v0.1
execution_branch/worktree_if_already_known = NOT_FROZEN
review_stage = ARCHITECTURE_REVIEW
```

## 1. 核心结论

PIE 0.3 应当继续以现有 `project-instructions-editor` 独立技能为唯一能力源，在保留 0.2 ChatGPT Project setting 编辑合同的基础上，新增独立的仓库指令模式。它不是新的 Bridge 功能、Delivery Assurance 子系统、工作流状态机或 AGENTS 数据库。

产品形态冻结为：

```text
同一个 standalone Skill
├── PROJECT_SETTING_MODE
│   └── 原 PIE 0.2 合同，语义不变
└── REPOSITORY_AGENTS_MODE
    └── root / nested AGENTS.md 与 AGENTS.override.md 的权威整理
```

ChatGPT 继续通过现有私人 Plugin wrapper 消费同一技能；Codex 继续通过现有独立技能安装机制消费同一技能。Plugin 是 ChatGPT 侧的安装包装，不成为新的能力真相源，也不要求把 PIE 改造成中央 Plugin。

Bridge Kit 只拥有新仓库模板、自己管理的区块、指令容量预检和实际加载身份；`workflow-core` 只判断当前任务是否必须维护 AGENTS；项目 owner 决定长期产品、科研、安全和验收语义；PIE 只负责在这些已存在的权威之间完成保真编辑、分层、去重、定位和可审阅交付。规则写得正确但运行时没有加载，属于指令消费失败，不允许靠继续堆字解决。

## 2. 用户承诺基线

本轮后续修订不得静默弱化以下要求：

1. AGENTS 太长、重复、冲突、路径失效或越积越乱时，必须有一个明确主体负责整理，不能继续依赖每个项目临时人工修文档。
2. Bridge Kit 负责模板、提醒和自己管理的运行区块，不负责决定或重写项目长期语义。
3. Codex 经常修改 AGENTS，正常的创建、更新、压缩、同步和重组任务必须能自然触发 PIE，不能要求用户每次手动提醒。
4. ChatGPT 可以保留显式调用入口；自动触发是可取能力，但不是 0.3 发布的唯一入口或用户必须依赖的前提。
5. ChatGPT 与 Codex 必须消费同一份技能合同，不能形成两个独立实现或两套语义。
6. PIE 0.2 的完整当前 Project setting 基线门、受保护缺失、语义保真、修改预览和完整干净结果必须全部保留。
7. PIE 不发明项目规则，不替项目 Planner、领域能力、Bridge、Delivery Assurance 或 Executor 决定产品、科研、权限、验收和完成标准。
8. 不新增 AGENTS registry、数据库、watcher、daemon、长期同步服务、第二状态机或新的跨仓库控制面。
9. 不能通过删掉 Gate locator、把 MUST 改成 SHOULD、移除人工授权、降低真实环境要求或改换 owner 来获得完成声明。
10. “文件中有规则”和“正常运行真实消费了规则”必须分开验收。

## 3. 当前事实与问题归因

当前正式技能版本为 `0.2`，只处理 ChatGPT Project setting。它要求用户提供完整当前 setting，并从同一基线生成可读修改预览和完整干净结果；`allow_implicit_invocation: true`，但 source description 明确排除通用 agent/system prompts。0.2 已正式发布并完成真实 ChatGPT Web 显式调用验收。

Bridge Kit 已有 `templates/repo/AGENTS_TEMPLATE.md`，并在新仓库正常入口创建简短 root scaffold；对已有仓库则只维护自己的 managed block，不自动迁移或重写项目 prose。这一边界是正确的：模板和运行区块属于 Bridge，项目 AGENTS 的语义整理不属于 Bridge。

Codex 的正式发现规则不是“只读 root AGENTS”。它按当前运行的 `CODEX_HOME` 读取全局 `AGENTS.override.md` 或 `AGENTS.md`，再从仓库根目录向当前工作目录逐层读取每一级中优先级最高的 `AGENTS.override.md`、`AGENTS.md` 或已配置 fallback；更深层文件出现在组合指令的后面，因而能够覆盖上层内容。组合内容还受 `project_doc_max_bytes` 限制。PIE 0.3 因此必须理解作用域、遮蔽、覆盖和总预算，而不能只对单个 root 文件做语言压缩。

真实失败至少分为三类：

- **内容维护失败**：重复、冲突、过期 locator、最新局部需求挤掉长期规则、root/nested 作用域放错、长 SOP 被复制进 root；由 PIE 处理。
- **权威设计失败**：项目 owner 尚未决定哪份合同有效，或两个同级权威冲突；PIE 停止并交回 owner，不自行选择。
- **消费失败**：正确文件存在，但实际 Codex session 没有加载、被 override 遮蔽、因预算截断或入口错误未消费；由 Bridge/Delivery Assurance 验证和修复，PIE 不重复写同义规则。

## 4. 五遍预检

### 4.1 产品检查

用户实际需要的不是一个 AGENTS 格式化器，而是一个可重复调用的长期指令编辑能力：知道当前真实基线、知道规则属于 root、nested、深层合同还是当前任务，能保护权限和完成语义，并给出人能审查的前后变化。成功结果是 AGENTS 更短或更整齐之外，未来任务还能找到正确 owner、在行动前读到必要边界，而且没有丢失或削弱规则。

### 4.2 现实检查

现有 PIE 0.2 已提供基线、保真、定位、受保护缺失和修改预览的核心。现有 AI Skills 安装器已能向 Codex 暴露独立技能及其 description；现有私人 wrapper 已能在 ChatGPT 使用同一技能。Bridge 已拥有模板与 managed block。无需新服务即可完成 repo 文件读取、编辑和证据输出。

当前尚未证明的是：扩展后的 description 在新鲜 Codex session 中能否自然触发；多文件 root/nested 编辑能否保持 0.2 保真；私人 wrapper 能否在 ChatGPT 通过 GitHub connector 或用户提供的准确文件包完成 repo 模式。这些必须由后续 Gate 直接验证，不能靠文档声明。

### 4.3 替代方案检查

本提案比较了不改、另建 `repository-agents-editor`、改成中央 Plugin、交给 Bridge、交给 `workflow-core` 和扩展 PIE 六条路线。只有扩展 PIE 能在不新增用户入口和第二实现的前提下复用现有编辑合同，同时保持 Bridge/工作流 owner 边界。

### 4.4 反证检查

最危险的反例是：技能只会压缩文字，却不理解 active instruction chain；Executor 用自己刚改写的规则证明自己通过；nested override 合法覆盖和恶意削弱无法区分；真实 Codex 没加载文件却被误诊为内容问题；ChatGPT 只拿到局部文件却声称完成 repo-wide 审计；合成 fixture 通过但真实仓库失败。后续 Gate 必须逐项封住这些路径。

### 4.5 执行检查

0.3 可在现有技能目录内完成，不需要新服务。先做架构审查；`PROCEED` 后由 Planner 准备同版本 Plan/Goal/Kickoff 和最终 execution-ready 审查。当前提案不授权改技能 source、Plugin wrapper、Bridge、Delivery Assurance 或任何 consumer AGENTS。

## 5. 产品边界

### 5.1 两个正式模式

`PROJECT_SETTING_MODE` 保留 0.2 全部行为：完整用户提供基线、preservation-sensitive/greenfield/explicit reset、受保护缺失、最小编辑、语义不变量、可读 Markdown 修改预览、完整干净 setting 和 `E(B)=C`。0.3 不借 repo 模式重新解释或放松这些要求。

`REPOSITORY_AGENTS_MODE` 处理明确仓库、ref/worktree 和作用域内的：

- `AGENTS.md`；
- `AGENTS.override.md`；
- 当前 Codex 配置实际启用的 fallback instruction file，仅在当前任务明确把它列为可编辑目标时；
- 这些文件直接引用、且本次编辑确实需要读取的 canonical contracts。

它支持五种任务意图：

```text
AUDIT_ONLY
BOUNDED_UPDATE
STRUCTURAL_REORGANIZATION
GREENFIELD
EXPLICIT_RESET
```

默认是 `BOUNDED_UPDATE`。只有用户明确要求，或存在跨作用域冲突、系统性复制、预算无法满足、严重 locator 漂移、遮蔽错误或作用域结构失效时，才进入 `STRUCTURAL_REORGANIZATION`。`GREENFIELD` 只适用于目标文件确实缺失且当前任务获准创建；`EXPLICIT_RESET` 必须由合法项目 owner 明确授权。

### 5.2 明确不拥有的能力

PIE 0.3 不负责：

- 决定项目产品、科研、领域、权限、发布或验收标准；
- 判断一个实现是否通过专业 Gate；
- 证明 Codex runtime 实际加载了哪些文件；
- 修改 `$CODEX_HOME`、Host Policy 或全局 AGENTS；
- 修改 Bridge、AI Skills installer 或其他 owner 的 managed/generated block；
- 创建或维护中央 AGENTS registry、持续同步服务或 stale watcher；
- 自动 commit、push、建分支、切工作树或扩大当前任务权限；
- 把任意 prompt、developer message、README 或普通文档编辑吞进本技能。

## 6. 产品身份与两端分发

### 6.1 唯一能力源继续是独立技能

保留：

```text
name = project-instructions-editor
canonical source = skills/core/codex-system/project-instructions-editor/
recommended_scope = global
candidate version = 0.3
```

不新建第二个 skill slug，不创建中央 Plugin，不迁移现有历史、TODO、wrapper 或安装身份。新增模式仍属于同一个可识别用户目标：维护长期、可执行的 Project/仓库指令表面，并保护语义、权威和作用域。

### 6.2 ChatGPT 入口

现有 PRIVATE / USER Plugin wrapper 继续作为 ChatGPT 安装包装，打包同一 canonical Skill。0.3 的正式 ChatGPT 入口要求显式调用或选择 PIE 能完成两种模式；隐式触发作为诊断和改进目标，但不把它设为唯一发布条件。

repo 模式取得当前文件的顺序为：

1. 当前对话可用且获准的 GitHub/文件 connector 读取 exact repo/ref；
2. 用户提供带 path/ref 的完整准确文件包；
3. 两者都没有时，请求缺失的准确文件，不从 Memory、旧聊天、摘要或模型知识重建。

ChatGPT 没有实际写入工具或授权时，只输出审阅包，不声称已经修改仓库。

### 6.3 Codex 入口

Codex 继续通过现有独立技能安装机制加载 PIE，`allow_implicit_invocation` 保持 `true`。技能 description 必须明确、窄范围地覆盖“创建、更新、审计、压缩、同步、重组或重置 ChatGPT Project setting 或 repository AGENTS files”，同时继续排除普通 prompt、README、通用写作和全局 Custom Instructions。

正式 Gate 必须证明：在安装 exact final candidate 的新鲜 Codex session 中，用户自然要求修改 AGENTS 而不写 `$project-instructions-editor`，Codex 会读取并执行该技能。若失败，优先修技能 metadata、安装/加载身份或 AI Skills 现有 routing，不先向 Bridge managed block 追加同义规则。

## 7. 职责矩阵

| 事项 | 语义 owner | 实际 actor | PIE 的边界 |
|---|---|---|---|
| 项目长期产品/科研/安全规则 | 项目 owner / 已批准合同 | Planner 或获准项目维护任务 | 只投影，不发明 |
| 判断本任务是否需要维护 AGENTS | 当前用户、项目合同；Delivery Assurance 场景由 `workflow-core` resolution | 当前任务入口 | PIE 也允许被用户直接调用，不依赖 DA 才能使用 |
| 编辑、压缩、分层、同步 AGENTS | 项目 owner 拥有语义；PIE 拥有编辑合同 | ChatGPT 或当前 Codex Executor | 不改变专业标准和权限 |
| Bridge managed block、模板和加载身份 | Bridge Kit | Bridge / Bridge maintainer | byte-preserve；内容错误交回 Bridge |
| AI Skills managed block 与 skill install | AI_Skills_Collection installer / Maintainer | AI Skills Maintainer | byte-preserve；不手改生成区 |
| 实际 session 消费证明 | Bridge / Delivery Assurance | 正常入口运行与证据采集 | PIE 只能报告内容问题或消费问题分类 |
| Git commit/push/release | 当前 repo 和任务授权 owner | Executor / Maintainer | PIE 不授予权限 |

## 8. repo 模式的当前基线

### 8.1 目标绑定

在任何分析或修改前，先绑定：

```text
repository identity
target branch/ref or exact worktree + HEAD
requested edit scope
target path set or repo-wide audit scope
current instruction discovery configuration when available
```

ChatGPT connector 读取必须使用明确 ref；Codex 使用当前实际 Git root/worktree/HEAD。目录名、旧任务路径和聊天摘要不能代替身份。

### 8.2 指令发现

对于一个或多个目标路径，按 Codex 当前正式规则构造项目指令链：

1. 从 Git root 到目标工作目录逐层检查；
2. 每个目录只选择一个 active file，顺序为 `AGENTS.override.md`、`AGENTS.md`、当前配置的 fallback；
3. 记录同目录被 active override 遮蔽的文件；
4. root 到更深目录按顺序组合，明确哪个较深规则可能覆盖哪个上层规则；
5. 计算或读取实际 `project_doc_max_bytes`；不知道时不得声称完整链能够被加载；
6. repo-wide 审计必须建立所有 instruction file 的 scope tree，而不是拿某一个 current working directory 的链冒充全仓覆盖。

全局 `$CODEX_HOME/AGENTS*.md` 只可作为可选、只读运行背景，不属于项目语义基线，也不由 repo 模式修改。

### 8.3 完整 repo baseline

基线 `B_repo` 至少包括：

- 作用域内所有 active root/nested instruction files 的 exact path、ref 和全文；
- 被 override/fallback precedence 遮蔽但可能造成维护误判的同目录文件；
- 已知 managed/generated regions 及 owner；
- 本次修改所依赖的 canonical contracts；
- 与本次规则相关的已接受、删除、拒绝和显式 supersession 记录；
- 已知总预算与当前组合字节数；
- 当前任务获准修改的文件集合。

缺少其中会改变结论的部分时，只能进行范围受限的审计或返回缺口，不能声称 repo-wide clean final。

## 9. 权威与放置规则

### 9.1 每条长期规则先判断两件事

- **语义 owner**：谁有权决定规则内容和当前版本；
- **执行放置**：未来 agent 在行动前应在哪里直接看到规则或看到强制 lookup trigger。

允许的放置结论为：

```text
ROOT_DIRECT
ROOT_TRIGGER_PLUS_LOCATOR
NESTED_DIRECT
CANONICAL_ONLY
TASK_ONLY
HISTORICAL_ONLY
REMOVE_STALE
UNRESOLVED_CONFLICT
```

这些结论只存在于当前审计/编辑证据，不形成中央 registry。

### 9.2 root、nested 与深层文档

root AGENTS 保存：

- 全仓任务入口和必须先读的稳定 locator；
- 项目、领域、Bridge、用户和外部服务的 authority 边界；
- 在 lookup 前就必须生效的权限、安全、隐私、分发和完成声明边界；
- 项目特有验收入口、最终消费对象和长期运行 owner 的短 trigger；
- 全仓 durable should-not-change。

nested AGENTS 只保存对应子树真正不同或新增的规则。相同规则应提升到最近共同 ancestor，不在多个文件复制。较深文件可以合法替换局部命令、测试入口或目录约定，但不得未经权威批准削弱以下受保护最低标准：

- 权限与人工授权；
- 安全、隐私和分发；
- 证据强度和完成声明；
- 领域最低标准和 required Gate；
- should-not-change；
- 恢复和失败诚实性。

对这些最低标准的例外必须由合法 owner 显式定义适用范围和替代安全路径；“nested 文件后加载”本身不是授权。

深层 canonical docs 保存完整 SOP、Gate rubric、fixture 清单、历史事故、波动环境清单、当前任务状态和长测试矩阵。AGENTS 只保留行动前必需的短规则与 locator。

### 9.3 冲突处理

权威判断顺序为：当前用户/项目 owner 的明确决定和已批准冻结合同；当前明确标为 canonical 且具有该语义 owner 身份的 repo 文档；当前 AGENTS baseline；真实实现/测试证据对事实的证明；历史记录作为辅助证据。

日期更新、文件更长、路径更靠近当前目录或 Executor 刚刚修改过，都不能单独产生语义 authority。同级来源冲突且没有明确 supersession 时，返回 `INSTRUCTION_AUTHORITY_CONFLICT`，列出冲突来源和所需 owner；PIE 不自行选择“更严格”“更新”或“更方便”的一份。

### 9.4 受保护缺失

0.2 的 protected absence 扩展到 repo 模式：当前 baseline 中不存在、且只出现在旧 candidate、旧聊天、历史报告或已被拒绝文本中的规则，默认继续缺失。只有当前用户重新采用，或本次明确同步的 canonical owner 当前确实支持时，才能加入。

## 10. managed/generated 区域

PIE 必须识别并保护至少以下已知 owner 区域：

```text
<!-- ai-bridge-kit:start --> ... <!-- ai-bridge-kit:end -->
<!-- AI_SKILLS_COLLECTION_START --> ... <!-- AI_SKILLS_COLLECTION_END -->
```

项目声明为 generated、vendor-owned 或 tool-managed 的其他成对标记同样处理。PIE 可以重组其周围的项目 prose，但不得修改 managed region 的字节、内容、顺序或 owner。managed region 本身错误、过期或超预算时，返回 `MANAGED_REGION_OWNER_REQUIRED` 并交给对应 maintainer。

`AGENTS.override.md` 不是普通重复文件。它会遮蔽同目录的 `AGENTS.md`，因此 PIE 必须在预览和 coverage 中显式显示遮蔽关系，不能同时修改两份后假装二者都会生效。

## 11. repo 模式处理流程

```text
识别模式与任务权限
→ 绑定 repo/ref/worktree/HEAD 和目标作用域
→ 构造 active instruction chain / repo-wide scope tree
→ 读取最小必要 canonical sources 与相关决定历史
→ 建立任务级 authority/placement map
→ 选择 no-op、局部编辑或结构重组
→ 在内存中形成全部 clean candidate set
→ 检查跨文件作用域、遮蔽、受保护最低标准、managed region 和预算
→ 从同一 baseline/candidate 生成可读 preview
→ ChatGPT 返回审阅包；Codex 在既有授权下写入
→ 重读实际文件并检查真实 diff
→ 输出范围匹配的 coverage evidence
```

多文件修改先形成完整 candidate set，再落盘。写入失败时停止并报告已改变的准确文件，不用 reset/clean/restore 吞掉用户工作，也不把部分成功冒充完整成功。

## 12. 输出合同

### 12.1 小型修改

输出：

1. 按文件和作用域组织的可读 Markdown 修改预览；
2. 每个被修改文件的完整干净内容；
3. 简短说明语义 owner、放置原因、保持不变的关键规则和预算变化。

预览沿用 0.2：删除使用删除线，新增使用粗体，替换同时显示；不使用 Git `+/-` diff 代替人类审阅。

### 12.2 正式结构整理或 Delivery Assurance adoption

除上述内容外，在当前任务结果目录保存：

```text
AGENTS_CHANGE_PREVIEW.md
AGENTS_AUTHORITY_MAP.md
AGENTS_COVERAGE_REPORT.md
```

`AGENTS_AUTHORITY_MAP.md` 至少记录 path/scope、规则摘要、canonical owner/locator、放置结论和变更类型。`AGENTS_COVERAGE_REPORT.md` 记录触发原因、读取范围、active/shadowed files、保留/迁移/删除/新增、未解决冲突、预算和实际 diff。可以记录 path/ref/content digest，但这些是任务证据，不是持久 authority registry。

### 12.3 no-op

说明为什么当前文件已满足作用域、权威、预算和可发现性要求；不制造空 diff，不重复输出完全相同的 clean files，也不为了证明调用而改措辞。

## 13. 失败分类与恢复

以下是失败原因，不是新工作流状态：

- `MISSING_REPO_BASELINE`：缺少会改变结论的当前文件/ref/scope；补齐准确输入后继续。
- `INSTRUCTION_AUTHORITY_CONFLICT`：同级权威冲突；交回项目/领域 owner 决定。
- `MANAGED_REGION_OWNER_REQUIRED`：问题位于其他 owner 的 managed/generated 区域；交给对应 maintainer。
- `INSTRUCTION_CONSUMPTION_FAILURE`：内容正确但实际 runtime 未加载/被截断/入口错；交给 Bridge 或 Delivery Assurance，不加同义规则。
- `RUNTIME_BUDGET_UNVERIFIED`：不知道真实配置或组合大小；可以完成内容编辑，但不得声称运行时完整加载。
- `OUT_OF_SCOPE_DURABLE_RULE`：当前任务想把未经 owner 冻结的临时决定写成长期规则；停止该条，不阻塞无关合法编辑。

PIE 不创建等待状态、重试循环或恢复服务。恢复点就是准确缺口、冲突来源、未写入文件和下一 owner。

## 14. 与 Delivery Assurance 的接口

Delivery Assurance requirement 文档是 0.3 的重要输入，但不直接成为 PIE runtime schema。

采用：

- 项目 owner 决定长期语义；
- `workflow-core` 可在复杂交付任务中要求调用 PIE；
- PIE 产生 task-local authority map、coverage 和 digest evidence；
- Bridge/Delivery Assurance 验证实际加载身份并判定 stale/consumption failure。

不采用到 PIE core：

- 持久 `agents_authority_set[]` registry；
- adapter 状态机；
- central stale watcher；
- 由 PIE 决定 `USER_READY`；
- 把七个 consumer 的专业字段塞进通用技能。

Delivery Assurance 后续可以消费 PIE evidence 并在自己的 adapter/证据合同中保存 digest，但该 schema、失效判定和 `USER_READY` 门属于 Delivery Assurance 设计，不是 PIE 0.3 的发布前置实现。

## 15. 生产源码结构

0.3 的最小正式修改面冻结为：

```text
skills/core/codex-system/project-instructions-editor/
├── SKILL.md
├── agents/openai.yaml
├── references/editor-contract.md
├── references/repository-agents-contract.md        # 新增
├── evals/trigger_queries.json
└── assets/app-facing.svg                           # 身份不变
```

设计要求：

- `SKILL.md` 收缩为两模式前门、共享不变量和加载指引，避免把两个完整合同堆在入口；
- `references/editor-contract.md` 继续作为 0.2 Project-setting 合同，除必要的模式定位外不改变语义；
- 新 `references/repository-agents-contract.md` 承担本提案第 8–13 节的详细合同；
- `agents/openai.yaml` 扩展 description/default prompt，保持 `allow_implicit_invocation: true`；
- frontmatter `writes_files` 由 `false` 改为 `true`，诚实声明 Codex repo 模式可能写文件；这不产生写权限，也不改变现有授权边界；
- `requires_network: false`、`executes_code: false`、`secrets_needed: []` 保持；
- 不新增 runtime script、MCP、外部 provider、数据库、ledger 或 diff service；测试可以使用 Python 标准库核对 fixture，不成为 runtime dependency。

测试和生成层预计包括现有 focused tests、standalone version baseline、trigger eval、registry/catalog/provenance 和新 repo-AGENTS fixtures。具体文件清单在 architecture `PROCEED` 后的 implementation Plan 冻结。

## 16. Capability Gate Matrix

0.3 不另造 Delivery Assurance 文档中的五个平行 Gate。它扩展并保持 PIE 已有 G1–G4 稳定 taxonomy，把新增失败归入现有能力族。

| Gate | Capability / claim | Normal entry | 必需证据 | 明确失败 | Regression boundary | Final candidate |
|---|---|---|---|---|---|---|
| `G1 — 路由、模式与当前基线` | ChatGPT/Codex 进入正确模式，并使用实际当前 setting 或 exact repo instruction baseline | ChatGPT 显式调用两类请求；Codex 新鲜 session 的自然 AGENTS 修改请求 | exact loaded skill identity；正确 mode；repo/ref/worktree/path chain；缺/局部/旧 baseline 被拒绝；near-miss 不触发 | AGENTS 请求走 Project-setting 固定回复；从 Memory 重建；普通 README/prompt 被吞入；Codex 只能靠 `$skill` 才进入 | 0.2 Project baseline gate、普通写作和其他 skill routing | 是 |
| `G2 — 核心编辑与放置` | 能从当前权威生成 root/nested/locator 的正确最小候选 | 小型更新、greenfield、结构重组、冲突输入 | 可读 preview + clean candidates；authority/placement map；active/shadowed scope 正确；合法 nested override 保留 | 只做语言压缩；复制全合同；root/nested 放错；冲突时自行选一份；preview 与 clean final 不一致 | 0.2 bounded/full/no-op、ownership/enforcement、protected absence | 是 |
| `G3 — 保真、安全与不应改变` | 不削弱权限、安全、证据、领域最低标准，不改 managed block，不用改规则换 PASS | 受控 mutation、旧删除历史、managed block、Project setting 回归 | MUST/SHOULD、owner、scope、evidence、exact strings 保真；删 Gate locator、旧 locator、root/nested conflict、managed edit 均被拒绝；0.2 regression bank 全过 | 任何未经权威的降级被接受；旧规则复活；0.2 行为回归；相邻 skill/route 受损 | 全部 0.2 fidelity、现有 wrapper、AI Skills/Bridge managed content | 是 |
| `G4 — 完整真实任务与最终产物` | 同一候选在两端完成代表性真实任务，产物可直接审查和使用 | ChatGPT wrapper 完整任务；Codex implicit normal entry；两个结构不同的真实 repo 隔离工作树 | 完整请求、baseline、sources、preview、clean files、authority map、coverage、实际 diff、独立定性审查、loaded identity | 只测字符串/fixture；不同 commit 拼证据；只看报告不看全文；真实 repo 需要用户修第一版 | 一个完整 0.2 Project-setting 任务保持；consumer product/runtime 不改 | 是 |

执行顺序固定为便宜确定性回归 → 0.2 regression bank → repo 模式 fixture/mutation → 冻结 final candidate → 真实 ChatGPT/Codex 正常入口 → 完整产物独立定性审查。不得跑到成功再挑结果，所有发布 Gate 绑定同一 candidate。

## 17. 真实仓库 Gate 与 consumer adaptation

中央实现 Gate 使用两个结构明显不同的真实仓库快照或隔离 task-owned worktree，默认：

- Asteria：检验 root map、固定入口、视觉/Browser contract locator 与长操作细节分离；
- SeminarArc：检验 Emulator-first、physical-device safety、nested/project-specific scope 和深层设备文档定位。

中央 Gate 不直接 push 两仓 canonical branch。它在冻结 ref 的隔离工作树中完成实际读取、候选编辑和 normal-entry consumption，避免把 consumer 集成混入中央 skill 实现。若这两个 ref 在执行时已不适合，替代仓库必须覆盖同样不同的失败类别，并经 execution-ready Critic 明确接受，不能临时挑最容易通过的仓库。

中央实现和 release 完成后，本 tracked item 属于 machine-consumed capability：

```text
central implementation complete
→ ADAPTING
→ 现有 ChatGPT PRIVATE / USER wrapper 更新并完成显式 repo-mode smoke
→ 至少一个用户真实使用的 Codex 环境安装 exact released Skill，并完成 fresh implicit normal-entry smoke
→ required consumers 全部 PASS/N/A 后才可 DONE
```

exact wrapper ID、Codex consumer identity 和 restart/fresh-session 边界必须在 execution package 前通过当前真实部署状态解析，不在本 Proposal 中猜测。其他仅“可能安装”的机器不自动进入 required set。

## 18. 版本与发布

当前设计候选：

```text
Affected standalone skill:
- project-instructions-editor: 0.2 -> 0.3 candidate

Affected central plugins:
- all: NO_BUMP

Repository bump decision during design/implementation:
- NONE
```

正式 repository release 类型必须在 release closure 时比较当时真实 `release` baseline，并按 `PLUGIN_VERSIONING_AND_CHANGELOGS.md` 决定；本提案不预判 PATCH/MINOR。ChatGPT wrapper 的包装版本在 adaptation 阶段单独推进，不成为 canonical Skill version。

README 因能力描述和版本变化预计需要更新；implementation 时必须按仓库 AGENTS 真实调用 Clear Writing 检查读者可见区域。该调用只服务仓库 README，不进入 PIE runtime。

Issue #108 已建立并具有正确 kind/scope/area labels。实质设计开始后，维护看板应为：

```text
Status = DOING
Area = standalone-skill
Resolution commit = blank
current anchor = 本 Proposal 与对应 Critic prompt
next action = independent architecture Critic
```

当前 surface 不能修改 GitHub Project 字段，Project mutation 尚未同步；不要求用户手工拖卡片。canonical TODO 还需要补 `tracking: #108` 的 0.3 source entry，该 locator mutation 应由下一次具备合法 repo write 的 maintenance action 完成，不能继续沿用已完成的 #93/#102 代表 0.3。

## 19. 替代方案与决定

### 19.1 不做 0.3，仅继续项目专项清理

不能解决 recurring owner 和自动调用问题，每个仓库继续重复 057/058 式人工整理。拒绝。

### 19.2 新建 `repository-agents-editor` Skill

边界最清楚，但会复制 PIE 的基线、权威、最小编辑、受保护缺失、预览和保真内核；“Project instructions”和“repo project instructions”触发重叠，用户还要选择两个入口。当前差异可以由模式 reference 隔离，暂不拆分。若未来 repo 模式加入运行时 enforcement、自动同步或与 Project setting 完全不同的成功标准，再重新评估 split。

### 19.3 把 PIE 改成中央 Plugin

Plugin 是安装包装；核心工作仍由 Skill 完成。现有私人 wrapper 已提供 ChatGPT 包装，Codex 已有独立技能安装路径。新增中央 Plugin 会制造新的版本、Marketplace/profile 和触发身份，没有解决内容维护的新增失败。拒绝。

### 19.4 交给 Bridge Kit

Bridge 应保护模板、managed block、入口身份和预算，不应判断项目科研/产品语义或迁移已有 prose。否则 Bridge 会变成跨仓库政策迁移器。拒绝。

### 19.5 交给 `workflow-core` / Delivery Assurance

它们可以决定何时必须维护、是否消费正确证据，但不应承担具体文本编辑和权威投影。拒绝。

### 19.6 采用：同一 Skill、双模式、分离 reference

复用成熟内核，只有一个用户入口；ChatGPT 和 Codex 使用同一 source；运行 owner 不被改写；新增复杂度与真实失败直接对应。采用。

## 20. 风险与恢复

- **触发过宽**：description 误吞普通 prompt/README。通过 G1 near-miss 与更窄 metadata 修复，不向正文堆排除词。
- **触发过弱**：Codex 仍不自动调用。检查安装 identity、skill index 和 description；若能力本身已正确但 runtime 未发现，归类 distribution/consumption，不改 Bridge 语义。
- **0.2 回归**：SKILL 前门重构导致 Project setting 行为漂移。保持现有 reference、冻结 exact replies，G2/G3 全量回归；必要时减少重构而非重写合同。
- **权威选择越权**：停止并返回冲突，不根据日期或“更严格”猜。
- **误删安全规则**：protected minima、mutation controls、完整 authority map 和独立 G4 审查共同拦截。
- **证据过重**：小编辑只需 preview + clean final；正式结构整理才生成三份 evidence，不给每次改一行制造审计包。
- **多文件部分写入**：预先形成 candidate set，写后重读；失败只回退当前任务明确拥有的修改，不 reset 用户工作。
- **消费与内容混淆**：正确内容未加载时明确交回 Bridge/Delivery Assurance，不继续同义改写。

## 21. 正常使用六问

1. **怎样开始**：ChatGPT 显式调用 PIE 并给完整 Project setting，或指定 repo/ref 并允许 connector 读取；Codex 中用户自然要求创建或修改 AGENTS，已安装技能自动触发。
2. **正常发生什么**：技能识别模式，取得准确基线，读取最小必要权威，形成最小候选和可读预览；ChatGPT 返回审阅包，Codex 在原任务授权内写文件并验证 diff。
3. **默认与配置**：默认局部编辑、root map + nested delta、managed block 不动；目标作用域、语言、预算和是否结构重组可以由当前任务指定。
4. **危险动作谁拦**：系统/用户/目标 repo/Bridge 的既有权限和 Git 合同继续拦截；PIE 不授权 branch、push、release、Host、全局 AGENTS 或 managed block 修改。
5. **失败怎样恢复**：缺 baseline 就补准确文件；权威冲突交项目 owner；managed block 交 maintainer；消费失败交 Bridge/Delivery Assurance；不会启动后台重试。
6. **本阶段唯一下一入口**：把本 Proposal 交给新的独立 Critic，只允许 `PROCEED / REVISE`；当前没有 Codex implementation 入口。

## 22. `PROCEED` 后才准备的执行包

只有 architecture Critic 给 `PROCEED` 后，Planner 才起草同版本：

- Implementation Plan；
- Goal；
- Kickoff；
- exact execution branch/worktree；
- source/test/generated/README/CHANGELOG allowlist；
- final candidate、真实 wrapper、Codex consumer 和 Gate 预算；
- tracking Issue/source backlink/Project pending mutation 的合法处理；
- execution-ready Critic prompt。

最终 execution-ready Critic 给唯一 `PASS` 且 `READY_FOR_CODEX=YES` 前，不修改 production source、不更新 wrapper、不改 consumer AGENTS、不运行正式真实 Gate。

## 23. 外部依据与采用决定

1. OpenAI，*Custom instructions with AGENTS.md*：Codex 按 global → root → nested 形成指令链；每目录只取一个 active file；更深文件后加载；受 `project_doc_max_bytes` 限制。采用其真实发现和验证模型。  
   https://developers.openai.com/codex/agent-configuration/agents-md
2. OpenAI，*Skills – Plugins*：Skill metadata 先被模型看到，请求匹配或显式调用后加载完整指令；Skill 可不依赖 MCP。采用同一 Skill 双端消费、metadata routing 和无服务实现。  
   https://developers.openai.com/plugins/concepts/skills
3. OpenAI，*Build skills*：每个 Skill 聚焦可识别用户目标；详细材料放 references；现有工具足够时不新增 script。采用精简 SKILL 前门与 mode-specific reference。  
   https://developers.openai.com/plugins/build/skills
4. OpenAI，*Plugin architecture*：Plugin 是可安装包装，可以只包含 Skill；Skill 是工作流层。采用“canonical Skill + ChatGPT wrapper”，不把包装提升为第二真相源。  
   https://developers.openai.com/plugins/concepts/plugins
5. OpenAI，*Harness engineering*：大而全 AGENTS 会挤占上下文、快速腐化且难验证；root 应作为 map，细节进入结构化 docs。采用 root map + canonical locator，而不把约 100 行当硬指标。  
   https://openai.com/index/harness-engineering/
6. OpenAI，*Custom Code Review rules for Codex*：规则应简短、有作用域，repo-wide 放 root，service-specific 放 nested，机械格式检查留给 CI。采用作用域放置和“规则 + safe path/locator”原则。  
   https://developers.openai.com/blog/custom-code-review-rules-for-codex
7. OpenAI Help，*Plugins in ChatGPT and Codex*：Plugin/Skill 在不同 surface 的可用性和安装可能不同。采用 required consumer adaptation，而不根据一个 surface 的安装推断另一个 surface 已加载。  
   https://help.openai.com/en/articles/20001256-plugins-in-codex

## 24. 交给 Critic 的核心问题

Critic 应重点判断：

- “一个 Skill、两个模式”是否仍然足够聚焦，还是必须拆 skill；
- canonical standalone Skill + ChatGPT wrapper + Codex standalone install 是否比中央 Plugin 更真实、更简单；
- baseline/discovery 是否完整覆盖 override、nested、fallback、shadowing 和总预算；
- nested 合法覆盖与未经授权削弱是否可实现地区分；
- PIE content maintenance 与 Bridge/Delivery Assurance consumption verification 是否真正分离；
- 0.2 合同是否得到充分保护；
- 小编辑与正式结构整理的输出是否足够而不过重；
- G1–G4 是否覆盖新增能力且没有重复 Gate；
- 两个真实仓库、两种产品 surface 和 required consumer closure 是否可执行；
- 是否仍有关键产品、权限、验收或恢复决定被留给未来 Codex 猜测。

```text
PROPOSAL_STATUS = DRAFT_FOR_ARCHITECTURE_CRITIC_REVIEW
IMPLEMENTATION_AUTHORIZED = NO
CONSUMER_AGENTS_MUTATION_AUTHORIZED = NO
READY_FOR_CODEX = NO
NEXT_HANDOFF = CRITIC
```
