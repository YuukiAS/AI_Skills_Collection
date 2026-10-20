# ChatGPT Web PASS 原子交付修复 — v0.5 设计/执行包 Critic Prompt

你现在担任 AI Research Stack 的独立 Critic，审查 Planner/Critic 治理 v0.5 的完整设计与 execution package。

## Active Review Context

```text
target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=ChatGPT Web Planner-Critic governance
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
proposal_path_and_version=docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_5_2026-10-20.md@v0.5
proposal_commit=afc19a46bf53d9f8841dee0cc9ec42fe17c41365
package_commit=af68349e1283a8cb8c1f6928f6bc821236412d28
previous_review_stage=DESIGN_PROPOSAL_REVIEW_V0_4
previous_verdict=REVISE
stable_blocker=PASSINT-V04-01
review_stage=DESIGN_AND_EXECUTION_PACKAGE_REVIEW_V0_5
```

本轮仍是设计/执行包审查，只允许：

- `PROCEED`
- `REVISE`

禁止输出 `PASS`，禁止 `READY_FOR_CODEX=YES`，禁止给 Codex 执行入口。

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

若 main 已前进，只吸收真正影响本包正确性的变化，不因无关提交机械失效。

## 2. 从 exact package commit 读取完整 v0.5 包

从：

`af68349e1283a8cb8c1f6928f6bc821236412d28`

完整读取：

- `results/chatgpt-web--pass-integrity/PASS_ATOMIC_DELIVERY_V0_4_CRITIC_REVIEW_2026-10-20.md`
- `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_5_2026-10-20.md`
- `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_EXECUTION_PLAN_V0_5_2026-10-20.md`
- `docs/goals/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_GOAL_V0_5.md`
- `docs/operations/prompts/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_KICKOFF_DRAFT_V0_5_2026-10-20.md`

不要只读 Proposal。

## 3. 核对旧 Clear Writing 真实负控

从 exact commit：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

核对至少：

- `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_CRITIC_PROMPT_V0_2_2026-10-20.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_2_2026-10-20.md`
- `docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_2_2026-10-20.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_2_2026-10-20.md`
- `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_2_2026-10-20.md`

确认旧 task-specific Critic prompt 的冲突真实存在，而不是 Planner 臆造。

## 4. 本轮首先复核 PASSINT-V04-01

v0.5 将原先自相矛盾的“同一 package 既应被 compatibility gate REVISE，又应作为正向 PASS package”拆成两阶段：

### 阶段一：负控

- exact old package `d7b810d...` 保持不变；
- 1.8 compatibility hard gate 必须拒绝它；
- 不允许忽略 task-prompt 冲突后继续 PASS。

### 阶段二：正向回归

- 阶段一通过后才准备；
- 只最小修正 Clear Writing task-specific execution-ready Critic prompt 与必要 locator/package identity；
- 产品 Proposal/Plan/Goal/Runbook/Kickoff 产品语义、G1-G6、生产代码均不重做；
- 必须形成新的 exact package commit；
- 独立 Critic 对新 package 做完整 execution-ready review；
- 不预设 PASS；若发现真实产品 blocker，正常 REVISE 并留在同一 Clear Writing task。

判断这是否完整关闭 PASSINT-V04-01。

## 5. 审查 Planner/Critic 1.8 的具体边界

### Planner 1.8

判断以下是否必要、充分、不过重：

1. execution-ready task-specific Critic prompt compatibility preflight；
2. task prompt 不得改写中央 verdict / READY_FOR_CODEX / NEXT_HANDOFF / PASS 输出合同；
3. task prompt 可以优先提示旧 blocker，但最终审查仍必须全量；
4. Planner 必须能从冻结 Goal/Kickoff/授权边界生成短 Codex handoff，否则 package 未闭合。

### Critic 1.8

判断以下是否必要、充分、不过重：

1. execution-ready compatibility hard gate；
2. 冲突存在时不得 PASS，但仍继续其余可完成审查，尽量一轮报全；
3. 有效 PASS 同一回复必须一次交齐：
   - 一屏实际架构说明；
   - exact approved locators；
   - `READY_FOR_CODEX=YES`；
   - `NEXT_HANDOFF=CODEX`；
   - 短 `COPY TO CODEX`；
