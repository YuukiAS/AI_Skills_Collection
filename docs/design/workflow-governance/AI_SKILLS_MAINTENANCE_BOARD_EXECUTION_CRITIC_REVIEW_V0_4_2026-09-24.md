# AI Skills 维护看板 — Execution Critic Review v0.4

- 日期：2026-09-24
- Review stage：`EXECUTION_READY_REVIEW_V0_4`
- Result：`REVISE`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- package version：`v0.4`
- package snapshot commit：`696c1bebad3e7f2dbe65026a02de3bdb4cf21117`
- execution branch：`reviewed/repo--maintenance-board-lifecycle`
- execution worktree：`../AI_Skills_Collection-repo--maintenance-board-lifecycle`
- approved design：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- approved design commit：`d14565e152b9b953c76c0722ad6e6343850335a7`
- previous execution review：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-24.md`
- previous execution review commit：`98b7b875eabedb773f0d1d5bcdcd23217cc9b055`
- rechecked blocker：`BOARD-TRACKING-LOCATOR-01`

## 1. 结论

`BOARD-TRACKING-LOCATOR-01` 已经实质关闭。

v0.4 现在同时具备：

- 创建 / reuse / merge tracking Issue 的 GitHub authority；
- 对 canonical plugin / standalone-skill TODO entry 写回 `tracking: #N` 的合法 repo-file authority；
- locator-only 边界，禁止借 backlink edit 改 maturity/problem/evidence/candidate action；
- TRACKED / MERGED / reused / rebind 的 steady-state backlink contract；
- 直接验证 source backlink 与 Project mapping；
- `TODO_COVERAGE.md` 继续只做一次性 completeness evidence，不承担长期 mapping。

因此 v0.3 的“设计要求 backlink，但合法 file scope 不允许写”的 contradiction 已关闭。

但是 v0.4 为关闭该 blocker 新增的动态 file-scope 语句存在一个新的、直接影响 execution authorization 的漏洞：**同一 task 允许修改 root `TODO.md`，同时又允许“execution-time current root TODO 新声明的 canonical inbox”自动进入 locator-write authority；这使 allowed file set 在字面上可以被 task 自己扩张。**

所以当前不能 `READY_FOR_CODEX=YES`。

## 2. BOARD-TRACKING-LOCATOR-01 复核

### L1 — blocker 已关闭

PASS。

v0.4 Plan / Goal / Kickoff 三者均明确：

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
-> same maintenance action
-> source entry tracking: #<issue-number>
```

并覆盖：

- independent entry -> own Issue；
- duplicate / merged entries -> shared top-level Issue；
- reused Issue -> actual reused number；
- merge / rebind -> update every affected source entry；
- raw NEW maturity stays NEW；
- Project Status does not go back to Markdown。

### L2 — locator-only substantive boundary

PASS。

locator authority 明确不能改变：

- source maturity/status；
- problem；
- evidence；
- project-specific context；
- target layer；
- candidate action；
- promotion gate；
- other substantive TODO fields；
- Project lifecycle Status。

non-tracked disposition 也不会为了 completeness 被强制加 locator。

### L3 — source truth

PASS。

canonical TODO 保留 evidence / maturity，Project 保留 execution lifecycle，`tracking: #N` 只是 durable source-to-Issue backlink。

GitHub 官方当前文档说明 issue references such as `#123` 是标准 repository-scoped issue identifier；在 repository files 中它不保证自动渲染为 clickable autolink，但这不影响本设计把它作为 machine/human-readable locator。当前 approved design 不要求它必须在 source Markdown 中自动变成链接。

### L4 — duplicate / reuse / rebind

PASS。

多个 canonical source entries 可以共享同一个 top-level Issue；reuse existing Issue 必须写实际 Issue number；rebind 会更新所有 affected source entries。

existing locator conflict 无法无歧义解析时 fail closed，不猜 mapping。

### L5 — TODO_COVERAGE 边界

PASS。

`TODO_COVERAGE.md` 仍然只记录 bootstrap completeness：

```text
source entry -> disposition -> Issue -> Area -> initial Status
```

steady-state mapping 明确来自 canonical source entry 自己的 `tracking: #N`，没有退化为第二 registry。

### L6 — validation

PASS。

v0.4 已加入直接检查：

- every TRACKED entry has correct locator；
- every MERGED entry has correct shared locator；
- reused Issue number correctly written back；
- non-tracked entry has no forced locator；
- raw NEW maturity unchanged；
- locator-only edits do not mutate substantive TODO content；
- Project Status not copied to Markdown；
- TODO_COVERAGE not used as runtime lookup；
- steady-state create/bind/reuse/merge maintains source backlink。

