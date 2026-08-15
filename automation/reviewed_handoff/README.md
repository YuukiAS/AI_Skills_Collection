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
