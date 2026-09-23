# AI Skills 维护看板 — Implementation Plan v0.2

- Date: 2026-09-22
- Human label: AI Skills 维护看板与完成语义
- Task key: `repo--maintenance-board-lifecycle`
- Repository: `YuukiAS/AI_Skills_Collection`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`
- Approved design commit: `da46f14141888c1bcd94bf94a486bcb1a1b0ec7c`
- Design Critic PASS: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`
- Design Critic review commit: `8213c843b4d91c63f6de62740e26ef8d215a59e0`
- Previous execution review: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-22.md`
- Previous execution review commit: `4aaa95d79e84af63c93362612988cf79829d8043`
- Package version: `v0.2`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Execution branch: `reviewed/repo--maintenance-board-lifecycle`
- Exact task worktree: sibling `../AI_Skills_Collection-repo--maintenance-board-lifecycle`, resolved from the canonical AI_Skills_Collection checkout root.
- This Plan does not itself authorize execution.

## 1. 本轮结论

v0.2 不重新设计 lifecycle，继续使用已经通过独立 Critic 的：

```text
TODO -> DOING -> ADAPTING -> DONE
```

本轮只关闭 execution review 的两个 stable blockers：

```text
BOARD-UX-01 = ACCEPT
BOARD-SYNC-01 = ACCEPT
```

新增的执行合同只有两类：

1. **看板必须真正给人看。** tracking Issue 的标题、顶部摘要、当前锚点和下一步必须自然、简洁、可直接读；Codex 只要创建或修改这些看板文字，必须调用 Clear Writing（`writing-style`）做最终语言层处理。
2. **Planner / Critic / maintenance thread 必须主动同步。** 看板不是 Codex 单独负责的账本。每次进入 tracking scope、开始实质设计、完成 review、进入 downstream adaptation 或最终 closure 时，当前语义 owner 都要主动 reconcile Issue / status / evidence；不能等用户提醒。

这两条不增加第五状态，不增加 Project 字段，不新增 controller、watcher、GitHub Action、database、registry、ledger 或另一套状态机。

## 2. Frozen implementation identity

### Git

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = latest origin/main at kickoff preflight
```

worktree locator 是 exact locator。执行时先从 canonical repo root 唯一解析 absolute path，并写入 `results/repo--maintenance-board-lifecycle/RESULT.md`。

如果当前 Host/sandbox 无法合法创建 exact approved worktree，必须在任何 Project / Issue mutation 之前停止。不得静默换成 `/tmp`、dirty checkout、alternate branch 或 alternate path。若执行时已经存在 sanctioned Bridge-owned bounded worktree primitive，只允许它执行同一 exact locator，不改变本任务语义。

### GitHub Project

```text
owner = YuukiAS
title = AI Skills Maintenance
visibility = PRIVATE
linked repository = YuukiAS/AI_Skills_Collection
tracking label = maintenance-track
```

Project 默认保持 PRIVATE，因为这是 maintainer 直接消费的工作面板。底层 public Issue / TODO 仍按现有 repo privacy 规则处理。

## 3. Allowed repository changes

只允许修改：

- `AGENTS.md`：增加简短 mandatory board locator / consumer rule，并明确 Codex 修改看板文字时必须调用 Clear Writing；
- `TODO.md`：解释 plugin TODO inbox 与 Project dashboard 的分工；
- `docs/plugin-todos/README.md`：允许 `tracking: #N` locator，但不复制 execution status；
- 新 `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`：canonical steady-state board contract；
- `README.md`：仅在 closure check 证明确需更新时修改；
- `results/repo--maintenance-board-lifecycle/**`：非敏感 bootstrap / surface review / backfill / validation / closure evidence；
- current task 的普通 Reviewed Handoff/control evidence，只在现有 repo contract 真正要求时写入。

禁止修改：

- `skills/`；
- generated Marketplace/plugin payload；
- plugin routing/runtime；
- profile；
- Bridge Kit；
- server / Host；
- provider / credential；
- production application behavior。

