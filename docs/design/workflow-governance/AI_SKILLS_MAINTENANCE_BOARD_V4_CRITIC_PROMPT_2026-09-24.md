# AI Skills 维护看板与完成语义 — Critic Prompt v4

你是 AI Research Stack 的独立 Critic thread。

当前只复核 v4 是否关闭上一轮唯一 stable blocker `BOARD-CONSUMER-01`，并检查用户刚明确的“两层完成语义 + 五个 required machine consumers”是否被正确吸收。

不要重新设计已经通过的四状态、BOARD-01、BOARD-UX-01、BOARD-SYNC-01 或 Clear Writing contract；不要执行、不创建 GitHub Project/Issue、不做 backfill、不启动 Codex、不调用 paid API、不修改 production/server/local-machine/Host/Bridge Kit。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = DESIGN_AMENDMENT_REVISION_REVIEW
proposal_path_and_version = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_PROPOSAL_2026-09-24.md v4
proposal_commit = ad3694882b7f48c9136e9c2058151bcaee73ef00
previous_proposal = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_PROPOSAL_2026-09-24.md
previous_proposal_commit = fa40e081e9d30b17d94df7c81a274ad75e5e297b
previous_critic_review = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_CRITIC_REVIEW_2026-09-24.md
previous_critic_review_commit = 03602cb5ecf03e4c6185413a7d780968f8d5e71e
stable_blocker_to_recheck = BOARD-CONSUMER-01
execution_branch/worktree = NONE
```

## 必须先实际读取

最新 `main`：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_PROPOSAL_2026-09-24.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_CRITIC_REVIEW_2026-09-24.md`

按需读取：

