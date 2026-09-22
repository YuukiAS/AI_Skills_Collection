# AI Skills 维护看板 — Execution-ready Critic Prompt v0.2

你是 AI Research Stack 的独立 Critic thread。

当前只复核 execution package v0.2 是否关闭上一轮两个 stable blockers：

- `BOARD-UX-01`
- `BOARD-SYNC-01`

不要重新设计已经 PASS 的 lifecycle，不创建 Project/Issue，不做 backfill，不启动 Codex，不调用 paid API，不修改 production/server/Host/Bridge Kit。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = EXECUTION_READY_REVIEW_R2
package_version = v0.2
package_snapshot_commit = b77f656fd6e3c690f5406cbf9b371e144708dcfc
execution_branch = reviewed/repo--maintenance-board-lifecycle
execution_worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
```

## Approved design

Proposal：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`

commit：

`da46f14141888c1bcd94bf94a486bcb1a1b0ec7c`

Design Critic PASS：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`

commit：

`8213c843b4d91c63f6de62740e26ef8d215a59e0`

BOARD-01 已在设计阶段 CLOSED，不重新打开，除非 v0.2 execution package 本身重新引入了同一直接风险。

## Previous execution review

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-22.md`

commit：

`4aaa95d79e84af63c93362612988cf79829d8043`

稳定 blockers：

```text
BOARD-UX-01
BOARD-SYNC-01
```

## 本轮必须审的同版 package

### Implementation Plan v0.2

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_2_2026-09-22.md`

### Canonical Goal v0.2

`docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_2.md`

### Kickoff Draft v0.2

`docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_2.md`

三件套同一 snapshot：

`b77f656fd6e3c690f5406cbf9b371e144708dcfc`

先读取最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- approved v2 Proposal
- v2 design Critic PASS
- v0.1 execution Critic review
- v0.2 Plan / Goal / Kickoff

按需读取 `README.md`、`scripts/codex_marketplace_config.json` 或当前 Clear Writing / `writing-style` source，只为核对当前 plugin identity / 可调用边界；不要重新全量审 plugin behavior。

## 已冻结 lifecycle 不改

```text
TODO -> DOING -> ADAPTING -> DONE
```

继续保持：

- Project item = top-level tracking Issue；
- plugin TODO = failure/evidence/maturity inbox；
- Planner–Critic / Reviewed Handoff / Executor task = execution evidence；
- WAITING/BLOCKED 不是主状态；
- Resolution commit = owner repo canonical closure/evidence commit；
- optional post-DONE consumer -> follow-up item；
- one-time bootstrap / steady-state maintenance 分离；
- BOARD-01 全部 guardrails；
- bounded one-pass backfill；
- NONE / NO_BUMP；
- private Project 下 README 默认 no update required；
- exact reviewed branch/worktree + fail-closed；
- UI-only built-in workflow dependency 只允许一次最小 HUMAN_ONLY action + same-Goal resume。

## BOARD-UX-01 v0.2 返修

v0.2 现在冻结以下人类可读契约：

1. tracking Issue title 必须自然、简洁，不以 task key/hash/path/internal status 为标题主体；
2. Issue 顶部固定：
   - 问题
   - 当前进度
   - 当前执行锚点
   - 下一步
3. DOING / ADAPTING 至少一个 current valid locator；
4. detailed history/evidence 放后面，不挤进顶部；
5. Board / By area 至少直接显示 human-readable title + Area + Status；
6. 每个有 tracked items 的 Area 可直接查看；
7. DONE / History 直接显示 Resolution commit；
8. B1/B4/B5 改成 actual GitHub Project / Issue surface qualitative review，不能用 field existence / keyword / API receipt 代替。

### 用户新增的 Clear Writing 硬要求

用户进一步明确：

> 以后大部分 reader-facing maintenance text 都应优先使用 Clear Writing；Codex 只要修改 Kanban，必须调用，否则不可读的垃圾看板没有价值。

v0.2 因此规定：

- Codex 创建/修改 tracking Issue title、top summary、board reader-facing copy、closure/History human text、backfill copy 时，**必须在 mutation 前真实调用当前 installed Clear Writing（`writing-style`）**；
- Clear Writing 不得修改 Status / Area / required downstream / exact locators / Resolution commit / evidence meaning；
- Codex 如果无法真实调用 Clear Writing，必须在 board-copy mutation 前 fail closed，报告 `CLEAR_WRITING_UNAVAILABLE`，不得假装调用或静默写 generic copy；
- Planner/Critic/GPT 在当前 surface可调用时也优先用；若 GPT surface 没有该 plugin，仍必须遵守同一人类可读契约，不把润色甩给用户；
- `CLEAR_WRITING_USED=YES` 只是 supporting evidence，真正权威是 actual Project surface 的 qualitative review。

请重点判断：

1. 这是否完整关闭 BOARD-UX-01；
2. 强制 Codex 使用 Clear Writing 是否忠实用户要求，且没有把 writing-style 改成新的 product dependency / version bump；
3. `CLEAR_WRITING_UNAVAILABLE` fail-closed 是否过重或必要；
4. actual surface review 是否足以防机械 PASS；
5. 是否还存在“字段齐全但用户看不懂”的真实漏洞。

## BOARD-SYNC-01 v0.2 返修

v0.2 现在冻结 proactive sync：

### Raw NEW

真实项目 thread 只写 plugin TODO inbox，不自动建 Project item。

### Planner triage

进入 tracking scope 后，同一轮主动：

- create / bind Issue；
- `maintenance-track`；
- readable title / top summary；
- Area；
- truthful initial Status；
- `tracking: #N` 回写 plugin TODO；
- current proposal/task locator。

