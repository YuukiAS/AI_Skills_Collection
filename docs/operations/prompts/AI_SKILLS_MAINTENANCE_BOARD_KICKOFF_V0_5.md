你现在执行 AI Skills Maintenance Board central implementation v0.5。只执行已经通过 v5 design review、并按 execution Critic v0.4 唯一 blocker 修订后的 v0.5 central stage；不要重新设计 lifecycle。

Repository:
YuukiAS/AI_Skills_Collection

Exact task identity:

task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle

必须读取并遵守：

- AGENTS.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_CRITIC_REVIEW_2026-09-24.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_4_2026-09-24.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_5_2026-09-24.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_5.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md

只有当独立 Critic 对这套 v0.5 package 给出 READY_FOR_CODEX=YES，且我随后实际发送这段 Kickoff，才形成当前执行授权。

我发送本 Kickoff，即授权以下 exact bounded central effects：

1. kickoff preflight 先冻结 unmodified base：
   - fetch kickoff-time latest origin/main
   - 记录 exact KICKOFF_BASE_COMMIT
   - 直接读取该 exact commit 的 root TODO.md，而不是任何 task-mutated copy
   - 只解析 root TODO 中正式声明 canonical maintenance inbox 的结构化导航 entries
   - 不把 explanatory prose、example links、changelog/workflow links 当 inbox declaration
   - 验证每个解析 path 在同一 base commit 存在
   - 得到 exact frozen canonical inbox path list

2. 从同一 KICKOFF_BASE_COMMIT 创建：
   - branch: reviewed/repo--maintenance-board-lifecycle
   - worktree: ../AI_Skills_Collection-repo--maintenance-board-lifecycle
   ordinary non-force commit/push 到 exact task branch。

3. 在任何其他 task tracked-file mutation、GitHub Project/Issue creation 或 backfill 前，把 frozen inbox list 作为本 task 第一份内容证据写入：

   results/repo--maintenance-board-lifecycle/FROZEN_CANONICAL_INBOX_ALLOWLIST.md

   至少记录：

   KICKOFF_BASE_COMMIT = <exact SHA>
   ROOT_TODO_BLOB_SHA = <exact SHA>
   FROZEN_INBOX_COUNT = <N>

   FROZEN_CANONICAL_INBOX_PATHS =
   - <exact path 1>
   - <exact path 2>
   ...

   该文件只是本 task 的 bounded evidence，不是长期 registry、service 或 runtime source。

4. 这份 frozen path list 是本 task **唯一**的 canonical-inbox locator-write authority。

   后续即使本 task 修改 root TODO.md：
   - 不得扩大这份 allowlist
   - 不得根据 task-mutated TODO.md 重新计算 locator write scope
   - 即使 task 自己新增一个 inbox declaration，该新 path 也不自动获得 write authority
   - rename/remove 也不允许把 authority静默转移到另一个 path

   如果 kickoff 后 upstream main 新增 canonical inbox：
   - 不自动纳入本 task
   - 如果该 inbox 必须纳入本次 bootstrap，按 semantic-drift / scope-expansion contract返回 Planner/用户
   - 否则留给后续 maintenance work并在 closure evidence记录

   不创建 watcher、动态 allowlist service 或 registry。

5. 在 GitHub 账号 YuukiAS 下创建或复用唯一 private Project：
   AI Skills Maintenance
   并只链接：
   YuukiAS/AI_Skills_Collection

6. 创建/更新这个 Project 已批准的：
   - Status = TODO / DOING / ADAPTING / DONE
   - Area
   - Resolution commit
   - Board / Active / By area / History
   - maintenance-track label
   - issue-only auto-add
   - approved built-in workflows

