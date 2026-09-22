# AI Skills 维护看板与完成语义 — Planner Proposal v2

- 日期：2026-09-22
- Human label：AI Skills 维护看板与完成语义
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- source_branch_or_ref：`main`
- Planner baseline：`main@471ecfa585f66e7b792a6dc29008b6116b5354df`
- supersedes：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_PROPOSAL_2026-09-22.md`
- v1 reviewed proposal commit：`e9804daf12611788f98d9ab3c2577c7744963c03`
- v1 Critic review：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_CRITIC_REVIEW_2026-09-22.md`
- v1 Critic review commit：`471ecfa585f66e7b792a6dc29008b6116b5354df`
- execution branch/worktree：NONE（本轮只做设计，不创建 Project、不迁移 Issue、不改 production plugin）
- 状态：DRAFT_FOR_CRITIC_REVIEW_R2

## 1. 结论与本轮变更

v1 的主设计保持不变：

```text
TODO -> DOING -> ADAPTING -> DONE
```

本轮只处理 Critic 的稳定 blocker `BOARD-01`。

Disposition：

```text
BOARD-01 = ACCEPT
```

原因是 GitHub 当前真实默认行为确实能形成一条绕过我们 completion contract 的链：

```text
中间 implementation/design PR
-> 与 top-level tracking Issue 建立 GitHub closing link，或使用 closing keyword
-> PR merge 到 default branch
-> tracking Issue 自动关闭
-> Project 的 issue-closed workflow
-> Status = DONE
```

这会在 required downstream adaptation 尚未完成时制造假 DONE。

v2 因此加入最小 GitHub-native 防线：

1. top-level lifecycle item 只能是专用 tracking Issue；
2. auto-add 显式只收 `is:issue label:maintenance-track`；
3. 关闭 Project 默认的 `pull request merged -> Done` workflow；
4. tracking Issue 真正达到 DONE 前，中间 PR 不得与它建立会触发自动关闭的 GitHub Development/linked relationship，也不得在 PR body 或 commit message 对该 tracking Issue 使用 `close/closes/fix/fixes/resolve/resolves` 等 closing keywords；
5. 中间 PR/commit 只用普通非关闭 reference，并把 locator 写回 tracking Issue；
6. `issue closed -> Done` 可以保留，但 close 是完成合同最后一步，而不是 merge 的副作用；
7. 不全仓关闭 repository-level linked-PR auto-close，不新增 GitHub Action、数据库、registry、ledger、controller、watcher 或新的 workflow state machine。

除此之外，没有发现需要新增 blocker 的新直接证据。

## 2. 为什么仍然是四状态，而不是三状态

GitHub Projects 技术上并不限制三个状态；单选字段可以有多个选项，Board 可按 single-select 分列。

本设计仍选择四个主状态：

### TODO

已经去重、值得持续追踪，但当前没有 active execution。

### DOING

top-level idea 正在被推进。包括：

- Planner / Critic 设计；
- execution package；
- Codex implementation；
- independent review / regression；
- central integration / release closure。

不为 Planner、Critic、Implementation、Review、Integration 分别再造主状态。

### ADAPTING

同时满足：

1. canonical owner source 已经落地；
2. top-level idea 的 completion contract 明确要求 downstream consumer adaptation；
3. 至少一个 required repo / server / Host / install / normal entry 尚未完成适配和验证。

这是真正对用户有用的交付阶段，不是内部 workflow phase。

### DONE

只有 top-level idea 的 completion contract 全部成立后才允许。

如果一个 idea 根本不需要 downstream adaptation，可直接：

```text
TODO -> DOING -> DONE
```

如果只用三个状态，则中央实现已完成但下游仍未落地的工作只能继续叫 DOING，无法一眼区分“还在做核心实现”和“核心已完成、正在真实消费侧适配”。三状态 + Phase 又增加第二个需要同步的字段，没有更简单。

`WAITING / BLOCKED` 仍不是主状态。它们可能发生在 DOING 或 ADAPTING 任意阶段，使用 Issue label + `Blocked by / Next action` 即可。

## 3. 看板追踪 top-level idea，而不是单个 task

必须继续区分三类对象。

### 3.1 Plugin TODO

`docs/plugin-todos/*.md` 继续是：

- 真实 failure / feedback inbox；
- evidence / maturity / promotion 判断；
- `NEW / CANDIDATE_GENERIC / PROMOTE_NOW / ...` 等现有 TODO 语义。

这些 TODO 标签不是执行状态。

### 3.2 GitHub Project tracking Issue

一个已经去重、值得持续追踪的 top-level idea / work item。

