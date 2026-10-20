# Clear Writing 0.6 — execution-ready Critic 审查提示词 v0.1

你继续担任本任务的同一独立 Critic。此前你已经对 Clear Writing 0.6 Proposal 给出：

```text
DECISION=PROCEED
ROOT_CAUSE_ASSESSMENT=PARTIALLY_SUPPORTED
SINGLE_ENTRY_DECISION=ACCEPT
ARTIFACT_BINDING_DECISION=ACCEPT
GATE_MATRIX_DECISION=ACCEPT
READY_FOR_CODEX=NO
NEXT_HANDOFF=PLANNER
```

本轮不是重新做架构研究。你要判断 Planner 是否已经把接受的方向收敛成 **Codex 不需要再猜产品/平台/验收决定** 的完整 execution-ready package。

本轮只有两种最终结论：

```text
PASS
READY_FOR_CODEX=YES
```

或：

```text
REVISE
READY_FOR_CODEX=NO
```

不得用 `PROCEED` 代替最终执行前判断。

## 1. Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = writing-style / Clear Writing
design_topic_or_task_key = clear-writing--single-entry-artifact-finalization
source_branch_or_ref = design/clear-writing--single-entry-artifact-finalization
approved_proposal = docs/design/clear-writing/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_PROPOSAL_V0_1_2026-10-20.md
approved_proposal_commit = 3eefc626b86566113125a06fc6046a2bec1eafb2
tracking_issue = YuukiAS/AI_Skills_Collection#13
review_stage = EXECUTION_READY_REVIEW_V0_1
```

用户交给你本提示词时还会同时给出唯一：

```text
PACKAGE_COMMIT=<exact branch head>
```

你必须从该 exact commit 读取整个 execution-ready package。若用户给的 PACKAGE_COMMIT 与当前分支上的五份包文件不是同一提交快照，直接 REVISE，不从 mutable branch head 猜。

## 2. 先读取最新治理来源

从 `YuukiAS/AI_Skills_Collection` 最新 `main` 实际读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `TODO.md`
- `docs/plugin-todos/writing-style.md`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`

读取 Issue #13 当前正文和最新评论。

若 latest main 相比 Planner package baseline 有变化，判断变化是否会影响本执行包；不能默默使用旧规则，也不能因为无关 main 前进就机械 REVISE。

## 3. 读取批准架构和完整执行包

先从 exact：

`3eefc626b86566113125a06fc6046a2bec1eafb2`

读取 approved Proposal。

再从用户给出的 exact `PACKAGE_COMMIT` 完整读取：

1. `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_1_2026-10-20.md`
2. `docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_1_2026-10-20.md`
3. `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_1_2026-10-20.md`
4. `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_1_2026-10-20.md`
5. `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_CRITIC_PROMPT_V0_1_2026-10-20.md`

Kickoff 仍是 draft，不得执行。

## 4. 重新核实现实，不接受 Planner 自报

### 4.1 Plugin Creator

只读回查：

- `writing-style / Clear Writing 0.5.0`
- `Project Instructions Editor 0.2.8`

核实 file list、manifest、current release、scope/discoverability、顶层 Skill exposure。

重点核对 Planner 冻结的 0.5 old-file `delete_paths` 是否与当前实际 0.5.0 release 一致；若 current plugin 已 drift，package 是否正确要求 fail closed 而不是继续更新。

### 4.2 OpenAI 当前平台资料

只用 OpenAI 官方当前资料核实：

- portable root `plugin.json`；
- compatibility `.codex-plugin/plugin.json`；
- Skills 的 activation/load contract；
- skills-only plugin 与 MCP 的职责边界；
- 当前是否存在无副作用 personal-plugin dry-run / restore 能力；
- Plugin Creator update 的 overlay、expected release、delete_paths 与 version行为。

如果平台没有证明 `Interactive` 的行为语义，检查 Plan 是否只把它当“当前接受的包装值”，而没有把它写成根因或成功机制。

## 5. 不重新打开的架构决定

除非 execution package 明确违反批准 Proposal，不要重新设计：

- ChatGPT Personal Plugin 唯一顶层 `clear-writing`；
- 六项专业能力继续由 canonical source拥有；
- Codex Marketplace六项 direct exposure保留；
- wrapper只拥有 target识别、route组合、候选先于写入、readback和逐对象状态；
- 0.6 默认不新增 MCP/App/外部模型/后台服务/数据库/状态机；
- Reader Guide 是 known regression；
- normal entry 外部链失败后必须回 Planner，而不是继续堆规则。

本轮只问：实现与 Gate 决定是否已冻结、是否真实可执行、是否安全可恢复。

## 6. Execution-ready findings

### CW06-ER01 — source ownership / builder 是否真正冻结

检查：

