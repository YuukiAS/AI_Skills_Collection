# Plugin Versioning and Changelogs

本文件定义 `AI_Skills_Collection` 的长期 repository release、independent plugin release version 与 changelog 规则。

目标是让多年持续迭代后仍能回答：

- 整个仓库当前是什么可安装 release；
- 每个 plugin 自己到了哪个用户可观察 release；
- 某次真实项目反馈改变了哪个 plugin；
- capability status 是否只是辅助说明，而不是第二套版本。

## 1. 两层版本

### Repository / CLI version

Repository 和 `ai-skills-collection-cli` 保留标准三段版本：

```text
5.0.0
5.0.1
5.1.0
6.0.0
```

本次长期维护基础 release 是：

```text
Repository / CLI: 5.0.0
```

`5.0.0` 是新的长期维护 epoch：

- real-world feedback driven refinement；
- 每个中央 plugin 有独立 TODO；
- 每个中央 plugin 有独立 changelog；
- 每个中央 plugin 有独立 release version；
- Reviewed Handoff 是 bounded batch，不是常驻自动优化系统；
- root `CHANGELOG.md` 是 repository release 首页；
- README 直接显示 repository version、plugin version、status 和 changelog。

它不表示所有 plugin 已经 stable。

Repository version 的 canonical source 是根目录 `VERSION`。`setup.py`、registry top-level release、README 当前 release 与 root `CHANGELOG.md` 必须与它一致。

### Individual plugin version

十个中央 Marketplace plugin 从 repository `5.0.0` 开始统一建立新的 independent plugin version epoch：

```text
0.1
```

Plugin version 只使用两段数字：

```text
0.1
0.2
0.3
...
0.9
1.0
1.1
...
2.0
```

不要使用 `0.1.0`、`0.1.1`、`0.2.0` 这类三段 plugin version。

Plugin version 的含义是“这个 plugin 第几个正式、用户可观察的 release”，不是严格 SemVer。`scripts/codex_marketplace_config.json` 的 `plugins[].version` 是 plugin version 的 canonical source。

此前 `4.x` 数字属于 legacy lockstep repository/plugin release metadata。它们不是每个 plugin 的真实独立发展历史。Independent plugin history 从 repository `5.0.0` 的 `0.1` 开始；旧历史保留在 root `CHANGELOG.md` 与 Git history。

## 2. 什么时候推进 plugin version

Plugin 不随普通 commit、TODO、provenance、synthetic benchmark 或文档整理自动升版。

只有某个 plugin 形成一次可发布的 user-facing improvement batch，才推进一次版本：

```text
0.1 -> 0.2 -> 0.3
```

标准证据链：

```text
real failure
-> bounded fix
-> original replay
-> unrelated regression
-> review
-> plugin changelog/version bump
```

不区分“这是 bugfix 所以 patch”或“这是 feature 所以 minor”。只要值得成为一个正式 plugin release，就推进一个两段版本。

小修、TODO、provenance、维护记录、尚未形成正式 release 的改动继续放在：

```text
## Unreleased
```

shared runtime 变化时，只推进真正受影响并形成 release batch 的 plugin，不机械全体升版。

## 3. Plugin 什么时候到 1.0

数字不等于 maturity。不要机械规定：

```text
0.1 -> alpha
0.5 -> beta
1.0 -> stable
```

`1.0` 保留明确产品意义：普通用户已经可以把该 plugin 作为长期默认工具使用，并且经过多个独立真实任务验证。

例如 `presentations` 只有当多个真实科研 deck、existing-deck revision、statistics、medical imaging、real render 和用户实际组会使用都表现稳定，且人工返修主要是科研判断而不是基础 AI/layout 问题时，用户或 Planner 才可以决定进入 `1.0`。

不要通过 CI、Terra 或 synthetic benchmark 自动升 `1.0`。

`1.0` 之后，`1.1`、`1.2`、`1.3` 继续表示 compatible improvement releases。只有 plugin 本身出现真正需要用户迁移的破坏性变化时，才从 `1.x` 进入 `2.0`。

## 4. 什么时候改 repository version

Repository `VERSION` 只在整个仓库形成正式可安装 release 时改变。普通 commit、TODO、provenance、project feedback 或 development branch work 不改变 repository `VERSION`。

所有未发布变化先进入 root `CHANGELOG.md` 的：

```text
## Unreleased
```

### Patch：`5.0.x`

当现有 repository architecture、plugin topology、安装方式和 profile 体系没有发生重要变化，只是发布一批兼容 refinement：

- 一个或多个 plugin 的正式 improvement release；
- validator / routing / renderer / quality / install tooling 修复；
- 若干 plugin 同时做兼容升级；
- existing collection contract 变得更好，但仍是同一个 contract。

例如 `presentations 0.1 -> 0.2` 通常对应 `repository 5.0.0 -> 5.0.1`，除非同时形成了新的 repository-level capability。

### Minor：`5.x.0`

只有整个 Collection 获得明显新的 repository-level capability，才推进中间位：

- 新中央 plugin；
- 新正式 profile / user workflow；
- 多个 plugin 联动形成此前不存在的完整科研工作流；
- research communication 从单独 presentation/report 形成新的 integrated workflow；
- 新 installation / environment capability；
- 一个大的真实科研能力阶段，使整个 collection 能完成以前明显不能完成的一类任务。

判断问题是：

```text
5.1.0 后，整个 AI_Skills_Collection 能完成什么 5.0.x 明显不能完成的用户任务？
```

回答不出来就不要升中间位。

### Major：`6.0.0`

只用于破坏性 repository contract：

- Marketplace / install 方式不兼容；
- 顶级 plugin topology 大改；
- plugin 被删除或重命名；
- profile contract 需要迁移；
- repository 结构或版本制度再次发生破坏性改变。

普通能力增强不得升 major。

## 5. Capability status 是可选注释

Plugin 的主要进度线是 independent plugin version + plugin changelog + real-task evidence。

`docs/PLUGIN_MATURITY.md` 只保留可选 capability status，用来说明“现在是否适合作为日常默认工具”。它不要求每个 plugin 必须按 `alpha -> beta -> stable` 走固定梯子。

默认可以保持 `unclassified` / `baseline`。只有真实使用证据足够且对用户有帮助时，才标 `alpha` 或 `stable`。status 不参与版本比较，也不触发 version bump。

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

Plugin changelog 只记录：

- user-visible behavior change；
- routing / workflow / quality contract change；
- 新增或移除的正式 capability；
- 重要 regression / compatibility fix。

不要把 commit list、测试数量、CI run ID、generated file noise、纯 provenance 整理当作 changelog 主体。

## 7. Root CHANGELOG 是 release 首页

根 `CHANGELOG.md` 是 repository release 的人类可读首页。

每个 release 至少包含：

- repository release version；
- affected plugin version delta；
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

README 同时显示 repository / CLI release version，并明确：

```text
repository release != plugin version
```

## 9. 5.0.0 release 的冻结规则

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

## 11. 与真实科研 refinement 的关系

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
