# 用户转交的 v0.11 最终执行就绪 Critic 审查原文

日期：2026-10-22  
任务：`chatgpt-web--pass-integrity`  
审查阶段：`FINAL_EXECUTION_READY_REVIEW_V0_11`  
审查对象：`3b3a66411b99872b329657529a133745db0114e8`  
结论：`REVISE`

性质：当前用户在 Planner 对话中转交的独立 Critic 实际审查 authority。原 Critic 没有向仓库写 review commit。以下正文按用户转交内容原样归档；不得把本 Planner 的转述冒充 Critic 自己提交的审查。

---

~~~text
reviewed_package_commit=
3b3a66411b99872b329657529a133745db0114e8

review_stage=
FINAL_EXECUTION_READY_REVIEW_V0_11

critic_verdict=
REVISE

previous_design_review=
PROCEED

previous_design_reviewed_commit=
1fb7edd9955764644edc299fb9bc5142ea882e58

当前独立 Critic 没有向仓库写 review commit。以下内容是本轮实际独立审查 authority；请如实归档，不得把 Planner 转述冒充 Critic 自己提交的 review。

总体架构继续保留。不要重新设计以下已接受方向：

- 同版 Proposal 中维护用户真正阅读的当前技术决策说明；
- Critic 独立对照真实技术审这份说明；
- 接收 Critic 结果的 Planner 必须验收真实交付，不能只消费 verdict token；
- 技术依据完整但表达失焦时，Planner可从已经受审的 Proposal 与 Critic 原 findings 忠实恢复用户说明；
- 技术依据、版本、权限、关键接口或结论本身不足时，Planner必须拒收并退回真正的独立补审；
- 未来正式 1.8 的唯一 execution-ready 技术 PASS 仍只能由 Critic产生，但 NEXT_HANDOFF=PLANNER，由原 Planner做一次读者交付接受后才生成 COPY TO CODEX；
- Planner不是第二个技术审批者，不能改 verdict、扩 scope、自授 PASS或补造技术依据；
- v0.7 已正确的关键接口真实性、非终态交接、候选身份、安全门、main集成/readback等能力仍应进入最终 1.8；
- 不修改 Project setting、Capability Gate Policy、Clear Writing、Slurm、Bridge Kit、Mica、Plugin Creator；
- 不新增第三人工角色、服务、数据库、状态机、watcher、daemon、prompt compiler、付费模型或浏览器拦截。

本轮只有两个 execution-ready blocker。

DV11-01 — 当前 v0.11 没有把旧 v0.7 的既有 1.8 语义完整冻结成当前批准实施合同。

事实：

正式 main 还是 Planner/Critic 1.7，所以旧 v0.7 设计中的能力尚未正式存在。

旧 exact v0.7 package：
0bd4dbf09be68811cafac53afdaad0f671206023

其中 docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_EXECUTION_PLAN_V0_7_2026-10-21.md 曾明确冻结：

Planner：
- P18-1 task-specific Critic prompt compatibility；
- P18-2 short handoff renderability；
- P18-3 critical-interface reality evidence；
- P18-3a pre-side-effect probe；
- P18-3b conditional capability；
- P18-4 non-terminal handoff closure。

Critic：
- C18-1 task-prompt compatibility hard gate；
- C18-2 atomic execution-ready PASS；
- C18-3 PASS 后 explanation / contradiction / new requirement；
- C18-4 critical-interface evidence hard gate；
- C18-5 whole-response handoff/readability acceptance。

以及：
- GOVERNANCE_CANDIDATE_COMMIT；
- candidate-defining source变化使旧 evidence失效；
- deterministic eight-case replay；
- post-implementation Critic safety gate；
- user-only fresh Web boundary；
- main integration + remote readback。

最小关闭条件：形成完整新版 execution package，不要要求 Codex自行拼历史。把所有仍有效的 P18/C18 语义明确写入当前 Planner/Critic 1.8 修改清单；对被 v0.11 修改的旧语义明确写 REPLACED BY；atomic PASS 在未来正式 1.8 下明确改成 technical PASS + READY_FOR_CODEX=YES -> NEXT_HANDOFF=PLANNER -> Planner delivery acceptance -> COPY TO CODEX；当前首次实施 1.8 的这一次 execution-ready review 仍服从正式 1.7；deterministic eight-case 在当前 Plan/Validation 中重新冻结或用 exact incorporation + override。

DV11-02 — 当前 Case C 不能同时作为 exact historical package 和新 1.8 的合法正向 PASS route。

当前冻结 Case C：
package=745e6748c5faa7cbad51973142661491224ba5a2
task=055_clear_writing_release_convergence

该 exact package 不含候选 1.8 所要求的同版 `## 1. 用户决策说明`。严格执行新 1.8 应 REVISE；grandfather 又不能验证新 receiver 机制。

最小关闭条件：执行前重新冻结一个结构上有资格按 1.8 获得 PASS 的复杂正控，并保持 fail-closed。优先考虑当前 v0.11/v0.12 自身的完整 execution-ready package，或测试开始前已经满足 1.8 同版 reader-object 要求的真实复杂 package。

无论选哪个：
- candidate生成输出前冻结 exact package；
- 旧 PASS不自动有效；
- fresh candidate Critic发现真实 blocker时必须 REVISE；
- 不得测试失败后换样本；
- 必须真实走 Critic technical PASS -> NEXT_HANDOFF=PLANNER -> Planner delivery acceptance -> short COPY TO CODEX；
- Planner不得生成第二技术 PASS或增加新事实；
- 旧055 package可保留历史复杂技术审查/兼容性材料，但不能称新 receiver机制唯一正向 PASS控制。

正式 main 后新发生真实任务继续保留为最终默认入口/泛化验证；不得凭空制造。

其余 Validation Contract、执行边界和非扩项要求均继续保留。
~~~