版本决策保持：

```text
Repository bump decision: NONE
Affected plugins: all NO_BUMP
```

原因：本任务只增加 maintenance docs + GitHub Project metadata，不改变 install/runtime/plugin production behavior。

## 4. 用户真正消费的看板契约

这个 Project 不是内部机器账本，而是用户直接查看当前插件维护状态的界面。结构正确但难读，视为失败。

### 4.1 Tracking Issue title

Issue title 必须：

- 用自然、简洁的人类语言直接说问题或工作目标；
- 默认优先使用自然中文；plugin / product / method 的正式专有名可保留；
- 不把 task key、branch、hash、文件路径、内部状态串作为标题主体；
- 不写成 `repo--maintenance-board-lifecycle / READY_FOR_...` 这类机器标题。

例如：

```text
好：让插件维护看板能区分“已集成”和“已真正适配完成”
坏：repo--maintenance-board-lifecycle / BOARD-SYNC-01 / reviewed/...
```

### 4.2 Issue 顶部摘要

每个 tracking Issue 顶部固定保留一个短的人类可读区，顺序为：

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

含义：

- **问题**：一句话说清这个 top-level idea 解决什么；
- **当前进度**：用自然语言说明现在处于 TODO / DOING / ADAPTING / DONE 的真实含义，不复述内部状态名；
- **当前执行锚点**：只突出当前仍有效的 proposal / workflow / task / branch / PR / commit locator，必须先用人话说明它是什么，再给 locator；
- **下一步**：说明真正下一动作以及谁负责，不写泛化的“继续推进”。

详细 historical evidence、旧 review、component commits、runtime logs 等全部放到后面的 Evidence / History 区，不挤进顶部摘要。

### 4.3 当前执行锚点

每个 `DOING` / `ADAPTING` item 至少必须有一个仍然有效的当前执行锚点。

合法锚点包括：

- 当前 proposal / execution package；
- active workflow / task；
- exact reviewed branch；
- active PR；
- canonical integration commit；
- downstream adaptation repo/branch/commit；
- current runtime validation locator。

不允许只堆历史 locators，让用户自己猜哪个还在生效。

### 4.4 DONE

DONE item 必须：

- 填写 `Resolution commit`；
- History view 直接显示 `Resolution commit`；
- Issue 顶部“当前进度”明确说明为什么已经完成；
- 旧 implementation / review / downstream evidence 继续留在详细 Evidence / History 区。

## 5. Clear Writing 是看板文字的生产依赖

用户明确要求：以后大部分维护类 reader-facing 文本都应优先使用 Clear Writing；其中 **Codex 只要创建或修改 Kanban / Project 的人类可见文字，就必须调用 Clear Writing**。

### 5.1 Codex / Executor

凡 Codex 创建或修改以下内容，必须在 GitHub mutation 前显式调用当前安装的 Clear Writing（slug `writing-style`）：

- tracking Issue title；
- 顶部“问题 / 当前进度 / 当前执行锚点 / 下一步”；
- Board card 直接显示的 reader-facing copy；
- History / closure 中面向人的完成说明；
- backfill 时新建或重写的 tracking Issue reader-facing text。

Clear Writing 只负责表达层，不得改变：

- Status lifecycle truth；
- plugin / Area owner；
- required downstream targets；
- proposal / task / branch / PR / commit locator；
- Resolution commit；
- factual evidence / claim strength。

如果 Codex execution runtime 无法真正调用 Clear Writing：

- 不得谎称已调用；
- 不得静默写一批低质量 board copy；
- 在写入这些 reader-facing board texts 前停止该文字 mutation，报告 `CLEAR_WRITING_UNAVAILABLE`，并返回同一 Goal 的最小恢复请求。

这不是要求修改 Clear Writing plugin，也不是本任务的 plugin production refinement。

### 5.2 Planner / Critic / GPT

