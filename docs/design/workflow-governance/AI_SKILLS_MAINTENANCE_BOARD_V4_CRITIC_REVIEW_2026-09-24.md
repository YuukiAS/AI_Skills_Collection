# AI Skills 维护看板与完成语义 — Critic Review v4

- 日期：2026-09-24
- Review stage：`DESIGN_AMENDMENT_REVISION_REVIEW`
- Result：`REVISE`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- reviewed proposal：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_PROPOSAL_2026-09-24.md` v4
- reviewed proposal commit：`ad3694882b7f48c9136e9c2058151bcaee73ef00`
- previous Critic review：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_CRITIC_REVIEW_2026-09-24.md`
- previous Critic review commit：`03602cb5ecf03e4c6185413a7d780968f8d5e71e`
- rechecked blocker：`BOARD-CONSUMER-01`
- execution branch/worktree：NONE

## 1. 结论

`BOARD-CONSUMER-01` 已经被 v4 正确关闭。

v4 把 board contract 的 normal-entry consumption 分到四个真实入口：

1. ChatGPT Project instructions：普通 GPT thread；
2. AI_Skills `AGENTS.md`：Codex repo session；
3. Planner Role Contract：formal Planner round；
4. Critic Role Contract：formal Critic review；

再把 future production-ready AI Skills Maintainer 定义为 machine adaptation downstream consumer。

这个分层是对的。canonical policy 仍只有：

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

其余入口只放 trigger + locator + 最小语义，没有复制第二套 policy。

OpenAI 当前官方文档也支持这一入口划分：Project instructions 在 Project settings 中维护，并应用于该 Project 内的 conversations；Codex CLI 自动枚举并注入适用的 `AGENTS.md`。因此 Project instructions 与 repo AGENTS 是两个不同但互补的 normal-entry surface，不能只改其中一个。

两层完成语义也正确：

```text
execution-ready Critic PASS
-> implementation
-> independent implementation review PASS
-> canonical integration/release closure（若 Goal 要求）
= central implementation complete
-> machine-consumed item: DOING -> ADAPTING
```

之后只有 required machine consumers 完成真实 adaptation + installed/loaded identity + normal-entry/fresh-session consumption，才允许 `ADAPTING -> DONE`。

五个 logical consumers 也是当前用户明确冻结的 required set，且 v4 没有把 hostname/path/account 永久硬编码进 policy，而是在进入 ADAPTING 的同一轮解析并冻结 exact current identity/locator，这个设计合理。

但 v4 对 AI Skills Maintainer 的跨机器责任仍有一个直接 scope 冲突，需要最小澄清后才能 PASS。

## 2. BOARD-CONSUMER-01 复核

### 2.1 ChatGPT Project instructions

PASS。

未来 Project instructions 只需要放：

- 触发条件；
- canonical board doc locator；
- raw NEW / tracking scope 的最小语义；
- no-tool surface 时生成 exact pending mutation；
- 不让用户手工拖 Kanban。

不需要复制 board 全文。

如果当前 Project settings 只能由用户/Project editor 修改，v0.3 把 exact text 做成一次性 HUMAN_ONLY setup 是合理的。完成一次后 routine sync 不应重复询问。

### 2.2 AI_Skills AGENTS

PASS。

AGENTS 作为 Codex normal-entry locator 合适，只需要要求：

- TODO / Planner / Critic / adaptation / closure 工作读取 canonical board doc；
- routine reconcile 不等用户提醒；
- board reader-facing copy 继续走 Clear Writing。

### 2.3 Planner / Critic contracts

PASS。

Planner 负责 triage、first substantive round、handoff、central-complete cutover；Critic 负责 review locator、next action、lifecycle truth。

`PASS / REVISE` 本身不机械换状态，这一点保持正确。

无 Project mutation tool 时，角色仍是 semantic owner，输出 exact pending mutation，而不是让用户自己维护。

### 2.4 两层完成时点

PASS。

特别确认：