它回答：

- 现在是否开始做；
- 中央实现是否已经落地；
- 是否还在 downstream adaptation；
- 是否真正 DONE；
- 最终由哪个 commit 形成关闭锚点。

Project 中的长期 lifecycle item 必须是 tracking Issue，不使用 implementation PR 或 draft item 作为 top-level lifecycle card。

### 3.3 Planner–Critic / Reviewed Handoff / Executor task

某一轮具体设计、实现、review、integration 的执行单位。

一个 idea 可以经过多个 task。某个 task 自己 ACHIEVED、PR merged 或中央 integration 完成，都不能自动令 top-level idea DONE。

## 4. Status 的严格语义

### TODO

满足至少一项：

- Planner 已把若干原始反馈去重成一个独立 idea；
- 它仍是有效的 `CANDIDATE_GENERIC / PROMOTE_NOW / BLOCKED_NEEDS_EVIDENCE`；
- 尚未进入 active implementation/design；
- 上游依赖存在，但当前还没有真正执行。

### DOING

idea 已开始实际推进，并且 canonical core implementation 尚未达到“只差 downstream consumption”的阶段。

具体内部进度留在 Issue 的 task/PR/commit locators 与 `Next action`，不复制成 Project 主状态。

### ADAPTING

仅当全部满足：

1. core/canonical source 已集成；
2. completion contract 中存在 required downstream target；
3. 至少一个 required target 尚未完成消费和验证。

required target 可以是：

- 指定 repo；
- 指定 server / Host；
- 本地或远程安装；
- site/profile；
- normal production entry；
- 其他对原本 completion claim 成立必不可少的 consumer。

“以后可能想支持”不是 required target。

### DONE

必须同时满足：

1. 原问题已真正解决，不只是 Plan/test/schema/PR；
2. canonical owner source 已集成；
3. frozen completion contract 中全部 required downstream adaptation 已完成，或有明确 `N/A / NO_CHANGE` 依据；
4. normal-entry / real-consumer validation 达到该 idea 的质量要求；
5. 若存在非 Git runtime/server/Host effect，其 durable evidence 已有长期 locator；
6. `Resolution commit` 已确定并写入 Project/Issue；
7. tracking Issue 以明确 closure action 关闭。

只有第 7 步完成后，Project 的 `issue closed -> Done` 自动化才把 Status 更新为 DONE。

## 5. ADAPTING 的边界：不能无限扩大 DONE

required adaptation target 必须来自以下之一：

1. idea 开始推进时已经冻结的 completion contract；
2. 执行中出现新的直接证据，证明若不适配该 consumer，则原 completion claim 实际并不成立。

以下均不阻止 DONE：

- 未来可选 repo；
- 以后可能新增的 server；
- 尚未决定采用的 consumer；
- 非当前 claim 所必需的 rollout；
- 单纯“顺便也应该升级”的维护愿望。

### Post-DONE rule

DONE 后才出现的新 optional consumer，默认创建新的 follow-up work item，不追溯扩大旧 item 的 completion contract。

只有新证据证明旧 item 当时声称的既有能力其实并未成立，才作为 regression 处理：重新打开原 item或创建明确关联的 regression item，由 Planner 根据现有 policy 决定，不以“未来 rollout 增加”自动撤销旧 DONE。

## 6. 每个 DONE idea 必须有 Resolution commit

Project 使用一个文本字段：

```text
Resolution commit
```

定义为：

> owner repo 中第一次让这个 top-level idea 的完整 DONE contract 可以被长期定位的 canonical closure/evidence commit。

它不是“第一版 implementation SHA”，也不是要求所有工作只能发生在一个 commit。

tracking Issue / closure evidence 中可以记录多个 component locator：

```text
Source TODO:
Tracking issue:
Design / implementation tasks:
Central implementation commits:
Canonical integration commit:
Required adaptation targets:
Downstream repo commits:
Server / Host / runtime evidence:
Normal-entry validation:
Resolution commit:
```

Project 字段只保留最终 `Resolution commit`，避免把一串 component SHA 塞进看板字段。

如果最后一个 required adaptation 自身就是可长期定位的 owner-repo commit，并且已经承载完整 closure evidence，它可以直接作为 Resolution commit。

如果最后一个必要动作是 server/Host mutation、没有 Git SHA，则先把 durable runtime evidence 写入 owner repo 的 closure/result artifact，再以该 closure/evidence commit 作为 Resolution commit。

不要求 tracked file 在同一 commit 中写自己的 SHA。commit 形成后，再由 Project field / Issue closing comment 回填 SHA，避免 self-reference。

