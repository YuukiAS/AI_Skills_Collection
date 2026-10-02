# AI Skills Maintenance Board — Issue Maturity Execution-ready Critic Prompt v0.1

你是 AI Research Stack 的独立 Critic thread。

当前只审 Maintenance Board Issue Maturity v7 的 implementation package v0.1 是否忠实、可执行、不过重、不过简，并决定是否 READY_FOR_CODEX。

不要执行，不创建 labels/forms/Actions，不修改 Issues/Project/.github/source，不启动 Codex，不实现 v6.1，不执行 machine adaptation。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = repository maintenance / plugin refinement workflow
design_topic_or_task_key = repo--maintenance-board-issue-maturity
human_label = Maintenance Board Issues 成熟化
source_branch_or_ref = main
review_stage = EXECUTION_READY_REVIEW_V7_V0_1
package_version = v0.1
package_snapshot_commit = ab4967abd6d8f1c3323b9c8074fdbe606eb083c9
execution_branch = reviewed/repo--maintenance-board-issue-maturity
execution_worktree = ../AI_Skills_Collection-repo--maintenance-board-issue-maturity
```

## Approved design

Proposal：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md`

commit：

`3d091421c7afe8d4f90687ef6e0ce2686bcaf426`

The user explicitly supplied:

`Design Critic result = PASS`

for this implementation-package preparation round.

Do not reopen v7 design unless the execution package introduces a direct regression or the Planner package materially departs from the approved Proposal.

v6.1 remains independent:

- Proposal:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_PROPOSAL_2026-09-30.md`
- Proposal commit:
  `515c42623c55f368eb84a1628839459afa909c09`
- Critic PASS:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V6_1_CRITIC_REVIEW_2026-09-30.md`
- review commit:
  `7566eb5726e92c4aff813e11b0d7addbf9852e6b`

Do not merge v7 into #4's required-consumer repair.

## Exact package to review

Plan：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_1_2026-10-01.md`

Goal：

`docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_1.md`

Kickoff Draft：

`docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_KICKOFF_V0_1.md`

All three coexist in package snapshot:

`ab4967abd6d8f1c3323b9c8074fdbe606eb083c9`

## 必须实际读取 latest main / reviewed snapshot

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- approved v7 Proposal
- v0.1 Plan / Goal / Kickoff
- `TODO.md`
- `docs/plugin-todos/README.md`
- current Project bootstrap/readback evidence
- representative Issues #4 / #5 / #35 / #63 / #86

Also inspect current `.github` issue-triage-related state to confirm the new file paths do not collide.

## 1. Exact taxonomy

v0.1 freezes:

### Triage

- `triage:needed` / `fbca04`
- `triage:needs-info` / `fef2c0`

### Kind

- `kind:regression` / `d73a4a`
- `kind:enhancement` / `a2eeef`
- `kind:new-capability` / `0e8a16`
- `kind:governance` / `7057ff`

### Scope

- `scope:plugin` / `c5def5`
- `scope:standalone-skill` / `bfdadc`
- `scope:repo-workflow` / `f9d0c4`
- `scope:cross-repo` / `d4c5f9`

### Area

Exactly the 13 existing Project Area values as `area:*`, all color `ededed`.

### Integration

- `integration:bridge-kit` / `0366d6`

Existing `maintenance-track` remains unchanged.

Check:

- exact names are searchable and orthogonal;
- descriptions are short enough for GitHub label API;
- colors are valid six-hex values;
- no lifecycle/priority/oncall labels were introduced;
- no `area:bridge-kit`.

## 2. Source-of-truth split

Package freezes:

- TODO -> problem/evidence/maturity/`tracking:#N`
- Project Status -> lifecycle
- Project Area -> primary owner
- `area:*` -> searchable mirror only
- kind/scope -> Issue-native classification

If Area drifts, Project Area wins.

Check whether any package text accidentally creates a second lifecycle or owner source.

## 3. Exact .github files

Only:

- `.github/ISSUE_TEMPLATE/existing_capability_failure.yml`
- `.github/ISSUE_TEMPLATE/new_capability.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/workflows/maintenance-board-intake.yml`

