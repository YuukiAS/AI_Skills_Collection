你现在执行 AI Skills Maintenance Board 最终收口 v0.2。

Repository:
YuukiAS/AI_Skills_Collection

Canonical task:
repo--maintenance-board-lifecycle

Tracking Issue:
#4

Exact branch:
reviewed/repo--maintenance-board-lifecycle

Exact worktree:
../AI_Skills_Collection-repo--maintenance-board-lifecycle

Primary environment:
Longleaf_Codex

只有当独立 execution-ready Critic 对 exact v0.2 package PASS，且我随后实际发送本 Kickoff，才形成执行授权。

必须读取 latest main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_GOAL_V0_2.md
- results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md
- results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md
- results/repo--maintenance-board-issue-maturity/V7_FINAL_CLOSURE.md
- results/repo--maintenance-board-issue-maturity/METADATA_AUDIT.json
- Issue #4
- Issue #92 / #93 / #94 only as needed for final evidence

不要等待或访问 Workstation / WSL。
不要做任何 machine adaptation。

==================================================
一、冻结 current required set
==================================================

CURRENT_REQUIRED_SET =

1. AI Research Stack ChatGPT Project instructions
2. Longleaf_Codex

两项都必须从 current durable evidence read back 为 PASS。

以下仅为 historical evidence，不是 #4 current closure prerequisite：

- CUHK_Workstation_WSL_Codex
- Longleaf_Backup_Codex
- Windows Workstation
- Legion

特别注意：

CUHK_Workstation_WSL_Codex 不标 PASS，也不标 outage-based N/A。
它是 NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT。

不得重新生成 WSL handoff。
不得等工位恢复。

==================================================
二、exact branch / worktree
==================================================

若 remote reviewed/repo--maintenance-board-lifecycle 不存在，
允许从 execution-time latest origin/main 创建这个 exact branch。

worktree：
../AI_Skills_Collection-repo--maintenance-board-lifecycle

禁止：
- successor task
- alternate branch/worktree
- /tmp fallback
- dirty canonical checkout
- force push/history rewrite

==================================================
三、实现 v6.1 canonical policy
==================================================

只修改 current normative：

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

§14：
删除 global fixed-five default。

改成：

required consumers =
actual normal-entry consumers
+ explicitly promised fallback environments
needed for the tracked item's frozen completion claim。

某台机器不能仅因：
- 装 AI Skills Maintainer
- 出现在别的 machine-update matrix
- 有 Codex
- 能 clone repo
自动 required。

fallback 只有 explicit product promise 才 required。

ADAPTING freeze evidence-backed set。
evidence ambiguous -> stay ADAPTING / return Planner。
不为了保险多加机器，也不能漏掉明确承诺环境。

§15：

保留 per-current-consumer Maintainer boundary。

将 fixed-five aggregate wording 改成：

当前 tracked item 的 required-consumer 聚合真值属于 tracking Issue / Project lifecycle。

§16：

保持 generic：

all required consumers PASS/N/A
+ durable evidence
+ Resolution commit
+ tracking Issue completed close
+ issue-closed workflow -> DONE

历史 Proposal / Review / Goal / Kickoff 不改。

==================================================
四、保留历史 handoff，追加 current truth
==================================================

修改：

results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md

不得删除旧五 consumer evidence。

追加：

HISTORICAL_HANDOFF_MATRIX

CURRENT_REQUIRED_SET — 2026-10-02

Project instructions = PASS
Longleaf_Codex = PASS

CURRENT_NON_REQUIRED_HISTORICAL_CONSUMERS

CUHK_Workstation_WSL_Codex = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Longleaf_Backup_Codex = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Workstation = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Legion = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT

每项附 direct evidence locator。

==================================================
五、final evidence
==================================================

创建：

results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.md

results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.json

results/repo--maintenance-board-lifecycle/FINAL_CLOSURE_STATUS_2026-10-02.md

必须记录：

CURRENT_REQUIRED_SET_FROZEN = YES
PROJECT_INSTRUCTIONS = PASS
LONGLEAF_CODEX = PASS
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
FINAL_REMAINING_CONSUMER = NONE
ISSUE_4_READY_FOR_COMPLETED_CLOSE = YES

==================================================
六、Longleaf PASS readback
==================================================

不要重跑 Longleaf adaptation。

