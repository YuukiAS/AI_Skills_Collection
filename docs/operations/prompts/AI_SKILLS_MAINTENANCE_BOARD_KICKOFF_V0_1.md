你现在执行 AI_Skills 维护看板与完成语义任务。只执行已经通过设计审查、并在 execution package v0.1 中冻结的范围，不重新设计。

Repository:
`YuukiAS/AI_Skills_Collection`

Exact task identity:

```text
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
```

必须读取并遵守：

- `AGENTS.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_1_2026-09-22.md`
- `docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_1.md`

我发送本 Kickoff，即明确授权以下 bounded effects：

1. 从 kickoff-time latest `origin/main` 创建 exact reviewed branch 和 exact sibling worktree；ordinary non-force commit/push 到该 task branch。
2. 在我的 GitHub 账号 `YuukiAS` 下创建或复用唯一的 private Project `AI Skills Maintenance`，并只链接 `YuukiAS/AI_Skills_Collection`。
3. 创建/更新该 Project 的四状态 `TODO / DOING / ADAPTING / DONE`、`Area`、`Resolution commit`、批准的最多四个 views，以及 approved built-in workflow / auto-add 配置。
4. 只创建/复用 `maintenance-track` tracking Issues，并按 Goal 的 bounded backfill 规则创建/更新 Project items；不得把 raw `NEW` 批量转成 Issue，不得关闭 unrelated backfilled Issues。
5. 修改 Goal 明确允许的 AI_Skills 文档与 `results/repo--maintenance-board-lifecycle/**` evidence；不修改 plugin production source/generated payload/profile/Marketplace。
6. 如果 `project` OAuth scope 缺失，可以发起一次正常的 `gh auth refresh -s project`；若需要我完成 GitHub 的一次性登录/授权，只向我提出这一项最小操作。
7. 如果当前 GitHub 官方接口仍只允许通过 Project Web UI 配置 built-in workflows，而当前 Executor 没有受支持的浏览器能力，可以向我提出一次最小 GitHub UI 操作；完成后自动继续同一 Goal。不要把它变成长期人工维护。
8. Stage A 完成并 push 后必须停止等待独立 implementation review。独立 Reviewer PASS 后，在本同一 Goal、scope 不变且 latest-main 无语义冲突时，已授权 ordinary non-force main integration、remote main verification、设置本任务 `Resolution commit`、关闭**本任务自身** tracking Issue 为 completed，并验证 Project 自动进入 DONE；不需要因为到达这个已冻结阶段再次向我索取同一授权。

BOARD-01 必须保持关闭：

- lifecycle item 只能是 `maintenance-track` Issue；
- auto-add 至少是 `is:issue label:maintenance-track`；
- implementation/design PR 不作为 lifecycle item；
- Project `pull request merged -> Done` 必须 disabled；
- DONE 前，中间 PR 不得对 tracking Issue 使用会 auto-close 的 Development/manual link，也不得在 PR body 或 commit message 使用 `close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved` closing keywords；
- repository-wide auto-close 不得关闭；
- `issue closed -> Done` 只能作为完整 DONE checklist 后的最后机械动作。

如果 exact worktree 无法合法创建、GitHub Project 身份/权限不符、Project workflow 无法验证、出现语义 main drift，或者动作需要 Bridge Kit、server/Host、paid API、force/destructive Git、Project publication、GitHub Action/database/registry/ledger/controller/watcher 等未授权 scope，停止并给出精确 blocker；不得换路径、换分支、用 `/tmp`、扩大权限或静默降级。

本任务不 bump repository/plugin version。README 必须按 Goal 做 closure check。

最终只有 Goal 中所有条件、独立 review、main integration、Resolution commit、tracking Issue completed close 和 Project DONE 全部成立，才能报告 overall achieved。
