# AI Skills 维护看板 — Implementation Plan v0.3

- Date: 2026-09-24
- Human label: AI Skills 维护看板与完成语义
- Task key: `repo--maintenance-board-lifecycle`
- Repository: `YuukiAS/AI_Skills_Collection`
- Package version: `v0.3`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- Approved design commit: `d14565e152b9b953c76c0722ad6e6343850335a7`
- Design Critic PASS: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_CRITIC_REVIEW_2026-09-24.md`
- Critic review commit: `012a43c7edefddd7f071d43425f7be937453f73a`
- Supersedes for execution: v0.2 Plan / Goal / Kickoff
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Execution branch: `reviewed/repo--maintenance-board-lifecycle`
- Exact task worktree: `../AI_Skills_Collection-repo--maintenance-board-lifecycle`
- This Plan does not itself authorize execution.

## 1. Product target

Create one human-readable, low-maintenance GitHub Project for the full AI_Skills maintenance backlog and make it part of the normal Planner / Critic / Codex maintenance path.

The lifecycle is fixed:

```text
TODO -> DOING -> ADAPTING -> DONE
```

Meanings:

- `TODO`: a current top-level maintenance idea is visible and worth tracking, but substantive execution has not started.
- `DOING`: design, implementation, review, or canonical central integration is actively in progress.
- `ADAPTING`: central implementation is complete, but required real machine consumers are not all adapted and verified.
- `DONE`: the top-level completion contract is fully satisfied.

The Project item is one top-level tracking Issue. Plugin TODO files remain the failure/evidence/maturity inbox. Planner–Critic / Reviewed Handoff / Executor tasks remain execution evidence.

`Project lifecycle status != plugin TODO maturity status`.

A raw `NEW` may be visible as Project `TODO` while remaining `NEW` in its source inbox.

## 2. Exact execution identity

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = kickoff-time latest origin/main
```

Before any external Project/Issue mutation:

1. resolve the relative worktree locator from the canonical repo root to one absolute sibling path;
2. record the resolved path in `results/repo--maintenance-board-lifecycle/RESULT.md`;
3. create only the exact reviewed branch/worktree after the user sends the Critic-approved Kickoff.

If the Host/sandbox cannot legally create this exact worktree, stop before Project/Issue mutation. Do not silently use `/tmp`, a dirty canonical checkout, another branch, or another path.

A sanctioned existing bounded worktree primitive may execute the same exact locator if available; this Plan does not authorize Bridge Kit changes.

## 3. GitHub Project identity

Create or reconcile exactly one:

```text
owner = YuukiAS
title = AI Skills Maintenance
visibility = PRIVATE
linked repository = YuukiAS/AI_Skills_Collection
tracking label = maintenance-track
```

If no exact-title Project exists, create one private Project.

If exactly one compatible Project exists, inspect and reconcile it.

If multiple exact-title Projects exist, or the only exact-title Project is unrelated, stop with ambiguity evidence; do not create another one.

## 4. Project fields and views

### Status

Canonical single-select values:

```text
TODO
DOING
ADAPTING
DONE
```

No fifth lifecycle state.

### Area

Use one primary-owner field with at least:

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

One text field:

```text
Resolution commit
```

It stores the canonical owner-repo closure/evidence commit for a DONE item, not every component SHA.

### Views

Create/reconcile no more than four:

1. **Board**
   - board layout;
   - grouped by Status;
   - cards visibly show human-readable title, Area, Status.

2. **Active**
   - table layout;
   - filter DOING / ADAPTING;
   - show title, Area, Status.

3. **By area**
   - table/grouped view;
   - direct filter/group by Area;
   - show title, Area, Status.

4. **History**
   - filter DONE;
   - show title, Area, Status, Resolution commit.

Do not add a `Current workflow`, `Machine state`, `Maturity`, WAITING, BLOCKED, or consumer-status Project field unless a future separately approved design proves it necessary.

## 5. GitHub bootstrap route

Keep the already reviewed GitHub-native path.

Use supported `gh project` commands for project/item operations where available, including create/edit/link/field-create/field-list/item-add/item-edit/item-list.

Use the documented Projects API/GraphQL for operations not exposed by dedicated CLI, including Status option or view mutation when required.

Do not invent nonexistent `gh project` subcommands.

For GitHub built-in Project workflows / auto-add configuration, use the current supported GitHub Project UI when no supported mutation API exists.

Read back real Project workflow/config state after setup; do not treat a click or command receipt as proof.