必须确认 current evidence仍成立：

- #92 v7执行记录绑定 Longleaf_Codex
- v7 final closure commit =
  700234d7e94bb5613f951b8adeb7155d3b15ec3f
- V7_FINAL_CLOSURE = COMPLETE
- latest METADATA_AUDIT ok=true / violation_count=0
- #93 是真实 tracked Issue，Project DOING / standalone-skill，source backlinks存在
- #94 pre-admission smoke已PASS
- Project auto-add仍open-only
- duplicate false-DONE不存在

如果 current readback直接矛盾：
stop，返回 Planner/Reviewer。

==================================================
七、independent implementation review
==================================================

branch 上准备：

- canonical policy diff
- CONSUMER_HANDOFFS current section
- final closure evidence
- Issue #4 final reader-facing draft
- metadata audit evidence
- README check

然后停止 main integration / Issue mutation，交 independent Reviewer。

Reviewer必须返回：

FINAL_CLOSURE_IMPLEMENTATION_REVIEW = PASS

CURRENT_REQUIRED_SET =
AI Research Stack ChatGPT Project instructions,
Longleaf_Codex

ALL_REQUIRED_CONSUMERS = PASS_OR_NA

ISSUE_4_READY_FOR_COMPLETED_CLOSE = YES

MAIN_INTEGRATION_AUTHORIZED = YES

REVISE -> 当前 package内修复并重新review。

==================================================
八、main integration + final Issue #4 closure
==================================================

Reviewer PASS 后：

1. ordinary non-force integrate reviewed branch到 latest main
2. verify remote main
3. 保存 exact integrated final-evidence commit = FINAL_RESOLUTION_COMMIT
4. invoke Clear Writing
5. 更新 Issue #4 final reader-facing copy，明确：
   - central Maintenance Board complete
   - v7 complete
   - fixed-five已被v6.1 evidence-backed contract替代
   - CURRENT_REQUIRED_SET = Project instructions + Longleaf_Codex
   - 两项PASS
   - WSL / Longleaf_Backup / Windows Workstation / Legion是historical evidence，不是current prerequisite
   - 用户不需要手工拖Kanban
   - Resolution commit + durable evidence visible
   - next action = none
6. write Project #4 Resolution commit = FINAL_RESOLUTION_COMMIT
7. close Issue #4
   state reason = completed
8. verify issue-closed workflow -> Project DONE
9. verify Area=repo
10. verify Resolution commit exact
11. run final metadata audit
12. final latest-main readback
13. workspace clean

==================================================
九、normal-use final acceptance
==================================================

不创建新 synthetic Issue。

使用现有：

- #92 v7 completed
- #93 real standalone-skill tracked Issue
- #94 historical pre-admission smoke
- latest metadata audit
- actual Project readback
- open-only auto-add

最终 claim：

real feedback
-> canonical TODO
-> tracking:#N
-> Issue / Project
-> Area / lifecycle
-> proactive Planner/Critic/Maintainer/Codex sync
-> truthful DONE/non-completion

USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO

这不表示bot自动猜 lifecycle。

==================================================
十、禁止
==================================================

禁止：

- 等待/访问 Workstation / WSL
- machine adaptation
- v7 redesign/rerun
- production plugin source mutation
- new lifecycle / Project field
- machine registry/controller/watcher/daemon/database
- new Skill/Plugin/Profile
- Bridge Kit mutation
- successor task
- fixed-five reintroduction

Repository bump = NONE
all plugins = NO_BUMP
Production Plugin Capability Gate = NOT REQUIRED

==================================================
十一、成功输出
==================================================

MAINTENANCE_BOARD_PROJECT = COMPLETE
ISSUE_4 = CLOSED_COMPLETED
PROJECT_4_STATUS = DONE
CURRENT_REQUIRED_SET = AI Research Stack ChatGPT Project instructions, Longleaf_Codex
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
V6_1_CANONICAL_POLICY = IMPLEMENTED
V7 = COMPLETE
KANBAN_NORMAL_ENTRY = PASS
USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO
README_CHECK = <PASS>
REPOSITORY_BUMP = NONE
PLUGIN_BUMP = NONE
FINAL_RESOLUTION_COMMIT = <exact SHA>

任何 required truth不能直接验证就停止并报告，不得伪装complete。
