# Canonical Goal v0.5 — chatgpt-web--pass-integrity

## 目标

将 ChatGPT Web Planner/Critic 治理升级到 1.8，使 execution-ready `PASS` 成为一次不可拆分的完整交付，并让任务专用 Critic prompt 不能覆盖中央审查合同。

## 用户可观察结果

完成后，复杂任务的最终 Critic 若给 `PASS`，同一条回复必须一次交齐：

- 一屏自然中文实际架构说明；
- 精确批准对象；
- `READY_FOR_CODEX=YES`；
- `NEXT_HANDOFF=CODEX`；
- 可直接发送的短 `COPY TO CODEX`。

用户不再需要追问“架构到底是什么”“Codex prompt 在哪里”。

任务专用 prompt 若缩小最终审查、改写 verdict、改写下一 handoff 或省略上述交付，当前 package 必须 `REVISE`。

## 必须实现

1. Planner Role Contract 1.8：
   - 最终 Critic prompt compatibility preflight；
   - short Codex handoff renderability preflight。
2. Critic Role Contract 1.8：
   - execution-ready compatibility hard gate；
   - atomic PASS；
   - PASS 后解释/矛盾/新要求分类。
3. 保存 deterministic compatibility replay。
4. 使用 Clear Writing 0.6 做两阶段真实回归：
   - old conflicting package 作为负控，必须 REVISE；
   - 新的最小兼容 package 作为真实正向 execution-ready 回归。
5. 若正向 package 真正 PASS，验证后续解释请求只解释冻结 G3，不临场加重架构。

## 明确不做

- 不修改 AI Research Stack Project setting；
- 不修改 Capability Gate Policy 1.2；
- 不重新设计 Clear Writing 0.6；
- 不修改 Clear Writing 产品代码或 G1-G6 产品语义；
- 不修改 Bridge Kit 或 Plugin Creator；
- 不新增角色、schema、状态机、数据库、服务、watcher、daemon 或 prompt compiler。

## 正向回归纪律

旧 package `d7b810d194ead881303aaca9c2e4f1d59a97c1f1` 永远只作为冲突负控。

正向回归必须先生成新的 exact Clear Writing package commit，且其产品语义保持冻结，只修 task-specific Critic prompt 的中央兼容性与必要 locator。

正向回归不预设 PASS。若完整审查发现产品 blocker，必须正常 REVISE 并留在原 Clear Writing task 修复。

## 完成条件

治理任务只有在以下全部成立后才重新记录 `CANDIDATE_ACCEPTED`：

- 1.8 实现与独立 implementation review 通过；
- 旧冲突 package 被兼容性硬门正确拒绝；
- 新合法 Clear Writing package 完成全量 execution-ready 审查；
- 若证据支持 PASS，同一回复五项原子交付全部出现；
- PASS 后解释 follow-up 稳定，不无依据新增机制；
- 优质 PASS 示例与协作回归记录按真实证据更新。

README checked: no update required。
