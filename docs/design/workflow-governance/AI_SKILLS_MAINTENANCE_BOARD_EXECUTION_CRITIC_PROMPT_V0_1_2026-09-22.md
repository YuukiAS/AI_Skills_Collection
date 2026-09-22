# AI Skills 维护看板 — Execution-ready Critic Prompt v0.1

你是 AI Research Stack 的独立 Critic thread。

当前设计阶段已经 PASS。现在只审 execution package 是否忠实实现已批准设计、是否足够小、是否真实可执行、是否把授权和恢复边界写清。不要重新设计 lifecycle，不创建 GitHub Project、不创建/迁移/关闭 Issue、不做 backfill、不启动 Codex、不调用 paid API、不修改 production/server/Host/Bridge Kit。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = EXECUTION_READY_REVIEW
package_version = v0.1
execution_branch = reviewed/repo--maintenance-board-lifecycle
execution_worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
package_snapshot_commit = 6adc5fcf1738235e4c5fe0b81e2ee1369e1bef2f
```

## 已批准设计

Proposal：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`

commit：

`da46f14141888c1bcd94bf94a486bcb1a1b0ec7c`

Design Critic PASS：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`

commit：

`8213c843b4d91c63f6de62740e26ef8d215a59e0`

previous blocker：

```text
BOARD-01 = CLOSED
```

不要重新打开 BOARD-01，除非 execution package 本身重新引入了同一真实风险。

## 本轮必须审的同版 execution package

### Implementation Plan v0.1

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_1_2026-09-22.md`

### Canonical Goal v0.1

`docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_1.md`

### Kickoff Draft v0.1

`docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_1.md`

三件套在 package snapshot commit：

`6adc5fcf1738235e4c5fe0b81e2ee1369e1bef2f`

同时读取最新 main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

只按需要读取 `TODO.md` / `docs/plugin-todos/README.md` 核对允许修改范围；不要重新全量审 plugin source。

## 已冻结的 lifecycle 语义必须保持

```text
TODO -> DOING -> ADAPTING -> DONE
```

以及：

- Project item = top-level tracking Issue；
- plugin TODO = failure/evidence/maturity inbox；
- Planner–Critic / Reviewed Handoff / Executor task = execution evidence；
- WAITING/BLOCKED 不是主状态；
- Resolution commit = owner repo canonical closure/evidence commit；
- optional post-DONE consumer -> new follow-up item，除非新证据证明旧 claim 原本不成立；
- one-time bootstrap 与 steady-state CLI maintenance 分离。

## BOARD-01 必须继续关闭

execution package 当前规定：

1. lifecycle item 只允许 `maintenance-track` tracking Issue；
2. auto-add 至少 `is:issue label:maintenance-track`；
3. implementation/design PR 不作为 lifecycle item；
4. Project `pull request merged -> Done` disabled；
5. DONE 前不建立会 merge-auto-close tracking Issue 的 Development/manual link；
6. PR body / commit message 不使用 targeting tracking Issue 的 closing keywords；
7. 中间 task/PR/commit 只用非关闭 reference；
8. 不全仓关闭 repository-level auto-close；
9. `issue closed -> Done` 只做完整 DONE checklist 后最后机械动作；
10. 若 admitted item 后来 REJECTED/SUPERSEDED/not-planned，先从 Project remove/archive，再 truthful close，不能显示成 DONE。

请确认第 10 条是对四状态语义的 implementation-level补全，而不是偷偷新增第五状态或重开设计。

## 重点审查 1：真实 GitHub bootstrap 路线

Plan 不假设不存在的 CLI 子命令。

当前 package 明确：

- project/create/edit/link、field-create/list、item-add/edit/list -> `gh project`；
- default Status option replacement -> documented GraphQL `updateProjectV2Field`；
- views -> documented Projects API / GraphQL `createProjectV2View/updateProjectV2View`；
- built-in Project workflow enable/disable / auto-add config -> 当前官方文档支持的 Project Web UI；如果未来执行时出现正式等价 mutation API，可以按同一批准语义使用；
- Project workflows -> GraphQL readback 验证 names/enabled state；
- `gh project` token 需要 `project` scope。

请独立核查 GitHub 官方当前文档，重点回答：

1. Plan 是否引用了真实存在的 CLI/API；
2. 是否仍有不存在的 `gh project` 命令；
3. built-in workflow 配置的 UI-only fallback 是否诚实且足够；
4. 如果 Executor 无 browser，允许一次 HUMAN_ONLY UI action、完成后自动 resume，是否符合当前 056/Human Gate contract；
5. 是否应因为这一个 bootstrap UI dependency 就新增自动化服务/Action（默认答案应基于证据，不追求更复杂）。

优先官方：
- `docs.github.com`
- `cli.github.com`

## 重点审查 2：exact branch/worktree 是否可执行

冻结：

```text
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
```

Plan 规定：

- relative locator 从 canonical repo root 唯一解析；
- 解析后的 absolute path 先写 evidence；
- 若 Host/sandbox 无法合法创建 exact worktree，在任何 Project/Issue mutation 前停止；
- 不允许 `/tmp`、dirty checkout、alternate path、alternate branch；
- 若执行时已有 sanctioned Bridge-owned bounded primitive，可以只用来执行同一 exact locator，不改本任务语义。