`gh project` preflight must verify the authenticated identity and required `project` scope.

If a necessary built-in workflow setting is UI-only and the Executor has no supported browser surface, request one minimal HUMAN_ONLY GitHub UI action and resume the same Goal after readback verification. This is one-time bootstrap, not routine maintenance.

## 6. BOARD-01 — false-DONE prevention

Before any backfill, configure and verify all of these:

### Admission

Auto-add must be restricted to tracking Issues:

```text
is:issue label:maintenance-track
```

Implementation/design PRs are not lifecycle items.

### Built-in workflows

- item added -> TODO: enabled if used;
- issue closed -> DONE: enabled for final closure;
- pull request merged -> DONE: disabled.

### PR / Issue link discipline

Before true DONE:

- do not create a Development/manual link that makes an intermediate PR merge auto-close the top-level tracking Issue;
- do not target the tracking Issue from PR body or commit message with `close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved`;
- use non-closing references only;
- store task/PR/commit/review locators in the Issue evidence/history section.

Do not disable repository-wide linked-PR auto-close.

### Non-completion closure

If an admitted item becomes rejected, superseded, duplicate, or not-planned:

1. remove/archive it from this Project;
2. close the Issue with the truthful non-completion reason;
3. do not let it appear in DONE/History.

## 7. Human-readable tracking Issue contract

The Project is a user-facing artifact.

Tracking Issue titles must be natural and concise. Task keys, hashes, branch names, file paths, or internal status strings may appear as locators but must not be the title's main content.

Every tracking Issue begins with this short section:

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

Rules:

- **问题**: one clear sentence describing the top-level user-visible problem/capability.
- **当前进度**: plain-language explanation of the current lifecycle truth.
- **当前执行锚点**: one or a few currently valid proposal/task/workflow/branch/PR/commit/runtime locators, each preceded by a human explanation.
- **下一步**: the real next action and current owner.

Detailed historical evidence goes after the top section.

Each DOING / ADAPTING item must have at least one current valid anchor.

DONE items must show Resolution commit directly in History.

## 8. Clear Writing is mandatory for Codex board copy

Whenever Codex creates or materially rewrites reader-facing Project/Issue text, it must invoke the installed Clear Writing plugin (`writing-style`) before the GitHub mutation.

This includes:

- tracking Issue titles;
- the top problem/progress/anchor/next-step section;
- reader-facing board copy;
- backfilled tracking Issue copy;
- human-readable closure / History text.

Clear Writing may improve structure and prose, but must not change:

- source maturity;
- lifecycle status;
- Area;
- required-consumer truth;
- proposal/task/branch/PR/commit locators;
- Resolution commit;
- evidence meaning or claim strength.

If Codex cannot truly invoke Clear Writing, it must not claim that it did and must not batch-write generic board copy. Stop that reader-facing mutation and report:

```text
CLEAR_WRITING_UNAVAILABLE
```

Actual Project-surface qualitative review is authoritative. A flag such as `CLEAR_WRITING_USED=YES` is only supporting evidence.

## 9. One-time full-inbox bootstrap

The initial bootstrap must scan every current canonical maintenance inbox named by the current root `TODO.md`, including:

- all central plugin TODO files;
- current standalone-skill TODO inboxes;
- any other current maintenance inbox explicitly declared by root TODO.

For every current entry that still has maintenance meaning, create a disposition. Allowed bootstrap dispositions:

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

### Raw NEW

A valid central raw `NEW` must not remain invisible only because it has not been promoted.

For each valid raw NEW:

- clear duplicate -> merge evidence into the existing top-level tracking Issue;
- independent top-level maintenance idea -> create a Project `TODO` tracking Issue;
- source maturity remains `NEW` unless Planner separately completes promotion triage.

Project TODO does not mean `CANDIDATE_GENERIC` or `PROMOTE_NOW`.

### Dedupe

Do not mechanically create one Issue per Markdown heading.

Group only when the evidence clearly represents the same top-level idea.

If combining two TODOs would require substantive genericity judgment, do not guess merely to reduce card count; preserve separate tracking or hand back to Planner triage.

### Coverage evidence

Create:

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

For every relevant source entry, record:

```text
source inbox + heading
-> disposition
-> tracking Issue (if any)
-> Area
-> initial lifecycle Status (if tracked)
```

This is one-time bootstrap completeness evidence, not a long-term registry/schema. It is never the steady-state status source.

Bootstrap fails completeness review if any current meaningful inbox item is neither represented by a tracking Issue nor given an explicit non-tracked disposition.