## 7. Project admission：不要把 TODO 垃圾山复制成 Issue 垃圾山

### 不自动进 Project

- 未去重的原始 `NEW`；
- `PROJECT_LOCAL`；
- `REJECTED`；
- `SUPERSEDED`；
- 纯历史 `PROMOTED`。

### 应进入 Project

Planner triage 后仍需要持续追踪的独立 idea，例如：

- `CANDIDATE_GENERIC`；
- `PROMOTE_NOW`；
- 仍有效的 `BLOCKED_NEEDS_EVIDENCE`；
- 已启动 Planner–Critic / Reviewed Handoff 的 work item；
- central implementation 已集成但 required downstream adaptation 未完成的 work item。

每个 Project lifecycle item 使用真实 GitHub Issue。

对应 plugin TODO 只保存：

```text
tracking: #<issue-number>
```

以及自身的 evidence/maturity 语义；不要把 Project Status 回写成第二份执行状态。

## 8. BOARD-01：GitHub auto-close / auto-Done 防线

### 8.1 只让 tracking Issue 成为 lifecycle item

Project auto-add 使用专用 tracking label：

```text
maintenance-track
```

auto-add filter 至少限定：

```text
is:issue label:maintenance-track
```

可以在实际 bootstrap 时根据当前 GitHub UI 支持增加 `is:open` 等过滤，但不得放宽成把普通 implementation PR 自动纳入 top-level lifecycle。

implementation/design PR 可以在 Issue 中作为 locator，但不是生命周期卡片。

### 8.2 关闭默认的 PR merged -> Done

GitHub 新 Project 默认启用两类会把 item 设为 Done 的 workflow：

- item closed -> Done；
- pull request merged -> Done。

本 Project 必须关闭：

```text
pull request merged -> Done
```

因为 PR merge 只证明某一个 component/integration step，不证明 top-level idea 的 required adaptation 已完成。

### 8.3 tracking Issue 达到 DONE 前，禁止会自动关闭它的 PR relationship

在 top-level tracking Issue 真正满足 §4 DONE contract 前：

- 中间 implementation/design PR 不得通过 GitHub `Development` / manual linked relationship 把 tracking Issue设置为该 PR merge 后自动关闭的 linked issue；
- PR body 不得对该 tracking Issue使用 `close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved` closing keywords；
- commit message 也不得对该 tracking Issue使用这些 closing keywords；
- 不得把“中央实现 PR 已 merge”当作 Issue closure signal。

需要建立关系时，使用普通非关闭 reference，例如：

```text
Related tracking issue: #123
Implements part of #123
See #123
```

并由 tracking Issue body/comment 保存：

- PR locator；
- task key；
- implementation commit；
- review / integration evidence。

### 8.4 不全仓关闭 repository auto-close

GitHub repository 当前允许全局关闭“merged linked PR auto-closes issue”。

本设计**不**要求修改这个 repository-level 行为。

原因：

- 普通 Issue/PR 仍可能合理使用 `Closes #N`；
- 本问题只需要保护 `maintenance-track` top-level tracking Issue；
- 用 item-level linking discipline 即可解决，不需要扩大 blast radius。

### 8.5 issue closed -> Done 可以保留

`issue closed -> Done` 是有价值的 GitHub-native自动化，但只能让“Issue closure”成为 DONE 的最后机械动作。

关闭 tracking Issue 前，Planner/maintainer/Codex 必须核对：

- required adaptation checklist 已全部完成或 N/A；
- normal-entry / real-consumer evidence 已完成；
- 非 Git runtime/server evidence 有 durable locator；
- Resolution commit 已确定并写入；
- 没有 unresolved completion blocker。

然后再执行：

```text
close tracking Issue
-> GitHub built-in issue-closed workflow
-> Project Status = DONE
```

因此 DONE 不再能由中间 PR merge 间接触发。

## 9. Project v1 最小字段

只创建三个必要字段。

### Status

```text
TODO
DOING
ADAPTING
DONE
```

### Area

单选，按主要 owner：

- central plugin slug；
- `workflow-core`；
- `ai-skills-core`；
- `repo / cross-plugin`。

一个 item 一个主要 owner；跨插件证据通过 Issue 引用，不复制 lifecycle card。

### Resolution commit

文本字段。DONE 前必填。

`task key`、`Blocked by`、adaptation checklist、component commits、runtime evidence 不新增 Project 字段，留在 tracking Issue。

## 10. 默认视图

第一版最多四个 view：

1. **Board**
   - 按 Status 分列；
   - 默认用户入口。

2. **Active**
   - 只看 DOING / ADAPTING。

