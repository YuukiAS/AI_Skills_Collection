# Project Instructions Editor 0.3：仓库 AGENTS 权威维护架构 Critic Prompt

你现在担任 AI Research Stack 的全新独立 Critic，审查 Project Instructions Editor（PIE）0.3 的仓库 AGENTS 权威维护架构。

这不是 execution-ready 审查，不是实现验收，也不授权修改生产源码、Plugin wrapper、Bridge Kit、Delivery Assurance 或任何 consumer AGENTS。本轮只能给：

```text
PROCEED
或
REVISE
```

不得给 Critic 级 `PASS`，不得写 `READY_FOR_CODEX=YES`。`PROCEED` 只表示 Planner 可以继续准备完整 Plan/Goal/Kickoff 和最终 execution-ready 审查包。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = standalone Skill / project-instructions-editor
design_topic_or_task_key = project-instructions-editor--0.3-agents-authority-maintenance
source_branch_or_ref = main
proposal_path_and_version = docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_3_AGENTS_ARCHITECTURE_PROPOSAL_V0_1_2026-10-20.md / v0.1
proposal_commit = 4b9d2014478e60d5ecf04d737740e7e04229e013
review_stage = ARCHITECTURE_REVIEW
tracking_issue = YuukiAS/AI_Skills_Collection#108
```

## 一、先读取当前真实规则

首先实际读取 `YuukiAS/AI_Skills_Collection` 最新 `main`，至少包括：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/skill-todos/project-instructions-editor.md`
- `skills/core/codex-system/project-instructions-editor/SKILL.md`
- `skills/core/codex-system/project-instructions-editor/agents/openai.yaml`
- `skills/core/codex-system/project-instructions-editor/references/editor-contract.md`
- `skills/core/codex-system/project-instructions-editor/evals/trigger_queries.json`
- Issue #108 的当前正文、labels 和 lifecycle evidence

然后读取本轮 Proposal 的 exact reviewed object：

- commit：`4b9d2014478e60d5ecf04d737740e7e04229e013`
- path：`docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_3_AGENTS_ARCHITECTURE_PROPOSAL_V0_1_2026-10-20.md`

如果最新 `main` 相比 proposal commit 已发生相关 source drift，明确说明哪些变化会影响审查；不要静默把新 source 或旧 Proposal 当作同一对象。

## 二、读取相邻 owner 和需求来源

通过 GitHub 实际读取：

### Delivery Assurance 需求输入

Repository：`YuukiAS/AI_Research_Toolkit`  
Branch：`research/software-production-decision-20261013`  
Path：

`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_AGENTS_LIFECYCLE_AND_PIE_0_3_REQUIREMENTS_V0_1_20261019.md`

把它当作需求输入，不把其中建议的 `agents_authority_set[]`、五个 Gate 或 adapter schema 自动视为已批准 PIE 架构。

### Bridge Kit 边界

读取 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 最新 `main` 的：

- `AGENTS.md`
- `templates/repo/AGENTS_TEMPLATE.md`
- `templates/prompts/AGENT_RULES.md`
- 与 `ai-bridge init` 创建/更新 root AGENTS、managed block 和 instruction budget 直接相关的当前实现与测试

核实 Bridge 当前真实职责，不依赖 Planner 摘要或旧 057/058 设计材料。

### AI Skills 安装入口

读取当前 installer / managed AGENTS source，至少包括：

- `shared/templates/AGENTS.md.template`
- 当前 standalone Skill 安装、registry/catalog/provenance 和 Codex normal-entry 路径

确认 Proposal 所说“Codex 可通过现有 standalone 安装和 metadata 自然触发”是否有真实实现基础。

## 三、做针对性外部核查

只使用当前官方 OpenAI 文档，至少核对：

- Codex 对 `AGENTS.override.md`、`AGENTS.md`、fallback、root→nested、`project_doc_max_bytes` 的实际发现与优先级；
- Skill metadata、description、显式/隐式激活、references/scripts 的当前合同；
- Skill 与 Plugin 的产品边界，以及 ChatGPT/Codex 是否可以消费同一技能；
- 官方对简短、分层、作用域化 AGENTS 的当前建议。

建议入口：

- https://developers.openai.com/codex/agent-configuration/agents-md
- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/concepts/plugins
- https://openai.com/index/harness-engineering/
- https://developers.openai.com/blog/custom-code-review-rules-for-codex
- https://help.openai.com/en/articles/20001256-plugins-in-codex

