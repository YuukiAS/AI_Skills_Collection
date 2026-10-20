# ChatGPT Web PASS 原子交付修复 — Execution Plan v0.5

日期：2026-10-20  
任务键：`chatgpt-web--pass-integrity`  
Proposal：`docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_5_2026-10-20.md@afc19a46bf53d9f8841dee0cc9ec42fe17c41365`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
候选执行分支：`reviewed/chatgpt-web--pass-integrity`  
阶段：execution package draft；需要独立 Critic；当前 `READY_FOR_CODEX=NO`

## 1. 目标

只实施 Planner/Critic 1.8 的中央治理修复，并用两阶段 Clear Writing 回归证明：

- 冲突的 task-specific Critic prompt 会被硬性拒绝；
- 合法 execution-ready package 获得 PASS 时，Critic 会一次交齐架构说明与短 Codex handoff；
- PASS 后的普通解释请求不会触发无依据的重新设计。

本任务不修改 Project setting、Capability Gate Policy、Clear Writing 产品架构、Bridge Kit 或 Plugin Creator。

## 2. 正式修改文件

中央候选只允许修改：

1. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
2. `docs/workflows/CRITIC_ROLE_CONTRACT.md`
3. `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`
4. `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md`
5. `results/chatgpt-web--pass-integrity/**`

版本：
- Planner Role Contract 1.7 → 1.8
- Critic Role Contract 1.7 → 1.8
- Capability Gate Policy：保持 1.2
- Project setting：NO CHANGE

README checked: no update required。

## 3. Planner 1.8 精确改动

在现有 execution-ready package / Critic prompt 生成职责中加入：

### 3.1 Task-prompt compatibility preflight

最终 Critic prompt 在交付前必须逐项确认：

- 中央 Critic 合同仍拥有 verdict 语义；
- 中央合同仍拥有 `READY_FOR_CODEX` 语义；
- 中央合同仍拥有下一 handoff 与 PASS 输出合同；
- task prompt 没有把最终审查缩成上一轮 blocker closure；
- task prompt 没有要求 `NEXT_HANDOFF=USER_AUTHORIZATION`；
- task prompt 没有删除架构说明或 `COPY TO CODEX`；
- task prompt 没有要求全文复制 Kickoff Draft。

task prompt 可以要求优先复核旧 finding，但必须明确最终 execution-ready 仍按最新中央合同全量审查。

### 3.2 Handoff renderability preflight

Planner 在送最终 Critic 前必须验证：从当前 Goal、Kickoff Draft、批准定位和授权边界可以生成一段短、可直接发送、不会新增授权的 Codex handoff。

若不能做到，package 尚未 execution-ready。

## 4. Critic 1.8 精确改动

### 4.1 Compatibility hard gate

execution-ready 审查开始先检查 task prompt 与中央合同。

若冲突：
- package 当前不得 PASS；
- 记录兼容性 blocker；
- 继续完成当前证据允许的其余实质审查；
- 一轮尽量报告全部 blocker。

不得通过“中央合同优先，所以忽略低层冲突”直接 PASS。

### 4.2 Atomic PASS

有效 execution-ready PASS 的同一回复必须同时包含：

1. 一屏自然中文实际架构说明；
2. exact approved locators；
3. `READY_FOR_CODEX=YES`；
4. `NEXT_HANDOFF=CODEX`；
5. 短 `COPY TO CODEX`。

缺任一项时只能 `REVISE`。

历史上已经输出的不完整 PASS 不能靠后续消息补齐后追认；只能对同一 exact package 重新审查。

### 4.3 PASS 后问题分类

收到 PASS 后 follow-up 时先判：

- **解释请求**：依据 approved package 解释；
- **矛盾证据**：approved package 无法支持其已批准承诺，旧批准相应失效，同 task 回 Planner；
- **新要求**：用户明确增加冻结范围之外的目标，才进入新设计。

矛盾可以由 Critic 自己在解释过程中发现。

## 5. 确定性兼容性回放

实现后保存：

`results/chatgpt-web--pass-integrity/v1_8_contract_replay/`

至少包含八个 case：

1. `CW_OLD_PROMPT_CONFLICT`  
   输入旧 Clear Writing prompt @ `d7b810d...`；期望 REVISE。
2. `PASS_WITHOUT_ARCHITECTURE_SUMMARY`  
   字段齐全但缺架构说明；期望无有效 PASS。
3. `PASS_WITHOUT_CODEX_HANDOFF`  
   缺 `NEXT_HANDOFF=CODEX/COPY TO CODEX`；期望无有效 PASS。
4. `FULL_KICKOFF_DUMP`  
   全文复制 Kickoff；期望不符合 PASS 合同。
5. `BLOCKER_PRIORITY_WITH_FULL_REVIEW`  
   prompt 优先看旧 blocker但明确全量最终审查；应兼容。
