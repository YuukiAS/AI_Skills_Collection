# AI Skills 维护看板与完成语义 — Critic Review v2

- 日期：2026-09-22
- Review stage：`DESIGN_PROPOSAL_REVISION_REVIEW`
- Result：`PASS`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- human label：AI Skills 维护看板与完成语义
- source branch/ref：`main`
- reviewed proposal：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md` v2
- reviewed proposal commit：`da46f14141888c1bcd94bf94a486bcb1a1b0ec7c`
- previous Critic review：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_CRITIC_REVIEW_2026-09-22.md`
- previous Critic review commit：`471ecfa585f66e7b792a6dc29008b6116b5354df`
- rechecked blocker：`BOARD-01`
- execution branch/worktree：NONE

## 1. 结论

`BOARD-01` 已被 v2 的最小 GitHub-native 防线关闭，本轮没有发现由返修引入的新真实 blocker。

上一轮风险链是：

```text
中间 implementation/design PR
-> linked relationship / closing keyword
-> merge 到 default branch
-> top-level tracking Issue 自动关闭
-> Project issue-closed workflow
-> 假 DONE
```

v2 已同时切断这条链的 Project 侧和 Issue 侧：

1. lifecycle item 只允许专用 tracking Issue；
2. auto-add 限定为 `is:issue label:maintenance-track`；
3. implementation/design PR 不作为 lifecycle item；
4. Project 默认 `pull request merged -> Done` 必须关闭；
5. DONE 前，中间 PR 不得把 tracking Issue 建成 merge 后自动关闭的 linked issue；
6. PR body 和 commit message 均不得对该 tracking Issue 使用 GitHub closing keywords；
7. 中间 task/PR/commit 只用普通非关闭 reference；
8. repository-level linked-PR auto-close 不全仓关闭；
9. `issue closed -> Done` 只作为完整 DONE checklist 通过后的最后机械动作。

因此，在 v2 规定的正常维护路径中，没有剩余的“中间 PR merge 自动把 required adaptation 尚未完成的 top-level tracking Issue 关闭”的路径。

## 2. 本轮实际读取与版本核对

本轮按要求实际读取最新 `main` 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_CRITIC_REVIEW_2026-09-22.md`

并对 v2 Proposal 的 `main` blob 与指定 proposal commit 做了核对，两者为同一 blob；本轮没有因为后续 Critic prompt commit 而发生 Proposal 漂移。

本轮未重新从零审查 v1 已通过的架构部分，只复核 `BOARD-01` 与 v2 修订的直接影响。

## 3. 独立 GitHub 官方现实核查

本轮重新独立检查 GitHub 官方当前文档。

### 3.1 Projects built-in automation

GitHub 官方说明：Project 初始化时默认启用两条相关 workflow：

- issue / pull request closed -> Status Done；
- pull request merged -> Status Done。

Project 内置 workflow 可以在 Workflows 页面启用或关闭。

来源：
https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations

这支持 v2 明确关闭 `pull request merged -> Done`，同时保留 final `issue closed -> Done`。

### 3.2 Auto-add filter

GitHub Projects auto-add 支持 `is` 与 `label` qualifier，其中 `is` 可限定 `issue` / `pr`。

来源：
https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically

因此 `is:issue label:maintenance-track` 是当前 GitHub-native 的可行边界，可以把 top-level lifecycle admission 限定在 tracking Issue。

### 3.3 Linked PR 与 default-branch merge

GitHub 官方说明：

- PR 可以通过手工 Development link 或 closing keyword 与 Issue 建立关系；
- linked PR merge 到 repository default branch 后，关联 Issue 会自动关闭；
- repository 默认开启这种 auto-close。

来源：
https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-auto-closing-issues

因此 v2 在 DONE 前禁止 tracking Issue 与中间 PR 建立会导致 auto-close 的 linked relationship，是对上一轮 blocker 的直接修复。

### 3.4 Closing keywords 也可以来自 commit message

GitHub 官方列出的 closing keywords 包括：

`close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved`

这些 keyword 可以出现在 PR description，也可以出现在 commit message；相应 commit 合入 default branch 时可以关闭 Issue。

来源：
https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue

因此 v2 同时约束 PR body 与 commit message 是必要且足够贴合 GitHub 真实行为的。

### 3.5 Repository-level auto-close 可以全局关闭，但本设计不需要

GitHub repository settings 可以全局关闭“merged linked pull requests auto-close issues”。

来源：
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-auto-closing-issues

v2 明确不采用这一全仓方案是正确的。BOARD-01 只涉及 `maintenance-track` tracking Issue；通过 item-level linking/keyword discipline 即可关闭风险，不应影响其他普通 Issue/PR 合法使用 `Closes #N` 的工作方式。

### 3.6 CLI 足以支撑稳态 maintenance

GitHub CLI 当前 `gh project` 提供：

- `item-add`
- `item-edit`
- `item-list`
- field/list 等项目维护动作

并要求 token 至少具备 `project` scope。