记录关键事实、采用或反对理由。不要因为官方说“可以”就推断本仓库的安装、wrapper 或自动触发已经接通。

## 四、重新建立用户目标

不要先接受 Planner 的结论。你必须独立判断用户真正需要的是不是 PIE 0.3，以及正常使用结果是什么。

至少检验以下承诺是否完整、相互兼容：

1. AGENTS 太长、混乱、重复、冲突或过期时，以后有一个明确主体负责整理；
2. Bridge 只负责模板、提醒、managed block、预算和加载身份，不承担项目语义编辑；
3. Codex 修改 AGENTS 时应能自动调用该主体；
4. ChatGPT 可以显式调用，但必须与 Codex 使用同一能力源；
5. PIE 0.2 Project setting 能力不能回归；
6. 内容维护和 runtime 消费验证必须分开；
7. 不新增 registry、watcher、daemon、数据库、第二状态机或不必要 Plugin；
8. Executor 不能靠改弱规则获得 PASS。

如果 Proposal 遗漏用户承诺、误解需求或把 Delivery Assurance 的局部要求扩大成 PIE 通用产品，要求 `REVISE`。

## 五、必须独立比较的产品路线

不要只判断 Proposal 内部是否自洽。至少比较：

1. 保持 PIE 0.2，不新增通用能力；
2. 新建独立 `repository-agents-editor` Skill；
3. 扩展现有 PIE 为双模式 standalone Skill；
4. 把能力改造成中央 Plugin；
5. 由 Bridge Kit 承担；
6. 由 `workflow-core` / Delivery Assurance 承担；
7. 只做一次 057/058 式跨仓库人工清理。

判断标准是正常用户入口、触发冲突、安装和版本复杂度、重复 owner、0.2 回归风险、真实自动调用、长期维护成本和失败恢复。历史投入或用户暂时偏好不能代替架构判断；若更简单路线明显更好，应直接要求改路线。

## 六、重点审查一：一个 Skill、两个模式是否成立

Proposal 选择同一个 `project-instructions-editor`，包含：

```text
PROJECT_SETTING_MODE
REPOSITORY_AGENTS_MODE
```

你必须检查：

- 两种模式是否真的共享同一核心用户目标和语义编辑内核，而不是为了保留名称强行合并；
- mode routing 能否由精确 metadata 和最小前门实现；
- trigger 是否会吞掉普通 prompt、README、global Custom Instructions、generic system/developer prompt 或 AI_Skills maintenance；
- 是否应保留 slug/display name，或名称已实质误导；
- `SKILL.md` 精简为 router、详细合同进入 references 是否会真实保护 0.2，而不是借重构丢语义；
- `writes_files: true` 是否诚实且安全，是否会被误解为获得写权限；
- 不增加 runtime script/MCP 是否足够，还是多文件保真确有需要的成熟 deterministic helper。

如果一个 Skill 会造成不可消除的触发歧义、输入合同冲突或验收混乱，要求拆分；如果拆分只是复制已有内核和增加入口，也应明确反对。

## 七、重点审查二：standalone Skill 与 Plugin 的真实边界

Proposal 选择：

- canonical source 继续是 standalone Skill；
- ChatGPT 继续使用现有 PRIVATE / USER Plugin wrapper；
- Codex 使用现有 standalone Skill 安装；
- 不创建中央 Plugin。

你必须核实：

- 当前产品和仓库是否真实支持这两个入口；
- 现有 personal wrapper 是否只是包装，还是实际上已经成为不可替代的第二 source；
- Codex 自动调用 standalone Skill 的 normal entry 是否比安装同一 skill-only Plugin 更可靠、更简单；
- ChatGPT/Codex 的安装和更新是否会形成两套漂移身份；
- required consumer adaptation 是否足够关闭这种漂移；
- Proposal 是否错误地把“Skill 可以用”推断成“当前用户环境已经安装并会自动用”。

结论可以维持、改为 Plugin、或要求先做受控探针，但必须说明真实失败和复杂度，而不是凭术语偏好。

## 八、重点审查三：repo baseline 与 Codex 指令链

逐项检查 Proposal 是否正确处理：

