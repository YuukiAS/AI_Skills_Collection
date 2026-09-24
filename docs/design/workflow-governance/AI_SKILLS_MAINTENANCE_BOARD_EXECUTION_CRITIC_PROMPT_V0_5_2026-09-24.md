# AI Skills 维护看板 — Execution-ready Critic Prompt v0.5

你是 AI Research Stack 的独立 Critic thread。

当前只复核 execution package v0.5 是否关闭上一轮唯一 stable blocker `BOARD-LOCATOR-SCOPE-01`。不要重新设计已经 PASS 的 lifecycle、full-inbox、Clear Writing、BOARD-01、BOARD-UX、BOARD-SYNC、BOARD-CONSUMER、BOARD-MAINTAINER-SCOPE、五 consumer、per-consumer Maintainer 或 tracking-locator architecture。

本轮只读审查，不执行、不创建 GitHub Project/Issue、不 backfill、不启动 Codex、不调用 paid API、不修改 ChatGPT Project settings、不修改 server/local machine/Host/Bridge Kit。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = EXECUTION_READY_REVIEW_V0_5
package_version = v0.5
package_snapshot_commit = d2afbc0fa984a14b659a416fdab5089566549861
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

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_4_2026-09-24.md`

commit：

`f8203829641588322215fba585a5fd6844240853`

Previous blocker status：

```text
BOARD-TRACKING-LOCATOR-01 = CLOSED
BOARD-LOCATOR-SCOPE-01 = NEW_STABLE_BLOCKER
```

上一轮已确认 v0.4 其余 execution architecture可保留。没有新直接事实时，不重新扩大审查范围。

## Exact v0.5 package

Implementation Plan：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_5_2026-09-24.md`

Canonical Goal：

`docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_5.md`

Kickoff Draft：

`docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_5.md`

三件套同一 package snapshot：

`d2afbc0fa984a14b659a416fdab5089566549861`

v0.4 package 已 superseded，不得交给 Codex。

## 必须先读取最新 main

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- approved v5 Proposal
- v5 Critic PASS
- latest execution Critic review v0.4
- v0.5 Plan / Goal / Kickoff
- root `TODO.md`

按需读取 root TODO 当前声明的 plugin / standalone-skill maintenance inbox navigation，只为理解 freeze semantics，不重新审 domain TODO内容。

## BOARD-LOCATOR-SCOPE-01 的 v0.5 修复

### 1. authority source 在 task mutation 前冻结

v0.5 要求 kickoff preflight：

1. fetch kickoff-time latest `origin/main`;
2. 记录 exact `KICKOFF_BASE_COMMIT`;
3. 读取该 exact commit 的 unmodified root `TODO.md`;
4. 只解析其中正式声明 canonical maintenance inbox 的 structured navigation entries；
5. 验证每个 parsed path 在同一 base存在；
6. freeze exact path set；
7. exact reviewed branch/worktree从同一 base创建；
8. 第一份 task-content evidence写：
   `results/repo--maintenance-board-lifecycle/FROZEN_CANONICAL_INBOX_ALLOWLIST.md`;
9. 在此 evidence存在前，不允许其他 task tracked-file mutation、Project/Issue creation或 backfill。

Branch/worktree bootstrap identity本身不改变 repo content。

### 2. frozen evidence

allowlist evidence 至少记录：

```text
KICKOFF_BASE_COMMIT = <sha>
ROOT_TODO_BLOB_SHA = <sha>
FROZEN_INBOX_COUNT = <N>
FROZEN_CANONICAL_INBOX_PATHS =
- <path>
...
```

这是 task evidence，不是长期 registry/service/runtime source。

### 3. task 自己不能扩权

v0.5 明确：

- 后续 task-mutated root TODO 不改变 frozen allowlist；
- task自己新增 inbox declaration也不给该 path write authority；
- 不允许重新读取 task-mutated TODO 来动态扩大 scope；
- rename/remove 不允许把 authority静默转给其他 path。

### 4. upstream main drift

kickoff后如果 upstream main新声明 canonical inbox：

- 不自动获得 locator-write authority；
- 不静默计入本 task full-inbox completeness；
- 若必须纳入本次 task，按 semantic-drift/scope-expansion contract返回 Planner/用户；
- 否则 defer给后续 maintenance并记录 closure evidence。

不新增 watcher / allowlist service。

### 5. locator-only architecture保持

只有 frozen path set中的 source entries，且 disposition为：

- TRACKED
- MERGED_INTO_TRACKING_ISSUE

才能在同一 maintenance action写/更新：

`tracking: #<issue-number>`

保持：

- independent -> own Issue；
- duplicate/merged -> shared Issue；
- reused Issue -> actual number；
- merge/rebind -> affected entries更新真实 current Issue；
- raw NEW maturity保持 NEW；
- locator-only不能改 problem/evidence/maturity/candidate action等；
- Project Status不回写 Markdown；
- non-tracked item不强制 locator；
- ambiguous locator -> fail closed。

### 6. TODO_COVERAGE保持一次性

`TODO_COVERAGE.md`仍只证明 frozen kickoff-base allowlist的 bootstrap completeness。

长期 mapping来自 source entry自己的 `tracking: #N`。

## Direct validation

v0.5要求直接证明：

