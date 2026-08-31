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

## 1.1 README 永远写给人看

根 `README.md` 是给用户和未来维护者看的，不是内部流程日志。

修改 README 时必须：

- 默认用自然中文解释“这是做什么、什么时候用、文件放哪里、下一步怎么办”；
- 先说人能直接理解的结论，再给命令、路径和内部文档；
- 不把 `provenance`、`promotion`、`bounded batch`、`source of truth`、状态机名、内部 reviewer 字段等词直接堆给普通读者；确实需要时先用中文解释；
- 不写 audit/CI/commit/run 的流水账，除非这些本身就是用户要查的内容；
- 历史实现细节优先放 CHANGELOG 或内部 docs，不让 README 越写越像维护日志。

如果一次 README 修改技术上正确但普通用户读不明白，视为需要继续改。

## 2. 真实任务驱动长期改进

长期 refinement 必须读取：

```text
TODO.md
docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md
docs/plugin-todos/<target-plugin>.md
```

根 `TODO.md` 只是统一导航页，不能成为第二份详细待办；具体 plugin 问题只维护在 `docs/plugin-todos/<target-plugin>.md`。

不要因为一个 synthetic task PASS 自动继续创造下一轮 synthetic recovery。

### 2.1 用户说“记录 repo 并保存到合适的地方”时先判断归属

不要机械地把所有问题都写进当前项目 repo，也不要机械地把所有问题都写进 AI_Skills_Collection。

先问：

> 这是项目本身的问题，还是正在使用的 AI_Skills plugin 做得不好？

**项目本身的问题**继续写当前项目 repo。例如研究方向、模型、数据、实验、业务逻辑、项目代码 bug、项目自己的长期 TODO。

**plugin 使用过程中暴露的问题**直接写回 AI_Skills_Collection 对应 plugin TODO。例如：

- `presentations` 生成/返修的 PPT 箭头穿字、图太小、已接受页面被改坏、现有 deck 被错误重做；
- `research-writing` 把导师报告写成运行日志；
- `statistical-modeling` 的通用分析流程或检查行为出现错误；
- `medical-imaging` 的通用影像处理工作流出现可复现问题。

这类问题不要为了“留证据”再在项目 repo 维护第二份 plugin TODO。项目 repo 只保存项目自己的事情。

如果分不清，一个实用判断是：

> 换成另一个真实项目，plugin 仍然可能犯同样的错吗？

如果大概率会，优先按 plugin 问题处理。

### 2.2 真实项目 thread 可以直接写中央 plugin TODO，但只能先写事实

当真实项目 thread 发现 plugin 问题，并且用户要求“记录 repo”“保存到合适的地方”或明确要求沉淀经验时，thread 应：

1. 读取 AI_Skills_Collection 当前 `main`；
2. 读取根 `TODO.md`；
3. 读取 `docs/plugin-todos/<target-plugin>.md`；
4. 先检查是否已有明显相同的问题；
5. 如果没有可直接合并的条目，就新增一个 `status: NEW` 的真实使用反馈。

项目 thread 写 `NEW` 时只需要：

```text
### <简短的问题标题>
status: NEW
source: <真实项目 / 当前任务>
evidence: <实际输出的路径、链接、commit 或 render>
problem: <用户实际看到的问题>
project-specific context: <哪些细节只属于当前项目，不应变成通用规则>
```

此时不要要求项目 thread 自己填写 `target layer`、`candidate action`、`promotion gate`，也不要直接把“P10 箭头穿字”改写成“所有科研 PPT 必须怎样”的永久规则。

**AI_Skills Planner / maintainer 负责后续提炼。**

Planner 在处理 `NEW` 条目前必须比较：

1. 当前 plugin TODO 是否已有同一问题；
2. active skill/reference/QA/runtime 是否已经有对应规则；
3. 其他真实项目是否出现过同类失败；
4. 当前反馈中哪些只是项目内容。

然后只允许以下处理之一：

- 已有 active rule，但真实输出仍失败：视为 production regression，补充真实证据并检查实际 consumer/runtime；不要再造一条同义规则。
- 已有 plugin TODO：合并新的真实案例；不要新增重复 TODO。
- 只属于当前项目：标 `PROJECT_LOCAL`，不升级成通用规则；必要时从活跃区清理。
- 新的、可能跨项目复用的问题：由 Planner 整理成 `CANDIDATE_GENERIC`。
- 已满足 promotion gate：由 Planner 标 `PROMOTE_NOW`，之后才允许进入 bounded implementation。
- 已解决、重复、错误方向：标 `SUPERSEDED` / `REJECTED` 或从活跃区清理。

**Executor 不拥有“是否通用”的最终决定。** 项目 Executor 只负责记录真实问题；中央 TODO 的抽象、去重、状态升级由 AI_Skills Planner/maintainer 完成。

如果项目 thread 无法访问或写入 AI_Skills_Collection，不要在项目 repo 建一份影子 plugin TODO；明确报告“中央 plugin TODO 尚未记录”，等获得中央 repo 访问后再补。

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

- 根 `TODO.md`：仓库 TODO 首页，只负责指向各 plugin TODO 和说明问题怎么进入中央维护流程；不复制详细条目。
- `docs/plugin-todos/<plugin>.md`：某个 plugin 还存在哪些真实问题、以后可能要改什么。
- `docs/plugin-changelogs/<plugin>.md`：这个 plugin 已经在哪个正式版本改变了什么。
- 根 `CHANGELOG.md`：整个 repository release 首页。
- 真实项目自己的 TODO/ROADMAP/decision：只保存项目本身的研究、产品、代码和实验工作，不再维护 AI_Skills plugin 问题副本。

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
