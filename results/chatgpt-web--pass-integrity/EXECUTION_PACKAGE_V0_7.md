# Planner–Critic 1.8 execution package manifest v0.7

日期：2026-10-21  
任务：`chatgpt-web--pass-integrity`  
阶段：`FINAL_EXECUTION_READY_CRITIC_PENDING`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
上一 package：`5dc95e155d4890d5bd311ef7c80baab830191949`  
形成 v0.7 时最新正式 main：`de460300f55b5617654dd50b2a5cfec9ab89a094`

## 为什么 v0.6 不再可直接送审

Clear Writing 0.6 Phase C 的真实证据证明 v0.6 尚未覆盖：

1. execution-ready 前关键接口的现实证据义务；
2. 中途停止后的真实 handoff closure；
3. user-visible whole-response acceptance。

因此 v0.7 是实质修订，不是给 v0.6 prompt 追加一段说明。

## v0.7 完整 package

同一次 final Critic review 必须从调用方提供的同一个 exact：

`PACKAGE_COMMIT=<exact v0.7 package commit>`

读取：

- `results/chatgpt-web--pass-integrity/CLEAR_WRITING_PHASE_C_GOVERNANCE_FAILURE_2026-10-21.md`
- `results/chatgpt-web--pass-integrity/real-validation/case-b/ORIGINAL_REPLY.md`
- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_7_2026-10-21.md`
- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_EXECUTION_PLAN_V0_7_2026-10-21.md`
- `docs/goals/CHATGPT_WEB_PASS_INTEGRITY_GOAL_V0_7.md`
- `docs/operations/prompts/CHATGPT_WEB_PASS_INTEGRITY_KICKOFF_DRAFT_V0_7_2026-10-21.md`
- `results/chatgpt-web--pass-integrity/EXECUTION_PACKAGE_V0_7.md`
- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_FINAL_CRITIC_PROMPT_V0_7_2026-10-21.md`

不得混读不同 commit 的 v0.7 文件。

## 保留的 v0.6 语义

- task-prompt compatibility；
- atomic execution-ready PASS；
- PASS 后 explanation / contradiction / new requirement；
- `GOVERNANCE_CANDIDATE_COMMIT`；
- post-implementation Critic safety gate；
- main integration + fresh readback；
- no third manual role / state machine / service / database。

## v0.7 新增语义

- critical-interface reality evidence；
- conditional capability 的 actor / surface / pre-side-effect probe / stop / recovery；
- non-terminal handoff closure；
- user-visible whole-response acceptance；
- real validation Case A/B/C。

## Real validation identities

### Case A

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

supporting evidence：

`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`

expected governance result：

`REVISE`

### Case B

source evidence：

`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`

frozen original reply：

`results/chatgpt-web--pass-integrity/real-validation/case-b/ORIGINAL_REPLY.md`

expected governance result：

whole-response handoff/readability PASS with a unique executable next entry。

### Case C

`745e6748c5faa7cbad51973142661491224ba5a2`

task：

`055_clear_writing_release_convergence`

historical evidence：

- `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_CRITIC_REVIEW_R2.md`
- `results/055_clear_writing_release_convergence/FINAL_REPORT.md`

expected governance behavior：

new full execution-ready review under candidate 1.8；PASS only if current truth genuinely supports it。No sample replacement inside this batch.

## Candidate / execution identity

只有 final Critic PASS + user-sent approved handoff 后才生效：

```text
task_key=chatgpt-web--pass-integrity
execution_branch=reviewed/chatgpt-web--pass-integrity
execution_worktree=/tmp/ai-skills-chatgpt-web-pass-integrity
```

Implementation 后冻结：

`GOVERNANCE_CANDIDATE_COMMIT=<exact sha>`

所有 deterministic replay、post-implementation Critic、A/B/C 都绑定该 candidate。

## Known user-only boundary

A/B/C 需要 fresh ChatGPT Web conversations；当前 package 不声称存在自动创建这些 conversations 的 verified action。

因此 final-evaluation 阶段冻结为最多三次 user-only UI action；所有 exact prompts/locators 必须由任务预先生成，用户不负责查 repo 或拼接 handoff。

## No authority yet

当前不得：

- 实施 1.8；
- 创建 execution branch/worktree；
- 修改 main；
- 修改 Project setting；
- 修改 Capability Gate Policy；
- 修改 Clear Writing 0.6；
- 修改 Plugin Creator / Bridge Kit；
- 跑 paid API；
- mutation Personal Plugin。