7. BOARD-01 必须保持关闭：
   - lifecycle item 只能是 maintenance-track Issue
   - auto-add 至少 is:issue label:maintenance-track
   - implementation/design PR 不作为 lifecycle item
   - Project pull request merged -> Done 必须 disabled
   - DONE 前禁止会 auto-close tracking Issue 的 Development/manual linked relationship
   - DONE 前 PR body / commit message 不得对 tracking Issue 使用 close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved
   - repository-wide auto-close 保持原样
   - issue closed -> Done 只作完整 closure 后最后机械动作
   - rejected/superseded/duplicate/not-planned item 不得显示为 DONE

8. 做一次完整 bootstrap，但范围只等于第 3 条 frozen allowlist：
   - 扫描 frozen list 中全部 canonical plugin / standalone-skill / other maintenance inbox
   - 每个仍有维护意义的 entry 都有 disposition
   - valid central raw NEW 可以成为 Project TODO，但 source maturity仍保持 NEW
   - duplicate 合并到同一个 top-level tracking Issue
   - PROJECT_LOCAL / REJECTED / SUPERSEDED / historical resolved 不机械上板，但必须进入 coverage evidence
   - 创建：
     results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md
   - 不把 TODO_COVERAGE 发展成长期 registry/schema/ledger
   - 不机械一 heading 一 Issue

   本次 completeness claim 只覆盖 frozen kickoff-base inbox allowlist，不覆盖 kickoff 后新出现的 inbox。

9. 对 disposition 为 TRACKED 或 MERGED_INTO_TRACKING_ISSUE 的每个 canonical source entry，必须在**同一 maintenance action**写入或更新：

   tracking: #<issue-number>

   规则：
   - independent entry -> own top-level tracking Issue
   - duplicate/merged entries -> 多个 source entries 可共享一个 Issue
   - reuse existing Issue -> 回写 actual reused Issue number
   - merge/rebind -> 更新 affected entries 到真实 current Issue
   - raw NEW maturity保持 NEW
   - Project Status 不得回写 Markdown

10. locator-only authority严格只适用于第 3 条 frozen allowlist 中的 exact paths，而且只能新增/更新：

    tracking: #<issue-number>

    不得借此修改：
    - source maturity/status
    - problem
    - evidence
    - project-specific context
    - target layer
    - candidate action
    - promotion gate
    - 任何其他 substantive TODO field
    - Project lifecycle Status

    non-tracked dispositions 不得为了 completeness 强行加 locator。

    如果 existing tracking locator 与 current真实 mapping冲突且无法无歧义判断，停止该 entry并报告 locator conflict；不得猜测/rebind。

11. TODO_COVERAGE.md 继续只是一轮 bootstrap completeness evidence。
    steady-state durable source -> Issue mapping 必须来自 canonical source entry 自己的：
    tracking: #N

12. tracking Issue / Project 是用户直接看的 artifact。
    每个 tracking Issue：
    - title 必须自然、简洁
    - 顶部固定：
      问题：
      当前进度：
      当前执行锚点：
      下一步：
    - DOING / ADAPTING 至少有一个 current valid anchor
    - detailed evidence/history 放后面
    - Board / By area 至少直接显示 human-readable title + Area + Status
    - DONE / History 直接显示 Resolution commit

13. 只要你创建或实质修改 Kanban / Project 的 reader-facing copy，必须在 GitHub mutation 前真实调用当前安装的 Clear Writing（writing-style）。

    Clear Writing 不得改变：
    - source maturity
    - Project Status
    - Area
    - tracking: #N
    - required-consumer truth
    - exact locators
    - Resolution commit
    - evidence meaning

    如果当前 Codex runtime 无法真正调用 Clear Writing：
    - 不得假装调用
    - 不得批量写 generic board copy
    - 在该 reader-facing mutation 前停止
    - 报告 CLEAR_WRITING_UNAVAILABLE

