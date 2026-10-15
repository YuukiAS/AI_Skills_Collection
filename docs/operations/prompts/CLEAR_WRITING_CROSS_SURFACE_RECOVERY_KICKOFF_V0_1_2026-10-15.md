继续现有 Clear Writing Reviewed Handoff 任务，不要新建任务、分支或 successor。

仓库：`YuukiAS/AI_Skills_Collection`
任务：`clear-writing--cross-surface-language-layer`
分支：`reviewed/clear-writing--cross-surface-language-layer`

先读取并严格执行：
- `docs/design/clear-writing/CROSS_SURFACE_RECOVERY_PLAN_V0_1_2026-10-15.md`
- `docs/goals/CLEAR_WRITING_CROSS_SURFACE_RECOVERY_GOAL_V0_1_2026-10-15.md`
- `results/clear-writing--cross-surface-language-layer/REAL_WEB_REGRESSION_BANK_V1.md`
- 原 task 的 `REQUEST.md`、`PLAN.md`、`CURRENT.json`、`REVIEW_1.md`
- `results/clear-writing--cross-surface-language-layer/CRITIC_CW_CI_01_RECOVERY_BOUNDARY_2026-10-13.md`
- 本 recovery package 的独立 Critic PASS。

执行顺序不得改：

1. 在任何 production source 修改或 merge main 前，先以现有实现 `cac70c3bfcce6aeeba9c3e80adfa317235b54ee9` 对 RW-WEB-01..05 建立 public-safe derived fixtures 和 baseline replay；保存 5 份完整输出与 case verdict。不要把 private Web transcript 提交到 repo。
2. baseline packet commit 后，普通 non-force merge 当前 `origin/main` 到同一 reviewed branch；禁止 rebase/force/successor。
3. 在同步后的候选上重跑 5 个 known regressions。只有真实失败才允许最小修 `response-clarity` 及直接相关 routing/eval tests；已经 PASS 的 case 不为了制造 diff 而改。
4. 修复范围必须针对通用失败：回答完成后的停止条件、格式复杂度与信息复杂度匹配、来源共识与助手建议分层、写作反馈意图匹配；必须保护正例中的具体解释/例子/不确定性。禁止禁词表、英文比例、固定长度/标题/箭头规则、项目名硬编码、新 skill/router/model/API。
5. 按 recovery Plan 关闭此前全仓 CI 的既有 baseline 类别。不得为测试改 `VERSION`，不得删除合法 TODO，不能弱化/跳过 full CI。Presentations / Research Authoring 只允许在 Critic 明确批准的范围内做“current canonical source 已唯一决定”的 generated-only 同步；任何 source-semantic choice 立即停止并回 Planner。
6. 跑 focused tests、5 个 known regressions、should-not-change controls、生成/镜像一致性、全仓 tests、Marketplace check 和 required GitHub CI。
7. full CI 仍失败时，不消费第二轮 Reviewer；准确归因并停在合法 Planner 路由。full CI PASS 后，准备完整 artifact/evidence 给现有独立 review，不能从局部 tests 宣布产品 PASS。

本轮不授权：ChatGPT 个人插件/账号修改、付费 API、PIE 0.2、版本发布、main/release merge、G7 fresh/holdout、Research Authoring 或 Presentations source-semantic 修改。

如果本 prompt 是在 Critic execution-ready PASS 后由用户发送，即授权上述 bounded repo 读取、修改、测试、普通非强制提交/push 和 required zero-paid CI；除此之外不得扩大。