Planner / Critic / maintenance GPT 同样默认优先使用 Clear Writing 来写面向人的 board copy；如果当前 GPT surface没有可调用的该 plugin，不因此把工作甩给用户，但必须遵守 §4 的同一 reader-facing contract。

GPT 不得用“当前没有 Project mutation tool”作为不维护语义的理由；详见 §7。

### 5.3 质量判断

`CLEAR_WRITING_USED=YES` 只能作为支持性过程证据，不能单独证明质量。

最终权威仍是实际 GitHub Project / Issue surface 的 qualitative review：用户看到的 title、Area、Status、top summary 和 current anchor 是否真正自然、清楚、低认知负担。

## 6. Project structure

### 6.1 Project metadata

Create / reconcile：

```text
Title: AI Skills Maintenance
Owner: YuukiAS
Visibility: PRIVATE
Linked repo: YuukiAS/AI_Skills_Collection
```

### 6.2 Status

canonical `Status` single-select 必须包含：

```text
TODO
DOING
ADAPTING
DONE
```

不增加 Planning / Review / Waiting / Blocked 主状态。

### 6.3 Area

创建或复用 `Area` single-select：

```text
workflow-core
ai-skills-core
writing-style
research-writing
presentations
scientific-visualization
web-development
statistical-modeling
bioinformatics
medical-imaging
standalone-skill
repo
cross-plugin
```

每个 item 只有一个 primary owner。跨 owner evidence 留在 Issue，不复制卡片。

### 6.4 Resolution commit

创建一个文本字段：

```text
Resolution commit
```

DONE 前为空。它保存 owner repo canonical closure/evidence commit，不塞入所有 component SHA。

## 7. 主动维护责任：BOARD-SYNC-01 contract

看板必须跟随真实 maintenance work 自动更新。用户不是 sync controller。

### 7.1 Raw NEW

真实项目 thread 新增 raw `NEW` 时：

- 仍然只写对应 plugin TODO inbox；
- 不自动创建 Project item；
- 不因为一条尚未 triage 的反馈制造 Issue。

### 7.2 Planner triage

Planner 判断某个 idea 进入 tracking scope 后，必须在同一轮主动：

1. create / bind 一个 top-level tracking Issue；
2. 加 `maintenance-track`；
3. 写符合 §4 的 human-readable title / top summary；
4. 设置真实初始 `Area`；
5. 设置真实初始 Status，通常为 TODO；
6. 把 `tracking: #N` locator 写回 canonical plugin TODO；
7. 记录当前 proposal / task locator（若已存在）。

不能等用户以后说“把它加到 Project”。

### 7.3 Planner 开始实质 round

一旦 Planner 开始实质 design / implementation round：

- tracking item 必须 reconcile 为 `DOING`；
- 顶部“当前进度”同步成自然语言；
- “当前执行锚点”更新为当前有效 proposal / execution package / workflow / branch；
- “下一步”更新为当前真实 handoff。

Status 变化依据 lifecycle truth，不依据“Planner 写了文档”本身。

### 7.4 Critic review

Critic 每一轮 formal review 后必须主动：

- 写入 / 更新当前 Critic review locator；
- 更新顶部“下一步”；
- 核对 tracking Issue 的 lifecycle truth；
- 如果真实 lifecycle 没变化，保持原 Status；
- `PASS` / `REVISE` 本身不能机械地改变 Status。

Critic 不代 Planner 改 Proposal，也不推进 Reviewed Handoff CURRENT；这里只同步 board evidence / next action。

### 7.5 ADAPTING

当 canonical core 已真正落地，但 frozen completion contract 中 required downstream target 仍未完成：

- 当前 owner 必须主动将 item 改为 `ADAPTING`；
- 顶部“当前进度”明确说中央部分已经完成，还差哪些 required downstream consumer；
- “当前执行锚点”切换到真实 downstream repo / branch / commit / runtime validation。

### 7.6 DONE

DONE 仍只按 approved closure contract：

