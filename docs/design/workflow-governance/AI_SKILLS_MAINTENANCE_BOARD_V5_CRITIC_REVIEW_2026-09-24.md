# AI Skills 维护看板与完成语义 — Critic Review v5

- 日期：2026-09-24
- Review stage：`DESIGN_AMENDMENT_REVISION_REVIEW`
- Result：`PASS`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- reviewed proposal：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md` v5
- reviewed proposal commit：`d14565e152b9b953c76c0722ad6e6343850335a7`
- previous review：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_CRITIC_REVIEW_2026-09-24.md`
- previous review commit：`9bf62bdce9d9da87a0fbc6b2ff73ea6ed20f3295`
- rechecked blocker：`BOARD-MAINTAINER-SCOPE-01`
- execution branch/worktree：NONE

## 1. 结论

`BOARD-MAINTAINER-SCOPE-01` 已关闭，本轮没有新的直接 blocker。

v5 已把 AI Skills Maintainer 从“可能被误读为五机 central orchestrator”收窄为 **per-current-consumer adaptation executor**：

- 每个 required consumer 在自己的 current Codex environment 中独立运行 production-ready Maintainer，或走另行批准的现有 remote execution route；
- Maintainer 只负责当前 consumer 的 discovery / adaptation / installed-loaded identity / fresh-session or normal-entry verification / durable evidence；
- 五 consumer 的 aggregate completion truth 由 tracking Issue / Project lifecycle 持有；
- 单台 consumer PASS 不能关闭 top-level Issue；
- 没有 Project mutation capability 时，Maintainer 输出 exact consumer completion mutation，由下一 Project-capable maintenance action在核对 tracking Issue 与 evidence freshness 后机械应用；
- 明确禁止 cross-machine controller、machine registry、watcher、daemon、central credential broker、新跨机 state machine和 board-specific remote-control service。

这与当前独立 machine-update architecture 的“one current Codex machine/server”边界一致，没有偷改成跨五机控制面。

## 2. Repo/source 核对

本轮实际读取了最新 `main` 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_CRITIC_REVIEW_2026-09-24.md`
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md`

并核对 v5 Proposal 在 `main` 的 blob 与指定 proposal commit `d14565e...` 一致；后续 prompt commit 未改变 Proposal。

当前 machine-update Goal 仍是 `PLANNER_DRAFT_FOR_CRITIC`，其产品目标明确是更新/适配 **one current Codex machine/server**，并把 cross-machine controller / machine registry / daemon 等列为 non-goals。因此本轮只审 board downstream-consumer contract，不把该独立能力冒充 production-ready。

## 3. 外部现实核查

本轮重新核对 OpenAI 官方当前文档。

### 3.1 Plugins / packaging

OpenAI plugin 文档把 plugin 包装为在具体 Codex / ChatGPT environment 中加载的 skills / MCP / marketplace package；marketplace source 可按 Git ref固定，安装/更新后需要在相应 app/session 边界重新加载。

采用结论：

> plugin 能在一个具体 environment 中提供维护能力，但官方文档本身不提供依据把普通 plugin 默认视为跨多台机器的 central controller。

来源：
https://developers.openai.com/plugins/build/plugins

### 3.2 Codex AGENTS

OpenAI 当前 Codex guidance 明确说明 Codex CLI 会自动枚举适用的 `AGENTS.md` 并注入 conversation。

采用结论：

> AI_Skills `AGENTS.md` 继续适合作为 Codex normal-entry board locator；不需要用 standalone Kanban skill 替代。

来源：
https://developers.openai.com/api/docs/guides/latest-model

### 3.3 ChatGPT Project instructions

OpenAI 当前 Projects 文档说明 Project instructions 在 Project settings 中维护，并应用于该 Project 内 conversations。

采用结论：

> ChatGPT Project instructions 仍是普通 GPT thread 的正确 board trigger/locator，与 Codex AGENTS 是互补入口。

来源：
https://help.openai.com/en/articles/10169521-projects-in-chatgpt

## 4. BOARD-MAINTAINER-SCOPE-01 复核

### 4.1 Maintainer per-consumer

PASS。

v5 明确：

- Maintainer 不持有五 consumer aggregate state；
- 每次只处理 current consumer；
- remote route 必须是另行批准、边界清楚的 existing route；
- 不因为 board completion contract 自动获得跨机 remote authority。

这关闭了上一轮“为了 Kanban DONE 而把 Maintainer 偷扩成 cross-machine controller”的风险。

### 4.2 Project 聚合五 consumer

PASS。

tracking Issue 的 five-consumer checklist 是 top-level idea 的 completion evidence，不是长期 machine registry。

每个 consumer 行要求：

- logical consumer；
- exact resolved current identity；
- durable evidence locator；
- PASS / PENDING / frozen N/A。

