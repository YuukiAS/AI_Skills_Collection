# AI Skills 维护看板 — Execution Critic Review v0.3

- 日期：2026-09-24
- Review stage：`EXECUTION_READY_REVIEW_V0_3`
- Result：`REVISE`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- package version：`v0.3`
- package snapshot commit：`aa0eb3e0e57714013f6de6eeb5d820efda2384cc`
- execution branch：`reviewed/repo--maintenance-board-lifecycle`
- execution worktree：`../AI_Skills_Collection-repo--maintenance-board-lifecycle`
- approved design：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- approved design commit：`d14565e152b9b953c76c0722ad6e6343850335a7`

## 1. 结论

v0.3 已经完整吸收了 v5 的主要 execution semantics：

- 四状态保持 `TODO -> DOING -> ADAPTING -> DONE`；
- full-inbox bootstrap + raw NEW 可见性；
- Clear Writing + actual Project surface review；
- BOARD-01 false-DONE guardrails；
- ChatGPT Project instructions / AGENTS / Planner-Critic contracts 的 normal-entry binding；
- central implementation complete 与最终 five-consumer DONE 的两层完成语义；
- Maintainer per-current-consumer、Project aggregate five consumers；
- initial Kickoff 不授权 server/local machine mutation；
- no standalone Kanban skill / cross-machine controller；
- NONE / NO_BUMP 与 private README no-update 默认边界。

GitHub bootstrap 路线也仍然真实：当前 `gh project` 提供 create/edit/link/field-create/field-list/item-add/item-edit/item-list，并要求 `project` scope；GitHub built-in Project workflows 仍可在 Project Workflows UI 配置和 enable/disable，auto-add 支持 `is:issue` 与 `label:` filter。ChatGPT Project instructions 与 Codex `AGENTS.md` 也仍是两个正确的 normal-entry instruction surface。

但 execution package 漏掉了一个已经在 approved v2 设计中冻结、而在 full-inbox 模式下更加关键的 source-to-board locator：**真正的 plugin/skill TODO entry 必须能保存 `tracking: #N`，但 v0.3 的 allowed repo scope 禁止修改这些 canonical inbox files。**

因此当前不能 `READY_FOR_CODEX=YES`。

## 2. 已通过的 execution boundaries

### 2.1 Full-inbox / maturity separation

PASS。

v0.3 会扫描 root `TODO.md` 正式声明的 central plugin / standalone-skill inbox，对每个 current meaningful entry 给 disposition，不机械一 heading 一 Issue。

valid central raw `NEW` 可以成为 Project TODO，同时 source maturity 保持 `NEW`，没有把 lifecycle admission 冒充 promotion。

`TODO_COVERAGE.md` 只是一轮 bootstrap completeness evidence，不被当成长期 registry/schema。

### 2.2 Human-readable surface / Clear Writing

PASS。

Package 不再允许“字段存在 = 用户可读”：

- natural Issue title；
- 问题 / 当前进度 / 当前执行锚点 / 下一步；
- DOING/ADAPTING current valid anchor；
- actual Board / By area / Issue surface qualitative review；
- Clear Writing invocation 只是 supporting evidence，不能替代 surface review。

### 2.3 BOARD-01

PASS。

full-inbox backfill 没有重新引入假 DONE：

- lifecycle item only tracking Issue；
- issue-only auto-add；
- PR merged -> Done disabled；
- early auto-closing link/keyword prohibited；
- non-completion item remove/archive before truthful close；
- final issue-close -> Done only after complete closure。

### 2.4 Bootstrap route

PASS。

当前官方 GitHub CLI / Project workflow现实与 Plan 一致。

如果 built-in workflow 仍只能通过 UI 配置，one-time HUMAN_ONLY setup + actual readback 是合法恢复，不需要 GitHub Action/service/controller。

### 2.5 Normal-entry consumer binding

PASS。

canonical policy 只有一份，其他 surface 都是 short trigger/locator：

- ChatGPT Project instructions；
- AI_Skills AGENTS；
- Planner Role Contract；
- Critic Role Contract；
- TODO / plugin TODO README ownership说明。

no-tool surface 输出 exact pending mutation，不把 routine Kanban维护甩给用户。

### 2.6 Central / ADAPTING / DONE

PASS。

execution-ready Critic PASS、Executor 自报完成、implementation review PASS 但 canonical closure 尚未完成，都不能进入 ADAPTING。

只有 central implementation complete 后，machine-consumed item 才进入 ADAPTING。

五个 required logical consumers仍是：

- Longleaf_Codex
- Longleaf_Backup_Codex
- CUHK_Workstation_WSL_Codex
- Workstation
- Legion

每台 future Maintainer 是 per-current-consumer executor；tracking Issue / Project是 aggregate owner。

### 2.7 Initial machine authorization boundary

PASS。

initial v0.3 Kickoff只授权 central implementation，不授权 server/local mutation。machine/credential/remote authority 在 ADAPTING 阶段按 exact consumer separately授权是正确的 bounded authorization。

