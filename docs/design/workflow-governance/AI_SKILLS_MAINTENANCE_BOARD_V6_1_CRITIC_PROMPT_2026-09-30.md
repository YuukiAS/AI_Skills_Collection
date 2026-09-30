# AI Skills Maintenance Board — Consumer-Scope Amendment v6.1 Critic Prompt

你是 AI Research Stack 的独立 Critic thread。

当前只复核 v6.1 是否关闭上一轮唯一 stable blocker
`BOARD-CONSUMER-NORMATIVE-01`。

不要重新设计已经接受的 required-consumer selection 方向，不实现 canonical
policy，不修改 Issue #4 / Project / CONSUMER_HANDOFFS，不执行 machine
adaptation，不修改 production plugin source。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = Maintenance Board required-consumer contract
source_branch_or_ref = main
review_stage = DESIGN_AMENDMENT_REVISION_REVIEW
proposal_path_and_version = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md v6.1
proposal_commit = 515c42623c55f368eb84a1628839459afa909c09
previous_proposal = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_PROPOSAL_2026-09-30.md
previous_proposal_commit = abdbf8ce571f7890889a774dd0f4740648769d57
previous_critic_review = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_CRITIC_REVIEW_2026-09-30.md
previous_critic_review_commit = 97de8aa3cf36a379aa978ec4f90535df5b04a538
stable_blocker_to_recheck = BOARD-CONSUMER-NORMATIVE-01
tracking_issue = #4
```

## 必须先读取 latest main

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_PROPOSAL_2026-09-30.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_CRITIC_REVIEW_2026-09-30.md`

按需读取：

- Issue #4 live state；
- `results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md`；
- `results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md`。

不要重新审 AI Skills Maintainer machine-update capability。

## 已接受、不要重开的方向

上一轮 Critic 已接受：

- required consumers 来自 tracked item's actual normal-entry / explicitly
  promised fallback contract；
- 不机械继承 AI Skills Maintainer machine-update task 的五机 coverage；
- Issue #4 pending Codex consumers：
  - `Longleaf_Codex`
  - `CUHK_Workstation_WSL_Codex`
- AI Research Stack ChatGPT Project instructions =
  already-satisfied normal entry；
- 当前 evidence 下，以下不属于 #4 required set：
  - `Longleaf_Backup_Codex`
  - `Workstation`
  - `Legion`
- future 明确承诺 multi-environment support 的 workflow 仍必须纳入真实 required
  environments；
- 不新增 Project field、registry、watcher、controller、skill、plugin 或
  cross-machine control plane。

本轮只复核 canonical normative convergence。

## Stable blocker 回顾

上一轮 blocker：

`BOARD-CONSUMER-NORMATIVE-01`

原因：

- canonical `AI_SKILLS_MAINTENANCE_BOARD.md §14` 固定五个 required consumers；
- §15 又写：
  `五 consumer aggregate truth 属于 tracking Issue / Project lifecycle。`
- v6 原 Proposal 只计划修改 §14；
- 如果只改 §14，动态 required set 与 fixed-five aggregate truth 会并存。

## v6.1 修复

### 1. §14

v6.1 规定 §14 不再列出 global fixed-five default。

新语义：

> machine-consumed/shared-maintenance tracked item 的 required consumers 是：
> 为了该 item 的 frozen completion claim 成立，必须真实消费该变化的
> actual normal-entry consumers + explicitly promised fallback environments。

明确不因以下原因自动 required：

- AI Skills Maintainer installed；
- another product 的 machine-update acceptance matrix；
- Codex installed；
- technically cloneable repo。

fallback只有 completion contract明确承诺时才 required。

ADAPTING cutover冻结 evidence-backed required set + exact locators。

有歧义 -> 保持 ADAPTING，返回 Planner；不“为了保险”扩大，也不静默漏掉明确承诺环境。

### 2. §15

保留：

> AI Skills Maintainer = per-current-consumer adaptation executor

把：

```text
五 consumer aggregate truth 属于 tracking Issue / Project lifecycle。
```

改成数量无关的：

```text
required-consumer aggregate truth 属于 tracking Issue / Project lifecycle。
```

或完全等价的自然中文。

Maintainer仍：

- 不持有 machine registry；
- 不做 multi-machine orchestrator；
- 不做 credential broker。

### 3. §16

保持当前 generic：

```text
all required consumers PASS/N/A
+ durable evidence complete
+ Resolution commit
+ tracking Issue completed close
+ issue-closed workflow -> DONE
```

不因本 blocker机械重写。

### 4. all normative fixed-five wording

实施范围定义为：