14. 在 exact task branch 内只允许修改：
    - AGENTS.md
    - root TODO.md
    - docs/plugin-todos/README.md
    - 新 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
    - docs/workflows/PLANNER_ROLE_CONTRACT.md
    - docs/workflows/CRITIC_ROLE_CONTRACT.md
    - README.md 仅在 closure check 证明确实需要 public-facing 更新时
    - results/repo--maintenance-board-lifecycle/**
    - 当前 task 按现有 Reviewed Handoff contract 真正需要的普通 control/evidence files
    - **FROZEN_CANONICAL_INBOX_ALLOWLIST.md 中列出的 exact inbox paths，且仅用于 tracking: #N locator maintenance**

    root TODO 后续修改不得扩大最后一项。

15. canonical board policy 只能完整存在于：
    docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

    其他 consumer 只加 short trigger/locator：
    - AGENTS: Codex normal entry
    - PLANNER_ROLE_CONTRACT: triage / first substantive Plan / handoff / ADAPTING cutover reconcile
    - CRITIC_ROLE_CONTRACT: review locator / next action / lifecycle truth reconcile
    - TODO / plugin TODO README: inbox vs Project + tracking locator

    canonical board doc必须明确：
    create/bind/reuse tracking Issue
    -> 同一 maintenance action回写/更新 source tracking: #N

    Issue merge/rebind
    -> 更新所有受影响 canonical source entries 到真实 current Issue

    不复制完整 policy。

16. no-tool surface 必须保留 semantic ownership。
    如果 Planner/Critic/GPT 当前不能修改 GitHub Project：
    - 更新自己能合法更新的 Issue/source evidence
    - 已知 binding 且有 repo write authority时保持 source tracking: #N 正确
    - 输出 exact pending Project mutation
    - 不得声称已经同步
    - 不得要求用户手工拖 Kanban或手工补 tracking locator

    下一 Project-capable maintenance action 应先核对 mutation 仍属于 current tracking Issue、evidence仍 current，再机械应用。

17. 本 board task 自身 tracking Issue 在 central implementation 期间保持 DOING。
    execution-ready Critic PASS 本身不进入 ADAPTING。
    Executor 自报完成也不进入 ADAPTING。

18. Stage A central implementation完成后：
    - push exact task branch
    - 保存真实 Project/config/frozen-allowlist/coverage/source-backlink/surface evidence
    - 停止等待独立 implementation Critic/Reviewer
    - Reviewer必须检查：
      - KICKOFF_BASE_COMMIT / ROOT_TODO_BLOB_SHA / frozen allowlist provenance
      - no locator edit outside frozen list
      - task-mutated root TODO没有扩权
      - TODO_COVERAGE
      - TRACKED/MERGED source backlinks
      - BOARD-01
      - Clear Writing结果
      - actual Project surface
      - role-consumer contract
    - Executor summary不能替代 review

19. 独立 implementation Reviewer PASS后，如果 latest main没有语义冲突，本 Kickoff已授权同一 central scope内：
    - fetch latest main
    - ordinary non-force integration到 main
    - verify remote main
    - README closure check
    不需要因为到达这一步再次询问同一 Git/main scope。

20. main integration后，必须给 AI Research Stack ChatGPT Project instructions安装下面 exact short trigger/locator：

AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步，并在 canonical source entry 回写/更新 tracking: #N。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。

    如果当前执行环境没有受支持的 ChatGPT Project-settings mutation surface，可以向我提出一次 HUMAN_ONLY 操作：
    Project -> ... -> Project settings -> instructions
    追加上面 exact text。
    我完成后同一 Goal自动继续；以后 routine sync不再重复问。

21. 如果 GitHub built-in Project workflow配置仍只能通过 UI，而你没有受支持浏览器，可以在 backfill前向我提出一次最小 HUMAN_ONLY GitHub UI操作；完成后必须 read back实际 workflow state，再继续同一 Goal。

22. central implementation complete 的条件是：
    - canonical board policy已落地
    - AGENTS / Planner / Critic short consumer rules已落地
    - TODO ownership docs已落地
    - frozen kickoff-base inbox allowlist evidence已落地并通过验证
    - 每个 TRACKED / MERGED source entry都有正确 durable tracking: #N
    - no locator edit outside frozen allowlist
    - private Project + frozen-inbox bootstrap已完成
    - actual surface qualitative review PASS
    - independent implementation review PASS
    - reviewed repo changes已进入 main
    - ChatGPT Project instructions trigger已安装

    只有这时才把本 task从 DOING切到 ADAPTING，并报告：

    CENTRAL_IMPLEMENTATION_COMPLETE = YES
    FROZEN_INBOX_ALLOWLIST_VERIFIED = YES
    SOURCE_TRACKING_LOCATORS_VERIFIED = YES
    PROJECT_STATUS = ADAPTING
    OVERALL_GOAL_ACHIEVED = NO

23. 进入 ADAPTING时，只解析并冻结当前五个 required logical consumers 的 exact current identities/locators：

    Server / remote Codex:
    - Longleaf_Codex
    - Longleaf_Backup_Codex
    - CUHK_Workstation_WSL_Codex

    Local:
    - Workstation
    - Legion

    这五 consumer requirement只适用于 machine-consumed workflow/shared maintenance mechanism。

    如果 exact identity resolution本身需要访问某台 machine，先经过该 consumer bounded authorization gate；不得无授权访问或猜 locator。

24. AI Skills Maintainer只能是 per-current-consumer adaptation executor，不是 cross-machine controller。
    每个 consumer后续在自己的 current Codex environment运行 future production-ready Maintainer，或走另行批准的 existing remote route。

    Maintainer只负责当前 consumer：
    - discovery
    - adaptation/update
    - installed/loaded identity
    - fresh-session / normal-entry verification
    - durable evidence
    - current-consumer PASS/truthful blocker

    五 consumer aggregate truth属于 tracking Issue / Project。

25. 本 Kickoff **不授权**任何 server/local machine adaptation。
    central implementation complete后：
    - 生成 exact per-consumer Maintainer handoff(s)
    - 等待对应 current-user machine/credential/remote authority
    - Project保持 ADAPTING
    不得为了 DONE静默访问机器或扩大 remote authority。

26. 最终 DONE不是本 initial central Kickoff执行范围。
    只有未来 tracking Issue聚合确认五个 required consumers全部 PASS/N/A，并有 durable evidence、Resolution commit、completed close，才能：
    ADAPTING -> DONE

    单台 Maintainer PASS不得关闭 top-level Issue。

27. 本任务 central stage明确禁止：
    - 根据 task-mutated root TODO动态扩大 frozen locator-write scope
    - 对 frozen allowlist外文件做 locator write
    - locator-only authority下修改 source maturity/problem/evidence/project-specific context/target layer/candidate action/promotion gate
    - skills/ production source修改
    - AI Skills Maintainer source修改
    - machine-update-orchestrator source修改
    - Marketplace/generated payload/profile修改
    - standalone Kanban skill
    - kanban-sync skill
    - new plugin/profile
    - board-specific MCP/service
    - cross-machine controller
    - machine registry
    - watcher/daemon
    - allowlist service
    - central credential broker
    - GitHub Action/database/ledger/controller/new state machine
    - Bridge Kit修改
    - server/local-machine/Host mutation
    - paid API
    - force/destructive Git
    - Project publication
    - repository-wide auto-close disable

28. Version：
    Repository bump decision = NONE
    all plugins = NO_BUMP

    tracking: #N 与 frozen allowlist evidence 都只是 maintenance metadata/evidence，不改变 plugin runtime。

    README必须 closure check；private Project默认预期：
    README checked: no update required

如果 exact worktree无法合法创建、kickoff-base root TODO的 canonical inbox declaration无法无歧义解析、GitHub身份/权限不符、project scope不可取得、Clear Writing unavailable、Project workflow无法验证、Project exact-title冲突、tracking locator冲突无法无歧义解析、post-kickoff新增 inbox 必须纳入本 task、出现语义 main drift，停止并报告 exact blocker；不得换路径、换分支、扩大权限、猜 locator或静默降级。

central stage不得声称 OVERALL_GOAL_ACHIEVED=YES。只有未来五 consumer aggregate closure才能最终 DONE。
