# AI Skills Maintenance Board — Consumer-Scope Amendment v6 Critic Prompt

你是 AI Research Stack 的独立 Critic thread。

当前只审 Maintenance Board required-consumer selection semantics。不要重新设计 Project、四状态 lifecycle、BOARD-01、full-inbox、Clear Writing、tracking locator、Planner/Critic proactive sync 或 AI Skills Maintainer machine-update capability。

本轮只读审查，不修改 production source，不修改 canonical board policy，不修改 Issue #4，不执行任何 machine adaptation。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = Maintenance Board required-consumer contract
source_branch_or_ref = main
review_stage = DESIGN_AMENDMENT_REVIEW
proposal_path = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_PROPOSAL_2026-09-30.md
proposal_commit = abdbf8ce571f7890889a774dd0f4740648769d57
tracking_issue = #4
```

## 必须实际读取最新 main

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_CRITIC_REVIEW_2026-09-24.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_PROPOSAL_2026-09-30.md`
- `results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md`
- `results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md`
- Issue #4 current live state

按需读取，用于区分两个不同 consumer contract：

- `results/ai-skills-core--machine-update-orchestration/FINAL_REPORT.md`
- `results/ai-skills-core--machine-update-orchestration/ADAPTING_CONSUMER_STATUS.md`

## 已批准且不要重开的内容

继续保持：

```text
TODO -> DOING -> ADAPTING -> DONE
```

以及：

- Project item = top-level tracking Issue；
- TODO inbox保存 evidence/maturity，Project保存lifecycle；
- `tracking: #N` durable backlink；
- full-inbox bootstrap；
- Clear Writing；
- BOARD-01 false-DONE guard；
- Planner/Critic proactive sync；
- no-tool exact pending mutation；
- central implementation complete -> ADAPTING when real downstream consumers remain；
- AI Skills Maintainer = per-current-consumer executor；
- no cross-machine controller；
- Resolution commit + completed close -> final DONE。

本轮只审“required consumer set 从哪里来”。

## 新发现

