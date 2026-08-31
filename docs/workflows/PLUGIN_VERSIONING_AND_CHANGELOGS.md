# Plugin Versioning and Changelogs

本文件是 `AI_Skills_Collection` 的长期版本号与 changelog **唯一规范**。任何 AI、Planner、Codex 或 maintainer 在修改版本号前必须读取本文件；不得根据改动文件数、commit 数、TODO 数量、测试数量、CI PASS 或“感觉改动很大”自行决定版本。

## 1. 两层版本，彼此独立

### Repository / CLI version

整个 `AI_Skills_Collection` 使用标准三段版本：

```text
5.0.0
5.0.1
5.1.0
6.0.0
```

它描述整个 collection 的正式、可安装 release，而不是某个 plugin 的成熟度。

Repository 5.0.0 起，`VERSION` 是 repository / CLI version 的 canonical source of truth。`setup.py`、registry top-level version、README 当前 repository release 和 root `CHANGELOG.md` 必须与它一致。

### Individual plugin version

十个中央 Marketplace plugin 各自使用简单的两段 release version：

```text
0.1 -> 0.2 -> 0.3 -> ... -> 1.0 -> 1.1 -> ...
```

canonical current plugin version 只来自：

```text
scripts/codex_marketplace_config.json
plugins[].version
```

Repository `5.0.0` 是 independent plugin history 的新起点。每个中央 plugin 从 `0.1` 开始独立记录；此前 `4.x` 是 legacy lockstep release metadata，历史继续保存在 root `CHANGELOG.md` / Git history，不把它伪装成独立 plugin 版本史。

Plugin version 不是严格三段 SemVer，也不等于 alpha/beta/stable。不要使用 `0.1.0`、`0.1.1`、`0.2.0` 这类三段 plugin version。

If an external Codex Marketplace validator actually rejects the two-part `0.1` format, stop publication and report the exact external error to the user. Do not silently change the policy to `0.1.0`.

## 2. Repository version 什么时候改变

Repository version **只在形成一次正式、可安装、经过验证的 release 时改变**。

普通 commit、TODO 更新、provenance、review note、未发布实验、synthetic benchmark 本身都不改变 repository version；这些先进入 `CHANGELOG.md -> Unreleased`。

### Patch：`5.0.x -> 5.0.(x+1)`

这是长期最常见的 release。

只要整个 collection 的顶层产品/安装 contract 没有出现新的系统级能力，只是在现有体系内变得更好，就升第三位。

典型情况：

- 一个或多个 plugin 发布新的兼容 improvement；
- Presentation / Reporting 从真实科研任务吸收一批通用改进；
- routing / validator / rendering / QA / source-fidelity bug fix；
- profile、install、release tooling 的兼容修复；
- 多个 plugin 同时升级，但用户仍然使用同一套 collection 工作流。

例如：

```text
Repository: 5.0.0 -> 5.0.1
presentations: 0.1 -> 0.2
research-writing: 0.1 (unchanged)
```

**单个 plugin 的正常升级，无论改动多少，默认都只触发 repository patch release。**

### Minor：`5.0.x -> 5.1.0`

只有整个 `AI_Skills_Collection` 获得了一个此前没有的 **repository-level user capability** 才升中间位。

Planner 必须能够回答：

> `5.1.0` 以后，整个 AI_Skills_Collection 能完成什么 `5.0.x` 明显不能完成的用户任务？

只有答案具体且可观察时才允许 minor bump。

典型情况：

- 新增正式中央 plugin；
- 新增重要正式 profile / user workflow；
- 多个 plugin 联动形成此前不存在的完整正常工作流；
- 新的安装 / environment / distribution 能力让 collection 支持此前不能支持的一类正常场景；
- 一个真实科研 workflow milestone 明显扩大整个 collection 的正常可用范围，而不是单一 plugin 变得更好。

以下 **不能** 单独成为 repo minor bump 理由：

- 某个 plugin 从 `0.3 -> 0.4` 或 `0.9 -> 1.0`；
- 某个 plugin 变成 alpha/stable；
- 多了 schema / tests / benchmark / TODO；
- README 或 changelog 大改；
- 内部架构重构但普通用户没有获得新的 collection-level task。

### Major：`5.x.x -> 6.0.0`

只用于破坏性 repository contract，需要现有用户迁移或重新学习系统时才升第一位。

例如：

- Marketplace / 安装方式发生不兼容变化；
- 顶级 plugin 被删除、重命名、合并或拆分并破坏旧入口；
- profile contract 发生不兼容变化；
- repository version / plugin architecture 再次发生破坏性重构。

普通能力增强不得升 major。

## 3. Plugin version 什么时候改变

Plugin version 只回答：**这个 plugin 是否形成了一次值得正式发布的用户可观察 improvement batch。**

不使用 patch/minor/major 三层判断；正常 compatible release 每次推进一个两段版本：

```text
0.1 -> 0.2 -> 0.3 -> ...
```

一个 plugin 只有同时满足下面条件才 bump：

1. 有真实 user-facing behavior / quality / workflow 改变；
2. 改动已经形成 bounded release，而不是半成品；
3. 原失败 replay 或真实任务验证成立；
4. unrelated regression / compatibility gate 通过；
5. 对应 plugin changelog 能清楚说出 before -> after。

满足以上条件并准备交付/release 时，affected plugin version 必须在同一个 refinement task 中 bump exactly once。换句话说，completed production behavior change 只有在原 failure replay PASS、unrelated regression PASS、version/changelog closure 同步完成后才能 PASS。不得以“先放 `Unreleased`，以后再 bump”为理由跳过版本更新；已完成、已验证、会改变 production 行为的 plugin improvement 不能以 unchanged plugin version 进入 PASS。

以下默认 **不 bump plugin version**：