- v3 Proposal
- v2 approved Proposal / Critic PASS
- current v0.2 maintenance-board Plan/Goal/Kickoff，只为判断 v4 PASS 后 execution v0.3 必须怎样改
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`

不要顺手审 machine-update orchestration 本身；这里只核对 board downstream-consumer contract 是否诚实。

## 已批准且不要重开的内容

继续保持：

```text
TODO -> DOING -> ADAPTING -> DONE
```

以及：

- Project item = top-level tracking Issue；
- plugin TODO = failure/evidence/maturity inbox；
- task/workflow = execution evidence；
- WAITING/BLOCKED 不是第五状态；
- Resolution commit；
- full-inbox coverage + dedupe/disposition；
- raw NEW 可以作为 Project TODO，但 source maturity仍 NEW；
- Project lifecycle != plugin TODO maturity；
- TODO_COVERAGE.md 只是一次性 completeness evidence；
- BOARD-01；
- BOARD-UX-01；
- BOARD-SYNC-01；
- Codex 修改 Kanban reader-facing copy 必须调用 Clear Writing；
- no controller/watcher/GitHub Action/database/registry/ledger/state machine。

没有新的直接事实时，不要移动这些终点。

## BOARD-CONSUMER-01 的 v4 返修

v4 将 canonical board policy 唯一放在：

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

其他入口只保留 trigger + locator + 最小必须语义。

### Consumer 1 — ChatGPT Project instructions

AI Research Stack Project instructions 作为 GPT normal-entry consumer。

v4 给出未来 v0.3 应一次性加入的最小文本：

```text
AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。
```

如果当前 Project instructions 只能由用户/Project editor 改，future execution v0.3 只允许一次 HUMAN_ONLY setup，same-Goal resume；以后 routine sync 不重复问。

### Consumer 2 — AI_Skills AGENTS

Codex normal entry 用短 locator：

- AI_Skills TODO / Planner / Critic / adaptation / closure 要读取 canonical board doc；
- routine reconciliation 不等用户提醒；
- Codex 修改 board copy 时使用 Clear Writing；
- 不复制完整 policy。

### Consumer 3 — Planner Role Contract

正式 AI_Skills maintenance round：

- triage -> tracking Issue / pending mutation；
- first substantive Plan/design -> DOING + current anchor；
- handoff -> current next action/evidence；
- central implementation complete + machine consumers pending -> ADAPTING + freeze required consumers；
- no-tool surface -> exact pending mutation；
- no user manual sync。

### Consumer 4 — Critic Role Contract

formal review：

- review locator；
- next action；
- lifecycle truth；
- PASS/REVISE 本身不机械改变 status；
- implementation Reviewer PASS 只有在 central implementation / canonical closure成立后才允许进入 ADAPTING；
- no-tool surface -> exact pending mutation；
- Critic仍不改 Proposal、不推进 CURRENT、不冒充 Executor。

### Downstream consumer — AI Skills Maintainer

machine-update capability production-ready 后：

- 执行 required machine adaptation；
- verified install/load + normal-entry/fresh-session consumption；
- 有 Project mutation能力 -> 直接更新；
- 无能力 -> exact completion mutation，自动交下一 Project-capable executor；
- 不能只报 PASS 然后让用户更新 board。

capability 未 production-ready时，对应 workflow保持 ADAPTING。

## 用户刚补充的两层完成语义

v4 现在明确：

### Central implementation complete / “插件本身已经做完”

```text
execution package Critic PASS
-> Codex implementation
-> independent Critic/Reviewer implementation review PASS
-> canonical owner integration/release closure（若 frozen Goal 要求）
= central implementation complete
```

execution-ready Critic PASS 本身仍只是 pre-execution approval。

对 machine-consumed workflow，到 central implementation complete 后：

```text
DOING -> ADAPTING
```

### Fully closed / workflow DONE

只有 required machine consumers 全部 actual adaptation + normal-entry consumption PASS，才：

```text
ADAPTING -> DONE
```

请判断这是否忠实用户表述：

> Critic审核 execution package后，Codex执行完成，再由Critic作为Reviewer审核实现通过，才可以说插件本身做完；然后才进入机器adaptation，全部adapt完成后才彻底收尾。

特别检查 canonical integration/release closure 作为 central implementation complete 的附加条件，是否与现有 repo completion contract兼容而不是不必要抬高门槛。

## 五个 required machine consumers

用户当前明确将 machine-consumed workflow 的默认 required set 暂定为五个 logical consumer：

Server / remote Codex：

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

Local machine：

4. `Workstation`
5. `Legion`

v4 不在 policy 硬编码 hostname / SSH alias / CODEX_HOME / checkout / account。

进入 ADAPTING 的同一轮再把五个 logical consumer 解析并冻结为 exact current identities/locators。

每个 consumer至少要有：

- actual target identity；
- update/adaptation action；
- installed/loaded identity；
- normal-entry consumption；
- fresh-session/restart boundary（如适用）；
- risk-matched should-not-change/failure safety；
- durable evidence locator。

只有五个全部 PASS，或 frozen contract 对某个 consumer有合法 N/A，才 DONE。

future optional machine 不追溯扩大旧 DONE。

## 独立外部核查

请独立核对 OpenAI 官方当前文档：

1. ChatGPT Projects：
   - Project instructions 是否应用于该 Project chats；
   - 是否在 Project settings 中维护；
   - 是否是 GPT normal-entry locator 的合理位置。
2. Codex AGENTS：
   - Codex 是否自动发现并注入适用 `AGENTS.md`；
   - 是否支持把 repo AGENTS 当 Codex normal-entry locator。

优先：
- `help.openai.com`
- `developers.openai.com`

不要只复述 Planner。

## 只需要审的关键问题

### C1 — BOARD-CONSUMER-01 是否真正关闭

是否已经有明确消费面：

- ChatGPT Project instructions
- AI_Skills AGENTS
- Planner contract
- Critic contract
- future production-ready AI Skills Maintainer

canonical policy 只有一份，是否能避免 drift？

### C2 — ChatGPT Project instructions 是否过重

v4 的 exact addition 是否足够短，只做 trigger/locator/最低行为，而不是复制 policy？

一次 HUMAN_ONLY setup 后不再重复问，是否合理？

### C3 — Role contract consumer 是否破坏角色边界

Planner / Critic主动 board reconciliation 是否会：

- 让 Critic变成 Planner；
- 让 Critic推进 CURRENT；
- 让 Planner冒充 Project mutation工具；

若 v4 已通过 pending mutation边界避免这些问题，应关闭 blocker。

### C4 — 两层完成语义是否准确

必须清楚区分：

- execution-ready Critic PASS；
- Codex implementation；
- independent implementation Reviewer PASS；
- canonical central closure；
- ADAPTING；
- five-consumer full closure。

是否仍可能出现“Reviewer PASS但机器没adapt就DONE”？

### C5 — 五 consumer set 是否合理且可验收

检查：

- 是否是用户明确当前要求；
- 是否只应用 machine-consumed workflow；
- exact locators在ADAPTING时冻结是否足够；
- 是否错误要求普通 domain plugin都在五台机器部署；
- future optional machine是否不会追溯扩大旧 DONE。

### C6 — Maintainer表述是否诚实

当前 machine-update capability尚未 production-ready。

v4 是否正确：

- 不顺手实现；
- 未 ready -> ADAPTING；
- ready后 -> normal adaptation consumer；
- 完成 adaptation 后必须更新 board或输出 exact completion mutation；
- 不假装当前已经支持。

## Red team

主动寻找：

- Project instructions locator 指向 repo file但普通 thread无法访问/读取；
- role contracts只写“应该同步”却没有 no-tool pending mutation；
- Critic review PASS被误当central complete；
- implementation Reviewer PASS后还没canonical integration却过早ADAPTING；
- 五个 logical consumer 永远不解析 exact identity；
- Maintainer只打印PASS、Project不更新；
- user再次被要求手工拖卡；
- optional future machine把旧 item永远拖回ADAPTING。

若 v4 已明确覆盖，不要为了“更保险”新增机制。

## 期望输出

先自然中文回答：

1. BOARD-CONSUMER-01 是否关闭；
2. ChatGPT Project instructions / Codex AGENTS / Planner-Critic contracts / Maintainer 的职责是否分层正确；
3. “插件本身做完”与“workflow彻底收尾”的区分是否正确；
4. 五个 required consumers 是否合理；
5. 是否存在新的 blocker。

然后：

```text
RESULT = PASS | REVISE
REVIEW_STAGE = DESIGN_AMENDMENT_REVISION_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_PROPOSAL_2026-09-24.md
REVIEWED_PROPOSAL_COMMIT = ad3694882b7f48c9136e9c2058151bcaee73ef00
RECHECKED_BLOCKERS = BOARD-CONSUMER-01
```

如果 REVISE：

- 新 blocker 只来自新事实、遗漏关键直接风险或 v4 引入的真实回归；
- stable ID；
- direct evidence / causal risk / minimum close condition；
- 自动生成完整 Planner返修 prompt。

如果 PASS：

- 明确 PASS 只批准 v4 amendment；
- 当前 execution v0.2 仍不可执行；
- 下一步 Planner 必须生成完整 execution package v0.3；
- v0.3 再做 execution-ready Critic review；
- 自动生成完整 Planner prompt，不让用户拼 locator。

## Review 文件授权

用户若把本 prompt 原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_CRITIC_REVIEW_2026-09-24.md`

并 ordinary non-force push。

除此之外禁止修改：

- v4 Proposal；
- v0.2 Plan/Goal/Kickoff；
- AGENTS / Planner/Critic contracts / TODO / README；
- ChatGPT Project instructions；
- Project / Issue；
- plugin source；
- AI Skills Maintainer source；
- Bridge Kit；
- server / local machine / Host；
- 任何其他 repo。

提交后报告 exact review commit。
