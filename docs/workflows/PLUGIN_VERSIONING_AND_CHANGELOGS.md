# Plugin Versioning and Changelogs

本文件是 `AI_Skills_Collection` 的长期版本号与 changelog **唯一规范**。任何 AI、Planner、Codex 或 maintainer 在修改版本号前必须读取本文件；不得根据改动文件数、commit 数、TODO 数量、测试数量或“感觉改动很大”自行决定版本。

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

Repository 5.0.0 是 independent plugin history 的新起点。每个中央 plugin 从 `0.1` 开始独立记录；此前 4.x 是 legacy lockstep release metadata，历史继续保存在 root CHANGELOG / Git history，不把它伪装成独立 plugin 版本史。

Plugin version 不是严格三段 SemVer，也不等于 alpha/beta/stable。

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

以下默认 **不 bump plugin version**：

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

`1.0` 以后 compatible improvement 继续：

```text
1.0 -> 1.1 -> 1.2
```

只有 plugin 自己发生需要用户迁移的破坏性公开 contract 变化时才进入 `2.0`。

## 5. Capability status 是可选注释

`docs/PLUGIN_MATURITY.md` 只提供可选 capability status，例如：

```text
unclassified
baseline
alpha
stable
```

不要求固定走完整 ladder，不设置 beta 作为必经阶段。

Status 不参与版本比较，也不自动触发 repository/plugin version bump。

## 6. 每个 plugin 一个 changelog

长期 changelog 位于：

```text
docs/plugin-changelogs/<plugin>.md
```

十个中央 plugin 各一个文件，与 `docs/plugin-todos/` 一一对应。

每个 plugin changelog 应有：

```text
# <plugin>

## Unreleased

## 0.2
...

## 0.1
Initial independent plugin baseline in repository 5.0.0.
```

plugin changelog 记录 user-visible behavior、routing/workflow/quality contract、新正式能力和重要 compatibility fix；不要用 commit list、测试数量、CI run ID、generated noise 填正文。

## 7. Root CHANGELOG 是 repository release 首页

根 `CHANGELOG.md` 记录 repository release，并链接各 plugin changelog。

每个正式 release 至少说明：

- repository version；
- affected plugin version delta；
- unchanged plugin；
- repository / CLI / distribution 变化；
- plugin changelog 路径。

例如：

```text
## 5.0.1

Affected plugins:
- presentations: 0.1 -> 0.2

Unchanged:
- research-writing: 0.1
- bioinformatics: 0.1
```

root CHANGELOG 不复制十份 plugin changelog。

未来 website 应读取 `VERSION`、Marketplace config、plugin changelogs、plugin TODO/status 等现有 source；现在不新增 website database/schema。

## 8. README 必须显示当前版本状态

README 应直接显示：

```text
Repository / CLI: 5.x.x

Plugin | Version | Status | Main entry / purpose | Changelog
```

其中：

- Repository version 来自 `VERSION`；
- Plugin version 来自 Marketplace config；
- Status 来自 `docs/PLUGIN_MATURITY.md`；
- Changelog 指向 `docs/plugin-changelogs/<plugin>.md`。

README 不是第二套 source of truth，必须有 regression 防漂移。

## 9. AI / Planner 不得自行发明版本号

任何 version/release 任务开始前，必须按顺序读取：

1. `AGENTS.md`；
2. `VERSION`（如果已经进入 5.0.0+）；
3. 本文件；
4. `scripts/codex_marketplace_config.json`；
5. root `CHANGELOG.md`；
6. affected `docs/plugin-changelogs/<plugin>.md`；
7. affected `docs/plugin-todos/<plugin>.md`。

然后先写出：

```text
Repository bump decision: NONE | PATCH | MINOR | MAJOR
Reason: ...
Affected plugins:
- <plugin>: NO_BUMP | <old> -> <new>
Reason: ...
```

如果无法用本文件的规则明确判断，**不要 bump**，返回 Planner/用户；不得为了“版本看起来整齐”统一升级。

## 10. Release workflow

标准路径：

```text
real feedback
-> docs/plugin-todos/<plugin>.md
-> bounded promotion
-> implementation + replay + unrelated regression
-> affected plugin release decision
-> plugin changelog
-> repository release decision
-> root CHANGELOG / README
-> install smoke + CI
```

版本提升必须对应真实可观察 improvement。TODO 增长、更多 metadata、更多 synthetic PASS 都不是版本提升理由。

## 11. 必须长期保护的 regression

至少检查：

- `VERSION` == CLI package == registry top-level == README repository release；
- 每个中央 plugin version 是合法的项目两段版本格式（例如 `0.1`, `1.2`），除非外部 Codex Marketplace 明确要求其他格式；
- 十个中央 plugin == `docs/plugin-changelogs/*.md` == `docs/plugin-todos/*.md`；
- plugin changelog latest released version == Marketplace config 对应 version；
- README plugin table == Marketplace version + capability status + changelog path；
- generated plugin manifest version == source config；
- plugin versions 允许彼此不同；
- maintenance changelog/TODO/provenance 不进入普通 plugin runtime payload。

如果外部 Codex/OpenAI runtime 明确拒绝两段 plugin version，必须记录真实 external error 并返回用户决定；不得静默把规则改成三段版本。
