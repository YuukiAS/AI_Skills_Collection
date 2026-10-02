# AI Skills Maintenance Board — Issue Maturity Goal v0.2

- Human label: Maintenance Board Issues 成熟化
- Task key: `repo--maintenance-board-issue-maturity`
- Repository: `YuukiAS/AI_Skills_Collection`
- Package version: `v0.2`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md`
- Approved design commit: `3d091421c7afe8d4f90687ef6e0ce2686bcaf426`
- Previous execution Critic review:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-01.md`
- Review commit: `c78c653c097fea7b9efd33e00ccf08cd324f454d`
- Stable blocker addressed: `BOARD-V7-LABEL-CUTOVER-01`
- Implementation Plan:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_2_2026-10-01.md`
- Supersedes for execution: v0.1 Goal / Plan / Kickoff
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`

This Goal is executable only after an independent execution-ready Critic passes the exact v0.2 Plan + Goal + Kickoff and the user then sends the approved Kickoff.

## 1. Exact execution identity

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-issue-maturity
branch = reviewed/repo--maintenance-board-issue-maturity
worktree = ../AI_Skills_Collection-repo--maintenance-board-issue-maturity
base = kickoff-time latest origin/main
primary_environment = Longleaf_Codex
```

Workstation and `CUHK_Workstation_WSL_Codex` availability are not prerequisites for this repository/GitHub governance task.

## 2. Required end state

v7 must deliver:

- approved `kind:*`, `scope:*`, `area:*`, `triage:*`, `integration:bridge-kit` taxonomy;
- two Issue Forms + blank route;
- one tiny pre-admission `issues:opened` / `issues:write` Action;
- one-time open+closed `maintenance-track` taxonomy migration;
- read-only metadata audit;
- native sub-issues/dependencies only;
- no stale auto-close for tracked maintenance backlog;
- no second lifecycle or owner source.

Sources of truth remain:

```text
canonical TODO -> problem/evidence/maturity/tracking:#N
Project Status -> lifecycle
Project Area -> primary owner
Issue labels -> searchable taxonomy/projection
```

v6.1 remains independent and must not be implemented by v7.

## 3. Exact labels

Preserve unchanged:

```text
maintenance-track | 5319e7 | Tracked by AI Skills Maintenance board
```

Create/reconcile exactly:

```text
triage:needed       | fbca04 | 进入正式维护前，等待 AI_Skills central triage
triage:needs-info   | fef2c0 | 进入正式维护前仍缺少关键事实或证据

kind:regression     | d73a4a | 已建立能力或规则在真实使用中失效或回归
kind:enhancement    | a2eeef | 改进现有能力的质量、易用性、完整性或可维护性
kind:new-capability | 0e8a16 | 新增当前系统尚未实质提供的用户能力
kind:governance     | 7057ff | 维护流程、生命周期、发布、交接或治理机制

scope:plugin           | c5def5 | 主要属于一个中央 plugin 的维护工作
scope:standalone-skill | bfdadc | 主要属于独立安装的 standalone skill
scope:repo-workflow    | f9d0c4 | AI_Skills_Collection 仓库级 workflow 或治理
scope:cross-repo       | d4c5f9 | AI_Skills owner 的工作跨越一个以上 canonical repo