- wrapper canonical source 是否唯一；
- `scripts/build_clear_writing_chatgpt_wrapper.py` 的 exact input/output 已冻结；
- 六项 route 是否为确定性完整投影；
- `SKILL.md -> ROUTE.md` 是否能避免额外 Skill discovery，同时保持 relative support files 可用；
- 是否禁止人工维护第二份专业正文；
- source/generated hash mismatch 是否 fail closed；
- BUILD_RECEIPT 是否只证明 parity，不冒充质量；
- Codex Marketplace六 Skill是否保持。

如果 Executor 仍可自行决定 route snapshot 形式、source owner、builder路径或第二份规则正文，REVISE。

### CW06-ER02 — Personal Plugin package / delete_paths / manifest 是否完整

检查：

- final package shape；
- dual manifest；
- Personal version `0.6.0`；
- exact delete_paths 是否覆盖当前 0.5.0 old skill tree；
- old unused asset deletion是否与新 manifest一致；
- update必须同 identity + expected_release_id；
- post-update逐文件回读；
- P0只读探针是否避免创建无法清理的临时 plugin；
- `Interactive` 是否没有被冒充因果机制。

### CW06-ER03 — external artifact claim 是否被正确收窄

必须确认正式 0.6 external-finalization claim 只覆盖：

**GitHub repository UTF-8 text files via current connected GitHub connector.**

检查 GitHub contract 是否冻结：

```text
full fetch
-> target identity/blob binding
-> full candidate + hash
-> pre-write re-fetch
-> update_file with blob SHA
-> returned commit/content SHA
-> post-write fetch
-> byte equality
-> ARTIFACT_FINALIZED
```

状态必须能区分：

- `TARGET_SOURCE_INCOMPLETE`
- `TARGET_IDENTITY_DRIFT`
- `ARTIFACT_NOT_WRITTEN`
- `ARTIFACT_FINALIZATION_UNVERIFIED`
- `ARTIFACT_FINALIZED`

不得把 Drive、本地文件、Notion 等由 GitHub Gate 推断为支持。

### CW06-ER04 — 对象级 contract 是否可执行且不过重

检查五种临时 target：

- CHAT_RESPONSE
- INLINE_DOCUMENT
- EXTERNAL_DOCUMENT
- PRODUCT_UI_COPY
- MACHINE_PAYLOAD

它们必须只是当前推理对象，不新增持久 schema/ledger。

确认：
- 多 target 独立路由/状态；
- chat PASS不能替代 document PASS；
- exact-only不污染；
- mixed只改自然语言；
- source不完整/不能写/不能回读都不能假称完成。

### CW06-ER05 — G1-G5 是否真正绑定正常入口

逐项审：

#### G1
- same Personal Plugin identity；
- exact old-path deletion；
- Plugin Creator readback；
- runtime只暴露 `clear-writing`；
- fresh Web explicit-selection smoke。

#### G2
任务必须实际覆盖：
- ordinary chat；
- Chinese formal Markdown；
- long structural Chinese technical rewrite；
- English scientific prose；
- UI copy；
- exact-only；
- mixed；
- necessary long answer；
- short answer。

Prompt 不得出现内部 Skill 名。固定 task set 是因为代表不同能力/风险，不得简单批评“数量固定”。

#### G3
必须是真实 known Reader Guide：

`YuukiAS/AI_Research_Toolkit@0ff0f43f3b04286273490e4c4870975f4aa7a7f8`

并在预定义 Gate branch 上用真实 ChatGPT Web + explicit Clear Writing + GitHub connector 完整执行 read -> candidate -> write -> readback。

helper/Codex script 不能替代。Gate branch 已存在时必须 fail closed，不覆盖。

#### G4
检查 source/final fidelity，而不是新造重复生成 task。

#### G5
检查 source/generated、Codex六项 direct exposure、profile和cross-plugin compatibility；不得把 hash parity升级成用户质量 PASS。

### CW06-ER06 — G6 是否真的 fresh 且没有留下自由选择

G6 的具体 source 不应现在暴露给 Executor，否则失去 holdout价值。

判断当前 selection protocol 是否足够冻结：

- G1-G5 PASS + final candidate immutable 后才选择；
- 由同一独立 Critic选择 exactly one；
- 有明确 eligibility；
- 在第一条模型请求前冻结 source/hash/prompt/model/plugin identity/rubric/budget；
- candidate不能再改；
- 一次产品输出；
- product FAIL 不追加样本；
- 若用于调优则永久失去 fresh身份。

如果 Critic仍能在看结果后换题，REVISE。

### CW06-ER07 — attempt budget / model / retry / stop

核对：

- ChatGPT Web；
- `GPT-5.6 Sol`；
- 每个 task one answer；
- only infrastructure-with-no-answer max one retry；
- product FAIL no retry；
- same input/plugin/model on retry；
- no winner picking；
- no rubric changes；
- any critical Gate FAIL stops downstream。

