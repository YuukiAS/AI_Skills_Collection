# workflow-core 0.5 正常入口与执行路线可靠性 — Critic Re-review Prompt v0.3

你继续作为 AI Research Stack 的独立 Critic thread，对 `workflow-core / Verified Workflow 0.5` 做 **DESIGN_REVIEW_R3**。

这是对唯一剩余 blocker `WC05-D7` 的最小复核。  
上一轮 `WC05-D1`–`WC05-D6` 已明确 CLOSED；不要重新设计这些 production mechanisms，不要扩大 G1–G5，不要重新引入 #7/#8/#9/#10 专属逻辑。

不要实现代码，不要修改 production plugin，不要创建 execution branch/worktree，不要 bump version，不要启动 paid API，也不要修改 Longleaf `/users`、STAT5060、render specialist 或 Bridge Kit runtime。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `workflow-core`
- design_topic_or_task_key: `workflow-core--normal-entry-reliability`
- source_branch_or_ref: `main`
- review_stage: `DESIGN_REVIEW_R3`
- reviewed proposal v0.2: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_2_2026-09-30.md`
- reviewed proposal v0.2 commit: `8575e86fce56d0c44c484477f578e90b65750c5c`
- revised proposal v0.3: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_3_2026-10-01.md`
- revised proposal v0.3 commit: `3c33e160351b2c63d8b844af87f3fd7224f0b09a`
- previous Critic result: `REVISE`
- previous Critic review repo path/commit: `NONE`
- only open blocker: `WC05-D7`
- execution branch/worktree: `NONE / NOT AUTHORIZED`

## 先重新读取最新 main

至少实际读取：

- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/plugin-todos/workflow-core.md`
- V0.2 Proposal
- V0.3 Proposal

如需核实 #5/#6/#11 的 resolving evidence，再读取对应现有 evidence；不要用旧聊天摘要替代当前 source。

## 已关闭内容

以下 findings 已由上一轮 Critic 明确 CLOSED，本轮除非 V0.3 引入直接回归，否则不得重新打开：

- `WC05-D1`：trigger hard negative / final-candidate invocation trace
- `WC05-D2`：#8 只借 generic capability-discovery regression
- `WC05-D3`：#7 不进入 0.5 production behavior
- `WC05-D4`：#9 拆出
- `WC05-D5`：不可拆分 final-candidate normal-entry replay + true absent contrast
- `WC05-D6`：六项 fail-closed fallback equivalence

V0.3 没有修改三项 production change，也没有扩大 G1–G5。

## 唯一需要复核：WC05-D7

请逐项确认 V0.3 是否关闭 blocker。

### D7.1 Bootstrap disposition 与 canonical TODO status 已分离

V0.3 明确：

- `HISTORICAL_RESOLVED` 只属于 Maintenance Board §8 bootstrap / coverage disposition；
- 它不是 canonical TODO 合法 `status:`；
- canonical source status 只能来自现有 vocabulary：
  - `NEW`
  - `PROJECT_LOCAL`
  - `CANDIDATE_GENERIC`
  - `PROMOTE_NOW`
  - `BLOCKED_NEEDS_EVIDENCE`
  - `REJECTED`
  - `SUPERSEDED`
- closure action 必须按当时真实语义选择或保持合法 status，不能发明 `RESOLVED` / `HISTORICAL_RESOLVED` / 新 schema；
- #11 当前 `NEW / POST_056_REFINEMENT` 被识别为不属于当前合法 vocabulary，但 design-only 本轮没有顺手修改 source；后续合法 triage/closure action 必须规范化为一个现有合法值。

请判断这是否与当前 source ownership / status vocabulary 一致。

### D7.2 #5/#6/#11 consumer classification

V0.3 逐项判断：

- #5 = machine-consumed/shared mechanism：Bridge plugin replay / Host Policy + AI_Skills Executor normal consumption；
- #6 = shared maintenance mechanism：真实 maintenance batch / Reviewed Handoff / watcher 的启动、停止和 successor discipline；
- #11 = machine-consumed workflow：Bridge bootstrap/rematerialization + workflow-core consumer path。

因此三项 product-level `HISTORICAL_RESOLVED` 都**不能直接推出 Project DONE**。

请检查这些 classification 是否符合当前 `AI_SKILLS_MAINTENANCE_BOARD.md` 的 consumer-scope policy。若某项不属于，请给直接 source 证据；不要仅因“它是文档规则”就机械排除 machine consumption。

### D7.3 ADAPTING closure

V0.3 对三项都要求：

```text
central implementation complete
-> ADAPTING
-> freeze required consumer identities / locators
-> each required consumer PASS or justified N/A
-> durable evidence complete
-> Resolution commit
-> tracking Issue completed close
-> issue-closed workflow
-> DONE
```

并使用当前 Board policy 的默认 required logical consumers：

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`
4. `Workstation`
5. `Legion`

请确认：

- central implementation complete 以前不会提前进入 ADAPTING；
- 进入 ADAPTING 后会冻结 exact current identity / locator；
- 单台 PASS 不关闭 top-level Issue；
- DONE 必须等全部 required consumers PASS/N/A + durable evidence + Resolution commit + Issue close；
- 没有把 Critic PASS / product-level historical resolution 当成 DONE。

### D7.4 N/A 规则

V0.3 明确 N/A 只能有 durable frozen reason，不能因为临时不可达、离线、方便性或想快速收口而机械填 N/A。

请确认这满足 current Board policy。

### D7.5 No-tool pending mutation truth

当前 Planner surface 没有 Project mutation 能力，且没有可调用的 Clear Writing，因此 V0.3：

- 没有修改 Project；
- 没有关闭 #5/#6/#11；
- 没有写 Resolution commit；
- 没有实际做 consumer adaptation；
- 没有规范化 canonical source status；
- 只记录 exact pending mutation；
- 不要求用户手工拖 Project 或补 locator。

请检查 pending mutation 是否足够准确，并且没有伪称已同步。

## Scope / version 不变

本轮仍然：

```text
workflow-core = 0.4 / NO_BUMP
repository bump = NONE
execution branch/worktree = NONE / NOT AUTHORIZED
paid API = NOT AUTHORIZED
production implementation = NOT STARTED
```

不要要求本轮修改：

- workflow-core 0.5 三项 production change；
- G1–G5；
- Longleaf `/users`；
- STAT5060；
- render specialist；
- Bridge runtime / Host Policy；
- #7/#8/#9/#10 专属逻辑；
- production source；
- version；
- branch/worktree。

## 输出要求

给出：

`RESULT = PASS` 或 `RESULT = REVISE`

本轮只允许围绕 `WC05-D7` 及 V0.3 新引入的直接回归形成 blocker。不要移动已经关闭的 WC05-D1–D6 终点。

如果 REVISE：

- 每个 blocker 给稳定 finding ID；
- 对应 source；
- 直接证据；
- 因果风险；
- 最小关闭条件；
- owner；
- 按 Critic Role Contract 自动附完整 Planner prompt。

如果 PASS：

- 先用用户可读中文说明 `WC05-D7` 如何关闭；
- 明确 `WC05-D1`–`WC05-D7` 至此全部关闭；
- PASS 只批准 V0.3 设计方向；
- 不批准实现、branch/worktree、version bump、release、Project DONE、consumer adaptation、Bridge/Longleaf mutation或 paid action；
- 下一步回 Planner，基于 approved V0.3 准备同一版本语义的 Proposal/Plan + Canonical Goal + Kickoff Draft execution package，再送 execution-ready Critic；
- 不要直接启动 Codex implementation。
