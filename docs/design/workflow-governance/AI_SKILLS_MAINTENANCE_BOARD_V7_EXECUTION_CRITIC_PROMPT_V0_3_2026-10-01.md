# Maintenance Board v7 — Lifecycle Drift Reconciliation Critic/Reviewer Prompt v0.3

你是 AI Research Stack 的独立 Critic / Reviewer。

当前只复核 Maintenance Board v7 execution package v0.3 是否关闭 Stage A implementation review 的唯一 blocker：

BOARD-V7-AUDIT-CLOSURE-DEADEND-01

不要重新设计 v7 taxonomy / Forms / pre-admission Action / audit / hierarchy / label-cutover / Longleaf execution route，不实现 v6.1，不执行任何 GitHub mutation。

Repository:
YuukiAS/AI_Skills_Collection

Task:
repo--maintenance-board-issue-maturity

Review stage:
EXECUTION_CONTRACT_REVIEW_AFTER_STAGE_A_BLOCKER

Approved v7 design:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md
commit:
3d091421c7afe8d4f90687ef6e0ce2686bcaf426

Stage A reviewed functional candidate:
c6202533b7617a4eec95eca60accd4d2c620192f

Stage A implementation review:
results/repo--maintenance-board-issue-maturity/IMPLEMENTATION_REVIEW.md
review commit:
78bb326a73aaa1cd44aeb17414648ae0b89c90bc

Exact v0.3 package snapshot:
69d2acb8f7c846dfc83405a016b96fbdc14362ce

Plan:
docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_3_2026-10-01.md

Goal:
docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_3.md

Kickoff:
docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_KICKOFF_V0_3.md

## 必须读取

latest main:
- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

reviewed Stage A evidence:
- results/repo--maintenance-board-issue-maturity/IMPLEMENTATION_REVIEW.md
- results/repo--maintenance-board-issue-maturity/PRE_MIGRATION_ISSUE_METADATA.json

exact v0.3 snapshot:
- Plan
- Goal
- Kickoff

## 已接受，不重新打开

- approved v7 taxonomy/source-of-truth split
- Forms + blank route
- tiny issues:opened / issues:write Action
- classification before mutation
- ambiguous kind fail closed
- read-only metadata audit
- native sub-issues/dependencies only
- v0.2 pre-publication label cutover
- stale auto-close forbidden
- v6.1 independence
- Repository bump NONE / all plugins NO_BUMP
- Longleaf_Codex primary execution route

## Blocker evidence to recheck

Stage A directly proved:

Completed + Project DONE + missing Resolution commit:
#53 #54 #55 #56 #57 #58 #59 #63 #64 #65

Duplicate + Project DONE:
#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72

The live audit is intentionally strict and would fail these rows.

v0.3 chooses truthful reconciliation rather than weakening/grandfathering the audit.

## 重点复核

### R1 — completed Resolution commit rule

v0.3 allows setting Resolution commit only when existing durable closure evidence directly binds:

- the exact tracked Issue / canonical source / closure task
- to an exact owner-repo commit SHA.

It explicitly rejects chronology/title/file-touch/PROMOTED/release-only inference.

If any one of the ten completed Issues lacks direct support:
- action must be BLOCKED_NO_TRUTHFUL_REPAIR;
- the whole repair stops before mutation;
- G7 remains blocked.

判断这个 evidence standard 是否足够严格，且不会为了 audit PASS 猜 commit。

### R2 — duplicate false-DONE repair

For:
#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72

v0.3 only authorizes:
- keep CLOSED / DUPLICATE;
- remove Project item from AI Skills Maintenance;
- verify absence;
- no Resolution commit;
- no reopen/reclose;
- no source TODO/tracking mutation.

这是否忠实 canonical false-DONE rule？

如果 auto-add re-adds the item, package要求 stop，而不是擅自删 maintenance-track / 改 Issue state。

### R3 — no unreviewed live repair

v0.3 requires:

1. LIFECYCLE_DRIFT_PRE_REPAIR.json
2. LIFECYCLE_DRIFT_RECONCILIATION_PLAN.json
3. independent reconciliation-plan review PASS
4. live repair
5. LIFECYCLE_DRIFT_POST_REPAIR.json
6. independent lifecycle-repair review PASS
7. only then G7

检查这是否真正避免 Stage A -> G7 的 deterministic dead-end，同时没有把普通 taxonomy migration 变成新的状态机。

### R4 — rollback

Completed repair rollback:
- restore exact pre-repair Resolution value.

Duplicate repair rollback:
- re-add same Issue to same Project;
- restore exact pre-repair Area / Status / Resolution.

Issue state/reason, maintenance-track, source TODO, tracking:#N never change.

Rollback back to historical drift does not claim validity; G7 stays blocked.

判断 rollback 是否真实可恢复 partial mutation，而不制造新的 false truth。

### R5 — audit contract

v0.3 explicitly keeps audit logic unchanged.

No grandfathering.
No exception suppression.
Final live audit must still PASS after taxonomy migration.

确认这是正确选择，而不是要求重新设计 audit。

### R6 — mutation scope

This repair may mutate only:
- Resolution commit Project field on the 10 reviewed completed Issues;
- Project membership of the 11 reviewed duplicate Issues.

It may not mutate:
- Issue state/title/body
- Project Area
- source TODO
- tracking:#N
- taxonomy labels during this repair
- Issue #4 consumer semantics
- other Issues

检查 scope 是否足够窄。

### R7 — G7 gating

G7 remains unauthorized until executed lifecycle repair itself has independent PASS.

Check Plan / Goal / Kickoff all say the same thing.

### R8 — environment

Primary environment remains Longleaf_Codex.

Workstation / CUHK_Workstation_WSL_Codex outage does not block this GitHub metadata repair or later v7 work.

This is routing only, not a machine-consumer adaptation change.

## 输出

如果 package仍有真实 blocker：

RESULT = REVISE
REVIEW_STAGE = EXECUTION_CONTRACT_REVIEW_AFTER_STAGE_A_BLOCKER
PACKAGE_SNAPSHOT_COMMIT = 69d2acb8f7c846dfc83405a016b96fbdc14362ce
READY_FOR_CODEX = NO
RECHECKED_BLOCKERS = BOARD-V7-AUDIT-CLOSURE-DEADEND-01

给 stable blocker、direct evidence、causal risk、minimum close condition。
不要重新打开已接受 v7 architecture。

如果 blocker关闭：

先用自然中文说明：
- completed commit evidence rule是否足够truthful；
- duplicate repair是否符合false-DONE；
- independent review sequence是否足够；
- rollback是否成立；
- audit是否仍完整；
- G7为何现在有合法前置repair route。

然后输出：

RESULT = PASS
REVIEW_STAGE = EXECUTION_CONTRACT_REVIEW_AFTER_STAGE_A_BLOCKER
PACKAGE_SNAPSHOT_COMMIT = 69d2acb8f7c846dfc83405a016b96fbdc14362ce
RECHECKED_BLOCKERS = BOARD-V7-AUDIT-CLOSURE-DEADEND-01
CLOSED_BLOCKERS = BOARD-V7-AUDIT-CLOSURE-DEADEND-01
NEW_BLOCKERS = NONE
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_3_2026-10-01.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_3.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_KICKOFF_V0_3.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX

然后逐字输出 snapshot 中 reviewed v0.3 Kickoff，不要临场改写。

特别说明：
这个 PASS 只批准 lifecycle drift repair continuation。
它不代表 reconciliation plan已找到所有 Resolution commits，也不代表 repair已经执行，更不授权 G7；G7必须等待后续 reconciliation-plan review + executed-repair review PASS。

## Review-file authorization

用户发送本 prompt，即授权你只在 latest main 新增：

docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_3_2026-10-01.md

并 ordinary non-force push。

除此之外禁止修改 Proposal / Plan / Goal / Kickoff / Issue / Project / labels / .github / scripts / source。
