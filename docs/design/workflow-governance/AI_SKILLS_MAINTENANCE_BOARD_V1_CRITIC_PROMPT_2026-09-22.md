# AI Skills 维护看板与完成语义 — Critic Prompt v1

你是 AI Research Stack 的独立 Critic thread。请审查 AI_Skills_Collection 新的 maintenance board / work-item lifecycle 设计，不实现、不创建 GitHub Project、不迁移 Issue、不启动 Codex、不调用 paid API。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = DESIGN_PROPOSAL
proposal_path_and_version = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_PROPOSAL_2026-09-22.md v1
proposal_commit = e9804daf12611788f98d9ab3c2577c7744963c03
execution_branch/worktree = NONE
```

## 必须先实际读取

最新 `main`：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `TODO.md`
- `docs/plugin-todos/README.md`
- `docs/plugin-todos/ai-skills-core.md`
- `docs/plugin-todos/workflow-core.md`

当前 review object：

- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_PROPOSAL_2026-09-22.md`

为了核对“中央 integration 与 downstream adaptation 不能混成 DONE”，至少按需读取：

- `docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_PROPOSAL_2026-09-18.md`
- `docs/goals/056_FINAL_INTEGRATION_RELEASE_CLOSURE_GOAL_V0_2.md`
- `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md`

不要因为这些历史任务存在就重新审 056/057/058；只把它们作为 lifecycle 现实证据。

## 独立外部核查

必须独立检查 GitHub 官方当前文档，至少确认：

1. GitHub Projects 的 Status / single-select 是否真的不限制三个值；
2. Board 是否可以用自定义 single-select 分列；
3. built-in automation 的 `issue closed -> Done` 与 auto-add 行为；
4. `gh project` / `gh project item-edit` 是否足以让 Codex/CLI 维护。

优先只用：

- `docs.github.com`
- `cli.github.com`

不要只复述 Planner 的外部结论。

## 用户真正要解决的问题

用户没有时间手工维护插件 backlog。

现在 `docs/plugin-todos/*.md` 越积越多，用户希望一个 GitHub Project / Kanban 一眼看到：

- 哪些 idea 还在 TODO；
- 哪些正在 DOING；
- 哪些已经真正 DONE；
- 每个 DONE idea 到底由哪个 commit 真正解决。

关键补充要求：

> “中央 implementation / integration 完成”不一定等于 idea DONE。  
> 如果这个 idea 还需要适配到具体 server / repo / Host / consumer，只有这些 required adaptation 真正完成后才能算 DONE。

Critic 必须重点判断 **Project 追踪的是 top-level idea，而不是单个 Reviewed Handoff task** 是否正确。一个 idea 可能经历多个 Planner/Critic/Executor task；不要因为其中一个 task 自己 ACHIEVED 就自动把 idea 关闭。

## 本提案的核心主张

v1 建议：

```text
TODO -> DOING -> ADAPTING -> DONE
```

其中：

- TODO：triage 后值得追踪，但未 active；
- DOING：Planner/Critic/implementation/review/central integration 正在推进；
- ADAPTING：canonical source 已落地，但 completion contract 中 required downstream consumers 还未全部适配并验证；
- DONE：中央 source + required adaptation + normal-entry validation 全部闭环，且 `Resolution commit` 已记录。

不需要 downstream adaptation 的 item 可以 `DOING -> DONE`。

`WAITING / BLOCKED` 不作为主状态；用 Issue label + Blocked by/Next action 表示，因为等待可能发生在 DOING 或 ADAPTING 的任何阶段。

## 必须攻击的八个问题

### C1 — 三状态还是四状态

请独立比较：

A. `TODO / DOING / DONE`，中央 integration 后但 adaptation 未完仍保持 DOING；

B. `TODO / DOING / ADAPTING / DONE`；

C. 三状态 + 单独 Phase 字段；

D. 更多细状态（Planning / Review / Integration / ...）。

不能因为“四个看起来更清楚”就 PASS。必须判断长期维护成本和真实信息增益。

### C2 — ADAPTING 会不会无限扩大 DONE

