# ChatGPT Web PASS 原子交付修复 — v0.6 最终 execution-ready Critic Prompt

你现在担任 AI Research Stack 的独立 Critic，对同一治理任务做最终 execution-ready 审查。

## Active Review Context

```text
target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=ChatGPT Web Planner-Critic governance
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
proposal_path_and_version=docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_6_2026-10-20.md@v0.6
review_stage=FINAL_EXECUTION_READY_REVIEW_V0_6
```

用户会同时提供唯一：

`PACKAGE_COMMIT=<exact package snapshot commit>`

必须从该 exact commit 读取本提示词和全部 v0.6 package 文件；若不是同一快照，直接 REVISE。

本轮是最终 execution-ready 审查。你必须按最新正式 `CRITIC_ROLE_CONTRACT.md` 的完整最终审查合同执行，不能把审查缩成 PASSINT-V05-01/V05-02 closure。

允许的最终结论只有：

- `PASS + READY_FOR_CODEX=YES`
- `REVISE + READY_FOR_CODEX=NO`

若 PASS，按当前中央 Critic 合同直接给出完整用户架构说明和短 `COPY TO CODEX`；不得停在等待用户再索取执行入口。

## 1. 先读取当前正式治理来源

实际读取并核实 `YuukiAS/AI_Skills_Collection` 最新 `main`：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-19.md`
- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`
- `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md`

本轮设计的是 1.8 candidate，但正式 central authority 在实施前仍是 main 上当前合同。不要把 Proposal 中拟议的 1.8 当成已经生效的正式规则；你要判断它是否足以成为批准后的实现目标。

若 main 有无关前进，不机械否定 package；若 Planner/Critic 正式合同或 AGENTS 的相关语义发生变化，必须按当前事实审查兼容性。

## 2. 从 exact PACKAGE_COMMIT 读取完整 v0.6 package

至少完整读取：

- `results/chatgpt-web--pass-integrity/PASS_ATOMIC_DELIVERY_V0_4_CRITIC_REVIEW_2026-10-20.md`
- `results/chatgpt-web--pass-integrity/PASS_ATOMIC_DELIVERY_V0_5_CRITIC_REVIEW_2026-10-20.md`
- `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_6_2026-10-20.md`
- `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_EXECUTION_PLAN_V0_6_2026-10-20.md`
- `docs/goals/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_GOAL_V0_6.md`
- `docs/operations/prompts/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_KICKOFF_DRAFT_V0_6_2026-10-20.md`
- `results/chatgpt-web--pass-integrity/EXECUTION_PACKAGE_V0_6.md`
- 本 v0.6 Critic prompt

不要只审 Proposal。

## 3. 回查真实 Clear Writing 事故证据

从 exact old Clear Writing package：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

至少核实：

- task-specific execution-ready Critic prompt；
- Plan；
- Goal；
- Runbook；
- Kickoff Draft。

确认旧 prompt 确实存在：

- 最终审查被缩成“只复核四个 blocker”；
- `NEXT_HANDOFF=USER_AUTHORIZATION`；
- 没有要求中央 execution-ready PASS 的完整审查与直接短 `COPY TO CODEX`。

不要重新设计 Clear Writing 0.6 产品；这里只把它作为治理事故和后续真实回归对象。

## 4. 先检查本 task-specific Critic prompt 自身是否与中央合同兼容

这是本轮必须实际应用的回归点。

检查本 v0.6 prompt 是否：

- 允许你重新核对完整 Proposal/Plan/Goal/Kickoff，而不是只关旧 blocker；
- 没有改写中央 verdict 语义；
- 没有把 PASS 后下一入口改成 USER_AUTHORIZATION；
- 没有要求省略架构说明或短 Codex handoff；
- 没有要求全文复制 Kickoff；
- 没有把用户授权与 Critic PASS 混为一谈。

若本 prompt 自己仍与当前中央合同冲突，REVISE。

## 5. 完整用户承诺与实际架构审查

重新核对完整承诺，不以旧 finding 清单代替：

### 5.1 Planner 1.8

是否只增加最小必要能力：

- task-specific Critic prompt compatibility preflight；
- short Codex handoff renderability preflight；

同时没有让 Planner 自审或取代 Critic。

### 5.2 Critic 1.8

是否只增加：

- execution-ready compatibility hard gate；
- atomic PASS；
- PASS 后解释 / 矛盾 / 新要求分类；

