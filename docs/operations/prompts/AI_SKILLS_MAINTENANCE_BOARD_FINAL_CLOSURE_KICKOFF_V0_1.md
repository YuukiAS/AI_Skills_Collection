你现在执行 AI Skills Maintenance Board 最终收口 v0.1。

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

只有当独立 execution-ready Critic 对 exact v0.1 package PASS，且我随后实际发送本 Kickoff，才形成执行授权。

必须读取 latest main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_GOAL_V0_1.md
- results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md
- results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md
- results/repo--maintenance-board-issue-maturity/V7_FINAL_CLOSURE.md
- results/repo--maintenance-board-issue-maturity/METADATA_AUDIT.json
- results/workflow-core--reviewed-first-bootstrap-normal-entry/RESULT.md
- Issue #4 current live state
- Issue #92 / #93 / #94 only as required by the final Plan

不要重新设计 v7，不要实现新的机制。

==================================================
一、冻结 current required set
==================================================

本 package 冻结：

CURRENT_REQUIRED_SET =
1. AI Research Stack ChatGPT Project instructions
2. Longleaf_Codex
3. CUHK_Workstation_WSL_Codex

Current states：

AI Research Stack ChatGPT Project instructions = PASS
Longleaf_Codex = PASS
CUHK_Workstation_WSL_Codex = PENDING

FINAL_REMAINING_CONSUMER =
CUHK_Workstation_WSL_Codex

当前不 required：

Longleaf_Backup_Codex
Windows Workstation
Legion

不得因为旧 five-machine matrix 重新纳入它们。

不得因为 Workstation 当前掉线把 WSL 自动判 PASS / N/A / non-required。

==================================================
二、exact branch/worktree
==================================================

当前 remote reviewed/repo--maintenance-board-lifecycle 若不存在，
允许从 execution-time latest origin/main 创建 exact branch。

worktree 必须解析为 canonical checkout 的 exact sibling：

../AI_Skills_Collection-repo--maintenance-board-lifecycle

记录 resolved absolute path。

禁止：
- alternate task/branch
- /tmp fallback
- dirty canonical checkout
- force push/history rewrite
- successor task

==================================================
三、实现 v6.1 canonical policy
==================================================

只修改 current normative：

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

§14：
删除 global fixed-five default。

改成 approved v6.1：

required consumers =
actual normal-entry consumers
+ explicitly promised fallback environments
needed for this tracked item's frozen completion claim。

某机器不能仅因：
- 安装 AI Skills Maintainer
- 出现在另一个 product machine-update matrix
- 有 Codex
- 能 clone repo
自动 required。

fallback 只有 explicit product promise 才 required。

ADAPTING 时 freeze evidence-backed required set。
evidence ambiguous -> stay ADAPTING / return Planner。
不为了保险多加环境，也不能漏掉明确承诺环境。

§15：
保留 per-current-consumer Maintainer boundary。

把 fixed-five aggregate wording 改成：

当前 tracked item 的 required-consumer 聚合真值属于 tracking Issue / Project lifecycle。

§16：
保持 all required consumers PASS/N/A generic closure 不变。

current canonical policy 若还有 direct normative fixed-five sentence，
只做 v6.1 quantity-neutral convergence。

不要改历史 Proposal / Review / Goal / Kickoff。

==================================================
四、CONSUMER_HANDOFFS 保留历史，追加 current truth
==================================================

保留：

results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md

既有历史五 consumer evidence 不删除、不改写。

追加 clearly labeled：

HISTORICAL_HANDOFF_MATRIX
CURRENT_REQUIRED_SET — 2026-10-02
CURRENT_NON_REQUIRED_HISTORICAL_CONSUMERS

CURRENT_REQUIRED_SET：

Project instructions = PASS
Longleaf_Codex = PASS
CUHK_Workstation_WSL_Codex = PENDING

Non-required historical：

Longleaf_Backup_Codex
Workstation
Legion

每项附 direct evidence locator。

==================================================
五、final closure evidence
==================================================

创建：

results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.md

results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.json

results/repo--maintenance-board-lifecycle/FINAL_CLOSURE_STATUS_2026-10-02.md

WSL前必须记录：

CURRENT_REQUIRED_SET_FROZEN = YES
PROJECT_INSTRUCTIONS = PASS
LONGLEAF_CODEX = PASS
CUHK_WORKSTATION_WSL_CODEX = PENDING
ALL_REQUIRED_CONSUMERS = NOT_YET_PASS_OR_NA
ISSUE_4_STATUS = ADAPTING

==================================================
六、Longleaf PASS 只用 current direct evidence
==================================================

不要重跑 Longleaf adaptation。

只在 execution-time readback仍成立时冻结 PASS：

- Issue #92 记录 v7 在 Longleaf_Codex 执行
- v7 closure commit = 700234d7e94bb5613f951b8adeb7155d3b15ec3f
- V7_FINAL_CLOSURE = COMPLETE
- latest METADATA_AUDIT ok=true / violation_count=0
- #93 是真实 Project tracking Issue，Project DOING / standalone-skill，source backlinks已存在
- #94 证明 pre-admission route 没有误入 Project

若 current evidence contradiction：
stop，返回 Planner/Reviewer，不自动重跑 v7。