- execution-ready Critic PASS：仍是 DOING；
- Codex 实现完成但尚未 independent implementation review：仍是 DOING；
- Reviewer PASS 但 frozen Goal 还要求 canonical integration/release closure：仍不能 ADAPTING；
- central implementation complete 真正成立后：machine-consumed item 才进入 ADAPTING；
- required machine consumers 全部 PASS：才 DONE。

这关闭了“Reviewer PASS 但 canonical source 还没落地就提前 ADAPTING”的风险。

## 3. 五个 required consumers

当前用户冻结的逻辑 consumer set：

### Server / remote Codex

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

### Local machine

4. `Workstation`
5. `Legion`

作为当前默认 completion contract，PASS。

这些名称是 logical consumer identity，而不是 hostname/path。进入 ADAPTING 时再解析为 exact current runtime identity/locator，可以避免 policy stale hardcode。

每个 consumer 要求：

- target identity；
- adaptation action；
- installed/loaded identity；
- normal-entry consumption；
- fresh-session/restart boundary（如适用）；
- risk-matched safety；
- durable evidence。

这足以防止“repo 已 pull / 文件已存在 / source SKILL 已读”冒充真实消费。

v4 也正确保留：

- 普通 domain plugin / artifact improvement 不自动继承五机要求；
- frozen contract 可有有证据的 N/A；
- future optional machine 不追溯扩大旧 DONE。

## 4. Stable blocker

### BOARD-MAINTAINER-SCOPE-01 — future Maintainer 被写成“五 consumer 适配器”，但当前 machine-update architecture 明确是单机 normal entry

**直接证据**

当前独立 machine-update source 明确写：

> AI Skills Maintainer should become the only user-facing entry for updating/adapting the AI Research Stack on **one current Codex machine/server**.

其 Non-goals 也明确禁止：

> cross-machine controller

也就是说，当前已设计但尚未 production-ready 的 AI Skills Maintainer machine-update orchestration 是 **per-current-machine executor**，不是一个从某台机器远程控制五个 consumer 的跨机 orchestration service。

而 v4 的 steady-state 叙述写成：

```text
AI Skills Maintainer适配五个 required consumers
-> 五 consumer normal-entry PASS
```

以及 §8.2/8.3 要求 Maintainer“对五个 required consumers 逐项报告 PASS / truthful blocker”。

如果按字面交给后续 Executor，可能被误实现成新的 cross-machine controller，直接扩大 machine-update 已冻结的 architecture / authorization boundary。

**因果风险**

这不是措辞洁癖。

它可能导致未来 implementation：

- 让一台机器上的 Maintainer 主动 SSH/远程控制其他 machine；
- 新增 cross-machine inventory/controller；
- 混淆五个 consumer 的 credential/Host/authority；
- 或者为了满足 board DONE，在未获批准情况下扩 machine-update scope。

这正违反当前 machine-update Proposal 的单机边界，也违反本 board 设计“不新增 controller/watchers”的原则。

**最小关闭条件**

不需要新 skill、不需要 standalone plugin、不需要 controller。

Planner v5 只需把 Maintainer 角色澄清为：

1. AI Skills Maintainer 是 **per-consumer adaptation normal executor**。
2. 五个 required consumers 的 aggregation / completion truth 由 tracking Issue + Planner/Critic/Project-capable executor 持有。
3. 对每个 consumer：
   - 在该 consumer 的 current Codex environment 中调用 production-ready Maintainer；
   - 或使用已另行批准的 existing remote execution route；
   - Maintainer只负责当前 consumer 的 discovery/update/verification/evidence。
4. 每次 per-consumer PASS：
   - 有 Project mutation能力则更新该 consumer 行；
   - 无能力则输出 exact completion mutation；
   - 下一 Project-capable executor 自动消费。
5. 只有 tracking Issue 聚合确认五个 consumer 全部 PASS/N/A 后，才执行 DONE closure。
6. 明确禁止因为 board contract 新建 cross-machine controller、machine registry、watcher 或“Kanban updater service”。

