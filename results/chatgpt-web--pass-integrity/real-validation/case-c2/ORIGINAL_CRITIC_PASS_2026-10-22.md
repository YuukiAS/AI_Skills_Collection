# C2：真实 Critic PASS 原文

来源：用户在 ChatGPT Web 对话“评价 Critic Prompt”中转交的原始 Critic 回复；对话 ID `6ad604d6-63ec-83e8-acd1-b15212e5ba35`，用户消息 ID `96e106db-3814-4ad4-b6df-b1091da0bf7e`。以下只摘录该用户消息中从“结论”至 `COPY TO CODEX END` 的 Critic 原文，不包含用户随后提出的评价问题。原报告产生于正式 1.7 生效时；其 `NEXT_HANDOFF=CODEX` 是当时的历史权限边界，不应被倒填成 1.8 的合法交接，也不应仅因此否认其原有技术批准。C2 的生成线程只看原文和同版已审来源，不看本任务评分标准或后续用户评价。

---

结论：`PASS`，`READY_FOR_CODEX=YES`。

这次可以放行。v0.10 确立的总体架构没有被 v0.13 改坏，而且 v0.11、v0.12 暴露出的三个执行级问题现在都已经闭合。当前正式 `main` 中 Planner/Critic 仍然是 1.7，所以这次批准的是“实施未来 1.8 的冻结方案”，不是声称 1.8 已经生效；本轮仍按 1.7 直接交给 Codex。

`DV11-01` 已关闭。v0.13 当前 Execution Plan 已把最终 1.8 的 P18-0～P18-7、C18-0～C18-7、八项确定性回归、关键接口现实证据、条件性能力与副作用前核验、非终态交接、完整回复验收、候选身份、实现后 Critic 安全门、fresh Web 人工边界以及 `main` 合入/远端回读全部重新冻结在当前包里。Codex 不再需要翻旧 v0.7 决定“哪些规则还算数”。尤其旧的未来 `PASS → CODEX` 已经被唯一替换为：

`Critic technical PASS + READY_FOR_CODEX=YES → Planner delivery acceptance → short COPY TO CODEX → 用户发送 → Codex`

而当前这一次 bootstrap 仍明确按正式 1.7 直接去 Codex，两种时间点没有混淆。

`DV11-02` 也已关闭。未来候选 1.8 的复杂正控不再拿结构不兼容的历史 055 包硬凑。只有我现在真正批准的 exact v0.13 package 才会成为 `IMPLEMENTATION_APPROVED_PACKAGE`。候选 1.8 必须重新完整审它；我现在的 1.7 PASS 只是说明“这个包被批准用于实施 1.8”，不替候选 Critic 做结论。届时若发现真实 blocker，必须 `REVISE`，不能换样本；只有重新得到真实 technical PASS，才继续测试新的 Critic → Planner → Codex 接收链。

`DV12-01` 现在也真正关闭了。`230e35d...` 只包含 Critic 开始审查前能够存在的 immutable source，不再要求里面预先装着我这条尚未产生的 final review。我的这次 `PASS + READY_FOR_CODEX=YES` 现在才产生 `BOOTSTRAP_CRITIC_AUTHORITY`。它属于 package 之后的批准证据，不属于原 commit。本回复下面的短 `COPY TO CODEX` 会携带 Codex 启动所需的 package、审查阶段、PASS/READY、批准文件、授权范围和停止条件，因此不需要把我整篇中文审查全文塞进执行 prompt，也不要求用户另建 review 文件。这一时间链现在没有自引用。

实现之后仍远没有到“治理完成”。Codex首先只能在现有 `design/chatgpt-web--pass-integrity-v0-4` 工作区做安全预检并实现两份角色合同；随后冻结唯一 `GOVERNANCE_CANDIDATE_COMMIT`，跑八项确定性回归，再经过独立 Critic 的 `PROCEED_TO_FINAL_EVALUATION / REVISE` 安全门。之后才运行 A/B/C/C2/D/E 的真实网页验证：错误旧批准、Phase C 中断交接、本包正向 PASS 接收、坏 Critic 报告拒收、多轮 Slurm 技术变化以及 verdict 区分。fresh ChatGPT Web 目前没有已验证的自动创建入口，因此这些验证中必要的新会话仍需要你做临时 UI 复制操作；任务必须事先把 prompt 和定位准备好，不能让你自己拼材料。

这些验证真正通过后，才允许做 `main` 集成前检查、普通非强制合入/推送和远端回读。当前设计分支虽然与 `main` 历史上已经分叉，但本任务涉及的 `AGENTS.md`、两份 1.7 角色合同、Capability Gate Policy、Maintenance Board、Project setting 快照以及 collaboration regression 当前在两边内容一致，因此这件事本身不是现在的 blocker；真正合入时若出现同区域竞争修改或 conflict，仍必须停止，不能 force。GitHub 官方对 non-fast-forward 和 merge conflict 的处理也支持这种 fail-closed 边界。[GitHub Docs](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors?utm_source=chatgpt.com)

