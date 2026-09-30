# AI Skills Maintenance Board — Issue Maturity Goal v0.1

- Human label: Maintenance Board Issues 成熟化
- Task key: `repo--maintenance-board-issue-maturity`
- Repository: `YuukiAS/AI_Skills_Collection`
- Package version: `v0.1`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md`
- Approved design commit: `3d091421c7afe8d4f90687ef6e0ce2686bcaf426`
- Design Critic result: `PASS` as explicitly supplied by the user for this package-preparation round
- Implementation Plan: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_1_2026-10-01.md`
- v6.1 remains an independent task and is not implemented here.
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`

This Goal becomes executable only after an independent execution-ready Critic passes the exact v0.1 Plan + Goal + Kickoff and the user then sends the approved Kickoff.

## 1. Exact execution identity

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-issue-maturity
branch = reviewed/repo--maintenance-board-issue-maturity
worktree = ../AI_Skills_Collection-repo--maintenance-board-issue-maturity
base = kickoff-time latest origin/main
```

No alternate branch/worktree, dirty-checkout fallback, force push or scope expansion is authorized.

## 2. Required end state

After completion, GitHub Issues must provide a mature searchable intake/triage layer while preserving the existing Maintenance Board sources of truth.

Required:

- canonical TODO remains problem/evidence/maturity + `tracking: #N`;
- Project `Status` remains the only lifecycle;
- Project `Area` remains the primary owner source;
- Issue labels add searchable orthogonal taxonomy only;
- `maintenance-track` remains the only formal admission label / Project auto-add key;
- human Issue intake has two Forms plus blank route;
- one tiny pre-admission Action ensures unadmitted new Issues have `triage:needed`;
- current open and closed tracked Issues are backfilled to the approved taxonomy;
- deterministic audit passes;
- no inactivity-based close path exists for `maintenance-track`;
- native sub-issues/dependencies are the only hierarchy/dependency mechanism.

## 3. Exact v7 labels

Existing, unchanged:

```text
maintenance-track | 5319e7 | Tracked by AI Skills Maintenance board
```

Create/reconcile exactly:

### Triage

```text
triage:needed     | fbca04 | 进入正式维护前，等待 AI_Skills central triage
triage:needs-info | fef2c0 | 进入正式维护前仍缺少关键事实或证据
```

### Kind

```text
kind:regression     | d73a4a | 已建立能力或规则在真实使用中失效或回归
kind:enhancement    | a2eeef | 改进现有能力的质量、易用性、完整性或可维护性
kind:new-capability | 0e8a16 | 新增当前系统尚未实质提供的用户能力
kind:governance     | 7057ff | 维护流程、生命周期、发布、交接或治理机制
```

### Scope

```text
scope:plugin           | c5def5 | 主要属于一个中央 plugin 的维护工作
scope:standalone-skill | bfdadc | 主要属于独立安装的 standalone skill
scope:repo-workflow    | f9d0c4 | AI_Skills_Collection 仓库级 workflow 或治理
scope:cross-repo       | d4c5f9 | AI_Skills owner 的工作跨越一个以上 canonical repo
```

### Area

All use color `ededed`:

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

Description for each:

`Search mirror of Project Area: <value>`

### Integration

```text
integration:bridge-kit | 0366d6 | AI_Skills-owned work has a real Bridge Kit integration/dependency dimension
```

Do not create lifecycle, priority, oncall or Bridge-area labels.

## 4. Exact source-of-truth behavior

For each `maintenance-track` Issue:

- exactly one `kind:*`;
- exactly one `scope:*`;
- exactly one `area:*`;
- no `triage:needed` / `triage:needs-info`;
- no `status:*` lifecycle label.

Project `Area` -> matching `area:*` label.

Project Area wins on drift. The migration must not change Project Area.

Canonical TODO maturity and `tracking: #N` must remain unchanged by taxonomy migration.

## 5. Exact repo implementation files

Authorized v7 repo surfaces:

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

No production plugin source, generated Marketplace payload, profile, Bridge Kit source, machine-update source, CODEOWNERS, Dependabot, labeler or stale workflow.

The board-policy edit may add v7 taxonomy/intake/hierarchy/audit semantics only. It must not implement or alter v6.1 required-consumer semantics.

## 6. Issue Forms

