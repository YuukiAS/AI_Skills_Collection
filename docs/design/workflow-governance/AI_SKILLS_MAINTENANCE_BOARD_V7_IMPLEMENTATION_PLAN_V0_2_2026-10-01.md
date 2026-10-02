# AI Skills Maintenance Board — Issue Maturity Implementation Plan v0.2

- Date: 2026-10-01
- Human label: Maintenance Board Issues 成熟化
- Task key: `repo--maintenance-board-issue-maturity`
- Repository: `YuukiAS/AI_Skills_Collection`
- Package version: `v0.2`
- Planner baseline: `main@54ef41ab8baa88d762f2129e28aa8d017fe471a8`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md`
- Approved design commit: `3d091421c7afe8d4f90687ef6e0ce2686bcaf426`
- Design Critic result: `PASS` as supplied by the user
- Previous execution package snapshot: `ab4967abd6d8f1c3323b9c8074fdbe606eb083c9`
- Previous execution Critic review:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-01.md`
- Previous execution Critic review commit:
  `c78c653c097fea7b9efd33e00ccf08cd324f454d`
- Stable blocker addressed: `BOARD-V7-LABEL-CUTOVER-01`
- Supersedes for execution: v0.1 Plan / Goal / Kickoff
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Execution branch: `reviewed/repo--maintenance-board-issue-maturity`
- Exact worktree: `../AI_Skills_Collection-repo--maintenance-board-issue-maturity`
- Primary execution environment: `Longleaf_Codex`
- This Plan does not authorize execution.

## 1. Planner disposition

```text
BOARD-V7-LABEL-CUTOVER-01 = ACCEPT
```

The v0.1 architecture remains unchanged. v0.2 repairs only the label publication
cutover and rollback evidence.

The repaired ordering is:

```text
Stage A source implementation + classification
-> independent implementation Reviewer PASS
-> latest-main drift check
-> snapshot current repo-level v7 label definitions
-> reconcile/create exact v7 labels
-> verify labels ready
-> only then publish Forms/Action by integrating reviewed branch to main
-> verify remote main
-> migrate reviewed Issue taxonomy
-> live audit / Forms / Action / search acceptance
-> closure
```

A label cutover failure prevents Forms/Action publication.

## 2. Product target and immutable architecture

v7 matures only the GitHub Issues layer.

Sources of truth remain:

```text
canonical TODO
  -> problem / evidence / maturity / tracking:#N

GitHub Project Status
  -> TODO / DOING / ADAPTING / DONE lifecycle

GitHub Project Area
  -> primary execution owner

GitHub Issue labels
  -> searchable kind / scope / area / triage / integration projection
```

No second lifecycle, custom bot, watcher, database, hierarchy store or machine
adaptation layer is introduced.

v6.1 remains independent. v7 must not implement or alter Issue #4
required-consumer semantics.