1. `KICKOFF_BASE_COMMIT` = task branch/worktree真正使用的 unmodified kickoff-time base；
2. `ROOT_TODO_BLOB_SHA` = 该 base 的 root TODO blob；
3. frozen path list = 该 unmodified root TODO正式声明的 canonical maintenance inbox exact set；
4. frozen paths在同一 base实际存在；
5. first task-content evidence是 frozen allowlist artifact；
6. every locator edit path属于 frozen set；
7. no locator edit outside frozen set；
8. task-mutated root TODO没有扩大 authority；
9. post-kickoff upstream新增 inbox没有被静默加入；
10. 原有 TRACKED/MERGED locator、maturity、substantive-field validation继续 PASS。

请判断这些是否足以关闭 self-expanding authorization envelope。

## External reality check

Planner本轮针对性核对了 GitHub官方 REST docs：repository content/commit可以按 exact commit/ref读取，因此 execution package使用 exact `KICKOFF_BASE_COMMIT`读取 root TODO而不是moving task branch是现实可实现的。

请独立核对官方 GitHub当前文档，重点只确认 exact commit/ref content读取能力；不要因此扩展成新API设计。

优先：
- `docs.github.com/en/rest/repos/contents`
- `docs.github.com/en/rest/commits/commits`

## 已通过且本轮不要重开的内容

v0.5保持：

```text
TODO -> DOING -> ADAPTING -> DONE
```

以及：

- full-inbox；
- raw NEW Project TODO / maturity unchanged；
- Clear Writing；
- actual Project surface review；
- BOARD-01；
- GitHub Project bootstrap；
- ChatGPT Project instructions one-time setup；
- AGENTS / Planner / Critic proactive sync；
- no-tool exact pending mutation；
- durable `tracking: #N` architecture；
- central implementation complete -> ADAPTING；
- five logical consumers：
  - Longleaf_Codex
  - Longleaf_Backup_Codex
  - CUHK_Workstation_WSL_Codex
  - Workstation
  - Legion
- per-current-consumer Maintainer；
- no cross-machine controller；
- initial Kickoff不授权 server/local mutation；
- exact branch/worktree；
- NONE / NO_BUMP；
- private README no-update default；
- no standalone Kanban skill/plugin；
- no Action/controller/watcher/database/registry/ledger。

上一轮 Critic已明确这些可保留。除非 v0.5 freeze修复直接引入回归，不要移动这些终点。

## Exact machine resolution

继续保持：

- initial Kickoff不授权 machine mutation；
- ADAPTING时按 per-consumer authority解析/freeze exact identities；
- identity解析如需访问machine，先走该consumer bounded authorization；
- 不猜 locator；
- 不建立cross-machine controller。

## 重点复核

### S1 — BOARD-LOCATOR-SCOPE-01 是否关闭

当前 task 是否已经不能通过修改 root TODO 来扩大自己的 locator-write allowlist？

### S2 — freeze时机是否足够早

authority 是否来自 unmodified kickoff-base root TODO，而不是 branch-mutated content？

### S3 — parser边界是否足够窄

structured canonical inbox navigation是否能避免 incidental links被误纳入scope？

若 root TODO格式本身歧义，fail-closed是否足够？

### S4 — upstream drift处理是否正确

kickoff后新inbox是否不会自动扩权；需要纳入时是否正确返回scope-expansion review？

### S5 — evidence是否过重

FROZEN_CANONICAL_INBOX_ALLOWLIST.md 是否只是 bounded task evidence，而没有变成长期registry/service？

### S6 — full-inbox claim是否诚实

v0.5明确 completeness只针对 frozen kickoff-base allowlist，而不是 moving post-kickoff inbox universe；是否与bounded execution一致？

### S7 — locator architecture是否完整保留

tracking backlink / raw NEW maturity / duplicate/reuse/rebind / TODO_COVERAGE边界是否没有回归？

### S8 — 其他 execution architecture是否保持

没有新直接风险则不新增与 blocker无关的REVISE。

## 输出要求

如果仍需要修改：

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW_V0_5
PACKAGE_SNAPSHOT_COMMIT = d2afbc0fa984a14b659a416fdab5089566549861
READY_FOR_CODEX = NO
RECHECKED_BLOCKERS = BOARD-LOCATOR-SCOPE-01
```

stable blocker必须给 direct evidence、causal risk、minimum close condition。

不要无新事实重新打开之前已关闭的 blocker。

然后按 Critic Role Contract自动生成完整 Planner返修 prompt。

如果 blocker已关闭且 package execution-ready：

先用自然中文说明：

- BOARD-LOCATOR-SCOPE-01如何关闭；
- kickoff-base freeze是否真正阻止self-expanding authority；
- frozen evidence是否足够、不过重；
- post-kickoff drift语义是否正确；
- locator architecture是否完整保留；
- v0.4其他已通过execution boundaries是否没有回归；
- PASS证明什么、不证明什么。

然后输出：

```text
RESULT = PASS
REVIEW_STAGE = EXECUTION_READY_REVIEW_V0_5
PACKAGE_SNAPSHOT_COMMIT = d2afbc0fa984a14b659a416fdab5089566549861
RECHECKED_BLOCKERS = BOARD-LOCATOR-SCOPE-01
CLOSED_BLOCKERS = BOARD-LOCATOR-SCOPE-01
NEW_BLOCKERS = NONE
APPROVED_PROPOSAL_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_5_2026-09-24.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_5.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_5.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
```

并按 Critic Role Contract逐字输出 package snapshot中已审过的 v0.5 Kickoff正文；不要PASS后改写一个不同prompt。

## Review 文件授权

用户若把本 prompt原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_5_2026-09-24.md`

并 ordinary non-force push。

除此之外禁止修改：

- v5 Proposal；
- v0.5 Plan / Goal / Kickoff；
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
