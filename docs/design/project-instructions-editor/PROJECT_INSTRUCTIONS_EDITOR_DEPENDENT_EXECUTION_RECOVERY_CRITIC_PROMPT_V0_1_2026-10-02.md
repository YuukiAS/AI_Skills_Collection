# Critic Prompt — Project Instructions Editor Dependent Execution Recovery v0.1

你现在负责对 project-instructions-editor standalone Skill implementation 的 dependent-execution recovery package 做独立 Critic 审查。

这不是产品重设计，也不是重新审四个 Capability Gate。产品/架构 design freeze、implementation package v0.2 和原 Gate taxonomy 保持有效。

## Active Review Context

target_repo:
YuukiAS/AI_Skills_Collection

target_plugin_or_domain:
standalone Skill / project-instructions-editor

design_topic_or_task_key:
project-instructions-editor--standalone-skill-implementation

source_branch_or_ref:
main

execution branch:
work/project-instructions-editor--standalone-skill-implementation

execution worktree:
../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation

review_stage:
dependent-execution recovery review after current-main drift

approved implementation Plan:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md

approved Goal:
docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_2.md

approved Kickoff:
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_2.md

prior implementation review:
results/project-instructions-editor--standalone-skill-implementation/IMPLEMENTATION_REVIEW.md

dependent blocker evidence:
results/project-instructions-editor--standalone-skill-implementation/R3_PRECHECK_BLOCKER.md

dependent blocker Critic review:
results/project-instructions-editor--standalone-skill-implementation/DEPENDENT_EXECUTION_BLOCKER_REVIEW.md

blocker-review commit:
ebbebee0c42f93d362811594a829bc336a481e8f

recovery Plan:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md

recovery Resume Draft:
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RESUME_V0_1.md

recovery package commit:
0cc2abb061ab95655b95bc22846f3aef8877f40c

tracking:
Issue #93

current unresolved review findings:
R1
R2

R3 status:
SUPERSEDED_BY_CURRENT_MAIN_SYNC

VERSION_DRIFT:
YES

READY_FOR_GATES=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO

如果 package commit 后 main 只有本 recovery 的 handoff/docs drift，使用最新真实 main，不回退。

## 必须先读取

读取 latest main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/skill-todos/project-instructions-editor.md
- VERSION
- scripts/codex_marketplace_config.json
- tests/test_candidate_plugin_replay.py

读取 approved implementation Plan / Goal / Kickoff。

读取 task branch 当前：

- R3_PRECHECK_BLOCKER.md
- DEPENDENT_EXECUTION_BLOCKER_REVIEW.md
- IMPLEMENTATION_REVIEW.md
- G4_COMPLETE_TASK_REVIEW.md

主要审查：

- PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md
- PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RESUME_V0_1.md

按需要核对 exact task branch current HEAD 与 main merge base。

不要重新做产品设计审查。

## 1. 先核对 current facts

Planner 规划时观察：

origin/main =
4ce1946ba047ea200c4ab41ae824de999ef535ed

main VERSION =
5.4.1

main workflow-core =
0.5

main shared replay timeout =
3

task branch HEAD =
ebbebee0c42f93d362811594a829bc336a481e8f

merge base =
98721a202bc557c0b9c0800e66e50cab466bfba2

task branch 当时相对 main：
ahead 8 / behind 14

task branch 当时仍有：

VERSION = 5.5.0
workflow-core = 0.4
shared replay timeout = 0.5

如果 current main 又前进，使用最新真实事实判断 recovery，不要求回到这些旧 SHA。

## 2. 审原 R3 的 supersede 归因

Recovery Plan 不再把 0.5 当成固定正确值。

它要求：

Project Instructions Editor task 不拥有 shared replay timeout；
同步 latest main 后继承 latest main 的 timeout；
不得在本 task 内重判 0.5 / 2 / 3 的优劣。

请判断：