1. 原问题真正解决；
2. canonical owner source 已集成；
3. required downstream adaptation 全部完成或有明确 N/A / NO_CHANGE；
4. normal-entry / real-consumer validation 完成；
5. runtime/server/Host evidence 有 durable locator；
6. Resolution commit 已确定；
7. tracking Issue completed close；
8. Project 通过 issue-closed workflow 机械进入 DONE。

### 7.7 Routine sync 不向用户索权

routine board sync 是本仓库已批准的维护动作：

- 不要求用户手工拖卡；
- 不要求用户每轮提醒 Planner/Critic；
- 不把普通 status/evidence update 包装成 Human Gate；
- 只有真正的新权限、数据、provider、外部副作用或用户决策才重新询问。

### 7.8 GPT surface 没有 Project mutation 能力时

当前 GPT 仍是语义 owner，不得写“请用户自己去 Project 改一下”。

它必须做两件事：

1. 使用自己已有的 GitHub 能力尽量直接更新 tracking Issue 的 human-readable summary / review locator / next action；
2. 在 handoff 中生成 **exact pending Project mutation**，交给下一有 Project 权限的 Executor / maintenance action 机械执行。

pending mutation 用普通人可读的小块即可，不创建 schema/state machine，例如：

```text
待同步到 Project：
- tracking Issue: #123
- Status: DOING
- Area: presentations
- 当前执行锚点: Presentations v3 proposal — <locator>
- 新增 review/evidence: <locator>
- 下一步: Critic 复核 v3
```

下一有权限的 Executor 在做其他 board mutation 前必须先消费这些 pending mutations，并核对 tracking Issue 当前事实没有过期。

不得谎称 Project 已更新。

## 8. GitHub bootstrap route

v0.1 已经通过 Critic 的真实能力核查，本轮保持：

- `gh project create/edit/link/field-create/field-list/item-add/item-edit/item-list` 用于支持的 Project / field / item 维护；
- default Status option replacement 使用 documented GraphQL `updateProjectV2Field`；
- views 使用 documented Projects API / GraphQL `createProjectV2View` / `updateProjectV2View`；
- built-in Project workflow enable/disable / auto-add config 使用当前官方支持的 Project Web UI；若执行时出现正式等价 mutation API，可在不改变批准语义的前提下使用；
- Project workflows 通过 GraphQL readback 验证 names / enabled state；
- `gh project` token 需要 `project` scope。

如果 workflow 配置仍只能通过 UI 且 Executor 没有受支持 browser，可提出一次最小 HUMAN_ONLY UI action，完成后 same-Goal 自动 resume。不要新增 GitHub Action/service/daemon 来回避这一点。

## 9. Bootstrap preflight

任何 external Project / Issue mutation 前：

1. fetch latest `origin/main`；验证 repo identity / remote；
2. 在用户发送 approved Kickoff 后，只创建 exact reviewed branch/worktree；
3. 验证当前 GitHub account = `YuukiAS`；
4. `gh auth status`；确认 repo access + `project` scope；
5. exact title `AI Skills Maintenance`：
   - none -> create one private Project；
   - exactly one -> inspect/reconcile；
   - multiple/unrelated -> stop with ambiguity evidence；
6. 检查 `maintenance-track` label 语义冲突；
7. 检查 Clear Writing（`writing-style`）是否在 Codex runtime 可真实调用；如果不能，先报告 blocker，不创建/重写 tracking Issue human-facing copy；
8. 记录 preflight snapshot，不回显 secrets。

未完成 BOARD-01 workflow guardrails 前，不开始 backfill。

## 10. Views

不超过四个。

### Board

- board layout；
- primary grouping = Status；
- 卡片至少直接显示：
  - human-readable title；
  - Area；
  - Status。

用户无需打开 Issue 就能看出“什么事 / 哪个 plugin / 现在在哪个阶段”。

### Active

- table layout；
- filter DOING / ADAPTING；
- 显示 title / Area / Status；
- current anchor 通过打开 Issue 顶部可立即看到，不新增 `Current workflow` Project field。

