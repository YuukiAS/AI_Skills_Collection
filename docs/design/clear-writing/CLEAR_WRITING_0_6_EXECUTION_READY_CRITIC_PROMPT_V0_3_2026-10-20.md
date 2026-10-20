# Clear Writing 0.6 revised execution-ready review — Critic prompt v0.3

你继续担任本任务的**原独立 Critic**。这是同一 Clear Writing 0.6 task 的正式语义修订，不是新版本、新任务或大规模架构研究。

用户发送本 prompt 时会同时给出一个 exact `PACKAGE_COMMIT`。从该 exact commit 审查，不从 mutable branch head猜。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = writing-style / Clear Writing
design_topic_or_task_key = clear-writing--single-entry-artifact-finalization
source_branch_or_ref = design/clear-writing--single-entry-artifact-finalization
tracking_issue = YuukiAS/AI_Skills_Collection#13
review_stage = REVISED_EXECUTION_READY_REVIEW_V0_3
previous_approved_proposal = 3eefc626b86566113125a06fc6046a2bec1eafb2
previous_execution_ready_package = d7b810d194ead881303aaca9c2e4f1d59a97c1f1
historical_candidate = 079bd7987bb33d624d244feb415327d5cf2343d8
new_regression_intake = results/clear-writing--single-entry-artifact-finalization/CHAT_RESPONSE_CONTENT_SELECTION_PLANNER_INTAKE_2026-10-20.md@2b4d74bd5acfafbb4473f669d80a3a48cd53b8c5
```

## 1. 必读来源

先实际读取最新 `main`：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/plugin-todos/writing-style.md`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`

然后从用户给出的 exact `PACKAGE_COMMIT` 读取：

1. `docs/design/clear-writing/CLEAR_WRITING_0_6_CHAT_RESPONSE_CONTENT_SELECTION_PROPOSAL_V0_2_2026-10-20.md`
2. `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_3_2026-10-20.md`
3. `docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_3_2026-10-20.md`
4. `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_3_2026-10-20.md`
5. `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_3_2026-10-20.md`
6. `results/clear-writing--single-entry-artifact-finalization/PLANNER_REVISION_STATUS_2026-10-20.json`

并重新读取：

- old wrapper `packaging/chatgpt/writing-style/clear-writing/SKILL.md@079bd798...`
- current `skills/writing/core/response-clarity/SKILL.md`
- current `skills/writing/core/writing-fidelity/SKILL.md`
- Phase C root cause / recovery amendment
- Issue #13当前正文与最新评论。

只用OpenAI官方当前资料核实skills-only plugin边界；不得把Skill写成不可绕过send hook。

## 2. 首先判断：本次语义修订是否必要且放在正确层

独立判断：

- production regression是否已证明 `response-clarity` loaded后仍会发生；
-现有 `response-clarity` 是否已经包含结论先行、内部噪声降低、停止条件等规则；
-问题是否更像“evidence pool -> user content selection”而非单纯措辞问题；
-唯一 `clear-writing` wrapper 是否是最小、正确的 CHAT_RESPONSE content-selection owner；
-这是否与domain owner的“科研/统计 evidence selection”发生冲突。

若 Planner只是换一种说法重复 `response-clarity`，REVISE。

## 3. 比较三种路线

必须明确评价：

1. only `response-clarity`；
2. only whole-response self-check；
3. wrapper pre-route reader-value selection + existing response-clarity/fidelity。

检查Planner选择第3条是否真的更接近失败点、blast radius更小，而不是为了保留既有架构强行解释。

## 4. 检查 CHAT_RESPONSE_READER_VALUE_SELECTION_V1

必须确认它：

- 先从user prompt确定问题、reply type、detail和action；
-允许domain analysis读取全部证据；
-正文纳入使用reader-value语义条件；
-明确“详细”不是“列完所有audit”；
-明确用户点名的算法/公式/复现细节有reader value；
-`writing-fidelity`只保护selected content，不强迫展示全部background；
- whole-response check同时防噪声和防遗漏；
-无固定字数/标题/英文比例/禁词；
-不创建持久schema/ledger；
-不冒充send-time hook。

若它实际会系统性压短科研/数学/工程答案，REVISE。

## 5. 检查旧候选失效和版本关系

确认：

- `079bd798...` 被正确降为历史实现基线；
- previous execution-ready PASS不再覆盖新版semantic；
-正式Personal Plugin仍是0.5.0；
-仍是同一 `writing-style 0.6`，不是0.7；
- Issue #13继续复用；
- #73/#49 pending不被清除。

## 6. 检查 Phase C 协调

必须把两个问题分开审：

### archive compatibility

- tar.gz是真实Plugin Creator upstream格式；
- ZIP-only reader是普通实现bug；
-新版implementation把archive fix和wrapper semantic change放入同一个新candidate；
-避免两个Codex线程各自冻结candidate。

### execution owner

- archive/mutation和fresh Web gate不再被强迫在一个tool surface；
- Phase C-A mutation前必须真实materialize账户0.5 archive bytes并生成restore；
- fresh Web UI若无自动控制能力，明确user-only动作；
- user只负责UI，不负责设计prompt、判Gate、整理证据或restore；
- terminal Web failure仍能回到同一个restore owner。

若执行职责仍依赖“理论上某surface可以”，REVISE。

## 7. 检查Gate是否证明新能力而不过重

不得新增顶层Gate。

重点看G2：

- G1-B simple smoke保留；
- T1 Bridge 0.11.1为known regression；
- T9 Phase C为known regression；
- T8保留深度正控制；
- T2-T7旧route覆盖保留。

判断这是否比“继续增加十几个回归”更有针对性。

Bridge T1必须基于真实：

```text
YuukiAS/GPT_Codex_AI_Bridge_Kit
ba9013b9fbbd242e51b09f9d09291f417df17652
README.md / QUICKSTART.md / CHANGELOG.md / AGENTS.md
```

Phase C T9必须基于真实停止报告。

独立定性review必须读取exact user prompt + source + full final response。

G3/G4/G5/G6不得被降低。Bridge/Phase C不得冒充G6 fresh。

## 8. 检查实现范围是否留给Codex关键决定

若Codex还需要决定以下任一项，则REVISE：

- content-selection owner；
- reader-value inclusion semantics；
-是否修改canonical response-clarity；
- old candidate是否仍可发布；
- archive bug与wrapper change是否同candidate；
- Phase C-A/B responsibility；
- user-only Web动作；
- Gate replacement；
-版本/release语义；
- terminal failure restore。

普通措辞、代码实现细节和测试实现可以留给Codex。

## 9. 禁止事项

本轮 Critic 不得：

-修改repo/Issue/Project；
-启动Codex；
-更新Personal Plugin；
-运行G1-G6；
-创建G3 branch；
-调用付费模型；
-把旧PASS自动延续到新package。

## 10. 结论

这是新版完整 execution-ready package。若所有产品/恢复/验收/执行职责都已经冻结，可以直接给新的唯一 execution-ready：

```text
DECISION=PASS
READY_FOR_CODEX=YES
```

否则：

```text
DECISION=REVISE
READY_FOR_CODEX=NO
```

若REVISE，只阻塞真实缺口，使用稳定finding ID `CW06-R3-xx`，并附一份可直接回Planner的最小返修prompt；不要重新设计已通过的单入口/GitHub finalization架构。

若PASS，必须输出：

```text
DECISION=PASS
READY_FOR_CODEX=YES
TARGET_REPO=YuukiAS/AI_Skills_Collection
TARGET_PLUGIN=writing-style
TASK_KEY=clear-writing--single-entry-artifact-finalization
APPROVED_PACKAGE_COMMIT=<用户消息中的 exact PACKAGE_COMMIT>
APPROVED_PROPOSAL=docs/design/clear-writing/CLEAR_WRITING_0_6_CHAT_RESPONSE_CONTENT_SELECTION_PROPOSAL_V0_2_2026-10-20.md
APPROVED_PLAN=docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_3_2026-10-20.md
APPROVED_GOAL=docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_3_2026-10-20.md
APPROVED_RUNBOOK=docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_3_2026-10-20.md
APPROVED_KICKOFF_DRAFT=docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_3_2026-10-20.md
NEXT_HANDOFF=USER_AUTHORIZATION
```

并明确：PASS只批准新版implementation入口；不是implementation/Gate/release PASS，也不授权用户发送Kickoff前的任何production mutation。