## 10. Steady-state canonical policy and consumer locators

Create one canonical board policy:

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

That file owns the full lifecycle/board contract.

Other surfaces only contain short trigger/locator/consumer rules and must not duplicate the policy.

### AI_Skills AGENTS.md

Add a concise mandatory locator covering:

- AI_Skills TODO / Planner / Critic / adaptation / closure work must read the canonical board doc;
- routine board reconciliation does not wait for user reminders;
- Codex board reader-facing copy requires Clear Writing;
- no early task/PR/integration -> DONE shortcut.

### Planner Role Contract

Add a minimal AI_Skills-maintenance consumer rule:

- triage into tracking scope -> create/bind tracking Issue or emit exact pending mutation;
- first substantive Plan/design round -> reconcile DOING + current anchor;
- handoff -> current next action/evidence;
- central implementation complete + required consumers pending -> ADAPTING and freeze exact consumer locators;
- no Project mutation tool -> exact pending mutation;
- no manual user Kanban sync.

### Critic Role Contract

Add a minimal AI_Skills-maintenance consumer rule:

- each formal review reconciles review locator, next action, lifecycle truth;
- PASS/REVISE alone does not mechanically change Status;
- implementation Reviewer PASS may lead to ADAPTING only after all required canonical central-closure conditions are actually satisfied;
- no Project mutation tool -> exact pending mutation;
- Critic still does not edit Planner Proposal, advance Reviewed Handoff CURRENT, or impersonate Executor.

### TODO.md / docs/plugin-todos/README.md

Clarify:

- TODO files remain the failure/evidence/maturity inbox;
- Project is the execution dashboard;
- `tracking: #N` is a locator, not a second maturity/status source;
- raw NEW may be visible as Project TODO without promotion.

## 11. ChatGPT Project instructions — one-time GPT normal-entry setup

The AI Research Stack ChatGPT Project requires one short trigger/locator, not a copy of the board policy.

Exact text to add:

```text
AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。
```

This is a one-time normal-entry setup.

Because the locator points to `main`, apply it only after the canonical board doc has been integrated to main.

If the current execution surface cannot modify ChatGPT Project instructions directly, request one HUMAN_ONLY action:

```text
Project -> ... -> Project settings -> instructions
append the exact approved text above
```

After the user confirms completion, resume the same Goal. Do not ask again during routine sync.

Do not claim this setting is installed unless it was actually set.

## 12. No-tool pending Project mutation contract

A Planner / Critic / GPT surface without Project mutation capability remains the semantic owner.

It must:

1. update any tracking Issue evidence/summary it can legitimately update;
2. produce an exact pending Project mutation in its handoff;
3. not claim the Project has been updated;
4. not ask the user to drag the card manually.

Minimal example:

```text
待同步到 Project：
- tracking Issue: #123
- Status: DOING
- Area: presentations
- 当前执行锚点: Presentations v3 proposal — <locator>
- 新增 review/evidence: <locator>
- 下一步: Critic 复核 v3
```

The next Project-capable maintenance action must check that the mutation still belongs to the current tracking Issue and remains current before applying it.

## 13. Two-level completion semantics

### Central implementation complete

For a formal AI_Skills implementation:

```text
execution-ready Critic PASS
-> Codex implementation
-> independent implementation review PASS
-> canonical owner integration/release closure (when the frozen Goal requires it)
= central implementation complete
```

Execution-ready Critic PASS by itself remains DOING.

Executor self-report remains DOING until independent implementation review passes.

If the frozen Goal requires canonical integration/release closure, Reviewer PASS alone still remains DOING until that closure actually occurs.

### Machine-consumed workflow cutover

If the top-level item is a machine-consumed workflow/shared maintenance mechanism:

```text
central implementation complete
-> DOING -> ADAPTING
```

For a non-machine-consumed item, the frozen completion contract may allow direct central closure without the five-consumer requirement.

## 14. Required logical consumers for machine-consumed workflow

Current default required logical consumer set:

### Server / remote Codex

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

### Local machine

4. `Workstation`
5. `Legion`

This applies only to machine-consumed workflow/shared maintenance mechanisms.

Pure docs, audit-only work, isolated artifact quality improvement, and ordinary domain-plugin professional improvement do not automatically inherit five-machine rollout.

### Freeze exact current consumer identities at ADAPTING

When the item enters ADAPTING, resolve each logical consumer into the current exact identity/locator needed for that item.

Do not hard-code hostname, SSH alias, CODEX_HOME, account, checkout, or credential into the long-lived policy.

