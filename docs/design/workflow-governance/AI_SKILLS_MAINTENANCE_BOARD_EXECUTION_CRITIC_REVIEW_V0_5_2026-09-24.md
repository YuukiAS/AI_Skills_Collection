# AI Skills 维护看板 — Execution Critic Review v0.5

- 日期：2026-09-24
- Review stage：`EXECUTION_READY_REVIEW_V0_5`
- Result：`PASS`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- package version：`v0.5`
- package snapshot commit：`d2afbc0fa984a14b659a416fdab5089566549861`
- execution branch：`reviewed/repo--maintenance-board-lifecycle`
- execution worktree：`../AI_Skills_Collection-repo--maintenance-board-lifecycle`
- approved design：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- approved design commit：`d14565e152b9b953c76c0722ad6e6343850335a7`
- previous execution review：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_4_2026-09-24.md`
- previous execution review commit：`f8203829641588322215fba585a5fd6844240853`
- rechecked blocker：`BOARD-LOCATOR-SCOPE-01`

## 1. 结论

`BOARD-LOCATOR-SCOPE-01` 已关闭，v0.5 execution package 可以进入 central implementation。

上一轮 blocker 的问题是：v0.4 同时允许 task 修改 root `TODO.md`，又让“execution-time current root TODO 新声明的 canonical inbox”自动获得 locator-write authority，导致 task 可能通过自己修改 root TODO 扩大可写文件集合。

v0.5 已把 authority source 移到 task mutation 之前的 kickoff base：

1. fetch kickoff-time latest `origin/main`;
2. 记录 exact `KICKOFF_BASE_COMMIT`;
3. 从该 exact commit 读取 unmodified root `TODO.md`;
4. 只解析正式的 structured canonical-inbox navigation entries；
5. 验证 path 在同一 base 存在；
6. freeze exact path set；
7. 从同一 base 创建 reviewed branch/worktree；
8. 第一份 task-content evidence 必须是
   `results/repo--maintenance-board-lifecycle/FROZEN_CANONICAL_INBOX_ALLOWLIST.md`;
9. frozen allowlist 形成后，后续 task-mutated root TODO 不得扩大 authority。

因此 task 自己已经不能通过修改 root TODO 扩大 locator-write scope。

本轮没有新的 direct blocker。

## 2. 外部现实核查

本轮独立核对 GitHub 官方当前 REST 文档。

GitHub “Get repository content” endpoint 支持 `ref` query parameter，官方定义为 commit / branch / tag name；因此从 exact `KICKOFF_BASE_COMMIT` 读取 root `TODO.md` 是受支持的真实路径。

GitHub “Get a commit” endpoint 也接受 commit reference，并返回对应 commit identity。

采用结论：

> v0.5 用 exact kickoff commit 固定 authority source，而不是从 moving task branch / later-mutated root TODO 派生 allowlist，现实可执行。

来源：

- https://docs.github.com/en/rest/repos/contents
- https://docs.github.com/en/rest/commits/commits

## 3. S1 — BOARD-LOCATOR-SCOPE-01

PASS。

locator-write authority 现在来自：

```text
unmodified kickoff-time origin/main
-> exact KICKOFF_BASE_COMMIT
-> root TODO at that exact commit
-> structured canonical-inbox navigation
-> frozen exact path set
```

而不是：

```text
task-mutated root TODO
-> dynamic scope
```

self-expanding authorization envelope 已被关闭。

## 4. S2 — freeze 时机

PASS。

Plan / Goal / Kickoff 三者都要求在：

- task tracked-file mutation；
- Project / Issue creation；
- backfill

之前完成 freeze。

branch/worktree creation 被明确限定为 bootstrap identity setup，并从同一 exact base 创建，不改变 repository content。

第一份 task-content evidence 必须是 frozen allowlist artifact，因此后续 Reviewer 能直接验证“authority 在何时冻结”。

## 5. S3 — parser 边界

PASS。

parser 只接受 root `TODO.md` 中正式声明 maintenance inbox 的 structured navigation entries；当前就是：

- plugin TODO entry table；
- standalone-skill TODO entry table。

明确排除：

- explanatory prose 中的 incidental links；
- examples；
- changelog links；
- workflow docs；
- arbitrary Markdown links。

若 root TODO 格式歧义到需要猜测，execution fail closed before locator write / backfill。

当前不需要新增 parser schema 或 registry。

## 6. S4 — post-kickoff drift

PASS。

post-kickoff upstream main 新增 inbox：

- 不自动获得 locator authority；
- 不静默扩大本次 full-inbox completeness claim；
- 如果它对当前 task 是语义必需，返回 Planner/user 做 scope expansion；
- 否则 defer，并在 closure evidence 记录。

这与 bounded execution 一致，也避免了为了“保持最新”引入 watcher / moving allowlist。

## 7. S5 — freeze evidence 不过重

PASS。

`FROZEN_CANONICAL_INBOX_ALLOWLIST.md` 只记录：

- kickoff base commit；
- root TODO blob SHA；
- frozen count；
- exact paths；
- 可选 parsing rule / section names。

它是 bounded task evidence，不是 long-lived registry、runtime source、watcher 或 service。

它回答的是本次 authorization provenance，而不是维护新的产品状态。

## 8. S6 — full-inbox claim

PASS。

v0.5 把“全部 current TODO”诚实地定义为：

> complete for the frozen kickoff-base canonical inbox allowlist

而不是对执行过程中不断变化的 post-kickoff universe 做无限 moving claim。

这仍满足用户的 bootstrap 目标：执行开始时的 canonical backlog 被完整整理；执行过程中后来新增的 inbox 不被偷偷纳入未审 scope。

## 9. S7 — tracking-locator architecture

继续 PASS，无回归。

保留：

- TRACKED / MERGED -> `tracking: #N`;
- independent entry -> own Issue；
- duplicate entries -> shared Issue；
- reused Issue -> actual reused number；
- merge / rebind -> update affected source entries；
- raw NEW maturity unchanged；
- locator-only mutation；
- Project Status 不回写 Markdown；
- non-tracked item 不强制 locator；
- ambiguous mapping fail closed；
- TODO_COVERAGE 只是一轮 completeness evidence。

