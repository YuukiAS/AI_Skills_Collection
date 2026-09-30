# AI Skills Maintenance Board — Issue Maturity Implementation Plan v0.1

- Date: 2026-10-01
- Human label: Maintenance Board Issues 成熟化
- Task key: `repo--maintenance-board-issue-maturity`
- Repository: `YuukiAS/AI_Skills_Collection`
- Package version: `v0.1`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md`
- Approved design commit: `3d091421c7afe8d4f90687ef6e0ce2686bcaf426`
- Design Critic result: `PASS` as explicitly supplied by the user for this package-preparation round
- v6.1 prerequisite semantics remain independent:
  - Proposal: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md`
  - Critic PASS: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md`
  - Proposal commit: `515c42623c55f368eb84a1628839459afa909c09`
  - Review commit: `7566eb5726e92c4aff813e11b0d7addbf9852e6b`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Execution branch: `reviewed/repo--maintenance-board-issue-maturity`
- Exact worktree: `../AI_Skills_Collection-repo--maintenance-board-issue-maturity`
- This Plan does not authorize execution.

## 1. Product target

Mature the existing AI Skills Maintenance Board at the GitHub Issues layer without creating a second lifecycle or a custom triage platform.

The current board contract remains authoritative:

```text
canonical TODO
  -> problem / evidence / maturity / tracking:#N

GitHub Project Status
  -> TODO / DOING / ADAPTING / DONE

GitHub Project Area
  -> primary execution owner

GitHub Issue labels
  -> searchable issue taxonomy only
```

v7 adds:

1. orthogonal Issue labels for kind, scope, area and pre-admission triage;
2. two human-facing Issue Forms plus the blank-Issue route;
3. one tiny pre-admission Issue Action;
4. native sub-issue/dependency policy only;
5. one-time taxonomy migration across current open and closed `maintenance-track` Issues;
6. one deterministic read-only metadata audit;
7. explicit stale safety.

v7 does not create a new lifecycle, new Project field, custom bot, hierarchy store, machine registry, watcher, daemon or database.

## 2. Exact execution identity

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-issue-maturity
branch = reviewed/repo--maintenance-board-issue-maturity
worktree = ../AI_Skills_Collection-repo--maintenance-board-issue-maturity
base = kickoff-time latest origin/main
```

The future approved Kickoff authorizes creation of only this exact branch/worktree.

If the exact sibling worktree cannot be created legally, fail closed. Do not use `/tmp`, a dirty canonical checkout, another branch or another path.

## 3. v6.1 remains independent

This task does **not** implement or reopen v6.1 required-consumer semantics.

v7 may update `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` only by adding Issue-taxonomy/intake/hierarchy/audit rules. It must not alter §§14–16 required-consumer semantics as part of v7.

At integration time:

- if v6.1 has already landed, preserve its latest canonical wording;
- if v6.1 has not landed, do not implement it opportunistically;
- if latest-main drift creates a semantic conflict in the same canonical file, return Planner/Critic rather than choosing one version silently.

Issue #4 is not the v7 tracking Issue and v7 must not move its lifecycle/status or completion target.

## 4. Exact label taxonomy

Existing label, unchanged:

| Label | Color | Description |
|---|---|---|
| `maintenance-track` | `5319e7` | Tracked by AI Skills Maintenance board |

v7 creates or reconciles the following labels exactly.

### 4.1 Pre-admission triage

| Label | Color | Description |
|---|---:|---|
| `triage:needed` | `fbca04` | 进入正式维护前，等待 AI_Skills central triage |
| `triage:needs-info` | `fef2c0` | 进入正式维护前仍缺少关键事实或证据 |

These labels are pre-admission only. A `maintenance-track` Issue must not keep either triage label after admission.

### 4.2 Kind — exactly one per maintenance-track Issue