### Planner substantive round

开始实质 design/implementation：

- 自动 reconcile DOING；
- 更新 progress / current anchor / next action。

### Critic formal review

每轮 review：

- 主动写入/更新 review locator；
- 更新 next action；
- 核对 lifecycle truth；
- PASS/REVISE 本身不机械改变 Status。

### ADAPTING

core 已集成但 required downstream 未完：

- 当前 owner 主动改 ADAPTING；
- anchor 切到真实 downstream work。

### DONE

仍只按批准 closure contract。

### GPT 没有 Project mutation tool

GPT 仍然是语义 owner：

1. 更新自己能更新的 Issue summary/evidence；
2. 在 handoff 生成 exact pending Project mutation；
3. 下一有权限 Executor 在其他 board mutation 前消费并核对仍然有效；
4. 不让用户手工拖卡；
5. 不谎称已经同步。

canonical `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` 将拥有完整规则；AGENTS 只加简短 mandatory locator/consumer rule。

请重点判断：

1. 是否完整关闭 BOARD-SYNC-01；
2. Critic 主动同步 board evidence 是否与 Critic“不改 Proposal / 不推进 CURRENT”的角色边界兼容；
3. no-Project-tool GPT 的 pending mutation 是否是轻量 handoff，而不是新 schema/state machine；
4. routine sync 无需每次 user authorization 是否符合用户明确要求与当前低风险 maintenance boundary；
5. 是否还有现实路径让 Planner/Critic工作完成后看板持续漂移、最后又要用户提醒。

## 保持 v0.1 已通过的执行现实

上一轮已明确通过、这轮不要无新事实重审：

- real `gh project` CLI / Projects GraphQL route；
- current built-in workflow UI-only fallback；
- one minimal HUMAN_ONLY action + same-Goal resume；
- exact sibling worktree fail-closed；
- BOARD-01；
- bounded backfill；
- private Project；
- NONE / NO_BUMP；
- independent implementation review；
- final main integration / Resolution commit / current tracking Issue completed close。

如果 v0.2 新改动破坏其中任一边界，可以提出 blocker；否则不要移动终点。

## Required direct validation in v0.2

Critic 要确认 package 不再只验证结构。

v0.2 B1–B7 要求：

- actual Project structure；
- actual workflow / auto-add；
- self-hosting normal entry；
- bounded backfill fidelity；
- **actual Board / By area surface**；
- **所有本轮新建/实质重写 tracking Issue title + top summary**；
- current anchors；
- role-sync contract in canonical doc + AGENTS locator；
- Clear Writing real invocation by Codex；
- no-Project-tool GPT pending mutation route；
- independent qualitative review；
- final integration + Resolution commit + Issue completed close + actual DONE。

请判断是否有 proxy PASS 漏洞。

## 输出要求

如果 stable blockers 仍未关闭或 v0.2 引入新真实 blocker：

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW_R2
REVIEW_OBJECTS =
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_2_2026-09-22.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_2.md
- docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_2.md
PACKAGE_SNAPSHOT_COMMIT = b77f656fd6e3c690f5406cbf9b371e144708dcfc
READY_FOR_CODEX = NO
RECHECKED_BLOCKERS =
- BOARD-UX-01
- BOARD-SYNC-01
```

新 blocker 只能来自新事实、先前遗漏的关键直接风险或 v0.2 返修引入的真实回归。每条必须给直接证据、因果风险和最小关闭条件。然后自动生成完整 Planner返修 prompt。

如果两项 blocker 均关闭且没有新 blocker：

先用自然中文说明：

- BOARD-UX-01 怎样被关闭；
- BOARD-SYNC-01 怎样被关闭；
- Clear Writing mandatory invocation 是否合理；
- proactive Planner/Critic/GPT sync 是否真实可执行；
- actual surface review / pending mutation / backfill / exact worktree / version/README 是否保持边界；
- PASS 证明什么、不证明什么。

然后输出：

```text
RESULT = PASS
REVIEW_STAGE = EXECUTION_READY_REVIEW_R2
PACKAGE_SNAPSHOT_COMMIT = b77f656fd6e3c690f5406cbf9b371e144708dcfc
RECHECKED_BLOCKERS =
- BOARD-UX-01
- BOARD-SYNC-01
CLOSED_BLOCKERS =
- BOARD-UX-01
- BOARD-SYNC-01
NEW_BLOCKERS = NONE
APPROVED_PROPOSAL_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_2_2026-09-22.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_2.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_2.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
```

并按 Critic Role Contract **逐字输出已审过的 v0.2 Kickoff 正文**。不要 PASS 后再写一个语义不同的新 Kickoff。

## Review 文件授权

用户若把本 prompt 原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-22.md`

并 ordinary non-force push。

除此之外禁止修改：

- Proposal / Plan / Goal / Kickoff；
- AGENTS / TODO / README；
- Project / Issue；
- plugin source；
- Bridge Kit；
- server / Host；
- 任何其他 repo。

提交后报告 exact review commit。
