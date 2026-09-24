# AI Skills 维护看板与完成语义 — Planner Proposal v4

- 日期：2026-09-24
- Human label：AI Skills 维护看板与完成语义
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- source_branch_or_ref：`main`
- Planner baseline：`main@03602cb5ecf03e4c6185413a7d780968f8d5e71e`
- supersedes：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_PROPOSAL_2026-09-24.md`
- v3 reviewed proposal commit：`fa40e081e9d30b17d94df7c81a274ad75e5e297b`
- v3 Critic review：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_CRITIC_REVIEW_2026-09-24.md`
- v3 Critic review commit：`03602cb5ecf03e4c6185413a7d780968f8d5e71e`
- stable blocker：`BOARD-CONSUMER-01`
- execution branch/worktree：NONE（本轮只做设计返修，不执行 settings/repo/plugin/machine mutation）
- 状态：DRAFT_FOR_CRITIC_REVIEW_R4

## 1. 结论

```text
BOARD-CONSUMER-01 = ACCEPT
```

v3 的两项 amendment 保持：

1. 第一次 bootstrap 要覆盖当前全部 canonical TODO inbox，但先 dedupe/disposition，不机械“一条 heading 一张 Issue”；
2. machine-consumed workflow 的 central source / plugin 本身完成，不等于整个 workflow DONE。真正收尾必须完成 required machine adaptation 与 normal-entry consumption。

本轮新增的只是 **normal-entry consumer binding**，再加上用户对“插件本身做完”和“整个 workflow 彻底收尾”的时间点进一步澄清。

四状态仍然不变：

```text
TODO -> DOING -> ADAPTING -> DONE
```

没有第五状态。

## 2. 两层完成语义：插件本身完成 != workflow 彻底收尾

用户当前明确区分两个里程碑。

### 2.1 Central implementation complete / “插件本身已经做完”

对正式 AI_Skills plugin / workflow implementation：

```text
execution package Critic PASS
-> Codex implementation
-> independent Critic/Reviewer implementation review PASS
-> canonical owner integration / release closure（若该 frozen Goal 要求）
= central implementation complete
```

解释：

- execution-ready Critic PASS 只说明“可以执行”，不能说插件做完；
- Codex 自己说实现完成也不能算；
- 必须有独立 Critic/Reviewer 实际审查最终实现并 PASS；
- 若 frozen Goal 本身要求 main integration / release identity / canonical source closure，则 reviewed candidate 真正进入 canonical owner 后，central implementation 才算完整落地。

对 machine-consumed workflow，达到这一里程碑后：

```text
Status: DOING -> ADAPTING
```

这里可以在 Issue 顶部自然语言写“中央实现已通过独立审核，正在适配实际机器”，但不新增 Project 状态字段。

### 2.2 Fully closed / “workflow 彻底收尾”

对 machine-consumed workflow，只有 required machine consumers 全部完成实际 adaptation 与正常入口验证，才允许：

```text
ADAPTING -> DONE
```

因此：

> “插件本身已经做完”是进入 ADAPTING 的前提，不是 Project DONE。

这直接防止 source/release 已完成但真实机器仍加载旧版本或旧规则时出现假完成。

## 3. 本用户当前冻结的 required machine consumer set

对需要 machine adaptation 的 AI Research Stack workflow/shared maintenance mechanism，当前默认 required consumer set 暂定为以下五个 normal-entry consumer：

### Server / remote Codex consumers

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

### Local-machine consumers

4. `Workstation`
5. `Legion`

这五个名称是当前 completion contract 的**逻辑 consumer identity**。

policy 不在这里硬编码：

- hostname；
- SSH alias；
- CODEX_HOME；
- checkout path；
- account；
- token；
- private local path。

原因是这些 runtime locator 可能变化，应由进入 ADAPTING 时的真实环境 source / AI Skills Maintainer discovery 解析。

### 3.1 ADAPTING cutover 时冻结 exact locators

进入 ADAPTING 的同一轮，tracking Issue 必须把上述五个 logical consumer 分别解析为当时真实的：

- machine / runtime identity；
- relevant installed plugin/profile/Bridge/AGENTS consumer；
- exact evidence locator；
- adaptation owner / current action。

从这一刻起，该 top-level idea 的 downstream completion contract 以这五个 exact resolved consumers 为准。

### 3.2 五个 consumer 的完成证据

每个 required consumer 至少证明：

1. actual target identity；
2. approved update/adaptation action；
3. installed / loaded identity；
4. relevant normal-entry consumption；
5. fresh-session / restart boundary（如果该 capability 的加载机制需要）；
6. risk-matched should-not-change / failure safety；
7. durable evidence locator。

仅以下情况都不够：

- repo pull 到新 commit；
- 文件存在；
- source SKILL 已读；
- install script PASS；
- 某个测试 fixture PASS；
- “AI Skills Maintainer reported success”但没有验证 normal entry。