来源：
https://cli.github.com/manual/gh_project
https://cli.github.com/manual/gh_project_item-edit
https://cli.github.com/manual/gh_project_item-list

这足以支持 v2 定义的长期机械同步。一次性 Project workflow/view bootstrap 仍按 execution package 真实核对当前 Web UI/API/CLI 入口，不需要新增 daemon/service。

## 4. BOARD-01 复核

### 4.1 Blocker disposition

```text
BOARD-01 = CLOSED
```

上一轮最小关闭条件均已进入 v2：

- issue-only auto-add；
- disable `pull request merged -> Done`；
- no auto-closing linked relationship before final closure；
- no closing keywords in PR body / commit message before final closure；
- ordinary non-closing references only；
- Issue close is explicit final closure action；
- no repository-wide auto-close shutdown。

### 4.2 是否仍有现实的中间 PR merge -> 假 DONE 路径

在 v2 所规定的正常路径内，没有发现。

如果有人违反 v2，手工提前关闭 tracking Issue，Project 的 `issue closed -> Done` 当然仍会机械置为 DONE；但这不是 `BOARD-01` 中“PR merge 绕过 completion contract”的剩余路径，而是直接违反 tracking Issue closure contract。为防这种人为越权再新增 workflow、GitHub Action 或全仓禁用 close，不具备足够的直接风险证据，会造成不必要复杂度，因此不形成新 blocker。

execution package 只需要验证实际 Project configuration 与这些设计相符。

### 4.3 Blast radius

v2 没有扩大到全仓禁用 auto-close。

影响范围仅是：

- `maintenance-track` tracking Issue 的 lifecycle discipline；
- 本 Project 的 `pull request merged -> Done` workflow；
- 与这些 tracking Issue 相关的中间 PR/commit reference 方式。

普通 GitHub Issue/PR 仍可按 repository 原有语义使用 linked PR / closing keywords。

### 4.4 issue closed -> Done 是否安全

作为最后机械动作是安全的。

它不再承担“判断是否完成”的职责。完成判断发生在 Issue closure 之前，要求：

- required adaptation 完成或 N/A；
- normal-entry / real-consumer evidence 完成；
- runtime/server/Host evidence 有 durable locator；
- Resolution commit 已确定；
- 无 unresolved completion blocker。

随后 `close tracking Issue -> Status DONE` 只是把已经成立的 completion truth 映射到 Project。

## 5. 对两个 non-blocking clarification 的复核

两项均正确，且没有引入新的控制面。

### Post-DONE optional consumer

DONE 后新增的 optional consumer 默认形成新的 follow-up item，而不是追溯性扩大旧 completion contract。

这正好约束 `ADAPTING` 不会演变为无限 rollout。只有新证据证明旧 DONE 当时声称的原能力本身没有成立，才按 regression 处理。

### Bootstrap 与稳态 maintenance 分离

一次性 bootstrap 负责创建字段、views、workflow、label、scope/preflight 与 bounded backfill；稳态 maintenance 使用 Issue + `gh project item-add/item-edit/item-list` + built-in workflow。

这种拆分没有新增数据库、registry、ledger、controller、watcher 或同步 daemon，反而避免把一次性配置负担带进每次维护。

## 6. 四状态与 DONE 最终边界

上一轮已认可的四状态继续成立：

```text
TODO -> DOING -> ADAPTING -> DONE
```

`ADAPTING` 仍然只表示 canonical core 已落地、但 frozen completion contract 中 required downstream consumer 尚未全部适配与验证；不是未来所有可选 rollout 的无限集合。

DONE 的最终边界仍是 top-level idea，而不是 task/PR：

1. 原问题真正解决；
2. canonical owner source 已集成；
3. required downstream adaptation 全部完成或有明确 N/A/NO_CHANGE；
4. normal-entry / real-consumer validation 完成；
5. 非 Git runtime/server/Host evidence 有 durable locator；
6. Resolution commit 已确定；
7. tracking Issue 明确关闭，Project 再机械置 DONE。

## 7. 审查结论

```text
RESULT = PASS
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md
REVIEWED_PROPOSAL_COMMIT = da46f14141888c1bcd94bf94a486bcb1a1b0ec7c
REVIEW_STAGE = DESIGN_PROPOSAL_REVISION_REVIEW
RECHECKED_BLOCKERS = BOARD-01
CLOSED_BLOCKERS = BOARD-01
NEW_BLOCKERS = NONE
```

本 PASS 只批准 v2 的设计语义：四状态、top-level idea 生命周期、BOARD-01 防线、DONE 边界、Resolution commit 语义与 bootstrap/steady-state maintenance 分工。

本 PASS 不授权：

- 创建或修改 GitHub Project；
- 创建、迁移、关闭或批量修改 Issue；
- 修改 AGENTS/TODO/plugin source；
- backfill；
- 启动 Codex/Executor；
- production/server/Host 变更；
- Bridge Kit 变更；
- paid API；
- 任何未审 execution package 的外部副作用。

下一步应回 Planner，基于这个已通过设计准备最小 execution package，并再次按 Planner/Critic contract 提交 execution-ready review。
