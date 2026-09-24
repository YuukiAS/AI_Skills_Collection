# AI Skills 维护看板与完成语义 — Planner Proposal v5

- 日期：2026-09-24
- Human label：AI Skills 维护看板与完成语义
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- source_branch_or_ref：`main`
- Planner baseline：`main@9bf62bdce9d9da87a0fbc6b2ff73ea6ed20f3295`
- supersedes：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_PROPOSAL_2026-09-24.md`
- v4 reviewed proposal commit：`ad3694882b7f48c9136e9c2058151bcaee73ef00`
- v4 Critic review：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V4_CRITIC_REVIEW_2026-09-24.md`
- v4 Critic review commit：`9bf62bdce9d9da87a0fbc6b2ff73ea6ed20f3295`
- rechecked blocker：`BOARD-CONSUMER-01 = CLOSED`
- stable blocker：`BOARD-MAINTAINER-SCOPE-01`
- execution branch/worktree：NONE
- 状态：DRAFT_FOR_CRITIC_REVIEW_R5

## 1. 结论

```text
BOARD-MAINTAINER-SCOPE-01 = ACCEPT
```

v5 只澄清一个边界：

> **AI Skills Maintainer 是 per-consumer adaptation normal executor，不是五台机器的 cross-machine controller。**

五个 required machine consumers 的聚合、完成真值与最终 DONE 都由 **tracking Issue + Project lifecycle** 持有，不由任何一台机器上的 Maintainer 实例持有。

其余已经通过或未被 Critic 质疑的设计全部保留：

```text
TODO -> DOING -> ADAPTING -> DONE
```

并继续保持：

- BOARD-01；
- BOARD-UX-01；
- BOARD-SYNC-01；
- Clear Writing；
- full-inbox coverage；
- raw NEW tracking；
- Project lifecycle 与 plugin TODO maturity 分离；
- ChatGPT Project instructions / AGENTS / Planner-Critic contracts 的 consumer binding；
- 两层完成语义；
- 当前五个 required logical consumers；
- future optional machine 不追溯扩大旧 DONE；
- 不新增 controller / watcher / GitHub Action / database / registry / ledger / state machine。

## 2. 两层完成语义保持不变

### 2.1 Central implementation complete / “插件本身已经做完”

对正式 AI_Skills plugin / workflow implementation：

```text
execution package Critic PASS
-> Codex implementation
-> independent Critic/Reviewer implementation review PASS
-> canonical owner integration / release closure（若 frozen Goal 要求）
= central implementation complete
```

说明：

- execution-ready Critic PASS 只是允许开始实现；
- Codex 自报完成不算；
- 必须有独立 implementation review PASS；
- frozen Goal 若要求 canonical integration / release closure，则 reviewed candidate 真正进入 canonical owner 后才算 central implementation complete。

对 machine-consumed workflow：

```text
central implementation complete
-> DOING -> ADAPTING
```

### 2.2 Fully closed / “workflow 彻底收尾”

machine-consumed workflow 只有 required consumers 全部真实适配并通过 normal-entry consumption，才允许：

```text
ADAPTING -> DONE
```

因此“插件本身完成”是进入 ADAPTING 的条件，不是 Project DONE。

## 3. 当前 required logical consumer set 保持不变

对 machine-consumed workflow/shared maintenance mechanism，当前默认 required logical consumers：

### Server / remote Codex consumers

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

### Local-machine consumers

4. `Workstation`
5. `Legion`

这些只是当前 completion contract 的 logical consumer names。

policy 不长期硬编码：

- hostname；
- SSH alias；
- CODEX_HOME；
- checkout path；
- account；
- private path；
- credential。

进入 ADAPTING 的同一轮，tracking Issue 必须把五个 logical consumers 分别解析并冻结为当时 exact current identities/locators。

## 4. 每个 required consumer 的完成条件

每个 consumer 至少需要：

1. actual target identity；
2. approved adaptation/update action；
3. installed/loaded identity；
4. relevant normal-entry consumption；
5. fresh-session/restart boundary（如加载机制要求）；
6. risk-matched should-not-change / failure safety；
7. durable evidence locator。

以下都不能单独证明 consumer PASS：

- repo pull；
- 文件存在；
- source SKILL 已读；
- install helper PASS；
- synthetic fixture PASS；
- Maintainer 只打印 success summary。

只有 tracking Issue 中该 consumer 的真实 evidence 足够，才可标 PASS。

## 5. BOARD-MAINTAINER-SCOPE-01 — per-consumer executor contract

### 5.1 当前 machine-update architecture 的 authority

当前独立设计：

- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md`

明确将 AI Skills Maintainer 的目标定义为：

> update/adapt AI Research Stack on **one current Codex machine/server**

并明确 non-goal：

```text
cross-machine controller
```

本 board contract 不得扩大这个 frozen architecture。

### 5.2 Maintainer 只负责当前 consumer

对每个 required consumer，正常路线是：

1. 在该 consumer 的 current Codex environment 中调用 production-ready AI Skills Maintainer；
2. Maintainer 只对**当前 consumer**做：
   - discovery；
   - release/update-impact resolution；
   - adaptation/update；
   - installed/loaded identity verification；
   - fresh-session / normal-entry verification；
   - durable evidence generation；
3. 完成后返回当前 consumer 的 PASS / truthful blocker。

如果已有另行批准、权限边界清楚的 remote execution route 可以合法到达该 consumer，也可以使用该 route，但这只是执行某一个 consumer 的 adaptation；不能因此把 AI Skills Maintainer 变成新的 cross-machine controller。

### 5.3 五 consumer aggregation 只属于 tracking Issue / Project lifecycle

tracking Issue 是五 consumer completion truth 的唯一 top-level aggregation owner。

进入 ADAPTING 后，Issue 详细区记录：

```text
Required consumers:
- Longleaf_Codex: PENDING | PASS | N/A(frozen reason)
- Longleaf_Backup_Codex: PENDING | PASS | N/A(frozen reason)
- CUHK_Workstation_WSL_Codex: PENDING | PASS | N/A(frozen reason)
- Workstation: PENDING | PASS | N/A(frozen reason)
- Legion: PENDING | PASS | N/A(frozen reason)
```

每一行都必须有 exact current identity + durable evidence locator。

这不是 machine registry；它只是当前 top-level idea 的 completion evidence。

### 5.4 Per-consumer completion mutation

每个 consumer 完成后：

#### 如果当前 Maintainer 有 GitHub Project mutation capability

它可以直接：

- 更新 tracking Issue 的该 consumer evidence；
- 将该 consumer 行更新为 PASS；
- 更新 top summary / next action；
- 如仍有 consumer pending，保持 ADAPTING。

#### 如果当前 Maintainer 没有 Project mutation capability

它必须输出 exact completion mutation，例如：

```text
待同步到 Project：
- tracking Issue: #123
- consumer: Longleaf_Codex
- consumer result: PASS
- exact consumer identity: <locator>
- adaptation evidence: <locator>
- normal-entry evidence: <locator>
- lifecycle Status: ADAPTING
- next action: adapt Longleaf_Backup_Codex
```

下一 Project-capable Codex / Maintainer / maintenance action必须在做后续 board mutation 前：

1. 核对 mutation 仍对应当前 tracking Issue；
2. 核对 evidence 未过期；
3. 机械应用。

不得要求用户手工拖 Kanban。

### 5.5 最终 DONE 只能由聚合层决定

任意单台机器上的 Maintainer：

- 不拥有五 consumer completion truth；
- 不得因为当前 consumer PASS 就关闭 top-level Issue；
- 不得把 Project 状态直接改 DONE，除非它同时作为 Project-capable executor读取 tracking Issue，确认五个 required consumers 已全部 PASS/N/A，并满足完整 DONE contract。

最终 closure 仍是：

```text
tracking Issue confirms all five required consumers PASS/N/A
+ durable evidence complete
+ Resolution commit
+ completed close
-> DONE
```

## 6. 明确禁止 cross-machine control plane

本 board contract 不授权、也不要求实现：

- cross-machine controller；
- machine registry；
- machine inventory service；
- watcher；
- background sync daemon；
- central credential broker；
- 新跨机 state machine；
- 常驻 remote orchestrator；
- 自动扫描所有机器；
- 为了 Kanban 新增远程控制服务。

如果未来真实使用证明现有 per-consumer route 无法合理完成机械适配，再单独经 Planner–Critic 评估最小 helper；当前没有证据支持预先增加。

## 7. 不新增 standalone Kanban skill / plugin

### 7.1 Architecture decision

当前不新增：

- standalone maintenance-board skill；
- `kanban-sync` top-level skill；
- 新 plugin；
- 新 profile；
- 新 board-specific MCP/service。

原因：

1. board 首先是 repository-maintenance lifecycle contract，不是用户需要主动触发的独立专业任务；
2. ChatGPT 普通 thread 的入口由 Project instructions消费；
3. Codex repo入口由 AGENTS消费；
4. Planner/Critic职责由 role contracts消费；
5. central maintenance已经有 `ai-skills-repository-maintainer`；
6. machine adaptation已有独立规划中的 `machine-update-orchestrator`；
7. 再建 board skill 会新增 trigger/owner 冲突，却不能替代 Project instructions / AGENTS。

### 7.2 现有 ai-skills-repository-maintainer 的未来消费

central maintenance 使用 existing `ai-skills-repository-maintainer`。

future implementation 只需给它增加一个短 board locator / closure-consumption rule，例如语义上要求：

- central maintenance工作读取 canonical board policy；
- release/central closure后若 machine-consumed work仍有 required consumers -> ADAPTING；
- 无 Project mutation tool -> exact pending mutation。

不在本 board design round修改其 source。

### 7.3 何时才重新考虑 helper/skill

只有未来真实失败证明：

- Project mutation机械步骤在多个 maintenance route反复失败；
- 现有 canonical doc + GitHub CLI/API + existing maintainer 无法可靠承担；
- 且有清楚 user-visible failure / independent value；

才允许重新进入 Planner–Critic，评估内部 helper/skill。

当前不预造。

## 8. Canonical policy 与 normal-entry consumers

唯一 canonical board policy：

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

其他 surface只存 trigger + locator + 最小行为。

### 8.1 ChatGPT Project instructions — GPT normal entry

AI Research Stack Project instructions 只增加短 trigger/locator：

```text
AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。
```

如果 ChatGPT Project settings只能用户/Project editor修改，future execution package只允许一次 HUMAN_ONLY exact-text setup；完成后不重复询问。

### 8.2 AI_Skills AGENTS — Codex normal entry

短 locator覆盖：

- AI_Skills TODO / Planner / Critic / adaptation / closure工作读取 canonical board doc；
- routine board sync不等用户提醒；
- Codex修改 board reader-facing copy时使用 Clear Writing；
- 不复制完整 board policy。

### 8.3 Planner Role Contract

formal AI_Skills maintenance round：

- triage进入 tracking scope -> create/bind Issue或 exact pending mutation；
- first substantive design -> DOING + current anchor；
- handoff -> next action/evidence；
- central implementation complete + required machine consumers pending -> ADAPTING + freeze exact consumer locators；
- 无 Project mutation能力 -> exact pending mutation；
- 不让用户手工同步。

### 8.4 Critic Role Contract

formal Critic review：

- review locator；
- next action；
- lifecycle truth；
- PASS/REVISE本身不机械改变 Status；
- implementation Reviewer PASS + required canonical closure完成后，machine-consumed item才进入 ADAPTING；
- 无 Project mutation能力 -> exact pending mutation；
- 不改 Planner Proposal；
- 不推进 Reviewed Handoff CURRENT；
- 不冒充 Executor。

### 8.5 Future machine-update-orchestrator

production-ready 后只作为 **per-current-consumer adaptation executor**。

它不持有五 consumer总状态，不新增跨机控制面。

## 9. full-inbox coverage 保持不变

第一次 bootstrap扫描全部 current canonical maintenance inbox。

每个仍有维护意义的条目必须有 disposition：

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

raw `NEW` 可以进入 Project TODO，但 source maturity保持 NEW。

`Project lifecycle status != plugin TODO maturity status`

一次性 evidence：

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

只证明 completeness，不成为 registry/schema。

## 10. BOARD-UX / Clear Writing 保持不变

Project 是用户直接消费的 artifact。

所有 tracking Issue 顶部保持：

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

Codex创建/修改 reader-facing board copy时必须真实调用 Clear Writing（`writing-style`）。

Clear Writing不得改变：

- maturity；
- lifecycle truth；
- consumer PASS/N/A；
- Area；
- exact locators；
- Resolution commit；
- evidence meaning。

实际 GitHub Project surface qualitative review仍是最终权威。

## 11. Steady-state end-to-end flow

```text
真实项目 thread
-> raw NEW 写 canonical inbox
-> tracking scope -> Project TODO
-> Planner first substantive round
-> DOING
-> execution package Critic PASS（仍 DOING）
-> Codex implementation
-> independent Critic/Reviewer implementation PASS
-> canonical integration/release closure（若 Goal 要求）
-> central implementation complete
-> machine-consumed workflow: ADAPTING
-> 对五个 required consumers 分别在其 current environment 调用 production-ready Maintainer
-> 每个 consumer PASS -> Project update或 exact completion mutation
-> tracking Issue聚合五 consumer 全部 PASS/N/A
-> Resolution commit + completed close
-> DONE
```

整个流程中，用户不负责 routine Kanban maintenance。

## 12. 用户当前五 consumer contract 的适用边界

默认五 consumer要求只用于 machine-consumed workflow/shared maintenance mechanism，例如：

- workflow-core execution/delivery/Human Gate/Reviewed Handoff behavior；
- ai-skills-core machine update/install/distribution/adaptation behavior；
- repo-wide/cross-plugin shared workflow；
- Bridge/AI_Skills联动且必须在真实 Codex runtime消费的 shared rule；
- 其他明确需要 install/reload/profile/Host/machine consumer才生效的机制。

普通：

- 纯文档；
- 纯审计；
- 单一 artifact quality improvement；
- 普通 domain plugin专业质量改进；

不自动要求五 consumer rollout。

## 13. future optional consumer 与 N/A

进入 ADAPTING时冻结当前 exact required consumer set。

之后新增 optional machine：

- 默认新建 follow-up；
- 不追溯扩大旧 DONE。

合法 N/A 必须在 frozen completion contract有直接理由，不能为快点关闭临时宣布。

## 14. 外部现实核查

本轮做了针对性 OpenAI 官方文档核查。

官方 plugin 文档把 plugin描述为把 skills/MCP加载到具体 environment/session，Codex的 repo plugin settings也作用于具体 local project/environment。没有本轮读到的官方能力依据支持把一个普通 plugin默认视为“跨五台机器中央控制器”。

采用结论：

> 不从 plugin 能力推断跨机 orchestration；继续服从当前 repo 已冻结的 one-current-machine Maintainer architecture，五 consumer 聚合留给 tracking Issue / Project lifecycle。

官方来源：

- https://developers.openai.com/plugins
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/api/docs/guides/agents-api/overview

这不是声称跨机控制技术上绝对不可能；只是当前设计没有证据或授权去新增它。

## 15. Alternatives

### A. 一台 Maintainer orchestrate五台机器

拒绝。与 current machine-update architecture 的 one-current-machine boundary直接冲突，并引入 credential/controller风险。

### B. 每台 consumer independently adapt，tracking Issue聚合

采用。符合用户“五台都完成才 DONE”，同时保持 Maintainer单机边界。

### C. 新建 Kanban skill / plugin

拒绝。入口与 owner已经由 Project instructions / AGENTS / role contracts / existing maintainer覆盖。

### D. 新增后台 watcher/controller

拒绝。没有必要的 user-visible failure证据。

### E. 用户手工汇总五台机器

拒绝。违反 BOARD-SYNC-01。

## 16. v5 对 future execution package 的影响

v5 PASS 后，current execution v0.2仍不可执行。

Planner必须生成完整 execution package v0.3，至少冻结：

1. canonical board doc；
2. ChatGPT Project instructions一次性 setup；
3. AGENTS short locator；
4. Planner/Critic role-contract consumption；
5. full-inbox coverage；
6. raw NEW tracking；
7. Clear Writing；
8. BOARD-01；
9. central implementation complete -> ADAPTING cutover；
10. 当前五 logical consumers；
11. ADAPTING时 exact consumer resolution；
12. per-consumer Maintainer semantics；
13. consumer completion mutation；
14. no cross-machine controller；
15. TODO_COVERAGE evidence；
16. five-consumer aggregation/final DONE evidence；
17. no standalone Kanban skill/plugin；
18. independent execution-ready Critic review。

## 17. Non-goals

本设计轮不：

- 修改 ChatGPT Project settings；
- 修改 AGENTS / Planner/Critic contracts；
- 修改 ai-skills-repository-maintainer；
- 修改 machine-update-orchestrator；
- 创建 Project / Issue；
- backfill；
- 访问/适配任一 machine；
- 新增 remote controller/helper；
- 修改 Bridge Kit；
- 调用 paid API；
- 改版本。

## 18. BOARD-MAINTAINER-SCOPE-01 disposition

```text
BOARD-MAINTAINER-SCOPE-01 = ACCEPT
```

关闭条件对应关系：

1. Maintainer = per-consumer normal executor；
2. tracking Issue / Project = five-consumer aggregation owner；
3. 每个 consumer在自己的 current environment执行Maintainer或另行批准的现有 remote route；
4. Maintainer只负责当前 consumer的 discovery/adaptation/verification/evidence；
5. 有 Project mutation -> 更新当前 consumer；无能力 -> exact completion mutation；
6. 只有聚合层确认五个 PASS/N/A -> Resolution commit + close -> DONE；
7. 明确禁止 cross-machine controller / machine registry / watcher / daemon / credential broker / new state machine；
8. 不新增 standalone Kanban skill/plugin；
9. BOARD-CONSUMER-01 的四个 normal-entry consumers + future Maintainer downstream consumption继续保留。

## 19. 当前 blocker 状态

Planner未发现新的直接证据支持新增 blocker。

```text
BOARD-MAINTAINER-SCOPE-01 = ACCEPTED_AND_REVISED
NEW_BLOCKERS_FOUND_BY_PLANNER = NONE
NEXT_HANDOFF = CRITIC
```
