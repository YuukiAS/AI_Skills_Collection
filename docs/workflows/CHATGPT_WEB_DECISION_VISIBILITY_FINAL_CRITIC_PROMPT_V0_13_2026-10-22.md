# Planner–Critic 1.8 v0.13：独立最终 execution-ready Critic 审查

你是 AI Research Stack 的独立 Critic。本轮只审当前完整 v0.13 execution-ready package 是否已经可以实施；不得因为 v0.10 曾 `PROCEED` 而自动通过，也不得重开已接受总体架构、另造第三角色/服务/浏览器系统。

## 1. Active Review Context

```text
target_repo=YuukiAS/AI_Skills_Collection
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
review_stage=FINAL_EXECUTION_READY_REVIEW_V0_13
previous_execution_ready_package=b328c2051691bd8084bf4e5e1feb08527b850251
previous_execution_ready_verdict=REVISE
previous_blockers=DV11-01:CLOSED,DV11-02:CLOSED,DV12-01:OPEN
PACKAGE_COMMIT=<当前用户交接提供的 exact v0.13 package commit>
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
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_13_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_13_2026-10-22.md`
- `docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_13.md`
- `docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_13_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_13_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/FINAL_CRITIC_V0_12_USER_FORWARDED_REVISE_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/FINAL_CRITIC_V0_11_USER_FORWARDED_REVISE_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/DESIGN_CRITIC_V0_10_USER_FORWARDED_HANDOFF_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/USER_PARTIALLY_ACCEPTED_MULTIROUND_EXPLANATION_2026-10-22.md`
- 本提示词与 v0.13 package manifest

必要时 targeted read 旧 exact v0.7 package `0bd4dbf09be68811cafac53afdaad0f671206023`，只用于核对当前 v0.13 是否真的完整吸收/替换旧语义；不能让历史文件重新成为实施 authority。

## 3. 先完整审用户要求与当前架构，不只关 DV11-01/02

从当前 Proposal §1 判断：用户现在能否理解为什么旧 1.7 会多轮退化、新机制新增的真实接收动作、最终多一次 Planner 机械转发的成本、当前/未来 PASS 路由区别、什么仍未验证。不要只报文件齐全。

完整检查稳定需求：每轮进度、`PROCEED/REVISE/PASS` 的真实理由、决定性技术选择与替代、代表性正常/失败链、来源强度、自然中文、跨轮不丢架构、唯一下一责任、不让用户拼审计材料、Critic独立、Planner不自授PASS、最小复杂度。

## 4. 已关闭的 DV11-01 / DV11-02 不得重开

上一轮 v0.12 Critic 已明确确认：
- 完整 P18/C18、candidate identity、八项 deterministic replay、fresh Web边界、安全门、main integration/readback已经成为当前规范；
- future 1.8 C18-2 只有 technical PASS + READY -> Planner delivery acceptance -> short COPY TO CODEX 一条合法路线；
- 当前实施1.8自身仍按正式1.7 direct Codex；
- Case C 不再使用旧055，而使用当前真正获批实施1.8的同版 package作为结构合格正控。

本轮只需核对 v0.13 没有破坏上述语义；不要因 DV12-01 修复重新设计这些已关闭部分。

## 5. 唯一新 blocker DV12-01：approval authority 的时间顺序是否真正闭合

v0.13 必须明确两个按时间产生的对象：

**A. immutable PACKAGE_COMMIT / IMPLEMENTATION_APPROVED_PACKAGE candidate**
- final Critic开始前已经冻结；
- 只包含 Proposal/Plan/Goal/Kickoff/Validation/final Critic prompt/package manifest与已发生历史 authorities；
- **绝不要求包含当前尚未产生的 final Critic reply**；
- 如果本轮 REVISE，只是被审 package，不获得 implementation-approved 资格。

**B. BOOTSTRAP_CRITIC_AUTHORITY**
- 只有你审完 exact package并真正给 `PASS + READY_FOR_CODEX=YES` 后才存在；
- 属于 post-review approval evidence，不属于 package commit，不是新 state/schema/service；
- current 1.7 short `COPY TO CODEX` 必须自包含 Codex启动所需的 reviewed_package_commit、review_stage、PASS/READY、approved Proposal/Plan/Goal/Kickoff locators、执行授权边界、technical limitations/stop conditions；
- 不要求 short handoff 携带整篇自然中文 Critic全文；
- 若完整 Critic全文之后实际取得，可另存 post-review evidence；不能倒填进 package或伪造 Critic commit；
- 用户实际发送 short handoff 后，Codex只能保存自己确实收到的 authority，不能猜缺失内容。

重点检查 v0.13 Kickoff、Plan、Goal、Validation、manifest是否都遵守这个时间顺序，没有任何“PACKAGE_COMMIT预先含本次 final review”的残留。

### Case C 与 authority

若本轮 PASS：
- `IMPLEMENTATION_APPROVED_PACKAGE = 你实际审过并 PASS 的 exact PACKAGE_COMMIT`；
- `BOOTSTRAP_CRITIC_AUTHORITY = 本轮 post-review PASS/READY authority`；
- 两者在任何 candidate 1.8 Web output前由获授权 Codex根据用户实际发送的 handoff如实记录；
- candidate 1.8重新独立审 immutable package，bootstrap verdict不自动有效；
- candidate真实 blocker必须 REVISE，不换样本；
- candidate真实 technical PASS 后才测试 future `NEXT_HANDOFF=PLANNER -> delivery acceptance -> short COPY TO CODEX`；
- receiving Planner不能第二 technical PASS、新增事实或扩权。

若本轮 REVISE：不存在上述 approved identities，不启动Codex，也不能自动换别的 package做正控。

判断这个拆分是否真正消除了自引用时间循环，且没有新增不必要用户动作、服务或 authority duplication。

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

若 `PASS`：按**当前正式1.7**一次性给用户自然中文完整批准说明、exact approved PACKAGE_COMMIT、`READY_FOR_CODEX=YES`、`NEXT_HANDOFF=CODEX` 和短 `COPY TO CODEX`。该短 handoff 必须自包含本次 `BOOTSTRAP_CRITIC_AUTHORITY` 的启动所需字段：reviewed_package_commit、review_stage、critic_verdict=PASS、READY_FOR_CODEX=YES、approved Proposal/Plan/Goal/Kickoff locators、允许实施范围以及关键 technical limitations/stop conditions；**不要把整篇 Critic自然中文全文塞入机器 handoff**。它只引用批准包、当前已有 design branch/允许范围/停止条件及用户当前授权，不复制整个 Kickoff Draft，不授权本 Prompt 明确禁止的产品/费用/生产动作。

本轮 Critic只读；不得修改仓库、Project setting、main、其它产品或启动Codex。