### By area

- table or grouped view；
- 按 Area 直接分组 / filter；
- 至少显示 title / Area / Status；
- 每个有 tracked items 的 plugin / Area 都能直接查看该 Area 中的 TODO / DOING / ADAPTING / DONE。

### History

- filter DONE；
- 直接显示 title / Area / Status / Resolution commit。

## 11. BOARD-01 guardrails

继续原样保持。

### Admission

auto-add 至少：

```text
is:issue label:maintenance-track
```

Implementation/design PR 不是 lifecycle item。

### Built-in workflows

配置并 readback 验证：

- item added -> TODO：enabled（若采用）；
- issue closed -> DONE：enabled for final closure；
- pull request merged -> DONE：disabled。

### Tracking Issue link discipline

DONE 前：

- 不建立会让中间 PR merge 自动关闭 tracking Issue 的 Development/manual linked relationship；
- PR body / commit message 不对 tracking Issue 使用 `close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved`；
- 只用 ordinary non-closing references；
- task/PR/commit/review locators 记入 tracking Issue。

不关闭 repository-wide linked-PR auto-close。

### Non-completion terminal path

REJECTED / SUPERSEDED / duplicate / not-planned：

1. 先从 Project remove/archive；
2. 再 truthful close Issue；
3. 不进入 DONE / History。

这不是第五主状态。

## 12. Bounded backfill

仍然只做 current-main one-pass snapshot。

### Include

- `CANDIDATE_GENERIC`；
- `PROMOTE_NOW`；
- still-valid `BLOCKED_NEEDS_EVIDENCE`；
- active Planner–Critic / Reviewed Handoff work not otherwise represented；
- canonical core integrated + explicitly required downstream incomplete。

### Exclude

- raw `NEW`；
- `PROJECT_LOCAL`；
- `REJECTED`；
- `SUPERSEDED`；
- project-specific research/product/code TODO；
- historical completed item without specific retrieval need。

### Deduplication

- one top-level idea -> one Issue；
- one primary Area；
- same evidence merges into existing Issue；
- ambiguous duplicate -> skip + report。

### Backfill copy

每个新建/重写的 tracking Issue：

1. 先建立准确 evidence map；
2. 用 Clear Writing 处理 title + top summary；
3. 保留 locator 原值；
4. 写入 Project；
5. independent surface review 检查实际可读性。

## 13. Repository consumer rules

新 canonical doc：

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

必须完整拥有：

- 四状态与 DONE contract；
- TODO / tracking Issue / execution task 边界；
- admission / bounded backfill；
- BOARD-01；
- §4 human-facing board contract；
- Codex mandatory Clear Writing requirement；
- §7 Planner/Critic/GPT proactive sync contract；
- Resolution commit；
- pending mutation fallback；
- non-completion terminal path；
- post-DONE optional consumer / regression rule。

### AGENTS

只增加简短 mandatory locator / consumer rule，至少明确：

- AI_Skills maintenance thread 在 triage / design / Critic review / integration / adaptation / closure 时必须主动 reconcile board，不等用户提醒；
- raw NEW 只进 plugin TODO；
- follow `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`；
- Codex 修改 tracking Issue / Kanban reader-facing copy 时必须调用 Clear Writing；
- 不因 task/PR/integration PASS 提前 DONE；
- 不在 tracking Issue 上使用 early auto-closing link/keywords。

不要把整份 board doc 复制进 AGENTS。

### TODO.md / docs/plugin-todos/README.md

解释：

- TODO files = failure/evidence/maturity inbox；
- Project = execution dashboard；
- `tracking: #N` = locator，不是第二状态。

### README

Project 仍为 PRIVATE 时默认：

```text
README checked: no update required
```

除非执行改变了 public user entry。

## 14. Verification gates

所有 gate 必须针对同一个 final Project configuration / candidate。

### B1 — Project structure + visible surface

直接验证：

