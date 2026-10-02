你现在执行 AI Skills Maintenance Board Issue Maturity v7 execution package v0.2。

Repository:
YuukiAS/AI_Skills_Collection

Task key:
repo--maintenance-board-issue-maturity

Exact branch:
reviewed/repo--maintenance-board-issue-maturity

Exact worktree:
../AI_Skills_Collection-repo--maintenance-board-issue-maturity

Primary execution environment:
Longleaf_Codex

只有当独立 execution-ready Critic 对 exact v0.2 Plan / Goal / 本 Kickoff 返回 READY_FOR_CODEX=YES，且我随后实际发送本 Kickoff，才形成执行授权。

必须读取并遵守 latest main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_2_2026-10-01.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_2.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-01.md
- TODO.md
- docs/plugin-todos/README.md

v6.1 required-consumer amendment保持独立：
- 本任务不实现 v6.1；
- 不修改 Issue #4 completion semantics；
- 不借 v7 修改 canonical board policy required-consumer semantics；
- integration 时保留 latest main 上任何已经合法落地的 v6.1 wording；
- 若出现同文件 semantic conflict，返回 Planner/Critic，不自行合并。

==================================================
一、Git / execution identity
==================================================

1. 从 kickoff-time latest origin/main 创建：

branch = reviewed/repo--maintenance-board-issue-maturity
worktree = ../AI_Skills_Collection-repo--maintenance-board-issue-maturity

2. ordinary non-force commit/push 到 exact task branch。

3. 禁止：
- /tmp fallback
- dirty canonical checkout
- alternate branch/worktree
- force push
- history rewrite

4. 优先在 Longleaf_Codex 执行本任务。

Workstation 和 CUHK_Workstation_WSL_Codex 当前是否在线，不得成为以下工作的前置条件：
- Stage A
- classification
- independent review
- label cutover
- Issue taxonomy migration
- Action smoke
- metadata audit
- GitHub search acceptance

本 v7 不是 machine-consumer adaptation。

==================================================
二、v7 tracking Issue
==================================================

允许 create/reuse 一个 v7 top-level tracking Issue，标题自然表达：

完善 AI Skills Maintenance Board 的 Issue 分类与 intake

要求：

- maintenance-track
- Project = AI Skills Maintenance
- Project Area = repo
- Project Status = DOING
- reader-facing body遵守 canonical board copy contract
- reader-facing mutation 前真实调用 Clear Writing

不得修改 Issue #4 lifecycle / completion semantics。

==================================================
三、exact taxonomy labels
==================================================

maintenance-track 保持 existing definition，不得被 v7 修改：

maintenance-track
color = 5319e7
description = Tracked by AI Skills Maintenance board

v7 exact labels：

triage:needed
color = fbca04
description = 进入正式维护前，等待 AI_Skills central triage

triage:needs-info
color = fef2c0
description = 进入正式维护前仍缺少关键事实或证据

kind:regression
color = d73a4a
description = 已建立能力或规则在真实使用中失效或回归

kind:enhancement
color = a2eeef
description = 改进现有能力的质量、易用性、完整性或可维护性

kind:new-capability
color = 0e8a16
description = 新增当前系统尚未实质提供的用户能力

kind:governance
color = 7057ff
description = 维护流程、生命周期、发布、交接或治理机制

scope:plugin
color = c5def5
description = 主要属于一个中央 plugin 的维护工作

scope:standalone-skill
color = bfdadc
description = 主要属于独立安装的 standalone skill

scope:repo-workflow
color = f9d0c4
description = AI_Skills_Collection 仓库级 workflow 或治理

scope:cross-repo
color = d4c5f9
description = AI_Skills owner 的工作跨越一个以上 canonical repo

area:workflow-core
area:ai-skills-core
area:writing-style
area:research-writing
area:presentations
area:scientific-visualization
area:web-development
area:statistical-modeling
area:bioinformatics
area:medical-imaging
area:standalone-skill
area:repo
area:cross-plugin

所有 area:*：
color = ededed
description = Search mirror of Project Area: <exact area value>

integration:bridge-kit
color = 0366d6
description = AI_Skills-owned work has a real Bridge Kit integration/dependency dimension

禁止新增：
- lifecycle status labels
- priority labels
- oncall labels
- area:bridge-kit

==================================================
四、exact repo files
==================================================

本任务允许修改/新增：

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

.github/ISSUE_TEMPLATE/existing_capability_failure.yml
.github/ISSUE_TEMPLATE/new_capability.yml
.github/ISSUE_TEMPLATE/config.yml
.github/workflows/maintenance-board-intake.yml

scripts/audit_maintenance_board_issue_metadata.py
tests/test_maintenance_board_issue_metadata.py

