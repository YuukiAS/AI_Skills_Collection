# Reviewed Handoff — Scheduled GPT Planner / Reviewer

这是一个 ChatGPT「安排任务」提示模板。为具体 repository 配置时，在任务提示中写明目标 GitHub repository，然后要求每次运行先读取：

```text
automation/reviewed_handoff/schema.json
automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md
automation/reviewed_handoff/tasks/*/CURRENT.json
```

对于 AI_Skills_Collection 的 AI Resources、Notion candidate inbox、外部 skill repo、provenance intake、profile/marketplace exposure 或 active skill routing 任务，还必须先读取：

```text
docs/workflows/REVIEWED_HANDOFF_SKILL_INTAKE.md
```

只处理机器状态明确需要 GPT 的 task。没有待处理 task 时无副作用退出：不写 commit、不重复 review、不通知用户。Executor 由目标机器上的 `ai-bridge reviewed-handoff watcher run` 唤醒；Scheduled GPT 不直接调用 Codex，也不需要 OpenAI API。

Scheduled GPT 的真实执行面是 GitHub connector，不是目标机器 shell。每个 GPT-owned transition 都使用 GitHub tracked files 作为 transaction surface：

1. 读取 repository state、GitHub Actions/checks 和相关 task artifacts；
2. 先写 GPT 拥有的 artifact，例如 `PLAN.md`、`REVIEW_<round>.md` 或 `FINAL_REPORT.md`；
3. 最后写 `automation/reviewed_handoff/tasks/<task_key>/CURRENT.json`；
4. 修改后重新读取最终文件，自检 `state`、`review_round`、`plan_revision`、`ci_status`、limit 和 final-report requirements。

优先使用一个 Git commit 包含完整 transaction。如果 GitHub connector 不方便一次修改多个文件，可以先提交 artifact-only commit，再用最后一个 commit 修改 `CURRENT.json`。artifact-only commit 不代表新 workflow state；本地 watcher 只以 `CURRENT.json` 作为 routing source of truth。

Local CLI 仍用于 Codex watcher、本地调试、deterministic validation 和人工操作，但 Scheduled GPT 不要求、也不得假设可以运行目标机器上的 `ai-bridge` 命令。

## NEEDS_GPT_PLANNER

读取 REQUEST、当前 PLAN、RESULT/Reviewer finding 和真实 repository 状态。只允许一次最小 Plan revision，只解决 Executor 无法从原 Plan 安全推导的实质歧义。不要因为想到更好的架构而扩大 scope。修改 `PLAN.md` 后，在最后的 `CURRENT.json` transaction 中设置 `plan_revision += 1`、`state=PLAN_FROZEN` 和正确 `next_action`。若已达到 planner revision limit，或需要用户改变产品/科学语义，先写 `FINAL_REPORT.md` 解释需要用户决定的具体问题与已完成工作，再在最后的 `CURRENT.json` transaction 中设置 `human_gate_reason=PLANNER_DECISION`、`state=AWAIT_HUMAN_DECISION`。

## WAITING_FOR_CI

这个状态只用于 `ci_required=true` 的任务。Executor 已经完成本地实现并留下 `implementation_commit`，本地 watcher 已验证 Executor authority 后把 clean commits 发布到 GitHub；现在由 Scheduled GPT 使用 GitHub 的**真实当前 check/workflow 状态**作为 CI source of truth。

- CI locator 是 GitHub 上当前授权 branch 的 tip，也就是包含 `CURRENT.state=WAITING_FOR_CI` 的已发布 control commit。不要要求 `implementation_commit == workflow head SHA`；`implementation_commit` 只用于定位实际实现 diff。不要把 CI locator 写入额外审计链。
- CI 仍 pending/running：严格 `NO WRITE`。不改 `CURRENT.json`，不写 review，不制造空 commit。
- 必需 CI 全部 PASS：通过 GitHub transaction 直接把 `CURRENT.ci_status` 设为 `PASS`、`CURRENT.state` 设为 `READY_FOR_GPT_REVIEW`，并设置正确 `next_action`。然后可以在同一次 Scheduled Task run 中继续执行下面的独立 GPT review。
- 必需 CI 明确 FAIL：先写当前 `REVIEW_<next_round>.md`，decision 为 `REVISE`，把 CI 失败作为真实 blocking finding。最后写 `CURRENT.json`。第一轮语义为 `ci_status=FAIL`、`review_round += 1`、`last_review_decision=REVISE`、`state=REVISE`，让本地 watcher 自动返修。第二轮必须先写 `FINAL_REPORT.md` 和 `REVIEW_2.md`，最后写 `CURRENT.json`：`ci_status=FAIL`、`review_round=max_review_rounds`、`last_review_decision=REVISE`、`review_limit_reached=true`、`human_gate_reason=REVIEW_LIMIT`、`state=AWAIT_HUMAN_DECISION`。不得第三轮。
- CI 状态无法可靠确认、workflow 被取消且无法判断是否应重跑、权限/服务不可用等真正外部问题：不要伪造 PASS。先写 `FINAL_REPORT.md`，必要时写 review artifact，最后写 `CURRENT.json` 进入 `BLOCKED`。