请检查这是否忠实遵守当前 AGENTS，且没有靠文字假装 Host capability 已存在。

如果你认为当前 main 已经有直接证据证明这个 exact worktree 在正常 Executor 环境必然不可执行，请用该新事实形成 blocker；否则不要因为历史曾出现过 sandbox gap 就预设未来执行一定失败。

## 重点审查 3：bounded GitHub side effects

Kickoff 未来一旦由用户原样发送，授权：

- create/reconcile one private Project under `YuukiAS`;
- link only AI_Skills repo；
- fields/views/workflows；
- `maintenance-track` label；
- bounded tracking Issues/backfill；
- current task Issue final close only；
- exact allowed repo docs/results；
- ordinary non-force task-branch push；
- after independent implementation review PASS and no semantic main drift, ordinary non-force main integration + current task Resolution commit + current task completed close。

禁止：

- unrelated Issue close；
- public Project；
- plugin runtime；
- Bridge/server/Host；
- paid API；
- GitHub Action/database/registry/ledger/controller/watcher；
- force/history rewrite；
- arbitrary branch/worktree；
- repository-wide auto-close disable。

检查授权是否过宽/过窄，尤其是否会造成后续重复向用户索取同一 frozen scope。

## 重点审查 4：bounded backfill

只允许 current-main one-pass snapshot：

include：
- CANDIDATE_GENERIC
- PROMOTE_NOW
- still-valid BLOCKED_NEEDS_EVIDENCE
- active Planner–Critic / Reviewed Handoff work not otherwise represented
- core integrated + explicitly required downstream incomplete

exclude：
- raw NEW
- PROJECT_LOCAL
- REJECTED
- SUPERSEDED
- ordinary project-specific TODO
- historical completed items unless specific retrieval need

duplicate/ownership ambiguity -> skip + report，不猜。

请检查是否会把 TODO 垃圾山复制成 Issue 垃圾山，或是否过窄到漏掉用户真正正在做的维护 idea。

## 重点审查 5：验证是否证明真实能力

Execution gates B1–B6 应证明：

- actual Project structure；
- actual workflow enabled states / exact auto-add filter；
- live self-hosting tracking Issue normal entry；
- no PR lifecycle items；
- real CLI/API item update；
- one-pass backfill fidelity；
- repo doc consumption；
- no production plugin/version change；
- independent implementation review；
- final main integration；
- Resolution commit；
- current tracking Issue completed close；
- actual Project DONE。

检查是否仍用 Markdown/关键词替代真实 Project behavior。

## 重点审查 6：version / README / completion

Package 当前决定：

```text
Repository bump decision: NONE
Affected plugins: all NO_BUMP
```

原因：maintenance docs + GitHub Project metadata，不改变 install/runtime/plugin production。

Project 默认 PRIVATE，因此 README 预期：
`README checked: no update required`
除非执行时改变 public entry。

请按当前 version policy 核实。

## 需要特别判断的 execution-level issue

Planner 没有把下面两项视为 blocker，但请独立判断：

1. built-in workflow configuration 可能需要一次 UI-only HUMAN_ONLY action；
2. exact sibling worktree 在某些 Host sandbox 上可能被禁止，但 Plan 要求 mutation 前 fail closed。

如果这两项已有合法恢复路径且不改变设计，应作为 bounded execution condition，而不是架构 REVISE；如果其中任何一个实际让 Goal 无法完成，则给稳定 blocker。

## 输出要求

如果 package 需要实质修改：

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW
REVIEW_OBJECTS =
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_1_2026-09-22.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_1.md
- docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_1.md
PACKAGE_SNAPSHOT_COMMIT = 6adc5fcf1738235e4c5fe0b81e2ee1369e1bef2f
READY_FOR_CODEX = NO
```

Stable blocker 必须有直接证据、因果风险、最小关闭条件。然后按 Critic Role Contract 自动生成完整 Planner返修 prompt。

如果 package 可以执行：

先用自然中文说明：

- v0.1 package 如何忠实实现 approved v2；
- BOARD-01 如何在 execution contract 中保持关闭；
- bootstrap / steady-state 分工；
- exact branch/worktree、GitHub effects、backfill、version/README 边界是否合格；
- PASS 证明什么、不证明什么。

然后必须按 Critic Role Contract 输出：

```text
RESULT = PASS
REVIEW_STAGE = EXECUTION_READY_REVIEW
PACKAGE_SNAPSHOT_COMMIT = 6adc5fcf1738235e4c5fe0b81e2ee1369e1bef2f
APPROVED_PROPOSAL_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_1_2026-09-22.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_1.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_1.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
```

并逐字输出已审过的 Kickoff 正文；不要 PASS 后另写一个语义不同的新 prompt。

## Review 文件授权

用户若把本 prompt 原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-22.md`

并 ordinary non-force push。

除此之外禁止修改：

- Proposal / Plan / Goal / Kickoff；
- AGENTS/TODO/README；
- Project/Issue；
- plugin source；
- Bridge Kit；
- server/Host；
- 任何其他 repo。

提交后报告 exact review commit。