检查 required adaptation 的边界是否足够严格。

不能出现：

> “还有任何 repo/server 以后可能想升级” -> 永远不能 DONE。

只有 frozen completion contract 中必要 consumer，或者后续新证据证明“不适配这个 consumer，原本声称的能力实际上没有交付”，才允许阻塞 DONE。

### C3 — idea vs task 是否分层正确

检查是否应该：

- Project item = top-level idea；
- Reviewed Handoff task = implementation/review evidence；
- plugin TODO = failure/evidence inbox。

若不同意，请给更简单且不会重复维护的替代。

### C4 — Resolution commit 是否真实

Planner 要求每个 DONE item 有：

```text
Resolution commit = owner repo 的 canonical closure commit
```

它不是第一版 implementation SHA，而是第一次让 top-level idea 满足 DONE contract 的可追踪 commit。

对于 server mutation 没有 SHA 的情况，runtime evidence 可单独保存，但最终 owner repo closure commit 应引用这些证据。

请检查：

- 这是不是假精确；
- 是否应该记录一个 commit 还是多个；
- Project text field + Issue closing comment 是否足够；
- 是否会制造自引用 commit 问题。

### C5 — TODO / Issue / Project 会不会三份重复

检查 v1 的 admission rule：

- 原始 `NEW` 不自动入 Project；
- Planner triage 后仍需持续追踪的独立 idea 才创建 tracking Issue；
- TODO 保存 evidence/maturity + `tracking: #N`；
- Project/Issue 保存 execution lifecycle；
- 不复制 execution status 回 Markdown。

是否足以防漂移？

### C6 — GitHub automation 是否会误关

特别检查：

- Issue close -> DONE 是否安全；
- PR merged -> DONE 是否必须关闭/避免；
- tracking Issue 是否应在 adaptation 完成前保持 open；
- 是否应该使用 label auto-add。

### C7 — 是否过重

本方案禁止：

- 自研数据库；
- registry/ledger/controller；
- 新状态机；
- 把每个 workflow internal phase 变成 Project status；
- 为了当前 ChatGPT connector 不支持 Projects 而自建 service。

检查是否仍然有不必要机制。

### C8 — 长期无人手工维护是否可行

用户希望 Planner/Codex/thread 自动维护，不是用户自己拖卡。

检查 `gh project` + GitHub built-in automation 是否足够；如需用户一次性 token scope / project setup，可以接受，但不要设计持续人工维护。

## Alternatives / reality check

必须至少比较一个现实替代，不只评价 v1。

Critic 可以判定：

- 三状态已经足够，拒绝 ADAPTING；
- 四状态合理；
- 或需要别的极简方案。

但不能新增复杂 Control / watcher / database / project-sync daemon 来解决本问题。

## 期望输出

先用自然中文回答用户最关心的结论：

> GitHub 技术上是否只能三个状态？  
> 这套仓库实际上应该用几个状态？  
> DONE 的真实边界是什么？

然后给：

```text
RESULT = PASS | REVISE
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_PROPOSAL_2026-09-22.md
REVIEWED_PROPOSAL_COMMIT = e9804daf12611788f98d9ab3c2577c7744963c03
REVIEW_STAGE = DESIGN_PROPOSAL
```

若 `REVISE`：

- blocker 使用稳定编号；
- 每条必须包含直接证据、因果风险、最小关闭条件；
- 按 Critic Role Contract 自动生成完整 Planner 返修 prompt。

若 `PASS`：

- 明确 PASS 只批准设计，不授权创建 Project、改 Issue、改 AGENTS 或执行 backfill；
- 下一步应回 Planner 准备最小 execution package；
- 按 Critic Role Contract 自动生成完整 Planner prompt。

## Review 文件授权

用户若把本 prompt 原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增一份：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_CRITIC_REVIEW_2026-09-22.md`

并做 ordinary non-force push。

除此之外禁止修改：

- Proposal；
- AGENTS；
- TODO；
- plugin source；
- GitHub Project / Issue；
- Bridge Kit；
- 任何其他 repo；
- production / server / Host。

提交后报告 exact commit。
