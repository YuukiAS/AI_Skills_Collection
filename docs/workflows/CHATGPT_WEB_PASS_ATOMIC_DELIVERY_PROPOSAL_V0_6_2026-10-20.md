# ChatGPT Web PASS 原子交付与正式集成闭环 — Proposal v0.6

日期：2026-10-20  
任务键：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
当前正式基线：`main@272f5cd1b3599acb0c5b95ef57ce00a0cf1b0ac3`  
上一版：`docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_5_2026-10-20.md@v0.5`  
上一轮 Critic：`results/chatgpt-web--pass-integrity/PASS_ATOMIC_DELIVERY_V0_5_CRITIC_REVIEW_2026-10-20.md`  
阶段：最终 execution-ready package 候选；仍需独立 Critic；不得实施

## 1. 本轮结论

上一轮两个结论保持不变：

`PASSINT-V04-01=CLOSED`

旧 Clear Writing 0.6 package `d7b810d194ead881303aaca9c2e4f1d59a97c1f1` 永久作为兼容性负控；正向回归必须使用新的合法 package，且不得预设 PASS。

本轮只关闭：

`PASSINT-V05-01=CLOSED_IN_V0_6_DESIGN`  
`PASSINT-V05-02=CLOSED_IN_V0_6_DESIGN`

v0.6 不新增产品机制。它只把 1.8 候选的 exact authority、候选验证、正式合入 main 和 post-implementation Critic 安全门串成一条完整闭环。

## 2. 冻结用户承诺

以下语义继续冻结：

1. task-specific Critic prompt 不能覆盖中央 Critic 合同。
2. execution-ready `PASS` 必须在同一回复一次交齐：
   - 一屏实际架构说明；
   - exact approved locators；
   - `READY_FOR_CODEX=YES`；
   - `NEXT_HANDOFF=CODEX`；
   - 短 `COPY TO CODEX`。
3. 缺任一项时不存在有效 PASS，不能事后零散补齐追认。
4. PASS 后 follow-up 按“解释请求 / 矛盾证据 / 新要求”处理；普通解释请求不能自动升级成更重架构。
5. 矛盾可以由 Critic 自己发现，不要求用户先指出。
6. deterministic replay 保持现有 8 个 case，不机械增量。
7. Clear Writing 回归保持两阶段：旧包负控 + 新合法包真实 execution-ready 回归；正向回归不预设 PASS。
8. Project setting、Capability Gate Policy 1.2、Clear Writing 产品架构/G1-G6、Bridge Kit、Plugin Creator 均不改。
9. 不新增角色、schema、状态机、数据库、服务、watcher、daemon 或 prompt compiler。

## 3. PASSINT-V05-01：冻结 1.8 candidate authority

### 3.1 唯一候选身份

Codex 在批准的执行分支完成 Planner/Critic 1.8 文本与本轮候选记录后，必须先提交一个 candidate-defining commit，并冻结：

`GOVERNANCE_CANDIDATE_COMMIT=<exact commit>`

该 commit 必须唯一绑定：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md` version 1.8；
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` version 1.8；
- 本轮 collaboration regression 的候选更新；
- 本轮 deterministic replay contract / manifest；
- 本轮正向回归 contract / stop conditions；
- 本轮结果目录中用于定义 candidate identity 的 manifest。

从该点起，Planner/Critic 1.8 的 candidate-defining文本不可再修改。后续结果文件可以追加证据，但每份 evidence 必须记录：

`governance_candidate_commit=<GOVERNANCE_CANDIDATE_COMMIT>`

若合同正文发生任何变化，旧 evidence 失效，必须冻结新的 candidate commit 并重跑受影响验证。

### 3.2 候选阶段统一 authority

以下所有 candidate-phase 验证必须显式读取**同一个** `GOVERNANCE_CANDIDATE_COMMIT` 中的 Planner/Critic 1.8，禁止读取当前 main 1.7 冒充候选：

1. 本地/确定性合同检查；
2. 8-case compatibility replay；
3. implementation 后 Critic safety gate；
4. Clear Writing 第一阶段旧 package 负控；
5. Clear Writing 第二阶段新 package execution-ready Critic 回归；
6. PASS 后解释 follow-up。

这是候选验证，不表示 main 已经升级。

## 4. 正式集成闭环