这些检查针对真实 mapping，而不是字符串存在就 PASS。

## 3. New stable blocker

### BOARD-LOCATOR-SCOPE-01 — canonical inbox write scope 可以被当前 task 自己通过 root TODO 动态扩大

**直接证据**

v0.4 Kickoff / Plan 同时允许：

1. 当前 task 修改 root `TODO.md`；
2. locator-only 修改 kickoff-time root TODO 已声明的 canonical inbox；
3. 并额外允许：
   > execution-time current root TODO 如果正式新增其他 canonical maintenance inbox，也允许对这些 newly declared inbox 做 tracking-locator maintenance。

root `TODO.md` 本身正是当前 task 的合法修改面。

因此字面执行合同存在：

```text
task edits root TODO
-> adds another path as "canonical maintenance inbox"
-> that path becomes locator-write authorized
```

即使 Planner 的意图不是这样，Kickoff 是未来 current-user authorization envelope，不能依赖 Executor 自己推断“我不应该利用这条动态扩权”。

当前 root `TODO.md` 已经足够明确地列出十个 central plugin inbox 和一个 standalone-skill inbox；本任务没有现实需要让自己在执行中扩大 canonical inbox write set。

**因果风险**

这是实际授权边界问题：

- current task 可以在运行中扩大自身可写文件集合；
- 新加入的 path 未经过本次 execution-ready review；
- 可能把 locator-only write 权限带到原本不在冻结 scope 的 maintenance file；
- 与 exact bounded authorization / fail-closed 原则冲突。

这不是假设 hostile Executor。普通实现只要在更新 root TODO 文档时顺便新增一个 maintenance inbox，就会使后续合法 scope发生变化，导致 review object 与实际 write set不再一致。

**最小关闭条件**

不需要重开 design，也不需要删掉 locator support。

v0.5 execution package只需把 canonical inbox set冻结在 kickoff preflight：

1. 在任何 task mutation 前，从 **unmodified kickoff-base root `TODO.md`**（即 kickoff-time latest `origin/main`）解析 exact canonical inbox paths；
2. 把 exact list记录到 repo evidence；
3. 本 task locator-only authority只适用于这份 frozen list；
4. task 后续自己对 root `TODO.md` 的修改**不能**扩大 allowed inbox set；
5. 如果 kickoff 之后 latest-main drift 新增 canonical inbox：
   - 默认不自动获得 write authority；
   - 若该 inbox 必须纳入本次 bootstrap，按现有 semantic-drift / scope-expansion规则返回 Planner/用户；
6. 不需要硬编码今天的十一条 path到长期 policy；只需 preflight snapshot freeze。

当前 root TODO 的 declared inbox set可作为执行时的 starting source，但 authority必须来自 pre-mutation snapshot，而不是 task-mutated root TODO。

## 4. v0.3 其余 execution architecture

没有发现 v0.4 对此前已通过部分造成回归。

继续 PASS：

- `TODO -> DOING -> ADAPTING -> DONE`
- full-inbox coverage；
- raw NEW Project TODO / maturity unchanged；
- Clear Writing + actual Project surface review；
- BOARD-01；
- GitHub Project bootstrap route；
- ChatGPT Project instructions one-time setup；
- AGENTS / Planner / Critic proactive sync；
- no-tool exact pending mutation；
- central implementation complete -> ADAPTING；
- five logical consumers；
- per-current-consumer Maintainer；
- no cross-machine controller；
- initial central Kickoff no server/local mutation；
- exact branch/worktree fail-closed；
- Repository NONE / plugins NO_BUMP；
- private README no-update default；
- no standalone Kanban skill/plugin；
- no Action/controller/watcher/database/registry/ledger。

## 5. 审查结论

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW_V0_4
PACKAGE_SNAPSHOT_COMMIT = 696c1bebad3e7f2dbe65026a02de3bdb4cf21117
READY_FOR_CODEX = NO
RECHECKED_BLOCKERS = BOARD-TRACKING-LOCATOR-01
CLOSED_BLOCKERS = BOARD-TRACKING-LOCATOR-01
NEW_BLOCKERS = BOARD-LOCATOR-SCOPE-01
```

本轮只新增了由 v0.4 scope expansion wording 本身引入的 execution-authorization blocker，没有移动其他已关闭终点。
