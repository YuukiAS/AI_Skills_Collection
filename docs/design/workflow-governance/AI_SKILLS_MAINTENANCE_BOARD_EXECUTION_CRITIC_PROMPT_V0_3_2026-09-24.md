# AI Skills 维护看板 — Execution-ready Critic Prompt v0.3

你是 AI Research Stack 的独立 Critic thread。

当前只审已经通过 v5 design amendment 的完整 execution package v0.3 是否忠实、可执行、不过重、不过简，并决定是否 READY_FOR_CODEX。

不要执行，不创建 GitHub Project/Issue，不 backfill，不启动 Codex，不调用 paid API，不修改 ChatGPT Project settings，不修改 server/local machine/Host/Bridge Kit。

## Active Review Context

target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-lifecycle
human_label = AI Skills 维护看板与完成语义
source_branch_or_ref = main
review_stage = EXECUTION_READY_REVIEW_V0_3
package_version = v0.3
package_snapshot_commit = aa0eb3e0e57714013f6de6eeb5d820efda2384cc
execution_branch = reviewed/repo--maintenance-board-lifecycle
execution_worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle

## Approved design

Latest approved Proposal:

docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md

commit:

d14565e152b9b953c76c0722ad6e6343850335a7

Latest design Critic PASS:

docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_CRITIC_REVIEW_2026-09-24.md

commit:

012a43c7edefddd7f071d43425f7be937453f73a

Design blockers already closed and not to be reopened without new direct evidence:

- BOARD-01
- BOARD-UX-01
- BOARD-SYNC-01
- BOARD-CONSUMER-01
- BOARD-MAINTAINER-SCOPE-01

## Exact v0.3 package to review

Implementation Plan:

docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_3_2026-09-24.md

Canonical Goal:

docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_3.md

Kickoff Draft:

docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_3.md

All three are present in package snapshot commit:

aa0eb3e0e57714013f6de6eeb5d820efda2384cc

The older v0.2 execution package is superseded and must not be approved or sent to Codex.

## 必须先读取

最新 main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
- approved v5 Proposal
- v5 Critic PASS
- v0.3 Plan / Goal / Kickoff

按需读取：

- current TODO.md
- docs/plugin-todos/README.md
- docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md
- docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md
- skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md

不要重新设计 machine-update orchestration；只核对 board package 是否忠实消费其 per-current-consumer boundary。

## 1. 核心 lifecycle 必须保持

TODO -> DOING -> ADAPTING -> DONE

并保持：

- Project item = top-level tracking Issue
- plugin/skill TODO = failure/evidence/maturity inbox
- task/workflow = execution evidence
- WAITING/BLOCKED 不是第五状态
- Resolution commit
- Project lifecycle != plugin TODO maturity

请检查 Plan / Goal / Kickoff 三者语义是否一致。

## 2. 第一次 full-inbox bootstrap

v0.3 要求：

- 扫描 root TODO.md 当前声明的全部 canonical central plugin / standalone-skill maintenance inbox
- 每个当前仍有维护意义条目都有 disposition
- valid central raw NEW 可以成为 Project TODO，但 source maturity 保持 NEW
- duplicate dedupe
- PROJECT_LOCAL / REJECTED / SUPERSEDED / historical resolved 不机械上板，但进入一次性 coverage evidence
- 创建 results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md
- TODO_COVERAGE 不是长期 registry/schema
- 不机械一 heading 一 Issue

请重点判断：

1. 是否真正满足用户“第一次把当前所有 TODO 整理清楚”；
2. 是否避免把 Project 变成第二个垃圾山；
3. 是否会把 Project TODO 误当 maturity promotion；
4. coverage evidence 是否足够验收且不过重。

## 3. 用户可读性与 Clear Writing

v0.3 冻结：

- human-readable title
- Issue top summary:
  问题 / 当前进度 / 当前执行锚点 / 下一步
- DOING / ADAPTING 必须有 current valid anchor
- Board / By area 直接显示 title + Area + Status
- DONE / History 显示 Resolution commit
- Codex 创建/实质修改 reader-facing board copy 必须真实调用 Clear Writing（writing-style）
- actual Project-surface qualitative review 才是最终质量依据

请检查是否还有“字段全了但看不懂”的 proxy-PASS 漏洞。

## 4. BOARD-01 execution contract

必须确认：

- lifecycle item only maintenance-track Issue
- issue-only auto-add
- PR merged -> Done disabled
- early auto-closing link/closing keyword prohibited
- repository-wide auto-close 保持不变
- final issue-close -> Done only after full closure
- rejected/superseded/duplicate/not-planned 不显示 DONE