只有下列条件全部成立后，治理候选才可记为 `CANDIDATE_ACCEPTED`：

- 1.8 candidate-defining source 已冻结；
- deterministic checks / replay 成立；
- implementation 后 Critic safety gate 给出 `PROCEED_TO_FINAL_EVALUATION`；
- Clear Writing 旧 package 负控按预期被拒绝；
- 新合法 Clear Writing package 完成真实 execution-ready 全量审查；
- 若该包证据足以 PASS，则 atomic PASS 五项在同一回复全部出现；
- 对该合法 PASS 的自然解释 follow-up 行为稳定；
- 没有被发现需要改变 Project setting、Capability Gate Policy 或产品架构。

达到 `CANDIDATE_ACCEPTED` 后，按当前 `AGENTS.md 8.5` 做正式集成：

```text
reviewed/chatgpt-web--pass-integrity
-> fetch current main
-> integration preflight
-> verify no competing change in same Planner/Critic contract area
-> merge task branch into main without force/history rewrite
-> push main
-> fresh readback from remote main
```

fresh readback 至少确认：

- `main:docs/workflows/PLANNER_ROLE_CONTRACT.md` version = 1.8；
- `main:docs/workflows/CRITIC_ROLE_CONTRACT.md` version = 1.8；
- 两份合同内容与 `GOVERNANCE_CANDIDATE_COMMIT` 的冻结合同字节/哈希一致；
- collaboration regression / final evidence locator 与最终候选一致；
- 预期优质 Critic 示例只在真实正向回归成功时记录；
- 没有竞争性 main drift 改写本轮冻结语义。

若 integration conflict、同一合同区域发生竞争修改或 fresh readback 不一致：

`STOP -> Planner/Critic`

不得 force、不得静默重放旧 candidate、不得把“候选通过”误报成“main 已升级”。

本轮不做 repository/plugin release；main integration 即本治理机制的正式生效点。

## 5. PASSINT-V05-02：删除未绑定的额外 implementation review

v0.6 删除独立的 separate implementation Reviewer stage。

理由：当前 package 没有冻结真实 task-scoped Reviewer transport，而 ChatGPT Web 人工协作只应有 Planner 与 Critic。继续保留一个未绑定的 Reviewer 会重新把隐藏角色路由甩给用户。

批准后的实现链改为：

```text
Codex implementation
-> candidate commit freeze
-> local deterministic checks + compatibility replay
-> implementation-after Critic safety gate
-> PROCEED_TO_FINAL_EVALUATION / REVISE
-> Clear Writing two-stage real regression
-> candidate acceptance
-> main integration preflight + merge/push/readback
```

implementation-after Critic 必须直接读取：

- actual diff；
- exact `GOVERNANCE_CANDIDATE_COMMIT`；
- Planner/Critic 1.8 完整文本；
- deterministic replay evidence；
- candidate identity manifest；
- 两阶段 Clear Writing 回归的输入、标准、identity 和停止条件。

该 Critic 只允许：

- `PROCEED_TO_FINAL_EVALUATION`
- `REVISE`

不产生第二个治理 PASS。

只有 `PROCEED_TO_FINAL_EVALUATION` 后才运行 Clear Writing 两阶段真实回归。

## 6. Planner 1.8

在 1.7 基础上只增加：

### 6.1 最终 Critic prompt compatibility preflight

Planner 形成 execution-ready package 时必须确认 task-specific Critic prompt：

- 不缩窄最终全量审查；
- 不改写中央 verdict / `READY_FOR_CODEX` / `NEXT_HANDOFF`；
- 不要求 `NEXT_HANDOFF=USER_AUTHORIZATION`；
- 不省略架构说明；
- 不省略短 `COPY TO CODEX`；
- 不要求全文复制 Kickoff Draft。

任务 prompt 可以强调旧 blocker，但必须明确最终审查仍由最新中央 Critic 合同控制。

### 6.2 短 Codex handoff 可生成性

Planner 送最终审查前必须确认：能够从冻结 Goal、Kickoff、批准定位和授权边界生成一段不猜测、不扩权的短 Codex handoff。做不到则 package 不可送最终审查。

## 7. Critic 1.8

### 7.1 Compatibility hard gate

execution-ready 审查开始时先检查 task prompt 与中央合同。存在冲突则当前 package 不得 PASS，但继续完成当前证据允许的其余审查，尽量一轮报告所有真实 blocker。