==================================================
七、独立 implementation review
==================================================

Longleaf 先完成 branch 上的：

- v6.1 policy diff
- CONSUMER_HANDOFFS current section
- final required-set evidence
- final WSL prompt
- Issue #4 proposed current-truth draft
- metadata audit / README check evidence

然后停止 live Issue #4 mutation和main integration，交 independent Reviewer。

Reviewer必须 PASS：

FINAL_CLOSURE_IMPLEMENTATION_REVIEW = PASS

CURRENT_REQUIRED_SET =
AI Research Stack ChatGPT Project instructions,
Longleaf_Codex,
CUHK_Workstation_WSL_Codex

FINAL_REMAINING_CONSUMER =
CUHK_Workstation_WSL_Codex

MAIN_INTEGRATION_AUTHORIZED = YES

REVISE -> 在当前 package内修复并重新review。

==================================================
八、Longleaf main integration + Issue #4 current truth
==================================================

Reviewer PASS 后：

1. ordinary non-force integrate reviewed repo changes 到 latest main
2. verify remote main
3. invoke Clear Writing
4. 更新 Issue #4 reader-facing current truth
5. 明确：
   - central implementation complete
   - v7 complete
   - fixed-five contract已被v6.1 evidence-backed semantics替代
   - Project instructions PASS
   - Longleaf PASS
   - WSL唯一pending
   - Longleaf_Backup / Workstation / Legion只是historical evidence
6. Issue #4 保持 open
7. Project #4 保持 ADAPTING / Area=repo
8. readback Issue + Project

不要等 WSL 才做这些工作。

==================================================
九、WSL 不可用时
==================================================

如果 CUHK Workstation / WSL 仍不可用：

- 到这里停止
- Issue #4 保持 ADAPTING
- Longleaf work保持有效
- 不回滚 policy/current truth
- 不要求用户继续做设计判断

用户只需等 WSL恢复后，把 package 内 exact prompt：

docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_FINAL_REMAINING_CONSUMER_CUHK_WSL_V0_1.md

发给该 WSL Codex 一次。

==================================================
十、WSL prompt 是同一个最终 Goal 的 continuation
==================================================

WSL prompt 已经属于本 Critic-reviewed package。

不得另开 successor task。
不得重新 Planner/Critic 设计。

该 prompt 必须：
- verify latest main
- verify current v6.1 policy
- verify only WSL remains pending
- run one fresh ordinary read-only Codex repo-entry smoke
- prove latest Maintenance Board contract consumed
- write durable WSL PASS evidence
- automatically complete aggregate closure
- not rerun Longleaf
- not rerun v7

==================================================
十一、final aggregate closure
==================================================

WSL PASS 后同一 WSL action：

1. update current CONSUMER_HANDOFFS:
   Project instructions PASS
   Longleaf PASS
   WSL PASS
2. update FINAL_CLOSURE_STATUS_2026-10-02.md
3. run current metadata audit
4. README check
5. add final evidence on same canonical task branch
6. ordinary non-force integrate to main
7. use exact integrated final-evidence commit as Issue #4 Resolution commit
8. invoke Clear Writing
9. update Issue #4 final reader-facing copy
10. write Project Resolution commit
11. close Issue #4 completed
12. verify Project Status DONE
13. verify Area=repo
14. verify Resolution commit exact
15. final latest-main readback
16. workspace clean

No rerun Longleaf/v7。

==================================================
十二、normal-use final acceptance
==================================================

不要创建新的 synthetic Issue。

使用：

- #92 v7 completed
- #93 real tracked standalone-skill Issue
- #94 existing pre-admission acceptance evidence
- latest metadata audit
- actual Project readback
- current open-only auto-add

最终必须证明：

real feedback
-> canonical TODO
-> tracking:#N
-> Issue / Project
-> Area / lifecycle
-> proactive Planner/Critic/Maintainer/Codex sync
-> truthful DONE/non-completion handling

USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO

==================================================
十三、禁止
==================================================

不允许：

- production plugin source mutation
- v7 redesign / rerun
- new lifecycle / Project field
- machine registry
- cross-machine controller
- watcher / daemon / scheduled reconciler / database
- new Skill / Plugin / Profile
- Bridge Kit mutation
- successor task
- fixed-five reintroduction
- 把Workstation outage当理由自动N/A WSL

Repository bump = NONE
all plugins = NO_BUMP
Production Plugin Capability Gate = NOT REQUIRED

==================================================
十四、成功最终输出
==================================================

MAINTENANCE_BOARD_PROJECT = COMPLETE
ISSUE_4 = CLOSED_COMPLETED
PROJECT_4_STATUS = DONE
CURRENT_REQUIRED_SET = AI Research Stack ChatGPT Project instructions, Longleaf_Codex, CUHK_Workstation_WSL_Codex
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
V6_1_CANONICAL_POLICY = IMPLEMENTED
V7 = COMPLETE
KANBAN_NORMAL_ENTRY = PASS
USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO
README_CHECK = <PASS>
REPOSITORY_BUMP = NONE
PLUGIN_BUMP = NONE

如果任何 required truth无法直接验证，停止并报告exact blocker，不得伪装complete。