- 这是否正确关闭旧 R3 的 scope 问题；
- 是否仍有 task-specific shared-test behavior残留；
- 是否避免把 current-main正式变化误当成本任务 regression。

若成立，记录：

R3_SUPERSEDE_DECISION=PASS

注意：这不表示 implementation overall PASS；R1/R2仍 OPEN。

## 3. 审 VERSION_DRIFT 修正

approved release type 保持：

Repository bump decision = MINOR
standalone project-instructions-editor = 0.1
central plugins = NO_BUMP

Recovery 只把 baseline 从 5.4.0 更新到 current main。

若 current main仍为 5.4.1：

candidate = 5.5.0
release delta = 5.4.1 -> 5.5.0

必须保留：

- 5.4.1 release history；
- workflow-core 0.5；
- current-main central plugin versions；
- current-main shared tests/source/generated facts。

请检查：

- 5.5.0 target是否仍符合已接受 MINOR decision；
- recovery 是否会错误覆盖 current-main 5.4.1 history；
- workflow-core 0.5 是否明确受到保护；
- 如果 main 再次 version drift，是否正确返回 Planner而不是 Executor猜版本。

## 4. 审 branch synchronization route

Recovery 只允许：

same exact task branch/worktree
-> fetch latest main
-> ordinary history-preserving merge origin/main into task branch
-> bounded conflict resolution
-> ordinary non-force task branch publication

明确禁止：

- rebase；
- force push / force-with-lease；
- successor branch；
- new clone；
- remote remap；
- destructive reset/clean/restore；
- task branch merge回 main。

请检查：

- 对已推送且 diverged 的 exact task branch，这是否是最小、合法、不改写历史的恢复路线；
- 是否需要任何新的 branch/worktree/user authorization；
- Resume Draft 是否已经把 ordinary merge 的授权边界写清。

如果 Git/Bridge current contract 与此存在直接冲突，请给 current source 与最小关闭条件，不要引入新 workflow。

## 5. 审 conflict-resolution boundary

current main owns：

- workflow-core source/version/generated plugin；
- all central plugin current versions；
- shared replay tests；
- current-main release history；
- unrelated main changes。

Project Instructions Editor task owns：

- new Skill source；
- focused test；
- standalone baseline entry；
- Skill card/icon；
- generated registry/catalog/provenance identity；
- 5.5.0 candidate addition；
- task evidence history。

generated conflicts must be regenerated source-first.

请检查是否足够防止两类错误：

1. task candidate把 main 的 workflow-core 0.5 / 5.4.1 等正式状态回滚；
2. merge conflict粗暴选择 main 导致 Project Instructions Editor candidate丢失。

不要要求全仓手工逐文件冲突表，除非有具体当前冲突证明本边界不足。

## 6. 审 C2 formation

Recovery 要求：

main synchronization
-> candidate-owned reconciliation
-> deterministic/full validation
-> all candidate-owned content stable
-> create FINAL_CANDIDATE_COMMIT=C2

旧 C 只作历史。

之后：

C2
-> install from C2
-> G1
-> G2
-> G3
-> G4 full packet
-> zip from C2
-> evidence-only commits
-> EVIDENCE_HEAD=E2
-> prove C2..E2 no candidate-owned changes
-> independent Reviewer

请检查这是否继续满足 same-final-candidate contract。

不得允许 old C Gate PASS 直接拼接成 C2 PASS。

## 7. 审 R1 continuity

R1 保持 OPEN。

Recovery 没有缩小 G4要求。

新的 C2 G4 packet必须逐字保存：

- exact natural user request；
- full live Project-setting baseline；
- targeted history；
- deletion/rejection evidence，包括 nightly-build deletion；
- exact budget/headroom；
- all canonical sources；
- actual AGENTS.md content或 exact repo-safe copy + stable hash；
- source identities/hashes；
- fresh session/runtime identity；
- complete output；
- output length；
- non-independent self-check boundary。

Executor仍只能：

G4_READY_FOR_INDEPENDENT_REVIEW=YES
G4=NOT_CLAIMED_BY_EXECUTOR

