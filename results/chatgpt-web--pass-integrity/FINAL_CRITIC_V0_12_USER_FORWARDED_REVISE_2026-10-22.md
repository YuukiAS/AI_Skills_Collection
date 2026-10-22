# 用户转交的 v0.12 最终 execution-ready Critic REVISE 原文

日期：2026-10-22  
任务：`chatgpt-web--pass-integrity`  
所审包：`b328c2051691bd8084bf4e5e1feb08527b850251`  
结论：`REVISE`  
新 blocker：`DV12-01 = CURRENT_FINAL_REVIEW_AUTHORITY_TIME_CYCLE`

来源边界：原 Critic 没有向仓库写 review commit；以下是当前用户在 Planner 线程转交的本轮实际独立审查 authority，按原文归档。本提交由 Planner 保存，不冒充 Critic 自己的 GitHub commit。

---

~~~text
继续 AI Research Stack 同一治理任务：

target_repo=YuukiAS/AI_Skills_Collection
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4

review_stage=FINAL_EXECUTION_READY_REVIEW_V0_12
reviewed_package_commit=b328c2051691bd8084bf4e5e1feb08527b850251
critic_verdict=REVISE
READY_FOR_CODEX=NO

previous_blockers:
DV11-01=CLOSED
DV11-02=CLOSED

new_blocker:
DV12-01=OPEN

当前正式 main：
f1de8e85957d32a50f4458349f450ec65add13bb

正式 Planner/Critic 仍为 1.7。不得实施 1.8，不得启动 Codex。

本轮 Critic 未向 repo 写 review commit。以用户转交的本段原文作为本轮 Critic authority，如实归档，不得伪造 Critic Git commit。

一、已经确认关闭的部分

DV11-01 已关闭。

v0.12 Execution Plan 已经把最终 Planner/Critic 1.8 所需语义完整冻结为当前规范，不再要求 Executor 从旧 v0.7 拼装：

Planner:
- P18-0 current source / user decision identity
- P18-1 task-specific Critic prompt compatibility
- P18-2 short Codex handoff renderability
- P18-3 critical-interface reality evidence
- P18-3a pre-side-effect probe
- P18-3b conditional capability
- P18-4 non-terminal handoff closure
- P18-5 Critic-result receiving / delivery acceptance
- P18-6 final technical PASS delivery acceptance
- P18-7 explanation / contradiction / new requirement

Critic:
- C18-0 review identity / independent source reading
- C18-1 task-prompt compatibility hard gate
- C18-2 atomic technical PASS
- C18-3 PASS follow-up classification
- C18-4 critical-interface evidence hard gate
- C18-5 whole-response acceptance
- C18-6 user-decision/source consistency
- C18-7 self-contained receiver handoff

以及：
- GOVERNANCE_CANDIDATE_COMMIT
- candidate-defining source变化使旧 evidence失效
- 当前规范性 eight-case deterministic replay
- fresh Web user-only boundary
- post-implementation Critic safety gate
- main integration + remote readback

future C18-2 也已经无歧义：

Critic technical PASS + READY_FOR_CODEX=YES
-> NEXT_HANDOFF=PLANNER
-> Planner delivery acceptance
-> short COPY TO CODEX
-> user sends
-> Codex

旧 future NEXT_HANDOFF=CODEX 已明确 REPLACED BY。

同时 bootstrap boundary 正确：
这一次“实施 1.8 自身”的 execution-ready review仍服从当前正式 1.7；未来真正获 PASS 时，本次启动入口仍应 direct COPY TO CODEX。

不要再修改这些语义。

DV11-02 也已关闭。

新的 Case C 逻辑成立：

- 不再使用结构上缺少 ## 1. 用户决策说明 的历史 055 包作为 receiver 正控；
- 只有当前 v0.12 exact package真正获得 current 1.7 execution-ready PASS 后，才存在 IMPLEMENTATION_APPROVED_PACKAGE；
- exact value 必须是 Critic实际审过并 PASS 的 package commit；
- 必须在任何 candidate 1.8 Web output 前冻结；
- candidate 1.8 Critic重新完整审该包；
- old current-1.7 PASS只作历史证据，不决定 candidate verdict；
- 真实 blocker => REVISE；
- 不换样本；
- candidate真正 technical PASS 后才能测试：
  NEXT_HANDOFF=PLANNER
  -> Planner delivery acceptance
  -> short COPY TO CODEX；
- Planner不得产生第二 technical PASS、新增技术事实或扩大授权。

历史 055 继续只作复杂兼容材料即可。

二、唯一新 blocker：DV12-01

问题名称：

CURRENT_FINAL_REVIEW_AUTHORITY_TIME_CYCLE

当前 v0.12 Kickoff：

docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_12_2026-10-22.md

在“唯一当前包”中要求同一 PACKAGE_COMMIT 包含：

“当前 Critic 最终 review 的真实完整回复/归档 locator”

这是时间上不可能成立的。

当前审查对象：

PACKAGE_COMMIT=
b328c2051691bd8084bf4e5e1feb08527b850251

该 commit 必须在 Critic开始本轮 review之前冻结。

而本轮 final Critic review只有在读取并审完该 commit之后才产生。

因此：

