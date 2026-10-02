你现在执行 AI Skills Maintenance Board 最终剩余 consumer 的一次性 closure。

Repository:
YuukiAS/AI_Skills_Collection

Canonical task:
repo--maintenance-board-lifecycle

Tracking Issue:
#4

Current consumer:
CUHK_Workstation_WSL_Codex

Canonical checkout:
 /home/yuukias/AI_Skills_Collection

Task branch:
reviewed/repo--maintenance-board-lifecycle

Exact worktree:
 /home/yuukias/AI_Skills_Collection-repo--maintenance-board-lifecycle

这是最终 closure continuation，不是新 task，不重新设计，不重跑 Longleaf，不重跑 v7。

只有在主 final-closure package 已获得 execution-ready Critic PASS，Longleaf stage 已完成并已把 v6.1/current required-set truth 集成 latest main 后，才运行本 prompt。

==================================================
一、preflight：latest main 与 current truth
==================================================

先：

1. cd /home/yuukias/AI_Skills_Collection
2. git fetch origin
3. verify clean canonical checkout
4. verify latest origin/main
5. 读取：
   - AGENTS.md
   - docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
   - results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md
   - results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.md
   - results/repo--maintenance-board-lifecycle/FINAL_REQUIRED_CONSUMER_SET_2026-10-02.json
   - results/repo--maintenance-board-lifecycle/FINAL_CLOSURE_STATUS_2026-10-02.md
   - results/repo--maintenance-board-issue-maturity/V7_FINAL_CLOSURE.md
   - Issue #4 live state

必须确认：

- canonical policy §14 已是 evidence-backed actual normal-entry / explicit fallback semantics；
- §15 已是 quantity-neutral required-consumer aggregate truth；
- §16 仍是 generic all required consumers closure；
- CURRENT_REQUIRED_SET exactly:
  AI Research Stack ChatGPT Project instructions,
  Longleaf_Codex,
  CUHK_Workstation_WSL_Codex
- Project instructions = PASS
- Longleaf_Codex = PASS
- CUHK_Workstation_WSL_Codex = PENDING
- Longleaf_Backup_Codex / Workstation / Legion 不是当前 #4 closure prerequisite
- Issue #4 = OPEN / ADAPTING
- v7 = COMPLETE
- latest metadata audit prior evidence = PASS

任何一项不符：
STOP_FINAL_CLOSURE_PRECONDITION_DRIFT
不要重跑 Longleaf / v7，不要自行重新设计 required set。

==================================================
二、verify exact consumer identity
==================================================

确认当前环境：

consumer = CUHK_Workstation_WSL_Codex
platform = WSL
canonical repo = /home/yuukias/AI_Skills_Collection

确认：

- current user / HOME / CODEX_HOME
- codex executable/version
- current repo remote = YuukiAS/AI_Skills_Collection
- latest origin/main checkout可读
- GitHub repo/project mutation能力可用

不要使用旧 machine-update PASS 代替本轮 latest board-contract verification。

==================================================
三、fresh normal-entry read-only smoke
==================================================

运行一次 fresh ordinary Codex repo-entry smoke。

目标：
证明一个 fresh Codex 正常进入 current AI_Skills_Collection repo 时，会实际消费 latest AGENTS + current Maintenance Board policy。

fresh request语义必须等价于：

“只读检查当前 AI_Skills_Collection 的维护看板正常入口。读取 repo 的 AGENTS.md 和 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md，不修改任何文件或 GitHub 状态。报告：
1. 当前 Project active auto-add filter；
2. machine-consumed/shared-maintenance required consumer 如何选择；
3. Issue #4 当前 remaining required consumer；
4. 用户是否需要手工维护 Kanban。”

期望至少明确：

- active admission = is:issue is:open label:maintenance-track
- required consumers = actual normal-entry + explicitly promised fallback
- fixed-five global default = NO
- Issue #4 final remaining consumer = CUHK_Workstation_WSL_Codex
- user manual Kanban maintenance required = NO

该 fresh smoke 必须 read-only。
保存：

- fresh session id
- exact request
- exact output
- source main SHA
- codex version

如果 fresh normal entry没有消费latest contract：
CONSUMER_STATUS = FAIL
Issue #4保持ADAPTING
停止，不做aggregate closure。

==================================================
四、durable WSL PASS evidence
==================================================

使用同一个 canonical task branch。

如果 remote branch不存在或不能安全continue：
停止，不新建successor task。

如果 branch存在且是latest main ancestor/compatible continuation：
- fast-forward到latest main
- materialize：
  /home/yuukias/AI_Skills_Collection-repo--maintenance-board-lifecycle

创建：

results/repo--maintenance-board-lifecycle/FINAL_CONSUMER_CUHK_WORKSTATION_WSL_CODEX_2026-10-02.md

results/repo--maintenance-board-lifecycle/FINAL_CONSUMER_CUHK_WORKSTATION_WSL_CODEX_2026-10-02.json

必须记录：

CONSUMER = CUHK_Workstation_WSL_Codex
STATUS = PASS
LATEST_MAIN = <exact SHA used>
NORMAL_ENTRY_CONSUMED_BOARD_CONTRACT = YES
FRESH_SESSION = <id>
AUTO_ADD_OPEN_ONLY = PASS
EVIDENCE_BACKED_REQUIRED_SET = PASS
CURRENT_REQUIRED_SET_MATCH = YES
USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO

不要执行 AI Skills Maintainer machine-update campaign。
本轮只验证 Maintenance Board current contract consumption。

==================================================
五、current aggregate truth
==================================================

更新：

results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md

只更新/追加 CURRENT_REQUIRED_SET section，不删除历史五 consumer evidence。

改成：

Project instructions = PASS
Longleaf_Codex = PASS
CUHK_Workstation_WSL_Codex = PASS

ALL_REQUIRED_CONSUMERS = PASS

同时更新：

results/repo--maintenance-board-lifecycle/FINAL_CLOSURE_STATUS_2026-10-02.md

明确：

CURRENT_REQUIRED_SET =
AI Research Stack ChatGPT Project instructions,
Longleaf_Codex,
CUHK_Workstation_WSL_Codex

ALL_REQUIRED_CONSUMERS = PASS_OR_NA
FINAL_REMAINING_CONSUMER = NONE
ISSUE_4_READY_FOR_COMPLETED_CLOSE = YES

==================================================
六、final repo checks
==================================================

运行 existing Maintenance Board metadata audit against current live Project。

必须：

ok = true
violation_count = 0

同时 verify：

- v7 closure commit 700234d7e94bb5613f951b8adeb7155d3b15ec3f 在 latest main ancestry
- Project auto-add = is:issue is:open label:maintenance-track
- #93仍 Project DOING / standalone-skill，canonical tracking source存在
- historical duplicates没有false-DONE
- Issue #4仍OPEN / ADAPTING / Area=repo
- Issue #4 taxonomy labels正确
- README check完成
- no production plugin source changes
- no repository/plugin version bump

任何 failure：
不要 close #4。

==================================================
七、final evidence commit
==================================================

只提交 final consumer / aggregate closure evidence与允许的current handoff更新。

ordinary non-force push task branch。

将 exact final closure evidence ordinary non-force integrate to latest main。

verify remote main。

这个 exact integrated commit = FINAL_RESOLUTION_COMMIT。

保存 exact SHA。

==================================================
八、Clear Writing + Issue #4 final copy
==================================================

在任何 reader-facing Issue #4 mutation 前，真实调用当前安装的 Clear Writing / writing-style。

Issue #4 final copy必须自然中文表达：

- Maintenance Board central implementation已完成；
- v7 Issue maturity已完成；
- current canonical consumer contract已从旧fixed-five改为evidence-backed actual normal-entry / explicit fallback；
- CURRENT_REQUIRED_SET exactly:
  AI Research Stack ChatGPT Project instructions,
  Longleaf_Codex,
  CUHK_Workstation_WSL_Codex；
- 三项全部PASS；
- Longleaf_Backup_Codex / Windows Workstation / Legion只保留为历史handoff/machine-update evidence，不是current closure prerequisite；
- #92/#93/#94与metadata audit证明normal daily path；
- 用户不需要手工拖Kanban；
- Resolution commit = FINAL_RESOLUTION_COMMIT；
- durable evidence locators清楚可见；
- 下一步 = 无，本Issue完成。

不得删除历史证据，只更新当前进度/当前锚点/下一步为final truth。

==================================================
九、Project Resolution + completed close
==================================================

写：

Project #4 Resolution commit = FINAL_RESOLUTION_COMMIT

read back exact value。

然后：

close Issue #4
state reason = completed

等待/读取 existing issue-closed -> DONE workflow。

必须 verify：

ISSUE_4 = CLOSED / COMPLETED
PROJECT_4_STATUS = DONE
PROJECT_4_AREA = repo
PROJECT_4_RESOLUTION_COMMIT = FINAL_RESOLUTION_COMMIT

如果 close 后 Project不是DONE：
不要伪装complete，报告exact blocker。

==================================================
十、final latest-main / workspace readback
==================================================

最后确认：

- origin/main = expected latest final evidence commit ancestry
- canonical policy v6.1 semantics存在
- v7 = COMPLETE
- metadata audit = PASS / 0
- #4 closed completed / Project DONE
- current required set全部PASS
- README check完成
- task worktree clean
- canonical checkout无未授权dirty state

最终输出exactly包含：

MAINTENANCE_BOARD_PROJECT = COMPLETE
ISSUE_4 = CLOSED_COMPLETED
PROJECT_4_STATUS = DONE
CURRENT_REQUIRED_SET = AI Research Stack ChatGPT Project instructions, Longleaf_Codex, CUHK_Workstation_WSL_Codex
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
V6_1_CANONICAL_POLICY = IMPLEMENTED
V7 = COMPLETE
KANBAN_NORMAL_ENTRY = PASS
USER_MANUAL_KANBAN_MAINTENANCE_REQUIRED = NO
README_CHECK = <PASS result>
REPOSITORY_BUMP = NONE
PLUGIN_BUMP = NONE
FINAL_RESOLUTION_COMMIT = <exact SHA>

禁止：
- rerun Longleaf
- rerun v7
- successor task
- machine registry/controller
- new watcher/daemon/database
- production plugin mutation
- v6.1 redesign
- fixed-five reintroduction