请检查 main sync recovery是否无意放松 R1。

## 8. 审 R2 continuity

R2 保持 OPEN。

C2 的 G1 必须在 relevant neighboring owners actually discoverable 的正常环境里覆盖：

ordinary Chinese prose -> chinese-prose
ordinary writing fidelity -> writing-fidelity
scientific rewrite -> scientific-rewrite
AI_Skills maintenance -> ai-skills-core
complex workflow -> workflow-core
generic agent/system prompt -> not editor
global Custom Instructions -> not editor

每个 runtime case仍要求：

- natural unnamed prompt；
- fresh session；
- actual owner/load evidence；
- user-visible output；
- editor misrouting check。

静态 trigger JSON不能替代。

请检查 recovery没有把 R2偷换成静态测试。

## 9. Gate taxonomy 不重开

仍只有：

G1 — Normal entry / routing boundary
G2 — Core Project editing semantics
G3 — Fidelity / authority / should-not-change
G4 — Representative complete task + qualitative final artifact

本 recovery 不增加 Gate、不改 capability claim、不改 owner。

如果你发现真正因 main sync 新增的 capability risk，必须给直接证据；不要因为发生 merge 就机械新增 Gate。

## 10. 权限边界

Resume Draft 在用户实际发送后才授权：

- exact branch/worktree；
- ordinary non-force main merge into exact task branch；
- bounded conflict resolution；
- candidate reconciliation；
- tests；
- task-local install/fresh Codex gates；
- public-safe evidence；
- zip；
- normal task commits；
- ordinary non-force exact-branch publication。

仍不授权：

- task branch merge回 main；
- release/tag/publish；
- paid API/review；
- private data external transfer；
- live ChatGPT account mutation；
- central Plugin专项 redesign；
- Bridge Kit write；
- force push/rebase；
- remote remap；
- destructive Git；
- watcher/daemon/database/ledger/state machine。

请检查恢复权限是否恰好够用且没有扩大。

## 11. Maintenance state

Issue #93继续：

state=open
maintenance-track
kind:new-capability
scope:standalone-skill
area:standalone-skill

Project target：

Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current execution anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md

若当前没有 Project field mutation surface：
记录 exact pending mutation，不声称已同步，不要求用户手工维护。

Issue reader-facing copy 只有真实调用 Clear Writing 后才可改；无 invocation surface：

CLEAR_WRITING_UNAVAILABLE

## 12. PASS / REVISE

如果 recovery Plan + Resume足以恢复 execution，而不改变产品架构/Gate：

CRITIC_RESULT=PASS
R3_SUPERSEDE_DECISION=PASS
VERSION_DRIFT_RECOVERY=PASS
MAIN_SYNC_ROUTE=PASS
C2_FORMATION_CONTRACT=PASS
R1=OPEN
R2=OPEN
APPROVED_RECOVERY_PLAN_PATH=
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md
APPROVED_RESUME_PATH=
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RESUME_V0_1.md
APPROVED_PACKAGE_COMMIT=
0cc2abb061ab95655b95bc22846f3aef8877f40c
RECOVERY_EXECUTION_APPROVED=YES
READY_FOR_GATES=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
NEXT_HANDOFF=EXECUTOR

READY_FOR_GATES remains NO at the review boundary because C2 does not yet exist. The approved Resume may create C2 and only then proceed to Gate reruns under the already-approved sequence.

按照 Critic Role Contract，在 PASS 回复末尾逐字输出 approved Resume 正文，不要另写一个不同恢复 prompt。

如果 REVISE：

CRITIC_RESULT=REVISE
RECOVERY_EXECUTION_APPROVED=NO
READY_FOR_GATES=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
NEXT_HANDOFF=PLANNER

只允许因 recovery route、version reconciliation、conflict boundary、C2 identity 或权限存在真实执行风险而阻塞。

不要重新审已 PASS 产品架构或因为“还能更详细”扩大本轮。
