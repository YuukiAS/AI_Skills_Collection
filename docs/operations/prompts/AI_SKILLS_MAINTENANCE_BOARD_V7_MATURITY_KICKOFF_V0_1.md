你现在执行 AI Skills Maintenance Board Issue Maturity v7，task key：

repo--maintenance-board-issue-maturity

Repository:
YuukiAS/AI_Skills_Collection

Exact branch:
reviewed/repo--maintenance-board-issue-maturity

Exact worktree:
../AI_Skills_Collection-repo--maintenance-board-issue-maturity

只有当独立 execution-ready Critic 对 v0.1 Plan / Goal / 本 Kickoff 给出 READY_FOR_CODEX=YES，且我随后实际发送本 Kickoff，才形成执行授权。

必须先读取 latest main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md
- docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_1_2026-10-01.md
- docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_1.md
- TODO.md
- docs/plugin-todos/README.md

v6.1 required-consumer amendment保持独立：
- 不在本任务实现 v6.1；
- 不修改 Issue #4 completion semantics；
- 不借 v7 修改 canonical board policy §§14–16 required-consumer semantics；
- integration时若latest main已落地v6.1，保留其current canonical wording；
- 若出现语义冲突，返回Planner/Critic，不自行合并语义。

我发送本 Kickoff，即授权以下 bounded effects。

==================================================
一、Git / task identity
==================================================

1. 从 kickoff-time latest origin/main 创建：
   - branch = reviewed/repo--maintenance-board-issue-maturity
   - worktree = ../AI_Skills_Collection-repo--maintenance-board-issue-maturity

2. ordinary non-force commit/push 到 exact task branch。

3. 不允许：
   - /tmp fallback
   - dirty canonical checkout
   - alternate branch/worktree
   - force push / history rewrite

==================================================
二、v7 tracking Issue
==================================================

允许 create/reuse 一个 v7 top-level tracking Issue，human-readable title表达：
“完善 AI Skills Maintenance Board 的 Issue 分类与 intake”

要求：

- label: maintenance-track
- Project: AI Skills Maintenance
- Project Area: repo
- Project Status: DOING
- reader-facing body遵守 canonical board copy contract
- GitHub mutation前真实调用 Clear Writing

该 Issue 是 v7 自己的 lifecycle item。
不得改 Issue #4 lifecycle / completion semantics。

==================================================
三、exact labels
==================================================

保留 existing：

maintenance-track
color = 5319e7
description = Tracked by AI Skills Maintenance board

创建或 reconcile 以下 exact labels：

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

如果同名 existing label 有不相容旧语义：
- 不得直接 --force 覆盖；
- 停止 label mutation并报告 conflict。

不得创建：
- lifecycle status labels
- priority labels
- oncall labels
- area:bridge-kit

==================================================
四、exact repo files
==================================================

本任务可修改/新增：

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

.github/ISSUE_TEMPLATE/existing_capability_failure.yml
.github/ISSUE_TEMPLATE/new_capability.yml
.github/ISSUE_TEMPLATE/config.yml
.github/workflows/maintenance-board-intake.yml

scripts/audit_maintenance_board_issue_metadata.py
tests/test_maintenance_board_issue_metadata.py

