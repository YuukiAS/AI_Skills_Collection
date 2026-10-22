# 用户转交的 v0.11 最终 execution-ready Critic REVISE 原文

日期：2026-10-22  
任务：`chatgpt-web--pass-integrity`  
所审包：`3b3a66411b99872b329657529a133745db0114e8`  
结论：`REVISE`

来源边界：原 Critic 没有向仓库写 review commit；以下是当前用户在 Planner 线程转交的本轮实际独立审查 authority，按原文归档。本提交由 Planner 保存，不冒充 Critic 自己的 GitHub commit。

---

~~~text
继续同一治理任务：

target_repo=YuukiAS/AI_Skills_Collection
task_key=chatgpt-web--pass-integrity
source_branch=design/chatgpt-web--pass-integrity-v0-4

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

本轮完整重审了 v0.11 Proposal、Execution Plan、Goal、Kickoff、Validation Contract、上一轮用户转交 Critic authority、用户部分认可样本，以及最新正式 main 的 Planner/Critic 1.7、AGENTS、Capability Gate Policy、Maintenance Board 和 Project setting。

最新正式 main：
f1de8e85957d32a50f4458349f450ec65add13bb

正式角色仍是 1.7；1.8 尚未实施。

总体架构继续保留。不要重新设计以下已接受方向：

- 同版 Proposal 中维护用户真正阅读的当前技术决策说明；
- Critic 独立对照真实技术审这份说明；
- 接收 Critic 结果的 Planner 必须验收真实交付，不能只消费 PROCEED / REVISE / PASS token；
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

其中
docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_EXECUTION_PLAN_V0_7_2026-10-21.md
曾明确冻结：

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

但当前 v0.11 的正式合同修改章节主要冻结了本轮新增的 decision visibility / receiving semantics，其余只用“保留 v0.7”概括。

同时当前 Kickoff 又写明：
旧 v0.7/v0.8/v0.9 不能作为当前批准版本。

这会留下关键歧义：
Codex 到底应从哪个历史文件继承哪些规则、哪些旧语义已被 v0.11 覆盖、特别是旧 C18-2 的 NEXT_HANDOFF=CODEX 怎样被新的未来 1.8 NEXT_HANDOFF=PLANNER 精确替换。

最小关闭条件：

形成完整新版 execution package，不要要求 Codex自行拼历史。

推荐 v0.12 直接在当前 Execution Plan 中给出完整 1.8 role-change contract：

1. 把所有仍有效的 P18/C18 语义明确写入当前 Planner/Critic 1.8 修改清单；
2. 对被 v0.11 修改的旧语义明确写 REPLACED BY，而不是让 Executor推断；
3. 特别冻结：
   - task-prompt compatibility；
   - short handoff renderability；
   - critical-interface evidence；
   - conditional/pre-side-effect verification；
   - non-terminal handoff closure；
   - whole-response acceptance；
   - PASS follow-up classification；
   - candidate identity；
   - post-implementation safety gate；
   - deterministic replay；
   - main integration/readback；
4. atomic PASS 在未来正式 1.8 下明确改成：
   technical PASS + READY_FOR_CODEX=YES
   -> NEXT_HANDOFF=PLANNER
   -> Planner delivery acceptance
   -> COPY TO CODEX
   不得同时保留旧 NEXT_HANDOFF=CODEX 作为另一合法解释；
5. 当前首次实施 1.8 的这一次 execution-ready review 仍服从正式 1.7，若最终 PASS 则直接 COPY TO CODEX，这一点继续保持；
6. deterministic eight-case 的实际八项也在当前 Plan/Validation Contract 中重新冻结，或用一个明确 exact locator 声明“以下 exact historical section 作为当前规范性 incorporation”，并逐项列出 v0.11 override。不要只写“保留旧八项”。

无需把旧 v0.7 全文复制进用户说明；机器执行合同必须完整即可。

DV11-02 — 当前 Case C 不能同时作为 exact historical package 和新 1.8 的合法正向 PASS route。

当前冻结 Case C：

package=
745e6748c5faa7cbad51973142661491224ba5a2

task=
055_clear_writing_release_convergence

独立核对该 exact package 的：
docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md

其章节为：

- ## 0. 结论
- ## 1. 已核对的当前事实
- ## 2. 最终正常用户到底应得到什么
- ...

它并没有候选 1.8 新正式要求的：

## 1. 用户决策说明

而 v0.11 当前准备写入正式 Planner/Critic 1.8 的核心能力恰恰要求：

