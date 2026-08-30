# Plugin Versioning and Changelogs

本文件定义 `AI_Skills_Collection` 的长期 repository release、plugin SemVer 与 changelog 规则。

目标不是让所有 plugin 永远锁步，也不是用 alpha/beta 代替真实版本，而是让多年持续迭代后仍能回答：**整个仓库当前是什么 release、每个 plugin 自己到了哪个版本、某次真实项目反馈究竟改变了哪个 plugin。**

## 1. Repository release 与 plugin version 是两层版本

### Repository / CLI release

仓库与 `ai-skills-collection-cli` 维护一个顶层 release version。它描述一次可安装、可复现的整库发布，包括 distribution、profiles、registry、Marketplace、维护协议以及当次发布包含的 plugin 版本集合。

当前 4.x 历史存在过 lockstep plugin version。下一次长期版本模型切换统一作为：

```text
Repository release: 5.0.0
```

`5.0.0` 的含义是 **repository release/maintenance contract 的新 epoch**，不是“所有 plugin 都已经成熟”。

5.0.0 起必须有一个 repository-version single source of truth，供 CLI package、registry top-level release、README 当前 release 与 root `CHANGELOG.md` 共同消费。不要继续在多个脚本里手写同一个 repository version。

### Plugin SemVer

十个中央 Marketplace plugin 各自维护独立 SemVer，canonical current version 继续来自：

```text
scripts/codex_marketplace_config.json
plugins[].version
```

**不要把 plugin version 数字向下重置。** 现有 plugin 已经发布到 `4.4.2`；把同名 plugin 改成 `1.0.0` / `0.x` 会制造版本倒退和升级语义歧义。OpenAI 的 GitHub Marketplace sync 会持续更新同名 plugin，版本也是用户可见元数据，因此版本应保持单调。5.0.0 只重置 repository 的版本语义，不重写 plugin 历史。

因此：

- `4.4.2` 是十个中央 plugin 最后的 lockstep baseline；
- 从 repository `5.0.0` 开始，各 plugin **立即解耦**；
- 只有实际改变的 plugin 才 bump；未改变的 plugin 保持原版本；
- plugin changelog 从 `4.4.2` baseline 开始即可，不猜测式回填更早的独立历史。

## 2. 什么时候改 repository version

Repository version 只在一次正式、可安装 release 时改变；普通 commit、TODO/provenance 更新不自动发版。

### Patch：`5.0.x`

用于：

- 一个或多个 plugin 的 patch-level bug/quality fix；
- distribution/install/docs/release tooling 的兼容性修复；
- 不新增 repo-level 用户工作流，也不改变顶层安装/Marketplace contract。

### Minor：`5.x.0`

用于出现明确新的 repository-level 用户能力，例如：

- 新的中央 plugin 或正式 profile；
- 多 plugin 协同形成新的正常工作流；
- 安装/发布/maintenance 获得新的长期用户能力；
- 一个真实科研 workflow milestone 明显扩大整个 collection 的正常可用范围。

不是因为 TODO 多了、benchmark 多跑了或 schema 多了就升 minor。

### Major：`6.0.0` 及以后

只用于破坏性 repository contract，例如：

- 中央 Marketplace / 安装方式发生不兼容变化；
- 顶级 plugin 被删除、重命名或发生需要用户迁移的语义改变；
- version/distribution model 再次发生破坏性重构。

## 3. 什么时候改 plugin version

每个 plugin 独立判断。

### Patch

现有用户任务边界不变，只修可靠性或质量，例如：

- routing bug；
- validator/QA false positive 或 false negative；
- source fidelity / rendering / writing regression；
- existing workflow 的窄范围 production fix。

### Minor

普通用户获得以前没有的真实能力，例如：

- 新的正式 user-facing task / artifact mode；
- 明显扩大正常支持的任务范围；
- 新的稳定工作流入口；
- 真实项目驱动的一组改进使该 plugin 从“只能做 X”变成“现在可以稳定做 X+Y”。

### Major

只用于 plugin 自己的破坏性 contract：

- trigger / front-door 被不兼容替换；
- 正常输出格式/语义需要用户迁移；
- 关键安装依赖或公开工作流发生不兼容变化。

以下默认 **不 bump plugin version**：

- 只更新 `docs/provenance/`；
- 只整理 `docs/plugin-todos/`；
- 只更新未进入 runtime payload 的维护文档；
- synthetic benchmark / audit metadata 本身没有改变 production behavior。

shared runtime 变化时，只 bump 真正受影响的 plugin，不机械全体升版。

## 4. Capability status 是可选注释，不是第二套版本

Plugin 的主要进度依据是独立 SemVer + changelog + 真实任务 evidence。