results/repo--maintenance-board-issue-maturity/**

以及现有 Reviewed Handoff 真正需要的 task-control/evidence files。

禁止修改：

- skills/ production source
- generated Marketplace payload
- profiles
- AI Skills Maintainer production source
- machine-update source
- Bridge Kit repo/source
- CODEOWNERS
- dependabot.yml
- .github/labeler.yml
- stale workflow
- PR path-labeler
- 其他 repo

==================================================
五、canonical board policy v7 append
==================================================

只追加/收敛以下 v7 semantics：

- Issue taxonomy source-of-truth
- intake / pre-admission contract
- Project Area -> area:* mirror
- native sub-issues / dependencies only
- bounded intake Action boundary
- deterministic metadata audit
- maintenance-track stale-close prohibition

不得：
- 重写 lifecycle
- 重写 BOARD-01
- 改 tracking:#N semantics
- 实现 v6.1 consumer amendment
- 修改 §§14–16 required-consumer semantics作为v7工作

==================================================
六、Issue Forms
==================================================

创建：

.github/ISSUE_TEMPLATE/existing_capability_failure.yml

必须：
- name = Existing plugin / skill real failure
- title prefix = [Failure]
- default labels = triage:needed only
- fields:
  owner_type dropdown
  target input
  real_context textarea
  expected textarea
  actual textarea
  evidence textarea
  project_specific textarea
  privacy_check checkbox

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

必须：
- name = New AI_Skills capability proposal
- title prefix = [Capability]
- default labels:
  triage:needed
  kind:new-capability
- fields:
  user_problem
  current_gap
  expected_entry
  owner_if_known
  examples
  non_goal
  privacy_check

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

exact policy：

blank_issues_enabled: true
contact_links: []

不得使用 forms projects: key。

==================================================
七、pre-admission Action
==================================================

创建：

.github/workflows/maintenance-board-intake.yml

event只能是：

issues:
  types: [opened]

permissions只能授予：

issues: write

所有未列权限保持 none。

行为：

- 若opened Issue已有 maintenance-track -> no-op
- 否则 ensure triage:needed
- 不checkout
- 不使用 repo secrets
- 不执行Issue body
- 不加 maintenance-track
- 不猜 kind/scope/area
- 不close/reopen
- 不改Project
- 不改TODO

优先使用 runner现有gh：

gh issue edit "$ISSUE_NUMBER" --repo "$GITHUB_REPOSITORY" --add-label "triage:needed"

GH_TOKEN只能使用 github.token。

==================================================
八、Stage A：先review，禁止live taxonomy migration
==================================================

Stage A 允许：

1. create branch/worktree
2. create/reuse v7 tracking Issue
3. 写 exact repo files
4. snapshot live current maintenance Issues / Project metadata
5. 准备完整 migration classification
6. tests/static validation
7. push branch
8. handoff independent implementation Reviewer

必须创建：

results/repo--maintenance-board-issue-maturity/PRE_MIGRATION_ISSUE_METADATA.json

results/repo--maintenance-board-issue-maturity/MIGRATION_CLASSIFICATION.csv

classification columns至少：

issue_number
issue_state
source_locator
project_area
kind
scope
area_label
integration_labels
classification_rationale
evidence_locator

在Reviewer PASS前禁止：

- create/reconcile v7 taxonomy labels
- 给existing maintenance Issues添加/删除v7 labels
- 修改existing Issue state
- 修改existing Project Status/Area
- 修改canonical TODO maturity/evidence/tracking:#N

==================================================
九、classification authority
==================================================

Area：

Project Area是唯一authoritative owner。

area label = area:<Project Area>

不得用Issue title/keyword覆盖Project Area。

Scope：

依据canonical source ownership + Issue真实contract：
- plugin -> scope:plugin
- standalone skill -> scope:standalone-skill
- repo governance/workflow -> scope:repo-workflow
- AI_Skills-owned real cross-repo contract -> scope:cross-repo

Kind：

依据：
- canonical source problem/evidence/maturity
- Issue body/current evidence
- 必要的design/closure evidence

由Planner/maintainer语义判断。

禁止：
- regex kind classification
- keyword bot
- LLM Action自动猜分类

如果任何maintenance-track Issue的kind真有歧义：

创建：

results/repo--maintenance-board-issue-maturity/MIGRATION_EXCEPTIONS.md

然后：
- 在任何live taxonomy migration前停止
- 返回Planner
- 不部分迁移

==================================================
十、representative frozen anchors
==================================================

除非execution-time current evidence出现实质冲突：

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

若冲突，返回Planner，不擅自改变这些review anchor。

==================================================
十一、native hierarchy
==================================================

只允许GitHub native：

- sub-issues
- blocked by / blocking dependencies

不新增hierarchy database/schema。

本v7不要求机械backfill hierarchy。

只有reviewed classification/evidence明确存在真实关系时才能创建。

Bridge runtime bug：
- owner仍是Bridge canonical repo
- AI_Skills integration Issue可 native dependent on Bridge Issue
- 可加 integration:bridge-kit
- 不建立 area:bridge-kit

==================================================
十二、deterministic audit
==================================================

新增只读：

scripts/audit_maintenance_board_issue_metadata.py

CLI：

python scripts/audit_maintenance_board_issue_metadata.py   --repo YuukiAS/AI_Skills_Collection   --project-owner YuukiAS   --project-number 5   --json-output results/repo--maintenance-board-issue-maturity/METADATA_AUDIT.json

可使用standard-library Python + authenticated gh。

必须只读。

检查每个maintenance-track Issue：

- exactly one kind:*
- exactly one scope:*
- exactly one area:*
- no triage:needed / triage:needs-info
- no status:* lifecycle labels
- area:* == Project Area
- TODO-backed plugin/standalone Issue有canonical tracking:#N backlink
- open Issue != Project DONE
- closed completed -> Project DONE + Resolution commit
- non-completion close不得false DONE

audit violation -> non-zero exit。

tests：

tests/test_maintenance_board_issue_metadata.py

至少覆盖：

- valid case
- missing kind
- multiple kind
- area mismatch
- admitted Issue带triage label
- lifecycle label leakage
- completed close缺DONE/Resolution commit
- plugin/standalone backlink missing
- non-TODO-backed cross-repo Issue无需本地TODO backlink

禁止scheduled audit workflow。

==================================================
十三、Stage A independent review
==================================================

Reviewer必须实际检查：

- exact changed-file scope
- canonical policy v7 append没有碰v6.1 semantics
- exact labels
- Forms
- intake Action event/permissions/safety
- audit code/tests
- PRE_MIGRATION snapshot
- complete MIGRATION_CLASSIFICATION
- rollback evidence plan

Executor summary不能替代review。

如果Reviewer REVISE：
- 修复在approved v7 scope内
- 重新review final candidate
- 不开始live migration

==================================================
十四、Stage B：Reviewer PASS 后
==================================================

若latest main无semantic conflict，本Kickoff授权同一v7 scope：

1. ordinary non-force integrate reviewed branch to main
2. verify remote main
3. create/reconcile exact v7 labels
4. apply reviewed classification to current open + closed maintenance-track Issues
5. run live deterministic audit
6. live Forms / intake Action / search usability acceptance
7. save post-migration evidence
8. README closure
9. closure v7 tracking Issue

如果snapshot后新增maintenance-track Issue：
- 不静默遗漏
- 先用同一classification contract refresh
- refresh需Reviewer认可后才能live migration
- ambiguous -> Planner

==================================================
十五、Issue migration mutation boundary
==================================================

对existing maintenance-track Issues，migration只允许：

- add/remove v7 taxonomy labels
- exact kind/scope/area reconciliation
- optional integration:bridge-kit where reviewed classification says so

禁止：

- reopen/close
- 改Issue title/body
- 改Project Status
- 改Project Area
- 改canonical TODO
- 改tracking:#N
- 改source maturity

Project Area wins；只改area label匹配Project Area。

==================================================
十六、live acceptance
==================================================

A. live template chooser：

必须实际看到：
- Existing plugin / skill real failure
- New AI_Skills capability proposal
- Blank issue

不得只靠YAML parse宣布PASS。

B. Action smoke：

创建一个 bounded non-tracked acceptance Issue：

[v7 acceptance] pre-admission triage action

创建时不带maintenance-track。

验证：
- workflow真实run
- triage:needed出现
- 没有kind/scope/area/maintenance-track自动出现
- 没有Project item
- 保存Issue + workflow run证据

验证后：
- close as not_planned
- 不添加maintenance-track

C. search usability：

真实GitHub Issue search至少核对：

label:maintenance-track label:kind:regression label:area:presentations

label:maintenance-track label:kind:governance

label:maintenance-track label:scope:cross-repo

label:maintenance-track label:area:workflow-core

结果必须与MIGRATION_CLASSIFICATION projection一致。

D. stale safety：

确认 current .github/workflows 中没有 inactivity-close maintenance-track 的workflow。

==================================================
十七、required evidence
==================================================

results/repo--maintenance-board-issue-maturity/

至少：

PRE_MIGRATION_ISSUE_METADATA.json
MIGRATION_CLASSIFICATION.csv
POST_MIGRATION_ISSUE_METADATA.json
METADATA_AUDIT.json
LIVE_INTAKE_ACCEPTANCE.md
SEARCH_ACCEPTANCE.md
ROLLBACK_SNAPSHOT.md
RESULT.md

MIGRATION_EXCEPTIONS.md仅在需要时生成。

==================================================
十八、rollback
==================================================

rollback只允许恢复v7 taxonomy/intake层：

- restore pre-migration label sets
- remove v7-only label definitions if safe
- revert v7 Forms/Action/audit/policy changes
- remove v7-created native relations if any

rollback禁止：

- remove maintenance-track
- 改Project Status/Area
- 改source maturity/evidence/tracking:#N
- reopen/closeexisting Issues solely for rollback
- 改v6.1 semantics

acceptance Issue保持历史closed not_planned即可。

==================================================
十九、deferred
==================================================

本v7禁止：

- PR path labeler
- .github/labeler.yml
- custom triage bot
- scheduled Project audit
- CODEOWNERS
- Dependabot
- priority labels
- oncall labels
- Issue Types migration
- stale automation
- custom hierarchy store

==================================================
二十、version / gate
==================================================

Repository bump decision = NONE

Reason:
maintenance metadata、Issue intake config、bounded repo Action和read-only audit；
不是正式installable repository release，不改变formal plugin runtime。

Affected plugins:
- all = NO_BUMP

No production Plugin Capability Gate Matrix。

但Action必须做：
- permission review
- event/safety tests
- live smoke

README closure mandatory。
默认：
README checked: no update required

==================================================
二十一、final closure
==================================================

只有全部成立才DONE：

- implementation Reviewer PASS
- main integration
- exact label migration完成
- live metadata audit PASS
- live Forms acceptance PASS
- Action smoke PASS
- search usability PASS
- stale safety PASS
- rollback evidence完成
- README closure完成
- Resolution commit写入v7 tracking Issue/Project
- v7 tracking Issue close completed
- Project Status DONE verified

这个v7是repo governance maturity，不因为机器安装AI Skills Maintainer而自动进入five-consumer ADAPTING。

如果任何关键能力不真实可验证，不得用config存在、test receipt或synthetic-only evidence冒充PASS。