- important architecture Proposal 有同版、可定位的用户决策说明；
- final Critic PASS 实际审该同版说明；
- 最终 technical PASS 后测试 Critic -> Planner receiving path。

因此存在两种都不合格的情况：

A. candidate Critic严格执行新 1.8：
旧 Case C package缺必需的同版 reader object，应 REVISE；
则它无法承担 final PASS -> Planner acceptance 正控。

B. 为了让 Case C PASS而给旧 package grandfather exemption：
则正控没有真正验证本次新增的同版说明与 receiver机制。

不能把这个决定留到看到 Case C 输出后再选。

最小关闭条件：

在执行前重新冻结一个“结构上有资格按 1.8 获得 PASS”的复杂正控，并保持 fail-closed。

优先考虑：

- 使用当前 v0.11/v0.12 自身的完整 execution-ready package作为已见复杂正向路径回归：它已经含同版用户决策说明，并且当前 1.7 final review可提供历史真实技术结论；candidate 1.8实现后可重新完整审查，不沿用旧 verdict；
- 或冻结另一个在测试开始前已经满足 1.8同版 reader-object要求的真实复杂 package。

无论选哪个：

- 必须在 candidate生成输出前冻结 exact package；
- 旧 PASS不自动有效；
- fresh candidate Critic发现真实 blocker时必须 REVISE；
- 不得测试失败后换样本；
- 必须真实走
  Critic technical PASS
  -> NEXT_HANDOFF=PLANNER
  -> Planner delivery acceptance
  -> short COPY TO CODEX
  的完整链；
- Planner不得生成第二技术 PASS或增加新事实；
- 旧 055 package仍可以保留为历史复杂技术审查/兼容性材料，但不要称它为新 receiver机制的唯一正向 PASS控制。

正式 main 后的“新发生真实任务”继续保留为最终默认入口/泛化验证；它不需要在当前设计阶段凭空制造，也不能由新的正控替代。

其余 Validation Contract 继续保留：

A：
Clear Writing旧错误 execution-ready package负控。

B：
Phase C真实非终态交接。

D：
真实 Slurm多轮技术更替。继续使用真实历史：

- request_user_input/PostToolUse 的旧设计；
- 后续方案更替；
- 正式 slurm-workflows 0.5 的 PreToolUse/PermissionRequest + parallel mcp_tool。
  用户部分认可的 Wrapper→Hook说明仍只作开发参考，不是技术历史或质量金标准。

正式 main 后新任务：
保持 NOT_VERIFIED，直到真实新任务自然出现。

不得增加更多同义样本、固定字数/英文比例/标题数或机器文本评分器。

其它正确 execution boundary 保留：

- 当前 design branch HEAD 就是 reviewed package：
  3b3a66411b99872b329657529a133745db0114e8
- 不新建 /tmp 正式工作树；
- 当前实际 workspace/branch 不匹配时只做安全 preflight 后 STOP，不自行切换/改拓扑；
- Git ordinary commit/push/main integration只有用户真正发送最终批准入口后才进入授权；
- 不 force/rewrite history；
- 不付费；
- 不操作 Slurm/Plugin Creator/Personal Plugin；
- post-implementation Critic只给 PROCEED_TO_FINAL_EVALUATION / REVISE；
- candidate source改变使旧 evaluation失效；
- main相关竞争修改/conflict/readback mismatch时停止；
- 只有 remote main确认两份正式角色合同为同一受审1.8候选，才可说正式源升级；
- 新真实任务出现前不得声称长期默认可靠已验证。

外部方法核查不改变这两个 blocker：
AWS ADR实践支持 owner维护、版本化、审查决策记录；
OpenAI instruction hierarchy支持高层合同优先，但不是不可绕过runtime guarantee。
这支持总体架构，不支持让 Codex自己从历史设计拼出当前正式合同。

下一步请形成完整 v0.12 Proposal / Execution Plan / Goal / Kickoff / Validation Contract / final Critic prompt。

第一屏自然中文说明：

- v0.10总体接收架构继续保留；
- DV11-01如何把所有最终1.8语义重新冻结进当前包；
- DV11-02采用什么正控并为什么现在真实可测试；
- 用户永久新增成本仍只有唯一技术PASS后一次机械转发；
- 验证期临时fresh Web UI成本另外如实说明；
- 当前正式main仍为1.7；
- 用户现在不需要实施动作。

完成后自动生成新的完整 COPY TO CRITIC，要求对整个 v0.12 execution-ready package重新做最终审查。

本轮不得启动 Codex、不得修改main、不得实施1.8。

=== COPY TO PLANNER END ===
~~~