3. **By area**
   - Table；
   - 按 Area 分组/过滤。

4. **History**
   - 只看 DONE；
   - 显示 Resolution commit。

不新增 timeline/sprint/controller。

## 11. 一次性 bootstrap 与长期 maintenance 分开

### 11.1 一次性 bootstrap

Critic PASS 后的 execution package 才允许：

- 创建/link Project；
- 建 Status / Area / Resolution commit；
- 配置 views；
- 配置 `maintenance-track` auto-add；
- 关闭默认 `pull request merged -> Done`；
- 保留/配置 `issue closed -> Done`；
- 创建最小 tracking Issue template/contract；
- 做 bounded backfill。

bootstrap 时必须重新核对：

- 当前 GitHub Project 实际配置入口；
- 当前 token 是否有 `project` scope；
- built-in workflow 的真实启用状态；
- auto-add filter 实际保存结果。

不要假设所有 bootstrap 设置都有 `gh project` 专用子命令；必要的一次性配置可使用 GitHub 当前正式 Web UI/API，只要 execution package 明确且用户授权。

### 11.2 稳态 maintenance

稳态由 Planner/Codex/thread 承担，不要求用户手工拖卡：

- GitHub Issue create/update/close；
- `gh project item-add`；
- `gh project item-edit`；
- `gh project item-list`；
- built-in auto-add / issue-close automation。

GitHub CLI 当前 `gh project` 需要 token 具备 `project` scope；这属于 bootstrap/preflight，而不是每次维护都重新询问。

当前 ChatGPT GitHub connector 没有 Projects mutation action，因此不为此自建 service；当前可靠写入口是 Codex/CLI + GitHub built-in automation。

## 12. 一次性 backfill

不机械把所有历史 TODO 建 Issue。

上线时：

1. 扫描中央 plugin TODO + standalone skill TODO；
2. 去重；
3. 对仍活跃的 `CANDIDATE_GENERIC / PROMOTE_NOW / BLOCKED_NEEDS_EVIDENCE` 建 tracking Issue；
4. 对当前 active Planner–Critic / Reviewed Handoff work item 建 tracking Issue；
5. 对 core 已集成但 required downstream 尚未完成的 top-level idea 设 ADAPTING；
6. `NEW` 先 triage，不未经判断全部入板；
7. 历史 DONE 只在有明显检索价值时 backfill，不做全量考古。

## 13. 维护责任

### 真实项目 thread

仍按现有规则：

- 真实 plugin failure 直接写对应 `docs/plugin-todos/*.md`；
- 不自行决定 generic promotion；
- 不因新增 `NEW` 就自动创建 Project lifecycle item。

### AI_Skills Planner / maintainer

- 去重与 triage；
- 创建/绑定 tracking Issue；
- TODO -> DOING；
- core 落地且 required consumers 未完成时 -> ADAPTING；
- 定义 completion contract / required adaptation targets；
- 最终核对 DONE checklist；
- 不因单个 task PASS / PR merge / central integration 自动 DONE。

### Codex / Executor

在批准范围内：

- 做机械 Issue/Project同步；
- 记录 task/PR/commit/evidence；
- 不自行扩大 required adaptation；
- 不自行改变 top-level completion contract；
- 不对 tracking Issue 使用 closing link/keyword，除非当前动作就是批准的 final closure。

### Critic / Reviewer

不日常维护 Board，但设计/closure review 时检查：

- 是否过早 DONE；
- required downstream 是否遗漏或无限扩大；
- Resolution commit 是否对应 durable closure evidence；
- BOARD-01 防线是否被执行。

## 14. GitHub 官方现实核查

本轮重新独立核对 GitHub 官方当前文档：

1. Built-in Projects automation：
   - 新 Project 默认启用 item closed -> Done；
   - 新 Project默认启用 pull request merged -> Done；
   - workflow 可在 Project 的 Workflows 页面启用/关闭。
   - https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations

2. Auto-add：
   - filter 支持 `is:issue`、`label:` 等 qualifier。
   - https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically

3. Linked PR / closing keyword：
   - linked PR merge 到 default branch 默认自动关闭关联 Issue；
   - closing keywords 包括 close/fix/resolve 等变体；
   - closing keyword 也可以出现在 commit message；
   - repository-level auto-close 可被管理员全局关闭，但 v2 明确不采用这种全仓方案。
   - https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
   - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-auto-closing-issues

4. GitHub CLI：
   - `gh project` 支持 item-add/item-edit/item-list 等稳定维护动作；
   - minimum token scope 为 `project`。
   - https://cli.github.com/manual/gh_project
   - https://cli.github.com/manual/gh_project_item-edit
   - https://cli.github.com/manual/gh_project_item-list

