# AI Skills 维护看板 — Canonical Goal v0.2

- Human label: AI Skills 维护看板与完成语义
- Task key: `repo--maintenance-board-lifecycle`
- Repository: `YuukiAS/AI_Skills_Collection`
- Package version: `v0.2`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`
- Approved design commit: `da46f14141888c1bcd94bf94a486bcb1a1b0ec7c`
- Design Critic PASS: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`
- Design Critic review commit: `8213c843b4d91c63f6de62740e26ef8d215a59e0`
- Previous execution review: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-22.md`
- Previous execution review commit: `4aaa95d79e84af63c93362612988cf79829d8043`
- Implementation Plan: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_2_2026-09-22.md` v0.2
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`

This Goal is not executable until an independent Critic reviews this exact v0.2 Plan + Goal + Kickoff and returns `READY_FOR_CODEX=YES`. Only when the user later sends the verbatim approved Kickoff does the current user message authorize the bounded effects below.

## 1. Exact execution identity

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = latest origin/main at kickoff preflight
```

The worktree path is exact relative to the canonical repository root. Resolve it once to its absolute sibling path and record that path before creation. No alternate worktree, branch, `/tmp` fallback, dirty-checkout substitution, or task-key substitution is authorized.

## 2. Required user result

The overall Goal is achieved only when the user has one working, readable, actively maintained GitHub Project for AI_Skills maintenance with these semantics:

```text
TODO -> DOING -> ADAPTING -> DONE
```

The user must be able to open the Project and directly understand:

- which plugin / Area each tracked idea belongs to;
- which ideas have not started;
- which are actively being designed / implemented / reviewed;
- which have central core complete but still require downstream adaptation;
- which are truly complete;
- what the current active execution anchor is for each DOING / ADAPTING item;
- which canonical Resolution commit closed each DONE item.

The Project item is the top-level tracking Issue. Plugin TODO files remain the failure/evidence/maturity inbox. Planner–Critic / Reviewed Handoff / Executor tasks remain execution evidence.

## 3. Lifecycle contract

### TODO

A triaged idea that is worth tracking but is not currently in substantive execution.

### DOING

The top-level idea is actively in design, implementation, review or central integration.

### ADAPTING

The canonical core is already integrated, but one or more required downstream repo/server/Host/install/normal-entry consumers from the completion contract are still incomplete.

### DONE

Only after the complete top-level idea contract is closed.

DONE requires:

1. the original problem is actually solved;
2. canonical owner source is integrated;
3. all required downstream adaptation is complete or explicitly N/A / NO_CHANGE;
4. normal-entry / real-consumer validation is complete;
5. non-Git runtime/server/Host evidence has a durable locator when applicable;
6. Resolution commit is recorded;
7. the tracking Issue is explicitly closed as completed;
8. the Project reaches DONE through the final issue-closed workflow.

A task PASS, Critic PASS, PR merge, test PASS or central integration alone cannot produce DONE.

WAITING / BLOCKED are not fifth lifecycle states; they remain next-action / blocker conditions.

## 4. Required Project identity and fields

Create or reconcile exactly one private maintainer Project:

```text
owner = YuukiAS
title = AI Skills Maintenance
visibility = PRIVATE
linked repo = YuukiAS/AI_Skills_Collection
tracking label = maintenance-track
```

Required fields:

### Status

```text
TODO
DOING
ADAPTING
DONE
```

No fifth lifecycle status.

### Area

At least:

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

Text field. Empty before final closure.

Required views, no more than:

- Board
- Active
- By area
- History

## 5. Human-readable board contract — BOARD-UX-01

Every tracking Issue must use a natural, concise human-readable title.

Task key, branch, hash, path or internal status string must not be the title's main content.

Every tracking Issue top section must contain, in this order:

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

Detailed historical evidence goes below this top section.

Each DOING / ADAPTING item must have at least one current valid proposal/task/workflow/branch/PR/commit/runtime locator, preceded by a short human explanation of what that locator represents.

DONE items must expose Resolution commit directly in History.

Board / By area must let the user see at least:

- human-readable title;
- Area / plugin;
- Status.

Each Area with tracked items must be directly filterable or groupable.