- repo/ref/worktree/HEAD 身份；
- root→current directory 的 active chain；
- 每目录 `AGENTS.override.md` 对 `AGENTS.md`/fallback 的遮蔽；
- fallback filenames；
- nested scope；
- repo-wide audit 与单一路径 chain 的区别；
- global `$CODEX_HOME` 指令的只读、非项目 owner 边界；
- `project_doc_max_bytes` 和组合字节，而非单文件长度；
- absent/greenfield/reset；
- ChatGPT connector、用户文件包和 Codex workspace 三种 baseline 取得方式；
- 缺输入时是否 fail closed，又没有要求用户重复提供工具可直接读取的内容。

特别攻击以下失败：只读 root；修改被 override 遮蔽的 inactive file；只从某个 cwd 推断全仓；不知道 runtime config 却声称已完整加载；从 Memory/历史摘要重建 current baseline。

## 九、重点审查四：权威、作用域和安全单调性

检查 Proposal 的 authority/placement 模型是否能够实现，而不是抽象正确：

- project owner、canonical docs、current AGENTS baseline、runtime evidence、history 的关系；
- root、nested、deep docs、task-only、historical-only 的放置；
- 相同规则提升到共同 ancestor；
- nested 合法替换局部测试/命令，与未经授权削弱权限、安全、隐私、证据和领域最低标准的区别；
- explicit exception 的 owner、范围和 safe path；
- protected absence；
- 同级冲突不能靠日期、路径深度或“更严格”自动消解；
- current Executor/Goal 是否可能自我授予长期规则修改权；
- managed/generated regions 是否 byte-preserved；
- `AGENTS.override.md` 遮蔽是否在 preview/coverage 中可见。

若“安全单调性”只能通过关键词比较或一律禁止 nested override 实现，要求 `REVISE`。

## 十、重点审查五：与 Bridge、workflow-core、Delivery Assurance 的边界

核实以下因果链是否清楚：

```text
project owner 决定长期语义
→ workflow-core/当前任务决定是否需要维护
→ PIE 生成和应用保真候选
→ Bridge/Delivery Assurance 验证实际加载与完成门
```

重点判断：

- PIE 是否偷偷承担 adapter registry、stale watcher、`USER_READY`、运行时加载验证或专业 Gate；
- Bridge 是否仍只拥有 managed block、模板、预算和运行身份；
- Delivery Assurance 输入中的 `agents_authority_set[]` 是否被合理留在 DA，而不是未经审查进入 PIE；
- `INSTRUCTION_CONSUMPTION_FAILURE` 是否有真实下一 owner，而不是一句推卸责任；
- workflow-core 是否只是可选 trigger owner，普通用户仍能直接使用 PIE；
- Proposal 是否要求 Delivery Assurance 尚未定案的 schema 才能实现 PIE。

边界过重或有循环依赖时要求修订。

## 十一、重点审查六：输出和操作是否成比例

检查三档输出是否合理：

- no-op 不制造假 diff；
- 小编辑给 preview + clean files + 简要权威说明；
- 正式结构整理/DA adoption 才生成 `AGENTS_CHANGE_PREVIEW.md`、`AGENTS_AUTHORITY_MAP.md`、`AGENTS_COVERAGE_REPORT.md`。

进一步检查：

- preview 是否与实际 clean candidate 同源；
- 多文件 candidate set 和实际写入后重读是否能防部分错配；
- authority map 是 task evidence 而非新 registry；
- path/ref/digest 是否只是证据，不被误当语义正确；
- ChatGPT 无写权限时是否诚实只交付审阅包；
- Codex 写文件、commit、push、branch 和 release 权限是否仍由原任务控制；
- 小修改是否被过度流程化，正式重组是否又缺少充分证据。

## 十二、Capability Gate Matrix 审查

按 `PLUGIN_CAPABILITY_GATE_POLICY.md` 审查 Proposal 保留并扩展现有 G1–G4，而不是采用五个平行新 Gate 的决定。

逐 Gate 判断：

