# AI Skills Maintenance Board — Consumer-Scope Amendment v6 Critic Review

- Date: 2026-09-30
- Review stage: `DESIGN_AMENDMENT_REVIEW`
- Result: `REVISE`
- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: repository maintenance / plugin refinement workflow
- design_topic_or_task_key: `repo--maintenance-board-lifecycle`
- source_branch_or_ref: `main`
- review object: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_PROPOSAL_2026-09-30.md`
- reviewed proposal commit: `abdbf8ce571f7890889a774dd0f4740648769d57`
- reviewed proposal blob: `5f2e9bc978a87c2afc616b4b830967dfabfe2ce8`
- latest-main proposal blob at review: same as reviewed proposal blob
- tracking Issue: `#4`

## 1. Conclusion

Planner v6 的核心方向正确：

> Maintenance Board 的 required consumers 应从当前 tracked workflow 自己真实的 normal-entry / explicitly designated fallback contract 冻结，而不是机械继承 AI Skills Maintainer machine-update task 的五机 acceptance matrix。

因此本轮接受以下语义判断：

- canonical policy §14 当前确实固定了五个 logical consumers，所以这不是“重新解释旧规则”即可完成，必须做 semantic amendment；
- machine-update task 的五机 PASS 只证明该 machine-update 产品的环境覆盖，不自动证明 Maintenance Board #4 也需要同样五机 closure；
- `Workstation` / `Legion` 的 ordinary plugin / machine-update consumption 不足以使其成为 #4 的 required board consumers；
- `Longleaf_Backup_Codex` 的名字含 Backup 不构成 central-maintenance fallback contract；当前 board handoff 没有为它观察到 AI_Skills_Collection repo locator，后来的 machine-update PASS 也只证明 updater coverage；
- `Longleaf_Codex` 与 `CUHK_Workstation_WSL_Codex` 在 board handoff 中有直接观察到的 AI_Skills_Collection Codex repo locator，并被当前用户语境明确指向为实际负责该 repo 的环境；对 #4 这一 bounded item，当前证据足以把它们作为 pending Codex consumers；
- AI Research Stack ChatGPT Project instructions 已经是 board normal-entry surface，并且 central closure 已记录用户确认的语义安装；它属于 already-satisfied normal entry，不需要再作为 machine adaptation 重跑；
- future general rule 应按每个 tracked item's actual normal-entry / explicitly promised fallback contract 冻结 required set；明确承诺多环境支持的 workflow 仍必须把那些环境纳入，因此不会因本 amendment 自动 under-test；
- 不需要新 Project field、registry、watcher、controller、skill 或 plugin。

Option A（固定五机）会把另一个产品的环境覆盖误当成所有 machine-consumed workflow 的完成合同，造成无关机器授权、适配和 ADAPTING 阻塞。Option B（按真实 normal entry / promised fallback 冻结）与实际 owner/entry boundary 更一致，应采用。

但 v6 当前 implementation boundary 留下一个直接的 canonical-policy 自相矛盾，因此本版本还不能 PASS。

## 2. Stable blocker

### BOARD-CONSUMER-NORMATIVE-01 — v6 只计划改 §14，但 canonical §15 仍硬编码“五 consumer aggregate truth”

**Requirement**

本 amendment 的目标是把 required-consumer selection 从 fixed-five 改成 per-item frozen required set。canonical policy 必须在同一版本内保持一致，不能一节改成动态集合、下一节仍要求五 consumer aggregate truth。

**Direct evidence**

当前 latest-main `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`：

- §14 明确列出固定五个 required logical consumers；
- §15 明确写着：`五 consumer aggregate truth 属于 tracking Issue / Project lifecycle。`

而 v6 Proposal §10 的 proposed implementation 只列：

- amend `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md §14`；
- amend Issue #4 / `CONSUMER_HANDOFFS.md`；
- 不改 production plugin source，不做 machine adaptation。

也就是说，如果按 v6 原文执行，§14 会变成动态 required set，但 §15 仍会把聚合真值描述成固定五 consumer。

