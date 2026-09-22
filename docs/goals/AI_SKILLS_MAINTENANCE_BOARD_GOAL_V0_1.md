# AI Skills 维护看板 — Canonical Goal v0.1

- Human label: AI Skills 维护看板与完成语义
- Task key: `repo--maintenance-board-lifecycle`
- Repository: `YuukiAS/AI_Skills_Collection`
- Package version: `v0.1`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`
- Approved design commit: `da46f14141888c1bcd94bf94a486bcb1a1b0ec7c`
- Design Critic PASS: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`
- Critic review commit: `8213c843b4d91c63f6de62740e26ef8d215a59e0`
- Implementation Plan: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_1_2026-09-22.md` v0.1
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`

This Goal is not executable until an independent Critic reviews this exact v0.1 Plan + Goal + Kickoff and returns `READY_FOR_CODEX=YES`. Only when the user later sends the verbatim approved Kickoff does the current user message authorize the bounded effects below.

## 1. Exact execution identity

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = latest origin/main at kickoff preflight
```

The worktree path is exact relative to the canonical repository root. Resolve it once to its absolute sibling path and record that path before creating it. No alternate worktree, branch, `/tmp` fallback, dirty-checkout substitution, or task-key substitution is authorized.

## 2. Required product result

The overall Goal is achieved only when the user has one working GitHub Project for AI_Skills maintenance with these lifecycle semantics:

```text
TODO -> DOING -> ADAPTING -> DONE
```

The Project must make a top-level maintenance idea visibly distinguishable from a single implementation task:

- Project item = top-level tracking Issue.
- plugin TODO = failure/evidence/maturity inbox.
- Planner–Critic / Reviewed Handoff / Executor task = implementation/review evidence.
- WAITING/BLOCKED = label / next-action condition, not a main Status.
- `Resolution commit` = owner-repo canonical closure/evidence commit.
- optional consumers discovered after DONE create follow-up work rather than retroactively expanding the old completion contract, unless new evidence proves the old claim was false.

## 3. Required GitHub Project identity

Create or reconcile exactly one maintainer Project:

```text
owner = YuukiAS
title = AI Skills Maintenance
visibility = PRIVATE
linked repo = YuukiAS/AI_Skills_Collection
tracking label = maintenance-track
```

Do not create a second Project if an exact-title compatible Project already exists. Ambiguous or unrelated exact-title Projects are a stop condition.

The Project must have:

### Status

```text
TODO
DOING
ADAPTING
DONE
```

No fifth lifecycle state.

### Area

At least these primary-owner options:

```text
workflow-core
ai-skills-core
writing-style
research-writing
presentations
scientific-visualization
web-development
statistical-modeling
bioinformatics
medical-imaging
standalone-skill
repo
cross-plugin
```

### Resolution commit

A text field, empty until final closure.

### Views

No more than:

- Board
- Active
- By area
- History

The Plan defines their layout/filter semantics.

## 4. BOARD-01 is a frozen acceptance boundary

The previously closed blocker must remain closed in actual configuration.

Required:

1. lifecycle item only = `maintenance-track` tracking Issue;
2. auto-add filter at least `is:issue label:maintenance-track`;
3. implementation/design PRs are not lifecycle items;
4. Project `pull request merged -> Done` workflow is disabled;
5. before true DONE, tracking Issues are not linked to intermediate PRs through any relationship that auto-closes on merge;
6. PR bodies and commit messages do not target the tracking Issue with GitHub closing keywords;
7. intermediate task/PR/commit relationships use only non-closing references;
8. repository-wide linked-PR auto-close remains unchanged;
9. `issue closed -> Done` is retained only as the last mechanical mapping after the full DONE checklist passes.

A task/PR merge, a Critic PASS, a test PASS, or central integration alone cannot produce top-level DONE.

## 5. Allowed external GitHub effects after approved Kickoff

Within the exact GitHub account/repository/project scope above, the Executor may:

- inspect current Projects, fields, views and Project workflows;
- verify/request the `project` OAuth scope when genuinely absent;
- create or reconcile the one private `AI Skills Maintenance` Project;
- link it to `YuukiAS/AI_Skills_Collection`;
- create/reconcile Status, Area and Resolution commit fields;
- create/reconcile the four approved views;
- configure the approved built-in Project workflows and auto-add rule through current supported GitHub surfaces;
- create/reuse the `maintenance-track` repository label;
- create/reuse/update tracking Issues that pass the bounded backfill rules;
- add/update those Issues in the Project and set approved field values;
- create the tracking Issue for this maintenance-board idea;
- update tracking Issue comments/body with non-closing task/PR/commit/evidence locators;
- after final closure only, set this task's Resolution commit and close this task's tracking Issue with completed reason.

The Executor may not close unrelated backfilled tracking Issues in this task.

If a required Project workflow setting is available only through GitHub's supported Web UI and the Executor has no supported browser surface, one minimal HUMAN_ONLY UI action may be requested. This is a one-time bootstrap dependency, not recurring board maintenance. No backfill may begin until actual workflow state has been re-read and verified.

## 6. Allowed repository modifications

Only:

- `AGENTS.md`
- `TODO.md`
- `docs/plugin-todos/README.md`
- new `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `README.md` only if the required README closure check concludes an update is genuinely needed
- `results/repo--maintenance-board-lifecycle/**`
- current task's ordinary Reviewed Handoff/control evidence as required by existing repo contract

No plugin source/generated payload/runtime/profile/Marketplace behavior changes.

Version decision:

