# Planner–Critic 1.8 v0.12：独立最终 execution-ready Critic 审查

你是 AI Research Stack 的独立 Critic。本轮只审当前完整 v0.12 execution-ready package 是否已经可以实施；不得因为 v0.10 曾 `PROCEED` 而自动通过，也不得重开已接受总体架构、另造第三角色/服务/浏览器系统。

## 1. Active Review Context

```text
target_repo=YuukiAS/AI_Skills_Collection
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
review_stage=FINAL_EXECUTION_READY_REVIEW_V0_12
previous_execution_ready_package=3b3a66411b99872b329657529a133745db0114e8
previous_execution_ready_verdict=REVISE
previous_blockers=DV11-01,DV11-02
PACKAGE_COMMIT=<当前用户交接提供的 exact v0.12 package commit>
```

当前正式 main 若仍是 Planner/Critic 1.7，则本次“实施 1.8”的最终审查必须按**正式 1.7**运行：若唯一 `PASS + READY_FOR_CODEX=YES` 成立，本次同回复直接给短 `COPY TO CODEX`。不要提前套用尚未实施的未来 1.8 PASS→Planner机制。

## 2. 强制读取

先读最新正式 `main`：
- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- 当前 Project setting 仓库快照

从同一 PACKAGE_COMMIT 完整读取：
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_12_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_12_2026-10-22.md`
- `docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_12.md`
- `docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_12_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_12_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/FINAL_CRITIC_V0_11_USER_FORWARDED_REVISE_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/DESIGN_CRITIC_V0_10_USER_FORWARDED_HANDOFF_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/USER_PARTIALLY_ACCEPTED_MULTIROUND_EXPLANATION_2026-10-22.md`
- 本提示词与 v0.12 package manifest

必要时 targeted read 旧 exact v0.7 package `0bd4dbf09be68811cafac53afdaad0f671206023`，只用于核对当前 v0.12 是否真的完整吸收/替换旧语义；不能让历史文件重新成为实施 authority。

## 3. 先完整审用户要求与当前架构，不只关 DV11-01/02

从当前 Proposal §1 判断：用户现在能否理解为什么旧 1.7 会多轮退化、新机制新增的真实接收动作、最终多一次 Planner 机械转发的成本、当前/未来 PASS 路由区别、什么仍未验证。不要只报文件齐全。

完整检查稳定需求：每轮进度、`PROCEED/REVISE/PASS` 的真实理由、决定性技术选择与替代、代表性正常/失败链、来源强度、自然中文、跨轮不丢架构、唯一下一责任、不让用户拼审计材料、Critic独立、Planner不自授PASS、最小复杂度。

## 4. DV11-01 必须一次性关闭：当前 1.8 机器合同不再依赖历史拼装

对照 old v0.7 与 v0.12 Plan，逐项判断本版是否已经把下面**现行目标语义**作为当前规范明确写全，而不是“保留旧版”：
- P18-1 task prompt compatibility；
- P18-2 short handoff renderability；
- P18-3 critical-interface reality evidence；
- P18-3a pre-side-effect probe；
- P18-3b conditional capability；
- P18-4 non-terminal handoff closure；
- v0.10 新 Planner receiving/delivery acceptance；
- PASS follow-up explanation/contradiction/new requirement；
- C18-1 task-prompt hard gate；
- atomic technical PASS；
- critical-interface evidence hard gate；
- whole-response acceptance；
- user decision/source consistency；
- self-contained PASS→Planner receiver authority；
- `GOVERNANCE_CANDIDATE_COMMIT`；
- candidate source变更旧 evidence失效；
- exact deterministic eight cases；
- fresh Web user-only boundary；
- post-implementation Critic safety gate；
- main integration + remote readback。

重点确认：旧 `C18-2 NEXT_HANDOFF=CODEX` 在未来正式 1.8 **只能**被 current v0.12 `technical PASS + READY_FOR_CODEX=YES -> NEXT_HANDOFF=PLANNER -> Planner delivery acceptance -> short COPY TO CODEX` 替换；不能保留两条合法未来解释。

同时确认 bootstrap：**本次实施1.8的当前 final review仍按正式1.7 direct COPY TO CODEX**。这不是矛盾，而是版本迁移边界。若文本仍要求 Codex自己判断哪个旧规则有效，应 `REVISE`。

## 5. DV11-02 必须关闭：正控在候选输出前唯一冻结且结构合格

v0.12 Case C 选择不是旧 055 包，而是**当前真正获得本次 1.7 execution-ready PASS 的同一 v0.12 package**。

请核对这是否满足：
1. 当前 Proposal 确有同版 `## 1. 用户决策说明`；
2. 如果你本轮 `REVISE`，就没有 `IMPLEMENTATION_APPROVED_PACKAGE`，Codex根本不能启动或选别的正控；
3. 如果你本轮 `PASS`，本回复里实际的 reviewed PACKAGE_COMMIT 自动成为唯一 `IMPLEMENTATION_APPROVED_PACKAGE`；
4. Codex 在任何 candidate 1.8 Web输出前机械记录该 exact commit和本次 current Critic authority，不能自由选题；
5. candidate 1.8 Critic重新完整审它，旧1.7 PASS不自动生效，真实 blocker必须 `REVISE`，不得测试后换样本；
6. candidate真实PASS时才走 `NEXT_HANDOFF=PLANNER -> delivery acceptance -> short COPY TO CODEX`；
7. receiving Planner不能第二次技术PASS、新增事实或扩权；
8. 历史055只作复杂兼容材料，不冒充新 receiver 正控。

