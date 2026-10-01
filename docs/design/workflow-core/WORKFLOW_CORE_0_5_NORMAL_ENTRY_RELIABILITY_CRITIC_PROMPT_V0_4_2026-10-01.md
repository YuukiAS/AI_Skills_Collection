# workflow-core 0.5 正常入口与执行路线可靠性 — Critic Re-review Prompt v0.4

你继续作为 AI Research Stack 的独立 Critic thread，对 `workflow-core / Verified Workflow 0.5` 做最后一次最小 **DESIGN_REVIEW_R4**。

本轮只复核 `WC05-D7` 的最后 vocabulary closure。

上一轮已经确认：

- `WC05-D1`–`WC05-D6` 全部 CLOSED；
- `WC05-D7.2`–`WC05-D7.5` 已 CLOSED；
- 三项 production change 不再重设计；
- G1–G5 不再扩大；
- #7/#8/#9/#10 专属逻辑不再引入。

不要实现代码，不要修改 production plugin，不要创建 execution branch/worktree，不要 bump version，不要启动 paid API，不要修改 Project/Issue、consumer machines、Longleaf `/users`、STAT5060、render specialist 或 Bridge Kit runtime。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `workflow-core`
- design_topic_or_task_key: `workflow-core--normal-entry-reliability`
- source_branch_or_ref: `main`
- review_stage: `DESIGN_REVIEW_R4`
- reviewed proposal v0.3: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_3_2026-10-01.md`
- reviewed proposal v0.3 commit: `3c33e160351b2c63d8b844af87f3fd7224f0b09a`
- revised proposal v0.4: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md`
- revised proposal v0.4 commit: `de66a18123059f76fd0ead4aa715f84ad066c62b`
- previous Critic result: `REVISE`
- previous Critic review repo path/commit: `NONE`
- only open blocker: `WC05-D7`
- execution branch/worktree: `NONE / NOT AUTHORIZED`

## 最小读取范围

先实际读取最新 `main` 的：

- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`，重点 §5 Feedback lifecycle
- `docs/plugin-todos/workflow-core.md`
- V0.3 Proposal
- V0.4 Proposal

不要重新审查已经关闭的 production design。

## 唯一复核对象：WC05-D7

最新 `CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md` §5 的 canonical TODO 合法 status vocabulary 是：

```text
NEW
PROJECT_LOCAL
CANDIDATE_GENERIC
PROMOTE_NOW
PROMOTED
BLOCKED_NEEDS_EVIDENCE
REJECTED
SUPERSEDED
```

请核对 V0.4 是否已经在**所有声明 canonical TODO 合法 vocabulary 的地方**完整保留这八项，尤其补回 `PROMOTED`。

同时确认：

1. `HISTORICAL_RESOLVED` 仍只属于 Maintenance Board bootstrap / coverage disposition，不是 canonical TODO `status:`。
2. V0.4 没有预先替 #5/#6/#11 决定最终 canonical status：
   - 已进入 active production 且已有回归时，`PROMOTED` 是合法候选；
   - 只有确实被另一机制取代时才考虑 `SUPERSEDED`；
   - evidence 不足时不得为了 closure 强制改状态。
3. #11 当前 `NEW / POST_056_REFINEMENT` 的非法复合 status 仍留给未来具有合法 maintenance mutation authority 的 triage/closure action 规范化；V0.4 design-only 没有修改 source。
4. #5/#6/#11 的 consumer classification、ADAPTING closure、五个 required consumers、N/A durable-reason、Resolution commit、Issue close -> DONE 规则与 V0.3 完全保持，不因 vocabulary 修正而改变。
5. V0.4 §15 已修正 next-step：下一轮只要求 Critic 复核 V0.4 的 `WC05-D7` closure，不再声称复核 V0.2 / WC05-D1–D6。
6. 当前仍没有 Project/Issue mutation、consumer adaptation、source-status mutation 或 Resolution commit；pending mutation 不得被解释为已经完成。

## 不得重新打开的范围

除非 V0.4 的 vocabulary 修正直接引入新回归，否则不要重新打开：

- `WC05-D1`–`WC05-D6`
- `WC05-D7.2`–`WC05-D7.5`
- workflow-core 0.5 三项 production change
- G1–G5
- #7/#8/#9/#10 production logic
- Bridge runtime / Host Policy
- Longleaf / STAT5060 / render specialist

## Scope / version boundary

继续保持：

```text
workflow-core = 0.4 / NO_BUMP
repository bump = NONE
execution branch/worktree = NONE / NOT AUTHORIZED
production implementation = NOT STARTED
paid API = NOT AUTHORIZED
```

本轮 PASS 仍然只代表 design closure，不授权实现、release、Project DONE、consumer adaptation 或任何机器 mutation。

## 输出要求

给出：

`RESULT = PASS` 或 `RESULT = REVISE`

如果 REVISE：

- 只允许围绕 `WC05-D7` vocabulary closure 或 V0.4 新引入的直接回归形成 blocker；
- 给稳定 finding ID、source、直接证据、因果风险、最小关闭条件和 owner；
- 按 Critic Role Contract 自动附完整 Planner prompt。

如果 PASS：

- 先用用户可读中文说明 `WC05-D7` 如何最终关闭；
- 明确 `WC05-D1`–`WC05-D7` 至此全部 CLOSED；
- 明确 PASS 只批准 V0.4 设计方向；
- 不批准实现、branch/worktree、version bump、release、Project DONE、consumer adaptation、Bridge/Longleaf mutation或 paid action；
- 下一步回 Planner，基于 approved V0.4 准备同一语义的 Proposal/Plan + Canonical Goal + Kickoff Draft execution package，再送 execution-ready Critic；
- 不要直接启动 Codex implementation。