这样仍完全符合用户“最后五个环境都适配完才算 DONE”的目标，但不会偷改 AI Skills Maintainer 的单机 architecture。

## 5. Kanban workflow 应不应该做成 skill

当前结论：**不应该新增 standalone skill，也不应该为了 Kanban 单独新增一个顶级 AI Skills Maintainer skill。**

原因：

1. 这套能力首先是 repository-maintenance lifecycle contract，而不是一个用户主动调用的独立领域任务；
2. ordinary ChatGPT thread 的 trigger 由 Project instructions 消费，standalone skill 不能替代；
3. Codex 的 trigger 由 AGENTS 消费，skill 也不能替代；
4. Planner/Critic 的责任在 role contracts；
5. machine adaptation 已经有独立设计中的 `machine-update-orchestrator`，再造 `kanban-sync` skill 会引入重复 owner。

推荐结构：

```text
canonical policy
  docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

ChatGPT entry
  Project instructions -> short locator

Codex repo entry
  AGENTS.md -> short locator

formal GPT roles
  PLANNER_ROLE_CONTRACT.md
  CRITIC_ROLE_CONTRACT.md
  -> short board consumption rule

central repo maintenance
  existing ai-skills-repository-maintainer
  -> future implementation可加短 board locator/closure consumption，不复制 policy

machine adaptation
  future machine-update-orchestrator
  -> per-consumer adaptation + exact completion mutation
```

只有以后真实运行证明“Project mutation 的机械步骤本身复杂、重复、跨多个 AI_Skills maintenance route 无法由 canonical doc + existing maintainer稳定执行”，才有理由考虑内部 helper/skill。当前没有这种证据。

尤其不建议 standalone skill：它会制造新的 discoverability/trigger 问题，反而削弱“普通 thread 自动维护”的目标。

## 6. 实际需要改哪些东西

在本 amendment PASS 前后应分两层。

### Board v0.3 execution package 应负责

- 新建 canonical `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`；
- AI Research Stack ChatGPT Project instructions：一次性 short trigger/locator；
- AI_Skills `AGENTS.md`：short Codex locator；
- `PLANNER_ROLE_CONTRACT.md`：Planner reconcile rule；
- `CRITIC_ROLE_CONTRACT.md`：Critic reconcile rule；
- TODO / plugin TODO README：inbox vs Project + tracking locator；
- Project / Issue bootstrap、full-inbox coverage、Clear Writing、BOARD-01；
- tracking Issue 中五 consumer checklist；
- no cross-machine controller。

### 独立 AI Skills Maintainer machine-update task 在未来 release 前负责

- 在已规划的 `machine-update-orchestrator` 中消费 board downstream contract；
- 明确自己是 per-current-machine adaptation executor；
- current consumer PASS 后直接 Project update 或 exact completion mutation；
- fresh-session / installed-loaded / normal-entry evidence；
- 不承担跨五机 controller。

现有 `ai-skills-repository-maintainer` 不需要现在拆出一个 Kanban standalone skill；未来若它负责 central maintenance closure，可加一个短 board locator/consumer rule即可。

## 7. 审查结论

```text
RESULT = REVISE
REVIEW_STAGE = DESIGN_AMENDMENT_REVISION_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_PROPOSAL_2026-09-24.md
REVIEWED_PROPOSAL_COMMIT = ad3694882b7f48c9136e9c2058151bcaee73ef00
RECHECKED_BLOCKERS = BOARD-CONSUMER-01
CLOSED_BLOCKERS = BOARD-CONSUMER-01
NEW_BLOCKERS = BOARD-MAINTAINER-SCOPE-01
```

本轮没有重新打开四状态、BOARD-01、BOARD-UX-01、BOARD-SYNC-01、Clear Writing、full-inbox coverage 或五 consumer DONE requirement。

只需要澄清“Maintainer 每次适配一个 consumer，Project 聚合五个 consumer”，避免把现有单机 updater 误变成跨机器 controller。
