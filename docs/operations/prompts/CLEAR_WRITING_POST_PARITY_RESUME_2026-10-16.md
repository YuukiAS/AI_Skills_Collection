继续现有 Clear Writing Reviewed Handoff 任务，不要新建任务、分支或 successor。

仓库：`YuukiAS/AI_Skills_Collection`
任务：`clear-writing--cross-surface-language-layer`
分支：`reviewed/clear-writing--cross-surface-language-layer`

Planner 已核验外部 source-authority blocker 已在：

`main@3c3a1a393dd99c40dc641d6b1abc478f14e65a19`

关闭，且：
- 4 个已知仓库 failure 全部关闭；
- generator clean/idempotent；
- full tests = `338/338 PASS`；
- 当前没有剩余 external blocker。

Planner 已把当前任务恢复为：
- `state=PLAN_FROZEN`
- `next_action=RUN_CODEX_EXECUTOR`
- `plan_revision=1`
- `review_round=1`
- `ci_status=PENDING`

先读取：
- `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/PLAN.md`
- `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/CURRENT.json`
- `results/clear-writing--cross-surface-language-layer/PLANNER_EXTERNAL_DEPENDENCY_RESUME_2026-10-16.md`
- `results/clear-writing--cross-surface-language-layer/REAL_WEB_REGRESSION_BANK_V1.md`
- `results/clear-writing--cross-surface-language-layer/web-regression-pre-repair/3212a6a/PRE_REPAIR_VERDICTS.md`
- `results/clear-writing--cross-surface-language-layer/GEN_PARITY_SEMANTIC_BLOCKER_2026-10-15.md`

不要重新做 Phase A baseline，也不要重新设计 Clear Writing。已经完成的事实是：
- 原始候选与同步旧 main 后均为 RW-WEB-01..04 PASS、RW-WEB-05 FAIL；
- 已在 `0284bb264b56a218a60deb4dfbe56fb66f6b1e6e` 做了 bounded `response-clarity` 修复，只增加语义停止条件和“来源共识 vs 助手建议”分层；
- focused Clear Writing tests 已通过；
- 之前唯一阻塞 full CI 的外部 source/generated parity 已由新 main 修好。

现在只继续剩余执行：

1. `git fetch origin`，确认当前 branch/worktree 干净且仍在 `reviewed/clear-writing--cross-surface-language-layer`。
2. 普通 non-force merge `origin/main@3c3a1a393dd99c40dc641d6b1abc478f14e65a19` 到当前 reviewed branch；禁止 rebase/force/successor。
3. 解决冲突时：
   - 保留当前 Clear Writing task 的 `response-clarity` 修复与 regression evidence；
   - 接受 main 已完成的 source-authority/test 修复；
   - 不重新设计 Presentations / Research Authoring；
   - 若出现真正需要专业语义二选一的冲突，停止并回 Planner。
4. 在合并后的 candidate 上运行 RW-WEB-01..05 post-repair replay，保存完整输出与 verdict：
   - RW-WEB-01 / 02 / 04 / 05 必须 PASS；
   - RW-WEB-03 必须继续作为 positive control PASS，保留必要例子、因果解释和不确定性；
   - 不得靠固定字数、标题数、禁词、英文比例、箭头/代码框禁令判 PASS。
5. 运行 frozen should-not-change controls：
   - 用户明确要求完整 report / executable prompt / contract；
   - 真正有分支或逐步执行价值的流程；
   - pure JSON/YAML/code/raw log exact output；
   - 正式产品名和 exact machine strings。
6. 运行完整验证：
   - response-clarity focused tests；
   - writing-style source/generated parity；
   - `python scripts/build_codex_marketplace.py --write --validate --check --path-report`；
   - 再跑 generator check 确认 idempotent clean；
   - full repository unit tests；
   - `git diff --check`。
7. 若上述全部 PASS：
   - commit + ordinary non-force push 当前 reviewed branch；
   - 更新 `results/clear-writing--cross-surface-language-layer/RESULT.md`，绑定新的 implementation commit；
   - 更新 `CURRENT.implementation_commit`；
   - 按 frozen Plan 进入 `WAITING_FOR_CI / ci_status=PENDING`；
   - 触发/等待 required zero-paid GitHub CI。
8. required GitHub CI 真正 PASS 后，才交第二轮独立 Reviewer；不要提前消费 `review_round=2`，也不要从本地 PASS 直接宣布产品完成。

本轮仍不授权：
- ChatGPT 个人插件/账号修改；
- PIE 0.2；
- paid API/model review；
- G7 fresh/holdout；
- release/main merge；
- 新 skill/router/state machine；
- Presentations / Research Authoring 新产品设计。

如果 post-repair known regressions 或 full tests 失败，只修 frozen Plan 已允许的 Clear Writing 问题；若需要改变 Plan/产品语义，则停止，不自行扩大。