### Existing capability failure

Path:

`.github/ISSUE_TEMPLATE/existing_capability_failure.yml`

Top-level contract:

```text
name = Existing plugin / skill real failure
title prefix = [Failure]
default labels = triage:needed only
```

Fields:

- owner type dropdown;
- target plugin/skill;
- real task/project context;
- expected;
- actual;
- evidence;
- project-specific detail;
- privacy checkbox.

Must not default `maintenance-track`, kind, scope or area.

### New capability

Path:

`.github/ISSUE_TEMPLATE/new_capability.yml`

Top-level contract:

```text
name = New AI_Skills capability proposal
title prefix = [Capability]
default labels = triage:needed + kind:new-capability
```

Fields:

- user problem;
- current gap;
- expected normal entry;
- owner if known;
- examples/evidence;
- non-goal/project-specific detail;
- privacy checkbox.

Must not default `maintenance-track`, scope or area.

### Chooser

`.github/ISSUE_TEMPLATE/config.yml`:

```yaml
blank_issues_enabled: true
contact_links: []
```

No form may add itself to the Project.

## 7. Pre-admission Action

Path:

`.github/workflows/maintenance-board-intake.yml`

Event:

```yaml
on:
  issues:
    types: [opened]
```

Permissions:

```yaml
permissions:
  issues: write
```

Behavior:

- if opened Issue already has `maintenance-track`: no-op;
- otherwise ensure `triage:needed`;
- no checkout;
- no secrets;
- no issue-body execution;
- no close/reopen;
- no maintenance-track;
- no kind/scope/area guess;
- no Project mutation;
- no TODO mutation.

Preferred mutation uses authenticated `gh issue edit --add-label triage:needed`.

## 8. Migration sources and no-guess rule

Before live taxonomy mutation, produce:

- `PRE_MIGRATION_ISSUE_METADATA.json`;
- `MIGRATION_CLASSIFICATION.csv`.

Area source:

`Project Area`.

Scope source:

canonical source ownership + real Issue contract.

Kind source:

canonical problem/evidence + Issue body/current evidence, classified semantically by Planner/maintainer under the approved taxonomy.

Keyword-only / title-regex / Action classification is forbidden.

If any current tracked Issue has genuinely ambiguous kind:

- write `MIGRATION_EXCEPTIONS.md`;
- stop before **any** Issue taxonomy mutation;
- return Planner.

## 9. Required representative classifications

Unless current evidence has materially changed:

```text
#4  kind:governance / scope:repo-workflow / area:repo
#5  kind:governance / scope:cross-repo / area:workflow-core / integration:bridge-kit
#35 kind:regression / scope:plugin / area:presentations
#63 kind:enhancement / scope:plugin / area:web-development
#86 kind:new-capability / scope:plugin / area:ai-skills-core
```

Contradiction -> stop Planner; do not silently relabel.

## 10. Native hierarchy / dependency contract

Use only GitHub-native:

- sub-issues for a real parent maintenance goal decomposed into independent child Issues;
- `blocked by` / `blocking` for real dependencies.

Do not backfill hierarchy just for appearance.

A release/refinement batch is not automatically a parent Issue.

A Bridge runtime defect remains Bridge-owned; an AI_Skills integration Issue may depend on it and optionally carry `integration:bridge-kit`.

## 11. Deterministic audit

Add read-only script:

`scripts/audit_maintenance_board_issue_metadata.py`

Required CLI:

```text
python scripts/audit_maintenance_board_issue_metadata.py \
  --repo YuukiAS/AI_Skills_Collection \
  --project-owner YuukiAS \
  --project-number 5 \
  --json-output results/repo--maintenance-board-issue-maturity/METADATA_AUDIT.json
```

Must check:

- exactly one kind/scope/area;
- no pre-admission triage labels on admitted Issues;
- no lifecycle status labels;
- area label equals Project Area;
- TODO-backed plugin/standalone Issues have canonical `tracking: #N`;
- open Issue != Project DONE;
- closed completed Issue -> Project DONE + Resolution commit;
- non-completion closed Issue is not falsely DONE.

Must be read-only and exit non-zero on violations.

No scheduled audit Action.

## 12. Migration phases

### Stage A — reviewed branch, no live taxonomy mutation

Allowed:

- create exact branch/worktree;
- create/reuse one v7 tracking Issue, Project `DOING / Area=repo`;
- implement only authorized repo files;
- take pre-migration snapshot;
- prepare complete migration classification;
- run unit/static validation;
- push branch;
- independent implementation review.

No live taxonomy label creation/application yet.

### Stage B — only after independent implementation review PASS

If main drift does not change semantics:

1. ordinary non-force integration to main;
2. create/reconcile exact labels;
3. apply the reviewed classification to every current open + closed `maintenance-track` Issue;
4. run live metadata audit;
5. run live forms / Action / search acceptance;
6. save post-migration evidence;
7. close v7 tracking Issue only after all gates pass.

Issue-set drift after Stage A requires bounded classification refresh and Reviewer approval before live mutation.

## 13. GitHub mutation authority

Future approved Kickoff may mutate only:

- exact v7 tracking Issue;
- exact v7 taxonomy labels;
- v7 taxonomy labels on current `maintenance-track` Issues according to reviewed classification;
- one bounded non-tracked acceptance Issue;
- native sub-issue/dependency relations only when explicitly present in the reviewed classification/evidence.

Forbidden:

- existing Issue lifecycle changes due to migration;
- Project Status/Area changes for taxonomy reconciliation;
- source TODO maturity/evidence/tracking changes;
- automatic admission;
- Issue #4 consumer semantics;
- other repositories.

## 14. Live acceptance

### Forms

Use live GitHub chooser/UI readback:

- both forms visible;
- blank Issue route visible;
- no Project auto-target from forms.

YAML validation alone is not enough.

### Action

Create one acceptance Issue:

`[v7 acceptance] pre-admission triage action`

It must:

- start without `maintenance-track`;
- receive `triage:needed` from the workflow;
- receive no kind/scope/area/maintenance-track automatically;
- not enter the Project;
- record workflow run/readback;
- close `not_planned` after verification.

### Search

Real search results must match migration-table projections for at least:

```text
label:maintenance-track label:kind:regression label:area:presentations
label:maintenance-track label:kind:governance
label:maintenance-track label:scope:cross-repo
label:maintenance-track label:area:workflow-core
```

### Stale safety

No workflow may close `maintenance-track` for inactivity.

## 15. Pre/post evidence and rollback

Required evidence:

```text
results/repo--maintenance-board-issue-maturity/
  PRE_MIGRATION_ISSUE_METADATA.json
  MIGRATION_CLASSIFICATION.csv
  MIGRATION_EXCEPTIONS.md          # only if needed
  POST_MIGRATION_ISSUE_METADATA.json
  METADATA_AUDIT.json
  LIVE_INTAKE_ACCEPTANCE.md
  SEARCH_ACCEPTANCE.md
  ROLLBACK_SNAPSHOT.md
  RESULT.md
```

Rollback may restore only v7 label/config/relation changes.

Rollback must not change:

- `maintenance-track`;
- Project Status;
- Project Area;
- Issue open/closed state solely for rollback;
- canonical TODO maturity/evidence/`tracking: #N`;
- v6.1 semantics.

## 16. Deferred by contract

Not part of v7:

- PR path labeler;
- custom triagebot;
- scheduled Project audit;
- CODEOWNERS;
- Dependabot;
- priority/oncall labels;
- Issue Types migration;
- stale automation;
- custom hierarchy store.

## 17. Version / gate decision

```text
Repository bump decision: NONE
Reason: maintenance metadata, contributor intake configuration, bounded repo automation and read-only audit only.

Affected plugins:
- all: NO_BUMP
  Reason: no production plugin runtime/package/profile behavior changes.
```

No production Plugin Capability Gate Matrix.

The intake Action must still pass direct workflow permission/safety/live behavior acceptance.

README closure required; expected `README checked: no update required`.

## 18. Completion

v7 may be marked DONE only after:

- independent implementation review PASS;
- main integration;
- exact label migration complete;
- metadata audit PASS;
- live forms acceptance PASS;
- intake Action live smoke PASS;
- search usability PASS;
- stale safety PASS;
- rollback evidence complete;
- Resolution commit recorded;
- v7 tracking Issue closed completed;
- Project shows DONE.

No machine-consumer ADAPTING stage is added merely because this repository uses AI Skills Maintainer.
