你现在继续执行 AI Skills Maintenance Board Issue Maturity v7，但只处理 Stage A implementation review 暴露的 lifecycle metadata blocker。

Repository:
YuukiAS/AI_Skills_Collection

Task:
repo--maintenance-board-issue-maturity

Branch:
reviewed/repo--maintenance-board-issue-maturity

Worktree:
../AI_Skills_Collection-repo--maintenance-board-issue-maturity

Primary environment:
Longleaf_Codex

Stable blocker:
BOARD-V7-AUDIT-CLOSURE-DEADEND-01

只有当独立 execution-ready Critic 对 v0.3 Plan / Goal / 本 Kickoff 返回 READY_FOR_CODEX=YES，且我随后实际发送本 Kickoff，才形成新的执行授权。

必须读取：

- AGENTS.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_3_2026-10-01.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_3.md
- results/repo--maintenance-board-issue-maturity/IMPLEMENTATION_REVIEW.md
- results/repo--maintenance-board-issue-maturity/PRE_MIGRATION_ISSUE_METADATA.json

继续使用现有 reviewed branch / worktree。不要重做已通过的 v7 taxonomy / Forms / Action / audit implementation，除非当前 blocker repair 暴露直接冲突。

==================================================
一、G7 继续禁止
==================================================

在本 blocker 完整关闭前：

G7_LABEL_CUTOVER_AUTHORIZED = NO

不得：

- 创建/reconcile v7 taxonomy labels
- publish Forms / intake Action 到 default main
- taxonomy migrate existing Issues
- 声称 live metadata audit PASS

==================================================
二、冻结已知 drift cohort
==================================================

Completed + Project DONE + missing Resolution commit：

#53 #54 #55 #56 #57 #58 #59 #63 #64 #65

Duplicate + Project DONE：

#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72

先 read back 这 21 个 Issue / Project live state。

若与 Stage A snapshot materially 不一致，停止并报告 exact delta，不自行扩大/缩小 cohort。

==================================================
三、先做 evidence plan，不做 live repair
==================================================

创建：

results/repo--maintenance-board-issue-maturity/LIFECYCLE_DRIFT_PRE_REPAIR.json

results/repo--maintenance-board-issue-maturity/LIFECYCLE_DRIFT_RECONCILIATION_PLAN.json

PRE_REPAIR 对每个 Issue 保存：

- issue number/title
- state/reason
- Project item id
- Project Status
- Project Area
- Resolution commit
- labels
- canonical source locator
- examined closure evidence locators

PLAN 每个 Issue只能是：

SET_RESOLUTION_COMMIT

REMOVE_FROM_PROJECT_AS_NON_COMPLETION

BLOCKED_NO_TRUTHFUL_REPAIR

此阶段不修改 live Project metadata。

==================================================
四、completed Issue Resolution commit 不能猜
==================================================

#53–#59、#63–#65 只有现有 durable closure evidence 明确支持 exact owner-repo commit，才能提议 SET_RESOLUTION_COMMIT。

Evidence 必须同时能直接证明：

- exact commit SHA
- 这个 commit 是同一个 tracked Issue / exact canonical source entry / exact closure task 的 closure/evidence anchor

允许：

- existing Issue body/comment明确写 Resolution/closure commit
- existing RESULT / FINAL_REPORT / closure artifact明确绑定同一 Issue/source并写 exact commit
- existing canonical closure record 同时有同一 identity + exact commit

不允许：

- 按日期猜
- 用 close 前最后一个 commit
- 相关文件 commit
- PROMOTED status
- title similarity
- 未绑定该 Issue 的 release/tag
- 复制别的 Issue Resolution commit

任意 completed Issue 找不到 direct evidence：

- action = BLOCKED_NO_TRUTHFUL_REPAIR
- 整批不 mutation
- 返回 Planner
- 不为了 audit PASS 猜 commit

==================================================
五、duplicate/non-completion repair plan
==================================================

#52、#60–#62、#66–#72：

action = REMOVE_FROM_PROJECT_AS_NON_COMPLETION

只计划：

- Issue继续 CLOSED / DUPLICATE
- 不 reopen / re-close
- 不写 Resolution commit
- 不改 source TODO maturity/evidence/tracking:#N
- 从 AI Skills Maintenance Project 移除 item

这是 canonical false-DONE repair。