## 4. 双环境规则的适用范围仍保持窄

五 consumer closure 默认只适用于 **machine-consumed workflow/shared maintenance mechanism**，例如：

- workflow-core execution / delivery / Human Gate / Reviewed Handoff behavior；
- ai-skills-core machine update / install / distribution / adaptation behavior；
- repo-wide / cross-plugin shared workflow；
- Bridge/AI_Skills 联动且必须进入真实 Codex runtime 才算交付的规则；
- 其他明确需要 install/reload/profile/Host/machine consumer 才会生效的机制。

普通：

- 纯文档；
- 纯 audit；
- 单一 artifact quality improvement；
- 普通 domain plugin 的专业质量改进；

不因为“也是 plugin”就自动要求五台机器都安装验证。

是否属于 machine-consumed workflow，必须在该 top-level idea 的 frozen completion contract 中明确。

## 5. future optional machine 不追溯扩大旧 DONE

对某个 tracking Issue，一旦进入 ADAPTING 时已经冻结 exact required consumer set：

- 后来新增的 optional machine / repo 默认形成新的 follow-up work item；
- 不追溯扩大旧 item；
- 只有新证据证明旧 DONE 当时声称的既有范围其实不成立，才按 regression 处理。

若用户将来明确修改默认 required machine set，则只影响之后冻结的 work item，除非用户明确要求追溯。

## 6. Amendment A 保持：第一次 full-inbox coverage

第一次 bootstrap 必须扫描所有 current canonical maintenance inbox：

- 十个中央 `docs/plugin-todos/<plugin>.md`；
- root `TODO.md` 当前正式列出的 standalone skill TODO inbox；
- 其他 root TODO 正式声明的当前 maintenance inbox。

每一个当前仍有维护意义的条目都必须有 disposition。

允许：

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

### 6.1 raw NEW

仍有效、确属中央 maintenance 的 raw `NEW`：

- duplicate -> merge 到已有 tracking Issue；
- 独立 top-level idea -> 可以创建 Project `Status=TODO` 的 tracking Issue；
- source maturity 仍保持 `NEW`，除非 Planner 后续独立做 promotion triage。

必须始终区分：

```text
Project lifecycle status != plugin TODO maturity status
```

### 6.2 coverage evidence

保留一次性：

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

至少记录：

```text
source inbox + heading
-> disposition
-> tracking Issue (if any)
-> Area
-> initial lifecycle Status
```

它只证明 bootstrap completeness，不成为长期 registry/schema。

## 7. BOARD-CONSUMER-01：canonical policy 与四个 normal-entry consumer

canonical board policy 只有一份：

`YuukiAS/AI_Skills_Collection main: docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

其他入口只保存 **trigger + locator + 最小必须语义**，不得复制整份 policy。

### 7.1 ChatGPT Project instructions — GPT normal entry

AI Research Stack 的 ChatGPT Project instructions 是 GPT 任意 thread 的 normal-entry consumer。

当前 OpenAI 官方 Projects 文档说明：

- Project instructions 应用于该 Project 内的 conversations；
- Project instructions 在 Project settings 中维护；
- 它们只在该 Project 内生效。

因此仅修改 repo `AGENTS.md` 不能保证普通 ChatGPT Project thread 自动消费 board contract。

未来 v0.3 execution package 必须准备以下**一次性最小 Project-instructions addition**：

```text
AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。
```

这是 trigger/locator，不是 policy copy。

#### 一次性 HUMAN_ONLY setup

当前本线程没有可验证的 ChatGPT Project-instructions mutation action。

如果 execution 时仍然只能由用户/Project editor 在 Project settings 修改，v0.3 必须：

1. 给出上面的 exact text；
2. 请用户只执行一次：`Project -> ... -> Project settings -> instructions` 中追加；
3. 完成后同一 Goal 自动继续；
4. 验证后不在后续 routine sync 中重复询问。

不要求用户每次 thread 手工提醒。

OpenAI 官方 Projects 文档：
https://help.openai.com/en/articles/10169521-projects-in-chatgpt

### 7.2 AI_Skills AGENTS.md — Codex normal entry

Codex normal entry 继续由 repo `AGENTS.md` 自动消费。

OpenAI 当前 Codex 官方文档说明 Codex CLI 会自动枚举并注入适用的 AGENTS 文件。

AI_Skills `AGENTS.md` 只增加短 locator，例如语义必须覆盖：

- AI_Skills TODO / Planner / Critic / adaptation / closure 工作必须读取 `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`；
- routine board reconciliation 不等用户提醒；
- Codex 修改 board reader-facing copy 时使用 Clear Writing；
- 不复制完整 lifecycle policy。

OpenAI 官方 Codex AGENTS guidance：
https://developers.openai.com/api/docs/guides/latest-model

### 7.3 Planner Role Contract — formal Planner consumer

`docs/workflows/PLANNER_ROLE_CONTRACT.md` 增加一条最小 consumption rule：

对正式 AI_Skills maintenance round：

- triage 后进入 tracking scope -> create/bind tracking Issue 或 exact pending mutation；
- first substantive Plan/design -> reconcile DOING + current anchor；
- handoff 前 -> reconcile current next action / evidence；
- central implementation complete 且剩 required machine consumers -> reconcile ADAPTING + freeze required consumers；
- 不等用户提醒；
- 无 Project mutation tool 时生成 exact pending mutation，不假装已更新。

Role contract 只引用 canonical board doc，不复制全文。

### 7.4 Critic Role Contract — formal Critic consumer

`docs/workflows/CRITIC_ROLE_CONTRACT.md` 增加一条最小 consumption rule：

每轮 formal AI_Skills maintenance review：

- 更新 / 交付 Critic review locator；
- 更新 next action；
- 核对 lifecycle truth；
- `PASS / REVISE` 本身不机械改变 Status；
- implementation Reviewer PASS 只有在 central implementation / canonical closure 真正成立后，才允许该 machine-consumed item 进入 ADAPTING；
- 无 Project mutation tool时生成 exact pending mutation；
- 不要求用户手工同步。

Critic 仍然：

- 不改 Planner Proposal；
- 不推进 Reviewed Handoff CURRENT；
- 不冒充 Executor。

board evidence/status reconciliation 不改变这些角色边界。

## 8. AI Skills Maintainer — downstream machine-adaptation consumer

当前 repo 已有独立设计：

- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md`