- exact owner/title/visibility/repo link；
- Status = TODO/DOING/ADAPTING/DONE；
- Area / Resolution commit；
- Board / Active / By area / History；
- **实际打开 Board 和 By area surface**，确认卡片/表格能直接看到自然 title + Area + Status；
- 不允许用 API receipt / field existence 替代 actual surface review。

### B2 — BOARD-01

直接验证实际 workflow：

- auto-add exact issue-only filter；
- PR merged -> Done disabled；
- issue closed -> Done enabled；
- item added -> TODO（若使用）enabled；
- no PR lifecycle item；
- live tracking Issue 只有 non-closing references。

### B3 — Normal entry / idempotency

使用本任务自身 tracking Issue：

- auto-add once；
- Area=repo；
- Status=DOING；
- CLI/API list/update works；
- reconcile rerun 不产生 duplicate；
- Issue title / top summary 已实际经过 Clear Writing；
- Codex invocation evidence只作 supporting evidence。

### B4 — Backfill fidelity + reader-facing quality

对本轮所有新建/重写的 tracking Issues：

- current source locator valid；
- raw NEW / rejected / project-local 未误入；
- duplicates 已合并；
- ADAPTING 只给 required downstream；
- title + top summary 符合 §4；
- DOING / ADAPTING 至少有一个 current valid anchor；
- old locators 不冒充 current anchor。

然后实际浏览整个 Board / By area，确认每个有 tracked items 的 Area 都能直接查看其条目。

### B5 — Clear Writing / human-readability qualitative review

独立 Reviewer 必须检查真实 GitHub surface，而不是只看 Markdown source：

- Board；
- By area；
- 本任务 tracking Issue；
- 本轮所有新建/重写 tracking Issue 的 title + top summary。

Reviewer 要回答：

1. 不点开卡片时，能否看懂“什么事 / 哪个 plugin / 现在在哪个状态”；
2. 点开 Issue 后，顶部是否能立即看懂“问题 / 当前进度 / 当前执行锚点 / 下一步”；
3. 是否仍有 task key/hash/path/internal status stack 充当人类标题或说明；
4. locator 是否被放在解释之后，而不是用机器字符串代替解释；
5. Clear Writing 是否保持事实、Status、commit locator 不漂移。

字符串扫描、字数、field count、API receipt 不能单独 PASS。

### B6 — Role sync contract + repository docs

验证：

- canonical board doc 明确 Planner / Critic / GPT proactive sync；
- AGENTS 有 mandatory locator/consumer rule；
- raw NEW remains inbox-only；
- Planner triage -> tracking Issue；
- substantive Planner round -> DOING + current anchor；
- Critic review -> review locator + next action + truth check；
- core integrated/downstream pending -> ADAPTING；
- no-Project-tool GPT -> exact pending mutation handoff；
- Codex board-copy -> mandatory Clear Writing；
- TODO / plugin TODO README 不复制 execution status；
- no production plugin/generated payload change；
- NONE / NO_BUMP；
- README closure recorded。

### B7 — Final closure

Only after independent implementation review PASS + latest-main integration：

1. integrate reviewed docs/evidence to main with ordinary non-force Git；
2. verify remote main；
3. canonical main closure/integration commit becomes this idea's Resolution commit；
4. write Resolution commit to Project + Issue；
5. confirm all required adaptation for this board idea is complete；
6. close this tracking Issue with completed reason；
7. verify issue-closed workflow sets Project DONE；
8. verify History directly shows Resolution commit。

Overall Goal not achieved before B7.

## 15. Independent review and integration

Stage A：

- exact branch/worktree；
- bootstrap；
- BOARD-01；
- human-facing copy + Clear Writing；
- self-hosting tracking Issue；
- bounded backfill；
- repo docs；
- B1–B6；
- commit/push task branch；
- stop for independent implementation review。

Stage B：

Reviewer must inspect：

- actual Project configuration；
- actual Board / By area / Issue human-facing surface；
- repo diff；
- role sync contract；
- evidence。

