# Planner–Critic 1.8：执行就绪提案 v0.13

日期：2026-10-22  
任务：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
当前正式基线：`main@f1de8e85957d32a50f4458349f450ec65add13bb`，Planner/Critic 仍为 1.7。  
上一最终执行就绪审查：v0.12 @ `b328c2051691bd8084bf4e5e1feb08527b850251`，Critic = `REVISE`；原文归档于 `results/chatgpt-web--pass-integrity/FINAL_CRITIC_V0_12_USER_FORWARDED_REVISE_2026-10-22.md`。  
当前阶段：重新提交完整 execution-ready 包；未获 `PASS`，不得实施。

## 1. 用户决策说明

v0.12 已经关闭此前两个 blocker，整体架构继续不变：同版 Proposal 维护用户真正阅读的当前技术决策说明；Critic 独立对照真实技术审这份说明；接收 Critic 结果的 Planner 必须验收实际交付，而不能只消费 verdict token；未来正式 1.8 的唯一技术 `PASS` 仍由 Critic 产生，但先回原 Planner 做一次读者交付接受后才生成 Codex 入口。

v0.12 唯一的新问题不是架构设计，而是一个**时间顺序错误**：Kickoff 把“当前 final Critic review 的真实回复/归档 locator”列进同一个待审 `PACKAGE_COMMIT`。但 package 必须先冻结，Critic 才能审；Critic 的最终回复只能在审完以后产生。所以一个 commit 不可能同时是“审查前的对象”和“包含审查后结果的对象”。如果不修，Codex只能忽略要求、自己猜 authority 或停止，三种都不允许。

v0.13 只做一个修复：**把审查前的不可变实施包与审查后产生的批准 authority 分开。**

审查前冻结的是：

```text
IMPLEMENTATION_APPROVED_PACKAGE candidate
= exact v0.13 PACKAGE_COMMIT
```

这个 package 只包含在 Critic 开始前就能存在的 Proposal、Execution Plan、Goal、Kickoff Draft、Validation Contract、final Critic prompt、package manifest 和历史 review authorities。它**不包含、也不要求包含**未来才产生的本轮 final Critic reply。

Critic 审完以后，只有它真正给出：

```text
PASS
READY_FOR_CODEX=YES
```

才产生第二个对象：

```text
BOOTSTRAP_CRITIC_AUTHORITY
```

它不是新的状态机、数据库或服务，只是当前正式 1.7 最终回复/短 Codex handoff 中必须自包含的批准证据。至少包含：审了哪个 exact package、审查阶段、verdict、READY、批准的 Proposal/Plan/Goal/Kickoff locator、当前执行授权边界和关键技术限制。短 Codex handoff **不需要携带整篇 Critic 自然中文全文**。

如果当前 Critic 能合法写 repo，可以在审查之后把完整原文另存为 post-review evidence；如果不能，用户也不需要手工创建文件。短 `COPY TO CODEX` 已携带 Codex启动所需的 authority，Codex 在用户明确发送并授权后，才可在 task scope 内把它实际收到的 authority 如实归档到 `results/`。这个归档发生在 package 之后，绝不能反过来声称属于原 package commit。

因此 Case C 也保持清楚：只有当前 Critic 真正 PASS 时，**它实际审过的 exact v0.13 package** 才成为 `IMPLEMENTATION_APPROVED_PACKAGE`；同时存在真实 `BOOTSTRAP_CRITIC_AUTHORITY`。candidate 1.8 后续重新独立审 package，bootstrap verdict 只证明“这是曾被当前 1.7 批准用于实施 1.8 的冻结包”，不替代 candidate 自己的技术判断。candidate 发现真实 blocker就 `REVISE`，不换样本；只有 candidate自己真实 technical PASS，才测试未来的新链路：
`NEXT_HANDOFF=PLANNER -> Planner delivery acceptance -> short COPY TO CODEX`。

这项修复**不改变任何已经通过的 P18/C18、八项 deterministic replay、A/B/C/C2/D/E/F、候选身份、安全门、fresh Web 边界或 main integration/readback**。旧 v0.12 的 DV11-01、DV11-02 已关闭，不再重开。