## 3. Exact execution identity

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-issue-maturity
branch = reviewed/repo--maintenance-board-issue-maturity
worktree = ../AI_Skills_Collection-repo--maintenance-board-issue-maturity
base = kickoff-time latest origin/main
primary_environment = Longleaf_Codex
```

The future approved Kickoff authorizes only this branch/worktree.

Workstation and `CUHK_Workstation_WSL_Codex` availability are not prerequisites
for Stage A, classification, independent review, label migration, Action smoke,
audit or GitHub search.

If the exact sibling worktree cannot be legally created on the executing
environment, fail closed. Do not use `/tmp`, another worktree or a dirty
canonical checkout.

## 4. Exact v7 label taxonomy

Existing protected admission label, never modified by v7:

| Label | Color | Description |
|---|---|---|
| `maintenance-track` | `5319e7` | Tracked by AI Skills Maintenance board |

### Pre-admission triage

| Label | Color | Description |
|---|---:|---|
| `triage:needed` | `fbca04` | 进入正式维护前，等待 AI_Skills central triage |
| `triage:needs-info` | `fef2c0` | 进入正式维护前仍缺少关键事实或证据 |

### Kind — exactly one per `maintenance-track` Issue

| Label | Color | Description |
|---|---:|---|
| `kind:regression` | `d73a4a` | 已建立能力或规则在真实使用中失效或回归 |
| `kind:enhancement` | `a2eeef` | 改进现有能力的质量、易用性、完整性或可维护性 |
| `kind:new-capability` | `0e8a16` | 新增当前系统尚未实质提供的用户能力 |
| `kind:governance` | `7057ff` | 维护流程、生命周期、发布、交接或治理机制 |

### Scope — exactly one per `maintenance-track` Issue

| Label | Color | Description |
|---|---:|---|
| `scope:plugin` | `c5def5` | 主要属于一个中央 plugin 的维护工作 |
| `scope:standalone-skill` | `bfdadc` | 主要属于独立安装的 standalone skill |
| `scope:repo-workflow` | `f9d0c4` | AI_Skills_Collection 仓库级 workflow 或治理 |
| `scope:cross-repo` | `d4c5f9` | AI_Skills owner 的工作跨越一个以上 canonical repo |

### Area — searchable mirror of Project Area

All area labels use color `ededed` and description
`Search mirror of Project Area: <exact-area-value>`.

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

### Optional integration metadata

| Label | Color | Description |
|---|---:|---|
| `integration:bridge-kit` | `0366d6` | AI_Skills-owned work has a real Bridge Kit integration/dependency dimension |

Do not create lifecycle, priority, oncall or `area:bridge-kit` labels.

## 5. Exact repository files

Authorized v7 implementation surfaces:

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

plus ordinary Reviewed Handoff task-control/evidence files required by the
current repository workflow.

Forbidden:

- production plugin source;
- generated Marketplace payload;
- profiles;
- AI Skills Maintainer / machine-update source;
- Bridge Kit source/repo;
- CODEOWNERS;
- Dependabot;
- PR labeler;
- stale workflow;
- any other repo.

The canonical board policy edit may add only v7 Issue taxonomy/intake/hierarchy/
audit/stale-safety semantics. It must not implement v6.1 or alter the
required-consumer contract as v7 work.

## 6. Exact Issue Forms

### `.github/ISSUE_TEMPLATE/existing_capability_failure.yml`

Frozen behavior:

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

Required:

- owner type;
- target;
- real context;
- expected;
- actual;
- evidence;
- privacy checkbox.

Must not default `maintenance-track`, kind, scope, area or Project.

### `.github/ISSUE_TEMPLATE/new_capability.yml`

Frozen behavior:

```text
name = New AI_Skills capability proposal
title prefix = [Capability]
default labels = triage:needed + kind:new-capability
```

Required:

- user problem;
- current gap;
- expected normal entry;
- examples/evidence;
- privacy checkbox.

Optional:

- owner if known;
- non-goal/project-specific detail.

Must not default `maintenance-track`, scope, area or Project.

### `.github/ISSUE_TEMPLATE/config.yml`

```yaml
blank_issues_enabled: true
contact_links: []
```

No form uses a `projects:` key.

## 7. Pre-admission Action

File:

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

All unspecified permissions remain none.

Behavior:

- if opened Issue already has `maintenance-track` -> no-op;
- otherwise ensure `triage:needed`;
- no checkout;
- no repository secrets;
- no Issue-body execution;
- no maintenance-track;
- no kind/scope/area classification;
- no close/reopen;
- no Project mutation;
- no TODO mutation.

Preferred mutation:

`gh issue edit "$ISSUE_NUMBER" --repo "$GITHUB_REPOSITORY" --add-label "triage:needed"`

with `GH_TOKEN=${{ github.token }}`.

## 8. Stage A — reviewed source candidate, no live v7 taxonomy labels

Stage A may:

1. create exact branch/worktree;
2. create/reuse one v7 tracking Issue in Project `DOING / Area=repo`;
3. implement only authorized repo files;
4. snapshot current Issue/Project metadata;
5. prepare the complete migration classification;
6. run static/unit validation;
7. push exact task branch;
8. hand off independent implementation Reviewer.

Required before Reviewer:

```text
PRE_MIGRATION_ISSUE_METADATA.json
MIGRATION_CLASSIFICATION.csv
ROLLBACK_SNAPSHOT.md   # plan/scope snapshot; label-definition values are added at cutover
```

No live v7 taxonomy label create/reconcile/application before Reviewer PASS.

No existing maintenance Issue state, Project Status/Area, canonical TODO maturity,
evidence or `tracking:#N` mutation.

If any kind classification is genuinely ambiguous, create
`MIGRATION_EXCEPTIONS.md` and stop before any live taxonomy migration.

## 9. Migration classification authority

### Area

Project `Area` is authoritative.

`area label = area:<Project Area>`

Never change Project Area to fit an Issue label.

### Scope

Use canonical ownership + real Issue contract:

- central plugin -> `scope:plugin`;
- standalone skill -> `scope:standalone-skill`;
- repo governance/workflow -> `scope:repo-workflow`;
- AI_Skills-owned real cross-repo contract -> `scope:cross-repo`.

### Kind

Use canonical source problem/evidence/maturity + Issue body/current evidence and,
when necessary, design/closure evidence.

Do not classify by keyword regex, title automation or an LLM Action.

### Representative anchors

Unless execution-time evidence materially contradicts them:

```text
#4  kind:governance / scope:repo-workflow / area:repo
#5  kind:governance / scope:cross-repo / area:workflow-core / integration:bridge-kit
#35 kind:regression / scope:plugin / area:presentations
#63 kind:enhancement / scope:plugin / area:web-development
#86 kind:new-capability / scope:plugin / area:ai-skills-core
```

Contradiction -> Planner, not silent reclassification.

## 10. Independent implementation review

Reviewer must inspect the final Stage A candidate:

- exact changed-file scope;
- canonical policy append and v6.1 independence;
- exact label taxonomy;
- Forms;
- intake Action permissions/event/safety;
- read-only audit code/tests;
- pre-migration snapshot;
- complete classification;
- rollback plan.

No external v7 taxonomy label cutover occurs before PASS.

Reviewer REVISE -> repair within approved v7 scope and re-review the final
candidate.

## 11. G7 — label cutover gate before Forms/Action publication

This gate is the v0.2 repair for `BOARD-V7-LABEL-CUTOVER-01`.

After independent implementation Reviewer PASS and latest-main semantic drift
check, but **before integrating the reviewed branch to default main**:

### G7.1 Pre-cutover repository-label snapshot

Read the live repository-level definition for every exact v7 label from §4.

Also read and record protected `maintenance-track`, but never mutate it.

Create durable evidence:

`results/repo--maintenance-board-issue-maturity/PRE_CUTOVER_LABEL_DEFINITIONS.json`

For each v7 label record:

```text
name
existed_before_v7 = true|false
color = <hex|null>
description = <string|null>
semantic_compatibility = COMPATIBLE | ABSENT | INCOMPATIBLE
```

For `maintenance-track` record only its protected baseline definition.

The snapshot must reflect live repo state at cutover time, after Reviewer PASS
and latest-main drift check.

A cutover-only evidence commit is allowed after Reviewer PASS **only** if its
diff is restricted to
`results/repo--maintenance-board-issue-maturity/PRE_CUTOVER_LABEL_DEFINITIONS.json`
and related cutover journal evidence. Functional source must remain byte-identical
to the reviewed candidate; otherwise re-review is required.

### G7.2 Compatibility rule

If an exact v7 label already exists:

- identical or semantically equivalent meaning -> may reconcile its approved
  color/description;
- unrelated/conflicting existing meaning -> `INCOMPATIBLE`, fail closed before
  any label mutation.

Do not use `--force` to overwrite incompatible semantics.

### G7.3 Create/reconcile labels before publishing Forms/Action

After the snapshot proves no incompatible names, create/reconcile every exact v7
label.

`maintenance-track` is verified but never reconciled by v7.

Record each mutation in:

`results/repo--maintenance-board-issue-maturity/LABEL_CUTOVER_RESULT.json`

including:

- before definition;
- intended definition;
- mutation result;
- post-mutation readback.

### G7.4 Atomic failure behavior

If any label create/reconcile or readback fails:

1. do **not** integrate the branch to main;
2. immediately rollback all v7 label-definition mutations already made:
   - if `existed_before_v7=false`, delete that newly created label;
   - if `existed_before_v7=true`, restore its exact prior color/description;
3. never alter `maintenance-track`;
4. read back rollback state;
5. record exact residual drift if rollback itself fails;
6. stop and report blocker.

Only when all exact v7 labels read back with approved definitions may Forms and
Action be published.

## 12. Stage B — publish reviewed source only after labels are ready

After G7 PASS:

1. ordinary non-force integrate the byte-reviewed functional branch to main
   together with allowed cutover evidence;
2. verify remote main contains Forms/Action/audit/policy source;
3. verify exact v7 label definitions still exist;
4. apply the reviewed classification to current open + closed
   `maintenance-track` Issues;
5. run live metadata audit;
6. run live Forms / Action / search acceptance;
7. save post-migration evidence;
8. README closure;
9. close the v7 tracking Issue only after all gates pass.

If label readiness is lost between G7 and main verification, stop before Issue
taxonomy migration.

## 13. Issue-set drift after Stage A

If a new `maintenance-track` Issue appears after the reviewed classification:

- do not ignore it;
- classify it under the same contract;
- refresh classification through bounded Reviewer approval before live taxonomy
  mutation;
- ambiguity -> Planner.

No watcher/database is added.

## 14. Existing-Issue mutation boundary

Migration may only:

- add/remove v7 taxonomy labels;
- enforce exactly one kind/scope/area;
- add `integration:bridge-kit` when reviewed classification says so.

It may not:

- reopen/close existing maintenance Issues;
- edit their title/body as taxonomy migration;
- change Project Status;
- change Project Area;
- modify canonical TODO;
- change `tracking:#N`;
- change source maturity/evidence.

Project Area wins; only the `area:*` mirror changes.

## 15. Native hierarchy

Only GitHub-native:

- sub-issues;
- `blocked by` / `blocking`.

No hierarchy database.

No mechanical hierarchy backfill.

Bridge runtime bugs remain Bridge-owned. AI_Skills may keep its own integration
Issue, optional `integration:bridge-kit`, and native dependency on the
Bridge-owned Issue.

## 16. Deterministic metadata audit

Add read-only:

`scripts/audit_maintenance_board_issue_metadata.py`

Frozen CLI:

```text
python scripts/audit_maintenance_board_issue_metadata.py \
  --repo YuukiAS/AI_Skills_Collection \
  --project-owner YuukiAS \
  --project-number 5 \
  --json-output results/repo--maintenance-board-issue-maturity/METADATA_AUDIT.json
```

The audit may use standard-library Python and authenticated `gh`, but must not
mutate GitHub.

For every `maintenance-track` Issue check:

- exactly one `kind:*`;
- exactly one `scope:*`;
- exactly one `area:*`;
- no triage labels;
- no lifecycle `status:*` label;
- area label == Project Area;
- TODO-backed plugin/standalone Issue has canonical `tracking:#N`;
- open Issue != Project DONE;
- closed completed Issue -> Project DONE + non-empty Resolution commit;
- non-completion closed Issue is not false-DONE.

Violations -> non-zero exit.

Tests cover valid, missing/multiple kind, area mismatch, triage leakage, lifecycle
label leakage, completed-close failure, source backlink failure and non-TODO-backed
cross-repo case.

No scheduled audit workflow.

## 17. Live acceptance

### Forms

Use supported live chooser/UI readback and verify:

- Existing plugin / skill real failure;
- New AI_Skills capability proposal;
- blank Issue route;
- no form auto-targets Project.

YAML parsing alone does not PASS.

### Action smoke

Create one bounded non-tracked Issue:

`[v7 acceptance] pre-admission triage action`

Verify:

- real Action run;
- `triage:needed` added;
- no kind/scope/area/maintenance-track auto-added;
- no Project item;
- evidence saved.

Then close that acceptance Issue as `not_planned`.

### Search

Real Issue search result sets must equal the reviewed classification projection
for at least:

```text
label:maintenance-track label:kind:regression label:area:presentations
label:maintenance-track label:kind:governance
label:maintenance-track label:scope:cross-repo
label:maintenance-track label:area:workflow-core
```

### Stale safety

Confirm no current workflow can close `maintenance-track` due to inactivity.

## 18. Execution-environment routing

Primary environment:

`Longleaf_Codex`

The task is repository/GitHub governance. It is **not** Maintenance Board
machine-consumer adaptation.

Therefore:

- Workstation outage does not block Stage A, classification, review, G7 label
  cutover, Issue migration, Action smoke, metadata audit or search;
- `CUHK_Workstation_WSL_Codex` outage does not block those steps;
- do not wait for either workstation environment;
- do not add a downstream ADAPTING machine-consumer phase to v7.

### Final UI-readback exception only

If `Longleaf_Codex` cannot provide a supported live GitHub Issue chooser UI
readback after every other gate passes:

1. isolate **only** live chooser readback as one final bounded acceptance
   handoff to any currently supported UI-capable surface;
2. do not replay classification, label cutover, migration, review, Action smoke,
   audit or search;
3. do not make Workstation/WSL recovery a prerequisite;
4. do not claim Forms live acceptance until that bounded readback is completed.

## 19. Required evidence