| Label | Color | Description |
|---|---:|---|
| `kind:regression` | `d73a4a` | 已建立能力或规则在真实使用中失效或回归 |
| `kind:enhancement` | `a2eeef` | 改进现有能力的质量、易用性、完整性或可维护性 |
| `kind:new-capability` | `0e8a16` | 新增当前系统尚未实质提供的用户能力 |
| `kind:governance` | `7057ff` | 维护流程、生命周期、发布、交接或治理机制 |

No priority, oncall or lifecycle kind is added.

### 4.3 Scope — exactly one per maintenance-track Issue

| Label | Color | Description |
|---|---:|---|
| `scope:plugin` | `c5def5` | 主要属于一个中央 plugin 的维护工作 |
| `scope:standalone-skill` | `bfdadc` | 主要属于独立安装的 standalone skill |
| `scope:repo-workflow` | `f9d0c4` | AI_Skills_Collection 仓库级 workflow 或治理 |
| `scope:cross-repo` | `d4c5f9` | AI_Skills owner 的工作跨越一个以上 canonical repo |

`scope:cross-repo` does not transfer ownership of another repo's bug into AI_Skills.

### 4.4 Area — exactly one per maintenance-track Issue

All area labels use color `ededed`. Project `Area` is authoritative; the Issue label is a searchable mirror.

| Label | Description |
|---|---|
| `area:workflow-core` | Search mirror of Project Area: workflow-core |
| `area:ai-skills-core` | Search mirror of Project Area: ai-skills-core |
| `area:writing-style` | Search mirror of Project Area: writing-style |
| `area:research-writing` | Search mirror of Project Area: research-writing |
| `area:presentations` | Search mirror of Project Area: presentations |
| `area:scientific-visualization` | Search mirror of Project Area: scientific-visualization |
| `area:web-development` | Search mirror of Project Area: web-development |
| `area:statistical-modeling` | Search mirror of Project Area: statistical-modeling |
| `area:bioinformatics` | Search mirror of Project Area: bioinformatics |
| `area:medical-imaging` | Search mirror of Project Area: medical-imaging |
| `area:standalone-skill` | Search mirror of Project Area: standalone-skill |
| `area:repo` | Search mirror of Project Area: repo |
| `area:cross-plugin` | Search mirror of Project Area: cross-plugin |

### 4.5 Optional integration metadata

| Label | Color | Description |
|---|---:|---|
| `integration:bridge-kit` | `0366d6` | AI_Skills-owned work has a real Bridge Kit integration/dependency dimension |

Do not create `area:bridge-kit`.

If the real defect belongs to Bridge Kit runtime/product behavior, its canonical Issue belongs in the Bridge repository. AI_Skills may retain only its own integration/adaptation Issue and use native dependency/locator metadata.

## 5. Exact source-of-truth contract

The future implementation must append a bounded Issue-maturity section to the canonical board policy while preserving all unrelated policy.

| Concern | Source of truth |
|---|---|
| problem / evidence / maturity | canonical plugin/skill TODO entry |
| source -> Issue mapping | source `tracking: #N` |
| lifecycle | Project `Status` |
| primary execution owner | Project `Area` |
| kind | exactly one `kind:*` Issue label |
| scope | exactly one `scope:*` Issue label |
| area search projection | exactly one `area:*` label mirroring Project Area |
| Bridge integration | optional `integration:bridge-kit` |
| parent/child | native GitHub sub-issue relation |
| blocked-by/blocking | native GitHub dependency relation |

Forbidden:

- `status:todo`, `status:doing`, `status:adapting`, `status:done` labels;
- copying canonical TODO maturity into Issue labels;
- treating area labels as a second owner source;
- custom hierarchy database.

If Project Area and `area:*` drift, Project Area wins and the Issue label must be reconciled.

## 6. Exact repository files

v7 may add or modify only these implementation surfaces plus task evidence:

### Canonical policy

- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
  - append Issue taxonomy / intake / hierarchy / bounded automation / stale-safety / audit rules;
  - do not implement v6.1 required-consumer changes.

### Issue Forms

- `.github/ISSUE_TEMPLATE/existing_capability_failure.yml`
- `.github/ISSUE_TEMPLATE/new_capability.yml`
- `.github/ISSUE_TEMPLATE/config.yml`