No CODEOWNERS / Dependabot / labeler / stale.

Check current repo state for path collisions.

## 4. Forms

Failure form defaults only:

`triage:needed`

New capability defaults:

`triage:needed + kind:new-capability`

Neither form:

- maintenance-track
- Project
- scope
- area

Blank issues remain enabled.

Check whether field requirements preserve enough real evidence without becoming an oversized questionnaire.

GitHub official docs state Issue Forms can define default labels and that a missing label is not auto-created; therefore package sequencing must ensure labels exist before live form acceptance.

## 5. Pre-admission Action

Exact file:

`.github/workflows/maintenance-board-intake.yml`

Event:

```text
issues: opened
```

Permissions:

```text
issues: write
```

No checkout, repo secrets or Issue-body execution.

Behavior:

- maintenance-track already present -> no-op
- otherwise ensure triage:needed
- never classify kind/scope/area
- never admit
- never close/reopen
- never mutate Project/TODO

Preferred mutation uses runner `gh issue edit --add-label`.

Independently judge whether this Action has enough value versus Forms alone, given blank/programmatic Issue creation remains supported.

If it is redundant, that is an execution/design mismatch worth REVISE. If it closes the intentional blank/API intake gap with minimal permissions, PASS it.

## 6. Migration authority

Stage A before live taxonomy mutation must freeze:

- `PRE_MIGRATION_ISSUE_METADATA.json`
- complete `MIGRATION_CLASSIFICATION.csv`

Area from Project Area.

Scope from real canonical ownership/Issue contract.

Kind from semantic Planner/maintainer classification using source/evidence, not regex or Action.

If any kind is ambiguous:

- write `MIGRATION_EXCEPTIONS.md`
- stop before **all** live taxonomy mutation
- return Planner

Check whether this is appropriately fail-closed rather than needlessly blocking migration.

## 7. Representative anchors

Unless live evidence materially changed:

```text
#4  governance / repo-workflow / repo
#5  governance / cross-repo / workflow-core / integration:bridge-kit
#35 regression / plugin / presentations
#63 enhancement / plugin / web-development
#86 new-capability / plugin / ai-skills-core
```

Check these against actual live Issues/source evidence.

## 8. Stage split

### Stage A

- branch/worktree
- v7 tracking Issue
- repo files
- pre-migration snapshot
- full classification table
- tests
- Reviewer

No live taxonomy label creation/application.

### Stage B after Reviewer PASS

- main integration
- exact label create/reconcile
- apply reviewed classification to open + closed maintenance-track Issues
- live audit
- live forms/action/search acceptance
- closure

Check whether this ordering keeps semantic classification independently reviewable before external mutations.

## 9. Drift handling

If a new maintenance-track Issue appears after Stage A classification:

- do not ignore it;
- refresh classification under same contract;
- Reviewer must approve refreshed migration plan before live mutation;
- ambiguous -> Planner.

Check whether this is enough without adding watcher/database.

## 10. Deterministic audit

New read-only:

`scripts/audit_maintenance_board_issue_metadata.py`

with tests.

Audit must prove:

- exactly one kind/scope/area;
- no admitted triage labels;
- no lifecycle labels;
- area label == Project Area;
- TODO-backed plugin/standalone Issue has `tracking:#N`;
- open != DONE;
- completed close -> DONE + Resolution commit;
- non-completion close does not false-DONE.

No scheduled Action.

Check:

- this helper is justified and not a hidden state machine;
- read-only boundary is enforceable;
- use of authenticated `gh` and Project readback is realistic;
- tests cover pure validation logic, not fake live PASS.

## 11. Native hierarchy

Sub-issues / native dependencies only.

No hierarchy backfill by default.

Bridge runtime bug remains Bridge-owned.

Check that package does not accidentally turn implementation rounds into lifecycle parent Issues.

## 12. Live acceptance

Package requires:

- live chooser shows 2 forms + blank Issue;
- one bounded blank acceptance Issue triggers Action;
- receives only triage:needed;
- does not enter Project;
- then close as not_planned;
- real search queries match classification-table projections.

Judge whether this is enough to validate normal usage without synthetic benchmark overkill.

