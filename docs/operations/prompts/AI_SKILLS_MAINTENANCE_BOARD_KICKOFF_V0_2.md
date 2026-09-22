你现在执行 AI_Skills 维护看板与完成语义任务。只执行已经通过设计审查、并在 execution package v0.2 中冻结的范围，不重新设计 lifecycle。

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
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-22.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_2_2026-09-22.md`
- `docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_2.md`

我发送本 Kickoff，即明确授权以下 bounded effects：

1. 从 kickoff-time latest `origin/main` 创建 exact reviewed branch 和 exact sibling worktree；ordinary non-force commit/push 到该 task branch。
2. 在我的 GitHub 账号 `YuukiAS` 下创建或复用唯一 private Project `AI Skills Maintenance`，并只链接 `YuukiAS/AI_Skills_Collection`。
3. 创建/更新四状态 `TODO / DOING / ADAPTING / DONE`、`Area`、`Resolution commit`、最多四个批准 views，以及 approved built-in workflow / auto-add 配置。
4. 只创建/复用 `maintenance-track` tracking Issues，并按 Goal 的 bounded backfill 规则创建/更新 Project items；raw `NEW` 不批量转 Issue，不关闭 unrelated backfilled Issues。
5. 修改 Goal 明确允许的 AI_Skills 文档与 `results/repo--maintenance-board-lifecycle/**` evidence；不修改 plugin production source/generated payload/profile/Marketplace。
6. 如果 `project` OAuth scope 缺失，可以发起一次正常 bounded `gh auth refresh -s project`；若需要我完成 GitHub 一次性登录/授权，只向我提出这一项最小操作。
7. 如果当前 GitHub 官方接口仍只允许通过 Project Web UI 配置必要 built-in workflows，而当前 Executor 没有受支持的浏览器能力，可以向我提出一次最小 GitHub UI 操作；完成后自动继续同一 Goal。不要把它变成长期人工维护。
8. Stage A 完成并 push 后必须停止等待独立 implementation review。独立 Reviewer PASS 后，在同一 Goal、scope 不变且 latest-main 无语义冲突时，已授权 ordinary non-force main integration、remote main verification、设置本任务 `Resolution commit`、关闭**本任务自身** tracking Issue 为 completed，并验证 Project 自动进入 DONE；不得因进入这个已冻结阶段再次索取同一授权。

## 看板必须给人看

所有 tracking Issue title 和顶部摘要必须是自然、简洁、面向人的表达。

每个 Issue 顶部至少保留：

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

task key、hash、branch、路径、内部状态串只能作为 locator，不能拿来代替人类说明或充当标题主体。

每个 DOING / ADAPTING item 至少有一个当前有效执行锚点。Board / By area 至少直接显示 human-readable title + Area + Status。History 中 DONE item 直接显示 Resolution commit。

## Codex 修改 Kanban 文字必须使用 Clear Writing

只要你创建或修改以下 reader-facing board text：

- tracking Issue title；
- “问题 / 当前进度 / 当前执行锚点 / 下一步”；
- board card reader-facing copy；
- closure / History 的人类可读说明；
- backfill 新建或实质重写的 tracking Issue copy；

你必须在 GitHub mutation 前显式调用当前安装的 Clear Writing（`writing-style`）做最终语言层处理。

Clear Writing 不得改变 Status、Area、required downstream targets、proposal/task/branch/PR/commit locator、Resolution commit 或 evidence meaning。

如果当前 Codex runtime 无法真正调用 Clear Writing：

- 不得假装调用；
- 不得批量写 generic board copy；
- 在 reader-facing board text mutation 前停止，并报告 `CLEAR_WRITING_UNAVAILABLE`，等待同一 Goal 的最小恢复。

最终仍要由独立 Reviewer 看真实 GitHub Project / Issue surface；`CLEAR_WRITING_USED=YES` 不能代替可读性判断。

## Planner / Critic / GPT 主动同步规则必须落地

本任务实现的 canonical board doc + AGENTS locator 必须明确：

- raw `NEW` 仍只进 plugin TODO inbox；
- Planner triage 后进入 tracking scope -> 主动 create/bind Issue + 设置真实初始状态；
- Planner 开始实质 design/implementation -> 主动 reconcile DOING + current proposal/task/workflow anchor；
- Critic 每轮 review -> 主动更新 review locator、next action、lifecycle truth；PASS/REVISE 不机械改状态；
- core 已集成、required downstream 未完成 -> 当前 owner 主动改 ADAPTING；
- final DONE 仍只按 approved closure contract；
- routine sync 不向用户索权，也不要求用户手工拖卡；
- 如果当前 GPT surface 没有 Project mutation 能力，它仍是语义 owner：先更新自己能更新的 Issue evidence/summary，并在 handoff 中生成 exact pending Project mutation，交下一有权限的 Executor机械完成；不得说“请用户自己改看板”，也不得谎称已同步。

你作为 Codex/Executor 在做任何新的 board mutation 前，应先消费 handoff 中仍然有效的 pending Project mutations。

## BOARD-01 必须保持关闭

- lifecycle item 只能是 `maintenance-track` Issue；
- auto-add 至少 `is:issue label:maintenance-track`；
- implementation/design PR 不作为 lifecycle item；
- Project `pull request merged -> Done` 必须 disabled；
- DONE 前，中间 PR 不得使用会 auto-close tracking Issue 的 Development/manual link；
- PR body / commit message 不得对 tracking Issue 使用 `close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved`；
- repository-wide auto-close 保持不变；
- `issue closed -> Done` 只作为完整 DONE checklist 后最后机械动作；
- rejected/superseded/duplicate/not-planned item 先从 Project remove/archive，再 truthful close，不显示为 DONE。

## 验收必须看真实 Project surface

除了 API/字段/readback，还必须对真实 GitHub surface 做 qualitative review：

- Board；
- By area；
- 本任务 tracking Issue；
- 本轮所有新建/实质重写 tracking Issue 的 title + top summary。

Reviewer 必须判断用户是否无需解析 task key/hash/path，就能直接看懂：

- 什么问题；
- 哪个 plugin / Area；
- 当前 Status；
- 当前执行锚点；
- 下一步。

不能只靠字段存在、关键词、字数、API receipt 或 Clear Writing 调用记录 PASS。

如果 exact worktree 无法合法创建、GitHub Project 身份/权限不符、Clear Writing 无法调用、Project workflow 无法验证、出现语义 main drift，或者动作需要 Bridge Kit、server/Host、paid API、force/destructive Git、Project publication、GitHub Action/database/registry/ledger/controller/watcher 等未授权 scope，停止并给出精确 blocker；不得换路径、换分支、用 `/tmp`、扩大权限或静默降级。

本任务不 bump repository/plugin version。Project 默认 PRIVATE，因此 README 必须按 Goal 做 closure check，预期 `README checked: no update required`，除非执行改变 public entry。

最终只有 Goal 中全部结构、BOARD-01、BOARD-UX-01、BOARD-SYNC-01、Clear Writing、真实 surface review、bounded backfill、独立 implementation review、main integration、Resolution commit、tracking Issue completed close 与 Project DONE 全部成立，才能报告 overall achieved。