integration:bridge-kit | 0366d6 | AI_Skills-owned work has a real Bridge Kit integration/dependency dimension
```

Area labels:

```text
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
```

All area labels use `ededed` and description
`Search mirror of Project Area: <value>`.

No lifecycle/priority/oncall labels and no `area:bridge-kit`.

## 4. Exact repo surfaces

Authorized:

```text
docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
.github/ISSUE_TEMPLATE/existing_capability_failure.yml
.github/ISSUE_TEMPLATE/new_capability.yml
.github/ISSUE_TEMPLATE/config.yml
.github/workflows/maintenance-board-intake.yml
scripts/audit_maintenance_board_issue_metadata.py
tests/test_maintenance_board_issue_metadata.py
results/repo--maintenance-board-issue-maturity/**
```

plus ordinary task-control/evidence required by current workflow.

No production plugin source, Marketplace payload, profiles, Bridge Kit source, machine-update source, CODEOWNERS, Dependabot, labeler or stale workflow.

## 5. Issue Forms and intake Action

Failure form:

- defaults only `triage:needed`;
- asks target, real context, expected, actual, evidence, project-specific detail, privacy confirmation.

New capability form:

- defaults `triage:needed` + `kind:new-capability`;
- asks user problem, current gap, expected normal entry, examples/evidence, optional owner/non-goal, privacy confirmation.

Chooser:

```yaml
blank_issues_enabled: true
contact_links: []
```

No form auto-adds `maintenance-track` or Project.

Action:

```text
event = issues: opened
permission = issues: write
```

If `maintenance-track` already exists -> no-op.
Otherwise ensure `triage:needed`.

No checkout, secrets, body execution, admission, classification, Project mutation, close/reopen or TODO mutation.

## 6. Stage A — reviewed candidate only

Before any live v7 taxonomy label creation/application:

- create exact branch/worktree;
- create/reuse one v7 tracking Issue in Project `DOING / Area=repo`;
- implement only authorized repo files;
- create `PRE_MIGRATION_ISSUE_METADATA.json`;
- create complete `MIGRATION_CLASSIFICATION.csv`;
- prepare rollback plan;
- run static/unit checks;
- push exact task branch;
- obtain independent implementation Reviewer PASS.

Area classification comes only from Project Area.
Scope comes from canonical ownership + real Issue contract.
Kind is semantic Planner/maintainer classification, never regex/Action/LLM auto-labeling.

Any genuine kind ambiguity -> `MIGRATION_EXCEPTIONS.md` and stop before all live taxonomy migration.

Representative anchors remain:

```text
#4  governance / repo-workflow / repo
#5  governance / cross-repo / workflow-core / integration:bridge-kit
#35 regression / plugin / presentations
#63 enhancement / plugin / web-development
#86 new-capability / plugin / ai-skills-core
```

## 7. G7 — mandatory pre-publication label cutover

After independent Reviewer PASS + latest-main semantic drift check, but before Forms/Action are published on default main:

### Snapshot current label definitions

Create:

`results/repo--maintenance-board-issue-maturity/PRE_CUTOVER_LABEL_DEFINITIONS.json`

For every exact v7 label record:

- existence;
- current color;
- current description;
- compatibility = ABSENT / COMPATIBLE / INCOMPATIBLE.

Also record protected `maintenance-track` baseline definition; never mutate it.

Incompatible same-name semantics -> fail closed before any label mutation.

### Create/reconcile labels

Only after snapshot success:

- create absent v7 labels;
- reconcile compatible existing labels to approved color/description;
- verify all by live readback.

Create:

`results/repo--maintenance-board-issue-maturity/LABEL_CUTOVER_RESULT.json`

with before/intended/result/after for every exact label.

### Failure rollback

If any label mutation/readback fails:

- do not integrate Forms/Action;
- delete only labels absent before v7;
- restore original color/description for labels that existed before v7 and were changed;
- never alter `maintenance-track`;
- read back rollback;
- residual drift -> hard blocker.

Functional source must remain byte-identical to the independently reviewed candidate. A post-review cutover evidence-only commit is allowed only under `results/repo--maintenance-board-issue-maturity/**`; any functional change requires re-review.

## 8. Stage B — publish only after G7 PASS

Only after all exact v7 labels are ready:

1. ordinary non-force integrate reviewed functional branch + allowed evidence to main;
2. verify remote main;
3. verify exact v7 labels remain ready;
4. apply reviewed taxonomy to current open+closed `maintenance-track` Issues;
5. run live audit;
6. run live Forms / Action / search acceptance;
7. save post-migration evidence;
8. README closure;
9. close v7 tracking Issue only after every acceptance gate passes.

Existing Issue taxonomy migration may change only v7 labels.

It may not change:

- existing Issue state/title/body;
- Project Status/Area;
- canonical TODO;
- source maturity/evidence;
- `tracking:#N`.

## 9. Migration drift

If new `maintenance-track` Issues appear after the reviewed classification:

- do not ignore them;
- refresh classification using the same contract;
- Reviewer approval is required before live migration;
- ambiguity -> Planner.

No watcher or registry is added.

## 10. Audit and native hierarchy

Use only GitHub-native sub-issues / dependencies. No custom hierarchy store.

Add read-only:

`scripts/audit_maintenance_board_issue_metadata.py`

It must check:

- exactly one kind/scope/area on each `maintenance-track` Issue;
- no triage labels;
- no lifecycle status labels;
- area label equals Project Area;
- TODO-backed plugin/standalone Issue has canonical backlink;
- open Issue is not DONE;
- completed close has DONE + Resolution commit;
- non-completion close is not false-DONE.

Non-zero exit on violations. No scheduled audit Action.

## 11. Live acceptance

Required:

### Forms

Supported live chooser/UI readback shows:

- Existing plugin / skill real failure;
- New AI_Skills capability proposal;
- blank Issue route;
- no form Project auto-target.

### Action smoke

Create one non-tracked acceptance Issue:

`[v7 acceptance] pre-admission triage action`

Verify:

- real workflow run;
- `triage:needed` added;
- no kind/scope/area/maintenance-track auto-added;
- no Project item.

Then close it `not_planned`.

### Search

Real searches must equal classification projection for at least:

```text
label:maintenance-track label:kind:regression label:area:presentations
label:maintenance-track label:kind:governance
label:maintenance-track label:scope:cross-repo
label:maintenance-track label:area:workflow-core
```

### Stale

No inactivity-close workflow may affect `maintenance-track`.

## 12. Execution environment

Primary execution environment is `Longleaf_Codex`.

Do not wait for Workstation or `CUHK_Workstation_WSL_Codex` to perform:

- Stage A;
- classification;
- review;
- G7 label cutover;
- live Issue migration;
- Action smoke;
- audit;
- search acceptance.

v7 is not machine-consumer adaptation.

If Longleaf cannot provide a supported live Issue chooser UI readback after all other gates pass, isolate **only** that final chooser readback as a bounded acceptance handoff to any supported UI-capable surface.

Do not replay previous migration/review and do not make workstation recovery a prerequisite.

## 13. Evidence and rollback

Required evidence includes:

```text
PRE_MIGRATION_ISSUE_METADATA.json
MIGRATION_CLASSIFICATION.csv
MIGRATION_EXCEPTIONS.md                   # only if needed
PRE_CUTOVER_LABEL_DEFINITIONS.json
LABEL_CUTOVER_RESULT.json
POST_MIGRATION_ISSUE_METADATA.json
METADATA_AUDIT.json
LIVE_INTAKE_ACCEPTANCE.md
SEARCH_ACCEPTANCE.md
ROLLBACK_SNAPSHOT.md
RESULT.md
```

Rollback:

- delete only labels that did not exist before v7;
- restore exact old color/description for compatible pre-existing labels changed by v7;
- leave unchanged pre-existing definitions untouched;
- never alter `maintenance-track`;
- may revert v7 Forms/Action/audit/policy/native relations;
- must not alter Project Status/Area, Issue state solely for rollback, canonical TODO, `tracking:#N` or v6.1.

## 14. Deferred features

Not part of v7:

- PR path labeler;
- custom triagebot;
- scheduled Project audit;
- CODEOWNERS;
- Dependabot;
- priority/oncall;
- Issue Types migration;
- stale automation;
- custom hierarchy store.

## 15. Version / gate / README

```text
Repository bump decision: NONE
Affected plugins: all NO_BUMP
Production Plugin Capability Gate Matrix: NOT REQUIRED
```

Reason: repository maintenance metadata/configuration, one bounded Issue Action and read-only audit; no plugin runtime/package/profile behavior change.

Action still requires direct safety/permission/live smoke validation.

README closure required; expected:

`README checked: no update required`.

## 16. Final completion

v7 is DONE only after:

- independent implementation Reviewer PASS;
- G7 label cutover PASS;
- main integration;
- existing-Issue taxonomy migration;
- live metadata audit PASS;
- live Forms chooser PASS;
- Action smoke PASS;
- search usability PASS;
- stale safety PASS;
- rollback evidence complete;
- README closure;
- Resolution commit recorded;
- v7 tracking Issue closed completed;
- Project DONE verified.

No machine-consumer ADAPTING stage is added.
