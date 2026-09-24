# AI Skills 维护看板 — Implementation Plan v0.5

- Date: 2026-09-24
- Human label: AI Skills 维护看板与完成语义
- Task key: `repo--maintenance-board-lifecycle`
- Repository: `YuukiAS/AI_Skills_Collection`
- Package version: `v0.5`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- Approved design commit: `d14565e152b9b953c76c0722ad6e6343850335a7`
- Design Critic PASS: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_CRITIC_REVIEW_2026-09-24.md`
- Design Critic review commit: `012a43c7edefddd7f071d43425f7be937453f73a`
- Previous execution review: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_4_2026-09-24.md`
- Previous execution review commit: `f8203829641588322215fba585a5fd6844240853`
- Stable blocker addressed: `BOARD-LOCATOR-SCOPE-01`
- Supersedes for execution: v0.4 Plan / Goal / Kickoff
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Execution branch: `reviewed/repo--maintenance-board-lifecycle`
- Exact task worktree: `../AI_Skills_Collection-repo--maintenance-board-lifecycle`
- This Plan does not itself authorize execution.

## 1. Planner disposition

```text
BOARD-LOCATOR-SCOPE-01 = ACCEPT
```

v0.4 的 locator architecture 保持不变。本版只修复一个 authorization-envelope 漏洞：

> locator-only write scope 必须来自 **task mutation 之前** 的 kickoff-base root `TODO.md`，不能由本 task 后续修改 root `TODO.md` 自己扩大。

不新增 registry、watcher、allowlist service 或长期控制面。

## 2. Product target

Create one human-readable, low-maintenance GitHub Project for the full AI_Skills maintenance backlog and make it part of the normal Planner / Critic / Codex maintenance path.

Lifecycle remains exactly:

```text
TODO -> DOING -> ADAPTING -> DONE
```

- Project item = one top-level tracking Issue.
- Plugin / standalone-skill TODO = failure, evidence, maturity inbox.
- Planner–Critic / Reviewed Handoff / Executor work = execution evidence.
- WAITING/BLOCKED are not fifth lifecycle states.
- DONE requires Resolution commit.
- `Project lifecycle status != plugin TODO maturity status`.

A raw `NEW` may be visible as Project `TODO` while remaining `NEW` in the canonical source inbox.

## 3. Exact execution identity

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = kickoff-time latest origin/main
```

No alternate branch, worktree, `/tmp` fallback, dirty-checkout substitution, task-key substitution, force push, or history rewrite is authorized.

## 4. Kickoff-base inbox allowlist freeze — BOARD-LOCATOR-SCOPE-01

### 4.1 Freeze source before any task content mutation

At kickoff preflight:

1. fetch `origin/main`;
2. record the exact commit SHA as `KICKOFF_BASE_COMMIT`;
3. read root `TODO.md` **at that exact commit SHA**, not from any task-mutated worktree copy;
4. parse the exact canonical maintenance inbox paths formally declared by that unmodified root TODO;
5. verify each parsed path exists at the same `KICKOFF_BASE_COMMIT`;
6. freeze the resulting exact path set in memory;
7. create the exact reviewed branch/worktree from the same base commit;
8. make the first task-content evidence write:
   `results/repo--maintenance-board-lifecycle/FROZEN_CANONICAL_INBOX_ALLOWLIST.md`;
9. do not perform any other task tracked-file mutation, Project/Issue creation, or backfill before this frozen allowlist evidence exists.

Branch/worktree creation itself is bootstrap identity setup; it must not change repository content.

### 4.2 What counts as a canonical inbox declaration

Parse only the structured root-TODO navigation entries that formally declare maintenance inboxes, currently the plugin TODO and standalone-skill TODO entry tables.

Do not treat incidental links in explanatory prose, examples, changelog links, workflow docs, or arbitrary Markdown links as inbox declarations.

If the kickoff-base root TODO format is ambiguous enough that the canonical inbox set cannot be determined without guessing, fail closed before locator writes and return Planner.

### 4.3 Durable freeze evidence

`FROZEN_CANONICAL_INBOX_ALLOWLIST.md` must record at least:

```text
KICKOFF_BASE_COMMIT = <exact SHA>
ROOT_TODO_BLOB_SHA = <exact blob SHA>
FROZEN_INBOX_COUNT = <N>