这些事实直接支持 BOARD-01 的 ACCEPT 与 v2 的最小修复。

## 15. Alternatives

### A. 继续只用 Markdown TODO

不采用。无法快速看到全局执行/adaptation状态，也不能稳定回答哪个 commit 真正关闭。

### B. 三状态 TODO / DOING / DONE

逻辑可行，但 central work 已结束、downstream adaptation 尚未完成的条目只能继续叫 DOING，丢失用户明确关心的信息。

若必须三状态，则 DONE 仍必须严格等到 required adaptation 完成；不能让 integration = DONE。

### C. 三状态 + Phase

不采用。增加第二个需要同步的字段，且 ADAPTING 本身就是用户关心的 lifecycle 状态，不需要再造 Phase。

### D. 七八个细状态

不采用。Planning/Review/Integration 等是内部 workflow phase。

### E. 全仓关闭 linked-PR issue auto-close

不采用。blast radius 过大，普通 Issue/PR 仍有合理 closing-keyword workflow。

### F. GitHub Action / sync daemon / database / registry / ledger / controller

不采用。GitHub Project + tracking Issue + built-in automation + CLI 已足够。

## 16. Failure modes 与防线

### 假 DONE：中间 PR merge

由 §8 关闭：

- tracking Issue only；
- auto-add only issue；
- disable PR merged -> Done；
- no closing link/keywords before final closure；
- Issue close as final action。

### ADAPTING 永远结束不了

由 frozen required targets + post-DONE follow-up rule 约束。

### TODO / Project 双写漂移

TODO 保存 evidence/maturity + tracking locator；Issue/Project保存 execution lifecycle，不复制 Status。

### server 没有 commit

durable runtime evidence 写入 owner repo closure artifact，以 closure/evidence commit 作为 Resolution commit。

### 用户仍需手工维护

稳态由 Planner/Codex/CLI + built-in automation维护；用户只在真正权限/产品决策/不可代理动作时介入。

## 17. Critic PASS 后的最小 execution scope

只有 Critic 对 v2 PASS 后，Planner 才准备 execution package。实现范围应限制为：

1. 创建或链接一个 GitHub Project，例如 `AI Skills Maintenance`；
2. Status = TODO / DOING / ADAPTING / DONE；
3. 建 Area、Resolution commit；
4. 配置最少 views；
5. 建 `maintenance-track` label / tracking Issue contract；
6. auto-add 只收 `is:issue label:maintenance-track`；
7. 关闭 Project 默认 `pull request merged -> Done`；
8. 保留并验证 `issue closed -> Done`；
9. bounded backfill 当前 active idea；
10. 在现有 `AGENTS.md` / `TODO.md` / `docs/plugin-todos/README.md` / workflow docs 中增加最小 consumer rule；
11. 不修改中央 plugin production behavior；
12. 不修改 Bridge Kit；
13. 不触碰 server/Host；
14. 不新增 GitHub Action/schema/database/registry/ledger/controller/watcher；
15. README checked：若没有人类入口变化，记录 `README checked: no update required`。

设计阶段不进行版本 bump。若 implementation 仅为 maintenance docs + GitHub Project metadata 且不改变 production plugin runtime，默认预期 `NO_BUMP`，最终仍按现行版本政策核对。

## 18. 本轮对 Critic finding 的明确 disposition

### BOARD-01 — ACCEPT

直接证据：

- GitHub Project 默认启用 `pull request merged -> Done`；
- linked PR merge default branch 会自动关闭 Issue；
- closing keyword 会建立/触发 auto-close关系；
- closing keyword 也可存在于 commit message；
- 随后 `issue closed -> Done` 会把 tracking Issue 置为 DONE。

因果风险：

- central implementation PR merge 可以在 required adaptation 尚未完成时产生假 DONE。

v2 最小关闭条件已落实在 §8：

- lifecycle item only tracking Issue；
- issue-only auto-add；
- disable PR merged -> Done；
- no linked/closing relationship before final closure；
- issue-close only after full DONE checklist；
- 不全仓关闭 repo auto-close；
- 不新增自研自动化层。

`BOARD-01` 在本版已完整接受并修订，等待独立 Critic 复核。

## 19. 当前 blocker 状态

Planner 没有发现新的直接证据支持新增 blocker。

```text
BOARD-01 = ACCEPTED_AND_REVISED
NEW_BLOCKERS_FOUND_BY_PLANNER = NONE
NEXT_HANDOFF = CRITIC
```
