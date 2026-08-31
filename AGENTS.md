# AGENTS.md — AI_Skills_Collection

本文件是仓库级 AI/Codex 约束。任何在本仓库工作的 Planner、Executor、Reviewer 或普通 Codex 都必须先遵守这里，再读取具体 skill / task / workflow 文档。

## 1. Source of truth

涉及真实系统或发布时，优先读取：

1. 用户当前要求与真实项目/artifact；
2. 当前 `main`；
3. 本 `AGENTS.md`；
4. 根 `TODO.md` / `CHANGELOG.md` 作为导航入口，再进入对应 workflow / skill / plugin TODO / changelog；
5. tests / CI /真实 render；
6. 历史记录 / benchmark。

旧聊天、旧计划、旧 benchmark PASS 不能覆盖当前 repo。

## 2. 真实任务驱动长期改进

长期 refinement 必须读取：

```text
TODO.md
docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md
docs/plugin-todos/<target-plugin>.md
```

根 `TODO.md` 只是统一导航页，不能成为第二份详细待办；具体 plugin 问题只维护在 `docs/plugin-todos/<target-plugin>.md`。

真实反馈先进入项目记录，再由 AI_Skills Planner 判断是否值得进入中央 plugin TODO。TODO 不是 active rule。只有满足 promotion gate 的通用问题才进入 bounded Reviewed Handoff implementation。原真实失败要 replay，并增加 unrelated regression。

不要因为一个 synthetic task PASS 自动继续创造下一轮 synthetic recovery。

### 2.1 谁记录，谁提炼

真实项目 thread / 项目 Codex 与中央 AI_Skills Planner 的职责必须分开。

**真实项目 thread / 项目 Codex 负责记录“实际发生了什么”。**

- 如果项目采用 task/result 结构，默认在 `results/<task_key>/result.md` 中增加 `## AI_Skills feedback handoff`；已有更合适的 review / revision result 文件时可以用已有位置，但必须稳定可引用。
- 保存用户原始反馈、对应 artifact/page/component、实际 render/result 和已经接受的元素。
- `AI_Skills feedback handoff` 至少记录：候选 plugin、原始问题、项目中的证据位置、明显只属于当前项目的边界。
- 可以标出“这个问题可能和哪个 plugin 有关”，但不要求项目 thread 自己证明问题一定通用，也不得直接把项目里的具体做法写成中央 plugin 的永久规则。
- 不为此强制所有项目建立统一的新目录或 schema；优先使用项目已经存在的任务/返修记录。

**AI_Skills Planner 负责提炼“中央 plugin 应该学到什么”。**

在更新 `docs/plugin-todos/<plugin>.md` 前，Planner 必须先比较：

1. 当前 plugin TODO 是否已有同一问题；
2. active skill/reference/QA/runtime 是否已经有对应规则；
3. 其他真实项目是否出现过同类失败；
4. 当前反馈是否只是项目科学内容、模板选择或一次性页面决定。

然后只允许以下处理之一：

- 已有 active rule，但真实输出仍失败：视为 production regression，记录新的真实证据并检查 consumer/runtime；不要再造一条同义规则。
- 已有 plugin TODO：合并新的项目证据；不要新增重复 TODO。
- 只属于当前项目：保留在项目 repo，标 `PROJECT_LOCAL`，不写中央 TODO。
- 新的、可能跨项目复用的问题：由 Planner 创建/更新 `CANDIDATE_GENERIC`。
- 已满足 promotion gate：由 Planner 标 `PROMOTE_NOW`，之后才允许进入 bounded implementation。
- 已解决、重复、错误方向：标 `SUPERSEDED` / `REJECTED` 或不再保留在活跃区。

**Executor 不拥有“是否通用”的最终决定。** 项目 Executor 可以给出候选解释和证据定位，但中央 TODO 的抽象、去重、状态升级由 AI_Skills Planner/maintainer 在明确的 triage 步骤中完成。

## 3. 版本号：禁止 AI 自行发挥

任何涉及 `VERSION`、release、Marketplace/plugin `version`、README version table、root/plugin CHANGELOG 的任务，都必须先完整读取：