FROZEN_CANONICAL_INBOX_PATHS =
- <exact path 1>
- <exact path 2>
...
```

It may also record the parsing rule / root-TODO section names used.

This file is task evidence only. It is not a long-term registry, runtime source, or service.

GitHub officially supports reading repository content by an exact commit/ref; the execution must use the frozen commit identity rather than a moving task branch when deriving this allowlist.

## 5. Frozen allowlist is the only locator-write authority

For this task, locator-only write authority applies **only** to the exact paths listed in:

`results/repo--maintenance-board-lifecycle/FROZEN_CANONICAL_INBOX_ALLOWLIST.md`

No later file may enter locator-write scope merely because the task changes documentation.

Specifically:

- later task edits to root `TODO.md` do not change the frozen allowlist;
- if the task branch adds a new inbox navigation entry, that path does **not** gain locator-write authority in this task;
- if the task branch removes or renames an inbox declaration, the already frozen authority does not silently retarget to another path;
- no code may recompute the allowlist from task-mutated `TODO.md` and use the new result as authority.

Root `TODO.md` may still receive the already-approved documentation update explaining inbox vs Project ownership, but that documentation edit is not an authorization source.

## 6. Post-kickoff upstream main drift

If `origin/main` advances after `KICKOFF_BASE_COMMIT` and a newer upstream root `TODO.md` declares a new canonical maintenance inbox:

- it does **not** automatically enter this task's locator-write allowlist;
- it is not silently added to this task's full-inbox bootstrap claim;
- if that new inbox must be included for this task to remain semantically correct, return Planner/user under the existing semantic-drift / scope-expansion contract;
- otherwise leave it for later maintenance work and record the post-kickoff difference in closure evidence.

Do not create a watcher or repeatedly poll root TODO for new inboxes.

## 7. Project identity, fields, views

Create or reconcile exactly one:

```text
owner = YuukiAS
title = AI Skills Maintenance
visibility = PRIVATE
linked repository = YuukiAS/AI_Skills_Collection
tracking label = maintenance-track
```

If zero exact-title Projects exist, create one. If exactly one compatible Project exists, reconcile it. If multiple or unrelated exact-title Projects exist, stop with ambiguity evidence.

Required fields:

### Status

```text
TODO
DOING
ADAPTING
DONE
```

No fifth lifecycle state.

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

One text field storing the canonical owner-repo closure/evidence commit for a DONE item.

Required views:

1. Board — grouped by Status; cards expose readable title + Area + Status.
2. Active — DOING/ADAPTING; title + Area + Status.
3. By area — directly group/filter by Area; title + Area + Status.
4. History — DONE; title + Area + Status + Resolution commit.

Do not add a Maturity field, Current workflow field, machine-registry field, WAITING/BLOCKED status, or another Project schema.

## 8. GitHub bootstrap route

Keep the previously reviewed GitHub-native route:

- supported `gh project` commands for project/item operations where available;
- documented Projects API/GraphQL where required;
- built-in Project workflow / auto-add configuration via supported GitHub Project UI when no supported mutation API exists;
- actual readback after setup;
- authenticated identity + `project` scope preflight.

Do not invent nonexistent `gh project` subcommands.

If a required built-in workflow setting is UI-only and the Executor has no supported browser surface, request one minimal HUMAN_ONLY GitHub action, then resume the same Goal after real readback. This is one-time bootstrap, not recurring maintenance.

## 9. BOARD-01 — false-DONE prevention

Before backfill, configure and verify:

### Admission

```text
is:issue label:maintenance-track
```

Implementation/design PRs are not lifecycle items.

### Workflows

- item added -> TODO: enabled if used;
- issue closed -> DONE: enabled for final closure;
- pull request merged -> DONE: disabled.

### Link discipline

Before true DONE:

- no Development/manual link that makes an intermediate PR merge auto-close the tracking Issue;
- no `close/closes/closed/fix/fixes/fixed/resolve/resolves/resolved` targeting the tracking Issue from PR body or commit message;
- only non-closing references;
- task/PR/commit/review locators stay in the Issue evidence/history.

Do not disable repository-wide linked-PR auto-close.

### Non-completion close

Rejected/superseded/duplicate/not-planned items must be removed/archived from this Project before truthful close and must not appear as DONE.

## 10. Human-readable Issue contract

Every tracking Issue title must be natural and concise.

Task keys, hashes, branches, paths, or internal status strings may be locators but must not be the title's main content.

Each tracking Issue starts with:

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

Detailed evidence/history follows below.

Every DOING/ADAPTING item has at least one current valid anchor.

History directly shows Resolution commit for DONE items.

## 11. Clear Writing hard requirement

Whenever Codex creates or materially rewrites reader-facing Project/Issue copy, it must actually invoke installed Clear Writing (`writing-style`) before the GitHub mutation.

Covered copy includes Issue titles, top summaries, backfill copy, card copy, and human-readable closure/history copy.

Clear Writing may improve wording but must not change:

- source maturity;
- lifecycle Status;
- Area;
- source-to-Issue tracking locator;
- required-consumer truth;
- exact proposal/task/branch/PR/commit locator;
- Resolution commit;
- evidence meaning or claim strength.

If unavailable, stop the reader-facing mutation and report:

```text
CLEAR_WRITING_UNAVAILABLE
```

Actual Project-surface qualitative review is authoritative.

## 12. Full-inbox bootstrap uses only the frozen allowlist

The bootstrap scans exactly the paths in the frozen kickoff-base allowlist.

For every current entry in those frozen inboxes that still has maintenance meaning, assign one disposition:

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

A valid central raw `NEW` may become Project TODO without changing source maturity.

Do not mechanically create one Issue per Markdown heading. Dedupe only where evidence clearly represents the same top-level idea.

If merging two entries requires substantive genericity judgment, do not guess merely to reduce card count.

The completeness claim is:

> complete for the frozen kickoff-base canonical inbox allowlist.

It is not a moving claim over inboxes introduced after kickoff.

## 13. Durable tracking locator — retained from v0.4

For every canonical source entry in the frozen allowlist whose disposition is:

- `TRACKED`, or
- `MERGED_INTO_TRACKING_ISSUE`,

the same maintenance action must write/update exactly one durable backlink:

```text
tracking: #<issue-number>
```

Rules:

- independent entry -> its own top-level Issue;
- duplicate/merged entries -> multiple source entries may point to the same top-level Issue;
- reused existing Issue -> write actual reused Issue number;
- rebind/merge -> update every affected source entry to the actual current Issue;
- raw NEW admitted to Project remains maturity `NEW`.

### Locator-only mutation boundary

Writing/updating `tracking: #N` must not change:

- source maturity/status;
- problem;
- evidence;
- project-specific context;
- target layer;
- candidate action;
- promotion gate;
- any other substantive TODO field;
- Project lifecycle Status.

Do not copy `TODO / DOING / ADAPTING / DONE` into Markdown.

Do not add a locator to non-tracked dispositions merely for completeness.

If an existing locator conflict is ambiguous, stop that entry and route to Planner; do not silently guess/rebind.

## 14. TODO_COVERAGE remains one-time evidence

Create:

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

For every relevant source entry in the frozen allowlist record:

```text
source inbox + heading
-> disposition
-> tracking Issue (if any)
-> Area
-> initial lifecycle Status (if tracked)
```

This proves bootstrap completeness only.

It must not become:

- long-term source-to-Issue registry;
- runtime lookup source;
- status source;
- replacement for `tracking: #N`.

Steady-state durable mapping is the canonical source entry's own tracking locator.

## 15. Allowed central repository modifications

Central implementation may modify:

- `AGENTS.md`;
- root `TODO.md`;
- `docs/plugin-todos/README.md`;
- new `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`;
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`;
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`;
- `README.md` only if closure check proves a real public-facing update is needed;
- `results/repo--maintenance-board-lifecycle/**`;
- ordinary task-control/evidence files required by existing Reviewed Handoff rules;
- **only the exact canonical inbox paths frozen in `FROZEN_CANONICAL_INBOX_ALLOWLIST.md`**, and only for `tracking: #N` locator maintenance.

No task-mutated `TODO.md` can expand that last bullet.

Forbidden:

- substantive TODO-field edits under locator-only authority;
- any canonical inbox path not in the frozen allowlist;
- `skills/` production source;
- generated Marketplace/plugin payload;
- profile exposure;
- ai-skills-repository-maintainer production source;
- machine-update-orchestrator source;
- Bridge Kit;
- server/local-machine/Host state;
- paid API;
- force/destructive Git.

## 16. One canonical policy and short consumer locators

Create one full canonical policy:

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

Other surfaces contain short trigger/locator/consumer rules only.

### AGENTS

Require AI_Skills TODO / Planner / Critic / adaptation / closure work to consume the canonical board doc, reconcile without user reminders, and use Clear Writing for reader-facing board copy.

### Planner Role Contract

For formal AI_Skills maintenance:

- triage into tracking scope -> create/bind/reuse tracking Issue or exact pending mutation;
- same maintenance action -> write/update source `tracking: #N` when the source path is a canonical inbox under the applicable maintenance authority;
- first substantive Plan/design -> DOING + current anchor;
- handoff -> next action/evidence;
- central implementation complete + required consumers pending -> ADAPTING + freeze exact consumer locators;
- no Project mutation surface -> exact pending mutation;
- no manual user Kanban/source-locator sync.

### Critic Role Contract

For formal AI_Skills maintenance review:

- review locator + next action + lifecycle truth;
- PASS/REVISE alone does not mechanically change Status;
- implementation Reviewer PASS may lead to ADAPTING only after required canonical central closure holds;
- no Project mutation surface -> exact pending mutation;
- Critic does not edit Planner Proposal, advance Reviewed Handoff CURRENT, or impersonate Executor.

### TODO / plugin-todos README

Clarify inbox vs dashboard ownership, raw NEW Project visibility, and `tracking: #N` as the only durable source backlink; Project Status is not copied into Markdown.

## 17. ChatGPT Project-instructions one-time setup

After the canonical board doc is integrated to `main`, add this exact short trigger/locator once to AI Research Stack Project instructions:

```text
AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步，并在 canonical source entry 回写/更新 tracking: #N。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。
```

If the execution surface cannot modify Project instructions, request one HUMAN_ONLY exact-text Project-settings action after main integration and resume the same Goal after truthful confirmation.

Do not ask again during routine sync.

## 18. No-tool pending mutation

A GPT/Planner/Critic surface without Project mutation capability remains semantic owner.

It must:

1. update any Issue/source evidence it can legitimately update;
2. preserve/update the canonical source `tracking: #N` if it has repo write access and the binding is known;
3. emit an exact pending Project mutation;
4. not claim the Project has already been synchronized;
5. not ask the user to drag cards or manually add source locators.

The next Project-capable maintenance action verifies freshness before applying.

## 19. Two-level completion truth

Central implementation complete:

```text
execution-ready Critic PASS
-> Codex implementation
-> independent implementation review PASS
-> canonical owner integration/release closure when required by frozen Goal
= central implementation complete
```

Execution-ready PASS alone remains DOING.

Executor self-report alone remains DOING.

Reviewer PASS without required canonical closure remains DOING.

For a machine-consumed workflow/shared maintenance mechanism:

```text
central implementation complete
-> ADAPTING
```

Non-machine-consumed work follows its own frozen completion contract.

## 20. Required logical consumers

For machine-consumed workflow/shared maintenance mechanisms, current default required logical consumers remain:

### Server / remote Codex

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

### Local

4. `Workstation`
5. `Legion`

When an item enters ADAPTING, resolve and freeze exact current identities/locators under per-consumer authority.

If resolving exact identity itself requires machine access, first obtain that consumer's bounded authority; do not guess locators.

Do not hard-code hostname, SSH alias, CODEX_HOME, account, checkout, credential, or private path in the long-lived policy.

Future optional consumers do not retroactively enlarge a frozen contract.

N/A requires a durable frozen reason.

## 21. AI Skills Maintainer scope

AI Skills Maintainer remains a **per-current-consumer adaptation executor**.

It is not:

- cross-machine controller;
- five-machine orchestrator;
- machine registry owner;
- credential broker.

When the independent machine-update capability becomes production-ready, each consumer is adapted from that consumer's current Codex environment or through a separately approved existing remote route preserving the same per-consumer boundary.

For the current consumer only, Maintainer handles:

- discovery;
- adaptation/update;
- installed/loaded identity;
- fresh-session / normal-entry verification;
- durable evidence;
- current-consumer PASS / truthful blocker.

