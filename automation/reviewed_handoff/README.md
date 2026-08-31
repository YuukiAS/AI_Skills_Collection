# Reviewed Handoff Core

Reviewed Handoff 是 Lite Handoff 与 Agent-Flow 之间的中档工作流。它适合需要 GPT 先做产品/语义规划、Codex 大量实现、随后由独立 GPT 审核一到两轮的任务。

它只有三个逻辑角色：Planner、Executor、Reviewer。Controller 只允许做机械状态推进，不是独立思考角色。

AI_Skills_Collection 的 skill intake 任务还有一个本仓库 adapter：

```text
docs/workflows/REVIEWED_HANDOFF_SKILL_INTAKE.md
```

任何涉及 AI Resources、Notion candidate inbox、外部 skill repo、provenance intake、profile/marketplace exposure 或 active skill routing 的任务，Planner、Executor、Reviewer 都必须先读该 adapter，再处理本目录下的通用 Reviewed Handoff artifact。

核心流程：

```text
GPT Planner
→ local Codex watcher launches Executor
→ Scheduled GPT Reviewer
→ optional Codex repair
→ Scheduled GPT Reviewer
→ human reads FINAL_REPORT.md
```

GPT 异步唤醒使用 ChatGPT「安排任务」定时检查 GitHub 上的 `CURRENT.json`，不需要 OpenAI API。Codex 异步唤醒由机器上的轻量 watcher 完成：它只处理 `PLAN_FROZEN` 和 `REVISE`，同步当前已授权 branch 后启动一次新的 `codex exec`。Reviewer/Planner 和 Executor 仍然通过 GitHub tracked state 通信，不直接调用彼此。

机器上长期运行 watcher：

```bash
ai-bridge reviewed-handoff watcher run \
  --target /path/to/project \
  --branch <existing-authorized-branch>
```

单次检查或部署前 dry run：

```bash
ai-bridge reviewed-handoff watcher once --target /path/to/project --branch <branch> --dry-run
```

Watcher 不创建 branch/PR，不为执行尝试写入额外审计链。机器本地的 event 去重和日志位于 `${AI_BRIDGE_STATE_HOME:-~/.ai-bridge}/reviewed-handoff/<repo>/`，不会写进目标 repository。Codex exit code 为 0 也不自动视为成功：只有 task state 真正离开原 executor event 才算有进展；同一 event 的执行尝试有界，耗尽后进入可见的 `BLOCKED`，而不是无限重试。

## External GPT wait contract

Executor 成功发布实现并把 `CURRENT` 推进到 GPT-owned state 后，外部 GPT 尚未产出新 decision 属于正常等待，不属于 watcher retry，也不是 `BLOCKED`。常见等待态包括 `NEEDS_GPT_PLANNER`、`READY_FOR_GPT_REVIEW`，以及 `WAITING_FOR_CI` 在 CI 已经 PASS/FAIL 后需要 Scheduled GPT 继续写 review/transition 的阶段。

如果 `CURRENT.visual_review_required=true` 且不需要 CI，Executor 必须先发布渲染图片和 `results/<task_key>/visual_review/visual_inputs.json`，再进入 `READY_FOR_GPT_REVIEW`。`VISUAL_REVIEW.json` 缺失但 input manifest 有效时是 `waiting_visual_review_evidence`，等待 GitHub Actions 写回 evidence；这不消耗 `review_round`，也不是 `BLOCKED`。

如果 `CURRENT.text_review_required=true` 且不需要 CI，Executor 必须先发布 `results/<task_key>/text_review/payload.age` 和 `results/<task_key>/text_review/text_inputs.json`，再进入 `READY_FOR_GPT_REVIEW`。`TEXT_REVIEW.json` 缺失但 input manifest 有效时是 `waiting_text_review_evidence`，等待 GitHub Actions ephemeral decrypt + OpenAI Responses API `store=false` 写回 evidence；这不消耗 `review_round`，也不是 `BLOCKED`。plaintext private artifact、age private identity 和 OpenAI key 都不得提交到 repository。

如果同一个视觉或文本审查任务还设置了 `CURRENT.ci_required=true`，合法顺序是先发布 implementation、artifact inputs 和对应 manifest，并停在 `WAITING_FOR_CI` / `ci_status=PENDING`。此时 required evidence 仍可缺失，waiting owner 是 CI。只有 CI PASS 后 Scheduled GPT 才把任务推进到 `READY_FOR_GPT_REVIEW`；随后缺失 `VISUAL_REVIEW.json` 或 `TEXT_REVIEW.json` 才表示等待对应 evidence。

旧 review 只能作为历史上下文。`REVIEW_<n>.md` 的 `implementation_commit` 必须等于当前 `CURRENT.implementation_commit` 才是 fresh decision；不匹配时视为 stale review，不得重复执行旧 `REVISE`，也不得把旧 PASS/BLOCKED 当成当前实现的结论。等待期间不得增加 `review_round`、`plan_revision`、Executor retry 或 blocked-audit attempts。

Reviewed Handoff 刻意保持轻量：不把 Agent-Flow 的额外规划、审核、角色证明或来源图谱 artifact family 复制进本项目。`base_commit` 与 `implementation_commit` 只作为 Git 定位信息；review 是否通过取决于冻结 Plan、当前 diff、真实测试/CI 和 regression risk。

如果 `CURRENT.ci_required=true`，Executor 只能发布 `WAITING_FOR_CI` 且保持 `CURRENT.ci_status=PENDING`。Scheduled GPT 读取 GitHub 上当前授权 branch tip 的真实 checks；该 branch tip 是普通 CI locator，不要求等于 `implementation_commit`，也不会写入 hash/receipt 链。`CURRENT.ci_status` 是唯一机器 CI 真值，`RESULT.md` 只负责说明本地执行和验证。

每个任务的机器状态位于：

```text
automation/reviewed_handoff/tasks/<task_key>/CURRENT.json
```

人类/模型交接 artifact：

```text
automation/reviewed_handoff/tasks/<task_key>/REQUEST.md
automation/reviewed_handoff/tasks/<task_key>/PLAN.md
results/<task_key>/RESULT.md
results/<task_key>/REVIEW_1.md
results/<task_key>/REVIEW_2.md    # optional
results/<task_key>/FINAL_REPORT.md
```

Review 最多两轮。第二轮仍为 `REVISE` 时必须进入 `AWAIT_HUMAN_DECISION`，不得继续自动返修。Planner 在执行中最多允许一次 scheduled re-plan；再次出现需要改变冻结 Plan 的实质歧义时交给用户。所有终态都必须有 `FINAL_REPORT.md`，因此用户回来后始终有一份面向人的总结可读，而不是只能翻 CI/Reviewer 日志。

如果 Reviewer 已经 `PASS` 并进入 `AWAIT_HUMAN_DECISION`，但用户实际检查 artifact 后明确拒绝，不能手改 `CURRENT.json`，也不能把用户拒绝冒充成 Reviewer decision。使用 `ai-bridge reviewed-handoff human record --decision REJECT --route REVISE|NEEDS_GPT_PLANNER` 记录机械事务：只需按冻结 Plan 修复时回到 `REVISE`，证明 Plan 本身需要一次最小修订时回到 `NEEDS_GPT_PLANNER`。事务保留原 `REVIEW_<n>.md`、`last_review_decision=PASS` 和当前 `review_round`，相关预算用尽后不得无限重开。
