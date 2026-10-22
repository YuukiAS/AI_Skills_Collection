# Codex 收到的 1.8 实施授权与身份记录

日期：2026-10-22
任务：`chatgpt-web--pass-integrity`
性质：Codex 根据用户实际发送到本任务的短实施入口记录的审查后证据；不是独立 Critic 的完整原文或 review commit，也不属于审查前的不可变实施包。

## 实际收到的批准身份

- `target_repo=YuukiAS/AI_Skills_Collection`
- `task_key=chatgpt-web--pass-integrity`
- `source_branch=design/chatgpt-web--pass-integrity-v0-4`
- `reviewed_package_commit=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f`
- `IMPLEMENTATION_APPROVED_PACKAGE=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f`
- `review_stage=FINAL_EXECUTION_READY_REVIEW_V0_13`
- `critic_verdict=PASS`
- `READY_FOR_CODEX=YES`
- 批准的 Proposal、Plan、Goal、Kickoff 分别为 `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_13_2026-10-22.md`、`docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_13_2026-10-22.md`、`docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_13.md`、`docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_13_2026-10-22.md`；验证合同为 `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_13_2026-10-22.md`。

上述 `PASS/READY` 来自用户实际发送的当前短入口，只证明该不可变包曾获正式 1.7 的执行就绪技术批准；本文件不补造未收到的 Critic 全文，不预判未来 1.8 候选的技术 verdict。

## 实际收到的执行范围和限制

用户授权在现有任务分支修改两份角色合同及批准的治理回归/验证材料，运行零付费检查，进行 task-owned add/commit 和普通非强制 push。只有冻结验证真实通过，才可按批准包进行 `main` 集成预检、普通非强制 merge/push 与远端回读。稳定实现后冻结唯一 `GOVERNANCE_CANDIDATE_COMMIT`，先完成八项确定性回放，再交独立 Critic 安全门；只有 `PROCEED_TO_FINAL_EVALUATION` 后才运行 A/B/C/C2/D/E 真实验证。Case C 仍须由候选重新完整审本 `IMPLEMENTATION_APPROVED_PACKAGE`；旧 PASS 不决定候选 verdict。

未授权修改 live Project setting、Capability Gate Policy、AGENTS、Clear Writing、Slurm、Bridge Kit、Mica、Plugin Creator 或其它产品；未授权付费 API、真实 Slurm/插件生产操作、账号/凭据或私有数据新传输、第三人工角色或新服务/数据库/状态机、force push、history rewrite 或破坏性 Git。fresh ChatGPT Web 没有已验证自动入口；必要界面动作由执行方先备好完整 prompt、locator 和回传方式，只让用户完成批准包要求的操作。

冻结治理语义改变、候选身份漂移、真实验证出现架构 blocker、fresh Web 路径不能按合同执行、`main` 同区域竞争修改或冲突，以及新增 provider、数据、费用、账号、生产副作用或权限边界时，按批准合同停止并返回相应 Planner/Critic。远端 `main` 两份正式合同实际回读为同一受审 1.8 候选前，不称正式规则源升级；未来新真实复杂任务未经自然运行验证，长期默认可靠性保持 `NOT_VERIFIED`。

## 工作区预检与顺序

首次预检时仓库 `origin` 为 `https://github.com/YuukiAS/AI_Skills_Collection.git`，当前工作区在干净的 `reviewed/clear-writing--scientific-explanation-readability-repair`，因此按原 Kickoff 停止。用户随后明确要求“你自己给我切过去做”；据此只为远端已有的 exact `design/chatgpt-web--pass-integrity-v0-4` 建立同名本地跟踪分支并切换当前干净工作区，未创建其它分支/工作树，未修改原 reviewed 分支。切换后本地 HEAD 为 `5d1ebfa9a2627882d62d94aa9469b37062c2e995`，与当前 `origin/design/chatgpt-web--pass-integrity-v0-4` 一致，工作区干净；批准包提交 `230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f` 是其祖先，之后只新增批准接收与停止清单。

本记录写入时尚未生成任何 candidate 1.8 Web 输出，也未形成 `GOVERNANCE_CANDIDATE_COMMIT`。