用户永久新增成本仍只有未来唯一 technical PASS 后一次机械转发给已有 Planner。候选验证期间的 fresh Web UI 是临时验收成本，单独说明。当前正式 main 仍是 1.7，用户现在不需要实施任何动作；v0.13 只是重新交最终 execution-ready Critic 审查。

## 2. 已接受且不再修改的总体架构

保持 v0.12 的完整 Planner/Critic 1.8 合同：
- 同版 `## 1. 用户决策说明` 与实质技术变化同步；
- Critic 从真实 source 独立审技术与说明；
- Planner receiving acceptance 三分法；
- future technical PASS → Planner delivery acceptance → Codex；
- Planner不能第二 technical PASS、不能扩权/补事实；
- task-prompt compatibility、short handoff、critical-interface reality、pre-side-effect probe、conditional capability、non-terminal handoff、whole-response acceptance、follow-up classification；
- `GOVERNANCE_CANDIDATE_COMMIT`、candidate-source drift invalidation、八项 deterministic replay、post-implementation safety gate、fresh Web user-only boundary、main integration/readback。

不修改 Project setting、Capability Gate Policy、AGENTS、Clear Writing、Slurm、Bridge Kit、Mica、Plugin Creator 或其它产品；不新增第三人工角色、service/watcher/daemon、database/state machine、prompt compiler、paid model 或浏览器拦截。

## 3. 两个按时间顺序产生的身份

### A. IMPLEMENTATION_APPROVED_PACKAGE

在 Critic 开始审查前就冻结的 immutable `PACKAGE_COMMIT`。它包含：
- Proposal；
- Execution Plan；
- Goal；
- Kickoff Draft；
- Validation Contract；
- final Critic prompt；
- package manifest；
- 已经发生的历史 review authorities。

它不包含当前 final Critic reply。若本轮 `REVISE`，这个 package只是“被审但未批准”的 package，**不存在 implementation-approved 资格**，不得启动 Codex。

### B. BOOTSTRAP_CRITIC_AUTHORITY

只有当前正式 1.7 final Critic 对上述 exact package 真正给 `PASS + READY_FOR_CODEX=YES` 后才产生。当前 short `COPY TO CODEX` 至少携带：
- `reviewed_package_commit`；
- `review_stage`；
- `critic_verdict=PASS`；
- `READY_FOR_CODEX=YES`；
- approved Proposal/Plan/Goal/Kickoff locators；
- 当前实施授权边界；
- 关键 technical approval limitations / stop conditions。

这是一份 post-review approval evidence，不属于原 package commit。若完整 Critic自然中文原文后续有实际可用输入，可在实施开始后按原文归档；若没有，不能伪造 review commit，也不能要求用户整理全文。

## 4. Case C 的真实关系

只有本次 exact v0.13 package 被当前 1.7 Critic PASS，才同时成立：
- `IMPLEMENTATION_APPROVED_PACKAGE = reviewed_package_commit`；
- `BOOTSTRAP_CRITIC_AUTHORITY = current PASS/READY authority`。

Codex 接到用户真正发送的 short handoff 后，先把自己实际收到的两项 identity/limitations 如实存入 task evidence，**早于任何 candidate 1.8 Web output**。candidate 1.8 Critic只把 bootstrap authority当来源/历史批准身份，仍重新审 immutable package全部技术语义。

本轮 REVISE则没有 approved package、没有 bootstrap authority、没有 Codex启动，也不能选其它包顶替。

## 5. 当前完成边界

v0.13 仍只是待最终审查包。只有当前正式 1.7 Critic 对同一 exact package 给 `PASS + READY_FOR_CODEX=YES`，并且用户实际发送它生成的短 Codex 入口，才授权实施两份角色合同 1.8。之后候选冻结、实现后安全门、真实 Web评估、合法 main integration/readback及未来新真实任务仍分别取得证据，不提前宣称完成。