PACKAGE_COMMIT
不可能同时预先包含
“审查这个 PACKAGE_COMMIT 后才产生的 final Critic review”。

不能通过后续修改同一个 package解决，因为一旦修改就产生新的 commit，而原 Critic PASS绑定的就不是那个新 commit。

如果保持当前文本并给 PASS，Codex启动后只能：
- 忽略 Kickoff 这一要求；
- 自己猜 Critic authority；
- 或因缺少 impossible locator停止。

三者都不允许。

三、最小修复

不要重新设计 1.8，不要再改 DV11-01 / DV11-02。

形成 v0.13，只修 approval authority 的时序。

明确区分两个 identity：

A. IMPLEMENTATION_APPROVED_PACKAGE

这是 Critic审查前已经冻结的 immutable package：

IMPLEMENTATION_APPROVED_PACKAGE=
<exact v0.13 PACKAGE_COMMIT>

它包含：
- Proposal
- Execution Plan
- Goal
- Kickoff Draft
- Validation Contract
- final Critic prompt
- package manifest
- 历史 review authorities

它不能、也不需要包含未来才产生的 current final Critic reply。

B. BOOTSTRAP_CRITIC_AUTHORITY

这是 Critic审完 IMPLEMENTATION_APPROVED_PACKAGE 后产生的独立批准 authority。

只有 final Critic真正：

PASS
READY_FOR_CODEX=YES

时才存在。

它至少必须由当前 1.7 的最终回复/短 handoff自包含冻结：
- reviewed_package_commit
- review_stage
- verdict
- READY_FOR_CODEX
- approved Proposal/Plan/Goal/Kickoff locators
- 当前执行授权边界
- 必要的 technical approval identity / limitations

如果现有 surface能合法保存完整 Critic原文，可在执行开始后按真实内容归档，并明确“这是 package 后产生的 evidence”，不能声称它属于原 package commit。

如果当前 Critic不能写 repo：
- 不要求用户手工建 review file；
- 不伪造 review commit；
- 当前 short COPY TO CODEX 必须携带 Codex启动所需的真实 Critic authority；
- Codex可在已授权 task scope内把实际收到的 authority如实保存到 results，前提是它真的收到了这些内容。

关键点：
不要要求短 COPY TO CODEX 携带整篇 Critic自然中文全文。

Case C 需要的是：
- exact IMPLEMENTATION_APPROVED_PACKAGE；
- current bootstrap Critic确实 PASS + READY；
- exact authority identity /限制。

candidate 1.8 后续会独立重新审 package，不应依赖 bootstrap Critic全文替它做判断。

如果你认为后续验证必须保存本轮完整 Critic自然中文回复，则必须额外冻结一个现实可行的传输入口，并如实计算用户动作成本；不能再次要求它预先存在于 package commit。

四、同步修正这些文件

只需形成完整同版 v0.13：
- Proposal
- Execution Plan
- Goal
- Kickoff Draft
- Validation Contract
- final Critic prompt
- package manifest

重点统一：
1. 删除任何“PACKAGE_COMMIT 必须包含当前尚未产生的 final Critic review”的语义；
2. 明确 package identity 与 post-review approval authority 是两个按时间顺序产生的对象；
3. Case C 的 IMPLEMENTATION_APPROVED_PACKAGE 仍是 current Critic真正 PASS 的 exact package；
4. current Critic REVISE 时不存在 approved package，不得启动；
5. candidate 1.8重新独立审 approved package，不沿用 bootstrap verdict；
6. 不增加额外 Planner/Critic技术批准；
7. 不新增服务、schema、数据库或后台归档器。

五、其它设计全部保持

继续保留当前 v0.12：
- 同版 ## 1. 用户决策说明
- Planner receiver acceptance
- Critic独立技术 authority
- future PASS -> Planner -> Codex
- 全部 P18/C18
- eight deterministic cases
- A/B/C/C2/D/E
- post-implementation safety gate
- fresh Web user-only boundary
- candidate identity
- main integration/readback
- F 新真实任务 NOT_VERIFIED claim ceiling

用户永久新增成本仍应是：
future唯一 technical PASS后多一次机械转发给现有 Planner。

candidate验证期的临时 fresh Web UI成本单独说明。

不要修改：
- Project setting
- Capability Gate Policy
- AGENTS.md
- Clear Writing
- Slurm
- Bridge Kit
- Mica
- Plugin Creator
- 其它 Plugin/生产系统

不要新增：
- 第三人工角色
- service/watcher/daemon
- database/state machine
- prompt compiler
- paid model
- 浏览器拦截

六、下一步

形成完整 v0.13 execution-ready package后，再交独立 Critic做整个包的最终重审，不只复核 DV12-01。

Planner面向用户先讲清：
- v0.12 两个旧 blocker都已关闭；
- 新问题只是 final Critic authority 的时序自引用；
- v0.13怎样把 immutable package 与 post-review authority 分开；
- 总体架构没有再改；
- 当前正式 main仍是1.7；
- 用户现在不需要实施动作。

然后自动生成完整 COPY TO CRITIC。

本轮不得实施1.8、不得启动Codex、不得修改main。

=== COPY TO PLANNER END ===
~~~
