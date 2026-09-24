# AI Skills 维护看板 — Execution-ready Critic Prompt v0.4

你是 AI Research Stack 的独立 Critic thread。

当前只复核 execution package v0.4 是否关闭上一轮唯一 stable blocker `BOARD-TRACKING-LOCATOR-01`。不要重新设计已经 PASS 的 lifecycle、full-inbox、Clear Writing、BOARD-01、BOARD-UX、BOARD-SYNC、BOARD-CONSUMER、BOARD-MAINTAINER-SCOPE、五 consumer 或 per-consumer Maintainer architecture。

本轮只读审查，不执行、不创建 GitHub Project/Issue、不 backfill、不启动 Codex、不调用 paid API、不修改 ChatGPT Project settings、不修改 server/local machine/Host/Bridge Kit。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = EXECUTION_READY_REVIEW_V0_4
package_version = v0.4
package_snapshot_commit = 696c1bebad3e7f2dbe65026a02de3bdb4cf21117
execution_branch = reviewed/repo--maintenance-board-lifecycle
execution_worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
```

## Approved design

Proposal：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`

commit：

`d14565e152b9b953c76c0722ad6e6343850335a7`

Design Critic PASS：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_CRITIC_REVIEW_2026-09-24.md`

commit：

`012a43c7edefddd7f071d43425f7be937453f73a`

## Previous execution review

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-24.md`

commit：

`98b7b875eabedb773f0d1d5bcdcd23217cc9b055`

Stable blocker：

`BOARD-TRACKING-LOCATOR-01`

上一轮已明确 v0.3 其他 execution architecture 可保留。没有新直接证据时，不重新扩大审查范围。

## Exact v0.4 package

