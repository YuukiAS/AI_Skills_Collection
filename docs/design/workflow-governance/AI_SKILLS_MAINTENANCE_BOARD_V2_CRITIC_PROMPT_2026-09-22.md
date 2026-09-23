# AI Skills 维护看板与完成语义 — Critic Prompt v2

你是 AI Research Stack 的独立 Critic thread。

当前只复核 Planner 对上一轮唯一 stable blocker `BOARD-01` 的返修；不要重新扩大审查范围，不实现、不创建 GitHub Project、不创建/迁移 Issue、不执行 backfill、不启动 Codex、不调用 paid API、不修改 production/server/Host/Bridge Kit。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = DESIGN_PROPOSAL_REVISION_REVIEW
proposal_path_and_version = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md v2
proposal_commit = da46f14141888c1bcd94bf94a486bcb1a1b0ec7c
previous_proposal = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_PROPOSAL_2026-09-22.md
previous_proposal_commit = e9804daf12611788f98d9ab3c2577c7744963c03
previous_critic_review = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_CRITIC_REVIEW_2026-09-22.md
previous_critic_review_commit = 471ecfa585f66e7b792a6dc29008b6116b5354df
stable_blocker_to_recheck = BOARD-01
execution_branch/worktree = NONE
```

## 必须先实际读取

最新 `main`：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_CRITIC_REVIEW_2026-09-22.md`

v1 Proposal 只在需要对比 BOARD-01 改动时读取，不重新从零审整套架构。

## 本轮 Planner disposition

```text
BOARD-01 = ACCEPT
NEW_BLOCKERS_FOUND_BY_PLANNER = NONE
```

v2 保留上一轮 Critic 已认可的主设计：

```text
TODO -> DOING -> ADAPTING -> DONE
```

并保留：

- Project item = top-level idea；
- plugin TODO = failure/evidence/maturity inbox；
- Planner–Critic / Reviewed Handoff / Executor task = 某一轮执行证据；
- WAITING/BLOCKED 不成为主状态；
- Resolution commit = owner repo canonical closure/evidence commit；
- optional post-DONE consumer 默认形成新的 follow-up item；
- 一次性 Project bootstrap 与长期 CLI maintenance 分离。

除非发现新的直接证据证明这些已认可部分会产生用户可见错误，不要重新移动终点。

## BOARD-01 的 v2 修复

上一轮 blocker 是：

> central implementation/design PR 可能因为 GitHub linked relationship / closing keyword 自动关闭 top-level tracking Issue，随后 Project 的 issue-closed -> Done 造成 required adaptation 未完成却假 DONE。

v2 现在明确：

1. top-level lifecycle item 只能是专用 tracking Issue；
2. Project auto-add 使用：
   `is:issue label:maintenance-track`
3. implementation/design PR 不作为 lifecycle item；
4. 关闭 Project 默认的：
   `pull request merged -> Done`
5. top-level tracking Issue 真正达到 DONE 前，中间 PR 不得通过 GitHub Development/manual linked relationship 形成 merge 后自动关闭该 tracking Issue 的关系；
6. PR body 和 commit message 都不得对该 tracking Issue 使用 `close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved` closing keywords；
7. 需要关联时只用普通非关闭 reference，并把 task/PR/commit locator 写回 tracking Issue；
8. 不全仓关闭 repository-level linked-PR auto-close；
9. `issue closed -> Done` 保留，但只有在 required adaptation、normal-entry/real-consumer evidence、durable runtime evidence、Resolution commit 与其他 completion checklist 全部满足后，才主动 close tracking Issue。

## 独立外部核查

必须再次用 GitHub 官方当前文档独立核实 BOARD-01 所依赖的现实：

- GitHub Projects built-in automation 默认是否包含 pull request merged -> Done / closed -> Done；
- auto-add 是否支持 `is:issue` + `label:`；
- linked PR merge default branch 是否会 auto-close Issue；
- closing keywords 是否会建立/触发关闭关系；
- closing keywords 是否也可能来自 commit message；
- repository-level auto-close 是否可以全局关闭，以及为什么本设计不需要这样做；
- `gh project` / `gh project item-edit` / `gh project item-list` 是否足以支撑稳态维护。

优先使用：

- `docs.github.com`
- `cli.github.com`

不要只引用 Planner 的结论。

## 你本轮必须回答

1. BOARD-01 是否已经被 v2 的最小 GitHub-native 防线关闭？
2. 是否还存在一条现实路径，使中间 PR merge 在 required adaptation 未完成时把 top-level tracking Issue 自动关闭 / Project 置 DONE？
3. v2 是否错误地扩大为全仓禁用 auto-close？如果没有，确认 blast radius 仍是 tracking Issue discipline。
4. `issue closed -> Done` 作为最后机械动作是否仍安全？
5. Planner 吸收的两个 non-blocking clarification 是否正确且没有引入新复杂度？
6. 是否出现由 v2 修订本身引入的新的真实 blocker？

如果 BOARD-01 已关闭且没有新的直接风险，应 PASS；不要因为“还可以更保险”新增 blocker。

## 期望输出

先用自然中文说明：

- BOARD-01 如何关闭；
- 四状态是否继续成立；
- DONE 的最终边界；
- 这次 PASS（若有）证明什么、不证明什么。

然后给：

```text
RESULT = PASS | REVISE
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md
REVIEWED_PROPOSAL_COMMIT = da46f14141888c1bcd94bf94a486bcb1a1b0ec7c
REVIEW_STAGE = DESIGN_PROPOSAL_REVISION_REVIEW
RECHECKED_BLOCKERS = BOARD-01
```

如果 `REVISE`：

- 优先复核 BOARD-01；
- 新 blocker 只能来自新事实、先前遗漏的直接关键风险或 v2 引入的真实回归；
- 每个 blocker 给稳定编号、直接证据、因果风险和最小关闭条件；
- 按 Critic Role Contract 自动生成完整 Planner返修 prompt。

如果 `PASS`：

- 明确只批准 v2 设计；
- 不授权创建 Project、改 Issue、改 AGENTS/TODO、做 backfill 或执行任何 production/server/Host/Bridge 变更；
- 下一步回 Planner 准备最小 execution package；
- 按 Critic Role Contract 自动生成完整 Planner prompt。

## Review 文件授权

用户若把本 prompt 原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`

并 ordinary non-force push。

除此之外禁止修改：

- Proposal；
- AGENTS；
- TODO；
- plugin source；
- GitHub Project / Issue；
- Bridge Kit；
- 任何其他 repo；
- production/server/Host。

提交后报告 exact commit。