并保持：
- 中间设计 `PROCEED / REVISE`；
- 唯一 execution-ready PASS；
- implementation 后安全门 `PROCEED_TO_FINAL_EVALUATION / REVISE`；
- 不新增第三人工角色。

### 5.3 正常成功链

必须能完整解释：

```text
用户批准 v0.6
-> Codex 在 exact reviewed branch/worktree 实施 1.8
-> 冻结 GOVERNANCE_CANDIDATE_COMMIT
-> exact candidate deterministic replay
-> post-implementation Critic safety gate
-> Clear Writing old-package negative control
-> new legal Clear Writing positive package
-> full execution-ready Critic regression
-> atomic PASS + explanation follow-up（若产品证据支持 PASS）
-> governance CANDIDATE_ACCEPTED
-> integration preflight
-> main merge/push
-> remote main fresh readback
-> Planner/Critic 1.8 正式生效
```

任何关键阶段若仍只有“以后再决定”，REVISE。

### 5.4 失败与恢复链

检查至少：

- candidate-defining source 改变 -> old evidence 失效；
- deterministic replay fail -> same Codex task 修；
- post-implementation Critic REVISE -> 根据是否改变冻结语义返回 Codex 或 Planner；
- old Clear Writing package 未被拒绝 -> governance candidate FAIL；
- positive Clear Writing review 发现真实产品 blocker -> 同一 Clear Writing task REVISE，不换题追 PASS；
- integration conflict / same-area main drift -> STOP -> Planner/Critic；
- fresh main readback mismatch -> 不得宣称 1.8 已生效；
- 不允许 force/history rewrite。

## 6. PASSINT-V05-01 最终复核：candidate authority + main integration

判断 v0.6 是否真正解决：

1. `GOVERNANCE_CANDIDATE_COMMIT` 的生成时间和 candidate-defining file set 是否清楚；
2. deterministic replay、post-implementation safety gate、Clear Writing stage 1/stage 2、follow-up 是否都明确读取同一个 exact candidate 中的 1.8；
3. current main 1.7 与 candidate 1.8 是否不会混淆；
4. evidence 追加是否不会改变 candidate-defining source；
5. candidate source 改变时旧 evidence 是否明确失效；
6. 达到治理 `CANDIDATE_ACCEPTED` 后是否有真实 main integration path；
7. 是否遵守当前 `AGENTS.md 8.5`：
   - integration preflight；
   - no force；
   - same-area competing change/conflict 不能静默覆盖；
   - merge/push 后 fresh readback；
8. fresh readback 是否足以证明 main 的两个 role contracts 已真正变成 1.8；
9. 本任务不需要额外 release 是否合理。

如果候选验证通过却仍可能永久留在 branch、normal entry 继续读 main 1.7，REVISE。

## 7. PASSINT-V05-02 最终复核：去掉隐藏 implementation Reviewer

确认 v0.6 已删除 separate independent implementation-review stage。

检查 post-implementation Critic safety gate 是否足以直接读取：

- actual diff；
- exact candidate commit；
- Planner/Critic 1.8 完整文本；
- deterministic replay evidence；
- candidate manifest；
- 两阶段 Clear Writing regression contracts / inputs / rubrics / stop conditions。

不得要求用户再手工选择一个未绑定 Reviewer。

如果你认为必须恢复 separate Reviewer，必须证明当前仓库存在 exact task-scoped automatic reviewer locator、transport、evidence path 和 failure recovery；否则不要增加。

## 8. 两阶段 Clear Writing 回归最终复核

### 8.1 阶段一

旧 exact package `d7b810d...` 永久保持不变，并作为 1.8 compatibility negative control。

预期必须 REVISE。

### 8.2 阶段二

只有阶段一和 post-implementation safety gate 通过后，才允许最小修正 Clear Writing task-specific Critic prompt。

检查：

- 只改 prompt / necessary locator/package identity；
- 不改变 Clear Writing 产品 Proposal/Plan/Goal/Runbook/Kickoff 产品语义；
- 不改变 G1-G6；
- 新 prompt 显式绑定 exact `GOVERNANCE_CANDIDATE_COMMIT` 的 Critic 1.8；
- 新 package 有新的 exact commit；
- full execution-ready review 不预设 PASS；
- 若产品有 blocker 正常 REVISE；
- 不能为了治理样本换题、放松标准或强迫 PASS。