- `G1` 是否同时覆盖两端 routing、mode、exact baseline、near-miss 和 Codex implicit normal entry；是否过宽而应拆分；
- `G2` 是否真正验证 root/nested/locator、bounded/full/no-op、authority conflict 和 preview/clean consistency；
- `G3` 是否覆盖 managed block、MUST→SHOULD、owner、Gate locator、protected absence、0.2 全回归和 should-not-change；
- `G4` 是否让独立 Reviewer 直接看到完整请求、baseline、source、preview、clean files、authority map、coverage、实际 diff 和 loaded identity；
- 所有 Gate 是否由同一个 final candidate 直接通过；
- deterministic fixture、mutation、真实 ChatGPT wrapper、fresh Codex session 和两个真实 repo 是否按成本顺序安排；
- 是否存在 test-specific hardcode、synthetic-only PASS、不同 commit 拼证据、只看报告不看全文或无限追加样本；
- 两个真实 repo 是否证明不同失败类型，而不是为数量而数量；
- central Gate 使用隔离工作树、不直接 push consumer 是否足够；
- ChatGPT 显式调用作为 required、implicit 作为诊断是否符合用户需求；
- Codex implicit invocation 是否有足够强的 final normal-entry Gate。

Gate 过重时要求合并，过简时补真实能力，但不要按固定数量移动终点。

## 十三、版本、发布和维护看板

核对：

- standalone Skill `0.2 -> 0.3 candidate` 是否成立；
- design/implementation 阶段 repository bump `NONE` 是否正确；
- formal release 类型是否正确留到真实 release baseline 决定；
- central plugins `NO_BUMP` 是否真实；
- wrapper version 是否应只在 adaptation 单独推进；
- README/Clear Writing 边界是否正确；
- Issue #108 是否是当前 tracked item，#93/#102 不应复用；
- 当前 Project 应进入 `DOING`，但无 Project mutation surface 时只能输出 exact pending mutation；
- canonical TODO 缺 `tracking: #108` 是否必须在 execution package 前修复；
- machine-consumed capability 的 ChatGPT wrapper 和至少一个真实 Codex consumer 是否应在中央 release 后进入 `ADAPTING`，required consumer set 是否需要更精确冻结。

不要因为架构 `PROCEED` 就把 Issue 或 Project 当 DONE。

## 十四、正常使用六问与失败链

独立问穿：

1. 用户怎样从 ChatGPT 和 Codex 开始；
2. 正常运行实际读取什么、修改什么、用户看到什么；
3. 哪些行为默认，哪些逐任务配置；
4. 写文件、Git、managed block、全局 AGENTS、权限和高影响动作由谁拦；
5. 缺 baseline、权威冲突、预算未知、部分写入、消费失败和自动触发失败后怎样恢复；
6. 本轮 `PROCEED` 后用户侧唯一下一入口是什么。

重点检查是否有关键决定被留给 Codex：是否拆 Skill、是否改 Plugin、如何判 authority、何时全量重组、哪些 consumer required、什么算真实 normal entry。架构阶段可以把 exact branch/worktree/hash 留给后续 Plan，但不能把产品、职责、权限、验收或恢复语义留空。

## 十五、输出要求

先给一屏自然中文，说明：

- 结论；
- 架构最重要的真实优点或问题；
- 相比 Planner Proposal 需要改变什么；
- 对用户正常使用的影响；
- 剩余 blocker；
- 用户现在是否需要动作；
- 下一入口。

然后给完整审查，区分：

- 已验证事实；
- 有证据支持的推断；
- blocker；
- 非阻塞改进；
- Planner 必须修改的准确章节与语义。

最终机器块必须严格为：

```text
DECISION = PROCEED | REVISE
TARGET_REPO = YuukiAS/AI_Skills_Collection
TARGET_PLUGIN_OR_DOMAIN = standalone Skill / project-instructions-editor
DESIGN_TOPIC_OR_TASK_KEY = project-instructions-editor--0.3-agents-authority-maintenance
SOURCE_BRANCH_OR_REF = main
PROPOSAL_PATH = docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_3_AGENTS_ARCHITECTURE_PROPOSAL_V0_1_2026-10-20.md
PROPOSAL_COMMIT = 4b9d2014478e60d5ecf04d737740e7e04229e013
REVIEW_STAGE = ARCHITECTURE_REVIEW
READY_FOR_EXECUTION_PACKAGE = YES | NO
READY_FOR_CODEX = NO
BLOCKERS = <NONE or concise list>
PROJECT_108_STATUS = DOING_PENDING_PROJECT_MUTATION | OTHER_WITH_REASON
NEXT_HANDOFF = PLANNER
```

若 `PROCEED`，只能表示架构足以进入 execution-package drafting。不要输出 Codex Goal，不要启动实现，不要修改 repo、Issue、Project 或 consumer。