Once resolved, record the exact consumer identities in the tracking Issue and freeze them for that item's downstream completion contract.

A future optional machine does not retroactively expand an already frozen contract.

A consumer may be N/A only when the frozen completion contract contains a direct, durable reason.

## 15. Per-consumer AI Skills Maintainer route

AI Skills Maintainer is a **per-current-consumer adaptation executor**, not a cross-machine controller.

This board task does not implement or release the future machine-update capability.

When that capability is production-ready, for each required consumer:

1. invoke Maintainer in that consumer's current Codex environment;
2. or use an existing separately approved remote execution route that preserves the same per-consumer boundary;
3. Maintainer handles only that consumer's:
   - discovery;
   - update/adaptation;
   - installed/loaded identity;
   - fresh-session / normal-entry verification;
   - durable evidence;
   - PASS or truthful blocker.

Maintainer must not hold the five-consumer aggregate completion truth.

No cross-machine authority is created by this board contract.

## 16. Per-consumer evidence and completion mutation

Each required consumer needs, at minimum:

- actual target identity;
- approved adaptation/update action;
- installed/loaded identity;
- normal-entry consumption;
- fresh-session/restart boundary when applicable;
- risk-matched should-not-change / failure safety;
- durable evidence locator.

A repo pull, file existence, source-SKILL read, install-helper PASS, synthetic fixture PASS, or unverified success summary is not enough.

### If Maintainer can mutate the Project

It may update the current consumer evidence/checklist and the Issue summary.

If other consumers remain pending, lifecycle Status stays ADAPTING.

### If Maintainer cannot mutate the Project

It emits an exact completion mutation:

```text
待同步到 Project：
- tracking Issue: #123
- consumer: Longleaf_Codex
- exact current consumer identity: <locator>
- consumer result: PASS | N/A
- adaptation evidence: <locator>
- normal-entry evidence: <locator>
- current lifecycle truth: ADAPTING
- next action: <next consumer or closure check>
```

Before applying it, the next Project-capable maintenance action must verify:

1. the mutation still belongs to the current tracking Issue;
2. the resolved consumer identity still matches the frozen contract;
3. the evidence is not stale;
4. the lifecycle truth has not changed incompatibly.

Then it may mechanically apply the update.

Do not make the user the five-consumer aggregator.

## 17. Final DONE aggregation

The tracking Issue / Project lifecycle is the only top-level aggregate owner.

Detailed ADAPTING evidence contains:

```text
Required consumers:
- Longleaf_Codex: PENDING | PASS | N/A(frozen reason)
- Longleaf_Backup_Codex: PENDING | PASS | N/A(frozen reason)
- CUHK_Workstation_WSL_Codex: PENDING | PASS | N/A(frozen reason)
- Workstation: PENDING | PASS | N/A(frozen reason)
- Legion: PENDING | PASS | N/A(frozen reason)
```

Each PASS/N/A line must have the exact resolved consumer identity and durable evidence locator.

One consumer PASS must never close the top-level Issue.

For a machine-consumed workflow, final DONE requires:

```text
all five required consumers PASS/N/A under the frozen contract
+ durable evidence complete
+ Resolution commit recorded
+ tracking Issue completed close
-> issue-closed workflow
-> DONE
```

Future optional consumers create follow-up work rather than retroactively expanding old DONE, unless new evidence proves the old completion claim was false.

## 18. This board task's own central and downstream phases

This maintenance-board capability is itself a shared maintenance mechanism consumed by GPT/Codex environments.

Therefore its own overall Goal is two-stage.

### Central implementation stage

Central implementation includes:

- canonical board policy created;
- AGENTS + Planner/Critic contract locators implemented;
- TODO / plugin TODO ownership docs updated;
- GitHub Project configured;
- full-inbox bootstrap complete;
- actual Project surface passes qualitative review;
- independent implementation review PASS;
- reviewed repo changes integrated to main;
- ChatGPT Project instructions one-time trigger/locator installed after main integration.

Once all central conditions are true:

```text
CENTRAL_IMPLEMENTATION_COMPLETE = YES
PROJECT_STATUS = ADAPTING
```

### Machine adaptation stage

The five required logical consumers must then be resolved and adapted per §§14–17.

This initial v0.3 Kickoff does **not** authorize remote/local machine mutation because exact current consumer identities, environment authority, and future production-ready Maintainer capability are not yet established.

At ADAPTING cutover, produce exact per-consumer Maintainer handoff(s) for separate current-user authorization under the same overall tracking Issue.

