# AI Skills 维护看板与完成语义 — Critic Prompt v5

你是 AI Research Stack 的独立 Critic thread。

当前只复核 v5 是否关闭上一轮唯一 stable blocker `BOARD-MAINTAINER-SCOPE-01`。不要重新设计已经通过的四状态、BOARD-01、BOARD-UX-01、BOARD-SYNC-01、Clear Writing、full-inbox coverage、raw NEW tracking、BOARD-CONSUMER-01 或五 consumer DONE requirement。

本轮只读审查，不执行、不创建 GitHub Project/Issue、不做 backfill、不启动 Codex、不调用 paid API、不修改 production/server/local-machine/Host/Bridge Kit。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = DESIGN_AMENDMENT_REVISION_REVIEW
proposal_path_and_version = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md v5
proposal_commit = d14565e152b9b953c76c0722ad6e6343850335a7
previous_proposal = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_PROPOSAL_2026-09-24.md
previous_proposal_commit = ad3694882b7f48c9136e9c2058151bcaee73ef00
previous_critic_review = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_CRITIC_REVIEW_2026-09-24.md
previous_critic_review_commit = 9bf62bdce9d9da87a0fbc6b2ff73ea6ed20f3295
stable_blocker_to_recheck = BOARD-MAINTAINER-SCOPE-01
execution_branch/worktree = NONE
```

## 必须先实际读取最新 main

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_CRITIC_REVIEW_2026-09-24.md`
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md`

按需读取：

- v4 Proposal；
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`；
- current maintenance-board execution v0.2，只用于确认 v5 PASS 后 future v0.3 要怎样返修。

## 已关闭且本轮不要重开的内容

保持：

```text
TODO -> DOING -> ADAPTING -> DONE
```

以及：

- BOARD-01；
- BOARD-UX-01；
- BOARD-SYNC-01；
- BOARD-CONSUMER-01；
- Clear Writing；
- full-inbox coverage；
- raw NEW 可以作为 Project TODO，但 source maturity 不变；
- Project lifecycle != plugin TODO maturity；
- TODO_COVERAGE.md 只是一轮 bootstrap completeness evidence；
- “插件本身做完”与“workflow 彻底收尾”两层完成语义；
- machine-consumed workflow 才需要五 consumer closure；
- future optional machine 不追溯扩大旧 DONE；
- 不新增 controller/watcher/GitHub Action/database/registry/ledger/state machine。

没有新的直接证据时，不要移动这些终点。

## 当前五个 required logical consumers

对 machine-consumed workflow/shared maintenance mechanism，当前默认 required set：

### Server / remote Codex

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

### Local machine

4. `Workstation`
5. `Legion`

进入 ADAPTING 的同一轮再解析并冻结 exact current identities/locators。

普通纯文档、纯审计、单一 artifact quality improvement、普通 domain plugin professional improvement 不自动继承五机 rollout。

## BOARD-MAINTAINER-SCOPE-01 的 v5 返修

上一轮 blocker 指出：

> current AI Skills Maintainer machine-update architecture 明确是 one current Codex machine/server，且禁止 cross-machine controller；v4 如果写成“一台 Maintainer 适配五个 consumer”，会偷改其 architecture。

v5 现在明确：

### 1. AI Skills Maintainer = per-consumer adaptation normal executor

对每一个 required consumer：

- 在该 consumer 的 current Codex environment 中调用 production-ready AI Skills Maintainer；
- 或使用另行批准、边界清楚的 existing remote execution route；
- Maintainer只负责**当前 consumer**：
  - discovery；
  - adaptation/update；
  - installed/loaded identity；
  - fresh-session / normal-entry verification；
  - durable evidence；
  - current-consumer PASS / truthful blocker。

不要求、也不允许它成为五机 central orchestrator。

### 2. 五 consumer aggregation = tracking Issue / Project lifecycle

tracking Issue 持有：

```text
Required consumers:
- Longleaf_Codex: PENDING | PASS | N/A(frozen reason)
- Longleaf_Backup_Codex: PENDING | PASS | N/A(frozen reason)
- CUHK_Workstation_WSL_Codex: PENDING | PASS | N/A(frozen reason)
- Workstation: PENDING | PASS | N/A(frozen reason)
- Legion: PENDING | PASS | N/A(frozen reason)
```

每项要有 exact identity + durable evidence locator。

这只是当前 top-level idea 的 completion evidence，不是 machine registry/schema。

### 3. Per-consumer completion mutation

如果当前 Maintainer有 Project mutation capability：

- 更新对应 consumer evidence / checklist；
- 仍有 pending -> Status 保持 ADAPTING。

如果没有：

- 输出 exact completion mutation；
- 下一 Project-capable Codex/Maintainer自动消费；
- 不要求用户手工拖卡。

### 4. 最终 DONE 只由聚合层决定

单台 Maintainer PASS 不得关闭 top-level Issue。

只有 tracking Issue确认五 consumer全部 PASS/N/A，并满足完整 closure：

```text
five-consumer aggregate complete
+ durable evidence
+ Resolution commit
+ completed close
-> DONE
```

### 5. 明确禁止新的跨机控制面

v5 禁止：

- cross-machine controller；
- machine registry/inventory service；
- watcher；
- background sync daemon；
- central credential broker；
- new cross-machine state machine；
- persistent remote orchestrator；
- 为 Kanban 新建 remote-control service。

### 6. 不新增 standalone Kanban skill/plugin

v5 architecture decision：

```text
canonical board policy
  docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

ChatGPT normal entry
  Project instructions short trigger/locator

Codex repo normal entry
  AGENTS short locator

formal Planner/Critic
  role-contract consumption

central repo maintenance
  existing ai-skills-repository-maintainer
  -> future short board locator/closure-consumption rule only

machine adaptation
  future machine-update-orchestrator
  -> per-consumer adaptation
```