Implementation Plan：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_4_2026-09-24.md`

Canonical Goal：

`docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_4.md`

Kickoff Draft：

`docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_4.md`

三件套同一 package snapshot：

`696c1bebad3e7f2dbe65026a02de3bdb4cf21117`

v0.3 package 已 superseded，不得交给 Codex。

## 必须先读取最新 main

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- approved v5 Proposal
- v5 Critic PASS
- v0.3 execution Critic review
- v0.4 Plan / Goal / Kickoff
- root `TODO.md`
- `docs/plugin-todos/README.md`

按需查看 root TODO 当前列出的 plugin / standalone-skill inbox，只为验证 canonical inbox scope；不要重新审其 domain 内容。

## BOARD-TRACKING-LOCATOR-01 的 v0.4 修复

### 1. Allowed repo scope 只扩到 canonical inbox locator edits

v0.4 允许修改：

- kickoff-time root `TODO.md` 正式列出的 `docs/plugin-todos/*.md` canonical inbox；
- kickoff-time root `TODO.md` 正式列出的 `docs/skill-todos/*.md` canonical inbox；
- execution-time current root TODO 若正式声明其他 canonical maintenance inbox，也只允许这些 declared inbox entry 的 tracking-locator maintenance。

这不是对目录 glob 的任意 source-write 授权。

### 2. TRACKED / MERGED source entry 必须 durable backlink

对于 disposition：

- `TRACKED`
- `MERGED_INTO_TRACKING_ISSUE`

同一 maintenance action 必须写入/更新：

```text
tracking: #<issue-number>
```

规则：

- independent entry -> own Issue；
- duplicate/merged entries -> 多条 source entry 可共享一个 top-level Issue；
- reuse existing Issue -> 写实际 reused Issue number；
- merge/rebind -> 更新 affected source entries 到真实 current Issue；
- raw NEW source maturity仍保持 NEW。

### 3. Locator-only boundary

写 tracking locator 不能顺手改：

- source maturity/status；
- problem；
- evidence；
- project-specific context；
- target layer；
- candidate action；
- promotion gate；
- 其他 substantive TODO field；
- Project lifecycle Status。

Project TODO/DOING/ADAPTING/DONE 不回写 Markdown。

non-tracked disposition 不被强制加 locator。

existing locator 冲突且无法无歧义判断 -> fail that entry / return Planner，不猜。

### 4. TODO_COVERAGE 仍是一次性 evidence

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

仍只证明 bootstrap completeness。

steady-state durable mapping必须来自 canonical source entry自身的：

`tracking: #N`

不得把 TODO_COVERAGE 变成长期 runtime lookup registry。

### 5. Steady-state contract

canonical board doc必须明确：

```text
create / bind / reuse tracking Issue
-> same maintenance action write/update source tracking: #N

Issue merge / rebind
-> update every affected canonical source entry to actual current Issue
```

routine sync不得让用户手工补 locator。

### 6. Direct validation

v0.4 B3/B6/C3/C6 等价 gates 已要求验证：

- every TRACKED source entry has correct tracking locator；
- every MERGED source entry has correct shared locator；
- reused Issue number正确回写；
- non-tracked entry不强制 locator；
- raw NEW maturity不因 Project admission改变；
- locator-only edits没有改 substantive TODO content；
- Project Status没有复制回 Markdown；
- TODO_COVERAGE不是 steady-state/runtime mapping source；
- create/bind/reuse/merge steady-state path 自动维护 locator。

## Kickoff authorization

v0.4 Kickoff 已显式授权：

- root-TODO-declared canonical plugin/skill/other maintenance inbox files 的 `tracking: #N` locator-only edits；
- 不授权其他 substantive TODO mutation。

请确认这解决了 v0.3 “设计要求写 backlink，但合法 file scope不允许写”的 execution contradiction。

## 已通过且本轮不要重开的内容

v0.4 保持：

```text
TODO -> DOING -> ADAPTING -> DONE
```

以及：

- full-inbox coverage；
- raw NEW Project TODO / maturity unchanged；
- Clear Writing + actual Project surface review；
- BOARD-01；
- GitHub Project bootstrap route；
- ChatGPT Project instructions one-time setup；
- AGENTS / Planner / Critic normal-entry consumer rules；
- no-tool exact pending mutation；
- central implementation complete -> ADAPTING；
- five logical consumers：
  - Longleaf_Codex
  - Longleaf_Backup_Codex
  - CUHK_Workstation_WSL_Codex
  - Workstation
  - Legion
- per-current-consumer Maintainer；
- no cross-machine controller；
- initial central Kickoff 不授权 server/local mutation；
- exact branch/worktree + fail-closed；
- Repository NONE / all plugins NO_BUMP；
- private README no-update default；
- no standalone Kanban skill/plugin；
- no Action/controller/watcher/database/registry/ledger。

上一轮 Critic已明确这些 execution boundaries PASS。没有 v0.4 新回归时不要重新移动终点。

## Exact machine resolution

不需要新增 blocker。

继续保持：

- initial Kickoff不授权 machine mutation；
- ADAPTING时按 per-consumer authority解析/freeze exact identities；
- 如果解析 exact identity 本身需要访问某个 machine，先经过该 consumer bounded authorization；
- 不无授权访问，不猜 locator，不新增 cross-machine controller。

## 重点复核

### L1 — blocker 是否关闭

现在 Codex 是否既有能力创建/reuse Issue，又有合法 authority在真实 canonical source entry写回 `tracking: #N`？

### L2 — scope 是否过宽

“root TODO 正式声明的 canonical inbox + locator-only”是否足够窄，不会变成 arbitrary plugin TODO rewrite 权限？

### L3 — source truth 是否保持

raw NEW maturity、problem/evidence等是否仍由原 source保持，Project lifecycle不回写 Markdown？

### L4 — duplicate/reuse/rebind

多个 source entry共享 Issue是否可持续；reuse existing Issue / rebind后是否能保持 canonical source locator正确？

### L5 — TODO_COVERAGE 边界

是否仍只是 one-time completeness evidence，而不是偷偷变成第二个 registry？

### L6 — validation 是否能抓到真实失败

是否能发现：

- TRACKED entry无 locator；
- MERGED entry指错 Issue；
- reused Issue未回写；
- maturity被误改；
- Status写回 Markdown；
- non-tracked entry被强行加 locator；
- TODO_COVERAGE被当长期 lookup。

### L7 — 其他 v0.3 execution architecture 是否被 v0.4 破坏

如果没有，不得新增与 blocker无关的 REVISE。

## 输出要求

如果仍需要修改：

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW_V0_4
PACKAGE_SNAPSHOT_COMMIT = 696c1bebad3e7f2dbe65026a02de3bdb4cf21117
READY_FOR_CODEX = NO
RECHECKED_BLOCKERS = BOARD-TRACKING-LOCATOR-01
```

stable blocker必须有 direct evidence、causal risk、minimum close condition。

不要无新事实重新打开之前已关闭的 design/execution blocker。

然后按 Critic Role Contract自动生成完整 Planner返修 prompt。

如果 blocker已关闭且 package execution-ready：

先自然中文说明：

- BOARD-TRACKING-LOCATOR-01 怎样关闭；
- canonical TODO -> Issue backlink 是否持久且不过度双写；
- locator-only scope 是否足够窄；
- TODO_COVERAGE 是否仍只是一次性 evidence；
- v0.3 已通过的 full-inbox / Clear Writing / BOARD-01 / normal-entry / five-consumer architecture 是否保持；
- PASS 证明什么、不证明什么。

然后输出：

```text
RESULT = PASS
REVIEW_STAGE = EXECUTION_READY_REVIEW_V0_4
PACKAGE_SNAPSHOT_COMMIT = 696c1bebad3e7f2dbe65026a02de3bdb4cf21117
RECHECKED_BLOCKERS = BOARD-TRACKING-LOCATOR-01
CLOSED_BLOCKERS = BOARD-TRACKING-LOCATOR-01
NEW_BLOCKERS = NONE
APPROVED_PROPOSAL_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_4_2026-09-24.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_4.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_4.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
```

并按 Critic Role Contract **逐字输出 package snapshot 中已审过的 v0.4 Kickoff正文**；不要 PASS 后重新写一个语义不同的新 Kickoff。

## Review 文件授权

用户若把本 prompt原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_4_2026-09-24.md`

并 ordinary non-force push。

除此之外禁止修改：

- v5 Proposal；
- v0.4 Plan / Goal / Kickoff；
- AGENTS / Planner/Critic contracts / TODO / README；
- canonical plugin/skill TODO inbox；
- ChatGPT Project instructions；
- Project / Issue；
- plugin source；
- machine-update source；
- Bridge Kit；
- server/local machine/Host；
- 任何其他 repo。

提交后报告 exact review commit。