如果执行时模型不可选，必须 stop；不得静默换模型。

### CW06-ER08 — final candidate identity 与证据失效

检查 `FINAL_CANDIDATE.json` 是否足以绑定：

- exact source commit；
- central plugin version；
- personal wrapper version；
- wrapper archive hash；
- build receipt hash；
- Codex generated identity；
- profile identity；
- gate contract version。

candidate-defining source改变时，旧 Web/fresh evidence 必须失效。results/tracking-only evidence不能被误判为产品 drift。

### CW06-ER09 — Personal Plugin recovery 是否真实

当前 Plugin Creator没有直接 restore-old-release action时，Planner提出 bounded forward restore：

- 保存 0.5.0 archive/current release；
- 0.6 live Gate失败时停止 release；
- 必要时用 old behavior content + personal version `0.6.1` forward restore；
- 删除 0.6-only paths；
- readback parity；
- central 0.6不发布。

独立判断该恢复是否真实、是否比“留下坏 0.6.0”更安全。若当前 tool/version规则不支持，应 REVISE；不得假装有 rollback API。

### CW06-ER10 — version / release / Issue #13

核对：

```text
writing-style 0.5 -> 0.6 exactly once on successful release path
Personal Plugin 0.5.0 -> 0.6.0
repository eventual PATCH, late-bound from current origin/release
other central plugins NO_BUMP
maturity NO CHANGE
```

Gates失败时不得发布 central 0.6。

Issue #13 必须复用且保持 open；新设计轮次为 DOING；成功 0.6 不自动清除 statistical-modeling / scientific-visualization downstream adaptation truth。

### CW06-ER11 — README / changelog closure

检查：

- plugin changelog update；
- root release metadata仅在正式 release closure；
- README实际检查；
- README修改时真实调用 installed Clear Writing；
- “读 SKILL.md”不能冒充 invocation。

### CW06-ER12 — Goal / Kickoff 是否把关键选择留给 Codex

逐项对照 Proposal、Plan、Runbook和Kickoff。

若 Codex仍需要决定：
- source owner；
- package shape；
- delete list；
- manifest capability；
- external surface claim；
- Gate input；
- retry；
- failure recovery；
- version；
- G3失败后是否上MCP；

则 REVISE。

## 7. 复杂度检查

你必须再次问：

- 新 builder + single wrapper source 是否真的是解决当前失败所需的最小新增机制；
- 是否错误建立了第二套写作系统；
- 是否应该现在就新增 MCP/App；
- P0/G1-G6 是否重复过重。

如果删掉某个 Gate仍能完整证明相同能力，可要求合并；但不得为了“更轻”删掉真实 Reader Guide read/write/readback 或 fresh full-artifact review。

## 8. 禁止 live action

本轮不得：

- 修改 repo；
- 修改 Issue/Project；
- 启动 Codex；
- 更新 Personal Plugin；
- 创建 G3 branch；
- 运行 G1-G6；
- 修改 Project setting；
- 创建 App/MCP；
- 调用付费模型；
- 把 PASS 当用户授权。

## 9. 输出格式

先用一屏自然中文回答：

- execution package 是否已把 Proposal 收敛成可执行计划；
- 最大剩余风险；
- 是否有关键选择仍留给 Codex；
- 是否现在可以交 Codex（只表示 readiness，不表示用户已授权）。

若 REVISE，使用稳定 finding ID `CW06-ERxx`，只阻塞真实问题，并附一份可直接交回 Planner 的最小完整返修提示词。

若 PASS，必须输出：

```text
DECISION=PASS
READY_FOR_CODEX=YES
TARGET_REPO=YuukiAS/AI_Skills_Collection
TARGET_PLUGIN=writing-style
TASK_KEY=clear-writing--single-entry-artifact-finalization
APPROVED_PROPOSAL_COMMIT=3eefc626b86566113125a06fc6046a2bec1eafb2
APPROVED_PACKAGE_COMMIT=<用户提供的 exact PACKAGE_COMMIT>
APPROVED_PLAN=docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_1_2026-10-20.md
APPROVED_GOAL=docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_1_2026-10-20.md
APPROVED_RUNBOOK=docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_1_2026-10-20.md
APPROVED_KICKOFF_DRAFT=docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_1_2026-10-20.md
NEXT_HANDOFF=USER_AUTHORIZATION
```

并明确：

- 该 PASS 只批准这个 exact execution package；
- 不是 implementation PASS；
- 不是 G1-G6 PASS；
- 不是 release PASS；
- 不授权用户未发送 Kickoff 前的任何 mutation；
- 用户下一步只需在 Planner thread 发送批准后的 Kickoff，不需要手工维护 Plugin ID、ZIP、GitHub Project 或 Gate。
