# ChatGPT Web PASS 原子交付与正式集成闭环 — Execution Plan v0.6

日期：2026-10-20  
任务键：`chatgpt-web--pass-integrity`  
Proposal：`docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_6_2026-10-20.md@12fd55d24022410b3a03376af0c610bc41446166`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
执行分支：`reviewed/chatgpt-web--pass-integrity`  
执行工作树：`/tmp/ai-skills-chatgpt-web-pass-integrity`  
当前阶段：execution package draft；`READY_FOR_CODEX=NO`

## 1. 本轮完成定义

本任务只完成 Planner/Critic 1.8 中央治理升级，并证明：

1. task-specific Critic prompt 不能覆盖中央 execution-ready 合同；
2. 有效 PASS 一次交齐架构说明与 Codex handoff；
3. PASS 后普通解释请求不会触发无依据重设计；
4. 1.8 候选先在 exact candidate commit 上验证，再按 `AGENTS.md 8.5` 正式集成到 main；
5. main fresh readback 直接证明正常入口已经实际升级到 1.8。

## 2. 实施文件范围

中央 candidate-defining source 只允许修改：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`
- `results/chatgpt-web--pass-integrity/GOVERNANCE_CANDIDATE_MANIFEST.md`
- `results/chatgpt-web--pass-integrity/v1_8_contract_replay/CONTRACT.md`
- `results/chatgpt-web--pass-integrity/clear-writing-positive-regression/CONTRACT.md`

只有真实正向 PASS 回归成功后，才允许更新：

- `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md`
- 最终 collaboration regression 收口段落；
- 对应 final evidence/result 文件。

不修改：
- Project setting；
- `PLUGIN_CAPABILITY_GATE_POLICY.md`；
- Clear Writing 产品 Proposal/Plan/Goal/Runbook/Kickoff 的产品语义；
- Clear Writing 生产代码；
- Bridge Kit；
- Plugin Creator；
- README。

Repository bump：NONE。  
Central plugin bump：NONE。  
README checked: no update required。

## 3. Planner Role Contract 1.8

在 1.7 原有规则上新增且仅新增：

### P18-1 最终 task prompt compatibility preflight

Planner 在形成 execution-ready Critic prompt 时，必须确认：

- 最终审查仍由最新中央 Critic 合同控制；
- task prompt 只提供当前任务事实、locators、风险重点和历史 finding；
- task prompt 不得把最终审查缩成旧 blocker closure；
- task prompt 不得改写 `PASS/REVISE`、`READY_FOR_CODEX`、`NEXT_HANDOFF`；
- task prompt 不得要求 `NEXT_HANDOFF=USER_AUTHORIZATION`；
- task prompt 不得省略实际架构说明或短 `COPY TO CODEX`；
- task prompt 不得要求全文复制 Kickoff Draft。

若发现冲突，Planner 必须先修 task prompt，不能送最终审查后依赖 Critic自行解释优先级。

### P18-2 short handoff renderability preflight

Planner 在送最终审查前，必须从冻结 Proposal/Plan/Goal/Kickoff 与授权边界实际构造一份短 Codex handoff 草案并检查：

- 不猜测；
- 不新增权限；
- 不复制批准前控制面；
- 包含 exact task、approved locators、执行定位、当前授权和 stop condition。

若做不到，execution package 尚未闭合。

## 4. Critic Role Contract 1.8

### C18-1 task-prompt compatibility hard gate

execution-ready 审查开始时先核对 task-specific prompt 与中央合同。

冲突存在时：

- 当前 package 不得 PASS；
- 记录 compatibility blocker；
- 继续完成当前证据允许的其他实质审查；
- 尽量一轮报告全部真实 blocker。

不得通过“中央合同优先，所以忽略 package 内冲突”直接 PASS。

### C18-2 atomic PASS

同一条有效 execution-ready PASS 回复必须一次包含：

1. 一屏自然中文实际架构说明；
2. exact approved locators；
3. `READY_FOR_CODEX=YES`；
4. `NEXT_HANDOFF=CODEX`；
5. 短 `COPY TO CODEX`。

缺任一项时不得先 PASS。历史不完整 PASS 不能靠后续消息补齐追认；只能对同一 exact package 重新审查。

### C18-3 PASS 后 follow-up 分类

- 解释请求：依据 approved package 解释，不新增机制；
- 矛盾证据：若 approved package 无法支持已批准承诺，同一 task 回 Planner；
- 新要求：用户明确增加冻结范围之外的目标时才进入新设计。

Critic 在解释过程中自行发现的真实矛盾同样属于第二类。

## 5. GOVERNANCE_CANDIDATE_COMMIT

### 5.1 生成

Codex 完成 1.8 source 修改、candidate regression contracts 与 candidate manifest 后，先提交一次 candidate-defining commit。

必须记录：

`GOVERNANCE_CANDIDATE_COMMIT=<exact sha>`

并写入：

`results/chatgpt-web--pass-integrity/GOVERNANCE_CANDIDATE_MANIFEST.md`

manifest 至少包含：

- exact commit；
- Planner contract path/version/hash；
- Critic contract path/version/hash；
- collaboration regression candidate hash；
- replay contract hash；
- Clear Writing two-stage regression contract hash；
- source branch；
- current base main；
- candidate-defining file allowlist。

### 5.2 冻结

从 candidate freeze 开始：

- candidate-defining source 不再改变；
- 后续 evidence 可以追加；
- 每份 evidence 必须记录 `governance_candidate_commit`；
- 若 candidate-defining source 改变，旧 evidence 失效，必须生成新 candidate commit 并重跑受影响验证。

### 5.3 authority

以下验证一律从 `GOVERNANCE_CANDIDATE_COMMIT` 读取 1.8，不读取 main 1.7 冒充候选：

- deterministic/local checks；
- 8-case contract replay；
- implementation-after Critic safety gate；
- Clear Writing 旧包负控；
- Clear Writing 新包 execution-ready Critic review；
- PASS 后解释 follow-up。

## 6. 本地与 deterministic checks

Codex 在冻结 candidate 后，针对 exact candidate commit 完成：

- git diff / scope check；
- role contract version/content check；
- Project setting 未修改证明；
- Capability Gate Policy 未修改证明；
- forbidden-path diff check；
- 8-case contract replay；
- candidate manifest/hash consistency；
- exact base/main/branch identity receipt。

输出写入：

`results/chatgpt-web--pass-integrity/v1_8_contract_replay/`

八个 case 保持 v0.5 原定义，不新增固定数量。

## 7. Implementation 后 Critic safety gate

本轮没有 separate implementation Reviewer。

独立 Critic 直接读取：

- exact `GOVERNANCE_CANDIDATE_COMMIT`；
- actual diff；
- Planner/Critic 1.8 完整文本；
- candidate manifest；
- deterministic/local check evidence；
- 8-case replay evidence；
- Clear Writing 两阶段回归 contract、input identities、rubric 与 stop conditions。

只允许：

- `PROCEED_TO_FINAL_EVALUATION`
- `REVISE`

若 REVISE：
- 冻结语义未变的普通实现/doc 错误回同一 Codex task 修；
- 若必须改变冻结治理语义，回 Planner。

只有 `PROCEED_TO_FINAL_EVALUATION` 后进入两阶段 Clear Writing 真实回归。

## 8. Clear Writing 两阶段真实回归

### 8.1 第一阶段：旧包负控

固定输入：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

使用 exact `GOVERNANCE_CANDIDATE_COMMIT` 中 Critic 1.8 作为中央审查 authority。

必须得到 `REVISE`，并明确指出旧 task-specific prompt 至少存在：

- 最终审查被限制为四个旧 blocker；
- `NEXT_HANDOFF=USER_AUTHORIZATION`；
- 缺中央原子 PASS 输出合同。

若旧包仍能 PASS，治理 candidate FAIL。

### 8.2 第二阶段：新合法正向 package

第一阶段通过后，在：

`design/clear-writing--single-entry-artifact-finalization`

仅修改：

- task-specific execution-ready Critic prompt；
- 因新 commit 必须同步的 package/locator identity。

不得修改：

- Clear Writing 产品 Proposal；
- Plan；
- Goal；
- Runbook；
- Kickoff 的产品语义；
- G1-G6；
- 生产代码。

新的 task prompt 必须写明：

- 中央 execution-ready review authority = `GOVERNANCE_CANDIDATE_COMMIT` 中 Critic 1.8；
- 本 prompt 只补 Clear Writing task facts / locators / historical focus；
- verdict、完整审查范围、PASS 输出、下一接收方由中央合同决定；
- 最终 Critic 必须重新核对完整稳定用户承诺、Proposal/Plan/Goal/Kickoff、正常成功链、关键失败与恢复。

形成新的：

`CW_POSITIVE_PACKAGE_COMMIT=<exact sha>`

然后由独立 Critic 做完整 execution-ready review。

不预设 PASS。若发现真实产品 blocker，正常 `REVISE` 并留在同一 Clear Writing task；本治理 positive regression 保持 PENDING。

### 8.3 atomic PASS 验收

若新合法 Clear Writing package 真正获得 PASS，保存整条回复并验证同一回复内：

- 架构说明存在且足以回答正常用户使用；
- approved locators 精确；
- `READY_FOR_CODEX=YES`；
- `NEXT_HANDOFF=CODEX`；
- 短 `COPY TO CODEX` 可直接发送。

缺一项，正向回归失败。

### 8.4 follow-up

随后使用自然问题：

`写入 repo 的文件怎么保证确实走了 Clear Writing？`

合格结果只解释 approved G3：

全文读取 → 完整终审候选 → 写前 identity 复核 → 写入 → 回读 → 与 candidate 一致 → 全文质量审查。

不得临场新增 `create_blob`、MCP、App、全局网关或新 Gate。

## 9. CANDIDATE_ACCEPTED

只有以下全部成立才记录治理 candidate：

`CANDIDATE_ACCEPTED`

- candidate source identity 冻结；
- deterministic checks/replay PASS；
- post-implementation Critic = `PROCEED_TO_FINAL_EVALUATION`；
- Clear Writing 第一阶段旧包被拒绝；
- 第二阶段新合法 package 完成全量审查；
- 若其证据支持 PASS，则 atomic PASS 五项齐全；
- follow-up 稳定；
- 无需改变 Project setting、Capability Gate Policy 或产品架构。

如果第二阶段因真实 Clear Writing 产品 blocker REVISE，则治理 task 不换题，不伪造 positive PASS；等待 Clear Writing 同 task 修复后继续。

## 10. 正式 main integration

达到 `CANDIDATE_ACCEPTED` 后执行：

1. `git fetch origin main`；
2. 核对 current remote main 与 candidate base 的差异；
3. 检查 Planner/Critic contract、collaboration regression、example/result 相关区域是否有竞争修改；
4. 若无冲突，按当前仓库规则把 `reviewed/chatgpt-web--pass-integrity` 合入 main；
5. 普通 non-force push main；
6. 从 remote main fresh read：
   - Planner contract version == 1.8；
   - Critic contract version == 1.8；
   - 两份合同内容/hash 与 candidate freeze 一致；
   - final regression/evidence locator 存在且绑定同一 candidate；
   - 正向 PASS 示例只在真实成功后出现；
7. 记录 integration commit / remote main tip；
8. 只有 fresh readback 成功才可宣称 1.8 正式生效。

若 integration conflict、同合同区域竞争修改或 fresh readback 不一致：

`STOP -> Planner/Critic`

不得 force、rebase rewrite 或静默丢弃 main 变化。

不做 release。

## 11. 执行授权 envelope

最终用户实际发送 approved Codex handoff 后，授权限定为：

```text
task_key=chatgpt-web--pass-integrity
execution_branch=reviewed/chatgpt-web--pass-integrity
execution_worktree=/tmp/ai-skills-chatgpt-web-pass-integrity
target_repo=YuukiAS/AI_Skills_Collection
```

允许：
- 创建 exact branch/worktree；
- normal non-force push exact task branch；
- 修改本 Plan allowlist；
- 产生 candidate/evidence；
- 满足全部条件后 main integration preflight + ordinary merge/push + fresh readback。

禁止：
- force/history rewrite；
- release；
- paid model calls；
- Personal Plugin mutation；
- Project setting 修改；
- Capability Gate Policy 修改；
- Clear Writing 产品代码/Gate 语义修改；
- Bridge Kit/Plugin Creator 修改。

## 12. Tracking pending

仍未发现本任务专属 tracking Issue。Issue #13/#99 不属于本任务。

当前 surface 缺少真实 Clear Writing reader-facing mutation + GitHub Project mutation 组合入口，因此只保留 exact pending mutation，不要求用户手工维护，不声称已同步。

## 13. 当前阶段 stop

当前 execution-ready Critic PASS 前：

- 不创建 execution branch/worktree；
- 不实施 1.8；
- 不运行 replay；
- 不修改 Clear Writing branch；
- 不运行 Clear Writing G1-G6；
- 不合并 main；
- 不启动 Codex。