如果解析 exact consumer identity 本身需要访问某一 machine，必须先经过同一 per-consumer authority gate；不得为了“先冻结 locator”而无授权访问或猜测。现有 stop/recovery contract足以承载这一点，因此不形成独立 blocker。

## 3. Stable blocker

### BOARD-TRACKING-LOCATOR-01 — v0.3 无法把 tracking Issue locator 写回 canonical TODO inbox

**已批准要求**

approved v2 Proposal 明确规定：

```text
对应 plugin TODO 只保存：

tracking: #<issue-number>

以及自身的 evidence/maturity 语义；
不要把 Project Status 回写成第二份执行状态。
```

这个 locator 是 TODO inbox 与 top-level tracking Issue 之间唯一允许的 durable backlink。

后续 v3-v5 改变了 raw NEW admission / full-inbox coverage / machine closure，但没有取消这个 locator contract。

**直接证据**

v0.3 Plan / Goal / Kickoff 的 allowed central repository modifications 只包括：

- `AGENTS.md`
- root `TODO.md`
- `docs/plugin-todos/README.md`
- canonical board doc
- Planner/Critic contracts
- optional README
- results / control evidence

并**不允许修改**：

- `docs/plugin-todos/<plugin>.md`
- `docs/skill-todos/<skill>.md`

与此同时，v0.3 会为 valid raw NEW / active top-level idea 创建或复用 tracking Issue。

v0.3 还明确规定 `TODO_COVERAGE.md` 只是一次性 bootstrap evidence，不能成为长期 registry/status source。

因此执行后会出现：

```text
canonical TODO entry
-> Project tracking Issue exists
-> TODO_COVERAGE temporarily knows mapping
-> canonical TODO entry itself has no tracking locator
```

**因果风险**

这会直接破坏 steady-state 自动维护：

- 后续 Planner/GPT 从 canonical plugin TODO 进入时，无法稳定知道该 entry 已绑定哪个 tracking Issue；
- dedupe/reconcile 需要重新搜索/猜映射；
- 容易创建 duplicate tracking Issues；
- 或被迫把一次性 `TODO_COVERAGE.md` 当长期 lookup registry，违反已批准设计；
- 用户最终仍可能看到 Markdown TODO 与 Project 卡片关系漂移。

这是用户可见的真实维护失败，不是文档格式问题。

**最小关闭条件**

Planner 只需做 v0.4 execution-package 小修，不需要重开 design：

1. 在 Plan / Goal / Kickoff 的 allowed repo scope 中增加当前 canonical maintenance inbox files：
   - `docs/plugin-todos/*.md`
   - root `TODO.md` 正式列出的 `docs/skill-todos/*.md`
   - 仅限当前 root TODO 声明的 canonical inbox，不扩大到任意 repo files。

2. 对 bootstrap 中 disposition 为：
   - `TRACKED`
   - `MERGED_INTO_TRACKING_ISSUE`
   
   的每个 canonical source entry，写入或更新：
   
   ```text
   tracking: #<issue-number>
   ```
   
   多个 duplicate source entries 可以指向同一个 tracking Issue。

3. locator-only mutation 不得：
   - 改 source maturity；
   - 把 Project Status 复制回 Markdown；
   - 顺手改 problem/evidence/candidate action；
   - 把 non-central / rejected / historical item强行上板。

4. B3/B6/normal-entry validation 增加：
   - every TRACKED/MERGED canonical source entry has the correct durable tracking locator；
   - reused existing Issue也必须回写正确 locator；
   - `TODO_COVERAGE.md` 仍只证明 bootstrap completeness，不承担长期 mapping。

5. steady-state canonical board doc 明确：
   - 新建/bind tracking Issue时，同一维护动作自动回写 `tracking: #N`；
   - Issue复用/merge时更新为真实 locator；
   - routine sync不要求用户手工补 locator。

这只是实现 approved architecture 所需的 source backlink，不新增字段、状态、registry、watcher 或 control plane。

## 4. Non-blocking notes

- GitHub CLI / UI bootstrap route：无新 blocker。
- ChatGPT Project instructions one-time HUMAN_ONLY setup：有真实 platform boundary，且 package禁止未设置就声称成功，无新 blocker。
- exact sibling worktree：fail-closed 合理，无证据证明必然不可执行。
- five-consumer machine effects：initial Kickoff正确不授权；后续按 exact consumer再授权。
- version：Repository NONE / all plugins NO_BUMP 仍正确。
- README：private Project 下默认 no update required 仍正确。

## 5. 审查结论

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW_V0_3
PACKAGE_SNAPSHOT_COMMIT = aa0eb3e0e57714013f6de6eeb5d820efda2384cc
READY_FOR_CODEX = NO

STABLE_BLOCKERS =
- BOARD-TRACKING-LOCATOR-01
```

本轮没有重新打开 BOARD-01、BOARD-UX-01、BOARD-SYNC-01、BOARD-CONSUMER-01、BOARD-MAINTAINER-SCOPE-01 或 v5 lifecycle。

只需要让 v0.3 已经承诺的 `tracking: #N` source locator 真正可写、可验收，再复核 execution package。