- Baseline replay 证明当前 plugin 已经够用；
- 只更新 `docs/provenance/`；
- 只更新 `docs/plugin-todos/`；
- 只更新未进入 runtime payload 的维护文档；
- 只新增 tests / benchmark / audit metadata，但 production behavior 未改变；
- 尚未形成正式 release 的中间 commit。

多个小修可以积累在 plugin changelog 的 `Unreleased`，等形成一个值得发布的 batch 再统一 bump 一次。

## 4. Plugin 什么时候进入 1.0

Plugin version 数字不是 maturity ladder，不要求 `0.1=alpha`、`0.5=beta`。

`1.0` 只保留一个产品意义：该 plugin 已经在多个独立真实任务中证明可作为长期默认工具，用户明确认可它进入稳定使用阶段。

例如 `presentations` 只有当 statistics / medical imaging / existing-deck refinement / real render 等多个真实场景稳定，且人工修改主要是科研判断而不是基础 AI/layout 问题时，才考虑进入 `1.0`。

这必须是用户/Planner 基于真实证据的明确决定；不能由 CI、Terra 或 synthetic benchmark 自动触发。

## 5. Capability status

`docs/PLUGIN_MATURITY.md` 只保留可选 capability status，用来说明“现在是否适合作为日常默认工具”。它不要求每个 plugin 必须按 `alpha -> beta -> stable` 走固定梯子。

Status 不参与版本比较，也不触发 version bump。默认可以保持 `unclassified` / `baseline`。只有真实使用证据足够且对用户有帮助时，才标 `alpha` 或 `stable`。

## 6. 每个 plugin 一个 changelog

长期 changelog 位于：

```text
docs/plugin-changelogs/<plugin>.md
```

十个中央 plugin 各一个文件，与 `docs/plugin-todos/` 一一对应。

每个 plugin changelog 必须说明：

```text
Independent plugin versioning starts at 0.1 with AI_Skills_Collection repository 5.0.0.
Earlier 4.x values were legacy lockstep release metadata; see root CHANGELOG / Git history.
```

Plugin changelog 只记录 user-visible behavior、routing/workflow/quality contract、新增或移除的正式 capability、重要 regression / compatibility fix。不要把 commit list、测试数量、CI run ID、generated file noise、纯 provenance 整理当作 changelog 主体。

## 7. Root CHANGELOG 是 release 首页

根 `CHANGELOG.md` 是 repository release 的人类可读首页。

每个 release 至少包含：

- repository release version；
- affected plugin version delta 或 initial plugin baseline；
- unchanged plugin 列表；
- repository / CLI / distribution infrastructure 变化；
- `docs/plugin-changelogs/` 索引链接；
- 具体 affected plugin changelog 链接。

Root changelog 回答：“整个 repository 哪次正式 release 发生了什么？”

Plugin changelog 回答：“这个 plugin 自己在哪个版本改变了什么？”

不要把十份 plugin changelog 正文复制进 root CHANGELOG。

未来如果建立 website，website 应读取 repository version、Marketplace config、plugin changelog/status 等现有 source；现在不为了未来 website 新增 database/schema/API。

## 8. README release dashboard

README 提供紧凑表格：

```text
Plugin | Version | Status | Main entry / purpose | Changelog
```

其中：

- Version 来自 Marketplace config；
- Status 来自 `docs/PLUGIN_MATURITY.md`，允许 `unclassified` / `baseline` / `alpha` / `stable`；
- Changelog 指向 `docs/plugin-changelogs/<plugin>.md`；
- README 不是第二套 source of truth，必须有 regression 防漂移。

README 同时显示 repository / CLI release version，并明确 repository release 不等于 plugin version。

## 9. 5.0.0 release 冻结规则

本 Goal 完成后发布 repository `5.0.0`，因为这是长期维护、independent plugin release tracking 与真实科研反馈循环正式落地的 repository-level major epoch。

本 Goal 内十个中央 plugin 全部为 `0.1`。这不表示它们能力一样，只表示从 repository `5.0.0` 开始第一次拥有真正独立的 plugin release history。

本 Goal 中 `ai-skills-core` 与 `presentations` 的 release 相关变化写进各自 `0.1 initial release`。从本 Goal 之后的下一批真实 feedback 开始，才使用 `0.1 -> 0.2 -> 0.3`。

## 10. 必须有的 regression

长期至少保护：

- repository `VERSION` == setup package version == registry top-level == README current release；
- Marketplace config 中每个中央 plugin 都有合法两段 plugin release version；
- 十个中央 plugin == `docs/plugin-changelogs/*.md` == `docs/plugin-todos/*.md`；
- 每个 plugin changelog latest released version == Marketplace config 对应 version；
- README plugin table == Marketplace version + capability status + changelog path；
- generated plugin manifest version == source config；
- plugin versions 允许彼此不同，且不要求三段 SemVer；
- maintenance changelog/TODO/provenance 不进入普通 plugin runtime payload。

## 11. Release plan/result format

Every release plan/result must state:

```text
Repository bump decision: NONE | PATCH | MINOR | MAJOR
Reason: ...
Affected plugins:
- <plugin>: NO_BUMP | <old> -> <new>
  Reason: ...
```

If the bump cannot be justified exactly under this policy, choose `NO_BUMP` and return to Planner/user.

## 12. 与真实科研 refinement 的关系

标准路径：

```text
real feedback
-> docs/plugin-todos/<plugin>.md
-> Planner triage
-> bounded promotion
-> implementation + replay + unrelated regression
-> affected plugin version bump
-> plugin changelog
-> repository release（仅在形成正式可安装 release 时）
```

版本提升最终必须对应可观察的 user-facing improvement。TODO 增长、更多 metadata、更多 synthetic PASS 都不是版本提升理由。