```text
results/repo--maintenance-board-issue-maturity/
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

`ROLLBACK_SNAPSHOT.md` must summarize both Issue-label memberships and the
repo-level pre-v7 label definitions from
`PRE_CUTOVER_LABEL_DEFINITIONS.json`.

## 20. Rollback contract

Rollback is provenance-aware.

For each exact v7 label:

- if it did **not** exist before v7 -> delete only that v7-created label when
  rolling back;
- if it **did** exist and v7 reconciled color/description -> restore the exact
  prior color and description from the pre-cutover snapshot;
- if it existed and no definition mutation occurred -> leave it unchanged.

Never change `maintenance-track`.

Rollback may also revert v7 Forms/Action/audit/policy files and remove native
relations created by v7.

Rollback must not:

- change Project Status/Area;
- change canonical TODO maturity/evidence/`tracking:#N`;
- reopen/close existing Issues solely for rollback;
- alter v6.1 semantics.

The acceptance Issue remains closed `not_planned` as historical evidence.

## 21. Deferred features

Still excluded:

- PR path labeler;
- custom triagebot;
- scheduled Project audit;
- CODEOWNERS;
- Dependabot;
- priority/oncall labels;
- Issue Types migration;
- stale automation;
- custom hierarchy store.

## 22. Version / gate / README

```text
Repository bump decision: NONE
Reason: maintenance metadata, contributor intake configuration, bounded repo
        Action and read-only audit; no installable repository release or formal
        plugin runtime behavior change.

Affected plugins:
- all: NO_BUMP
```

No production Plugin Capability Gate Matrix.

The Action still requires direct permission/event/safety tests and live smoke.

README closure is mandatory; expected:

`README checked: no update required`

unless execution creates a real public entry requiring documentation.

## 23. Validation gates

### G1 — scope / branch

Exact branch/worktree, authorized files only, v6.1 untouched.

### G2 — taxonomy / Forms / Action static contract

Exact labels, exact Forms, blank route, Action event/permissions and no
classification/admission/close behavior.

### G3 — classification

Complete open+closed tracked-Issue classification, zero unresolved ambiguous
kind before live mutation, representative anchors correct.

### G4 — audit tests

Read-only helper + deterministic validation tests.

### G5 — independent implementation review

Review the functional branch, complete classification and rollback plan before
live v7 labels.

### G6 — latest-main drift check

No semantic conflict with current canonical board policy / v6.1 / Issue set.

### G7 — pre-publication label cutover

- snapshot every exact v7 label existence/color/description;
- snapshot protected maintenance-track definition;
- incompatible same-name semantics -> fail closed;
- create/reconcile all exact v7 labels;
- read back exact definitions;
- any failure -> provenance-aware rollback;
- only PASS allows Forms/Action publication.

### G8 — main integration + Issue migration

Integrate reviewed branch only after G7 PASS, verify remote main, then apply
reviewed taxonomy to current tracked Issues.

### G9 — live behavior

Live audit, Forms chooser, Action smoke, search usability, stale safety.

The chooser may be the one isolated final bounded UI handoff if Longleaf lacks a
supported UI surface; all other G9 checks proceed on Longleaf when possible.

### G10 — closure

Post-migration snapshot, rollback evidence, README closure, Resolution commit,
close v7 tracking Issue completed, Project DONE verification.

## 24. Failure recovery

- exact worktree unavailable -> stop;
- v6.1 overlap/semantic drift -> Planner/Critic;
- ambiguous kind -> stop before live migration;
- label snapshot unavailable -> no label mutation and no main integration;
- incompatible same-name label -> no label mutation and no main integration;
- partial label create/reconcile failure -> provenance-aware rollback, verify
  rollback, no main integration;
- label rollback failure -> stop with exact residual label drift, no main
  integration;
- functional source changes after Reviewer PASS -> re-review;
- latest-main Issue-set drift -> bounded classification refresh + Reviewer
  approval before migration;
- metadata audit failure -> v7 tracking Issue remains open;
- Action cannot write label with `issues:write` -> stop; do not widen token
  permissions without new review;
- Workstation / WSL offline -> continue all non-UI v7 work on
  `Longleaf_Codex`;
- Longleaf cannot perform supported live chooser readback -> isolate only that
  final readback as a bounded UI acceptance handoff; do not replay prior stages.

## 25. Completion

v7 can be DONE only after:

- implementation Reviewer PASS;
- G7 label cutover PASS;
- main integration;
- taxonomy migration;
- live metadata audit PASS;
- live Forms acceptance PASS;
- Action smoke PASS;
- search usability PASS;
- stale safety PASS;
- rollback evidence complete;
- README closure;
- Resolution commit recorded;
- v7 tracking Issue closed completed;
- Project DONE verified.

No machine-consumer ADAPTING phase is added to v7.