v5 / canonical policy当前把以下五台机器写成 machine-consumed/shared-maintenance work 的默认 required consumers：

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`
4. `Workstation`
5. `Legion`

但独立 machine-update task 的 later evidence也使用完全相同的五机矩阵。

现在需要判断：

> Maintenance Board 是否错误继承了 AI Skills Maintainer machine-update product 的 machine coverage，而不是按 Maintenance Board 自己真实 normal-entry consumer选择？

## v6 Planner proposal

v6选择：

> required consumers = 该 tracked workflow 的真实 normal-entry consumers，
> 即为了该 item 的 frozen completion claim 成立，必须真正消费该变化的环境。

一个 machine **不会**仅因为以下事实自动 required：

- AI Skills Maintainer installed；
- 曾参加 machine-update task 的五机 acceptance；
- 有 Codex；
- 技术上可以 clone repo。

Intentional backup/fallback entry 只有在 completion contract明确承诺该路径时才 required。

进入 ADAPTING 时冻结 evidence-backed set。future optional consumer不追溯扩大旧 DONE。

## Issue #4 proposed set

Planner根据当前 repo证据建议：

### Already satisfied central/non-machine normal entry

- AI Research Stack ChatGPT Project instructions：central closure中已确认 semantic installation，不再是 pending machine handoff。

### Pending required downstream consumers

1. `Longleaf_Codex`
2. `CUHK_Workstation_WSL_Codex`

理由：Maintenance Board `CONSUMER_HANDOFFS.md` 对这两项直接观察到当前 `AI_Skills_Collection` Codex repo locator。

### Exclude under current evidence

- `Longleaf_Backup_Codex`
- `Workstation`
- `Legion`

其中：

- Board handoff 对 Backup只观察到host，当时没有观察到AI_Skills repo locator；
- Board handoff对Workstation/Legion没有观察到AI_Skills repo locator；
- 后续 machine-update evidence证明这三台可以消费 machine-update capability，但不证明它们承担 Maintenance Board central maintenance normal entry。

特别注意：`Longleaf_Backup_Codex` 名字里的 “Backup” 不应自动被当作 central-maintenance fallback contract。需要direct product evidence或用户明确designate。

## 必须比较的两个方案

### A. 固定五机

优点：简单、与machine-update acceptance一致。

风险：

- conflates two products；
- over-adaptation；
- unnecessary machine/credential gates；
- irrelevant machine可以阻塞Issue #4 DONE；
- future machine coverage容易被错误继承。

### B. 按真实 normal-entry consumer冻结

优点：

- completion与真实产品边界一致；
- 现有tracking Issue已经能保存required-consumer evidence；
- 不新增field/schema/controller；
- per-consumer Maintainer architecture保持不变。

Planner推荐 B。

## Critic重点问题

### C1 — semantic change是否真的需要

canonical policy §14目前明确写死五个 default required logical consumers。

是否可以在不改policy情况下，把 #4 直接解释成两台？

如果字面policy与Issue #4 current body/CONSUMER_HANDOFFS都已经freeze五台，那么应判断需要amendment，而不是静默重新解释。

### C2 — recommended #4 set是否有足够证据

当前证据是否足够支持：

```text
pending required:
- Longleaf_Codex
- CUHK_Workstation_WSL_Codex
```

以及排除：

```text
- Longleaf_Backup_Codex
- Workstation
- Legion
```

如果你认为repo locator observed仍不足以证明“normal central-maintenance entry”，指出最小补证据条件；不要因为“不确定”默认保留五机。

### C3 — Longleaf_Backup_Codex

独立判断它是否有证据是：

- central maintenance normal entry；或
- intentionally supported fallback entry。

Machine-update PASS本身不能作为唯一依据。

### C4 — Workstation / Legion

独立判断普通plugin使用 / machine-update consumer是否应该影响Maintenance Board #4 closure。

### C5 — future general rule

是否应该把fixed five改成：

> 每个 machine-consumed tracked item按自己的真实normal-entry/fallback contract冻结required set。

检查这是否会导致under-testing。如果一个workflow确实承诺多环境支持，所有被承诺环境仍应required。

### C6 — no new mechanism

v6不得引入：

- machine registry；
- new Project field；
- consumer-discovery service；
- watcher；
- controller；
- new plugin/skill。

tracking Issue中现有required-consumer section应足够。

## External check

请做一次针对性官方核查：

- ChatGPT Project instructions只作用于对应Project conversations；
- Codex AGENTS按repo/CWD消费。

优先：

- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://developers.openai.com/api/docs/guides/latest-model

这个external check只用于验证“consumer跟normal-entry surface走”的产品现实，不用于替代repo内completion contract。

## 期望输出

先直接回答：

1. Maintenance Board #4 当前真正required consumers是什么？
2. Workstation / Legion是否排除？
3. Longleaf_Backup_Codex是否排除？
4. fixed-five是否应改成per-workflow real normal-entry set？
5. 是否必须改canonical policy？
6. 是否有新的direct blocker？

然后输出：

```text
RESULT = PASS | REVISE
REVIEW_STAGE = DESIGN_AMENDMENT_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_PROPOSAL_2026-09-30.md
REVIEWED_PROPOSAL_COMMIT = abdbf8ce571f7890889a774dd0f4740648769d57
```

如果 PASS，明确：

- v6只批准required-consumer selection amendment；
- 不授权修改policy/Issue/consumer handoff；
- 下一步回Planner准备最小 implementation package / Goal / Kickoff；
- 不执行machine adaptation。

如果 REVISE，stable blocker必须给：

- direct evidence；
- causal risk；
- minimum close condition。

并按 Critic Role Contract自动生成完整Planner返修prompt。

## Review 文件授权

用户若把本 prompt原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_CRITIC_REVIEW_2026-09-30.md`

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
