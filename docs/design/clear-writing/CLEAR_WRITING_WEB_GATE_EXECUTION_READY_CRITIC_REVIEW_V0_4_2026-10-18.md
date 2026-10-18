# Clear Writing Web Gate execution package v0.4 — 独立 execution-ready Critic Review

日期：2026-10-19  
审查阶段：execution package v0.4 re-review after execution-ready REVISE  
审查对象：`clear-writing--every-response-invocation-policy`  
Package commit：`2d30f940aee60e9e70ce8c5e8e49c5ff8876c2ca`  
Approved invocation-policy proposal：`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md@1f905d294c3c2e5b0951c9d5e818c285d236cef7`  
Proposal Critic PASS：`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_CRITIC_REVIEW_V0_2_2026-10-18.md@50e09a2dc68a097ef21e0cf245f7951eb9d06f89`  
Frozen production candidate：`fd7a1578a5042a46a55c5b638f6d550655b1096b`  
Bridge Kit checked：`YuukiAS/GPT_Codex_AI_Bridge_Kit@35a976e79c036f6e68ba70e9d2364abc1c274a45`

## Decision

**PASS / READY_FOR_WEB_GATE=YES**

本轮只复核两个剩余 blocker：

- `CW-WEB-ER-01 = CLOSED`
- `CW-WEB-ER-05 = CLOSED`

此前已经关闭的 `CW-WEB-ER-02/03/04` 未重新打开；invocation-policy proposal v0.2、六技能架构、production candidate、W0/W1/W2/W3 主设计、W2 4/7 scoring、one-answer / infrastructure-only retry、privacy、raw evidence 与 G7 boundary 均保持不变。

## CW-WEB-ER-01 — CLOSED

### Bridge state graph 与 terminal route

当前 Bridge Kit 实现明确允许：

`NEEDS_GPT_PLANNER -> AWAIT_HUMAN_DECISION`

并在该 transition 上自动设置：

`human_gate_reason=PLANNER_DECISION`

`AWAIT_HUMAN_DECISION` 属于 Bridge `TERMINAL_STATES`，且不在 watcher 的 eligible states；watcher 只消费 `PLAN_FROZEN` 与 `REVISE`。

Bridge 对 terminal transition 还要求 `FINAL_REPORT.md` 先通过严格结构校验。

### Durable repository evidence

Git 历史满足该合法顺序：

1. `3e4ff53d0754fe15008e5dc6364d6876d2f06cf0` 只新增 task-local `FINAL_REPORT.md`；
2. `2798fc5e26fea81634ebf1151354ccc7576035a0` 随后只将 `CURRENT.json` 从：
   - `state=NEEDS_GPT_PLANNER`
   - `plan_revision=1`
   - `max_plan_revisions=1`
   
   转为：
   - `state=AWAIT_HUMAN_DECISION`
   - `human_gate_reason=PLANNER_DECISION`
   - revision budget 保持 `1/1`
   - `review_round=0`、`last_review_decision=null` 保持不变。

最终 `CURRENT.json` 与当前 Bridge 的 Planner-decision terminal semantics 完全一致。

没有 production、Bridge state graph/schema、revision budget 或 Reviewer history 被修改；没有伪造 `REVIEW_1.md`。

因此 exhausted Reviewed Handoff machine transport 已合法终止，manual Web evaluation 可以作为另一个用户授权的执行表面独立运行，而不声称自己是 Reviewed Handoff Executor event。

### Manual transport boundary

v0.4 明确冻结：

- execution-ready Critic PASS + 用户发送 approved Kickoff 前零 live Web execution；
- live mutation 前仍必须证明 exact target/branch watcher inactive；
- manual Web batch 不 re-arm `CURRENT`；
- 不启动 watcher/Codex 执行 Web Gate；
- `CURRENT` 在整个 manual batch 保持 terminal state；
- Web evidence 完成后使用预冻结 final-review prompt 手工交独立 Critic；
- 不创建 `REVIEW_1.md`，不增加 `review_round`，不伪造 machine review transition。

因此 `CW-WEB-ER-01` 已关闭。

## CW-WEB-ER-05 — CLOSED

### Project-memory isolation

OpenAI 当前 Projects 文档明确说明 project-only memory 下：

- saved memories 不会被该 Project 引用；
- Project chat 可以引用同 Project 内其他 conversations；
- Project chat 不能引用 Project 外 conversations；
- Project 外 chats 也不能引用该 Project conversations。

因此上一轮“fresh thread in current AI Research Stack Project 不足”的判断仍成立，而 v0.4 已正确增加“new + empty Project/context”条件。

### Frozen blind-review context

v0.4 要求初始 W2 preference Reviewer 使用：

- 新空白 Project `CW-W2-BLIND-v04`；
- project-only memory；
- zero prior task chats；
- zero Project files；
- zero Project knowledge/source；
- 不属于当前 AI Research Stack Project；
- 不访问 `YuukiAS/AI_Skills_Collection`；
- 不使用 GitHub、Files、Plugin Creator、Plugin Management、web 或 connected apps/sources；
- 只接收 frozen blind prompt + sanitized blind packet。

在第一条盲评输出之前还必须记录：

- sanitized blind context identity；
- surface/model/effort；
- isolation mode；
- zero prior chats/files/knowledge；
- blind packet hash；
- blind prompt hash。

任何 required isolation 无法证明，则 W2 不能 PASS。

### Tool/source fail-closed

盲评完成前任何被禁止的 tool/connector/source access 都直接使 blind review invalid；不得重跑到 favorable result。

这解决了 reveal map 仍保存在 repository 的问题：blind Reviewer 的真实 context/tool boundary 使 repository 在 verdict freeze 前不可达。只要 execution evidence 证明这一 boundary 成立，repo 内保存 reveal map 不破坏 blindness。

### Verdict freeze / reveal order

P01-P08 verdict + reason 必须先完整写入：

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/W2/blind/BLIND_VERDICTS_FROZEN.md`

并先记录 hash。只有随后 execution operator 才能读取/use reveal map；blind Reviewer 本身无需 reveal。

execution-ready Critic 因已读取 reveal map，已被永久排除为后续 blind Reviewer。

因此 `CW-WEB-ER-05` 已关闭。

## Change-impact check

v0.4 未破坏已接受内容：

- `CW-WEB-ER-02/03/04` 继续关闭；
- W2 preflight 仍发生在所有 live mutation 之前；
- exact candidate materialization/parity 不变；
- frozen contracts execution-ready PASS 后继续 read-only；
- W2 INCONCLUSIVE 立即停止，W3 不 rescue；
- W2 4/7 scoring 未变；
- one-answer / infra-only retry 未变；
- privacy/raw evidence 未弱化；
- G7 继续禁止；
- production candidate / 六技能不变；
- PIE、Mica、Research Authoring、Presentations 仍 out of scope。

当前 package 本身没有执行 watcher mutation、W2 preflight、candidate creation、Project creation/edit、W0/W1/W2/W3/G7，也没有修改真实 Project setting、global custom instructions 或 plugin state。

## Claim boundary

本 PASS **只批准 Clear Writing Web Gate execution package v0.4**。

它不代表：

- watcher inactivity proof 已完成；
- W2 matched environment 已存在或 preflight 已 PASS；
- test candidate 已创建；
- Project 已创建或修改；
- W0/W1/W2/W3 已执行或 PASS；
- G7 已执行；
- user acceptance 已完成；
- release 已完成。

下一入口是 Planner/manual Web execution thread，且只有用户实际发送 approved v0.4 Kickoff 后才获得本 package 内冻结的 test-only live authorization。
