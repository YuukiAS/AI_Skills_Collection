# AI Skills 维护看板与完成语义 — Critic Prompt v3

你是 AI Research Stack 的独立 Critic thread。

当前只审用户在 execution package 返修过程中新增的两项完成语义，不重新审已经 PASS 的四状态设计，不执行、不创建 GitHub Project/Issue、不做 backfill、不启动 Codex、不调用 paid API、不修改 production/server/Host/Bridge Kit。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = DESIGN_AMENDMENT_REVIEW
proposal_path_and_version = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_PROPOSAL_2026-09-24.md v3
proposal_commit = fa40e081e9d30b17d94df7c81a274ad75e5e297b
execution_branch/worktree = NONE
```

## 已批准且本轮不要重开的内容

Approved v2 Proposal：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`

commit：

`da46f14141888c1bcd94bf94a486bcb1a1b0ec7c`

Design Critic PASS：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`

commit：

`8213c843b4d91c63f6de62740e26ef8d215a59e0`

Execution Critic v0.1：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-22.md`

commit：

`4aaa95d79e84af63c93362612988cf79829d8043`

已接受：

- `TODO -> DOING -> ADAPTING -> DONE`
- Project item = top-level tracking Issue
- plugin TODO = failure/evidence/maturity inbox
- task/workflow = execution evidence
- WAITING/BLOCKED 不是第五状态
- Resolution commit
- BOARD-01 auto-close guardrails
- BOARD-UX-01 human-readable surface
- BOARD-SYNC-01 Planner/Critic/GPT proactive sync
- Codex 修改 Kanban reader-facing copy 必须调用 Clear Writing
- no controller/watcher/GitHub Action/database/registry/ledger/state machine

除非 v3 amendment 直接破坏这些已批准边界，不要重新移动终点。

## 必须读取

最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_PROPOSAL_2026-09-24.md`

按需读取：

- v2 Proposal / v2 Critic PASS
- v0.1 execution Critic review
- current v0.2 Plan/Goal/Kickoff，只用于确认 amendment 后哪些 execution semantics 需要后续返修
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md`
- current `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`

不要因为读取 machine-update proposal 就顺手审那个独立任务；这里只核对“AI Skills Maintainer 是不是可以被诚实地描述为未来 adaptation normal entry”。

## 用户新增的两个语义

### Amendment A — Codex 第一次要把当前所有 TODO 整理清楚

用户的实际理解是：

> Codex 先把目前所有 TODO 整理进去；后续主要由 GPT 推进。

v3 的解释不是“每个 Markdown heading 机械生成 Issue”，而是：

- 第一次 bootstrap 扫描所有 current canonical TODO inbox；
- 每一个当前仍有维护意义的 TODO 条目都必须有 disposition；
- raw `NEW` 不再仅因 maturity 尚未 promotion 就自动从 Project 隐身；
- 一个仍有效、确属中央 plugin maintenance 的 raw NEW：
  - duplicate -> merge 到已有 tracking Issue；
  - 独立 top-level idea -> 创建 `Project Status=TODO` tracking Issue；
  - source maturity 仍然保持 `NEW`，除非 Planner 另行 promotion triage；
- PROJECT_LOCAL / REJECTED / SUPERSEDED / purely historical resolved 可以不上板，但必须在一次性 coverage evidence 中有明确 disposition；
- Project lifecycle Status 与 plugin TODO maturity 必须继续分开。

v3 建议一次性 evidence：

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

只用于证明没有静默遗漏，不作为长期 registry/schema。

### Amendment B — workflow 只有 server + local machine 都真正适配后才 DONE

用户明确：

> adaptation 我会用 AI Skills Maintainer plugin 解决；只有 adapt 到服务器和 local machine 上，才能算一个 workflow 彻底收尾，而不只是插件做完本身。

v3 因此规定：

- 对 machine-consumed workflow / shared maintenance mechanism：
  - plugin/source/test/release/main integration 不能单独 DONE；
  - central core complete 后进入 ADAPTING；
  - 默认 required downstream consumers：
    1. current canonical server consumer
    2. current canonical local-machine consumer
  - 进入 ADAPTING 时必须解析成真实 consumer identity/locator，不能永久写抽象占位；
  - 两边都必须有实际 adaptation + installed/loaded identity + normal-entry/fresh-session consumption evidence；
  - 只有两边 PASS（或 frozen contract 有合法 N/A）后才能 DONE。
- 普通纯文档、纯审计、单一 artifact/domain improvement 不自动继承双环境要求。
- 用户希望后续用 AI Skills Maintainer 做 adaptation，但 v3 不声称当前 machine-update orchestration 已 production-ready。
- 当前 repo 的 machine-update Proposal/Goal 可以作为未来路线证据；如果该能力尚未正式发布，workflow 就保持 ADAPTING，而不是假 DONE。

## Critic 必须独立判断的问题