当前不新增：

- standalone board skill；
- kanban-sync skill；
- new plugin/profile；
- board-specific MCP/service。

只有未来真实 failure证明机械 Project mutation复杂到 existing layers 无法承担，才另行 Planner/Critic评估 helper。

## 两层完成语义仍保持

### Central implementation complete / “插件本身做完”

```text
execution package Critic PASS
-> Codex implementation
-> independent Critic/Reviewer implementation review PASS
-> canonical owner integration/release closure（若 frozen Goal 要求）
= central implementation complete
```

对 machine-consumed workflow：

```text
DOING -> ADAPTING
```

### Fully closed

五 consumer required adaptation全部 PASS/N/A + normal-entry consumption + durable evidence + Resolution commit + completed close：

```text
ADAPTING -> DONE
```

请确认一台 consumer 的 Maintainer PASS 不会被误作整个 workflow DONE。

## BOARD-CONSUMER-01 继续保持关闭

v5 仍保留：

- ChatGPT Project instructions normal entry；
- AI_Skills AGENTS Codex normal entry；
- Planner Role Contract consumption；
- Critic Role Contract consumption；
- no-tool surface exact pending mutation；
- no user manual Kanban maintenance；
- future Maintainer downstream consumption。

canonical policy 只有 `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` 一份。

## 独立外部现实核查

请做针对性官方核查，优先 OpenAI 官方当前文档：

- Plugins / plugin packaging；
- Codex environment/session/plugin loading；
- AGENTS consumption。

重点只判断：

> 是否存在足够官方依据要求/默认允许把普通 AI Skills Maintainer plugin 设计成跨五台机器的 central controller？

若没有，不应为了“更自动”扩大当前 repo 已冻结的 one-current-machine architecture。

不要把“官方没有写”夸大成“技术上绝对不可能”。

## 只需要审的关键问题

### M1 — BOARD-MAINTAINER-SCOPE-01 是否关闭

v5 是否已经明确：

- Maintainer per-consumer；
- Project/tracking Issue aggregate five consumers；
- no cross-machine controller。

### M2 — completion mutation 是否足够

无 Project mutation capability时输出 exact consumer completion mutation，下一 Project-capable executor自动消费，是否能关闭“Maintainer只打印PASS然后用户自己更新”的风险？

### M3 — 五 consumer聚合是否仍真实可验收

是否会出现：

- consumer PASS无 evidence；
- logical name永远不解析 exact identity；
- 某一台 PASS被误当全部 PASS；
- future optional machine追溯扩大旧 DONE。

### M4 — 不新增 Kanban skill 是否正确

当前是否真的没有独立 user capability / trigger gap 支持新 standalone skill/plugin？

现有：

- Project instructions；
- AGENTS；
- role contracts；
- ai-skills-repository-maintainer；
- future machine-update-orchestrator；

是否已经足够覆盖 owner？

### M5 — 是否仍保持用户真正要的最终效果

用户要的是：

- GPT自己推进语义；
- Codex / Maintainer做机械执行；
- 五个 consumer都真正消费后才彻底收尾；
- 不让用户手工拖卡；
- 不因此造一个跨机 control plane。

v5 是否同时满足？

## Red team

至少主动检查：

- 一台 Maintainer通过remote route偷偷变成cross-machine controller；
- tracking Issue被误用成长期machine registry；
- exact completion mutation丢失consumer identity/evidence；
- final Project-capable executor不核验pending mutation freshness；
- standalone skill虽然没建但normal entry反而缺失；
- ai-skills-repository-maintainer被迫承担machine adaptation；
- machine-update-orchestrator被迫承担五机aggregation；
- 用户又成为人工aggregator。

已覆盖就不要为了“还能更保险”新增机制。

## 期望输出

先自然中文回答：

1. `BOARD-MAINTAINER-SCOPE-01` 是否关闭；
2. Maintainer per-consumer / Project aggregate 分层是否正确；
3. 不新增 standalone Kanban skill/plugin 是否正确；
4. 五 consumer DONE requirement 是否仍完整；
5. 是否有新 direct blocker。

然后：

```text
RESULT = PASS | REVISE
REVIEW_STAGE = DESIGN_AMENDMENT_REVISION_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md
REVIEWED_PROPOSAL_COMMIT = d14565e152b9b953c76c0722ad6e6343850335a7
RECHECKED_BLOCKERS = BOARD-MAINTAINER-SCOPE-01
```

如果 REVISE：

- 新 blocker 只能来自新事实、遗漏关键直接风险或 v5 引入的真实回归；
- stable ID；
- direct evidence / causal risk / minimum close condition；
- 按 Critic Role Contract 自动生成完整 Planner返修 prompt。

如果 PASS：

- 明确只批准 v5 amendment；
- current execution v0.2仍不可执行；
- 下一步 Planner要生成完整 execution package v0.3；
- v0.3 仍需独立 execution-ready Critic review；
- 自动生成完整 Planner prompt，不让用户拼 locator。

## Review 文件授权

用户若把本 prompt 原样发送给你，即授权你只在：

`YuukiAS/AI_Skills_Collection`

最新 `main` 上新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_CRITIC_REVIEW_2026-09-24.md`

并 ordinary non-force push。

除此之外禁止修改：

- v5 Proposal；
- current execution package；
- AGENTS / Planner/Critic contracts / TODO / README；
- Project / Issue；
- plugin source；
- AI Skills Maintainer machine-update source；
- Bridge Kit；
- server / local machine / Host；
- 任何其他 repo。

提交后报告 exact review commit。