不能只看 Executor summary。

Stage C：

Review PASS 后：

- fetch latest main；
- semantic overlap -> return Planner/Critic；
- unrelated drift -> normal merge；
- ordinary non-force main integration；
- B7；
- final remote verification。

Stage C 同一 frozen scope 已在 Kickoff 预授权，不因到达 later step 重复索权。

## 16. Failure recovery

### Missing `project` scope

Project mutation 前停止；请求一次 bounded auth refresh；同一 Goal resume。

### Clear Writing unavailable to Codex

reader-facing tracking Issue / board copy mutation 前停止；如实报告 `CLEAR_WRITING_UNAVAILABLE`。不得假装调用，也不得批量写 generic board text。

### Exact worktree unavailable

任何 external Project/Issue mutation 前停止；不换 locator。

### Workflow UI only

Project private + safe metadata 可保留；不 backfill。提出一次最小 HUMAN_ONLY UI action，完成后 readback verify，same-Goal resume。

### Project field/view partial failure

不 reset/delete Project；re-read IDs/state，idempotent reconcile。

### Backfill ambiguity

skip + report；不猜。

### GPT cannot mutate Project

GPT 更新它能更新的 tracking Issue evidence/summary，并生成 exact pending Project mutation；下一有权限 Executor 机械执行。不得要求用户手工拖卡。

### Accidental early Issue closure

停止 lifecycle mutation；合法时 reopen，恢复 truthful DOING/ADAPTING，记录 incident；若违反 approved guardrail，返回 Planner。

### Main drift

unrelated only -> integrate；semantic overlap -> Planner/Critic。

## 17. Explicit non-goals

Do not：

- change plugin production behavior / routing / generated payload / profile / release identity；
- modify Clear Writing plugin source；
- modify Bridge Kit；
- touch server/Host/production deployment；
- call paid APIs；
- create GitHub Actions / sync daemon / database / registry / ledger / controller / watcher / new workflow state machine；
- make Project public；
- add fifth lifecycle Status；
- bulk-promote raw NEW；
- disable repository-wide auto-close；
- use tracking Issue closing keywords/auto-close link before final closure；
- delete unrelated Projects/Issues/branches；
- force push / rewrite history。

## 18. User-visible value after closure

完成后，用户打开 Project 就应该直接看到：

- 每个 plugin / Area 有哪些真正需要追踪的 idea；
- 哪些还没开始、哪些正在做、哪些核心完成但还在适配、哪些真正结束；
- 每个 active item 当前到底由哪个 workflow / task / PR / commit 推进；
- 每个 DONE item 的 Resolution commit；
- Issue 顶部用自然语言说明问题、进度、当前锚点和下一步；
- 不需要用户自己提醒 Planner/Critic 去同步；
- 不需要用户手工拖卡；
- Codex 不得把内部状态串、路径和 hash 堆成不可读看板。

## 19. Stable blocker dispositions

### BOARD-UX-01 — ACCEPT

已落实：

- human-readable title；
- top summary 四项；
- current anchor；
- Board / By area visible title + Area + Status；
- DONE Resolution commit；
- Codex mandatory Clear Writing；
- B1/B4/B5 actual surface qualitative review。

### BOARD-SYNC-01 — ACCEPT

已落实：

- canonical doc + AGENTS mandatory sync rule；
- raw NEW inbox-only；
- Planner triage auto create/bind；
- substantive Planner round -> DOING/current anchor；
- Critic review -> review locator/next action/truth check；
- downstream pending -> ADAPTING；
- final DONE approved closure only；
- routine sync no user reminder；
- no Project mutation tool -> exact pending mutation；
- no new controller/watcher/Action/state machine。

```text
BOARD-UX-01 = ACCEPTED_AND_REVISED
BOARD-SYNC-01 = ACCEPTED_AND_REVISED
NEW_BLOCKERS_FOUND_BY_PLANNER = NONE
NEXT_HANDOFF = CRITIC
```