**Causal risk**

`AI_SKILLS_MAINTENANCE_BOARD.md` 是唯一完整 canonical board policy。留下这个冲突后，Planner / Critic / Maintainer / Codex 在后续 closure 时可能：

- 按 §14 只冻结真实 required set；
- 又按 §15 继续解释为必须聚合五机；
- 使 Issue #4 或未来 tracked item 再次发生本轮正在修复的 over-adaptation；
- 或迫使实现者自行猜哪一节优先。

这会直接破坏本 amendment 的用户可见目的，不是格式问题。

**Minimum close condition**

Planner 只需做最小 v6 revision：

1. 保留 Option B 和 #4 当前 recommended set 不变；
2. 把 implementation boundary 改成“更新 canonical policy 中所有 normative fixed-five wording”，至少包括：
   - §14：fixed five -> evidence-backed frozen required set；
   - §15：`五 consumer aggregate truth` -> `required-consumer aggregate truth`（或等价不绑定数量的表述）；
3. §16 已使用 `all required consumers`，无需为了本 blocker 改写；
4. 不要求修改历史 v4/v5 Proposal/Review/Goal/Kickoff；这些是历史证据；
5. Planner/Critic role contracts 当前使用 generic `required consumers` / exact locators，不因本 blocker机械改动；
6. Issue #4 / `CONSUMER_HANDOFFS.md` 的后续实现仍按 v6 计划保留历史五机 handoff 作为 evidence，再新增/更新 current truth，不删除历史记录。

关闭以上一点即可重新审，不需要重新打开 Project、lifecycle、BOARD-01、Clear Writing、tracking locator、machine-update architecture 或版本策略。

## 3. Evidence assessment for Issue #4

### Longleaf_Codex / CUHK_Workstation_WSL_Codex

当前 evidence 足以支持 bounded #4 selection。

`CONSUMER_HANDOFFS.md` 对两者分别记录了当前 Codex app 中直接观察到的 AI_Skills_Collection project/repo locator，并标为 `HANDOFF_READY`。这比“某机器装有 Codex / Maintainer”更直接地绑定到该 repo 的 normal entry。

本轮不要求证明“过去每一次 maintenance 都在这两台运行”；required-consumer selection 需要的是当前 frozen completion claim 所承诺/依赖的 normal entry，而不是历史使用次数。

### Workstation / Legion

当前没有 board-specific central-maintenance contract。后来 machine-update closure 中在这两台执行 `sync this machine`，证明的是 updater 能力和机器覆盖，不是 board lifecycle normal entry。因此从 #4 排除有直接依据，不是为了少测而删环境。

### Longleaf_Backup_Codex

board handoff 在 cutover 时只观察到 host，没有观察到该 repo locator；后来的 machine-update task 证明它能运行 AI Skills Maintainer，但没有建立“Maintenance Board central-maintenance fallback”的承诺。仅凭名称中的 `Backup` 不能推导 fallback contract。

如果未来用户或 repo contract 明确把它指定为 central-maintenance fallback，未来 tracked item 必须纳入；v6 的 proposed future rule 已覆盖这一点。

## 4. Under-testing check

v6 的 general rule 没有把“少环境”当默认目标，而是要求：

- actual normal-entry consumer；
- explicitly promised environment；
- intentionally designated fallback；
- Project/AGENTS/normal-entry contract；

有任一证据就应纳入 frozen required set；有歧义则保持 ADAPTING 并返回 Planner。

因此 amendment 不会合法化“为了省事少测”。它只是阻止把另一个 tracked product 的 acceptance matrix 横向继承到所有 workflow。

## 5. External reality check

独立核对了当前 OpenAI 官方资料：

- ChatGPT Projects：Project instructions 在 Project settings 中维护，只在对应 Project 内生效。  
  https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Codex guidance / cookbook 继续把 repo `AGENTS.md` 作为 Codex 项目级 instruction surface。  
  https://developers.openai.com/cookbook/examples/codex/code_modernization

