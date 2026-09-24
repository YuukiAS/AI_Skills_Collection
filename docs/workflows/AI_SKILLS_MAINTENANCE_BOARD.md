# AI Skills Maintenance Board

本文件是 AI_Skills_Collection 维护看板的唯一完整规则。其他入口只引用本文件，不复制整套规则。

看板解决的是一个很具体的问题：plugin / skill TODO 保存真实问题和证据，GitHub Project 保存执行生命周期。两者要互相定位，但不能混成一套状态机。

## 1. 适用范围

当 AI_Skills_Collection 的 thread、Planner、Critic、Codex 或 AI Skills Maintainer 要做以下任一动作时，先读取本文件：

- 向中央 plugin / standalone skill TODO 记录真实使用反馈；
- triage TODO 条目是否进入 central maintenance tracking；
- 为 AI_Skills maintenance proposal、review、implementation 或 adaptation 维护看板；
- 判断一个 tracked item 该在 `TODO`、`DOING`、`ADAPTING` 还是 `DONE`；
- 合并、复用或重新绑定 tracking Issue；
- 在没有 Project mutation surface 时输出 pending mutation。

本文件不创建新 plugin、skill、watcher、database、ledger、registry、GitHub Action、MCP service 或跨机器控制面。

## 2. Source Ownership

### Canonical inbox

根 `TODO.md` 只声明 canonical maintenance inbox 的导航入口。具体问题仍写在：

```text
docs/plugin-todos/<plugin>.md
docs/skill-todos/<standalone-skill>.md
```

这些 inbox 保存：

- 真实失败；
- source / evidence；
- maturity 或 triage 状态；
- target layer、candidate action、promotion gate 等维护语义；
- durable source backlink：`tracking: #N`。

它们不保存 Project lifecycle Status。

### Tracking Issue / Project

GitHub Project `AI Skills Maintenance` 和其中的 tracking Issue 保存：

- top-level maintenance idea；
- 当前执行进度；
- 当前执行锚点；
- 下一步；
- lifecycle Status；
- Resolution commit；
- adaptation consumer checklist when applicable。

Project lifecycle status 不是 plugin TODO maturity status。一个 source 条目可以仍然是 `status: NEW`，同时因为它是真实、central、仍有维护意义的问题而出现在 Project `TODO`。

## 3. Lifecycle

看板只有四个 lifecycle Status：

```text
TODO -> DOING -> ADAPTING -> DONE
```

- `TODO`：已进入 central tracking，但尚未开始实质执行。
- `DOING`：已有当前执行锚点，例如 Planner round、implementation branch、review package、CI / review gate。
- `ADAPTING`：central implementation 已完成，但 machine-consumed workflow / shared maintenance mechanism 仍需 downstream consumer adaptation。
- `DONE`：完整 closure 已成立，tracking Issue 已完成关闭，并记录 Resolution commit。

不要新增 `WAITING`、`BLOCKED`、`REVIEWING`、`READY` 等第五状态。等待外部 review、CI、user-only action 或 tool availability 时，保持当前真实 lifecycle，并在 Issue 的“当前进度 / 下一步”里写清楚。

## 4. Project Shape

唯一 Project：

```text
owner = YuukiAS
title = AI Skills Maintenance
visibility = private
linked repository = YuukiAS/AI_Skills_Collection
tracking label = maintenance-track
```

必需字段：

- `Status`：`TODO` / `DOING` / `ADAPTING` / `DONE`
- `Area`
- `Resolution commit`

必需视图：

- `Board`：按 Status 分组，卡片至少直接显示 title、Area、Status。
- `Active`：显示 DOING / ADAPTING，至少显示 title、Area、Status。
- `By area`：按 Area 组织，至少显示 title、Area、Status。
- `History`：显示 DONE，至少显示 title、Area、Status、Resolution commit。

不要新增 maturity field、machine registry field、current workflow field 或另一个 board schema。

## 5. Admission And False-DONE Guard

Project lifecycle item 只能是带 `maintenance-track` label 的 Issue。

Auto-add 至少满足：

```text
is:issue label:maintenance-track
```

Implementation/design PR 不作为 lifecycle item。`pull request merged -> Done` 必须禁用。`issue closed -> Done` 只用于完整 closure 后的最后机械动作。

在真实 DONE 前：

