# Canonical Goal v0.6 — chatgpt-web--pass-integrity

## 目标

把 ChatGPT Web Planner/Critic 治理从 1.7 升级为 1.8，并让该候选先在一个冻结的 exact commit 上完成完整验证，再正式集成到 `main`，使正常入口真正加载 1.8。

## 用户最终应得到的行为

当未来复杂任务真正达到 execution-ready：

- task-specific Critic prompt 不能缩窄中央最终审查；
- Critic 若给唯一 `PASS`，同一回复必须一次交齐：
  1. 一屏实际架构说明；
  2. exact approved locators；
  3. `READY_FOR_CODEX=YES`；
  4. `NEXT_HANDOFF=CODEX`；
  5. 可直接发送的短 `COPY TO CODEX`；
- 用户不再追问“架构到底怎么工作”“Codex prompt 在哪里”；
- PASS 后普通解释请求只解释 approved package；真实矛盾回原 task Planner；用户明确提出更强目标才进入新设计。

## 必须实现

1. Planner Role Contract 1.8：
   - task-specific Critic prompt compatibility preflight；
   - short Codex handoff renderability preflight。
2. Critic Role Contract 1.8：
   - execution-ready task-prompt compatibility hard gate；
   - atomic PASS；
   - PASS 后解释 / 矛盾 / 新要求分类。
3. 冻结唯一：
   `GOVERNANCE_CANDIDATE_COMMIT`
   并让候选阶段所有 replay、Critic safety gate 和 Clear Writing 回归读取该 exact commit 的 1.8。
4. 不再设置未绑定的 separate implementation Reviewer；实现后由既有 Critic safety gate 直接审实际 diff、candidate identity 与 replay evidence。
5. 运行 8-case deterministic compatibility replay。
6. Clear Writing 两阶段真实回归：
   - `d7b810d...` 永久作为冲突负控；
   - 新合法 package 才能成为正向 execution-ready 回归对象；
   - 正向回归不预设 PASS。
7. 候选达到真实 `CANDIDATE_ACCEPTED` 后，按 `AGENTS.md 8.5` 完成 main integration preflight、ordinary merge/push 和 remote-main fresh readback。

## Candidate authority

候选验证期间：

`GOVERNANCE_CANDIDATE_COMMIT`

是 Planner/Critic 1.8 的唯一 authority。

当前 main 仍是 1.7，不得被称为候选 1.8。

后续 evidence 可以追加，但必须记录 candidate commit；candidate-defining source 若变化，旧 evidence 失效。

## Main integration 完成证明

最终只有 fresh remote-main readback 同时证明以下事实时，才能说 1.8 已正式生效：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md` version = 1.8；
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` version = 1.8；
- 两份合同与 candidate freeze 一致；
- regression / example / final evidence 与同一 candidate 对齐；
- 没有竞争性 main drift 改写冻结语义。

## 明确不做

- 不修改 AI Research Stack Project setting；
- 不修改 Capability Gate Policy 1.2；
- 不重新设计 Clear Writing 0.6；
- 不修改 Clear Writing 产品代码或 G1-G6 产品语义；
- 不修改 Bridge Kit 或 Plugin Creator；
- 不新增 Reviewer 机制、角色、schema、状态机、数据库、服务、watcher、daemon 或 prompt compiler；
- 不做 repository/plugin release；
- 不运行付费模型。

## 执行定位

```text
task_key=chatgpt-web--pass-integrity
execution_branch=reviewed/chatgpt-web--pass-integrity
execution_worktree=/tmp/ai-skills-chatgpt-web-pass-integrity
```

这些定位只有用户在唯一 execution-ready PASS 后实际发送批准的短 Codex handoff 时才成为执行授权。

## 完成条件

本治理任务只有在以下全部完成后才算真正收口：

- 1.8 candidate 实现；
- candidate identity 冻结；
- deterministic replay 成立；
- implementation-after Critic safety gate = `PROCEED_TO_FINAL_EVALUATION`；
- Clear Writing 旧包负控正确 REVISE；
- 新合法 Clear Writing package 完成全量 execution-ready review；
- 若其证据支持 PASS，五项 atomic delivery 同回复齐全；
- PASS 后解释 follow-up 稳定；
- governance candidate = `CANDIDATE_ACCEPTED`；
- 1.8 正式集成到 main；
- remote main fresh readback 成立。

README checked: no update required。