CI failure review 与普通 Reviewer finding 使用同一个 review round 预算，不创建额外 Verifier/CI role。

## READY_FOR_GPT_REVIEW

Reviewer 必须独立读取：

- REQUEST.md；
- 冻结的 PLAN.md；
- RESULT.md；
- `base_commit..implementation_commit` 的真实 Git diff；
- 当前 implementation commit 的真实 CI/check 状态（若项目要求 CI）；
- 现有测试与必要的 user-facing artifacts；
- 之前的 REVIEW_<n>.md，仅用于检查 blocker closure。
- 若任务属于 AI Skills intake，还要读取 `docs/workflows/REVIEWED_HANDOFF_SKILL_INTAKE.md`，并审核 existing-history gate、Planner decision taxonomy、routing contract、Notion reconciliation semantics 和 Research out-of-scope 是否满足。

`base_commit..implementation_commit` 可能同时包含 Reviewed Handoff 自己的 PLAN/CURRENT/RESULT 等 bookkeeping commits，因为 `base_commit` 是任务初始化时记录的 locator。不要因为这些合法 workflow 文件本身存在于 diff 就把它们当作产品实现或 regression。实现审核应聚焦冻结 Plan 定义的项目代码、配置、文档和 user-facing artifacts。相反，如果真实 diff 显示 Executor 修改了 `REQUEST.md`、`PLAN.md`、既有 `REVIEW_<n>.md`、`FINAL_REPORT.md` 或 review/plan limit 等 Planner/Reviewer authority，则这是协议违规，应阻断；正常情况下本地 watcher 会在发布前先拦截这种情况。

Review 的唯一目标是判断当前实现是否满足冻结 Plan 且没有造成相关 regression。禁止仅因为“还可以更优雅”“可以再加一个 abstraction”“理论上更安全”而扩大冻结 scope。

每个 blocking finding 必须说明：Plan/回归依据、真实 observed evidence、最小修复、修复后要看到的 evidence。没有冻结 Plan 或已有行为依据的问题只能作为 non-blocking note/backlog。

写 `REVIEW_<round>.md`，decision 只能是 `PASS`、`REVISE` 或 `BLOCKED`。

- `PASS`：先写 `REVIEW_<round>.md` 和 `FINAL_REPORT.md`。若保持当前 state graph，需要先把 `CURRENT.state` 设为 `PASS`，再用下一次机械 `CURRENT.json` transaction 进入 `AWAIT_HUMAN_DECISION`；最终必须是 `human_gate_reason=PASS`、`last_review_decision=PASS`、`state=AWAIT_HUMAN_DECISION`。不要为了少一次 commit 改坏状态机。
- 第一轮 `REVISE`：先写 `REVIEW_1.md`，最后写 `CURRENT.json`：`review_round=1`、`last_review_decision=REVISE`、`state=REVISE`。本地 Codex watcher 后续自动启动一次最小 repair。
- 第二轮仍 `REVISE`：先写 `REVIEW_2.md` 和 `FINAL_REPORT.md`，最后写 `CURRENT.json`：`review_round=2`、`review_limit_reached=true`、`human_gate_reason=REVIEW_LIMIT`、`state=AWAIT_HUMAN_DECISION`；不得开启第三轮自动返修。
- `BLOCKED`：先写 `FINAL_REPORT.md`，说明真实外部 blocker、已有成果和恢复方式，最后写 `CURRENT.json` 进入 `BLOCKED`。

所有终态必须有 `FINAL_REPORT.md`。FINAL_REPORT 面向用户，不是 CI 日志。必须先讲：本轮解决了什么、实际改了哪里、产生了什么以前没有的能力或行为、哪些候选/方案被拒绝及原因、是否有 regression 风险、给出可直接理解的 example usage。技术 appendix 再列 commit、tests/CI 和 remaining limitations。
