# Kickoff Draft v0.6 — chatgpt-web--pass-integrity

状态：DRAFT ONLY；当前未授权实施。

## Authority

- Proposal:
  `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_6_2026-10-20.md`
- Execution Plan:
  `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_EXECUTION_PLAN_V0_6_2026-10-20.md`
- Canonical Goal:
  `docs/goals/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_GOAL_V0_6.md`
- Critic review history:
  `results/chatgpt-web--pass-integrity/PASS_ATOMIC_DELIVERY_V0_5_CRITIC_REVIEW_2026-10-20.md`

只有同一独立 Critic 对完整 v0.6 execution package 给出唯一：

```text
PASS
READY_FOR_CODEX=YES
```

并由用户实际发送批准后的短 `COPY TO CODEX`，才允许执行。

## Exact execution identity

```text
repo=YuukiAS/AI_Skills_Collection
task_key=chatgpt-web--pass-integrity
execution_branch=reviewed/chatgpt-web--pass-integrity
execution_worktree=/tmp/ai-skills-chatgpt-web-pass-integrity
```

用户发送批准后的短 handoff，即授权：

- 创建上述 exact branch/worktree；
- 普通 non-force push exact task branch；
- 在本批准范围内实现 Planner/Critic 1.8；
- 生成本任务 candidate/evidence；
- 全部冻结验收成立后，按当前 AGENTS.md 8.5 做 main integration preflight、ordinary merge/push 和 fresh readback。

不授权 force push、history rewrite、release、付费模型调用、Personal Plugin mutation、Project setting 修改、Capability Gate Policy 修改、Clear Writing 产品代码/G1-G6 产品语义修改、Bridge Kit 或 Plugin Creator 修改。

## Phase 1 — implement Planner/Critic 1.8

只修改 Execution Plan allowlist。

Planner 1.8 必须增加：
- task-specific execution-ready Critic prompt compatibility preflight；
- short Codex handoff renderability preflight。

Critic 1.8 必须增加：
- execution-ready compatibility hard gate；
- atomic PASS 五项同回复交付；
- PASS 后解释 / 矛盾 / 新要求分类。

不得改变 1.7 中其他已冻结角色边界。

## Phase 2 — freeze governance candidate

实现 candidate-defining source 后提交一次 exact commit，并生成：

`results/chatgpt-web--pass-integrity/GOVERNANCE_CANDIDATE_MANIFEST.md`

冻结：

`GOVERNANCE_CANDIDATE_COMMIT=<exact sha>`

manifest 必须记录：
- Planner 1.8 path/version/hash；
- Critic 1.8 path/version/hash；
- collaboration regression candidate；
- replay contract；
- Clear Writing two-stage regression contract；
- candidate-defining file allowlist；
- base main；
- exact task branch。

冻结后 candidate-defining source 不再改变；后续 evidence 只能追加并显式绑定该 commit。若 contract source 改变，旧 evidence 失效。

## Phase 3 — deterministic/local checks

针对 exact `GOVERNANCE_CANDIDATE_COMMIT` 运行并记录：

- scope/diff check；
- role contract version/hash check；
- Project setting unchanged；
- Capability Gate Policy unchanged；
- forbidden path unchanged；
- candidate manifest consistency；
- 8-case compatibility replay。

8 case 固定为：

1. old Clear Writing conflicting prompt；
2. PASS without architecture summary；
3. PASS without Codex handoff；
4. full Kickoff dump；
5. blocker priority + full final review；
6. follow-up explanation；
7. contradiction discovered during explanation；
8. explicit new requirement。

不得为凑数量新增 case。

## Phase 4 — post-implementation Critic safety gate

没有 separate implementation Reviewer。

把以下 evidence 交给独立 Critic：

- actual diff；
- exact `GOVERNANCE_CANDIDATE_COMMIT`；
- Planner/Critic 1.8 完整文本；
- deterministic replay；
- candidate manifest；
- Clear Writing 两阶段 regression contract、inputs、rubric、stop conditions。

该 Critic 只允许：

```text
PROCEED_TO_FINAL_EVALUATION
或
REVISE
```