- 只在**当前 canonical**
  `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
  内收敛所有 normative fixed-five wording；
- minimum known changes = §14 + §15；
- 若 canonical file 内还有另一句 normative fixed-five statement，与新 required-set
  rule矛盾，则同一 bounded implementation中收敛；
- 不借此修改 unrelated lifecycle / admission / BOARD-01 / Clear Writing /
  tracking locator / role ownership语义。

## Historical artifacts boundary

v6.1 明确不重写历史：

- v4/v5 Proposal / Critic review；
- historical v0.3-v0.5 Plan/Goal/Kickoff；
- 其他真实记录当时 five-consumer contract 的历史证据。

这些不是 current canonical policy。

请确认这是正确的 history-preserving boundary。

## Planner / Critic contracts

current role contracts已经用 generic语义：

- `required consumers pending`
- exact consumer identities / locators

不 hard-code five。

v6.1 therefore：

```text
ROLE_CONTRACT_CHANGES = NONE
```

请独立核实；没有 fixed-five direct evidence时不要要求机械改 role contracts。

## Issue #4 current truth

v6.1不改变上一轮 Critic已接受的 set：

### Already satisfied

- AI Research Stack ChatGPT Project instructions

### Pending required

- `Longleaf_Codex`
- `CUHK_Workstation_WSL_Codex`

### Non-required under current evidence

- `Longleaf_Backup_Codex`
- `Workstation`
- `Legion`

后续 implementation 必须：

- 保留原五机 `CONSUMER_HANDOFFS.md` evidence作为历史；
- 只新增/更新 current truth；
- 不删除历史证据；
- Issue #4 继续 ADAPTING，直到 current required set通过 existing closure contract。

本 review 不授权这些 mutation。

## §16 / final DONE check

请特别确认：

把 §14/§15 改成 quantity-neutral 后，§16 的：

`all required consumers PASS/N/A`

已经自然引用当前 item被冻结的 required set，无需“all five”语义。

如果你发现 §16 仍有 direct fixed-five contradiction，必须指出直接文本；不要因为习惯性“整节一起改”要求无必要重写。

## No new mechanism

v6.1 继续禁止：

- new Project field；
- registry；
- watcher；
- controller；
- daemon；
- consumer-discovery service；
- standalone skill/plugin；
- machine adaptation；
- production plugin source change。

## Version / Gate boundary

v6.1 Proposal保持：

```text
Repository bump decision: NONE
Affected plugins:
- all: NO_BUMP
```

理由：后续只是 maintenance policy / tracking completion semantics 修正，不改变 production plugin runtime。

不因本 amendment新增 production Plugin Capability Gate。

## External-research note

上一轮 Critic已独立核对 OpenAI Projects / Codex instruction surfaces，并接受“consumer跟真实 normal entry走”的方向。

v6.1没有新增 external capability assumption，只修 canonical §§14–16 内部 normative consistency。

如果没有新的外部事实改变该判断，不要重新扩大 research scope。

## 重点问题

### N1 — blocker是否关闭

§14 dynamic required set、§15 quantity-neutral aggregate、§16 all required consumers 是否已经语义一致？

### N2 — implementation boundary是否完整

“canonical policy内所有 normative fixed-five wording，至少§14/§15”是否比原 v6只改§14更完整，同时仍保持bounded？

### N3 — history是否正确保留

是否应该不改旧 v4/v5 / old execution artifacts？

### N4 — role contracts是否无需改

current generic required-consumer wording是否已经足够？

### N5 — Issue #4 set是否没有被重新打开

是否仍保持：

```text
pending = Longleaf_Codex, CUHK_Workstation_WSL_Codex
already satisfied = AI Research Stack ChatGPT Project instructions
non-required current evidence = Longleaf_Backup_Codex, Workstation, Legion
```

### N6 — 是否有新 direct blocker

只能来自 v6.1 新事实、遗漏的关键规范冲突或 revision引入的真实回归。

不要移动已接受终点。

## 输出要求

如果仍需修改：

```text
RESULT = REVISE
REVIEW_STAGE = DESIGN_AMENDMENT_REVISION_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md
REVIEWED_PROPOSAL_COMMIT = 515c42623c55f368eb84a1628839459afa909c09
RECHECKED_BLOCKERS = BOARD-CONSUMER-NORMATIVE-01
```

blocker必须给 direct evidence / causal risk / minimum close condition。

然后按 Critic Role Contract自动生成完整 Planner返修 prompt。

如果 blocker关闭：

先自然中文说明：

- BOARD-CONSUMER-NORMATIVE-01 如何关闭；
- §§14/15/16是否一致；
- history preservation是否正确；
- role contracts是否无需改；
- Issue #4 accepted set是否保持；
- PASS证明什么、不证明什么。

然后输出：

```text
RESULT = PASS
REVIEW_STAGE = DESIGN_AMENDMENT_REVISION_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md
REVIEWED_PROPOSAL_COMMIT = 515c42623c55f368eb84a1628839459afa909c09
RECHECKED_BLOCKERS = BOARD-CONSUMER-NORMATIVE-01
CLOSED_BLOCKERS = BOARD-CONSUMER-NORMATIVE-01
NEW_BLOCKERS = NONE
NEXT_HANDOFF = PLANNER
```

明确 PASS 只批准 v6.1 required-consumer semantic amendment。

它不授权：

- 修改 canonical policy；
- 修改 Issue #4；
- 修改 CONSUMER_HANDOFFS；
- machine adaptation；
- production source change。

下一步回 Planner准备最小 implementation package / Goal / Kickoff，再按 role contract做 execution-ready review。

## Review 文件授权

用户若把本 prompt原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md`

并 ordinary non-force push。

除此之外禁止修改：

- canonical board policy；
- Issue #4；
- CONSUMER_HANDOFFS；
- AGENTS / role contracts；
- plugin source；
- machine-update source；
- server/local machine；
- 任何其他 repo。

提交后报告 exact review commit。