尤其检查 full-inbox backfill 是否可能因为 Issue closure语义重新引入假 DONE。

## 5. GitHub Project bootstrap route

检查 v0.3 是否继续诚实使用：

- gh project supported commands where available
- Projects API / GraphQL where needed
- built-in workflow UI-only fallback when no supported mutation API exists
- project OAuth scope preflight
- actual readback verification

不要求为了 UI-only bootstrap 新增 GitHub Action/service/controller。

如果 Executor没有浏览器，允许一次最小 HUMAN_ONLY GitHub Project workflow setup + same-Goal resume 是否仍合理。

## 6. Normal-entry consumer binding

v0.3 central implementation将创建唯一 canonical：

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

并只在以下位置加 short trigger/locator/consumer rule：

- AGENTS.md
- PLANNER_ROLE_CONTRACT.md
- CRITIC_ROLE_CONTRACT.md
- TODO.md / docs/plugin-todos/README.md

ChatGPT normal entry 通过一次性 Project-instructions exact text。

请检查：

1. 是否只有一份 canonical full policy；
2. AGENTS 是否只做 Codex locator；
3. Planner/Critic 是否真正主动 reconcile；
4. no-tool surface 是否 exact pending mutation，而不是让用户手工拖卡；
5. 是否没有偷偷新增 standalone Kanban skill/plugin。

## 7. ChatGPT Project instructions one-time setup

v0.3 规定：

- canonical board doc 先进入 main
- 然后安装 exact short Project-instructions trigger
- 如果当前 surface不能修改设置，允许一次 HUMAN_ONLY exact-text setup
- 完成后 same Goal resume
- routine sync不再重复问

请审：

- exact text 是否够短、只做 trigger/locator/最低行为；
- 顺序是否正确（main doc存在后再挂 locator）；
- 是否不把用户变成长期维护者；
- 是否存在无法验证安装却声称成功的路径。

## 8. 两层 completion semantics

必须严格区分：

execution-ready Critic PASS
-> Codex implementation
-> independent implementation review PASS
-> canonical owner integration/release closure（若 frozen Goal 要求）
= central implementation complete

对本 board 这种 machine-consumed shared maintenance mechanism：

central implementation complete
-> ADAPTING

execution-ready PASS、Executor自报完成、Reviewer PASS但 canonical closure未完成，都不能进入 ADAPTING。

请检查 v0.3 Stage A/B/C 是否忠实。

## 9. 五个 required logical consumers

当前默认：

Server / remote Codex:
1. Longleaf_Codex
2. Longleaf_Backup_Codex
3. CUHK_Workstation_WSL_Codex

Local:
4. Workstation
5. Legion

v0.3 规定：

- 只适用于 machine-consumed workflow/shared maintenance mechanism
- 普通 domain plugin/pure docs/artifact improvement不自动继承
- 进入 ADAPTING 时才解析并冻结 exact current identities/locators
- future optional consumer不追溯扩大旧 DONE
- N/A必须有 frozen durable reason

请检查是否可验收且没有 stale hardcode。

## 10. AI Skills Maintainer scope

v0.3 必须忠实 v5：

AI Skills Maintainer = per-current-consumer adaptation executor

不是：

- cross-machine controller
- five-machine orchestrator
- machine registry owner
- credential broker

每台 consumer在自己的 current Codex environment运行 future production-ready Maintainer，或走另行批准的 existing remote route。

Maintainer只负责当前 consumer的：

- discovery
- adaptation/update
- installed/loaded identity
- fresh-session/normal-entry verification
- durable evidence
- current-consumer PASS/truthful blocker

五 consumer aggregate truth属于 tracking Issue / Project。

检查 package 是否重新引入跨机 controller倾向。

## 11. Initial Kickoff authorization boundary

这是本轮最需要独立审查的 execution-level边界。

v0.3 Kickoff只授权 central implementation stage，不授权任何 server/local-machine mutation。

理由：

- exact consumer identities 在 ADAPTING cutover才冻结
- machine/credential/remote authority届时才可精确绑定
- future production-ready Maintainer availability届时才真实知道

central stage完成后：

- Project -> ADAPTING
- 生成 exact per-consumer handoff(s)
- 再由用户对新 machine effect做 current-user authorization

请判断：

1. 这是否符合 current repo authorization contract；
2. 是否过窄到导致 central implementation无法完成；
3. 是否正确避免用逻辑 consumer name冒充机器执行授权；
4. 是否不会让用户承担 routine Kanban手工维护。

如果这是合法 downstream authorization gate，不应因为 overall Goal还没 DONE 就判 central v0.3 package不可执行。

## 12. Per-consumer completion mutation

无 Project mutation能力时，Maintainer必须输出至少：