## 6. Clear Writing requirement

The user-facing maintenance board is a reader-facing artifact, not an internal log.

### Codex / Executor hard requirement

Whenever Codex creates or modifies human-visible Kanban / Project text, it must invoke the current installed Clear Writing plugin (`writing-style`) before the GitHub mutation.

This applies to:

- tracking Issue titles;
- the top “问题 / 当前进度 / 当前执行锚点 / 下一步” summary;
- reader-facing board card copy;
- human-readable closure / History descriptions;
- backfilled tracking Issue copy that is created or materially rewritten.

Clear Writing may improve wording and structure but must not change lifecycle truth, Area ownership, required downstream targets, commit/branch/PR locators, Resolution commit or evidence meaning.

If Codex cannot actually invoke Clear Writing, it must not claim it did and must not batch-write generic board copy. It stops that reader-facing mutation and reports `CLEAR_WRITING_UNAVAILABLE` for same-Goal recovery.

### Planner / Critic / GPT

Planner / Critic / maintenance GPT should also use Clear Writing when that plugin is available on the current surface. If the current GPT surface cannot invoke it, GPT must still obey the same human-facing contract and may not offload copy cleanup to the user.

Clear Writing invocation evidence is supporting evidence only. Actual Project / Issue readability is authoritative.

## 7. Active synchronization contract — BOARD-SYNC-01

The board must follow actual AI_Skills maintenance work without waiting for user reminders.

### Raw NEW

A real-project thread that records a raw `NEW` still only updates the appropriate plugin TODO inbox. It does not automatically create a Project item.

### Planner triage

When Planner determines an idea has entered tracking scope, Planner must in the same round:

- create or bind a top-level tracking Issue;
- add `maintenance-track`;
- create the readable title and top summary;
- assign Area;
- set truthful initial Status;
- write `tracking: #N` back to the canonical plugin TODO;
- record the current proposal/task locator if one already exists.

### Planner substantive round

When a substantive design / implementation round starts, Planner must proactively reconcile:

- Status = DOING when lifecycle truth requires it;
- current progress;
- current execution anchor;
- next action.

### Critic review

After every formal Critic review, Critic must proactively reconcile:

- current Critic review locator;
- next action;
- lifecycle truth.

PASS / REVISE itself does not mechanically change Status. Status only changes when the top-level lifecycle truth changes.

Critic does not edit Planner's Proposal or Reviewed Handoff CURRENT; this synchronization is limited to board evidence and lifecycle truth.

### ADAPTING

When canonical core is integrated but required downstream adaptation remains, the current owner must set ADAPTING and replace the current anchor with the active downstream repo/branch/commit/runtime validation.

### DONE

Final DONE follows only §3.

### No routine user maintenance

Routine board reconciliation does not ask the user to drag cards or repeat authorization.

If the current GPT surface lacks Project mutation capability:

1. GPT updates any tracking Issue summary/evidence it can update directly;
2. GPT emits an exact pending Project mutation in its handoff for the next Project-capable Executor/maintenance action;
3. the next capable Executor consumes those pending mutations before unrelated board mutations, after checking they are still current.

Example:

```text
待同步到 Project：
- tracking Issue: #123
- Status: DOING
- Area: presentations
- 当前执行锚点: Presentations v3 proposal — <locator>
- 新增 review/evidence: <locator>
- 下一步: Critic 复核 v3
```

GPT must never claim the Project has been updated when it has not.

## 8. BOARD-01 remains frozen

Required:

1. lifecycle item only = `maintenance-track` tracking Issue;
2. auto-add filter at least `is:issue label:maintenance-track`;
3. implementation/design PRs are not lifecycle items;
4. Project `pull request merged -> Done` workflow is disabled;
5. before true DONE, tracking Issues are not linked to intermediate PRs through an auto-closing relationship;
6. PR body / commit message do not target tracking Issues with GitHub closing keywords;
7. intermediate task/PR/commit relations use only non-closing references;
8. repository-wide linked-PR auto-close stays unchanged;
9. `issue closed -> Done` remains only the final mechanical mapping after the full DONE checklist.