- 不要添加会让中间 PR merge 自动关闭 tracking Issue 的 Development/manual linked relationship；
- PR body 和 commit message 不得对 tracking Issue 使用 `close` / `closes` / `closed` / `fix` / `fixes` / `fixed` / `resolve` / `resolves` / `resolved`；
- 可以使用非关闭引用；
- repository-wide auto-close 规则保持原样。

Rejected、superseded、duplicate、not-planned item 不得显示为 DONE。需要关闭时，先从 Project 移除或归档，再 truthfully close。

## 6. Tracking Issue Copy

tracking Issue 是用户直接看的入口。标题必须自然、简洁，不能主要由 task key、hash、branch、路径或内部状态字符串构成。

每个 tracking Issue 顶部固定为：

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

详细 evidence / history 放在后面。DOING / ADAPTING 至少有一个 current valid anchor。DONE / History 必须直接显示 Resolution commit。

创建或实质改写 reader-facing Project / Issue copy 前，必须真实调用当前安装的 Clear Writing（`writing-style`）。Clear Writing 只能改善表达，不得改变：

- source maturity；
- lifecycle Status；
- Area；
- `tracking: #N`；
- required-consumer truth；
- exact locators；
- Resolution commit；
- evidence meaning。

如果当前 runtime 不能真实调用 Clear Writing，停止该 reader-facing mutation，并报告 `CLEAR_WRITING_UNAVAILABLE`。

## 7. Source Backlink

任何 canonical source entry 一旦进入 tracking scope，同一 maintenance action 必须写入或更新：

```text
tracking: #<issue-number>
```

规则：

- independent entry 绑定自己的 top-level tracking Issue；
- duplicate / merged entries 可以共享一个 top-level tracking Issue；
- reuse existing Issue 时回写真实 Issue number；
- merge / rebind 时更新所有受影响 canonical source entries 到当前真实 Issue；
- raw `NEW` maturity 保持 `NEW`；
- Project Status 不得回写 Markdown。

`tracking: #N` 是唯一 durable source-to-Issue backlink。`TODO_COVERAGE.md`、review report、Project item id 或临时结果文件都不能代替它。

locator-only edit 只能新增或更新 `tracking: #N`，不得借此改变：

- source maturity/status；
- problem；
- evidence；
- project-specific context；
- target layer；
- candidate action；
- promotion gate；
- 其他 substantive TODO field。

non-tracked disposition 不为了 completeness 强行加 locator。现有 locator 与 current mapping 冲突且无法无歧义判断时，停止该 entry，返回 Planner。

## 8. Bootstrap Coverage

一次 full-inbox bootstrap 只能声称覆盖被冻结的 canonical inbox allowlist。

bootstrap 对每个仍有维护意义的 source entry 给一个 disposition：

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

不要机械地一 heading 一 Issue。只有 evidence 清楚指向同一个 top-level idea 时才 merge。若 merge 需要实质 genericity 判断，不能为了减少卡片而猜。

`results/<task_key>/TODO_COVERAGE.md` 只是一轮 bootstrap completeness evidence，不是 registry、schema、runtime lookup、Project status source 或 steady-state mapping。

## 9. Planner Responsibilities

Planner 在 formal AI_Skills maintenance 中负责：

- triage 条目是否进入 tracking scope；
- create / bind / reuse tracking Issue，或在无 Project mutation surface 时输出 exact pending mutation；
- 同一 maintenance action 回写或更新 source `tracking: #N`；
- first substantive Plan/design 时把 tracking Issue 推进到 DOING，并写当前执行锚点；
- handoff 时更新 next action / evidence；
- central implementation complete 且 required consumers 尚未完成时推进到 ADAPTING；
- 不能要求用户手工拖 Kanban 或手工补 source locator。

Planner 不因为 execution-ready Critic PASS 或 Executor 自报完成就把 item 推到 DONE。

## 10. Critic Responsibilities

Critic 在 formal AI_Skills maintenance review 中负责核对：

- review locator；
- next action；
- lifecycle truth；
- tracking Issue 是否反映真实 evidence；
- source backlink 是否与 tracking Issue 一致；
- PASS / REVISE 是否被错误理解成 Project Status mutation。

Critic PASS 或 REVISE 本身不机械改变 Status。Critic 不改 Planner Proposal，不推进 Reviewed Handoff `CURRENT.json`，不冒充 Executor。