## 9. Atomic PASS 与 follow-up 最终复核

判断有效 PASS 五项是否真的是同一回复原子交付：

1. 一屏实际架构说明；
2. exact approved locators；
3. `READY_FOR_CODEX=YES`；
4. `NEXT_HANDOFF=CODEX`；
5. 短 `COPY TO CODEX`。

然后判断 follow-up：

`写入 repo 的文件怎么保证确实走了 Clear Writing？`

是否应按已批准 G3 解释，而不是临时新增 `create_blob` / MCP / App / global gateway；同时若解释本身发现冻结承诺无法成立，是否仍能回 Planner。

## 10. Scope / complexity / authorization

确认没有扩大：

- Project setting：NO CHANGE；
- Capability Gate Policy 1.2：NO CHANGE；
- Clear Writing product / G1-G6：NO CHANGE；
- Bridge Kit：NO CHANGE；
- Plugin Creator：NO CHANGE；
- paid model：NO；
- Personal Plugin mutation：NO；
- release：NO；
- new role/schema/state machine/database/service/watcher/daemon/prompt compiler：NO。

检查 Kickoff Draft 是否把用户未来发送短 Codex handoff后的授权边界冻结为：

```text
task_key=chatgpt-web--pass-integrity
execution_branch=reviewed/chatgpt-web--pass-integrity
execution_worktree=/tmp/ai-skills-chatgpt-web-pass-integrity
```

并且只授权普通 non-force task-branch push 和条件成立后的 main integration，不越权到 release/force/其他产品。

## 11. Tracking

核对 Maintenance Board。

当前证据是：
- 没有找到本任务专属 tracking Issue；
- Issue #13/#99 属于其他对象；
- 当前 Planner surface 无法证明同时具备真实 Clear Writing reader-facing copy 检查与 GitHub Project mutation；
- 因此保持 exact pending mutation，不要求用户手工维护，不声称已同步。

若你发现当前事实不同，给 exact evidence；否则不要把 tracking tool 不可用变成本设计 blocker。

## 12. 外部核查

做少量针对性官方核查，只验证：
- higher-level contract 与 lower-level task prompt 冲突时的优先级/兼容性处理；
- Git/main integration 的普通成熟安全边界。

不要引入外部代理框架或新控制系统。

## 13. Verdict

只有以下全部成立，才可给唯一：

```text
PASS
READY_FOR_CODEX=YES
```

- 当前 v0.6 task prompt 与中央合同兼容；
- PASSINT-V04-01 继续 CLOSED；
- PASSINT-V05-01 CLOSED；
- PASSINT-V05-02 CLOSED；
- Proposal/Plan/Goal/Kickoff 一致；
- candidate authority 与 main integration 闭合；
- 没有隐藏 implementation Reviewer；
- deterministic replay 与两阶段真实回归完整；
- failure/recovery 与授权闭合；
- Codex 只剩普通实现细节；
- 无需再做产品/架构/权限/验收/恢复决定。

否则：

```text
REVISE
READY_FOR_CODEX=NO
```

只阻塞真实风险，给最小关闭条件。

## 14. PASS 回复必须直接完成中央交付合同

若 PASS，你的回复本身必须按最新中央 Critic 合同一次完成：

- 先用一屏自然中文讲清：
  - 本次批准的实际治理架构；
  - Planner/Critic 1.8 与 1.7 的真实差异；
  - candidate 怎样验证；
  - 怎样正式进入 main；
  - 主要失败/恢复边界；
  - 这次 PASS 不证明什么；
- 再给 exact approved locators；
- `READY_FOR_CODEX=YES`；
- `NEXT_HANDOFF=CODEX`；
- 最后直接给简短、可复制的 `COPY TO CODEX`。

`COPY TO CODEX` 只能引用批准 Proposal/Plan/Goal/Kickoff/package，外加 exact branch/worktree、当前授权和 stop condition；不得全文倾倒 Kickoff Draft。

若 REVISE：
- 给 `NEXT_HANDOFF=PLANNER`；
- 自动生成完整 `COPY TO PLANNER`；
- 不让用户自己拼 prompt。

本轮不得实施、不得创建 execution branch/worktree、不得修改 main、不得运行 Clear Writing G1-G6、不得启动 Codex。