### Intake Action

- `.github/workflows/maintenance-board-intake.yml`

### Deterministic audit

- `scripts/audit_maintenance_board_issue_metadata.py`
- `tests/test_maintenance_board_issue_metadata.py`

### Task evidence

- `results/repo--maintenance-board-issue-maturity/**`

No plugin production source, generated Marketplace payload, profile, Bridge Kit source, machine-update source, CODEOWNERS, Dependabot, labeler config or stale workflow may be changed.

## 7. Exact Issue Forms

GitHub Issue Forms are defined in `.github/ISSUE_TEMPLATE/*.yml`. Default form labels must already exist before live acceptance.

### 7.1 `existing_capability_failure.yml`

Frozen top-level fields:

```yaml
name: Existing plugin / skill real failure
description: 记录现有 plugin 或 standalone skill 在真实任务里的失败
title: "[Failure] "
labels:
  - triage:needed
body:
  - markdown
  - dropdown id=owner_type
  - input id=target
  - textarea id=real_context
  - textarea id=expected
  - textarea id=actual
  - textarea id=evidence
  - textarea id=project_specific
  - checkboxes id=privacy_check
```

Required:

- `owner_type`: Central plugin / Standalone skill / Not sure
- `target`
- `real_context`
- `expected`
- `actual`
- `evidence`
- privacy checkbox confirming no private paper/data/credential content was copied.

`project_specific` may be optional but must be prompted explicitly.

Default labels:

`triage:needed`

Do not default `maintenance-track`, kind, scope or area.

### 7.2 `new_capability.yml`

Frozen top-level fields:

```yaml
name: New AI_Skills capability proposal
description: 提议当前 AI_Skills 尚未实质提供的新能力
title: "[Capability] "
labels:
  - triage:needed
  - kind:new-capability
body:
  - markdown
  - textarea id=user_problem
  - textarea id=current_gap
  - textarea id=expected_entry
  - input id=owner_if_known
  - textarea id=examples
  - textarea id=non_goal
  - checkboxes id=privacy_check
```

Required:

- `user_problem`
- `current_gap`
- `expected_entry`
- `examples`
- privacy checkbox.

Default labels:

- `triage:needed`
- `kind:new-capability`

Do not default `maintenance-track`, scope or area.

### 7.3 `config.yml`

Exact policy:

```yaml
blank_issues_enabled: true
contact_links: []
```

Forms must not use a `projects:` key. Admission remains `maintenance-track`-gated after triage.

Internal Codex/maintainer Issue creation remains allowed without an Issue Form.

## 8. Exact pre-admission Action

File:

`.github/workflows/maintenance-board-intake.yml`

Required event:

```yaml
on:
  issues:
    types: [opened]
```

Required token permissions:

```yaml
permissions:
  issues: write
```

All unspecified permissions remain none.

The workflow must:

1. inspect only `github.event.issue.labels`;
2. if `maintenance-track` is already present, do nothing;
3. otherwise ensure `triage:needed` is present;
4. never read/execute Issue body content as code;
5. never checkout repository content;
6. never use repository secrets;
7. never add `maintenance-track`;
8. never assign kind/scope/area;
9. never close/reopen Issues;
10. never mutate Project Status/Area;
11. never modify canonical TODO files.

Preferred implementation:

- one `ubuntu-latest` job;
- job-level `if` skips when `maintenance-track` is already present;
- use the runner's authenticated GitHub CLI with `GH_TOKEN: ${{ github.token }}`;
- run:
  `gh issue edit "$ISSUE_NUMBER" --repo "$GITHUB_REPOSITORY" --add-label "triage:needed"`;
- no checkout and no third-party action dependency.

This is an intake guard only, not a triage bot.

## 9. Native hierarchy policy

v7 does not create a hierarchy store.

Allowed native relations:

### Dependencies

Use GitHub `blocked by` / `blocking` only when one real tracked Issue cannot proceed until another Issue completes.

For a Bridge runtime dependency:

- Bridge runtime bug remains Bridge-owned;
- AI_Skills Issue may be blocked by the Bridge Issue;
- `integration:bridge-kit` may be added to the AI_Skills Issue if useful.

### Sub-issues

Use only when one real parent maintenance goal decomposes into independently meaningful child Issues.

Do not create a parent merely because several regressions happen to share an implementation/release round.

No hierarchy backfill is required in v7. Relations are only created when current evidence identifies a real relation.

## 10. Pre-migration snapshot

Before any v7 taxonomy label is added to an existing Issue:

1. identify the live `AI Skills Maintenance` Project and verify current Project identity;
2. enumerate all open and closed `maintenance-track` Issues;
3. read each Issue's:
   - number/title/state/state_reason;
   - existing labels;
   - Project Area;
   - Project Status;
   - Resolution commit when present;
4. map canonical source backlink(s) from current TODO files where applicable;
5. write:

`results/repo--maintenance-board-issue-maturity/PRE_MIGRATION_ISSUE_METADATA.json`

The snapshot is immutable task evidence, not a runtime registry.

No lifecycle/status/Issue close mutation occurs during snapshot.

## 11. Migration classification authority

Before any live taxonomy mutation, create:

`results/repo--maintenance-board-issue-maturity/MIGRATION_CLASSIFICATION.csv`

Required columns:

```text
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
```

### Area

Authority:

`Project Area -> area:<same-value>`

If Project Area is missing, invalid or ambiguous, record an exception and stop before Issue-label migration.

Do not infer a replacement Area label from title/keywords.

### Scope

Classify from canonical ownership and Issue contract:

- canonical plugin TODO source -> normally `scope:plugin`;
- canonical standalone-skill TODO -> normally `scope:standalone-skill`;
- repository governance/workflow -> `scope:repo-workflow`;
- AI_Skills-owned item whose real contract spans canonical repos -> `scope:cross-repo`.

A plugin-source Issue may still be `scope:cross-repo` when its real tracked problem is the AI_Skills side of a cross-repo integration.

### Kind

Kind is semantic Planner/maintainer classification using:

- canonical source problem/evidence/maturity;
- Issue title/body/current evidence;
- existing design/closure evidence when needed.

Do not classify kind by keyword regex or automated LLM Action.

If any Issue's kind is genuinely ambiguous, write:

`results/repo--maintenance-board-issue-maturity/MIGRATION_EXCEPTIONS.md`

and stop before **any** Issue taxonomy migration. Return Planner with exact Issue numbers and competing kinds.

This makes the live migration start only from a fully reviewed classification table.

### Integration

`integration:bridge-kit` is optional and requires direct evidence of an AI_Skills-owned Bridge integration/dependency.

## 12. Representative frozen classifications

The future migration must include these acceptance anchors unless live evidence has materially changed before execution:

| Issue | Expected taxonomy |
|---|---|
| #4 | `kind:governance`, `scope:repo-workflow`, `area:repo` |
| #5 | `kind:governance`, `scope:cross-repo`, `area:workflow-core`, `integration:bridge-kit` |
| #35 | `kind:regression`, `scope:plugin`, `area:presentations` |
| #63 | `kind:enhancement`, `scope:plugin`, `area:web-development` |
| #86 | `kind:new-capability`, `scope:plugin`, `area:ai-skills-core` |

If current evidence contradicts one of these anchors, stop and return Planner instead of silently changing the classification.

## 13. Two-stage implementation / mutation boundary

### Stage A — branch implementation and read-only migration planning

Allowed before independent implementation review:

- create exact task branch/worktree;
- create/reuse one v7 tracking Issue and put it in Project `DOING / Area=repo`;
- create/modify only the repo files listed in §6;
- create pre-migration snapshot;
- create migration classification table;
- create exception report if needed;
- run local unit/config validation;
- push exact task branch.

Do **not** create/reconcile v7 taxonomy labels on live Issues yet.
Do **not** add taxonomy labels to existing Issues yet.
Do **not** change Issue state, Project Status of existing items, Project Area, source maturity or `tracking: #N`.