- tracking Issue
- consumer
- exact current consumer identity
- PASS/N/A
- adaptation evidence
- normal-entry evidence
- lifecycle truth
- next action

下一 Project-capable action在应用前核验：

- tracking Issue仍匹配
- frozen consumer identity仍匹配
- evidence未过期
- lifecycle truth compatible

请确认这只是 lightweight handoff，不是新 cross-machine state machine。

## 13. Final DONE

单台 Maintainer PASS不得 close top-level Issue。

只有 tracking Issue聚合确认五个 required consumers全部 PASS/N/A + durable evidence + Resolution commit + completed close，才由 issue-closed workflow变 DONE。

v0.3 initial central Kickoff不得提前设置 Resolution commit或DONE。

## 14. Allowed repo scope / version / README

Central stage允许修改：

- AGENTS.md
- TODO.md
- docs/plugin-todos/README.md
- new docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- README only if closure check proves needed
- results/repo--maintenance-board-lifecycle/**
- ordinary task-control/evidence required by current Reviewed Handoff

明确禁止：

- skills/ production source
- generated Marketplace/plugin payload
- profile
- ai-skills-repository-maintainer source
- machine-update source
- Bridge Kit
- machine mutation
- paid API

Version：

Repository bump decision = NONE
all plugins = NO_BUMP

Project PRIVATE，所以 README默认 no update required。

请按当前 version policy核实。

## 15. Exact branch/worktree / recovery

Exact：

branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle

如果 Host/sandbox无法创建 exact locator，在任何 Project/Issue mutation前 fail closed。

不允许 /tmp / dirty checkout / alternate branch/path。

检查是否与 current AGENTS一致。

## 16. No new board/control plane

必须保持禁止：

- standalone board/Kanban skill
- kanban-sync skill
- new plugin/profile
- board-specific MCP/service
- cross-machine controller
- machine registry
- watcher/daemon
- central credential broker
- GitHub Action/database/ledger/controller/new state machine

现有 owner必须足够。

## 17. Validation是否证明真实能力

v0.3 central review必须看到：

- actual Project configuration
- actual Project workflows
- actual full-inbox coverage
- actual readable Board/By area/Issue surface
- real tracking Issue normal entry
- role/entry consumer rules
- no-tool pending mutation contract
- idempotency
- independent implementation review
- main integration
- Project-instructions one-time setup

然后才允许：

CENTRAL_IMPLEMENTATION_COMPLETE = YES
PROJECT_STATUS = ADAPTING
OVERALL_GOAL_ACHIEVED = NO

请检查是否还存在 Markdown/string/API receipt冒充真实能力的路径。

## 18. 期望输出

如果需要实质修改：

RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW_V0_3
PACKAGE_SNAPSHOT_COMMIT = aa0eb3e0e57714013f6de6eeb5d820efda2384cc
READY_FOR_CODEX = NO

并给 stable blocker ID、直接证据、因果风险、最小关闭条件。不要无新事实重新打开已关闭 design blocker。

然后按 Critic Role Contract自动生成完整 Planner返修 prompt。

如果 execution package 可以开始 central implementation：

先用自然中文说明：

- v0.3 如何完整吸收 v5；
- full-inbox / Clear Writing / BOARD-01 / consumer binding是否可执行；
- central vs ADAPTING vs DONE边界是否正确；
- initial Kickoff不授权机器适配是否是正确 bounded authorization；
- 五 consumer / per-consumer Maintainer scope是否保持；
- version/README/branch-worktree是否合格；
- PASS证明什么、不证明什么。

然后输出：

RESULT = PASS
REVIEW_STAGE = EXECUTION_READY_REVIEW_V0_3
PACKAGE_SNAPSHOT_COMMIT = aa0eb3e0e57714013f6de6eeb5d820efda2384cc
APPROVED_PROPOSAL_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_3_2026-09-24.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_GOAL_V0_3.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_KICKOFF_V0_3.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX

并按 Critic Role Contract逐字输出 package snapshot中已审过的 v0.3 Kickoff正文；不要 PASS 后临场改写一个不同 prompt。

## Review 文件授权

用户若把本 prompt原样发送给你，即授权你只在：

YuukiAS/AI_Skills_Collection

最新 main上新增：

docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-24.md

并 ordinary non-force push。

除此之外禁止修改：

- v5 Proposal
- v0.3 Plan / Goal / Kickoff
- AGENTS / Planner/Critic contracts / TODO / README
- ChatGPT Project instructions
- Project / Issue
- plugin source
- machine-update source
- Bridge Kit
- server/local machine/Host
- 任何其他 repo

提交后报告 exact review commit。
