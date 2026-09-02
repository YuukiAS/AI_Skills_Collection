# AGENTS.md — AI_Skills_Collection

本文件是仓库级 AI/Codex 约束。任何在本仓库工作的 Planner、Executor、Reviewer 或普通 Codex 都必须先遵守这里，再读取具体 skill / task / workflow 文档。

## 1. Source of truth

涉及真实系统或发布时，优先读取：

1. 用户当前要求与真实项目/artifact；
2. 当前任务明确绑定的 Git branch；若没有独立 workflow branch，才默认当前 `main`；
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

### 2.0 Production plugin refinement 必须使用 ai-skills-core

任何会改变正式中央 plugin production behavior 的 AI_Skills_Collection 任务，都必须同时使用：

```text
workflow-core
  -> 负责任务怎样规划、执行、review、完成

ai-skills-core
  -> 负责 AI_Skills plugin maintenance contract

target domain plugin
  -> 负责目标领域的专业判断
```

示例：

- 改 `presentations`：使用 `workflow-core` + `ai-skills-core` + `presentations`。
- 改 `writing-style`：使用 `workflow-core` + `ai-skills-core` + `writing-style`。
- 改 `statistical-modeling`：使用 `workflow-core` + `ai-skills-core` + `statistical-modeling`。

触发范围包括修改 `skills/`、plugin routing、runtime references、shared runtime、QA、generator、production scripts、Marketplace payload 或 profile exposure。`ai-skills-core` 是 maintenance companion，不是 domain expert，也不是第二套 workflow/state/schema。它负责 source authority、TODO/duplicate triage、domain ownership、generated parity、production replay、unrelated regression、version/changelog 和 release closure 是否真实执行。

`ai-skills-core` 是兼容性 slug，应保持不变；用户界面的 display name 是 `AI Skills Maintainer`。不要为了改名制造安装、profile、Marketplace、历史引用和兼容性迁移，除非有强证据证明 slug migration 必须发生。

不要把 `allow_implicit_invocation: false` 改成 true 来解决这个问题。正确入口是：AI_Skills 的 `AGENTS.md`、Planner 和 Executor 在识别为中央 production plugin refinement 时显式要求使用 `ai-skills-core`，同时继续使用真正的 target domain plugin。

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

如果一个 bounded plugin refinement 已经实际改变 production user-facing behavior / quality / workflow，并且 implementation 完成、原 failure replay PASS、unrelated regression PASS、准备交付/release，则 affected plugin version 必须在同一 refinement task 中 **exactly once** bump。不得以“先放 Unreleased，以后再 bump”跳过版本更新。

如果只是 baseline replay 证明当前 plugin 已经够用、TODO/provenance/docs-only、tests-only，或没有 runtime behavior change，则 `NO_BUMP` 是正确结果。

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

### 8.1 多插件并行：一个 workflow 一个 branch

AI_Skills_Collection 同时返修多个独立 plugin 是正常情况，不应因为其中一个 task 正在等待 CI/GPT Reviewer 就让整个仓库串行停住。

当存在多个相互独立的 Reviewed Handoff workflow 时，默认使用：

```text
reviewed/<task_key>
```

作为该 workflow 的独立 branch。该 branch 在任务被明确集成回 `main` 前，是本 task 的 Executor、CI、Scheduled GPT review source of truth。

规则：

- 不同 plugin /明显独立 source area 的 task 可以并行推进；一个 branch 的 `WAITING_FOR_CI`、`READY_FOR_GPT_REVIEW`、`NEEDS_GPT_PLANNER`、visual-evidence wait 或用户输入等待，不得让另一个独立 branch 低频空等。
- 同一 plugin、同一 shared runtime/schema/generator 或存在直接依赖的 task 不自动并行；先由 Planner/用户判断是否独立。
- Scheduled GPT automation 必须显式绑定 task + branch，不得静默回落到 `main` 或改另一个 task branch。
- 不因为 task branch 已隔离就自动 merge。最终回 `main` 前仍需检查当前 main、branch diff、CI/review 和 integration conflict。
- merge conflict 是 integration decision，不等于 task 本身失败；优先询问 Planner/用户。
- 当前 generic watcher 若不能绑定单个 task，就不得在含多个 Executor-owned task 的 checkout 中冒险自动选择；使用 task-bound goal，或等待 Bridge Kit 的 first-class task-scoped watcher/branch helper。不得假装现有 watcher 已经支持自动多 branch 并发。

