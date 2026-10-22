# Planner–Critic 1.8 v0.11：执行范围与授权草案

任务：`chatgpt-web--pass-integrity`；日期：2026-10-22。
状态：`DRAFT / NOT_AUTHORIZED`。该文件供最后独立 Critic 冻结执行语义；**不得直接发送 Codex**。只有此包经唯一 execution-ready `PASS + READY_FOR_CODEX=YES`，且用户在当前会话实际发送最终短 `COPY TO CODEX`，才能按范围开始。

## 当前与目标

目标仓库：`YuukiAS/AI_Skills_Collection`。
任务已存在的设计分支：`design/chatgpt-web--pass-integrity-v0-4`。
目标版本：两份正式 Planner/Critic Role Contract 由 1.7 更新为 1.8。正式 `main` 当前 1.7；未授权更改当前 ChatGPT 项目设置。

本次唯一执行包的准确 commit 由用户最终交接消息提供，含：
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_11_2026-10-22.md`；
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_11_2026-10-22.md`；
- `docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_11.md`；
- 本草案；
- `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_11_2026-10-22.md`；
- 对应独立最终 Critic 的完整审查结论与真实 locator。

旧 v0.7/v0.8/v0.9 或错误扩项 v1.0 不可作为当前批准版本。v0.10 设计 `PROCEED` 仅支持继续准备这个包，不能启动实施。

## 获准后具体允许做什么

1. 在用户选择的现有 AI Skills 工作区中验证真实仓库、`origin`、当前分支/工作树、HEAD、dirty ownership 与来源身份。**执行目标固定为已有 `design/chatgpt-web--pass-integrity-v0-4`**；本批准不允许悄悄创建新分支或在 `/tmp` 建正式新工作树。如现有 checkout 不位于该分支，先 STOP 给出必要的最小环境定位，不自行切换用户现存工作树或重写远端。
2. 按同版 Proposal/Plan/Goal 修改两份正式角色合同，保留用户设置既有入口；实现用户决策说明随技术同步、Critic 独立比对、Planner 接收 Critic 结果的三种判断、最终技术 `PASS` 返回原 Planner 以完成用户交付。保留唯一技术 PASS、没有新机器状态/第三人工角色。
3. 有界修改 `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md` 与 `results/chatgpt-web--pass-integrity/**`；必要时新增一个轻量机械合同回归测试，不能把关键词测试当真实专业解释验收。真实 case A/B/C、跨轮 D 的执行准备材料和候选身份都存同一任务目录。
4. 完成本地与已批准的相关仓库验证，形成 frozen candidate 的 exact commit；后继 manifest 持有候选 commit 与实际 role text identity，避免文件自引用哈希。用户可见的读者说明以当前准确 Proposal §1 为唯一真相，不单独复制一个会漂移的摘要。
5. 候选冻结后交现有独立 Critic 做实现后 `PROCEED_TO_FINAL_EVALUATION/REVISE` 安全门；获准才运行冻结的真实 Web 测试。执行者必须事先准备所有必要 fresh Web Planner/Critic 测试提示词和回传位置；目前没有证明有工具可以自动创建网页对话，所以用户只完成必须自己做的 UI 动作。
6. 原审查和实际 Web 验收符合当前合同且获得这次明确的普通集成授权后，按本仓库 `AGENTS.md §8.5` 做 main 合并前安全检查、非强制提交/推送和远端回读；若有冲突、相关文件竞争修改、超出当前授权或确切环境不同，则停止。正式 `main` 只有回读两份合同版本/内容无误，才能称治理 1.8 已作为规则源生效。自然新任务的长期可靠性另在正常入口出现后观察，不伪造任务。

## 权限边界

在用户实际授权以上范围之前不执行。授权范围若成立，只允许 task-owned docs/test/evidence、已存在任务分支上的普通 Git、按风险运行必要 CI/已批准无付费只读 Web 验收，以及达到安全检查后的普通 main 集成。当前设计审查并不提前授予上述行动。

禁止修改 `AGENTS.md`、README、AI Research Stack Project setting、`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`、Clear Writing 产品、其它正式 Plugin/Skill、Bridge Kit、Mica、Slurm、Plugin Creator；禁止新增 MCP 服务/机器网关/第三人工审核者/数据库/状态机/付费模型、真实 Slurm 操作、线上插件更新、任何未授权私有数据传输或账号/凭据变更；禁止 force/历史重写、删除无关分支或自行扩大执行语义。

正式执行中若技术判断需要增加新高影响费用、数据、账号、生产变更或架构职责，旧批准不覆盖，必须 STOP 并交当前 Planner/Critic/用户依合法流程决定。纯实现漏项和不改变冻结语义的测试缺陷由同一 Codex 任务完成，不默认创建另一个任务。

## 交接语义，不再临场猜

当前目标的**首次执行就绪审查**仍依据已正式生效的 1.7 合同：该次独立 Critic 的 PASS 如果成立，给用户直接可发送的短 `COPY TO CODEX`，用户发送才构成实施授权。

**未来 1.8 正式生效后的普通插件/架构任务**才使用新机制：Critic 技术 PASS → `NEXT_HANDOFF=PLANNER` → 原 Planner读者交付接收 → 短 `COPY TO CODEX`。不拿当前尚未实施的机制覆盖本包自身的启动入口。

用户不负责整理 Critic 全文、手工维护 Issue 或选择哪个内部 Reviewer；若独立 Critic 无仓库写能力，`COPY TO PLANNER` 自包含实质 verdict/findings/所审准确身份，由原 Planner 如实归档。不得把“Critic 已写 review commit”当成无证据事实。
