# AI Skills 维护看板 — Execution Critic Review v0.1

- 日期：2026-09-22
- Review stage：`EXECUTION_READY_REVIEW`
- Result：`REVISE`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- package version：`v0.1`
- package snapshot commit：`6adc5fcf1738235e4c5fe0b81e2ee1369e1bef2f`
- execution branch：`reviewed/repo--maintenance-board-lifecycle`
- execution worktree：`../AI_Skills_Collection-repo--maintenance-board-lifecycle`
- approved design：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`
- design PASS：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`

## 1. 结论

v0.1 package 的技术执行路线总体可行，而且保持了已批准的四状态设计与 `BOARD-01` 防线。但本轮用户明确补充了两个直接面向实际使用的要求，而 v0.1 还没有把它们冻结成 execution contract，因此当前不能给 `READY_FOR_CODEX=YES`：

1. 这个 Project 是给人看的，必须符合 Clear Writing 的可读性标准，不能只做到字段/Issue/状态“结构正确”；
2. 后续 Planner / Critic / 真实项目 thread 在处理 AI_Skills TODO 时必须主动维护 tracking/status/evidence，不应等用户每次提醒，也不能把状态维护理解成 Codex-only 责任。

这两项都不是重做 lifecycle，也不要求新增状态、数据库、GitHub Action 或 daemon；只需把现有 UI/Issue contract 和角色消费规则补完整。

## 2. Package 已通过的部分

### GitHub bootstrap 路线真实存在

独立核对当前 GitHub 官方文档后，Plan 引用的主要接口均真实存在：

- `gh project create/edit/link/field-create/field-list/item-add/item-edit/item-list`；
- `gh project` 最低需要 `project` token scope；
- GraphQL `updateProjectV2Field` 可更新 single-select options；
- GraphQL `createProjectV2View` / `updateProjectV2View` 当前存在；
- `ProjectV2.workflows` / `ProjectV2Workflow.enabled` 可用于 readback workflow 状态。

当前公开 `gh project` 没有 package 所假定之外的“view-create/workflow-enable”专用命令；package 没有虚构这些 CLI。

GitHub 官方当前仍把 built-in workflow / auto-add 的配置入口写成 Project Web UI。Projects GraphQL 当前有 workflow readback 和 delete mutation，但没有文档化的 enable/disable/update workflow mutation，因此 UI fallback 是诚实的。

### HUMAN_ONLY UI action 合法

当前仓库已发布的 056/Human-Gate 语义要求：只有真正不可代理的登录/授权/物理/用户决策才进入 HUMAN_ONLY；用户动作后必须在同一 Goal 自动 resume。

因此“当前 Executor 没有 browser，而 GitHub 仍只提供 Web UI 配置这一必要 workflow”时，提出一次最小 UI action，然后自动 resume，符合现有合同。没有证据支持为了这一个 bootstrap dependency 新增 GitHub Action、service 或同步 daemon。

### Exact branch/worktree 处理正确

Package 对 exact branch/worktree 的处理忠实于当前 AGENTS：

- exact semantic task branch；
- exact sibling worktree；
- 先解析 absolute path；
- Host/sandbox 不支持则在外部 Project/Issue mutation 前 fail closed；
- 不允许 `/tmp`、dirty checkout、alternate branch/path；
- 未来若已有 sanctioned Bridge primitive，只允许它执行同一 exact locator。

当前 main 有历史 evidence 说明某些 Host sandbox 曾阻止 sibling worktree，但没有直接证据证明本任务未来 normal Executor 环境必然失败。因此这是 execution condition，不是当前 blocker。

### BOARD-01 仍然关闭

Package 保留了：

- issue-only admission；
- `is:issue label:maintenance-track`；
- PR lifecycle exclusion；
- Project `pull request merged -> Done` disabled；
- DONE 前禁止 auto-closing link / closing keywords；
- repository-wide auto-close 不变；
- final `issue closed -> Done` 只作最后机械动作。

新增“REJECTED/SUPERSEDED/not-planned 先从 Project remove/archive，再 truthful close”只是非完成终止路径的 implementation-level 补全，不是第五状态，也没有重开 lifecycle 设计。

### Backfill、version、README 边界合理

Bounded backfill 没有把 raw `NEW` 全部复制成 Issue；它只收 triage 后有效候选、active work 和明确 ADAPTING work，duplicate/ownership ambiguity 则 skip + report。

版本政策也支持：

```text
Repository bump decision: NONE
Affected plugins: all NO_BUMP
```

因为本任务只改变 maintenance docs + GitHub Project metadata，不改变 install/runtime/plugin production behavior。

Project 为 PRIVATE 时，默认 `README checked: no update required` 也合理；若执行时 public entry 改变再更新 README。

## 3. Stable blockers

### BOARD-UX-01 — 人类可读看板质量没有进入验收合同

**用户要求**

用户当前明确要求：这个看板是给自己看的，必须符合 Clear Writing 标准；要能清楚分辨每个 plugin 有哪些 TODO，DOING/DONE 时要能看出对应 workflow / task / PR / commit 等实际锚点，不能只是 AI 生成的字段和技术垃圾。

**直接证据**

当前 Plan 已有：

- `Area`；
- `Board / Active / By area / History`；
- tracking Issue body 中的 task/PR/commit locator；
- DONE 的 `Resolution commit`。

但 B1–B5 只验证结构、filter、backfill fidelity 与 docs locator，没有验证：

- tracking Issue title / top summary 是否是自然、简洁、面向人的表达；
- Board / By area 是否真的让用户一眼分清每个 plugin 的条目；
- DOING / ADAPTING item 是否有一个当前有效 workflow/task/PR/commit locator，而不是一堆历史 locator；
- 实际 Project 页面是否存在内部 task key、长路径、状态字段堆砌导致的可读性退化。