只有 `PROCEED_TO_FINAL_EVALUATION` 后进入 Phase 5。

若只是批准范围内实现/doc bug，继续同一 Codex task 修；若必须改变冻结治理语义，停止并回 Planner。

## Phase 5 — Clear Writing stage 1 negative control

固定旧包：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

使用 exact `GOVERNANCE_CANDIDATE_COMMIT` 中的 Critic 1.8 审查合同。

预期必须 `REVISE`，因为旧 task-specific prompt：

- 把最终审查缩成四个旧 blocker；
- 使用 `NEXT_HANDOFF=USER_AUTHORIZATION`；
- 缺少中央 atomic PASS 输出合同。

若旧包仍能 PASS：停止，治理 candidate FAIL。

## Phase 6 — Clear Writing stage 2 positive execution-ready regression

只有 Phase 5 成立后，才允许对：

`design/clear-writing--single-entry-artifact-finalization`

做最小 review-package compatibility repair。

允许修改：
- task-specific execution-ready Critic prompt；
- 因新 commit 必须同步的 locator/package identity。

不得修改：
- Clear Writing 产品 Proposal；
- Plan；
- Goal；
- Runbook；
- Kickoff 的产品语义；
- G1-G6；
- production code。

新的 prompt 必须把 exact：

`GOVERNANCE_CANDIDATE_COMMIT`

作为本次治理回归的中央 Critic 1.8 authority，并明确 task prompt 只补 Clear Writing task facts/locators/historical focus，不能定义最终 verdict、PASS 输出或 next handoff。

形成：

`CW_POSITIVE_PACKAGE_COMMIT=<exact sha>`

再交独立 Critic 做完整 execution-ready review。

不预设 PASS。发现真实 Clear Writing 产品 blocker就正常 REVISE，保留同一 Clear Writing task，不换题追 PASS。

## Phase 7 — atomic PASS + explanation regression

若新合法 Clear Writing package 真正得到 PASS，必须在同一回复检查：

1. 一屏实际架构说明；
2. exact approved locators；
3. `READY_FOR_CODEX=YES`；
4. `NEXT_HANDOFF=CODEX`；
5. 可直接发送的短 `COPY TO CODEX`。

然后使用自然 follow-up：

`写入 repo 的文件怎么保证确实走了 Clear Writing？`

合格回答只解释 approved G3：

全文读取
→ 完整终审候选
→ 写前 identity 复核
→ 写入
→ 回读
→ 与 candidate 一致
→ 全文质量审查

不得临时新增 `create_blob`、MCP、App、全局网关或新 Gate。

## Phase 8 — governance candidate acceptance

只有 Proposal/Plan 冻结的所有治理回归成立后，记录：

`CANDIDATE_ACCEPTED`

若 Clear Writing stage 2 因真实产品 blocker REVISE，本治理 task 保持未完成，等待同一 Clear Writing task 修复；不得换样本或强迫 PASS。

## Phase 9 — main integration

达到 `CANDIDATE_ACCEPTED` 后：

1. `git fetch origin main`；
2. integration preflight：
   - current main identity；
   - task branch diff；
   - required evidence；
   - 同一 Planner/Critic contract 区域是否有竞争修改；
3. 无冲突时 ordinary merge task branch -> main；
4. ordinary non-force push main；
5. remote-main fresh readback；
6. 直接确认：
   - Planner Role Contract version = 1.8；
   - Critic Role Contract version = 1.8；
   - 两份合同 hash 与 `GOVERNANCE_CANDIDATE_COMMIT` 冻结值一致；
   - regression/example/final evidence locator 与同一 candidate 对齐；
7. 记录 integration commit 和 remote main tip。

若 merge conflict、同合同区域竞争修改或 fresh readback 不一致：

`STOP -> Planner/Critic`

不得 force、history rewrite 或静默丢弃 main 变化。

本任务不做 release。

## Completion

只有 remote main fresh readback 成立后，才允许声明：

- Planner/Critic 1.8 正式生效；
- 正常 Project 后续读取 main 时将获得 1.8。

README checked: no update required。
