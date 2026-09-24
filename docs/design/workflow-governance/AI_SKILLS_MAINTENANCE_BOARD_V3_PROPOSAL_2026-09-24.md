# AI Skills 维护看板与完成语义 — Planner Proposal v3

- 日期：2026-09-24
- Human label：AI Skills 维护看板与完成语义
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- source_branch_or_ref：`main`
- Planner baseline：`main@ce7f606e75dfa2bc7029b68655657c2d3d5b5d04`
- supersedes only where explicitly stated：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`
- v2 design PASS：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`
- execution-package v0.1 Critic：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-22.md`
- current execution draft：v0.2 exists but is **not** executable and must be revised only after this amendment receives Critic PASS
- execution branch/worktree：NONE in this design round
- 状态：DRAFT_FOR_CRITIC_REVIEW

## 1. 为什么必须重新回设计审查

上一轮 execution blockers `BOARD-UX-01` 与 `BOARD-SYNC-01` 已经在 v0.2 draft 中按 Critic 要求接受：

- 看板是用户直接消费的 artifact，Codex 修改 Kanban reader-facing copy 时必须使用 Clear Writing；
- Planner / Critic / GPT 是 lifecycle 的语义 owner，不能等用户提醒。

用户本轮又明确了两个**新的完成语义**：

1. 第一次 bootstrap 时，Codex 不是只挑 `CANDIDATE_GENERIC / PROMOTE_NOW`，而是要把当前 plugin TODO 全部系统整理，让用户不会因为 raw `NEW` 仍藏在 Markdown 里而看不到真实 backlog；
2. 对真正的 workflow / shared maintenance mechanism，central plugin/source 做完不等于完成。只有必要的 server 与 local-machine consumer 都完成 adaptation 和正常入口验证，才算这个 workflow 真正收尾；用户希望这一步后续通过 AI Skills Maintainer 执行。

这两点会改变 v2 已批准的 admission / DONE contract，因此不能静默塞进 execution package。v3 只审这两个 amendment；不重新打开四状态、BOARD-01、BOARD-UX-01、BOARD-SYNC-01。

## 2. 保持不变的已批准核心

继续使用：

```text
TODO -> DOING -> ADAPTING -> DONE
```

保持：

- Project item = top-level tracking Issue；
- plugin TODO = failure / evidence / maturity inbox；
- Planner–Critic / Reviewed Handoff / Executor task = execution evidence；
- WAITING/BLOCKED 不是第五个主状态；
- Resolution commit = owner repo canonical closure/evidence commit；
- Project 是用户直接消费的看板，必须满足 Clear Writing；
- Codex 修改 reader-facing Kanban copy 时必须真实调用 Clear Writing；
- Planner / Critic / maintenance GPT 主动 reconcile，不等用户提醒；
- BOARD-01 全部 auto-close guardrails；
- routine sync 不要求用户手工拖卡；
- 不新增 controller/watcher/GitHub Action/database/registry/ledger/state machine。

## 3. Amendment A — 第一次 bootstrap 要覆盖“当前所有 TODO”，但不能机械 1:1 复制

### 3.1 用户要的不是“只显示已经 promotion 的 TODO”

最初 v2 将 raw `NEW` 排除在 Project 之外，理由是避免把 TODO 垃圾山复制成 Issue 垃圾山。

但用户当前目标更具体：

> 第一次由 Codex 把目前所有 TODO 整理进去，之后由 GPT 持续推进和维护。

如果 raw `NEW` 仍全部只藏在 `docs/plugin-todos/*.md`，用户打开 Project 仍看不到大量真实积压，Project 不能解决“TODO 越积越多、不知道还有什么”的核心问题。

因此 v3 改成：

> **全覆盖，不等于一条 TODO 一张卡。**

### 3.2 One-time full-inbox coverage pass

第一次 bootstrap 必须扫描：

- 十个中央 `docs/plugin-todos/<plugin>.md`；
- 当前 standalone-skill TODO inbox；
- 其他被根 `TODO.md` 正式列为当前 maintenance inbox 的 source。

对**当前仍有维护意义的每个 TODO 条目**给出明确 disposition，不能静默遗漏。

允许 disposition：

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

这只是一次 bootstrap evidence 语义，记录在 task result 中，不创建长期 registry/schema。

### 3.3 Raw NEW 的新规则

raw `NEW` 不再因为“还没 promotion”而自动从 Project 隐身。

对一个当前仍有效、确属中央 plugin maintenance 的 `NEW`：

- 如果与已有 top-level idea 明显相同 -> 合并到已有 tracking Issue；
- 如果本身是独立、可理解的真实问题 -> 创建一个 `Status=TODO` tracking Issue；
- source TODO 的 maturity 仍然保持 `NEW`，除非 Planner 另行完成 promotion triage；
- Project `TODO` 只表示“这是当前 backlog 中一个需要跟踪的 top-level idea”，不表示它已经 `CANDIDATE_GENERIC` 或 `PROMOTE_NOW`。

因此：

```text
Project lifecycle status != plugin TODO maturity status
```

不能因为一条 `NEW` 进入 Project 就假装它已经获得通用化批准。

### 3.4 仍然不应该进入中央 Project 的内容

以下条目可以在 full-inbox coverage 中被明确 disposition 为“不上卡”，但必须有理由：

- `PROJECT_LOCAL`；
- 已 `REJECTED`；
- 已 `SUPERSEDED`；
- 纯历史、已经完成且当前没有检索价值的 `PROMOTED` / closure record；
- 根本不属于 AI_Skills 中央 maintenance 的项目研究/产品/code TODO。

这不是遗漏，因为它们会出现在 bootstrap coverage evidence 中并标明 disposition。

### 3.5 防止 Issue 爆炸

Codex 不得机械地按每个 Markdown heading 生成 Issue。

先做：

1. duplicate/overlap triage；
2. top-level idea grouping；
3. primary Area ownership；
4. reader-facing Clear Writing；
5. 再创建 Issue。

同一 failure 的多个真实案例应该合到一张 tracking Issue 的 evidence 区。

如果两个条目是否应合并存在实质判断歧义，Codex不得自己把它们合并为一个新通用规则；保留两个 TODO tracking Issues 或提交 Planner triage，不为了减少卡片数破坏语义。

### 3.6 完整性证据

bootstrap 结果必须有一个 repo 内 evidence 文件，例如：

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

它至少能让 Reviewer核对：

```text
source inbox + heading
-> disposition
-> tracking Issue（如适用）
-> Area
-> initial lifecycle Status
```

这是一次性验收 artifact，不成为长期数据库。

最终验收要能回答：

> 当前正式 TODO inbox 中有没有一个仍有维护意义的条目既没上板、也没被明确 disposition？

若有，bootstrap 不完整。

## 4. Amendment B — workflow 完成必须经过 server + local-machine adaptation

### 4.1 中央实现不再等于 workflow DONE

对真正会被机器/环境消费的 workflow / shared maintenance mechanism，以下都不能单独触发 DONE：

- plugin source 完成；
- tests / CI PASS；
- plugin release；
- main integration；
- AI_Skills central implementation complete。

这些最多意味着：

```text
DOING -> ADAPTING
```

### 4.2 哪些 item 默认受这个规则约束

若 top-level idea 的能力声明会改变以下任一正常使用行为，则默认视为 **machine-consumed workflow item**：

- `workflow-core` 的执行/交付/Human Gate/Reviewed Handoff行为；
- `ai-skills-core` 的机器更新、安装、维护、distribution/adaptation行为；
- repo-wide / cross-plugin shared workflow；
- Bridge/AI_Skills 联动后必须在真实 Codex environment 中被消费的 shared rule；
- 其他明确需要安装、reload、machine/profile/Host/repo consumer 才能生效的机制。

普通纯文档、纯审计、只属于某个 artifact 的 domain improvement 不自动继承“两台机器都必须适配”。

### 4.3 Default required consumer environments

对 machine-consumed workflow item，除非 frozen completion contract 明确给出不同且合理的适用范围，默认 required downstream consumer 是：

1. **current canonical server consumer**
2. **current canonical local-machine consumer**

进入 `ADAPTING` 时，tracking Issue 必须把这两个抽象名称解析成当前真实 consumer identity / locator；不能永远只写“server/local 待处理”。

具体 host/path/account 不在 Project policy 中硬编码，因为它们会变化，且应由当前环境 source / AI Skills Maintainer discovery 获取。

### 4.4 AI Skills Maintainer 的角色

用户希望后续 adaptation 通过 **AI Skills Maintainer** 完成。

当前 repo source 已经存在一个 machine-update orchestration 设计方向：

`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`

它明确把 AI Skills Maintainer 设计为当前 Codex machine/server 的 update/adaptation user entry。

但本 v3 **不能把一个仍处于独立设计/实现流程中的未来能力冒充已 production-ready**。

因此 canonical board contract 应写：

- 当 AI Skills Maintainer 的 machine-update/adaptation capability 已正式发布并从普通入口可用时，machine-consumed workflow 的 server/local adaptation 默认通过该入口执行；
- 如果该 capability 尚未 production-ready，则 tracking Issue 保持 `ADAPTING`，当前 anchor 指向相应 Maintainer rollout blocker / approved alternative consumer owner；
- 不得因为“以后会有 Maintainer”就把当前 workflow 标 DONE；
- 不在本 board task 中实现或修改 machine-update orchestration。

### 4.5 Adaptation 的完成证据

每个 required environment 都必须有：

- actual target identity；
- update/adaptation action；
- installed/loaded identity；
- fresh-session / normal-entry consumption evidence（如果该机制的加载边界需要新 session）；
- should-not-change / failure safety，按风险决定；
- durable evidence locator。

仅“源码同步到 machine”不够。

### 4.6 DONE contract

machine-consumed workflow 的 DONE 至少是：

```text
canonical central source/release complete
+ required server adaptation PASS
+ required local-machine adaptation PASS
+ normal-entry consumption PASS on both required environments
+ durable evidence
+ Resolution commit
+ tracking Issue completed close
```

如果其中任何一项未完成：

```text
Status = ADAPTING
```

不是 DONE。

### 4.7 环境适用性例外

只有在 frozen completion contract 明确说明某个 workflow 本来就**只适用于 server**或**只适用于 local machine**，并有 source 证据时，另一环境才可标 `N/A`。

不能为了快点 DONE 临时说“不适用”。

## 5. Steady-state ownership：GPT 推进语义，Codex/Maintainer做机械执行

用户当前期望可以概括为：

```text
一次性初始化 / 大规模整理 -> Codex
后续判断 / Planner / Critic / 状态推进 -> GPT
机器适配 -> AI Skills Maintainer（production-ready 后）
Project mutation -> 有权限的 Codex / Maintainer / GitHub surface
```

### GPT / Planner / Critic

负责：

- 读真实 TODO/source；
- triage；
- 定义 top-level idea；
- 决定 TODO/DOING/ADAPTING/DONE truth；
- 当前 anchor / next action；
- required consumer environments；
- Critic review locator；
- 生成 exact pending Project mutation（若当前 surface 无 Project mutation）。

### Codex / AI Skills Maintainer

负责：

- 一次性 full-inbox bootstrap；
- GitHub Project/Issue机械 mutation；
- approved implementation；
- machine/server/local adaptation；
- 真实 install/reload/normal-entry verification；
- durable evidence。

### 用户

不承担：

- 手工拖 Kanban；
- 提醒 Planner/Critic同步；
- 自己判断该从 DOING 切 ADAPTING；
- 自己寻找哪个 workflow/commit 是 current anchor。

只在真正 HUMAN_ONLY 登录/授权/物理/产品决策时介入。

## 6. Clear Writing 继续是硬要求

保持 execution v0.2 已写入的用户要求：

> Codex 只要创建或修改 Kanban / Project 的人类可见文字，必须真实调用 Clear Writing（`writing-style`）。

覆盖：

- tracking Issue title；
- 顶部“问题 / 当前进度 / 当前执行锚点 / 下一步”；
- backfill tracking copy；
- closure / History reader-facing copy。

Clear Writing 不得改变：

- maturity；
- lifecycle Status；
- Area owner；
- required consumer environments；
- exact locators；
- Resolution commit；
- evidence semantics。

实际 Project surface qualitative review 仍是质量权威。

## 7. Alternatives

### A. 继续隐藏 raw NEW，等 Planner promotion 后才上板

不采用。

优点是 Project 较干净，但用户仍看不到当前真实 backlog，不能解决“TODO 越积越多”的原问题。

### B. 每个 TODO heading 机械变成一张 Issue

不采用。

优点是表面上 100% 覆盖；缺点是重复、项目局部案例、历史项全部变成卡片，Project 很快不可用。

### C. Full coverage + dedupe/disposition

采用。

所有当前 TODO 都被扫描和解释；真正 active central items可见；duplicate/project-local/historical items不制造垃圾卡，但有 coverage evidence证明没有静默遗漏。

### D. workflow main merge 后 DONE，机器 rollout 当另一个 follow-up

不采用。

这会继续制造用户最关心的假完成：source 已发布，但真实 server/local 仍运行旧行为。

### E. 要求所有 plugin improvement 都必须 server + local 两边安装

不采用。

过重。只有 machine-consumed workflow/maintenance mechanism 默认需要双环境 adaptation；普通 domain/artifact improvement按自身 completion contract验收。

### F. 后台 watcher 自动持续扫描/同步

不采用。

GPT/Planner/Critic 已经是语义 owner；Codex/Maintainer机械执行足够，不新增 daemon/controller。

## 8. Capability /验收影响

本 amendment 不新增 plugin production capability gate；它改变 maintenance board 对“backlog覆盖”和“workflow DONE”的真实性要求。

后续 execution package 必须增加两类直接验收：

### Full-inbox coverage

- 扫描所有 current canonical TODO inbox；
- 每个当前有维护意义条目有 disposition；
- 每个 active central top-level idea对应 tracking Issue；
- raw NEW 不再因 maturity 未 promotion 而自动隐身；
- duplicate/PROJECT_LOCAL/rejected/history不制造卡但有明确记录；
- Reviewer能从 coverage artifact抽查回 source。

### Workflow adaptation closure

对 backfilled/current machine-consumed workflow items：

- 如果 central core 已完成而 server/local仍未全部适配 -> ADAPTING；
- required server/local consumer identity 被解析并记录；
- DONE item 必须有两个 required environment 的消费证据，除非一个有合法 N/A contract；
- AI Skills Maintainer 只有在其相应 machine-update capability production-ready 后才能作为该 adaptation 的 normal executor；
- 不能用“plugin release PASS”替代 machine consumption。

## 9. Non-goals

本设计轮不：

- 创建 GitHub Project / Issue；
- backfill；
- 修改 AGENTS/TODO；
- 启动 Codex；
- 修改 Clear Writing；
- 修改 AI Skills Maintainer machine-update source；
- 修改 Bridge Kit；
- 访问 server/local machine；
- 新增自动化；
- 改版本。

Critic PASS 后才允许 Planner 把 execution v0.2 返修成新的同版 execution package（建议 v0.3），并再次做 execution-ready review。

## 10. Critic 应只审的新问题

请不要重开已经关闭的：

- 四状态；
- BOARD-01；
- BOARD-UX-01；
- BOARD-SYNC-01；
- Clear Writing requirement；
- GitHub CLI/GraphQL/UI bootstrap route。

本轮只判断：

1. “所有当前 TODO 必须被 full-coverage 整理，但不是 1:1 发 Issue”是否满足用户目标且不过重；
2. raw NEW 作为 `Project TODO` 是否会被误解成 promotion，当前 lifecycle/maturity 分层是否足够；
3. machine-consumed workflow 默认 required server + local adaptation 是否过重或过简；
4. AI Skills Maintainer 作为后续 adaptation normal executor 的表述是否诚实，没有把尚未 production-ready 的能力冒充已可用；
5. server/local 的 exact identity 在进入 ADAPTING 时才绑定，而不是 policy 硬编码，是否合理；
6. 是否仍有 central source done -> false DONE 的漏洞；
7. 是否需要比本方案更简单的方式达到用户“我只想看清楚、GPT自己推进、真正机器都生效才算完成”的目标。

## 11. Planner disposition

这不是对上一轮 Critic blocker 的反驳。

```text
BOARD-UX-01 = ACCEPTED_AND_REVISED_IN_V0_2
BOARD-SYNC-01 = ACCEPTED_AND_REVISED_IN_V0_2
USER_AMENDMENT_TODO_FULL_COVERAGE = ACCEPT
USER_AMENDMENT_WORKFLOW_MACHINE_CLOSURE = ACCEPT
NEW_BLOCKERS_FOUND_BY_PLANNER = NONE
NEXT_HANDOFF = CRITIC
```