### A1 — “全部 TODO 整理进去”是否被正确理解

比较三个方案：

1. raw NEW 继续全部藏在 Markdown，只有 promoted item 上板；
2. 每个 TODO heading 机械 1:1 建 Issue；
3. v3：full coverage + dedupe/disposition + active central raw NEW 可作为 Project TODO，同时 maturity 不变。

请判断哪个最符合用户“我要看清楚所有 backlog”且不会制造第二个垃圾山。

### A2 — raw NEW 上板是否会误导 promotion

Project `Status=TODO` 是否可能被误解为 `CANDIDATE_GENERIC / PROMOTE_NOW`？

v3 通过明确：

`Project lifecycle != plugin TODO maturity`

以及 source TODO maturity 保持不变来隔离。

如果仍不足，要求最小改动；不要新增复杂字段/数据库。

### A3 — coverage evidence 是否必要且不过重

`TODO_COVERAGE.md` 只是一次性 bootstrap evidence。

判断它是否：

- 真能证明所有 current TODO 被处理；
- 不会变成永久 registry；
- 是否有更简单的等价 artifact。

### B1 — server + local 默认双环境 closure 是否合理

重点检查：

- 是否只应用于 machine-consumed workflow/shared mechanism；
- 是否避免把普通 domain plugin/artifact improvement都强行双环境验收；
- 是否仍可能产生“central main done -> false DONE”。

### B2 — required environment 的绑定时机

v3 不在 policy 里硬编码 host/path；进入 ADAPTING 时再解析：

- current canonical server consumer
- current canonical local-machine consumer

并把 exact locator 写入 tracking Issue。

这是否既避免 stale hardcode，又足够可验收？

### B3 — AI Skills Maintainer 表述是否诚实

当前 repo 有 machine-update orchestration 的独立 Proposal/Goal，但不要假定它已 production-ready。

v3 表述是：

- production-ready 后默认用 AI Skills Maintainer 执行 adaptation；
- 尚未 ready -> item 保持 ADAPTING，current anchor 指向 blocker / approved alternative owner；
- board task 不实现它。

请核对这是否避免“未来能力冒充当前能力”。

### B4 — GPT / Codex / Maintainer 分工

v3 steady state：

```text
一次性 full-inbox整理 -> Codex
后续 triage / Planner / Critic / lifecycle truth -> GPT
Project mechanical mutation -> Project-capable Codex/Maintainer
machine adaptation -> AI Skills Maintainer（production-ready 后）
用户 -> 只处理 HUMAN_ONLY
```

检查是否符合 BOARD-SYNC-01，又没有新增 watcher/control plane。

## Alternatives / red team

必须主动找：

- raw NEW 大量上板导致噪音爆炸；
- duplicate merge 把不同问题错误合并；
- source maturity 与 Project status 混淆；
- “server/local”成为永远不解析的抽象标签；
- AI Skills Maintainer 尚未发布却被当作已执行；
- 为了 DONE 强制不相关 plugin也安装到两台机器；
- future optional machine 被追溯加入旧 DONE contract；
- GPT 无 Project mutation能力后又把工作甩给用户。

但 blocker 必须来自真实用户可见风险，不因“还能更保险”增加机制。

## 期望输出

先用自然中文直接回答：

1. Codex 第一次是不是应该整理当前所有 TODO，而不是只挑 promoted item？
2. raw NEW 能不能作为 Project TODO，同时不改变它的 maturity？
3. workflow 是不是只有 server + local 都适配、普通入口都真正消费后才应该 DONE？
4. AI Skills Maintainer 在这里应该是什么角色？

然后给：

```text
RESULT = PASS | REVISE
REVIEW_STAGE = DESIGN_AMENDMENT_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_PROPOSAL_2026-09-24.md
REVIEWED_PROPOSAL_COMMIT = fa40e081e9d30b17d94df7c81a274ad75e5e297b
```

如果 REVISE：

- 只针对这两个 amendment；
- blocker stable IDs；
- 直接证据 / 因果风险 / 最小关闭条件；
- 按 Critic contract 自动生成完整 Planner返修 prompt。

如果 PASS：

- 明确 PASS 只批准 v3 amendment；
- v0.2 execution package 因 admission / DONE contract 已变化，不能直接执行；
- 下一步回 Planner 生成完整 execution package v0.3；
- 自动生成完整 Planner prompt，不让用户拼 locator。

## Review 文件授权

用户若把本 prompt 原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_CRITIC_REVIEW_2026-09-24.md`

并 ordinary non-force push。

除此之外禁止修改：

- Proposal / Plan / Goal / Kickoff；
- AGENTS / TODO / README；
- Project / Issue；
- plugin source；
- AI Skills Maintainer machine-update source；
- Bridge Kit；
- server / local machine / Host；
- 任何其他 repo。

提交后报告 exact review commit。