results/repo--maintenance-board-issue-maturity/**

以及当前 repo Reviewed Handoff 真正需要的 task-control/evidence files。

禁止修改：

- production plugin source
- generated Marketplace payload
- profiles
- AI Skills Maintainer / machine-update production source
- Bridge Kit source/repo
- CODEOWNERS
- Dependabot
- .github/labeler.yml
- PR path labeler
- stale workflow
- 其他 repo

==================================================
五、canonical board policy v7 scope
==================================================

只增加/收敛：

- Issue taxonomy source-of-truth
- pre-admission intake contract
- Project Area -> area:* mirror
- native sub-issues/dependencies only
- bounded intake Action
- deterministic metadata audit
- maintenance-track stale-close prohibition

不得：

- 重写 Project lifecycle
- 重写 BOARD-01
- 改 tracking:#N semantics
- 实现 v6.1
- 改 Issue #4 completion contract
- 借 v7 修改 required-consumer contract

==================================================
六、Issue Forms
==================================================

创建：

.github/ISSUE_TEMPLATE/existing_capability_failure.yml

要求：

name = Existing plugin / skill real failure
title prefix = [Failure]
default labels = triage:needed only

fields：
- owner_type dropdown
- target input
- real_context textarea
- expected textarea
- actual textarea
- evidence textarea
- project_specific textarea
- privacy_check checkboxes

required：
- owner_type
- target
- real_context
- expected
- actual
- evidence
- privacy_check

不得自动：
- maintenance-track
- kind
- scope
- area
- Project

创建：

.github/ISSUE_TEMPLATE/new_capability.yml

要求：

name = New AI_Skills capability proposal
title prefix = [Capability]
default labels：
- triage:needed
- kind:new-capability

fields：
- user_problem
- current_gap
- expected_entry
- owner_if_known
- examples
- non_goal
- privacy_check

required：
- user_problem
- current_gap
- expected_entry
- examples
- privacy_check

不得自动：
- maintenance-track
- scope
- area
- Project

创建：

.github/ISSUE_TEMPLATE/config.yml

exact：

blank_issues_enabled: true
contact_links: []

不得使用 projects: key。

==================================================
七、pre-admission Action
==================================================

创建：

.github/workflows/maintenance-board-intake.yml

event只能是：

issues:
  types: [opened]

permissions只能授权：

issues: write

其余权限 none。

行为：

- 如果 opened Issue 已有 maintenance-track -> no-op
- 否则 ensure triage:needed
- 不 checkout
- 不使用 repository secrets
- 不执行 Issue body
- 不加 maintenance-track
- 不猜 kind/scope/area
- 不 close/reopen
- 不改 Project
- 不改 TODO

优先使用当前 runner 自带 gh：

gh issue edit "$ISSUE_NUMBER" --repo "$GITHUB_REPOSITORY" --add-label "triage:needed"

GH_TOKEN = github.token

==================================================
八、Stage A：Reviewer PASS 前禁止 live v7 label mutation
==================================================

Stage A 允许：

1. exact branch/worktree
2. create/reuse v7 tracking Issue
3. 写 approved repo files
4. snapshot current tracked Issues / Project metadata
5. complete migration classification
6. tests/static checks
7. push reviewed branch
8. independent implementation review

必须准备：

results/repo--maintenance-board-issue-maturity/PRE_MIGRATION_ISSUE_METADATA.json

results/repo--maintenance-board-issue-maturity/MIGRATION_CLASSIFICATION.csv

results/repo--maintenance-board-issue-maturity/ROLLBACK_SNAPSHOT.md

Reviewer PASS 前禁止：

- create/reconcile v7 taxonomy labels
- 给现有 maintenance-track Issues 添加/删除 v7 labels
- 修改 existing Issue state
- 修改 Project Status/Area
- 修改 canonical TODO maturity/evidence/tracking:#N

==================================================
九、classification authority
==================================================

Area：
Project Area 是 authoritative source。

area label = area:<Project Area>

不得反向修改 Project Area。

Scope：
按 canonical ownership + real Issue contract：

- central plugin -> scope:plugin
- standalone skill -> scope:standalone-skill
- repo governance/workflow -> scope:repo-workflow
- AI_Skills-owned real cross-repo contract -> scope:cross-repo

Kind：
由 Planner/maintainer 基于：
- canonical problem/evidence/maturity
- Issue body/current evidence
- 必要 design/closure evidence
做语义判断。

禁止：
- keyword / title regex auto classification
- LLM Action 自动分类

如果任何 kind 真正 ambiguous：

创建 MIGRATION_EXCEPTIONS.md

然后在任何 live taxonomy migration 前停止并返回 Planner。

不得 partial migrate。

代表性 anchors：

#4
kind:governance
scope:repo-workflow
area:repo

#5
kind:governance
scope:cross-repo
area:workflow-core
integration:bridge-kit

#35
kind:regression
scope:plugin
area:presentations

#63
kind:enhancement
scope:plugin
area:web-development

#86
kind:new-capability
scope:plugin
area:ai-skills-core

execution-time evidence 若实质冲突 -> 返回 Planner。

==================================================
十、Stage A independent Reviewer
==================================================

Reviewer必须检查：

- exact file scope
- v6.1 independence
- canonical policy append
- exact taxonomy
- Forms
- intake Action event/permissions/safety
- audit code/tests
- PRE_MIGRATION snapshot
- complete MIGRATION_CLASSIFICATION
- rollback plan

Reviewer PASS 前不得进入 live label cutover。

若 REVISE：
- 在 approved v7 scope修复
- re-review final functional candidate
- 不 live migrate

==================================================
十一、G7：labels 必须先于 Forms/Action 发布
==================================================

只有 independent Reviewer PASS + latest-main semantic drift check 后，才进入 G7。

此时仍然 **不得先 integrate reviewed branch 到 default main**。

### 11.1 snapshot every exact v7 label definition

先读取 live repository-level label definitions。

对每个 exact v7 label记录：

- name
- existed_before_v7
- current color
- current description
- semantic compatibility：
  ABSENT / COMPATIBLE / INCOMPATIBLE

写入：

results/repo--maintenance-board-issue-maturity/PRE_CUTOVER_LABEL_DEFINITIONS.json

同时 snapshot maintenance-track baseline definition，但 maintenance-track 永不由 v7 mutate。

如果同名 label 已存在但语义 incompatible：
- fail closed
- 不 mutation
- 不 integrate Forms/Action

### 11.2 create/reconcile labels

仅在完整 snapshot + compatibility PASS 后：

- absent label -> create exact approved definition
- compatible existing label -> reconcile approved color/description
- incompatible -> 禁止 --force 覆盖

所有 mutation 写入：

results/repo--maintenance-board-issue-maturity/LABEL_CUTOVER_RESULT.json

每项至少：

- before
- intended
- result
- after readback

### 11.3 any failure = no publication

任何 label create/reconcile/readback 失败：

1. 不得 integrate Forms/Action
2. 立即 rollback 已发生的 v7 label definition mutation：
   - v7 前 absent -> delete newly created label
   - v7 前 existed -> restore exact old color/description
3. maintenance-track 不得改变
4. read back rollback
5. rollback residual drift -> hard blocker
6. stop

只有所有 exact v7 labels read back正确，G7才PASS。

### 11.4 post-review evidence-only commit

Reviewer PASS 后允许新增 cutover evidence commit，但 diff 只能位于：

results/repo--maintenance-board-issue-maturity/**

functional source必须与Reviewer PASS candidate byte-identical。

任何 functional diff -> 重新 Reviewer。

==================================================
十二、Stage B：G7 PASS后才发布
==================================================

G7 PASS后才允许：

1. ordinary non-force integrate reviewed functional branch + allowed cutover evidence 到 main
2. verify remote main
3. 再次 read back exact labels仍ready
4. apply reviewed classification to current open+closed maintenance-track Issues
5. run metadata audit
6. live Forms/Action/search acceptance
7. save post-migration evidence
8. README closure
9. final v7 Issue closure

如果G7后、migration前label readiness丢失：
- stop
- 不继续Issue taxonomy migration

==================================================
十三、Issue-set drift
==================================================

如果Stage A snapshot/classification后新增maintenance-track Issue：

- 不静默遗漏
- 使用同一 contract补classification
- refresh必须获得bounded Reviewer approval后才live mutation
- ambiguous -> Planner

不新增 watcher/database。

==================================================
十四、existing Issue mutation boundary
==================================================

taxonomy migration 对 existing maintenance-track Issues 只允许：

- add/remove v7 taxonomy labels
- exactly-one kind/scope/area reconciliation
- integration:bridge-kit where reviewed classification says so

禁止：

- reopen/close
- 改title/body
- 改Project Status
- 改Project Area
- 改canonical TODO
- 改tracking:#N
- 改source maturity/evidence

Project Area wins。

==================================================
十五、native hierarchy
==================================================

只使用 GitHub native：

- sub-issues
- blocked by / blocking dependencies

不创建 hierarchy database。

不要求机械 backfill hierarchy。

Bridge runtime bug仍属于Bridge canonical repo；
AI_Skills自己的integration Issue可 native dependent on Bridge Issue，并可带 integration:bridge-kit。

==================================================
十六、deterministic read-only audit
==================================================

新增：

scripts/audit_maintenance_board_issue_metadata.py

CLI：

python scripts/audit_maintenance_board_issue_metadata.py   --repo YuukiAS/AI_Skills_Collection   --project-owner YuukiAS   --project-number 5   --json-output results/repo--maintenance-board-issue-maturity/METADATA_AUDIT.json

只读。

检查：

- exactly one kind:*
- exactly one scope:*
- exactly one area:*
- no triage labels on maintenance-track
- no lifecycle status:* labels
- area label == Project Area
- TODO-backed plugin/standalone Issue有canonical tracking:#N
- open Issue != Project DONE
- closed completed -> Project DONE + Resolution commit
- non-completion close不false DONE

violation -> non-zero exit。

tests/test_maintenance_board_issue_metadata.py
覆盖 approved cases。

禁止 scheduled audit workflow。

==================================================
十七、live acceptance
==================================================

A. Forms chooser：

必须 live readback：

- Existing plugin / skill real failure
- New AI_Skills capability proposal
- blank Issue route
- no Project auto-target

不能只靠 YAML parse。

B. Action smoke：

创建 bounded non-tracked acceptance Issue：

[v7 acceptance] pre-admission triage action

验证：

- Action真实run
- triage:needed添加
- 无kind/scope/area/maintenance-track自动添加
- 无Project item

保存证据后 close as not_planned。

C. Search usability：

真实 search：

label:maintenance-track label:kind:regression label:area:presentations

label:maintenance-track label:kind:governance

label:maintenance-track label:scope:cross-repo

label:maintenance-track label:area:workflow-core

结果必须等于 reviewed classification projection。

D. stale safety：

确认没有 inactivity-close maintenance-track 的workflow。

==================================================
十八、execution environment routing
==================================================

优先 Longleaf_Codex。

不得因为：

- Workstation掉线
- CUHK_Workstation_WSL_Codex掉线

阻塞：

- Stage A
- classification
- Reviewer
- G7 label cutover
- GitHub Issue migration
- Action smoke
- audit
- search

v7不是machine-consumer adaptation。

如果 Longleaf_Codex 最终无法提供 supported live Issue chooser UI readback：

- 只把 chooser readback 隔离成最后一个 bounded acceptance handoff
- 可交给任意当前可用且 supported UI-capable surface
- 不重跑 classification
- 不重跑 Reviewer
- 不重跑 label cutover
- 不重跑 migration
- 不重跑 Action smoke/audit/search
- 不把 Workstation recovery 当整个 v7 prerequisite
- chooser readback没完成前不得声称 live Forms acceptance PASS

==================================================
十九、evidence
==================================================

至少保存：

PRE_MIGRATION_ISSUE_METADATA.json
MIGRATION_CLASSIFICATION.csv
MIGRATION_EXCEPTIONS.md         # if needed
PRE_CUTOVER_LABEL_DEFINITIONS.json
LABEL_CUTOVER_RESULT.json
POST_MIGRATION_ISSUE_METADATA.json
METADATA_AUDIT.json
LIVE_INTAKE_ACCEPTANCE.md
SEARCH_ACCEPTANCE.md
ROLLBACK_SNAPSHOT.md
RESULT.md

ROLLBACK_SNAPSHOT必须同时包含：

- pre-migration Issue label memberships
- pre-v7 repository-level label definitions

==================================================
二十、rollback
==================================================

v7前不存在的label：
- rollback时才允许delete

v7前存在且被reconcile的label：
- restore exact prior color/description

v7前存在但未改definition：
- leave unchanged

maintenance-track：
- never mutate
- never delete
- never redefine

rollback还可revert：
- Forms
- intake Action
- audit helper
- v7 policy append
- v7-created native relations

rollback禁止：

- 改Project Status/Area
- 改canonical TODO
- 改tracking:#N
- 改source maturity/evidence
- 为rollback reopen/close existing maintenance Issues
- 改v6.1

==================================================
二十一、deferred
==================================================

禁止：

- PR path labeler
- custom triagebot
- scheduled Project audit
- CODEOWNERS
- Dependabot
- priority/oncall
- Issue Types migration
- stale automation
- hierarchy database

==================================================
二十二、version / gate / README
==================================================

Repository bump decision = NONE

Affected plugins:
- all = NO_BUMP

No production Plugin Capability Gate Matrix。

Action仍必须：
- permission review
- event/safety tests
- live smoke

README closure mandatory。
默认：
README checked: no update required

==================================================
二十三、final closure
==================================================

只有全部成立才可以DONE：

- independent implementation Reviewer PASS
- G7 label cutover PASS
- main integration
- taxonomy migration
- metadata audit PASS
- live Forms acceptance PASS
- Action smoke PASS
- search usability PASS
- stale safety PASS
- rollback evidence complete
- README closure
- Resolution commit写入v7 tracking Issue/Project
- v7 tracking Issue close completed
- Project DONE verified

v7不进入machine-consumer ADAPTING。

如果任一真实能力无法验证，不得用config存在、unit test、receipt或synthetic evidence冒充PASS。