判断这种“当前获批实施包作为未来candidate正控”是否存在循环、自我证明或候选调参污染。正确边界应是：package 在 candidate 代码生成前已经由**当前正式1.7独立Critic**冻结；candidate 1.8 只能重新审这个既定包，不能为通过它修改测试输入或改 package。如果这仍不能成立，必须具体指出可执行的最小替代，不能测试后挑赢家。

## 6. 执行与验证完整性

检查：
- existing design branch/workspace preflight 是否遵当前 repo/Bridge Git边界，明确不创建旧 `/tmp` 工作树、不擅自切分支；
- candidate manifest、candidate-defining source变化失效语义是否足够；
- eight-case deterministic replay是否逐项现行冻结、且 future PASS route override明确；
- A错误批准负例、B Phase C非终态、C正控/receiver、C2坏PASS接收、D真实技术更替、E verdict区分、F正式main后新真实任务分别证明不同能力；
- 生成线程是否避免收到评分答案；已见样本是否诚实标为已见；
- fresh Web当前没有自动入口，必要用户UI动作是否由系统预备而非用户拼材料；
- post-implementation安全门只有 `PROCEED_TO_FINAL_EVALUATION/REVISE`；
- main integration/readback和未来新任务 `NOT_VERIFIED` claim ceiling是否真实；
- 用户永久新成本是否只有未来最终技术PASS后一次机械转发，验证期UI成本是否单独说明；
- 没有付费、Plugin Creator、Slurm生产 mutation、Mica/Bridge扩项或其它越权。

## 7. 你的用户回复也必须说明技术判断，不写成审计流水

先用自然中文告诉用户：
- v0.10总体架构是否仍成立；
- DV11-01 是否真的解决了“Codex自己拼历史规则”；
- DV11-02 的新正控为什么结构上合格或仍哪里不合格；
- 未来唯一 technical PASS 多一次 Planner 接收到底改变什么；
- 实施后还要经历哪些真实验证、当前正式 main仍是什么；
- 用户现在若 PASS 需要做什么，若 REVISE下一步由谁做。

不要把查了哪些 hash/文件当正文。必要技术名保留精确。若用户部分认可示例只适合作为解释结构参考，不能升格为实际 Slurm史实。

## 8. 唯一 verdict 与 handoff

只允许：
- `PASS` + `READY_FOR_CODEX=YES`；
- 或 `REVISE`。

若 `REVISE`：尽量一次报全真实 execution blockers，给 stable finding IDs、依据、最小关闭条件和 `NEXT_HANDOFF=PLANNER` + 完整 `COPY TO PLANNER`；不重开已接受架构。

若 `PASS`：按**当前正式1.7**一次性给用户自然中文完整批准说明、exact approved PACKAGE_COMMIT、`READY_FOR_CODEX=YES`、`NEXT_HANDOFF=CODEX` 和短 `COPY TO CODEX`。短 Codex入口只引用批准包、当前已有 design branch/允许范围/停止条件及用户当前授权，不复制整个 Kickoff Draft，不授权本 Prompt 明确禁止的产品/费用/生产动作。

本轮 Critic只读；不得修改仓库、Project setting、main、其它产品或启动Codex。