```text
Repository bump decision: NONE
Affected plugins: all NO_BUMP
```

This is maintenance docs + GitHub Project metadata, not a production plugin release.

## 7. Bounded backfill

Backfill only one current-main snapshot.

Eligible:

- `CANDIDATE_GENERIC`
- `PROMOTE_NOW`
- still-valid `BLOCKED_NEEDS_EVIDENCE`
- active Planner–Critic / Reviewed Handoff work not otherwise represented
- top-level ideas whose core is integrated but whose already-required downstream adaptation is explicitly incomplete

Excluded:

- raw untriaged `NEW`
- `PROJECT_LOCAL`
- `REJECTED`
- `SUPERSEDED`
- ordinary project-specific research/product/code TODOs
- historical completed items without a specific current retrieval need

Deduplicate to one top-level Issue per idea. Ambiguous duplicates are skipped and reported rather than guessed.

No unrelated Issue is closed during backfill.

## 8. Required repository contract

After implementation:

- one canonical `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` owns the board lifecycle contract;
- `AGENTS.md` contains only a short mandatory locator/behavior rule;
- `TODO.md` explains TODO-inbox vs Project-dashboard ownership;
- `docs/plugin-todos/README.md` permits `tracking: #N` as a locator but not as a second status;
- public README receives an explicit closure check.

Because v0.1 Project visibility is private, expected README result is:

```text
README checked: no update required
```

unless execution changes the public user entry.

## 9. Required direct validation

The same final Project configuration must prove:

1. exact Project owner/title/visibility/repo link;
2. exact four Status options;
3. Area + Resolution commit fields;
4. approved views;
5. actual workflow enabled states, including PR-merged -> Done disabled;
6. exact issue-only auto-add filter;
7. this task's real tracking Issue is admitted once and set to DOING;
8. no implementation PR is a lifecycle item;
9. CLI/API can list/update the real item;
10. backfilled Issues match eligible canonical source items and do not blindly promote raw NEW;
11. repository docs consume the board contract without changing plugin production;
12. rerunning reconciliation does not create duplicate Project/items.

Mechanical text checks cannot substitute for actual GitHub Project/API evidence.

## 10. Non-completion closure route

If a tracked idea is later rejected/superseded/duplicate/not-planned, it must not appear as DONE.

For such an item:

- remove/archive the item from this Project first;
- then close the Issue with the truthful non-completion reason;
- do not add a fifth main Status.

If a previously DONE item is legitimately reopened because new evidence proves the old claim false, restore a truthful DOING/ADAPTING state and preserve the old closure history in the Issue; do not silently rewrite history.

## 11. Execution/review/integration order

### Stage A — implementation/bootstrap

After approved Kickoff:

- create exact branch/worktree;
- perform preflight;
- create/reconcile Project configuration;
- configure/verify BOARD-01 workflows;
- self-host this work item as the first tracking Issue;
- perform bounded backfill;
- update allowed repository docs;
- write durable result evidence;
- run Plan B1–B5;
- commit/push the exact task branch;
- stop for independent implementation review.

### Stage B — independent implementation review

Reviewer must inspect the real Project configuration/evidence and the repo diff, not only an Executor summary.

A Stage-A PASS does not yet make the top-level idea DONE.

### Stage C — final integration/closure

Only after independent implementation review PASS:

- fetch latest main;
- if semantic overlap/drift changes this approved contract, return Planner/Critic;
- otherwise integrate the reviewed task branch with ordinary non-force Git;
- verify remote main;
- use the canonical main closure/integration commit as this idea's Resolution commit;
- write it to the Project and tracking Issue;
- close this task's tracking Issue with completed reason;
- verify Project Status becomes DONE through issue-closed automation.

Only then may overall Goal be reported achieved.

## 12. Recovery / stop conditions

Stop rather than improvise if:

- exact worktree cannot be legally created;
- current GitHub account/permission identity is wrong;
- `project` scope is unavailable and cannot be obtained through the normal bounded auth flow;
- exact Project title is ambiguous/unrelated;
- required workflow configuration cannot be verified;
- BOARD-01 guardrail cannot be represented on current GitHub;
- backfill ownership is ambiguous for an item;
- latest-main drift changes lifecycle semantics/allowed surfaces;
- any requested action would require Bridge Kit/server/Host/paid/destructive scope not listed here.

Do not delete the Project to recover from partial setup. Leave it private, stop backfill, record the partial state, and resume idempotently after the blocker is resolved.

## 13. Explicit forbidden scope

No:

- production plugin behavior changes;
- generated Marketplace/plugin edits;
- Bridge Kit modifications;
- server/Host mutations;
- paid APIs;
- GitHub Actions or synchronization daemons;
- new database/registry/ledger/controller/watcher/state machine;
- repository-wide auto-close disablement;
- Project publication;
- raw-NEW bulk promotion;
- force push/history rewrite;
- arbitrary branch/worktree substitution;
- destructive cleanup of unrelated Project/Issue/branch state.

## 14. README and completion statement

Final result must explicitly record:

```text
README checked: updated | no update required
PROJECT_CONFIG_VERIFIED = YES
BOARD_01_GUARDRAILS_VERIFIED = YES
BACKFILL_SCOPE_VERIFIED = YES
RESOLUTION_COMMIT = <canonical main closure commit>
TRACKING_ISSUE_CLOSED_COMPLETED = YES
PROJECT_STATUS = DONE
OVERALL_GOAL_ACHIEVED = YES
```

Anything less remains unfinished, even if implementation code/docs or central integration already succeeded.