它明确把 AI Skills Maintainer 设计为当前 Codex machine/server 的 update/adaptation normal entry。

但当前 source 不能证明该 machine-update capability 已 production-ready。

因此 v4 只冻结 consumer contract，不修改/发布它。

### 8.1 当前状态

在 AI Skills Maintainer machine-update capability 未正式发布前：

- board item 可以进入 ADAPTING；
- current anchor 必须说明 Maintainer rollout 是 blocker，或指向另一个已批准的真实 adaptation owner；
- 不得因为“未来 Maintainer 会做”而标 DONE。

### 8.2 production-ready 后

当该 capability 正式发布后，machine-consumed workflow 的 normal adaptation route 默认由 AI Skills Maintainer：

1. discovery 当前 target；
2. update/adapt；
3. verify installed/loaded identity；
4. verify normal-entry/fresh-session consumption；
5. 保存 durable evidence；
6. 对五个 required consumers 逐项报告 PASS / truthful blocker。

### 8.3 Maintainer 必须消费 board closure

machine-update orchestration 是 maintenance-board machine-adaptation semantics 的 downstream consumer。

它 production-ready 后完成某个 required consumer adaptation 时：

- 如果自身有 Project mutation能力：
  - 直接更新对应 tracking Issue evidence；
  - 更新 consumer checklist；
  - 仅在五个 required consumers 全部完成时完成 approved Project closure；
- 如果没有 Project mutation能力：
  - 输出 exact completion mutation；
  - 当前调用方或下一 Project-capable Executor 必须自动消费；
  - 不得只打印“server/local PASS”然后把 Kanban 留给用户手工更新。

本 board task 不顺手修改 machine-update production source。它只规定后续该独立 capability 在 release/implementation closure 前必须消费 canonical board contract。

## 9. 五 consumer closure 的 tracking Issue 表达

不新增 Project 字段。

进入 ADAPTING 后，Issue 顶部继续保持：

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

详细 adaptation section 记录：

```text
Required consumers:
- Longleaf_Codex: PENDING | PASS | N/A(frozen reason)
- Longleaf_Backup_Codex: PENDING | PASS | N/A(frozen reason)
- CUHK_Workstation_WSL_Codex: PENDING | PASS | N/A(frozen reason)
- Workstation: PENDING | PASS | N/A(frozen reason)
- Legion: PENDING | PASS | N/A(frozen reason)
```

这些是 Issue reader-facing evidence，不是新 machine schema/state machine。

每一行必须链接 durable evidence locator。

## 10. Planner / Critic / Codex / Maintainer 的完整 steady-state handoff

```text
真实项目 thread
-> raw NEW 写 canonical inbox
-> 若属于 tracking scope，GPT按 Project instructions消费 board contract
-> Project TODO
-> Planner first substantive round
-> DOING
-> execution package Critic PASS（仍 DOING）
-> Codex implementation
-> independent Critic/Reviewer implementation PASS
-> canonical integration/release closure
-> central implementation complete
-> machine-consumed workflow: ADAPTING
-> AI Skills Maintainer适配五个 required consumers
-> 五 consumer normal-entry PASS
-> Resolution commit + completed close
-> DONE
```

