# AI Skills 维护看板与完成语义 — Critic Review v3

- 日期：2026-09-24
- Review stage：`DESIGN_AMENDMENT_REVIEW`
- Result：`REVISE`
- target_repo：`YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain：repository maintenance / plugin refinement workflow
- design_topic_or_task_key：`repo--maintenance-board-lifecycle`
- human label：AI Skills 维护看板与完成语义
- source branch/ref：`main`
- reviewed proposal：`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_PROPOSAL_2026-09-24.md` v3
- reviewed proposal commit：`fa40e081e9d30b17d94df7c81a274ad75e5e297b`
- execution branch/worktree：NONE

## 1. 结论

两个 amendment 的业务语义本身都成立：

1. 第一次 bootstrap 应覆盖当前全部 canonical TODO inbox，但必须先 dedupe/disposition，不能机械“一条 heading 一张 Issue”；
2. 对 machine-consumed workflow/shared mechanism，central source/release/main integration 不能单独 DONE，默认要等 current canonical server + current canonical local-machine consumer 都完成真实 adaptation 与 normal-entry consumption 后才 DONE。

raw `NEW` 可以进入 Project 成为 `Status=TODO`，而 source maturity 继续保持 `NEW`。只要明确 `Project lifecycle != plugin TODO maturity`，这不会自动把它 promotion 成 `CANDIDATE_GENERIC/PROMOTE_NOW`。

`TODO_COVERAGE.md` 作为一次性 bootstrap evidence 也合理：它证明“所有当前 inbox 条目都被看过并有 disposition”，但不承担长期状态源，不是 registry/schema。

AI Skills Maintainer 的表述也诚实。当前 machine-update Goal 仍是 `PLANNER_DRAFT_FOR_CRITIC`，当前 `ai-skills-repository-maintainer` skill 也没有已发布的 machine-update orchestration；因此 v3 正确地规定“未来 production-ready 后作为 normal adaptation entry，未 ready 时保持 ADAPTING”。

但 v3 还缺一个直接决定“以后 GPT 会不会真的自动维护”的消费路径。用户已经明确说：普通项目 thread 说“推送 TODO”、Planner 第一次出计划、Critic review、Codex/Maintainer adaptation 后，都不应再靠用户手动提醒。仅在 repo policy 里写“GPT 是 semantic owner”并不足以保证 ChatGPT Project 内任意 thread 都会消费这条规则。

因此本轮只有一个 stable blocker：`BOARD-CONSUMER-01`。

## 2. Amendment A 复核

### 2.1 推荐方案

三种方案中，v3 的第三种最好：

```text
full inbox coverage
-> dedupe / disposition
-> still-active central raw NEW can become Project TODO
-> source maturity remains unchanged
```

“promoted 才上板”会继续隐藏真实 backlog；“每个 heading 机械 1:1 Issue”会把 duplicate、project-local、历史项全部复制成第二个垃圾山。

v3 通过 top-level idea grouping、Area ownership、duplicate merge、ambiguous merge fail-safe 和 Clear Writing，已经给出足够的防噪音边界。

### 2.2 raw NEW 不等于 promotion

`Project Status=TODO` 只回答“是否存在于当前 backlog / lifecycle”，而 source `status: NEW` 继续回答 maturity/genericity。

这两个维度分开是正确的。当前不需要再加 `Maturity` Project 字段；Issue 顶部/来源 locator 保留 source maturity 即可。

### 2.3 TODO_COVERAGE.md

保留。

它是一轮 bootstrap 的 completeness evidence：

```text
source inbox + heading
-> disposition
-> tracking Issue (if any)
-> Area
-> initial lifecycle Status
```

它不作为后续状态更新入口，不要求长期同步，也不影响 TODO/Project 的 source-of-truth 分工，因此没有形成新 registry/ledger。

## 3. Amendment B 复核

### 3.1 双环境 closure 的适用范围合理

默认 server + local 双环境只应用于 machine-consumed workflow/shared maintenance mechanism，不自动套到普通 domain plugin、纯文档、纯审计或单一 artifact improvement。

这个 scope 足够窄，能关闭“central main 已经更新但实际机器仍运行旧行为”的假 DONE，又不会让 presentations / research-writing 等普通改进被迫在两台机器安装验证。

### 3.2 exact consumer 在 ADAPTING 时绑定合理

policy 不硬编码 host/path 是正确的。

进入 `ADAPTING` 时，tracking Issue 必须把：

- current canonical server consumer
- current canonical local-machine consumer

解析成当时真实 identity/locator，然后该 item 的 completion contract 以这两个 exact consumer 为准。后续新增 optional machine 不应追溯扩大旧 DONE；除非新证据证明旧 claim 本来就不成立。

这避免了长期 policy 中的 stale host/path，又保留了可验收性。

### 3.3 AI Skills Maintainer 没有被冒充成当前能力

当前 repo 的：

- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`
- `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md`