validation 也直接检查：

- frozen source provenance；
- locator edit path membership；
- no write outside frozen list；
- task-mutated root TODO 不扩权；
- post-kickoff inbox 不静默纳入；
- TRACKED / MERGED backlinks；
- substantive TODO fields unchanged。

## 10. v0.4 已通过 execution boundaries

v0.5 没有对上一轮已通过部分造成回归。

继续批准：

- `TODO -> DOING -> ADAPTING -> DONE`
- full-inbox；
- raw NEW Project TODO / maturity unchanged；
- Clear Writing；
- actual Project surface qualitative review；
- BOARD-01；
- GitHub Project bootstrap；
- ChatGPT Project instructions one-time setup；
- AGENTS / Planner / Critic proactive sync；
- no-tool exact pending mutation；
- durable `tracking: #N`；
- central implementation complete -> ADAPTING；
- five logical consumers；
- per-current-consumer Maintainer；
- no cross-machine controller；
- initial central Kickoff 不授权 server/local mutation；
- exact branch/worktree fail-closed；
- Repository NONE / all plugins NO_BUMP；
- private README no-update default；
- no standalone Kanban skill/plugin；
- no Action/controller/watcher/database/registry/ledger。

## 11. PASS 的边界

本 PASS 证明：

- v0.5 Plan / Goal / Kickoff 同版一致；
- initial central execution scope 已冻结并可执行；
- `BOARD-LOCATOR-SCOPE-01` 已关闭；
- package 可以交给 Codex 开始 central implementation。

本 PASS 不证明：

- GitHub Project 已创建；
- Project workflows 已配置；
- full-inbox 已完成；
- Clear Writing 已真实调用；
- ChatGPT Project instructions 已安装；
- implementation 已通过独立 review；
- main integration 已完成；
- AI Skills Maintainer machine-update capability 已 production-ready；
- 五个 consumer 已适配；
- overall Goal 已 DONE。

initial Kickoff 仍不授权 server/local machine mutation；这些 downstream effects 要在 ADAPTING 阶段按 exact consumer 重新绑定 current-user authority。

## 12. 审查结论

```text
RESULT = PASS
REVIEW_STAGE = EXECUTION_READY_REVIEW_V0_5
PACKAGE_SNAPSHOT_COMMIT = d2afbc0fa984a14b659a416fdab5089566549861
RECHECKED_BLOCKERS = BOARD-LOCATOR-SCOPE-01
CLOSED_BLOCKERS = BOARD-LOCATOR-SCOPE-01
NEW_BLOCKERS = NONE
APPROVED_PROPOSAL_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_5_2026-09-24.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_5.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_5.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
```