单台 PASS 后仍保持 `ADAPTING`，直到 aggregate closure contract全部成立。

### 4.3 completion mutation

PASS。

无 Project mutation tool 时，exact mutation 至少包含：

- tracking Issue；
- consumer；
- consumer result；
- exact consumer identity；
- adaptation evidence；
- normal-entry evidence；
- lifecycle truth；
- next action。

并且下一 Project-capable action 在应用前必须：

1. 核对 mutation 仍属于当前 tracking Issue；
2. 核对 evidence 未过期；
3. 再机械应用。

这足以避免“Maintainer只打印 PASS、Project没人更新”和“过期 mutation 静默覆盖 current truth”。

### 4.4 Final DONE

PASS。

最终只有聚合层确认全部 required consumers PASS/N/A + durable evidence + Resolution commit + completed close，才允许 DONE。

一台 consumer 上的 Maintainer PASS 不拥有整个 workflow 的 completion authority。

## 5. 不新增 standalone Kanban skill / plugin

PASS，而且这是当前更简单的正确路线。

当前 board capability 的 owner 已经完整：

- canonical policy：`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- ChatGPT normal entry：Project instructions
- Codex repo entry：`AGENTS.md`
- formal Planner/Critic：role contracts
- central repository maintenance：existing `ai-skills-repository-maintainer`
- machine adaptation：future `machine-update-orchestrator`

新增 standalone board skill / `kanban-sync` skill / new plugin 不会解决 Project instructions 与 AGENTS 的入口消费问题，反而会新增 trigger 和 owner ambiguity。

只有未来真实 failure 证明 GitHub Project机械 mutation在多个 route 中反复失败、现有 canonical doc + GitHub surfaces + existing maintainer无法承担时，才有证据重新评估内部 helper/skill。

本轮不预造。

## 6. 五 consumer DONE requirement

继续 PASS，未被 v5削弱。

当前默认 logical consumers：

### Server / remote Codex
1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

### Local
4. `Workstation`
5. `Legion`

适用范围仍然只限 machine-consumed workflow/shared maintenance mechanism。

进入 ADAPTING 时再解析并冻结 exact current identity/locator；future optional machine不追溯扩大旧 DONE；普通 domain plugin / artifact improvement不自动继承五机验收。

## 7. 两层完成语义

继续 PASS：

```text
execution-ready Critic PASS
-> Codex implementation
-> independent implementation review PASS
-> canonical integration/release closure（若 frozen Goal 要求）
= central implementation complete
```

对于 machine-consumed item：

```text
central implementation complete
-> DOING -> ADAPTING
```

然后：

```text
per-consumer adaptation
-> five-consumer aggregate PASS/N/A
-> durable evidence
-> Resolution commit
-> completed close
-> DONE
```

因此 pre-execution PASS、Executor自报完成、单台 machine PASS 都不会被误当作最终 DONE。

## 8. 仍需执行层实现的 surfaces

v5 是设计 PASS，不是 implementation。

后续 v0.3 execution package 应忠实实现：

1. canonical `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
2. ChatGPT Project instructions一次性 short trigger/locator
3. AI_Skills `AGENTS.md` short locator
4. Planner Role Contract consumption
5. Critic Role Contract consumption
6. full-inbox coverage + `TODO_COVERAGE.md`
7. raw NEW Project TODO semantics
8. BOARD-01 / BOARD-UX / BOARD-SYNC / Clear Writing
9. central-complete -> ADAPTING cutover
10. five logical consumer contract + exact resolution at cutover
11. per-consumer Maintainer semantics
12. exact completion mutation freshness checks
13. no cross-machine controller
14. no standalone Kanban skill/plugin
15. final five-consumer aggregate closure

现有 execution v0.2 已经不匹配 v5 admission / consumer / closure contract，因此仍不可执行。

## 9. 审查结论

```text
RESULT = PASS
REVIEW_STAGE = DESIGN_AMENDMENT_REVISION_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md
REVIEWED_PROPOSAL_COMMIT = d14565e152b9b953c76c0722ad6e6343850335a7
RECHECKED_BLOCKERS = BOARD-MAINTAINER-SCOPE-01
CLOSED_BLOCKERS = BOARD-MAINTAINER-SCOPE-01
NEW_BLOCKERS = NONE
```

本 PASS 只批准 v5 amendment。

它不授权：

- 修改 ChatGPT Project settings；
- 修改 AGENTS / Planner / Critic contracts；
- 创建 GitHub Project / Issue；
- backfill；
- 修改 plugin / Maintainer source；
- 运行 machine adaptation；
- 访问 server/local machine；
- 修改 Bridge Kit；
- 调用 paid API；
- 执行 current v0.2 package。

下一步必须回 Planner 生成完整 execution package v0.3，并再做 execution-ready Critic review。
