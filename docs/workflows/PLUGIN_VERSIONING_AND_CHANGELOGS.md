# Plugin Versioning and Changelogs

本文件定义 `AI_Skills_Collection` 的长期 release / plugin version / changelog 规则。目标是让仓库可以持续多年迭代，而不会因为所有 plugin 永远锁步升版本、历史散落在 root CHANGELOG、或 maturity 与 SemVer 混用而失去可追踪性。

## 1. 三个概念必须分开

### Repository / CLI release

仓库与 `ai-skills-collection-cli` 有一个 repository release version，用于表示一次可安装、可复现的整库发布。

当前 `4.4.2` 之前采用中央 plugin 锁步版本。自下一次 release 起，应建立一个单一 repository-version source of truth，供 `setup.py`、`registry.json` 生成逻辑、README 当前 release 与 root `CHANGELOG.md` 共同消费；不要继续在多个脚本里硬编码同一个字符串。

### Plugin SemVer

十个中央 Marketplace plugin 各自维护独立 SemVer。canonical current plugin version 继续使用：

```text
scripts/codex_marketplace_config.json
plugins[].version
```

`4.4.2` 是独立 plugin version tracking 的共同 baseline；以后 plugin 可以分叉，例如一次 Presentation-only 修复可以只提升 `presentations`，而 `bioinformatics` 保持原版本。

### Capability maturity

`experimental / alpha / beta / stable` 只表示真实任务成熟度，source of truth 是：

```text
docs/PLUGIN_MATURITY.md
```

maturity 不参与 SemVer 比较，也不通过把整个仓库降到 `0.x` 表达。

## 2. Plugin version bump 规则

对某个 plugin，只有其普通用户可观察行为或安装 payload 实际改变时才 bump。

- **patch**：bug fix、错误 routing/QA 修复、保真/validator 修复、现有能力的窄范围可靠性提升，没有新增明显的用户任务边界；
- **minor**：新增真实 user-facing capability、明显扩大正常支持任务范围、增加新的稳定入口或重大 workflow 能力；
- **major**：破坏既有入口/安装/trigger/profile contract，或改变语义到现有用户需要迁移。

以下默认 **不 bump plugin version**：

- 只更新 `docs/provenance/`；
- 只整理 `docs/plugin-todos/`；
- 只更新未进入 runtime payload 的维护文档；
- synthetic benchmark / audit metadata 本身没有改变 production behavior。

shared runtime 改动时，不允许机械把十个 plugin 全部升版。必须识别哪些 generated plugin payload 或正常 user behavior 真正受影响，只 bump 受影响的 plugin。

## 3. 每个 plugin 一个 changelog

长期 changelog 位于：

```text
docs/plugin-changelogs/<plugin>.md
```

十个中央 plugin 各一个文件，与 `docs/plugin-todos/` 一一对应。

plugin changelog 只记录：

- user-visible behavior change；
- routing / workflow / quality contract change；
- 新增或移除的正式 capability；
- 重要 regression / compatibility fix；
- maturity 改变时可链接 `docs/PLUGIN_MATURITY.md`，但 maturity 不是 version 本身。

不要把以下内容当作 changelog 主体：commit list、generated file noise、测试数量、CI run ID、纯 provenance 整理。

`4.4.2` 以前的锁步历史无需为十个 plugin 人工猜测式回填。每个 plugin changelog 可从 `4.4.2` 写一个 baseline note，并链接 root `CHANGELOG.md` / Git history 作为早期历史来源。

## 4. Root CHANGELOG 的职责

根 `CHANGELOG.md` 继续记录 repository release，而不是复制十份 plugin changelog。

每次 release 至少说明：

- repository release version；
- 哪些 plugin version 发生变化，以及 old -> new；
- 哪些 plugin 未变；
- repository / CLI / distribution infrastructure 变化；
- 对应 plugin changelog 链接或路径。

一次 repository release 可以只包含 1–2 个 plugin bump，其他 plugin 保持原版本。

## 5. README 应显示当前状态

README 应提供一个紧凑的中央 plugin 状态表，至少显示：

```text
Plugin | Version | Maturity | Main entry / purpose
```

其中：

- Version 来自 marketplace config；
- Maturity 来自 `docs/PLUGIN_MATURITY.md`；
- 不把 README 变成第二套版本 source of truth；
- regression 必须阻止 README 表与 canonical source 漂移。

同时显示 repository / CLI 当前 release version，并明确 repository release 与 individual plugin versions 可以不同。

## 6. Release workflow

每个准备发布的 bounded batch：

1. 先根据真实 diff / user-facing effect 列出 affected plugins；
2. 为每个 affected plugin 决定 patch / minor / major；
3. 更新对应 `docs/plugin-changelogs/<plugin>.md`；
4. 更新 `scripts/codex_marketplace_config.json` 中受影响 plugin version；
5. 更新 repository release version source；
6. 运行既有 registry / catalog / marketplace generator；
7. 更新 root `CHANGELOG.md` release manifest 与 README 状态表；
8. 运行 version consistency、payload parity、install smoke 与 CI；
9. 只有真实 payload / behavior 与 changelog 一致才发布。

不要先统一 bump 十个 version，再事后寻找理由。

## 7. 必须有的 regression

长期至少保护：

- repository release source 与 CLI / registry / README current release 一致；
- Marketplace config 中每个中央 plugin 都有合法 SemVer；
- 十个中央 plugin 与 `docs/plugin-changelogs/*.md` 一一对应；
- changelog 当前版本与 marketplace config 对应 plugin version 一致；
- README plugin status 表与 version/maturity canonical sources 一致；
- generated plugin manifest version 与 source config 一致；
- maintenance changelog/TODO 不进入普通 plugin runtime payload。

## 8. 与真实任务 refinement 的关系

plugin TODO 回答“下一步可能要改什么”；plugin changelog 回答“已经在哪个版本正式改变了什么”。两者不能混用。

标准路径是：

```text
real feedback
-> docs/plugin-todos/<plugin>.md
-> bounded promotion
-> implementation + regression
-> plugin version bump（仅 affected plugin）
-> docs/plugin-changelogs/<plugin>.md
-> repository release
```

任何版本提升都必须最终落到可观察的 user-facing improvement；不能因为 TODO 变多、schema 变多或 benchmark 多跑了一轮就升 minor/major。