因此 package 可能“机械 PASS”但仍产生用户明确不要的 AI 垃圾看板。

**因果风险**

这是最终用户直接消费的 artifact。如果只验证 API/字段存在，用户仍需要点开多个 Issue、自己解释 task key/commit/history，无法达到“看板一眼看懂”的目标。

**最小关闭条件**

Planner v0.2 不需要新增 Project 字段或状态，只需补一个 human-facing contract：

1. tracking Issue title 使用自然、简洁的人类语言；task key/hash/path 不作为标题主体；
2. Issue 顶部固定保留短的“问题 / 当前进度 / 当前执行锚点 / 下一步”，详细 evidence 放后面；
3. 每个 DOING / ADAPTING item 至少有一个**当前有效**的 proposal/task/workflow/branch/PR/commit locator；
4. DONE item 必须有 Resolution commit；History 直接显示；
5. Board / By area 实际视图必须让用户看到清楚的 title + Area(plugin) + Status；每个有 tracked items 的 plugin/Area 都能直接过滤或分组查看；
6. B1/B4/B5 增加实际 Project surface 的 Clear-Writing 可读性检查：不以字段存在、字符串扫描代替人类可读性判断。

不要求新增 `Current workflow` Project field；现有 Issue contract + view 配置足以实现。

### BOARD-SYNC-01 — Planner/Critic/GPT 的主动状态维护责任仍未冻结

**用户要求**

用户当前明确要求：以后新增/triage TODO，以及 Planner/Critic 工作时，应主动推进或核对状态，不应每次由用户提醒；这不是 Codex-only 责任，GPT 也必须知道并执行。

**直接证据**

当前 Plan §11 只说 canonical board doc 拥有“steady-state Planner/Codex commands”，AGENTS 拟新增的规则主要是：

- triage 后才用 Project；
- 不因 task/PR/integration PASS 标 DONE；
- follow board doc；
- 不使用 early-closing relationship。

Plan §13 虽然写了 Planner/maintainer 会 `TODO -> DOING -> ADAPTING`，但没有冻结“每次 Planner/Critic handoff 必须自动 reconcile tracking Issue / status / evidence”的消费规则；Critic 目前被定义为“检查”，而不是主动同步 evidence/status。

当前 ChatGPT GitHub connector 也没有 Projects mutation action，因此如果不规定无工具时的合法 handoff 行为，实际使用很容易再次变成“用户提醒 Codex 去同步”。

**因果风险**

看板会在真实 Planner/Critic 工作后漂移，用户看到的状态滞后；最终又需要用户自己记得说“把这个改成 DOING/ADAPTING”，直接违背本任务减少人工维护的目标。

**最小关闭条件**

Planner v0.2 把以下规则写进拟新增的 canonical board doc，并在 AGENTS 用一条简短 mandatory locator/consumer rule绑定所有 AI_Skills maintenance threads：

1. 真实项目 thread 新增 raw `NEW` 时仍只写 inbox，不自动建 Project item；
2. Planner triage 后如果条目进入 tracking scope，必须自行 create/bind tracking Issue，并设置真实初始状态；
3. Planner 开始实质 design/implementation round 时自动 reconcile 为 DOING，并写入当前 proposal/task/workflow locator；
4. Critic 每次 review 必须主动 reconcile tracking Issue 的 review locator、next action 和 lifecycle truth；Critic PASS/REVISE 本身不机械改状态，只有语义条件变化才改；
5. canonical core 落地且 required downstream 未完时，由当前 owner 自动改为 ADAPTING；
6. final DONE 仍只按批准的 closure contract执行；
7. routine board sync 不向用户索权/提醒；如果当前 GPT surface没有 Project mutation能力，GPT 仍是语义 owner：必须在自己的 handoff 中生成 exact pending Project mutation，并让下一有权限的 Executor/maintenance action机械执行，不得把“请用户手工改看板”作为默认路径；
8. implementation acceptance 至少证明这套角色消费规则已进入 AGENTS + canonical board doc，而不是只存在于本 task Goal。

这不要求新增 controller/watcher/Action，也不要求 Critic 在没有工具时伪装已更新 Project。

## 4. 非阻塞判断

- GitHub API/CLI route：可执行。
- UI-only built-in workflow dependency：有合法 HUMAN_ONLY recovery，不是 blocker。
- exact sibling worktree：fail-closed 条件合理，目前无证据证明必然不可执行。
- bounded GitHub side effects：scope 合理；同一 frozen scope 已在 Kickoff 一次授权，Stage C 不应再次索权。
- backfill：既没有 raw-NEW 垃圾山复制，也没有明显漏掉当前 active maintenance idea。
- B1–B6：真实 Project/API evidence 方向正确；修复 BOARD-UX-01 后需补 actual human-facing surface review。
- version / README：NONE / NO_BUMP + private README no-update 默认合理。

## 5. 审查结论

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW
REVIEW_OBJECTS =
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_1_2026-09-22.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_1.md
- docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_1.md
PACKAGE_SNAPSHOT_COMMIT = 6adc5fcf1738235e4c5fe0b81e2ee1369e1bef2f
READY_FOR_CODEX = NO
STABLE_BLOCKERS =
- BOARD-UX-01
- BOARD-SYNC-01
```

本轮没有重新打开 `BOARD-01`，也没有要求重做四状态设计。只需把用户刚明确的“人看得懂”和“GPT 自己维护状态”补进 execution package，再做一次 execution-ready 复核。