### 7.2 Atomic PASS

同一条有效 PASS 必须一次包含五项冻结交付；缺任一项只能 `REVISE`。历史不完整 PASS 不能靠后续消息补齐后追认，只能对同一 exact package 做有界重审。

### 7.3 PASS 后解释稳定性

- 解释请求：依据 approved package 解释，不新增机制；
- 矛盾证据：approved package 无法支持既有承诺，同一 task 回 Planner；
- 新要求：只有用户明确增加冻结范围之外的目标才进入新设计。

## 8. 两阶段 Clear Writing 回归

### 阶段一：负控

固定旧包：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

用 `GOVERNANCE_CANDIDATE_COMMIT` 中的 1.8 审查合同判断。预期必须 `REVISE`，因为旧 task prompt 与中央合同冲突。

### 阶段二：合法正向回归

仅在阶段一通过且 implementation-after Critic 已给 `PROCEED_TO_FINAL_EVALUATION` 后准备。

允许在 Clear Writing 设计分支上只修改：

- task-specific execution-ready Critic prompt；
- 因新 commit 必须同步的 locator/package identity。

不得修改产品 Proposal/Plan/Goal/Runbook/Kickoff 的产品语义、G1-G6 或生产代码。

新的 Clear Writing prompt 必须显式规定：该治理回归的中央审查 authority 是 exact `GOVERNANCE_CANDIDATE_COMMIT` 中的 Critic 1.8，而不是当前 main 1.7。

必须形成新 exact package commit，再做完整 execution-ready review。

若发现真实产品 blocker，正常 `REVISE`；不换题、不强迫 PASS。

## 9. Deterministic replay

保留 8 个 case，不新增数量：

1. old Clear Writing conflicting prompt；
2. PASS missing architecture summary；
3. PASS missing Codex handoff；
4. full Kickoff dump；
5. blocker-priority but full final review；
6. follow-up explanation；
7. contradiction discovered during explanation；
8. explicit new requirement。

全部绑定 `GOVERNANCE_CANDIDATE_COMMIT`。

## 10. 执行与授权边界

若最终 execution-ready Critic 后续给出唯一治理 `PASS / READY_FOR_CODEX=YES`，短 Codex handoff必须把以下 exact execution identity 和范围作为用户实际发送后的授权：

```text
task_key=chatgpt-web--pass-integrity
execution_branch=reviewed/chatgpt-web--pass-integrity
execution_worktree=/tmp/ai-skills-chatgpt-web-pass-integrity
```

授权范围包括：

- 创建上述 exact task branch/worktree；
- 普通 non-force push exact task branch；
- 实施本 Proposal/Plan 的中央文档合同修改和 candidate evidence；
- 满足所有冻结验收后，按 AGENTS 8.5 做 main integration preflight、non-force merge/push、fresh readback；
- 若 approved handoff 明确包括 task branch cleanup，则只在 main fresh readback 成功后做该 exact branch 的普通 cleanup。

不授权：

- force push / history rewrite；
- release；
- Project setting 修改；
- Capability Gate Policy 修改；
- Clear Writing 产品代码/G1-G6 产品语义修改；
- Bridge Kit / Plugin Creator 修改；
- 付费模型调用；
- Personal Plugin mutation。

## 11. Tracking

当前未发现 `chatgpt-web--pass-integrity` 专属 tracking Issue。Issue #13/#99 属于其他对象，不绑定。

按维护看板保留 pending mutation。当前 Planner surface 无法证明同时具备真实 Clear Writing reader-facing copy 检查与 GitHub Project mutation，因此：

- 不创建 reader-facing tracking Issue；
- 不声称 Project 已同步；
- 不要求用户手工维护。

下一次具备合法组合入口的 maintenance action 再 create/bind，并按当时真实 Issue 回写 `tracking: #N`。

## 12. 当前状态

当前只形成 v0.6 Proposal 与完整 execution package；未实施 1.8，未创建 execution branch/worktree，未运行 Clear Writing G1-G6，未修改 main。

下一步：独立 Critic 对 v0.6 完整 execution-ready package 做**最终 execution-ready review**。只有所有 blocker 真正关闭，才允许该轮给唯一 `PASS + READY_FOR_CODEX=YES` 和短 `COPY TO CODEX`。