Rejected / superseded / duplicate / not-planned tracking Issues must first be removed or archived from this Project, then truthfully closed without appearing as DONE.

## 9. Allowed external GitHub effects after approved Kickoff

Within the exact account/repository/project scope, Executor may:

- inspect current Projects, fields, views and workflows;
- verify/request the `project` OAuth scope when genuinely absent;
- create or reconcile the single private `AI Skills Maintenance` Project;
- link only `YuukiAS/AI_Skills_Collection`;
- create/reconcile the approved Status, Area and Resolution commit fields;
- create/reconcile the approved four views;
- configure/read back the approved built-in Project workflows and auto-add rule;
- create/reuse the `maintenance-track` label;
- create/reuse/update only tracking Issues that pass bounded backfill;
- update Issue reader-facing text only after the required Clear Writing pass for Codex;
- add/update eligible tracking Issues in the Project;
- create the tracking Issue for this maintenance-board work itself;
- update its non-closing task/PR/commit/review locators;
- after final closure only, set this task's Resolution commit and close this task's tracking Issue as completed.

The Executor may not close unrelated backfilled tracking Issues.

If a required Project workflow setting remains available only through GitHub's supported Web UI and the Executor lacks a supported browser surface, one minimal HUMAN_ONLY UI action may be requested. The same Goal must automatically resume after the action is verified. No backfill begins before actual workflow state is read back.

## 10. Allowed repository modifications

Only:

- `AGENTS.md`
- `TODO.md`
- `docs/plugin-todos/README.md`
- new `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `README.md` only if the explicit closure check determines an update is genuinely needed
- `results/repo--maintenance-board-lifecycle/**`
- ordinary task-control/evidence files required by the current Reviewed Handoff contract

No plugin source/generated payload/runtime/profile/Marketplace behavior changes.

Version decision:

```text
Repository bump decision: NONE
Affected plugins: all NO_BUMP
```

## 11. Bounded backfill

One current-main snapshot only.

Include:

- `CANDIDATE_GENERIC`
- `PROMOTE_NOW`
- still-valid `BLOCKED_NEEDS_EVIDENCE`
- active Planner–Critic / Reviewed Handoff work not otherwise represented
- top-level ideas whose canonical core is integrated but whose already-required downstream adaptation remains incomplete

Exclude:

- raw untriaged `NEW`
- `PROJECT_LOCAL`
- `REJECTED`
- `SUPERSEDED`
- project-specific research/product/code TODOs
- historical completed items without a specific current retrieval need

Deduplicate to one top-level Issue per idea. Ambiguous duplicates are skipped and reported rather than guessed.

No unrelated Issue is closed during backfill.

## 12. Required repository contract

Implementation must produce one canonical:

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

It owns:

- lifecycle;
- human-readable copy contract;
- Clear Writing rule;
- Planner/Critic/GPT active sync contract;
- pending mutation fallback;
- BOARD-01;
- admission/backfill;
- Resolution commit;
- non-completion terminal path;
- post-DONE follow-up/regression rule.

`AGENTS.md` must contain only a short mandatory locator/consumer rule that requires AI_Skills maintenance threads to reconcile the board without user reminders and requires Codex board copy to use Clear Writing.

`TODO.md` and `docs/plugin-todos/README.md` must preserve TODO inbox ownership and permit only a `tracking: #N` locator, not duplicate execution status.

Because the Project remains private by default, expected README result is:

```text
README checked: no update required
```

unless execution changes the public user entry.

## 13. Required direct validation

The same final Project configuration must prove:

1. exact Project owner/title/visibility/repo link;
2. exact four Status options;
3. Area + Resolution commit fields;
4. approved views;
5. actual Project workflow enabled states, including PR-merged -> Done disabled;
6. exact issue-only auto-add filter;
7. this task's real tracking Issue is admitted once and set to DOING;
8. no implementation PR is a lifecycle item;
9. CLI/API can list/update the real item;
10. bounded backfilled Issues map to valid current source items;
11. role sync rules exist in both AGENTS locator and canonical board doc;
12. rerunning reconciliation does not create duplicates.

Mechanical checks cannot substitute for actual surface review.

## 14. Required qualitative Project-surface review

Independent implementation review must inspect the actual GitHub Project / Issue surface.

At minimum it must inspect:

- Board;
- By area;
- this task's tracking Issue;
- all tracking Issue titles/top summaries created or materially rewritten by this bootstrap.

The reviewer must determine whether:

- Board cards show understandable title + Area + Status;
- every Area with tracked items can be viewed directly;
- DOING / ADAPTING items expose one current valid execution anchor;
- Issue top summaries clearly show problem, current progress, current anchor and next step;
- machine task keys/hashes/paths do not substitute for human explanation;
- locators remain exact after Clear Writing;
- DONE/History exposes Resolution commit.

Field presence, keyword scan, character count, API receipt or `CLEAR_WRITING_USED=YES` cannot by themselves establish PASS.

## 15. Execution / review / integration order

### Stage A — bootstrap / implementation

After approved Kickoff:

- create exact branch/worktree;
- preflight GitHub scope and Clear Writing availability;
- create/reconcile Project;
- configure/read back BOARD-01;
- self-host this maintenance item as the first tracking Issue;
- perform bounded backfill;
- update allowed repository docs;
- run structural + surface + sync validations;
- commit/push exact task branch;
- stop for independent implementation review.

### Stage B — independent implementation review

Reviewer must inspect the actual Project configuration, actual human-facing surface, repo diff and role-sync contract.

Stage-A success does not make the top-level idea DONE.

### Stage C — final integration / closure

Only after independent implementation review PASS:

- fetch latest main;
- semantic overlap/drift -> return Planner/Critic;
- otherwise integrate with ordinary non-force Git;
- verify remote main;
- use the canonical main closure/integration commit as this idea's Resolution commit;
- write it to Project + tracking Issue;
- verify all required adaptation for this board idea is complete;
- close only this task's tracking Issue as completed;
- verify issue-closed workflow makes Project DONE;
- verify History directly shows Resolution commit.

Only then may overall Goal be reported achieved.

## 16. Recovery / stop conditions

Stop rather than improvise if:

- exact worktree cannot be legally created;
- GitHub account/permissions are wrong;
- `project` scope is unavailable and cannot be obtained via normal bounded auth;
- Clear Writing cannot be invoked by Codex before human-facing board copy mutation;
- exact Project title is ambiguous/unrelated;
- required workflow configuration cannot be verified;
- BOARD-01 cannot be represented;
- backfill ownership is ambiguous;
- latest-main drift changes lifecycle / allowed surfaces;
- any requested action would require Bridge Kit/server/Host/paid/destructive scope outside this Goal.

Do not delete the Project to recover from partial setup. Leave it private, stop unsafe follow-on mutations, record the partial state, and resume idempotently after the blocker is resolved.

## 17. Explicit forbidden scope

No:

- production plugin behavior change;
- generated Marketplace/plugin edits;
- Clear Writing plugin source modification;
- Bridge Kit modification;
- server/Host mutation;
- paid APIs;
- GitHub Action / sync daemon / database / registry / ledger / controller / watcher / new state machine;
- repository-wide auto-close disablement;
- Project publication;
- raw-NEW bulk promotion;
- fifth lifecycle state;
- force push/history rewrite;
- arbitrary branch/worktree substitution;
- destructive cleanup of unrelated Project/Issue/branch state.

## 18. Final completion statement

Final evidence must explicitly establish:

```text
README checked: updated | no update required
PROJECT_CONFIG_VERIFIED = YES
BOARD_01_GUARDRAILS_VERIFIED = YES
BOARD_UX_READABILITY_VERIFIED = YES
BOARD_SYNC_ROLE_CONTRACT_VERIFIED = YES
CLEAR_WRITING_BOARD_COPY_USED = YES
BACKFILL_SCOPE_VERIFIED = YES
RESOLUTION_COMMIT = <canonical main closure commit>
TRACKING_ISSUE_CLOSED_COMPLETED = YES
PROJECT_STATUS = DONE
OVERALL_GOAL_ACHIEVED = YES
```

`CLEAR_WRITING_BOARD_COPY_USED=YES` is not sufficient without the qualitative surface PASS.

Anything less remains unfinished.
