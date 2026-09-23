# AI Skills 维护看板 — Implementation Plan v0.1

- Date: 2026-09-22
- Human label: AI Skills 维护看板与完成语义
- Task key: `repo--maintenance-board-lifecycle`
- Repository: `YuukiAS/AI_Skills_Collection`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_PROPOSAL_2026-09-22.md`
- Approved design commit: `da46f14141888c1bcd94bf94a486bcb1a1b0ec7c`
- Design Critic PASS: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V2_CRITIC_REVIEW_2026-09-22.md`
- Critic review commit: `8213c843b4d91c63f6de62740e26ef8d215a59e0`
- Package version: `v0.1`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Execution branch: `reviewed/repo--maintenance-board-lifecycle`
- Exact task worktree: sibling `../AI_Skills_Collection-repo--maintenance-board-lifecycle`, resolved from the canonical AI_Skills_Collection checkout root. The resolved absolute path must be recorded before creation; no alternate worktree path is authorized.
- This Plan does not itself authorize execution.

## 1. Positive target

Create one low-maintenance GitHub Project that lets the user see the real lifecycle of AI_Skills maintenance ideas without replacing the existing plugin TODO source.

The finished system must make four facts visible:

```text
TODO -> DOING -> ADAPTING -> DONE
```

- `TODO`: valid tracked idea, not actively being executed.
- `DOING`: design / implementation / review / central integration is active.
- `ADAPTING`: canonical core is already integrated, but required downstream repo/server/Host/install/normal-entry consumption is still incomplete.
- `DONE`: the top-level idea's complete contract is actually closed, including required adaptation and durable evidence.

The Project item is the top-level tracking Issue. Plugin TODO files remain the failure/evidence/maturity inbox. Reviewed Handoff / Planner–Critic / Executor tasks remain execution evidence.

The system must also answer for every completed item:

> Which canonical closure/evidence commit made this top-level idea DONE?

That answer lives in the `Resolution commit` Project field and the tracking Issue closure record.

## 2. Frozen implementation identity

### Git

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = latest origin/main at kickoff preflight
```

The worktree locator is exact relative to the canonical repo root. Before mutation, resolve it to one absolute sibling path and record it in `results/repo--maintenance-board-lifecycle/RESULT.md`.

If the current Host/sandbox cannot legally create this exact approved worktree, fail before GitHub Project/Issue mutation. Do not silently substitute `/tmp`, the dirty canonical checkout, another branch, or another path. If a sanctioned Bridge-owned bounded worktree primitive exists by execution time, it may be used without changing this locator; otherwise report the exact environment denial.

### GitHub Project

```text
owner = YuukiAS
title = AI Skills Maintenance
visibility = PRIVATE
linked repository = YuukiAS/AI_Skills_Collection
tracking label = maintenance-track
```

PRIVATE is the bootstrap default because the board is a maintainer surface. This task does not make it public. The underlying public Issues/TODO evidence remain governed by existing repository privacy rules.

## 3. Allowed repository changes

Only the following tracked repository surfaces may be changed:

- `AGENTS.md` — add a concise locator/consumer rule; do not duplicate the full board contract.
- `TODO.md` — explain the board vs plugin-TODO boundary and how maintainers find the board.
- `docs/plugin-todos/README.md` — add the optional `tracking: #N` locator rule and preserve existing TODO maturity semantics.
- new `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` — canonical steady-state board contract.
- `README.md` only after explicit README closure check. Because the Project remains private by default, do not add a public dead/private link merely for symmetry; record `README checked: no update required` unless execution changes visibility or creates a genuinely useful public entry.
- `results/repo--maintenance-board-lifecycle/**` — non-secret bootstrap, validation, backfill, and closure evidence.
- ordinary task-control/evidence files required by the existing Reviewed Handoff contract, if the current workflow creates them.

No `skills/`, generated Marketplace/plugin payload, plugin routing/runtime, profile, Bridge Kit, server, Host, provider, credential, or production application behavior changes are allowed.

Version decision for this task:

```text
Repository bump decision: NONE
Reason: maintenance docs + GitHub Project metadata only; no install/runtime release.
Affected plugins: all NO_BUMP
Reason: no central plugin production behavior changes.
```

## 4. GitHub capability reality used by this Plan

At package preparation time, official GitHub surfaces support:

- `gh project create/edit/link/field-create/field-list/item-add/item-edit/item-list` for project/item maintenance.
- `gh project` requires token scope `project`.
- the default `Status` field can be updated through GitHub GraphQL `updateProjectV2Field`; `gh project` currently has no dedicated field-edit subcommand.
- Project views can be created/updated through the documented Projects v2 API / GraphQL `createProjectV2View` and `updateProjectV2View`; do not invent a nonexistent `gh project view-create` command.
- GitHub documents enabling/disabling/configuring built-in Project workflows through the Project Web UI. The current public CLI does not expose a dedicated command for enabling/disabling those built-in workflows. Do not substitute deletion of a workflow for the approved semantic `disable` unless a later official supported API explicitly exposes equivalent enable/disable behavior and the Critic-reviewed contract still matches.
- Project workflows can be queried through the Projects v2 GraphQL object to verify names and `enabled` state.

Therefore the one-time bootstrap is split honestly:

1. CLI/API for project creation, metadata, repository link, fields, items, status values and views.
2. GitHub's supported Project UI for built-in workflow configuration when no supported mutation API exists.
3. After bootstrap, steady-state maintenance is CLI/API + existing built-in workflows; no recurring browser maintenance is required.

If the future Executor has a supported browser/UI automation surface, it may perform the bounded UI steps itself. If it does not, request one minimal HUMAN_ONLY GitHub UI action for workflow configuration, then resume the same Goal. Do not turn this into recurring user maintenance.

## 5. Bootstrap preflight — no mutation yet

Before any external Project/Issue mutation:

1. Fetch latest `origin/main`; verify repository identity and remote.
2. Verify/create only the exact reviewed task branch/worktree after the user sends the approved Kickoff.
3. Verify the current GitHub account is `YuukiAS`.
4. Run `gh auth status`; verify the token can access `YuukiAS/AI_Skills_Collection` and has `project` scope.
   - If scope is missing, request the single bounded auth refresh needed for `project`; do not proceed partially.
5. List user Projects and search exact title `AI Skills Maintenance`.
   - none: create one private Project.
   - exactly one: inspect owner, visibility, linked repo, fields, workflows and content before reusing.
   - multiple exact-title matches or an unrelated existing Project: stop with ambiguity evidence; do not create another.
6. Verify no existing `maintenance-track` label conflicts semantically. Reuse an equivalent one; otherwise create the exact label.
7. Record the preflight snapshot in repo evidence without secrets.

Do not modify Issues/backfill before the Project workflow guardrails in §7 are verified.

## 6. Create/reconcile Project structure

### 6.1 Project metadata

Create or reconcile:

```text
Title: AI Skills Maintenance
Owner: YuukiAS
Visibility: PRIVATE
Linked repo: YuukiAS/AI_Skills_Collection
```

Use `gh project create/edit/link` where supported.

### 6.2 Status field

Use the Project's canonical `Status` single-select field. It must contain exactly these lifecycle values for this board:

```text
TODO
DOING
ADAPTING
DONE
```

Do not add Planning/Review/Waiting/Blocked as main statuses.

If the default field requires option replacement, use the documented Projects GraphQL field mutation after first fetching the exact field ID and existing configuration. Do not delete/recreate the Project merely to change Status.

### 6.3 Area field

Create one `Area` single-select field if absent.

Options:

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

Each tracking item has one primary owner. Cross-owner evidence stays in the Issue instead of duplicating cards.

### 6.4 Resolution commit

Create one text field:

```text
Resolution commit
```

It is empty until final closure. It stores the owner-repo canonical closure/evidence commit, not every component SHA.

### 6.5 Views

Create/reconcile no more than four views:

1. `Board`
   - board layout;
   - grouped vertically by Status where the current API supports the grouping configuration; otherwise complete the grouping once through the supported Project UI.
2. `Active`
   - table layout;
   - filter `status:DOING,ADAPTING`.
3. `By area`
   - table layout;
   - expose Area and Status; group/slice by Area only if supported by the current API/UI without custom machinery.
4. `History`
   - table layout;
   - filter `status:DONE`;
   - show Resolution commit.

Use the documented Projects API/GraphQL view surfaces. Do not invent unsupported `gh project` subcommands.

## 7. BOARD-01 guardrails — must be configured before backfill

The approved blocker closure must be preserved exactly.

### Admission

Auto-add must be restricted to top-level tracking Issues:

```text
is:issue label:maintenance-track
```

Implementation/design PRs are not lifecycle items.

### Built-in workflows

Configure and then verify:

- `item added -> TODO`: enabled, so admitted tracking Issues start with a lifecycle status.
- `issue / pull request closed -> DONE`: keep the issue-closed behavior used for final closure.
- `pull request merged -> DONE`: disabled.

Use GitHub's supported Project workflow UI if no supported mutation API exists.

After configuration, query the Project's workflows and save durable evidence of workflow names and enabled states. Do not infer success from clicks alone.

### Tracking Issue link discipline

Before a tracking Issue truly satisfies DONE:

- no Development/manual linked relationship that would auto-close it when an intermediate PR merges;
- no `close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved` keyword targeting that tracking Issue in PR body or commit message;
- use only non-closing references such as `Related tracking issue: #N` or `Implements part of #N`;
- record task/PR/commit locators in the tracking Issue body/comments.

Do not disable repository-wide linked-PR auto-close.

### Non-completion terminal path

If an admitted idea is later rejected, superseded, duplicate, or otherwise closed as `not planned`:

1. remove/archive the item from this maintenance Project before closing the Issue;
2. close the Issue with the truthful non-completion reason;
3. do not let it appear in History as DONE.

This preserves the approved four-state lifecycle without inventing a fifth CANCELLED state.

## 8. Tracking Issue contract

A tracking Issue body must minimally contain:

```text
Source TODO / source locator:
Problem / top-level idea:
Primary Area:
Current Status rationale:
Completion contract:
Required downstream adaptation targets:
Task / PR / commit locators:
Normal-entry / real-consumer evidence:
Runtime/server/Host evidence locator (if applicable):
Next action:
Blocked by (if applicable):
Resolution commit:
```

This is a lightweight human-readable contract, not a new machine schema.

Plugin TODO files keep their own maturity/evidence status. They may add only:

```text
tracking: #<issue-number>
```

They must not duplicate Project execution Status.

## 9. Self-hosting normal-entry check

Use this maintenance-board work item itself as the first real tracking Issue instead of creating a synthetic test Issue.

After the Project workflow guardrails are configured:

1. create or locate one Issue for `AI Skills 维护看板与完成语义`;
2. apply `maintenance-track`;
3. verify it is auto-added to the Project;
4. set `Area=repo`;
5. set `Status=DOING`;
6. verify with `gh project item-list` / API that the Project contains the Issue, not an implementation PR;
7. keep it open until all Goal closure conditions, including main integration, are complete.

This directly tests the normal entry that later Planner/Codex maintenance will use.

## 10. Bounded backfill

Backfill is a one-pass snapshot of current canonical sources at execution time; it is not a Git-history archaeology job.

### Include

From current central plugin TODOs and standalone-skill TODOs:

- `CANDIDATE_GENERIC`;
- `PROMOTE_NOW`;
- still-valid `BLOCKED_NEEDS_EVIDENCE`;
- any item already under an active Planner–Critic / Reviewed Handoff implementation and not otherwise represented;
- any top-level idea whose canonical core is integrated but whose already-required downstream adaptation is explicitly still incomplete.

### Exclude

- raw, untriaged `NEW`;
- `PROJECT_LOCAL`;
- `REJECTED`;
- `SUPERSEDED`;
- purely historical `PROMOTED` / completed items unless there is a specific current retrieval need;
- project-specific research/product/code TODOs outside AI_Skills maintenance.

### Deduplication

- one top-level idea -> one tracking Issue;
- one primary owner / Area;
- merge multiple evidence locators into that Issue;
- if an existing Issue clearly represents the same idea, reuse it and add the tracking label instead of creating another;
- ambiguous duplicate candidates are skipped and reported, not guessed.

### Initial status

- qualifying inactive candidate -> TODO;
- active design/implementation/review -> DOING;
- canonical core done + required downstream pending -> ADAPTING;
- do not mass-backfill historical DONE.

No backfilled Issue may be closed by this stage.

## 11. Repository consumer rules

Implement the approved semantics with one canonical board document and short locators.

### New canonical doc

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` owns:

- four-state definitions;
- top-level idea vs TODO vs task boundary;
- admission/backfill rule;
- BOARD-01 closing-link discipline;
- Resolution commit definition;
- steady-state Planner/Codex commands and closure checks;
- non-completion terminal handling;
- post-DONE optional-consumer / regression rule.

### AGENTS

Add only a short mandatory locator/behavior rule for central maintenance:

- use the Project only after Planner triage;
- never mark DONE merely on task/PR/integration PASS;
- follow the canonical board doc;
- do not use closing relationships/keywords on tracking Issues before final closure.

Do not duplicate the full policy.

### TODO.md / plugin-todos README

Explain:

- TODO files remain the source inbox;
- Project is the execution dashboard;
- `tracking: #N` is a locator, not a second status field.

### README closure

Because the board is private in v0.1, default result is:

```text
README checked: no update required
```

Only update README if execution changes Project visibility/public user entry. Do not expose a private-maintainer link in public README merely to advertise the internal board.

## 12. Verification gates

All checks target the same final Project configuration and task candidate.

### B1 — Project structure

Directly verify:

- exact owner/title/visibility/repo link;
- Status options exactly TODO/DOING/ADAPTING/DONE;
- Area and Resolution commit fields exist;
- Board / Active / By area / History views exist with intended filters/layouts.

### B2 — BOARD-01

Directly verify actual workflow state:

- auto-add filter is `is:issue label:maintenance-track`;
- PR-merged -> Done is disabled;
- issue-closed -> Done behavior is enabled for final closure;
- item-added -> TODO is enabled if used;
- no implementation PR is admitted as a lifecycle item;
- the live tracking Issue has only non-closing references before final closure.

Mechanical docs checks are supporting evidence only; actual Project workflow configuration is authoritative.

### B3 — Normal entry / idempotency

- this task's tracking Issue is admitted once;
- rerunning the reconcile/list path does not create a duplicate Project or duplicate tracking Issue;
- status/field update works through the supported CLI/API path.

### B4 — Backfill fidelity

For the one-pass canonical snapshot:

- every created tracking Issue points to a valid current source TODO/design locator;
- raw NEW / rejected / project-local items were not blindly promoted;
- duplicate source evidence maps to one Issue;
- ADAPTING is used only where required downstream work is explicitly part of the completion claim.

### B5 — Repository documentation

- canonical board doc exists;
- AGENTS/TODO/plugin TODO README point to it without duplicating the whole contract;
- no production plugin/generated payload changed;
- version decision is NO_BUMP;
- README closure is recorded.

### B6 — Final closure

Only after independent implementation review PASS and latest-main integration:

1. integrate the reviewed docs/evidence to `main` with ordinary non-force Git, preserving concurrent unrelated work;
2. verify remote `main`;
3. use that canonical main closure/integration commit as this idea's `Resolution commit`;
4. write it to Project + tracking Issue;
5. confirm all required adaptation for this idea is complete (for this board task, Project configuration itself is the required external consumer);
6. close this tracking Issue with completed reason;
7. verify Project Status becomes DONE by the issue-closed workflow.

Overall Goal is not achieved before B6.

## 13. Independent review and integration

Executor first completes bootstrap, docs, bounded backfill and B1–B5 on the reviewed branch, commits/pushes exact evidence, and stops for independent implementation review.

No user acceptance gate is required solely to inspect the board if B1–B5 provide direct Project/API evidence; a real user-only action is required only if GitHub exposes a necessary built-in workflow setting exclusively through UI and the current Executor has no supported browser surface.

After independent implementation review PASS:

- fetch latest main;
- if new drift changes this board contract, Project workflow semantics, TODO authority, or allowed docs, return Planner/Critic;
- unrelated drift may be integrated normally;
- perform ordinary non-force main integration;
- run B6 and final remote verification.

Do not use squash/rebase/history rewrite/force push.

## 14. Failure recovery

### Missing `project` scope

Stop before Project mutation. Request one bounded auth refresh; resume same Goal after success.

### Exact worktree cannot be created

Stop before external Project/Issue mutation. Do not change locator or fall back to `/tmp`/dirty checkout.

### Project created but workflow UI cannot be configured

Leave the Project private and empty except safe metadata. Do not start backfill. Surface one minimal UI action or use a supported browser-capable executor. Resume after querying and verifying actual workflow state.

### Partial field/view failure

Do not delete/reset the Project. Re-read existing fields/views and reconcile idempotently by name/id.

### Backfill ambiguity

Skip ambiguous item, record source locators and reason, continue independent items. Do not invent a merge decision.

### Accidental early Issue closure

Immediately stop lifecycle mutation. Reopen the tracking Issue if allowed, restore the truthful DOING/ADAPTING status, record the incident, and return Planner if the false-DONE path contradicts the approved guardrail rather than silently continuing.

### Main drift

Only unrelated drift may be integrated in the approved closure. Semantic overlap returns Planner/Critic.

## 15. Explicit non-goals

Do not:

- change plugin production behavior, routing, generated payload, profile exposure or release identity;
- modify Bridge Kit;
- touch server/Host/production deployment;
- call paid APIs;
- create GitHub Actions, sync daemons, databases, registries, ledgers, controllers, watchers or another workflow state machine;
- make the Project public;
- add Planning/Review/Waiting/Blocked as main Status values;
- convert every raw NEW item into an Issue;
- disable repository-wide Issue auto-close;
- use closing keywords/linked PR auto-close on maintenance tracking Issues before final closure;
- delete unrelated Projects/Issues/branches;
- force push or rewrite history.

## 16. User-visible value after closure

When this Plan succeeds, the user gets one durable maintenance dashboard where:

- backlog, active work, required downstream adaptation and true completion are visually distinct;
- DONE cannot be produced merely by an intermediate PR merge;
- every DONE item has one canonical Resolution commit plus detailed component/runtime evidence in its Issue;
- plugin TODOs remain the long-term evidence inbox instead of being duplicated;
- Planner/Codex can maintain the board through normal GitHub Issue + Project CLI/API operations without recurring manual drag-and-drop.