This is not a manual Kanban burden: the board remains ADAPTING automatically and the handoff contains exact pending consumer work.

Overall Goal remains open until five-consumer aggregate DONE.

## 19. Allowed repository changes in central implementation

Only:

- `AGENTS.md`
- `TODO.md`
- `docs/plugin-todos/README.md`
- new `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `README.md` only if the closure check proves a public-facing update is needed
- `results/repo--maintenance-board-lifecycle/**`
- ordinary task-control/evidence files required by existing Reviewed Handoff contracts

Do not modify:

- `skills/`;
- `scripts/codex_marketplace_config.json`;
- generated Marketplace/plugin payload;
- profile exposure;
- AI Skills Maintainer source;
- machine-update-orchestrator source;
- Bridge Kit;
- server/local machine/Host state.

Existing `ai-skills-repository-maintainer` remains an owner by architecture, but this board task does not modify its production source. A future production change adding a board locator to that skill must use the normal plugin refinement/version/gate process.

## 20. No new Kanban/control-plane product

Do not create:

- standalone Kanban skill;
- `kanban-sync` skill;
- new plugin/profile;
- board-specific MCP/service;
- cross-machine controller;
- machine registry/inventory service;
- watcher;
- background daemon;
- central credential broker;
- new cross-machine state machine;
- GitHub Action;
- database/ledger/controller.

Current owner surfaces are sufficient:

- canonical board doc;
- ChatGPT Project instructions;
- AI_Skills AGENTS;
- Planner/Critic role contracts;
- existing ai-skills-repository-maintainer as central-maintenance owner;
- future per-consumer machine-update-orchestrator.

## 21. Version / release decision

This task changes maintenance docs/contracts and GitHub Project metadata but not production plugin source/runtime/install payload.

```text
Repository bump decision: NONE
Reason: no formal installable repository/plugin release is created by this task.

Affected plugins:
- all central plugins: NO_BUMP
  Reason: no plugin production behavior/source/package is modified.
```

No Plugin Capability Gate Matrix is required for the board task itself because it does not change formal plugin production behavior.

If execution scope expands into `skills/`, Marketplace payload, plugin runtime, or machine-update production source, stop and return Planner/Critic for a separate production-plugin decision.

## 22. README closure

README closure is mandatory.

The Project is private and the canonical board policy is maintainer-facing.

Expected result:

```text
README checked: no update required
```

unless execution creates a real public user entry that should be documented.

Do not add a private/dead Project link to public README merely for symmetry.

## 23. Central-stage verification gates

All gates target the same final central candidate.

### B1 — Project structure

Directly verify:

- exact owner/title/visibility/repo link;
- exact four Status options;
- Area + Resolution commit fields;
- Board / Active / By area / History.

### B2 — BOARD-01

Directly verify actual Project workflow/config:

- exact issue-only auto-add filter;
- PR merged -> Done disabled;
- issue closed -> Done enabled for final closure;
- item added -> TODO if used;
- no PR lifecycle items;
- live tracking Issue uses only non-closing references.

### B3 — full-inbox completeness

Verify:

- every current canonical inbox was scanned;
- every current meaningful entry has a disposition in `TODO_COVERAGE.md`;
- valid central raw NEW is visible as tracking TODO or merged into an existing tracking Issue;
- maturity is not silently promoted;
- duplicate/project-local/rejected/history items are explicitly dispositioned rather than silently omitted.

### B4 — normal entry / idempotency

Use this board task's own real tracking Issue:

- admitted exactly once;
- Area=repo;
- Status=DOING during central work;
- supported CLI/API can list/update it;
- reconciliation rerun does not create duplicate Project/Issue;
- reader-facing copy passed Clear Writing.

### B5 — human-facing surface

Independent Reviewer inspects actual:

- Board;
- By area;
- this task Issue;
- every Issue title/top summary created or materially rewritten in bootstrap.

Reviewer must determine whether a user can understand:

- what the item is;
- which Area/plugin owns it;
- current lifecycle state;
- current execution anchor;
- next action;

without deciphering task keys/hashes/paths.

Field presence, keyword scans, API receipts, character counts, or Clear Writing invocation alone cannot PASS this gate.

### B6 — consumer-locator contracts

Verify the repo diff contains one canonical policy and only short consumer locators/rules in:

- AGENTS;
- Planner Role Contract;
- Critic Role Contract;
- TODO/plugin TODO docs.

Verify no duplicate full policy was copied.

Verify no-tool pending mutation and central-complete -> ADAPTING cutover semantics are present.

### B7 — independent implementation review

Reviewer must inspect actual Project configuration, actual surface, full-inbox coverage evidence, repo diff, and role-consumer behavior.

Executor summary alone is insufficient.

## 24. Central integration / ChatGPT Project-instructions setup

After B1–B7 PASS:

1. fetch latest main;
2. if semantic overlap changes the approved board contract or role contracts, return Planner/Critic;
3. integrate reviewed task branch with ordinary non-force Git;
4. verify remote main;
5. perform README closure check;
6. apply the exact ChatGPT Project-instructions trigger/locator from §11, using a supported surface or one HUMAN_ONLY exact-text action;
7. record truthful evidence that the one-time setup was completed;
8. update this task's tracking Issue current progress and anchor.

At this point, if all central conditions are satisfied:

```text
CENTRAL_IMPLEMENTATION_COMPLETE = YES
PROJECT_STATUS = ADAPTING
```

Do **not** set Resolution commit or close the top-level Issue yet; machine-consumer adaptation is still pending.

## 25. Downstream adaptation / final closure

At ADAPTING cutover:

1. resolve and freeze exact current identities/locators for the five required logical consumers;
2. generate exact per-consumer Maintainer handoff(s);
3. obtain any newly required current-user machine/credential/remote authority before mutation;
4. run the future production-ready Maintainer per consumer, or a separately approved existing route;
5. collect and apply each completion mutation;
6. keep Status ADAPTING while any required consumer is pending.

Only after all five are complete:

1. independent closure check confirms all five PASS/N/A and evidence is current;
2. create or identify the canonical owner-repo Resolution commit that durably records complete closure evidence;
3. write Resolution commit to Project + Issue;
4. close the tracking Issue as completed;
5. verify issue-closed workflow sets Status DONE;
6. verify History shows Resolution commit.

Overall Goal is achieved only then.

## 26. Failure recovery

### Missing GitHub `project` scope

Stop before Project mutation. Request one bounded auth refresh and resume the same central Goal.

### Exact worktree unavailable

Stop before Project/Issue mutation. Do not switch branch/path.

### Clear Writing unavailable

Stop before new/materially rewritten reader-facing board copy mutation. Report `CLEAR_WRITING_UNAVAILABLE`; do not silently create unreadable cards.

### GitHub workflow UI-only

Leave the Project private and safe; do not backfill until real workflow state is configured/read back. Request one minimal HUMAN_ONLY GitHub action only if no supported browser/API path exists.

### ChatGPT Project instructions user-only

After main integration, request the one exact-text Project-settings setup if no supported mutation surface exists. Resume the same Goal after confirmation. Do not repeat it later.

### Backfill ambiguity

Skip ambiguous merge decisions, record the source pair and reason, and route to Planner. Do not invent genericity.

### Main drift

Unrelated drift may be integrated normally. Semantic overlap with approved board/role contract returns Planner/Critic.

### Pending consumer mutation stale

Do not apply. Re-read tracking Issue, exact frozen consumer identity, and evidence. Produce a corrected mutation.

### Maintainer unavailable/not production-ready

Keep the top-level item ADAPTING. Do not substitute an unapproved machine-update implementation and do not claim DONE.

### Consumer needs new machine/credential authority

Request only the exact new bounded authorization at ADAPTING time. Do not expand to cross-machine controller authority.

## 27. Explicit non-goals

No:

- execution of v0.2 package;
- production plugin source change;
- Maintainer machine-update implementation;
- Bridge Kit modification;
- server/local-machine mutation under the initial central Kickoff;
- paid API;
- Project publication;
- force push/history rewrite;
- repository-wide auto-close disable;
- raw-NEW maturity promotion by virtue of Project admission;
- standalone board skill/plugin;
- cross-machine controller/registry/daemon/state machine;
- recurring manual user Kanban maintenance.

## 28. User-visible capability after full closure

After full DONE, the user can open one Project and see:

- the current maintenance backlog, including valid raw NEW items;
- what is TODO, actively DOING, centrally complete but still ADAPTING, and truly DONE;
- the current execution anchor and next step for active work;
- readable Issue/card copy rather than internal workflow garbage;
- Resolution commit for every DONE item;
- truthful five-consumer rollout state for machine-consumed workflows;
- Planner/Critic/GPT-driven lifecycle maintenance without manual card dragging.

Central implementation PASS alone does not claim this full five-consumer closure.