```text
docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
```

**不得根据改动文件数、commit 数、TODO 数、测试数量、CI PASS 或“感觉改动很大”自行决定版本号。**

### Repository / CLI

Repository 使用标准三段版本。

- `5.0.x -> 5.0.(x+1)`：现有 collection contract 内的兼容改进；这是默认 release 类型。
- `5.0.x -> 5.1.0`：只有整个 collection 获得此前没有的 repository-level user capability。必须回答“5.1.0 能做什么 5.0.x 明显不能做？”
- `5.x.x -> 6.0.0`：只有破坏性 repository contract / migration。

单个 plugin 升级、某个 plugin 进入 1.0、更多 tests/schema/TODO、内部重构，都不能单独触发 repository minor。

Repository version 只在正式、可安装 release 时变化；普通开发 commit 不 bump。

### Individual plugins

Plugin 使用独立两段 release version：

```text
0.1 -> 0.2 -> 0.3 -> ... -> 1.0 -> 1.1
```

Repository 5.0.0 起，每个中央 plugin 的 independent history 从 `0.1` 开始。Plugin 不随 repo lockstep 升级。

只有形成正式 user-facing improvement batch，且 replay/regression/review 可证明，才推进一次 plugin version。TODO/历史记录/纯测试/中间 commit 不 bump。

`1.0` 不是机械 maturity threshold；只有多个独立真实任务证明可长期默认使用，并由用户/Planner明确决定时才进入。

如果无法按版本规范明确决定：**NO BUMP，返回 Planner/用户。**

## 4. 发布前必须显式写版本决策

任何 release Plan / RESULT 必须包含：

```text
Repository bump decision: NONE | PATCH | MINOR | MAJOR
Reason: ...
Affected plugins:
- <plugin>: NO_BUMP | <old> -> <new>
  Reason: ...
```

不得为了“统一/好看”让所有 plugin 一起 bump。

## 5. TODO / Changelog 边界

- 根 `TODO.md`：仓库 TODO 首页，只负责指向各 plugin TODO 和说明问题怎么从真实项目流入；不复制详细条目。
- `docs/plugin-todos/<plugin>.md`：未来可能要改什么，由 AI_Skills Planner 负责抽象、去重和状态维护。
- `docs/plugin-changelogs/<plugin>.md`：这个 plugin 已经在哪个正式版本改变了什么。
- 根 `CHANGELOG.md`：整个 repository release 首页。
- `docs/provenance/`：详细来源/历史记录。
- 真实项目自己的 TODO/review/result：保存项目专属决定和原始用户反馈。

maintenance TODO / changelog /历史记录不应进入普通 generated plugin runtime payload。

## 6. Generated layer

以下是生成层，不手改：

```text
.agents/plugins/marketplace.json
plugins/codex/plugins/
```

先改 source，再使用现有 generator 生成并验证。

## 7. Skill / Plugin / Profile 边界

- Skill：具体任务能力。
- Plugin：用户入口/相关能力组合。
- Profile：安装组合。
- Domain：领域完整能力。

不要为了一个 TODO、一个项目或一个视觉问题新增顶级 skill/plugin。优先放回已有 routing / reasoning / rendering / QA / writing / distribution 层。

## 8. Reviewed Handoff

Planner 负责冻结 bounded Plan；Executor 只实现当前 Plan；Reviewer 独立验收。不得让 Executor 自己扩 scope、选下一阶段或宣布 Program PASS。

高成本 final holdout 必须预冻结完整 batch；失败后不能 adaptive replacement chasing。

## 9. 用户反馈优先于内部 PASS

如果用户指出真实 artifact 不好用、逻辑不对、没用上资源、不是目标模板或正常入口没有走新能力，先检查真实 artifact/production path。CI、validator、benchmark 或 reviewer 顶层 PASS 不能直接反驳用户。

## 10. Release acceptance

正式 release 前至少确认：

- source / generated parity；
- version/changelog/README 一致；
- relevant tests；
- real install/upgrade smoke；
- required GitHub CI；
- working tree clean；
- 普通用户正常入口确实获得了 changelog 声明的能力。