==================================================
六、先交独立 reconciliation-plan review
==================================================

完成 PRE_REPAIR + PLAN 后，停止 live mutation。

交独立 Reviewer。

Reviewer必须核对：

- exact 21 cohort
- 每个 completed proposed commit 与 direct evidence
- duplicate remove action
- rollback plan
- 没有 Issue state/source/taxonomy mutation

只有 Reviewer 返回：

LIFECYCLE_RECONCILIATION_PLAN = PASS
LIVE_LIFECYCLE_REPAIR_AUTHORIZED = YES

才可继续 live repair。

如果 REVISE：
- 修 evidence/plan
- re-review
- 不开始 G7

==================================================
七、reviewed live repair
==================================================

仅在 reconciliation-plan PASS 后：

Completed cohort：
- Issue仍 CLOSED / COMPLETED
- Project Status仍 DONE
- Area不变
- 写 exact reviewed Resolution commit
- read back exact field

Duplicate cohort：
- Issue仍 CLOSED / DUPLICATE
- remove Project item
- read back item absent
- 不改 source / tracking:#N

除此之外不授权 Project/Issue mutation。

如果 duplicate item 被 auto-add 重新加入：
- stop
- 不删除 maintenance-track
- 不改 Issue state
- 返回 Planner

==================================================
八、post-repair evidence + independent review
==================================================

创建：

results/repo--maintenance-board-issue-maturity/LIFECYCLE_DRIFT_POST_REPAIR.json

results/repo--maintenance-board-issue-maturity/LIFECYCLE_DRIFT_ROLLBACK.json

results/repo--maintenance-board-issue-maturity/LIFECYCLE_DRIFT_REVIEW.md

必须证明：

- 10 completed Issues仍 CLOSED/COMPLETED
- 10 completed仍 Project DONE
- 10 completed Resolution commit == reviewed exact commit
- 11 duplicate仍 CLOSED/DUPLICATE
- 11 duplicate已不在 Maintenance Project
- source TODO maturity/evidence/tracking:#N 未变
- unrelated Issue/Project metadata未变

再交独立 Reviewer。

只有其返回：

LIFECYCLE_DRIFT_REPAIR = PASS
G7_LABEL_CUTOVER_AUTHORIZED = YES

才进入原 v0.2 G7。

==================================================
九、rollback
==================================================

live repair前必须有完整 rollback metadata。

Completed：
- rollback只恢复 pre-repair Resolution commit 值
- Issue state / Status / Area不变

Duplicate：
- rollback re-add same Issue to same Project
- restore exact pre-repair Area / Status / Resolution values
- Issue state/reason不变
- source不变

maintenance-track永不改变。

rollback只是避免 partial mutation。
若 rollback 到原 drift，audit仍blocked，G7仍禁止。

rollback residual drift -> hard blocker。

==================================================
十、后续 v7 不变
==================================================

Lifecycle repair Reviewer PASS 后，继续原 v0.2：

G7 pre-publication label cutover
-> labels ready
-> main integration
-> taxonomy migration
-> full live metadata audit
-> Forms / Action / search acceptance
-> closure

audit contract不改。
不 grandfather historical violation。
不 suppress known audit failures。

==================================================
十一、环境
==================================================

优先 Longleaf_Codex。

Workstation / CUHK_Workstation_WSL_Codex 掉线不阻塞：

- evidence resolution
- reconciliation review
- lifecycle Project metadata repair
- G7
- Issue migration
- Action smoke
- audit/search

v7仍不是 machine-consumer adaptation。

原有 final live Issue chooser UI bounded handoff规则保持不变。

==================================================
十二、禁止
==================================================

本 amendment 不授权：

- 重设计 taxonomy / Forms / Action / audit
- 修改 audit checks 来 grandfather 这 21 个 drift
- reopen/reclose existing Issues
- 修改 source TODO maturity/evidence/tracking:#N
- 修改 Issue body/title
- 修改 Project Area
- 实现 v6.1
- production plugin source change
- machine adaptation
- repository/plugin version bump

Repository bump = NONE
all plugins = NO_BUMP
Production Plugin Capability Gate = NOT REQUIRED

如果 direct closure evidence不足、cohort drift、Project repair失败、rollback失败或 independent Reviewer不PASS，停止；不得进入G7。