仍是独立设计/Goal；Goal 状态是 `PLANNER_DRAFT_FOR_CRITIC`。

当前 `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md` 主要负责 central repository/plugin maintenance，并没有已经发布的 machine-update orchestrator。

所以 v3 的 fail-closed 语义正确：

- capability production-ready -> Maintainer 可作为 normal adaptation entry；
- 尚未 ready -> workflow item 保持 ADAPTING，anchor 指向该 blocker / approved alternative owner；
- board task 不顺手实现 machine-update source。

## 4. 状态切换时点的明确解释

用户当前补充的 steady-state 意图应按下面理解：

1. 用户/真实项目 thread 新增 plugin TODO：
   - raw NEW 进入 inbox；
   - 若属于当前 central backlog tracking scope，GPT 自动绑定/创建 Project TODO，而不是等 promotion。
2. Planner 第一次开始实质 Plan/设计：
   - item -> DOING。
3. Critic 的 **execution-ready PASS 本身** 不能直接把 item 变成 ADAPTING，因为此时 central implementation 还没发生。
4. 只有 central implementation / canonical integration 已真实完成并经过相应 implementation review，且剩余工作确实只是 required machine consumers：
   - item -> ADAPTING。
5. server + local exact consumers 都完成 adaptation + installed/loaded identity + fresh-session/normal-entry consumption：
   - 才允许 DONE。

如果用户所说“Critic 对完整通过的 execution package 实现没问题”是指 **实现已经完成、implementation review 通过且 central core 已落地**，那么进入 ADAPTING 正确；如果只是 Plan/Goal/Kickoff 的 pre-execution Critic PASS，则仍应保持 DOING。

## 5. Stable blocker

### BOARD-CONSUMER-01 — GPT 自动维护语义缺少跨入口的真实消费绑定

**用户要求**

用户明确要求：

- 以后任意项目 thread 说“推送 TODO 到某插件”时，不需要再提醒看板；
- 第一次 Planner 出实质 Plan 时自动 DOING；
- Critic / Planner 自动维护 current anchor、review locator、next action 和 lifecycle truth；
- machine adaptation 完成后自动完成 closure；
- 用户不承担手工拖卡/提醒同步。

用户还明确指出：当前 GPT Project 设置、Codex 的 AGENTS、AI Skills Maintainer 等实际消费面可能需要调整。

**直接证据**

v3 §5 已经正确声明 GPT/Planner/Critic 是 semantic owner，但没有冻结这些规则究竟由哪些 normal-entry source 保证消费。

当前实际产品有两个不同入口：

1. **ChatGPT Project threads**
   - ChatGPT Project instructions 会应用于该 Project 内的 chats；
   - repo 的 `AGENTS.md` 并不会自动成为所有 ChatGPT Project thread 的系统级 instruction。
2. **Codex repo sessions**
   - Codex 会自动枚举并注入适用的 `AGENTS.md`。

当前 AI Research Stack Project instructions 还没有 maintenance-board 的稳定 trigger/locator；而当前 `ai-skills-repository-maintainer` 也没有已发布的 machine-update/board-closure能力。

因此只在未来 repo canonical board doc / AGENTS 中写规则，不能证明“任意 GPT 项目 thread 会自动同步”。这会直接复现用户不想要的行为：GPT 把 TODO 写进 repo，但看板仍不动，直到用户再次提醒。

**外部现实依据**

OpenAI 当前官方文档说明：

- ChatGPT Project instructions 只在该 Project 内生效，并应用于项目对话；
- Codex CLI 会自动发现并把适用的 `AGENTS.md` 注入模型上下文。