Independent Reviewer must review the branch files **and the complete classification table**.

### Stage B — after independent implementation review PASS and main integration

If latest-main drift does not invalidate the frozen plan:

1. integrate reviewed branch to main with ordinary non-force Git;
2. verify remote main;
3. create/reconcile exact label definitions;
4. apply the reviewed classification table to all current open + closed `maintenance-track` Issues;
5. run deterministic live metadata audit;
6. perform live Issue Forms / Action / search usability acceptance;
7. write post-migration evidence;
8. close the v7 tracking Issue only after all acceptance gates pass.

If a maintenance-track Issue appears after the pre-migration snapshot but before live migration, treat it as migration drift:

- classify it before mutation using the same rules;
- if unambiguous, append it to the reviewed migration plan only through a bounded Reviewer-approved refresh;
- otherwise stop Planner.

Do not silently ignore newly admitted tracked Issues.

## 14. Exact label mutation authority

After Stage A Reviewer PASS and main integration, the Kickoff may authorize:

- `gh label create <name> --force --color <color> --description <description>`
  for the exact v7 taxonomy labels;
- preserve existing `maintenance-track` definition unchanged;
- add/remove only v7 taxonomy/triage/integration labels on Issues as required by the reviewed migration classification and intake acceptance.

Do not delete or rename unrelated pre-existing labels.

Do not alter Issue titles/bodies during taxonomy migration except the v7 tracking Issue's own reader-facing progress if needed.

## 15. Project Area ↔ area label reconciliation

Project `Area` is authoritative.

Migration:

- add exactly the matching `area:*` label;
- remove any other v7 `area:*` label from that Issue;
- never change Project Area merely to match a label.

Steady state:

- central triage/admission must set Project Area and matching area label in the same maintenance action;
- deterministic audit flags drift;
- no background reconciler is added.

## 16. Deterministic metadata audit

Add read-only:

`scripts/audit_maintenance_board_issue_metadata.py`

The script may use standard-library Python plus authenticated `gh` CLI; it must not mutate GitHub.

Frozen CLI:

```text
python scripts/audit_maintenance_board_issue_metadata.py \
  --repo YuukiAS/AI_Skills_Collection \
  --project-owner YuukiAS \
  --project-number 5 \
  --json-output results/repo--maintenance-board-issue-maturity/METADATA_AUDIT.json
```

It must check for every live `maintenance-track` Issue:

- exactly one `kind:*`;
- exactly one `scope:*`;
- exactly one `area:*`;
- no `triage:needed` or `triage:needs-info`;
- no `status:*` lifecycle label;
- `area:*` equals Project Area;
- `scope:plugin` and `scope:standalone-skill` Issues have at least one canonical `tracking: #N` backlink when their contract is TODO-backed;
- open Issue is not Project DONE;
- closed `completed` Issue has Project DONE + non-empty Resolution commit;
- non-completion closed Issue is not falsely represented as DONE.

Output:

- machine-readable JSON;
- non-zero exit code on any violation.

The script must not rewrite labels, Project fields or TODO files.

Tests:

`tests/test_maintenance_board_issue_metadata.py`

must cover at least:

- valid Issue;
- missing kind;
- multiple kind;
- area mismatch;
- forbidden triage label on admitted Issue;
- lifecycle label leakage;
- closed-completed without DONE/Resolution commit;
- plugin/standalone source backlink missing;
- cross-repo Issue not requiring local TODO backlink when not TODO-backed.

No scheduled audit workflow is added.

## 17. Live intake acceptance after main integration

### 17.1 Issue Forms

Using a supported browser/UI readback, verify:

- chooser shows both named forms;
- blank Issue route is visible;
- no form auto-targets a Project.

Do not claim live form acceptance from YAML parsing alone.

### 17.2 Intake Action

Create one bounded acceptance Issue through the blank-Issue route:

Title:

`[v7 acceptance] pre-admission triage action`

Requirements:

- create without `maintenance-track`;
- wait for `Maintenance Board Intake` workflow;
- read back `triage:needed`;
- verify no kind/scope/area/maintenance-track was added;
- verify no Project item was created;
- record workflow run + Issue evidence;
- close that acceptance Issue as `not_planned` after verification.

This acceptance Issue is not a lifecycle item and must never receive `maintenance-track`.

### 17.3 Form default-label check

The live chooser plus repository file readback must prove:

- failure form defaults only `triage:needed`;
- new-capability form defaults `triage:needed` + `kind:new-capability`.

If the execution environment can safely submit a disposable form Issue without user interaction, one form smoke is allowed, but it is not required if live chooser rendering and exact main-file readback are both available.

## 18. Search usability acceptance

After migration, run real GitHub Issue searches and compare to the migration table.

At least:

```text
is:issue label:maintenance-track label:kind:regression label:area:presentations
is:issue label:maintenance-track label:kind:governance
is:issue label:maintenance-track label:scope:cross-repo
is:issue label:maintenance-track label:area:workflow-core
```

The search result set must equal the classification table projection for each query.

This proves labels improve the normal Issues surface, not merely exist.

## 19. Stale safety

Do not add `actions/stale` or any other inactivity-closing workflow.

Acceptance must search current `.github/workflows` and confirm there is no workflow that can auto-close `maintenance-track` Issues based on inactivity.

Inactivity alone can never set DONE, completed or not-planned for tracked backlog.

## 20. Deferred features — hard boundary

v7 must not add:

- `.github/labeler.yml`;
- PR path-labeler workflow;
- Rust-style custom triage bot;
- scheduled Project metadata audit;
- CODEOWNERS;
- Dependabot;
- priority labels;
- oncall labels;
- GitHub Issue Types migration;
- stale automation;
- custom hierarchy store.

These remain future work only if real usage produces a concrete need.

## 21. Pre/post migration evidence

Required task evidence:

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

`ROLLBACK_SNAPSHOT.md` must record:

- exact pre-migration label sets for every Issue;
- v7 labels created/reconciled;
- v7 repo files;
- acceptance Issue number;
- no Issue state/Project lifecycle/source mutation occurred as part of classification migration.

## 22. Rollback contract

If v7 taxonomy/intake proves harmful, rollback may:

- remove v7-only labels from Issues and restore pre-migration label sets;
- remove the v7 label definitions if no longer used;
- revert the v7 Forms/Action/audit/policy commit;
- remove native dependency/sub-issue relations created by v7, if any.

Rollback must not:

- remove `maintenance-track`;
- change Project Status;
- change Project Area;
- change source maturity/evidence;
- change `tracking: #N`;
- reopen/close Issues solely for taxonomy rollback;
- rewrite v6.1 semantics.

The acceptance Issue remains historical evidence after being closed `not_planned`.

## 23. Representative acceptance anchors

The post-migration audit must confirm at least:

```text
#4  -> kind:governance / scope:repo-workflow / area:repo
#5  -> kind:governance / scope:cross-repo / area:workflow-core / integration:bridge-kit
#35 -> kind:regression / scope:plugin / area:presentations
#63 -> kind:enhancement / scope:plugin / area:web-development
#86 -> kind:new-capability / scope:plugin / area:ai-skills-core
```

Issue state must remain what it was immediately before migration.

## 24. Exact mutation safety

The future approved Kickoff may authorize GitHub mutations only within:

- exact v7 tracking Issue;
- exact v7 taxonomy labels;
- v7 taxonomy labels on current `maintenance-track` Issues according to reviewed classification;
- one bounded non-tracked acceptance Issue;
- native dependency/sub-issue relations only if current reviewed classification explicitly contains them.

It may not:

- change existing maintenance Issue state;
- change Project Status or Area for taxonomy reconciliation;
- change source TODO maturity/evidence/tracking;
- admit pre-admission Issues automatically;
- modify Issue #4 completion semantics;
- execute v6.1;
- touch another repository.

## 25. Version / capability-gate decision