无 Project mutation surface 时，Critic 输出 exact pending Project mutation，不声称已同步。

## 11. No-Tool Surface

如果当前 GPT / Planner / Critic / Maintainer 不能修改 GitHub Project，它仍然保留语义责任：

1. 更新自己能合法更新的 Issue / source evidence；
2. 若 repo write authority 与 binding 都存在，保持 source `tracking: #N` 正确；
3. 输出 exact pending Project mutation；
4. 明确 Project 尚未同步；
5. 不要求用户手工拖卡片或手工补 locator。

下一次 Project-capable maintenance action 必须先核对 pending mutation 仍属于当前 tracking Issue、evidence 仍 current、lifecycle 仍兼容，然后机械应用。

## 12. Normal Entry Triggers

### ChatGPT Project instructions

canonical board doc 进入 `main` 后，AI Research Stack ChatGPT Project instructions 需要一次性加入以下短 trigger：

```text
AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步，并在 canonical source entry 回写/更新 tracking: #N。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。
```

如果当前执行环境不能修改 Project instructions，只提出一次 HUMAN_ONLY exact-text setup。完成后，同一 Goal 继续；routine sync 不再重复询问。

### Codex repo entry

Codex 在 AI_Skills_Collection 中工作时，通过 `AGENTS.md` 的短 locator 消费本文件。不要为看板新建 standalone Kanban skill、`kanban-sync` skill、新 plugin 或新 profile。

### Planner and Critic

Planner 和 Critic 通过各自 role contract 的短入口消费本文件。正式 maintenance 轮次不得把看板同步留给用户手工操作。

## 13. Central Complete And ADAPTING

对于普通 plugin / workflow implementation：

```text
execution-ready Critic PASS
-> Codex implementation
-> independent implementation review PASS
-> canonical owner integration / release closure when required
= central implementation complete
```

execution-ready PASS、Executor summary、local tests、CI PASS 或 Reviewer PASS without required canonical closure 都不是 central implementation complete。

对于 machine-consumed workflow / shared maintenance mechanism：

```text
central implementation complete -> ADAPTING
```

ADAPTING 不等于 DONE。

## 14. Required Consumers For Machine-Consumed Work

当前默认 required logical consumers：

Server / remote Codex：

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

Local：

4. `Workstation`
5. `Legion`

这些 consumer requirement 只适用于 machine-consumed workflow / shared maintenance mechanism。普通文档、单一 artifact quality improvement、普通 domain plugin quality improvement 不自动继承五机验收。

进入 ADAPTING 时，tracking Issue 必须冻结每个 required consumer 的 exact current identity / locator。若解析 identity 需要访问某台机器，必须先获得该 consumer 的 bounded authority；不得猜 locator。

每个 consumer PASS 至少需要：

- actual target identity；
- approved adaptation / update action；
- installed / loaded identity；
- relevant normal-entry consumption；
- fresh-session / restart boundary when required；
- risk-matched should-not-change / failure safety；
- durable evidence locator。

单台 consumer PASS 不能关闭 top-level Issue。

## 15. AI Skills Maintainer Boundary

AI Skills Maintainer 是 per-current-consumer adaptation executor，不是 cross-machine controller。

它只负责当前 consumer 的：

- discovery；
- adaptation / update；
- installed / loaded identity；
- fresh-session / normal-entry verification；
- durable evidence；
- current-consumer PASS / truthful blocker。

五 consumer aggregate truth 属于 tracking Issue / Project lifecycle。AI Skills Maintainer 不持有 machine registry，不做五机 orchestrator，不做 credential broker。

## 16. Final DONE

machine-consumed item 的最终 DONE 需要：

```text
all required consumers PASS/N/A
+ durable evidence complete
+ Resolution commit
+ tracking Issue completed close
+ issue-closed workflow -> DONE
```

N/A 必须有 frozen durable reason。future optional machine 不追溯扩大已经冻结的 DONE contract。

## 17. Version Decision

看板 metadata、GitHub Project metadata、`tracking: #N` backlink、bootstrap coverage evidence 和本文件本身不改变任何 plugin runtime。

除非同一任务还明确修改 production plugin behavior 并满足版本政策，本类 board maintenance 默认：

```text
Repository bump decision: NONE
Affected plugins:
- all: NO_BUMP
```