当前首批明确 branch：

```text
reviewed/044_writing_style_deep_research_chinese_replay
reviewed/045_presentations_real_use_regression_hardening
```

### 8.2 不得为了结束 goal 随意 BLOCK

`BLOCKED` 是不可恢复的异常终态，不是“这次 Codex 暂时不能继续”的快捷出口。

优先级：

1. 普通可逆实现细节 -> Executor 自行处理；
2. frozen Plan 的实质歧义 -> `NEEDS_GPT_PLANNER`；
3. 只差一个用户答案的运行问题（路径、artifact identity、credential/authorization、branch/integration choice 等）-> 当前 goal 支持 `request_user_input` 时直接询问并保持合法 workflow state；
4. 无交互通道但问题可由用户决定 -> 走 human-decision route，不伪造不可恢复失败；
5. 只有 waiting、Planner re-entry、用户输入、Host Policy 已授权操作和 bounded recovery 都无法解决，并且有真实证据时，才允许 `BLOCKED`。

每个 `BLOCKED` 必须说明：实际失败、观测证据、检查过哪些恢复路径、为什么都不能工作，以及恢复方式（若存在）。approval prompt、missing-but-locatable artifact、可回答的 branch/path 问题、普通 merge conflict 本身都不是 BLOCKED 理由。

### 8.2.1 私有 artifact、credential 与重复授权边界

生产回放和 artifact review 必须区分“普通可逆执行细节”与“真正需要用户授权的外部动作”。不要为了谨慎把所有 credential 相关步骤都反复问用户，也不要因为已经有某一种授权就擅自扩大到另一种传输路径。

**Executor 默认自行处理，不需要用户重复批准：**

- clone/fetch public repository；
- 在 task-owned isolated/shadow home、cache、worktree 中写临时文件；
- user-space 安装任务所需的公开工具；
- 检查 GitHub repository secret 的名称是否 `PRESENT/MISSING`，但不得读取 secret value；
- 使用 repository 中公开的 age recipient 做本地加密；
- 通过已经配置并且已经被本 task 明确授权的 GitHub Actions/Text Review 路径消费 repository secrets；
- deterministic local checks、生成 encrypted payload/manifest、等待 CI/Planner/Reviewer；
- 删除 task-local 可恢复临时文件和隔离 cache。

**以下动作必须有用户明确授权，不能从“以前做过类似事情”自动推导：**

- 把尚未公开的用户文档、研究报告、专有数据、临床/患者材料或其他 private artifact 发送到新的外部 endpoint/provider；
- 将 `auth.json`、token-bearing config、credential file 或等价认证材料复制到新的运行环境，即使目标是 task-local isolated home；
- 使用新的账户、credential、第三方服务或扩大 credential scope；
- 修改 live global plugin installation/cache、真实账户状态或其他 session 正在使用的共享外部状态；
- destructive Git/远端删除、不可逆外部写入，或显著扩大原批准的数据范围/用途。

**同一授权不得重复询问。** 用户一旦明确批准了“具体 artifact / 数据类别 + 具体 provider/endpoint + 具体 purpose + credential 使用方式”，Executor 必须在 task-local non-secret evidence 中记录一个简短 authorization receipt，并在同一 task、同一范围内直接继续；不得在每次 replay、retry、Text Review 或 fresh session 时重新问。只有 artifact/data scope、provider/endpoint、purpose、credential scope 或 live-global mutation 边界发生实质变化时，才允许再次请求授权。

不同传输路径不是自动等价授权。例如，用户批准 `age -> GitHub Actions -> OpenAI Text Review`，并不自动等于批准“复制本地 Codex `auth.json` 到 isolated home 并通过 Codex session 发送同一 private artifact”。后者第一次仍需单独授权；一旦用户为该 bounded task 授权，就应记录并在该 task 内复用，不再重复询问。

任何情况下都不得打印、commit、push、回显或要求用户粘贴 secret value。若正式路径使用 GitHub repository secrets，本地 shell 中对应环境变量 `unset` 不是 blocker。task 完成后应删除 task-local credential 副本和不再需要的 private plaintext 临时副本，但保留不含秘密的授权范围、artifact hash、provider/purpose 和删除结果作为 evidence。

### 8.2.2 已停止 task 的 artifact 只能作为显式冻结的只读回归输入

