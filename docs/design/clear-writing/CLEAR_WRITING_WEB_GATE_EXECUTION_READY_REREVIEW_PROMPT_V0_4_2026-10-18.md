# Clear Writing Web Gate execution package v0.4 — execution-ready re-review prompt

你现在担任 Clear Writing Web Gate execution package v0.4 的独立 execution-ready Critic。

本轮只复核两个剩余 blocker：

- `CW-WEB-ER-01`
- `CW-WEB-ER-05`

以下已经关闭，不得重开：

- `CW-WEB-ER-02`
- `CW-WEB-ER-03`
- `CW-WEB-ER-04`

也不得重开：

- invocation-policy proposal v0.2；
- 六技能架构；
- frozen production candidate；
- W0/W1/W2/W3 主设计；
- W2 4/7 scoring；
- one-answer / infrastructure-only retry；
- privacy；
- raw evidence；
- G7 boundary。

## Active Review Context

- target_repo:
  `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain:
  `writing-style / Clear Writing`
- design_topic_or_task_key:
  `clear-writing--every-response-invocation-policy`
- source/evidence branch:
  `reviewed/clear-writing--scientific-explanation-readability-repair`
- approved invocation-policy proposal:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md`
- approved proposal commit:
  `1f905d294c3c2e5b0951c9d5e818c285d236cef7`
- proposal Critic PASS commit:
  `50e09a2dc68a097ef21e0cf245f7951eb9d06f89`
- prior Web Gate package v0.3:
  `870e5c1766549b27819c14fbd8109c7ad9484bf6`
- v0.3 execution-ready Critic review:
  `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_EXECUTION_READY_CRITIC_REVIEW_V0_3_2026-10-18.md@e33b42169aeade563ebb360e16d6380729a8b902`
