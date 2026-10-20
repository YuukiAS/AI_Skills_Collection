# ChatGPT Web PASS 原子交付修复 — Critic Prompt v0.4

你现在担任 AI Research Stack 的独立 Critic，审查 Planner/Critic 治理的 v0.4 修复提案。

## Active Review Context

```text
target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=ChatGPT Web Planner-Critic governance
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
proposal_path_and_version=docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_4_2026-10-20.md@v0.4
proposal_commit=756f99d77e878f99c440a409bf7620e6d038e4a4
design_base=main@272f5cd1b3599acb0c5b95ef57ce00a0cf1b0ac3
review_stage=DESIGN_PROPOSAL_REVIEW_V0_4
```

本轮是设计审查，只允许：

- `PROCEED`
- `REVISE`

禁止输出 PASS，禁止授权 Codex。

## 1. 先读取当前正式治理来源

实际读取并核实 `YuukiAS/AI_Skills_Collection` 最新 `main`，至少读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-19.md`
- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`
- `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md`
- 本轮 Proposal v0.4

如果最新 main 已前进，使用当前事实；不要因无关提交机械否定本提案。

## 2. 读取本轮真实回归证据

从 exact commit：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

读取：

- `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_CRITIC_PROMPT_V0_2_2026-10-20.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_2_2026-10-20.md`
- `docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_2_2026-10-20.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_2_2026-10-20.md`
- `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_2_2026-10-20.md`

核实真实冲突：任务专用 prompt 将最终审查缩成四个 blocker closure，并把通过后的下一步写成 `NEXT_HANDOFF=USER_AUTHORIZATION`；中央 Critic 1.7 则要求重新检查完整用户承诺与完整执行包，并在同一条 PASS 回复直接输出实际架构说明和短 `COPY TO CODEX`。

不要重新审 Clear Writing 0.6 产品架构是否正确。本轮只把它当作中央治理正向 PASS 路径的真实回归证据。

## 3. 独立判断根因

重点判断：

1. 问题是否确实属于 Planner/Critic 治理，而不是 Clear Writing G3、Plugin Creator 或 Bridge Kit；
2. 当前中央合同虽然写了正确要求，是否仍缺一个明确的 task-prompt compatibility hard gate；
3. 只验证两个优质 `REVISE` 案例、没有验证真实 `PASS` 交付，是否是此前过早收口的关键原因；
4. 用户询问批准架构怎样工作，却触发 Critic 临时新增 `create_blob`、MCP 和全局写入拦截，是否说明 PASS 后解释行为需要明确边界。

若根因归类不正确，REVISE；不要为了维持先前治理结论而接受错误 owner。

## 4. 审查 v0.4 的四项核心机制

### A. 任务专用 prompt 与中央合同兼容性

判断以下设计是否必要且比例适当：

- task prompt 可以描述对象、证据和返修重点；
- 不得缩小最终 execution-ready 审查范围；
- 不得重新定义 verdict、`READY_FOR_CODEX`、下一接收方或输出格式；
- 不得以 `NEXT_HANDOFF=USER_AUTHORIZATION` 代替 `NEXT_HANDOFF=CODEX`；
- 不得省略架构说明或短 Codex handoff；
- 有冲突时，执行包本身必须 REVISE。

特别判断：Critic 是否应继续完成其余审查、在同一轮报告全部 blocker，以避免只修 prompt 后再发现产品问题。

### B. PASS 一次性交付

判断 execution-ready PASS 是否必须在同一条回复同时包含：

1. 一屏实际架构说明；
2. 精确批准定位；
3. `READY_FOR_CODEX=YES`；
4. `NEXT_HANDOFF=CODEX`；
5. 可直接发送的短 `COPY TO CODEX`。

判断“缺任一项不得 PASS”是否过严；若认为过严，必须给出同样能避免用户连续追问的更简单机制。

不得接受“先 PASS、以后再补格式”的方案。

### C. PASS 后解释稳定性

判断“解释请求 / 矛盾证据 / 新要求”三分法是否合理：

- 解释请求应引用批准包，不重开设计；
- 真实矛盾应明确使哪项批准失效，并回同一 task Planner；
- 新要求只有在用户明确增加时才进入新设计。

检查这条规则是否会错误阻止 Critic 发现真实问题，或相反仍允许模型因普通追问擅自变重。

### D. 正向 PASS 回归

判断用 Clear Writing 0.6 做一次真实正向 PASS 回归是否足够：

- 同一回复一次交齐说明和 Codex handoff；
- 用户随后询问 repo 写回保证时，只解释冻结 G3 链；
- 不新增 `create_blob`、MCP、App、全局网关或新 Gate；
- 用户明确提出全局不可绕过保证时，才识别为新要求。

说明是否还需要一个不同任务族的补充回归；不要机械要求固定样本数。

## 5. 范围与复杂度

独立判断本轮只修改：

- Planner Role Contract → 1.8；
- Critic Role Contract → 1.8；
- ChatGPT Web collaboration regressions；
- 优质 Critic 示例；
- 结果证据；

是否足够。

本轮 Proposal 明确不修改：

- 当前 Project setting；
- Capability Gate Policy 1.2；
- Clear Writing 产品架构与代码；
- Bridge Kit；
- Plugin Creator；
- 任何新角色、schema、状态机、数据库、服务或统一 prompt compiler。

若你认为必须扩大 owner，必须证明现有 owner 无法轻量修复，而不是因为“更保险”。

## 6. 外部现实核查

做少量独立外部核查，优先官方资料。重点只检查“高层合同不能被低层任务提示词覆盖”这一设计原则是否成熟合理，不要把外部代理框架照搬进本仓库。

## 7. Verdict 标准

只有当以下均成立，才可：

`VERDICT=PROCEED`

- 根因和 owner 正确；
- task prompt compatibility 能真实挡住 Clear Writing 这次冲突；
- PASS 一次性交付能消除用户索取架构说明和 Codex prompt 的负担；
- PASS 后解释稳定性不会压制真实矛盾，也不会允许无依据变重；
- 正向 PASS 回归足以验证修复；
- 方案保持轻量；
- 不需要修改 Project setting 或产品架构。

否则：

`VERDICT=REVISE`

只阻塞会导致相同事故再次发生的真实问题，给最小关闭条件。

## 8. 用户可见输出

先用一屏以内自然中文告诉用户：

- 你是否认可这次根因判断；
- 相比 1.7 真正增加了什么；
- 这能否保证以后 PASS 同时给架构说明和 Codex prompt；
- 是否会让流程变重；
- 当前是否需要用户做任何事；
- 下一步由谁做。

不要把 finding ID、路径和 commit 当作用户摘要。

正式 Clear Writing 可调用时，只对摘要做最终表达检查；不可用时如实说明，不得伪称调用。机器交接保持精确原文。

## 9. 下一入口

若 `PROCEED`：

- `NEXT_HANDOFF=PLANNER`
- 自动生成完整 Planner prompt；
- 要求 Planner 形成 1.8 合同修改执行包和回归计划；
- 不得实施合同、不修改 Project setting、不重新审 Clear Writing 产品。

若 `REVISE`：

- 同样给完整 `COPY TO PLANNER`；
- 只处理本轮真实 blocker。

本轮不得输出 PASS，不得授权 Codex，不得更新任何 Personal Plugin，不得运行 Clear Writing G1–G6。