6. `FOLLOWUP_EXPLANATION`  
   只解释 approved mechanism；不得重开架构。
7. `FOLLOWUP_CONTRADICTION_DISCOVERED`  
   解释时发现冻结承诺无法成立；应回 Planner。
8. `FOLLOWUP_NEW_REQUIREMENT`  
   用户明确提出更强目标；应识别为新设计。

回放只验证合同语义，不用关键词命中代替人工语义检查。

## 6. 两阶段 Clear Writing 最终回归

### 6.1 阶段一：负控

固定：

`OLD_PACKAGE=d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

不修改。

使用 1.8 contract replay 明确证明它因 prompt 冲突不能 PASS。

成功证据至少记录：
- 旧 prompt 冲突原文；
- 中央 1.8 条款；
- 预期与实际 verdict；
- 不因中央优先级而忽略 package 内冲突。

### 6.2 阶段二：合法正向回归 package

只有阶段一通过后才准备。

目标分支：
`design/clear-writing--single-entry-artifact-finalization`

允许修改：
- 仅 task-specific execution-ready Critic prompt；
- 以及因新 commit 必须机械同步的 locator / package identity。

产品 Proposal/Plan/Goal/Runbook/Kickoff 的产品语义保持冻结；若任何产品语义必须改变，停止本治理回归，回 Clear Writing Planner。

新 prompt 必须：

- 不自行定义 verdict/output/next handoff；
- 引用最新 `CRITIC_ROLE_CONTRACT.md` 作为最终审查合同；
- 要求完整稳定用户承诺 + Proposal/Plan/Goal/Kickoff + 正常成功/失败/恢复链全量复核；
- 可以把 ER01/05/08/09 作为历史重点，但不能限制审查范围。

形成新的 exact package commit `CW_POSITIVE_PACKAGE_COMMIT`。

然后由独立 Critic执行真实 execution-ready review。

### 6.3 正向回归不预设 PASS

若完整审查发现新的产品 blocker：
- verdict = REVISE；
- 留在 `clear-writing--single-entry-artifact-finalization` 修复；
- 本治理最终正向回归保持 PENDING；
- 不换题、不换 package 追求 PASS。

只有合法 package 真实满足条件时，才允许一次 PASS。

### 6.4 PASS 输出验收

若 PASS，保存完整回复并检查五项原子交付全部在同一回复。

随后用户发自然 follow-up：

`写入 repo 的文件怎么保证确实走了 Clear Writing？`

预期只解释冻结 G3：
全文读取 → 完整终审候选 → 写前 identity 复核 → 写入 → 回读 → 与 candidate 一致 → 全文质量审查。

不得新增 `create_blob`、MCP、App、全局写入网关或新 Gate。

## 7. 实施后审查顺序

1. Codex 实施 1.8 中央合同；
2. 独立 implementation review；
3. deterministic compatibility replay；
4. implementation 后 Critic pre-final safety gate：`PROCEED_TO_FINAL_EVALUATION / REVISE`；
5. Clear Writing 阶段一负控；
6. 机械准备新合法 Clear Writing prompt/package；
7. Clear Writing execution-ready 全量 Critic review；
8. 若真实 PASS，再运行解释 follow-up；
9. 只有证据全部成立，治理任务恢复 `CANDIDATE_ACCEPTED`；
10. 把该真实 PASS 加入优质 Critic 示例。

## 8. 停止条件

任何以下情况停止并回 Planner：

- 1.8 需要修改 Project setting 或 Capability Gate Policy 才能成立；
- 需要新增角色、状态机、服务、数据库、watcher 或 prompt compiler；
- Clear Writing 正向 package 需要修改产品架构/Gate/recovery 语义；
- compatibility replay 无法稳定区分旧冲突 prompt 与合法 prompt；
- 短 Codex handoff 无法在不猜测/不扩权下生成。

普通文档实现错误留在同一 Codex task 修复。

## 9. 授权边界

execution-ready Critic PASS 前：
- 不创建 execution branch/worktree；
- 不实施 1.8；
- 不修改 Clear Writing 分支；
- 不运行真实 Clear Writing G1-G6；
- 不修改 Personal Plugin；
- 不修改 Project setting；
- 不做付费调用。

后续唯一 execution-ready PASS 只授权本 Plan 的中央合同实现与冻结回放准备，不自动授权 Clear Writing 0.6 产品发布。

## 10. Tracking pending

当前未发现可复用 tracking Issue。当前 surface 无法满足“实际 Clear Writing 调用 + GitHub Project mutation”组合，因此不创建 reader-facing Issue。

后续具备能力的 maintenance action 应创建/bind：
- title：`Planner/Critic PASS 原子交付与提示词兼容性`
- label：`maintenance-track`
- Area：`repo`
- Status：`DOING`
- current anchor：本 v0.5 execution package
- next：独立 Critic review
并按 board policy 回写真实 `tracking: #N`。