- frozen production candidate:
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`

先读取 latest main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

然后读取 Bridge Kit latest main 中与以下内容直接相关的当前实现：

- state graph；
- `NEEDS_GPT_PLANNER` / `AWAIT_HUMAN_DECISION`；
- Planner-decision terminal route；
- watcher eligible states；
- watcher status / stop；
- terminal-state FINAL_REPORT requirement。

然后完整读取 v0.4 package：

- `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_EXECUTION_PLAN_V0_4_2026-10-18.md`
- `docs/goals/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_WEB_GATE_GOAL_V0_4_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_4_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_W2_MATCHED_ENVIRONMENT_PREFLIGHT_V0_4_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_WEB_TEST_CANDIDATE_MATERIALIZATION_V0_3_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_W2_REVEAL_MAP_V0_3_2026-10-18.json`
- `docs/design/clear-writing/CLEAR_WRITING_W2_BLIND_REVIEW_CONTEXT_V0_4_2026-10-18.md`
- `docs/operations/prompts/CLEAR_WRITING_W2_BLIND_REVIEW_PROMPT_V0_4_2026-10-18.md`
- `docs/operations/prompts/CLEAR_WRITING_WEB_GATE_FINAL_REVIEW_PROMPT_V0_4_2026-10-18.md`
- `docs/operations/prompts/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_WEB_GATE_KICKOFF_V0_4_2026-10-18.md`
- `automation/reviewed_handoff/tasks/clear-writing--every-response-invocation-policy/CURRENT.json`
- `results/clear-writing--every-response-invocation-policy/FINAL_REPORT.md`

不要执行任何 live action。

# CW-WEB-ER-01 — manual Web transport 与耗尽 machine state 解耦

v0.3 的问题是：

`CURRENT.state=NEEDS_GPT_PLANNER`
且
`plan_revision=1 / max_plan_revisions=1`

因此真实 Bridge 拒绝再次
`NEEDS_GPT_PLANNER -> PLAN_FROZEN`。

v0.4 不再尝试 re-arm。

请核对当前 machine state 是否已经通过 existing Bridge 合法 Planner-decision terminal route 进入：

```text
CURRENT.state=AWAIT_HUMAN_DECISION
human_gate_reason=PLANNER_DECISION
plan_revision=1
max_plan_revisions=1
```

并确认：

1. task-local `FINAL_REPORT.md` 已存在；
2. 该 transition 不重置 revision budget；
3. 没有 raw edit state graph；
4. 没有新增 state/schema；
5. 没有修改 Bridge Kit；
6. `AWAIT_HUMAN_DECISION` 不在 watcher eligible states；
7. v0.4 明确不使用 Reviewed Handoff CURRENT / watcher / Codex Executor 作为 Web experiment transport；
8. execution-ready PASS + 用户 approved Kickoff 前仍然零 live Web execution；
9. Kickoff 后的 manual Web run 只依赖冻结 package + user authorization + watcher inactivity proof + W2 preflight PASS；
10. CURRENT 在 manual Web batch 中保持 terminal state，不再 re-arm；
11. Web evidence 完成后使用冻结的 manual final-review prompt 交独立 Critic，而不是伪造 REVIEW_1.md / review_round / CURRENT transition。

重点判断：

这是否属于“使用 current Bridge 合法 terminal path 终止耗尽的 machine workflow，再把 manual Web evaluation 与其解耦”，而不是跳过 state graph。

如果成立：

`CW-WEB-ER-01=CLOSED`

如果不成立，只指出真实不可执行/越权部分，不要要求修改 Bridge Kit 或重开 workflow 架构。

# CW-WEB-ER-05 — blind Reviewer 真实上下文隔离

v0.3 的 opaque mapping 与 blind packet 字段已经通过，本轮不要重审它们本身。

v0.4 新增：

`docs/design/clear-writing/CLEAR_WRITING_W2_BLIND_REVIEW_CONTEXT_V0_4_2026-10-18.md`

以及：

`docs/operations/prompts/CLEAR_WRITING_W2_BLIND_REVIEW_PROMPT_V0_4_2026-10-18.md`

请确认 blind preference Reviewer 必须运行在真正隔离的新 context：

优先：

- 新空白 Project：
  `CW-W2-BLIND-v04`
- project-only memory；
- zero prior task chats；
- zero Project files；
- zero Project knowledge/repo source；
- 不进入当前 AI Research Stack Project；
- 不访问 `YuukiAS/AI_Skills_Collection`；
- 不使用 GitHub、Files、Plugin Creator、Plugin Management、web、connected apps/source；
- 只接收 sanitized blind packet；
- 在第一条 blind Reviewer 输出前记录 context identity / isolation mode / zero-context evidence / blind packet hash / blind prompt hash。

确认：

1. “fresh thread in current AI Research Stack Project” 已被明确禁止；
2. project-only memory 不再被当成单独充分条件，而必须搭配新且空白 Project；
3. blind Reviewer 在 verdict freeze 前真实不可达 reveal map/repo/current Project history；
4. 若 isolation 无法证明，W2不能 PASS；
5. 任何 blind Reviewer tool/source access 都会使盲评 invalid，而不是重跑到有利结果；
6. P01-P08 verdict + reason 先完整冻结到 evidence，并记录 hash；
7. verdict freeze 后才允许 execution operator使用 reveal map；
8. blind Reviewer 本身无需读取 reveal map；
9. execution-ready Critic 因为看过 reveal map，仍被明确排除为后续 blind Reviewer；
10. reveal map 继续留在 repo 是可接受的，因为 blind Reviewer 的实际 context/tool boundary 让该 repo 在 reveal 前不可达。

如果成立：

`CW-WEB-ER-05=CLOSED`

# Change-impact check

只确认本 v0.4 没破坏此前已关闭/已接受内容：

- `CW-WEB-ER-02/03/04` 不变；
- W2 preflight仍在所有 live mutation 前；
- candidate exact materialization/parity不变；
- frozen contracts execution-ready PASS 后只读；
- W2 INCONCLUSIVE停止；
- W3不能 rescue W2；
- W2 4/7 scoring未改；
- one-answer / infra-only retry未改；
- privacy/raw evidence未改；
- G7仍禁止；
- production candidate与六技能不变；
- PIE/Mica/Research Authoring/Presentations仍 out of scope；
- 当前没有执行 Web Gate；
- 当前没有创建 test candidate；
- 当前没有修改真实 Project setting、global custom instructions 或 plugin state。

# 输出

给 `PASS` 或 `REVISE`。

若 `REVISE`：

- 只列 `CW-WEB-ER-01` / `CW-WEB-ER-05` 尚未关闭，或这两项返修直接引入的 execution-readiness blocker；
- 使用稳定 finding ID；
- 不重开 invocation-policy、六技能、production candidate；
- 不执行 Web Gate；
- 自动给 Planner 一段最小返修 prompt。

若 `PASS`，必须输出：

```text
DECISION=PASS
CLOSED_FINDINGS=CW-WEB-ER-01,CW-WEB-ER-05
READY_FOR_WEB_GATE=YES
NEXT_HANDOFF=PLANNER
```

并列出批准对象：

- `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_EXECUTION_PLAN_V0_4_2026-10-18.md`
- `docs/goals/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_WEB_GATE_GOAL_V0_4_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_4_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_W2_MATCHED_ENVIRONMENT_PREFLIGHT_V0_4_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_WEB_TEST_CANDIDATE_MATERIALIZATION_V0_3_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_W2_REVEAL_MAP_V0_3_2026-10-18.json`
- `docs/design/clear-writing/CLEAR_WRITING_W2_BLIND_REVIEW_CONTEXT_V0_4_2026-10-18.md`
- `docs/operations/prompts/CLEAR_WRITING_W2_BLIND_REVIEW_PROMPT_V0_4_2026-10-18.md`
- `docs/operations/prompts/CLEAR_WRITING_WEB_GATE_FINAL_REVIEW_PROMPT_V0_4_2026-10-18.md`
- `docs/operations/prompts/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_WEB_GATE_KICKOFF_V0_4_2026-10-18.md`

并明确本 PASS 只批准 Web Gate execution package v0.4，不代表：

- watcher inactivity proof 已完成；
- W2 preflight 已 PASS；
- test candidate 已创建；
- Project 已创建/修改；
- W0/W1/W2/W3 已执行或 PASS；
- G7 已执行；
- release 已完成。

最后逐字附上 approved v0.4 Kickoff，供用户复制回长期 Planner thread。

Critic 不修改 CURRENT、repo production、Project setting、账号或任何 plugin，也不执行 Gate。