## 13. Lifecycle safety

Migration must not:

- reopen/close existing maintenance Issues;
- change Project Status;
- change Project Area;
- modify TODO maturity/evidence/`tracking:#N`.

Only v7 labels may change on existing Issues.

Acceptance Issue is the only deliberately created/closed non-tracked smoke Issue.

## 14. Stale / deferred maturity features

Must remain absent:

- stale automation
- PR path labeler
- custom triagebot
- scheduled Project audit
- CODEOWNERS
- Dependabot
- priority/oncall
- Issue Types migration
- hierarchy database

Check whether any of these is actually necessary for v7 to deliver the claimed Issue maturity. Do not add for maturity optics.

## 15. v6.1 independence

v7 may append taxonomy semantics to the canonical board policy, but it must not modify §§14–16 required-consumer semantics as part of v7.

At integration:

- preserve whichever current v6.1 canonical wording exists on latest main;
- semantic conflict -> Planner/Critic.

Check whether this keeps #4's live semantic fix independent and avoids moving its goalposts.

## 16. Exact branch/worktree and GitHub authority

```text
branch = reviewed/repo--maintenance-board-issue-maturity
worktree = ../AI_Skills_Collection-repo--maintenance-board-issue-maturity
```

Future Kickoff authority is bounded to:

- v7 tracking Issue;
- exact v7 labels;
- v7 labels on existing tracked Issues from reviewed classification;
- one non-tracked acceptance Issue;
- native relations only if directly reviewed.

No other Issue lifecycle/Project/source mutation.

Check against current AGENTS authorization contract.

## 17. Version / Gate / README

Package says:

```text
Repository bump = NONE
all plugins = NO_BUMP
No production Plugin Capability Gate Matrix
README checked: no update required (expected)
```

Reason:

- maintenance metadata;
- repository contributor intake config;
- bounded Issue Action;
- read-only audit helper;
- no plugin runtime/package/profile behavior change.

Independently check against current version and Capability Gate policies.

## 18. Rollback

Rollback may restore only v7 labels/config/relations.

Must not touch:

- maintenance-track;
- Project Status/Area;
- TODO maturity/evidence/tracking;
- existing Issue state solely for rollback;
- v6.1 semantics.

Check pre-migration snapshot is enough for label rollback.

## 19. Validation integrity

PASS must require real evidence:

- actual live labels;
- live Issue migration;
- live Project Area comparison;
- live form chooser;
- actual Action run;
- actual acceptance Issue readback;
- actual GitHub search results;
- actual audit;
- independent review.

Config existence / unit tests alone cannot claim completion.

## 20. Output

If substantive revision is required:

```text
RESULT = REVISE
REVIEW_STAGE = EXECUTION_READY_REVIEW_V7_V0_1
PACKAGE_SNAPSHOT_COMMIT = ab4967abd6d8f1c3323b9c8074fdbe606eb083c9
READY_FOR_CODEX = NO
```

Give stable blocker IDs, direct evidence, causal risk and minimum close condition. Then generate a complete Planner repair prompt.

If package is execution-ready:

first explain in natural Chinese:

- taxonomy/source-of-truth boundary;
- forms + tiny Action;
- migration/review ordering;
- audit;
- live acceptance;
- v6.1 independence;
- version/gate;
- what PASS does and does not prove.

Then output:

```text
RESULT = PASS
REVIEW_STAGE = EXECUTION_READY_REVIEW_V7_V0_1
PACKAGE_SNAPSHOT_COMMIT = ab4967abd6d8f1c3323b9c8074fdbe606eb083c9
APPROVED_PROPOSAL_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_1_2026-10-01.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_1.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_KICKOFF_V0_1.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
```

Then reproduce the reviewed Kickoff from the package snapshot exactly; do not write a semantically different replacement.

## Review file authorization

用户发送本 prompt，即授权你只在 latest main 新增：

`docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_1_2026-10-01.md`

并 ordinary non-force push。

除此之外禁止修改：

- Proposal / Plan / Goal / Kickoff
- canonical board policy
- Issues / Project / labels
- `.github`
- scripts/tests
- plugin source
- machine state
- any other repo