一个旧 Reviewed Handoff task 被停止、废弃或设为只读，不等于它的真实失败 artifact 必须被遗忘。后续新 task 可以把旧 artifact 当作 `KNOWN_REGRESSION`，但只有在新 task 的 REQUEST/PLAN 明确冻结了该用途时才允许读取或 replay。

- 复用旧 artifact 不得重新开启、修改、merge 或消费旧 task 的 Reviewer budget/state；
- 旧 artifact 只能证明 regression closure，不能重新冒充 unseen holdout；
- 若新 Plan 没有明确要求该 regression replay，Executor 不得因为“以前用过”自行发送、重跑或上传旧 private artifact；
- 若新 Plan 明确要求，而 replay 又涉及新的 private external transmission / credential path，则仍按 8.2.1 的授权边界执行；
- regression 完成后 evidence 应归属新 task，不回写篡改旧 task 历史。

### 8.3 Artifact-aware review

Reviewed Handoff 必须区分：

```text
PROCESS PASS
PRODUCT / ARTIFACT PASS
```

CI、schema、protected-span、Executor summary、本地测试或 control-plane transaction PASS，只能证明对应 process gate。凡验收依赖真实 artifact 质量，Reviewer 必须读取或查看最终 artifact 本身：writing output、PDF/report、presentation render、scientific figure、frontend render 或其他真实交付物都适用。

Private/text artifact review 的底层 owner 是 `GPT_Codex_AI_Bridge_Kit` 的 Text Review 能力。046 不自行实现另一套 artifact transport/reviewer。等 Bridge Kit Text Review 落地后，AI Skills Maintainer / Reviewed Handoff 只负责消费其 evidence、locator 和 artifact identity。Text Review 未落地或 Reviewer 无法访问决定 PASS 所需 artifact 时，只能按 `WAITING_FOR_EVIDENCE / NEEDS_REVIEW` 处理；在当前 state graph 中表现为不写 PASS，并要求补 Bridge Kit Text Review evidence 或返回 Planner。不得用 Executor 摘要替代 artifact。

Planner / Reviewer 能依据 frozen requirement 自行判断的明显问题，必须自行 `REVISE` 或按真实不可恢复条件 `BLOCKED`；不得推给 `AWAIT_HUMAN_DECISION`。Human gate 默认只用于真正互斥的产品/科研选择、frozen criteria 无法决定的主观偏好、用户必须亲自授权的外部动作、显著风险/成本/隐私/许可决定，或 frozen Plan 明确要求的最终人工验收。明显违反用户明确规则、明显机器腔、明显 layout failure、明显 artifact regression，不属于 human judgment。

044 是当前回归例：用户报告完整 private `rewritten_report.md` 仍有 `provenance`、`estimand`、`scientific gap`、`resource contract`、`state of the art` 等 reader-facing 表达，违反 frozen writing requirement；Reviewer 未读取完整 artifact 却给 PASS。以后同类任务必须由 artifact-aware review 层自动挡住，不能等用户人工发现。

### 8.4 Visual review skipped 语义

`visual_review_required=true` 时，才运行真实 Visual Review，并且 evidence 必须绑定 artifact identity。`visual_review_required=false` 时，不运行昂贵模型/API review，GitHub UI/状态必须表达 `SKIPPED` / `NOT_REQUIRED`，不能让真正的 visual-review job 显示成容易误读的 PASS。

如果 GitHub Actions 需要先发现 task，可以使用 lightweight resolver job；真正的 visual-review job 必须按 resolver 输出条件执行。无待审视觉 artifact 时，resolver 可以成功退出，但真实 Visual Review job 应该 skipped。

### 8.5 Review PASS 后默认集成收口

独立 task branch 通过 required CI 和 required Reviewer PASS，且没有真实 human gate 时，默认执行：

```text
task branch
-> CI PASS
-> required Reviewer PASS
-> integration preflight
-> 合回 `main`
-> push
-> 删除 task branch
```

默认不要求 PR。只有 merge conflict、`main` 在同一 shared runtime/source area 有竞争性修改、branch protection 要求、release/migration/breaking change、真实高风险 integration，或用户明确要求 PR 时，才升级为 PR / Planner / human decision。

如果 task 本身需要最终 human acceptance，用户接受后执行同一套 integration preflight；不要让用户再手工决定普通 Git 操作。Reviewer PASS 前不得自动 merge；task branch 已隔离也不能跳过 integration preflight。

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