如果当前 GPT surface 没有 Project mutation：

- GPT 仍负责 lifecycle truth；
- 更新自己能写的 tracking Issue evidence；
- 生成 exact pending mutation；
- 下一 Project-capable Codex/Maintainer消费；
- 不让用户拖卡。

## 11. Clear Writing contract 保持不变

Codex 创建/修改：

- Issue title；
- top summary；
- board copy；
- backfill reader-facing text；
- adaptation/closure reader-facing text；

必须实际调用 Clear Writing（`writing-style`）做最终表达层处理。

Clear Writing 不得改动：

- maturity；
- lifecycle truth；
- five-consumer completion truth；
- exact locators；
- Resolution commit；
- evidence strength。

实际 Project surface qualitative review仍是最终质量依据。

## 12. 外部现实核查与采用结论

本轮针对 BOARD-CONSUMER-01 独立核查了 OpenAI 官方当前文档：

### ChatGPT Projects

官方帮助中心说明：

- Projects 将 chats、files、instructions 组合为同一项目上下文；
- Project instructions 在 `Project settings` 添加；
- Project instructions 只在该 Project 内生效并应用于该 Project conversations。

采用：

> ChatGPT Project instructions 是 GPT normal-entry locator 的正确位置；repo AGENTS 不能替代它。

来源：
https://help.openai.com/en/articles/10169521-projects-in-chatgpt

### Codex AGENTS

OpenAI 当前 Codex guidance 说明 Codex CLI 自动枚举并注入适用的 `AGENTS.md`。

采用：

> AI_Skills `AGENTS.md` 是 Codex normal-entry locator 的正确位置。

来源：
https://developers.openai.com/api/docs/guides/latest-model

没有证据支持为了同步这两个入口而新增 watcher/controller/service。

## 13. Alternatives

### A. 只改 canonical board doc

拒绝。普通 ChatGPT Project thread不保证自动读取 repo policy，BOARD-CONSUMER-01 会复发。

### B. 把整份 board policy复制到 ChatGPT Project instructions、AGENTS、Planner/Critic contracts

拒绝。会形成四份漂移 policy。

### C. canonical board doc + 四个轻量 consumer locators

采用：

- ChatGPT Project instructions；
- AI_Skills AGENTS；
- Planner Role Contract；
- Critic Role Contract；

再由 future AI Skills Maintainer 作为 machine-adaptation downstream consumer。

### D. 让用户每次提醒“记得更新 Kanban”

拒绝。违背本任务核心目标。

### E. 后台 watcher持续扫 repo

拒绝。现有 GPT/Planner/Critic/Executor handoff 已有足够事件点，不新增控制平面。

## 14. v4 对 execution package 的后续影响

v4 PASS 后，当前 v0.2 execution package **仍不可直接执行**。

Planner 必须生成完整 v0.3 Plan / Goal / Kickoff，至少加入：

1. full-inbox coverage；
2. raw NEW tracking semantics；
3. ChatGPT Project instructions exact one-time setup；
4. AGENTS locator；
5. Planner/Critic role-contract locators；
6. five required consumer semantics；
7. central implementation complete -> ADAPTING cutover；
8. AI Skills Maintainer downstream consumer contract；
9. TODO_COVERAGE evidence；
10.五 consumer adaptation evidence / final DONE validation；
11. BOARD-UX / BOARD-SYNC / Clear Writing / BOARD-01 所有既有要求。

execution v0.3 仍必须独立 Critic review 后才能交 Codex。

## 15. Non-goals

本设计轮不：

- 修改 ChatGPT Project settings；
- 修改 AGENTS / Planner / Critic contracts；
- 创建 Project / Issue；
- backfill；
- 修改 plugin source；
- 修改 AI Skills Maintainer source；
- 安装/适配五台机器；
- 修改 Bridge Kit；
- 调用 paid API；
- 新增自动化；
- 改版本。

## 16. BOARD-CONSUMER-01 disposition

```text
BOARD-CONSUMER-01 = ACCEPT
```

关闭方式：

- GPT normal entry -> ChatGPT Project instructions locator；
- Codex normal entry -> AI_Skills AGENTS locator；
- Planner formal round -> Planner contract locator；
- Critic formal review -> Critic contract locator；
- machine adaptation -> future production-ready AI Skills Maintainer downstream consumer；
- canonical policy -> only docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md；
- Project settings 若当前只能人工修改 -> v0.3 一次性 HUMAN_ONLY exact text，不重复询问；
- no controller/watcher/Action/database/registry/ledger/state machine。

## 17. 当前 blocker 状况

Planner 没有发现新的直接证据支持新增 blocker。

```text
BOARD-CONSUMER-01 = ACCEPTED_AND_REVISED
NEW_BLOCKERS_FOUND_BY_PLANNER = NONE
NEXT_HANDOFF = CRITIC
```