`docs/PLUGIN_MATURITY.md` 只保留可选 capability status，用来说明“现在是否适合作为日常默认工具”，不要求每个 plugin 必须按 `alpha -> beta -> stable` 走固定梯子。

默认可以保持 `unclassified` / `baseline`。只有真实使用证据足够且对用户有帮助时，才标 `alpha` 或 `stable`。status 不参与版本比较，也不触发 version bump。

## 5. 每个 plugin 一个 changelog

长期 changelog 位于：

```text
docs/plugin-changelogs/<plugin>.md
```

十个中央 plugin 各一个文件，与 `docs/plugin-todos/` 一一对应。

plugin changelog 只记录：

- user-visible behavior change；
- routing / workflow / quality contract change；
- 新增或移除的正式 capability；
- 重要 regression / compatibility fix。

不要把 commit list、测试数量、CI run ID、generated file noise、纯 provenance 整理当作 changelog 主体。

`4.4.2` 以前的 lockstep 历史无需人工猜测式回填。每个 plugin changelog 从 `4.4.2 — legacy lockstep baseline` 开始，并链接 root `CHANGELOG.md` / Git history。

## 6. Root CHANGELOG 是 release 首页

根 `CHANGELOG.md` 是 repository release 的人类可读首页。

每个 release 至少包含：

- repository release version；
- affected plugin version delta：`old -> new`；
- unchanged plugin 列表；
- repository / CLI / distribution infrastructure 变化；
- `docs/plugin-changelogs/` 索引链接。

不要把十份 plugin changelog 复制进 root CHANGELOG。

未来如果建立 website，website 应读取 repository version、Marketplace config、plugin changelog/status 等现有 source；现在不为了未来网站新增 database/schema。

## 7. README 应直接显示当前状态

README 提供紧凑表格：

```text
Plugin | Version | Status | Main entry / purpose | Changelog
```

其中：

- Version 来自 Marketplace config；
- Status 来自 `docs/PLUGIN_MATURITY.md`，允许 `unclassified` / `baseline`；
- Changelog 指向 `docs/plugin-changelogs/<plugin>.md`；
- README 不是第二套 source of truth，必须有 regression 防漂移。

README 同时显示 repository / CLI release version，并明确：

```text
repository release != plugin version
```

## 8. 5.0.0 release 的冻结规则

下一次 Goal 完成后发布 repository `5.0.0`，因为这是长期维护、独立 plugin release tracking 与真实科研反馈循环正式落地的 repository-level major epoch。

但 plugin 不锁步到 5.0.0，也不向下重置。

Executor 必须根据本次真实 diff 决定 affected plugins，并按本文件的 patch/minor/major 规则 bump。至少应检查：

- `ai-skills-core`：独立 version/changelog/release maintenance 是否形成新的正式能力；
- `presentations`：本 Goal 是否真实改变 normal production / validator / existing-deck refinement behavior；
- `research-writing`：若本 Goal 没有改变 runtime behavior，则不得为了 5.0.0 repo release 顺手 bump。

## 9. Release workflow

每次 bounded release：

1. 从真实 diff / user-facing effect 列 affected plugins；
2. 每个 affected plugin 独立决定 patch / minor / major；
3. 更新对应 `docs/plugin-changelogs/<plugin>.md`；
4. 更新 Marketplace config 中受影响 plugin version；
5. 更新 repository version source；
6. 运行 registry/catalog/Marketplace generator；
7. 更新 root CHANGELOG release manifest 与 README 状态表；
8. 做 version consistency、payload parity、install smoke、真实 CI；
9. 只有真实 payload/behavior 与 changelog 一致才发布。

## 10. 必须有的 regression

长期至少保护：

- repository version source == CLI package == registry top-level == README current release；
- Marketplace config 中每个中央 plugin 都有合法、独立、单调 SemVer；
- 十个中央 plugin == `docs/plugin-changelogs/*.md` == `docs/plugin-todos/*.md`；
- 每个 plugin changelog latest version == Marketplace config 对应 version；
- README plugin table == Marketplace version + capability status + changelog path；
- generated plugin manifest version == source config；
- plugin versions允许彼此不同；
- maintenance changelog/TODO/provenance 不进入普通 plugin runtime payload。

## 11. 与真实科研 refinement 的关系

标准路径：

```text
real feedback
-> docs/plugin-todos/<plugin>.md
-> bounded promotion
-> implementation + replay + unrelated regression
-> affected plugin version bump
-> plugin changelog
-> repository release（仅在形成正式可安装 release 时）
```

版本提升最终必须对应可观察的 user-facing improvement。TODO 增长、更多 metadata、更多 synthetic PASS 都不是版本提升理由。