Five-consumer aggregate truth belongs to the tracking Issue / Project.

## 22. Per-consumer completion mutation and final DONE

If current Maintainer can mutate Project, it may update that consumer evidence/checklist.

If any required consumer remains pending, Status remains ADAPTING.

If Maintainer cannot mutate Project, it emits an exact completion mutation containing at least:

- tracking Issue;
- consumer;
- exact current consumer identity;
- PASS/N/A;
- adaptation evidence;
- normal-entry evidence;
- current lifecycle truth;
- next action.

The next Project-capable action verifies tracking Issue identity, frozen consumer identity, evidence freshness, and lifecycle compatibility before applying.

A single consumer PASS never closes the top-level Issue.

Final machine-consumed DONE requires:

```text
all required consumers PASS/N/A
+ durable evidence complete
+ Resolution commit
+ tracking Issue completed close
+ issue-closed workflow -> DONE
```

## 23. This board task's stages

This board is itself a machine-consumed shared maintenance mechanism.

### Central stage

Central implementation is complete only after:

- canonical board policy exists;
- AGENTS + Planner/Critic short consumer rules exist;
- TODO ownership docs exist;
- frozen kickoff-base inbox allowlist evidence exists and is verified;
- every TRACKED/MERGED source entry within that frozen allowlist has the correct `tracking: #N`;
- private Project is configured;
- full-inbox bootstrap for the frozen allowlist is complete;
- actual Project surface passes qualitative review;
- independent implementation review passes;
- reviewed repository changes are integrated to main;
- one-time ChatGPT Project-instructions trigger is installed.

Then:

```text
CENTRAL_IMPLEMENTATION_COMPLETE = YES
FROZEN_INBOX_ALLOWLIST_VERIFIED = YES
SOURCE_TRACKING_LOCATORS_VERIFIED = YES
PROJECT_STATUS = ADAPTING
OVERALL_GOAL_ACHIEVED = NO
```

### Downstream stage

Resolve/freeze the five exact consumers and adapt each later under per-consumer authority.

The initial v0.5 central Kickoff does not authorize machine mutation.

## 24. Bounded external GitHub effects

The future approved central Kickoff may:

- inspect/create/reconcile the one private Project;
- link only `YuukiAS/AI_Skills_Collection`;
- configure approved fields/views/workflows;
- create/reuse `maintenance-track`;
- create/reuse/update tracking Issues required by full-inbox coverage;
- add/update eligible Issues in the Project;
- create/update this board task's tracking Issue;
- write non-closing task/PR/commit/review/evidence locators;
- perform bootstrap over the frozen kickoff-base inbox allowlist;
- write/update `tracking: #N` only in the frozen allowlist paths.

It may not close unrelated backfilled Issues, mark this top-level task DONE, mutate server/local consumers, publish the Project, disable repository-wide auto-close, or expand the locator-write path set.

## 25. One-time UI gates

If no supported automation surface exists:

- GitHub Project workflow setup may require one minimal HUMAN_ONLY action before backfill, followed by real readback.
- ChatGPT Project instructions may require one minimal HUMAN_ONLY exact-text action after main integration.

Neither is recurring routine maintenance.

## 26. Verification gates

### B1 — Frozen allowlist provenance

Verify:

- `KICKOFF_BASE_COMMIT` equals the unmodified kickoff-time `origin/main` base used for the reviewed task branch;
- `ROOT_TODO_BLOB_SHA` matches `TODO.md` at that base;
- the reported frozen inbox path set exactly equals the canonical maintenance inbox set formally declared by that unmodified root TODO;
- every frozen path existed at that base;
- no other tracked-file or Project/Issue mutation occurred before the allowlist evidence was written, apart from exact branch/worktree bootstrap identity setup.

### B2 — Project structure / BOARD-01

Verify actual Project identity, fields, views, issue-only auto-add, workflow state, PR-merged -> Done disabled, and non-closing link discipline.

### B3 — Full coverage + locator integrity

Verify:

- every meaningful entry in the frozen allowlist has a bootstrap disposition;
- every TRACKED entry has correct `tracking: #N`;
- every MERGED entry has correct shared locator;
- reused Issue number is correctly written back;
- non-tracked entry is not forced to get locator;
- raw NEW maturity unchanged;
- locator-only edits did not change substantive TODO content;
- Project Status not copied into Markdown;
- `TODO_COVERAGE.md` is not used as long-term mapping.

### B4 — Scope non-expansion

Verify directly:

- every locator edit path is in `FROZEN_CANONICAL_INBOX_ALLOWLIST.md`;
- no locator edit occurred outside that frozen path set;
- task-mutated root `TODO.md` did not change the frozen authority;
- no post-kickoff upstream inbox was silently added to the allowed set;
- if post-kickoff main added an inbox, closure evidence states whether it was deferred or triggered Planner/scope review.

### B5 — Normal entry / idempotency

Verify no duplicate Project/Issue/item and correct source-backlink behavior on create/bind/reuse/merge.

### B6 — Human-facing surface

Independent Reviewer inspects actual Board, By area, this task Issue, and new/materially rewritten Issue top summaries. No field/string/API receipt proxy PASS.

### B7 — Consumer locator contract

Verify one canonical policy, short AGENTS/Planner/Critic locators, proactive sync, same-action source backlink update, no-tool pending mutation, and no manual user source-locator sync.

### B8 — Independent central implementation review

Reviewer inspects actual Project/config, repo diff, frozen allowlist evidence, TODO_COVERAGE, source backlinks, BOARD-01, Clear Writing result, scope non-expansion, and consumer behavior.

Executor summary alone cannot PASS.

### B9 — Central integration / ChatGPT trigger

After B8 PASS, integrate approved changes to main with ordinary non-force Git, verify remote main, perform README closure, install the one-time ChatGPT Project trigger, record setup evidence, and reconcile this task to ADAPTING.

### B10 — Final five-consumer closure

Later, outside the initial central Kickoff.

## 27. Failure recovery

- missing `project` scope -> bounded auth refresh before Project mutation;
- exact worktree unavailable -> stop;
- kickoff-base root TODO canonical inbox parsing ambiguous -> stop before locator writes/backfill;
- Clear Writing unavailable -> stop reader-facing mutation;
- GitHub workflow UI-only -> one minimal HUMAN_ONLY setup + readback;
- ChatGPT Project settings user-only -> one exact-text setup after main integration;
- ambiguous TODO dedupe -> do not guess;
- ambiguous/stale source tracking locator -> do not guess/rebind;
- post-kickoff upstream new inbox required for this task -> return Planner/user for scope decision;
- semantic main drift -> Planner/Critic;
- stale pending mutation -> regenerate;
- Maintainer not production-ready -> stay ADAPTING;
- exact consumer identity needs machine access -> obtain per-consumer authority first;
- one consumer PASS -> never aggregate-DONE.

## 28. No new board/control-plane component

Do not create:

- standalone board/Kanban skill;
- `kanban-sync` skill;
- new plugin/profile;
- board-specific MCP/service;
- cross-machine controller;
- machine registry/inventory service;
- watcher/daemon;
- allowlist service;
- central credential broker;
- GitHub Action/database/ledger/controller;
- new cross-machine state machine.

## 29. Version / README

```text
Repository bump decision: NONE
Reason: maintenance docs/contracts, canonical TODO tracking metadata, frozen task evidence, and GitHub Project metadata only.

Affected plugins:
- all: NO_BUMP
  Reason: no plugin production source/runtime/package change.
```

README closure is mandatory.

Expected:

```text
README checked: no update required
```

unless implementation creates a real public entry.

## 30. Completion statement

Central stage may report only:

```text
CENTRAL_IMPLEMENTATION_COMPLETE = YES
FROZEN_INBOX_ALLOWLIST_VERIFIED = YES
SOURCE_TRACKING_LOCATORS_VERIFIED = YES
PROJECT_STATUS = ADAPTING
OVERALL_GOAL_ACHIEVED = NO
```

Only final five-consumer closure may report:

```text
FIVE_CONSUMER_AGGREGATE_VERIFIED = YES
RESOLUTION_COMMIT = <canonical closure commit>
TRACKING_ISSUE_CLOSED_COMPLETED = YES
PROJECT_STATUS = DONE
OVERALL_GOAL_ACHIEVED = YES
```

No earlier milestone may claim overall completion.