这说明 ChatGPT Project 与 Codex 的正常入口是两个不同 instruction surface，不能假设改一个 repo AGENTS 就自动覆盖另一个。

**因果风险**

如果不补 consumer binding，v3 的“GPT semantic owner”只是设计宣言，不是 normal-entry behavior。

最典型失败路径：

```text
用户在普通 AI Research Stack thread：
“把这个问题推送到 presentations TODO”
-> GPT 修改 docs/plugin-todos/presentations.md
-> 当前 thread 没消费 board contract
-> tracking Issue / Project Status 不更新
-> 用户以后仍要手工提醒
```

这正好违背 BOARD-SYNC-01 和用户当前新增要求。

**最小关闭条件**

Planner v4 / amendment revision 只需增加一个很小的“consumer adaptation contract”，不要新增 controller/watcher：

1. **ChatGPT Project instructions**
   - 当前 AI Research Stack Project instructions 必须增加一条短、稳定的 board trigger/locator：
     - 当用户要求向 AI_Skills plugin/skill TODO 记录问题时，自动读取/遵循 canonical maintenance-board contract；
     - 当当前 thread 是该 tracking idea 的 Planner/Critic 时，自动 reconcile lifecycle truth / anchor / next action；
     - 如果当前 ChatGPT surface 没有 Project mutation 能力，输出 exact pending Project mutation 给下一 Project-capable Executor/Maintainer，不让用户手工拖卡。
   - 不把完整 board policy复制进 Project instructions，只放 trigger + canonical locator/语义摘要。

2. **Codex repo sessions**
   - AI_Skills `AGENTS.md` 保留/新增短 locator，确保 Codex 在 repo normal entry 自动消费 canonical board doc；
   - no full-policy duplication。

3. **Planner / Critic role contracts**
   - 对 formal AI_Skills maintenance round，明确把“reconcile tracking Issue/status/evidence”作为 handoff closure 的机械责任；
   - PASS/REVISE 不机械改变 status，仍以真实 lifecycle 为准。

4. **AI Skills Maintainer**
   - 本 board task 不要求现在改 machine-update source；
   - 但 machine-update orchestration 的独立 Plan/Goal 必须被标记为这个 board contract 的 downstream consumer：production-ready 后，完成 machine adaptation 时必须直接更新 board，或输出 exact completion mutation 由调用方/Project-capable executor自动消费；
   - 在该 capability 未 production-ready 前不得假装自动 DONE。

5. **一次性设置**
   - 如果修改 ChatGPT Project instructions 只能由用户在 Project settings 中完成，v0.3 execution package 应生成 exact 最小文本，作为一次性 HUMAN_ONLY setup；
   - 这不是日常维护，完成后用户不再承担每次 sync。

这五点都只解决“正常入口到底谁会读到规则”；不新增第五状态、daemon、registry、GitHub Action或新的控制平面。

## 6. 非阻塞结论

以下不形成 blocker：

- raw NEW 上板：PASS；
- full inbox coverage + dedupe/disposition：PASS；
- TODO_COVERAGE.md：PASS；
- machine-consumed workflow 默认 server + local closure：PASS；
- ADAPTING 时再绑定 exact consumers：PASS；
- Maintainer 未 ready 时保持 ADAPTING：PASS；
- future optional machine 不追溯扩大旧 DONE：PASS；
- 普通 domain/artifact improvement 不继承双环境 requirement：PASS。

## 7. 审查结论

```text
RESULT = REVISE
REVIEW_STAGE = DESIGN_AMENDMENT_REVIEW
REVIEW_OBJECT = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V3_PROPOSAL_2026-09-24.md
REVIEWED_PROPOSAL_COMMIT = fa40e081e9d30b17d94df7c81a274ad75e5e297b
STABLE_BLOCKERS = BOARD-CONSUMER-01
```

本轮没有重新打开 v2 已通过的四状态、BOARD-01、BOARD-UX-01、BOARD-SYNC-01 或 Clear Writing requirement。

只需要把“GPT/Codex/Maintainer 到底从哪个 normal-entry source 自动消费这套 board contract”补清楚；其余两个用户 amendment 均可保留。