```text
Repository bump decision: NONE
Reason: v7 changes repository maintenance metadata, GitHub Issue intake configuration,
       one repo-maintenance Action and read-only audit tooling; it is not an installable
       repository release and does not change formal plugin runtime behavior.

Affected plugins:
- all: NO_BUMP
  Reason: no production plugin source/runtime/package/profile behavior changes.
```

No Plugin Capability Gate Matrix is required for v7 because the task does not change formal plugin production behavior.

The GitHub Action still requires direct workflow safety/permission/behavior tests and live intake acceptance.

README closure is required.

Expected:

`README checked: no update required`

unless execution creates a genuinely public user entry that must be documented. Issue Forms are repository contributor tooling; the default expectation remains no root README change.

## 26. Implementation validation gates

### G1 — branch / scope

- exact branch/worktree;
- changed-file scope only as authorized;
- v6.1 semantics untouched.

### G2 — label definitions

- exact names/descriptions/colors;
- maintenance-track unchanged;
- no priority/oncall/lifecycle labels.

### G3 — classification review

- complete current open+closed maintenance-track Issue table;
- zero unresolved kind exceptions before live migration;
- representative anchors correct;
- Project Area used as Area source of truth.

### G4 — Forms / workflow static safety

- Issue Form YAML valid;
- default labels exact;
- blank enabled;
- Action event = issues opened only;
- permissions = issues write only;
- no checkout/secrets/body execution;
- no close/admission/kind/scope/area mutation.

### G5 — audit tests

- unit tests cover all frozen violations;
- audit is read-only;
- no scheduled audit workflow/token.

### G6 — independent implementation review

Reviewer inspects:

- branch diff;
- policy append;
- exact labels;
- forms/action;
- audit code/tests;
- pre-migration snapshot;
- complete classification table;
- rollback snapshot.

No live taxonomy migration before Reviewer PASS.

### G7 — integration + live migration

After Reviewer PASS:

- ordinary non-force integration to main;
- verify remote main;
- create/reconcile labels;
- apply reviewed classification to current open+closed maintenance-track Issues;
- no lifecycle/source mutation.

### G8 — live acceptance

- live template chooser;
- blank intake Action smoke;
- action workflow readback;
- post-migration audit PASS;
- real search usability queries equal classification projection;
- no stale-close path;
- representative Issues pass.

### G9 — closure

- post-migration snapshot saved;
- README closure checked;
- v7 tracking Issue reader-facing evidence updated using Clear Writing before mutation;
- Resolution commit recorded;
- close v7 tracking Issue as completed;
- verify Project DONE.

v7 is repository-governance work, not a machine-consumed capability requiring Maintenance Board downstream machine adaptation merely because AI Skills Maintainer exists on machines.

## 27. Failure recovery

- exact branch/worktree unavailable -> stop;
- design PASS provenance questioned by execution Critic -> stop before execution and request the missing review locator, do not fabricate one;
- v6.1 semantic overlap/drift -> preserve independence and return Planner/Critic;
- Project identity/Area readback unavailable -> stop migration;
- any ambiguous kind -> write exceptions and stop before live taxonomy migration;
- existing label name conflicts with unrelated semantics -> stop before `--force`;
- Issue set drifts after classification -> bounded classification refresh + Reviewer approval before mutation;
- Action lacks write permission -> do not widen token beyond `issues: write` without new review;
- live form chooser unavailable -> do not claim live acceptance; use supported browser or report blocker;
- audit failure -> keep v7 tracking Issue open/DOING and repair within reviewed scope;
- migration partial failure -> use pre-migration snapshot to restore only v7 labels; do not touch lifecycle/source state.

## 28. User-visible capability after v7

After full closure, normal GitHub Issues can answer useful questions without opening the Project:

- which presentation Issues are regressions;
- which Issues are governance;
- which work is cross-repo;
- which Issues are owned by workflow-core;
- which new human Issues still need triage.

Human contributors get two useful structured forms, while Codex/internal maintenance can still create Issues directly.

The Maintenance Project remains the only lifecycle dashboard, and canonical TODO remains the only problem/evidence/maturity source.