这些资料支持“按真实入口绑定规则”的方向，没有提供任何依据要求 unrelated machine 因安装了同一 plugin 就自动成为某个 repository-maintenance workflow 的 required consumer。

## 6. Scope and version boundary

本 review 只审 required-consumer selection semantics。

本轮没有批准：

- 修改 canonical policy；
- 修改 Issue #4；
- 修改 `CONSUMER_HANDOFFS.md`；
- 执行任何 machine adaptation；
- 修改 AI Skills Maintainer production source；
- 新增任何 controller / registry / watcher / skill / plugin。

如果按 minimum close condition 修订，仍可保持：

```text
Repository bump decision: NONE
Affected plugins:
- all: NO_BUMP
```

因为这是 maintenance policy / tracking completion semantics 修正，不改变 production plugin runtime。

## 7. Final fields

```text
RESULT = REVISE
REVIEW_STAGE = DESIGN_AMENDMENT_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_PROPOSAL_2026-09-30.md
REVIEWED_PROPOSAL_COMMIT = abdbf8ce571f7890889a774dd0f4740648769d57
STABLE_BLOCKER = BOARD-CONSUMER-NORMATIVE-01
NEXT_HANDOFF = PLANNER
```

## 8. Planner repair prompt

```text
你现在继续 AI Skills Maintenance Board required-consumer selection amendment v6，只修 Critic 的唯一 stable blocker，不重新设计已经接受的 consumer-selection方向。

Repository:
YuukiAS/AI_Skills_Collection

Task:
repo--maintenance-board-lifecycle

Review stage:
DESIGN_AMENDMENT_REVISION

Reviewed proposal:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_PROPOSAL_2026-09-30.md

Reviewed proposal commit:
abdbf8ce571f7890889a774dd0f4740648769d57

Critic review:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_CRITIC_REVIEW_2026-09-30.md

Stable blocker:
BOARD-CONSUMER-NORMATIVE-01

先读取 latest main 的 AGENTS、Planner/Critic contracts、AI_SKILLS_MAINTENANCE_BOARD.md、v6 Proposal 和本次 Critic review。

已接受、不重开的结论：

- required consumers 应来自 tracked item's actual normal-entry / explicitly promised fallback contract，不机械继承 AI Skills Maintainer machine-update task 的五机 coverage；
- #4 pending Codex consumers 仍为 Longleaf_Codex、CUHK_Workstation_WSL_Codex；
- AI Research Stack ChatGPT Project instructions 是 already-satisfied normal entry；
- Longleaf_Backup_Codex、Workstation、Legion 在当前 evidence 下不属于 #4 required set；
- future explicitly promised multi-environment workflow 仍必须纳入其真实 required environments；
- 不新增 Project field、registry、watcher、controller、skill 或 plugin。

只修一个问题：

当前 v6 §10 只计划修改 canonical board policy §14，但当前 §15 仍写“five-consumer aggregate truth / 五 consumer aggregate truth”。这会让动态 required set 与固定五机聚合语义并存。

请提交完整 v6.1（或明确的新版本）Proposal：

1. 明确 implementation 必须更新 canonical AI_SKILLS_MAINTENANCE_BOARD.md 中所有 normative fixed-five wording，至少 §14 与 §15；
2. §14 改为 evidence-backed frozen required consumer set；
3. §15 改为 required-consumer aggregate truth，不绑定数量；
4. §16 当前 all required consumers 语义可保留；
5. 不修改历史 v4/v5 design/review/goal/kickoff；
6. Planner/Critic role contracts 若当前已是 generic required-consumer 语义则保持不变；
7. Issue #4 / CONSUMER_HANDOFFS 的 future implementation 保留历史五机 evidence，只更新 current truth；
8. 不修改 production plugin source，不执行 machine adaptation，不 bump repository/plugin version。

对 blocker 明确 ACCEPT / PARTIAL_ACCEPT / REBUT；若 rebut 必须给直接 source 证据。

完成后给出完整下一轮 Critic prompt，绑定新版 Proposal path + exact commit。本轮不要实现 canonical policy 或修改 Issue/Project/machine。
```