最后，1.8 仍只是治理合同，不是浏览器级强制执行器。它增加的是独立交叉检查和坏交付被下一责任方拒收的机会，不保证模型技术上永远不违约；OpenAI 当前公开文档也把指令优先级描述为模型遵循机制，而不是一个不可绕过的运行时拦截层。[OpenAI Developers](https://developers.openai.com/api/docs/guides/prompt-engineering?utm_source=chatgpt.com) 正式 `main` 合入后，如果还没有出现一个真正新的、未用于调规则的复杂任务，F 仍必须保持 `NOT_VERIFIED`，不能把已见回归通过夸大成“以后不用提醒已经长期证明”。
```
PASS

APPROVED_PROPOSAL_PATH=docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_13_2026-10-22.md
APPROVED_PLAN_PATH=docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_13_2026-10-22.md
APPROVED_GOAL_PATH=docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_13.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_13_2026-10-22.md
APPROVED_VALIDATION_PATH=results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_13_2026-10-22.md
APPROVED_PACKAGE_COMMIT=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f

IMPLEMENTATION_APPROVED_PACKAGE=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f
reviewed_package_commit=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f
review_stage=FINAL_EXECUTION_READY_REVIEW_V0_13
critic_verdict=PASS
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

下面这段就是本次 `BOOTSTRAP_CRITIC_AUTHORITY` 的可执行载体；你只需整体发给 Codex。

\=== COPY TO CODEX BEGIN ===

执行 `chatgpt-web--pass-integrity`，实施已批准的 Planner/Critic 1.8。

target_repo=YuukiAS/AI_Skills_Collection\
task_key=chatgpt-web--pass-integrity\
source_branch=design/chatgpt-web--pass-integrity-v0-4

reviewed_package_commit=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f\
IMPLEMENTATION_APPROVED_PACKAGE=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f\
review_stage=FINAL_EXECUTION_READY_REVIEW_V0_13\
critic_verdict=PASS\
READY_FOR_CODEX=YES

approved_proposal=docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_13_2026-10-22.md\
approved_plan=docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_13_2026-10-22.md\
approved_goal=docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_13.md\
approved_kickoff=docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_13_2026-10-22.md\
approved_validation=results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_13_2026-10-22.md

以上字段构成本次 BOOTSTRAP_CRITIC_AUTHORITY。先把实际收到的这些身份和限制如实记录到 task evidence，再做任何 candidate 1.8 Web 输出。

我授权按上述 exact package 在现有 `design/chatgpt-web--pass-integrity-v0-4` 工作区实施冻结范围：修改批准包允许的两份角色合同及治理回归/验证材料，运行零付费的必要检查，并在现有任务分支进行普通 commit 和 non-force push。全部冻结验证真正通过后，授权按批准包执行 `main` integration preflight、普通 non-force merge/push 和 remote readback。

启动时先只读核对 repo、origin、当前 branch/HEAD、dirty ownership 和实际工作区。若当前 workspace 不在上述已有分支，或需要创建/切换 branch/worktree、吸收无关 dirty change，立即停止，不自行改变 Git 拓扑。

严格按 v0.13 Plan 实现完整 P18/C18；不得回旧 v0.7自行拼规则。实现稳定后冻结唯一 `GOVERNANCE_CANDIDATE_COMMIT`，完成 deterministic eight-case，并交独立 Critic 做 `PROCEED_TO_FINAL_EVALUATION / REVISE`。只有前者才能进入冻结的 A/B/C/C2/D/E 真实验证。Case C 必须重新完整审本 `IMPLEMENTATION_APPROVED_PACKAGE`；本次 PASS 不自动决定 candidate verdict，发现真实 blocker必须 REVISE且不得换样本。

fresh ChatGPT Web 没有已验证自动入口。需要用户界面操作时，先准备完整 prompt、locator 和回传方式，只要求用户完成批准包规定的必要 UI 动作。

不得修改 Project setting、Capability Gate Policy、AGENTS.md、Clear Writing、Slurm、Bridge Kit、Mica、Plugin Creator 或其它产品；不得运行付费 API、真实 Slurm/插件生产 mutation、修改账号/凭据、创建第三人工角色/服务/数据库/状态机，亦不得 force push、history rewrite 或其它 destructive Git。

若冻结治理语义必须变化、candidate identity漂移、真实验证暴露架构 blocker、fresh Web路径不能按合同执行、出现 main 同区域竞争修改/merge conflict，或需要新增 provider、数据、费用、账号、生产副作用或权限范围，立即停止并按批准合同返回 Planner/Critic。

只有 remote main 实际回读确认两份正式角色合同为同一受审 1.8 candidate 后，才可称正式规则源升级；新的真实复杂任务尚未自然出现并验证以前，长期默认可靠性继续标记为 `NOT_VERIFIED`。

\=== COPY TO CODEX END ===