4. 缺任何一项不得先 PASS 后补；
5. follow-up 按“解释请求 / 矛盾证据 / 新要求”分类；
6. 矛盾可以由 Critic 在解释过程中自行发现，不要求用户先指出。

检查这些规则会不会错误阻止 Critic 发现新问题，或使普通解释请求再次触发无依据的架构升级。

## 6. 审查 execution package 是否真的可实现

重点检查：

- 正式修改范围是否只需 Planner/Critic 合同、回归记录、优质示例和 results；
- Project setting 与 Capability Gate Policy 保持不变是否合理；
- deterministic compatibility replay 的 8 个 case 是否足以直接验证 1.8；
- 两阶段 Clear Writing 回归是否有真实顺序、identity 和停止条件；
- 第二阶段只修 task-specific prompt 是否会意外改变 Clear Writing 产品语义；
- 正向回归若 REVISE 时是否能诚实停下，而不是换题追 PASS；
- governance `CANDIDATE_ACCEPTED` 的恢复条件是否足够；
- 是否出现新角色、schema、状态机、数据库、service、watcher、daemon 或 prompt compiler。

## 7. 真实回归重点

必须用过去事故反证：

1. 如果 task prompt 写“只复核四个 blocker”，1.8 是否会阻止最终 PASS？
2. 如果 task prompt 写 `NEXT_HANDOFF=USER_AUTHORIZATION`，是否会被 package compatibility gate 拦截？
3. 如果 Critic 给了 PASS 但没架构说明，是否明确属于无效 PASS？
4. 如果 Critic 给了 PASS 但没 `COPY TO CODEX`，是否明确属于无效 PASS？
5. 如果 Critic全文倾倒 Kickoff，是否会被判不合格？
6. 用户问“repo 写回怎么保证”时，是否应该先解释 approved G3，而不是临时设计 `create_blob` / MCP？
7. 如果解释过程中真的发现 approved G3 无法支持既有承诺，是否仍能回 Planner？
8. 如果用户明确要求“所有插件任何 repo 写入都不可绕过”，是否能识别为新要求？

## 8. 外部核查

做少量独立官方核查，重点只看“高层合同与低层 task prompt 冲突时必须有明确优先级/兼容性处理”是否合理。不要把外部 agent 框架照搬进仓库。

## 9. Tracking

按 `AI_SKILLS_MAINTENANCE_BOARD.md` 核对 tracking。

当前 Planner 搜索未发现既有 `chatgpt-web--pass-integrity` tracking Issue，并因缺少可验证的 Clear Writing + GitHub Project mutation 组合入口而没有创建。

若你能证明存在真实 tracking Issue，指出 exact locator；否则保持 pending，不要求用户手工维护，也不把它作为本设计 blocker，除非违反当前 board contract。

## 10. Verdict

只有以下全部成立才可：

`VERDICT=PROCEED`

- PASSINT-V04-01 真正关闭；
- 1.8 机制能直接阻止本次 Clear Writing 事故；
- execution package 完整且可实现；
- 两阶段回归不再自相矛盾；
- 正向回归不预设 PASS；
- 不需要改变 Project setting、Capability Gate Policy 或产品架构；
- 方案保持轻量。

否则：

`VERDICT=REVISE`

只阻塞真实风险，给最小关闭条件。

## 11. 用户可见输出

先用一屏自然中文说明：

- PASSINT-V04-01 是否真的关闭；
- 1.8 相比 1.7 新增的真实能力；
- 两阶段回归为何不再自相矛盾；
- 是否让流程明显变重；
- 还有哪些真实问题；
- 用户现在是否需要动作；
- 下一步唯一接收方是谁。

然后再给机器审查记录。

若 PROCEED：
- `NEXT_HANDOFF=PLANNER`
- 自动生成完整 `COPY TO PLANNER`；
- 要求 Planner 准备最终 execution-ready Critic round；
- 不得给 Codex。

若 REVISE：
- 同样给完整 `COPY TO PLANNER`；
- 只处理本轮 blocker。

本轮不得实施 1.8、不得修改 Project setting、不得修改 Clear Writing 产品、不得运行 G1-G6、不得启动 Codex。
