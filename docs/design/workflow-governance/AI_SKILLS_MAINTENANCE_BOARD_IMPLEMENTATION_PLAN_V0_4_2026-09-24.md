# AI Skills 维护看板 — Implementation Plan v0.4

- Date: 2026-09-24
- Human label: AI Skills 维护看板与完成语义
- Task key: `repo--maintenance-board-lifecycle`
- Repository: `YuukiAS/AI_Skills_Collection`
- Package version: `v0.4`
- Approved design: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md`
- Approved design commit: `d14565e152b9b953c76c0722ad6e6343850335a7`
- Design Critic PASS: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_CRITIC_REVIEW_2026-09-24.md`
- Design Critic review commit: `012a43c7edefddd7f071d43425f7be937453f73a`
- Previous execution review: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-24.md`
- Previous execution review commit: `98b7b875eabedb773f0d1d5bcdcd23217cc9b055`
- Stable blocker addressed: `BOARD-TRACKING-LOCATOR-01`
- Supersedes for execution: v0.3 Plan / Goal / Kickoff
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Execution branch: `reviewed/repo--maintenance-board-lifecycle`
- Exact task worktree: `../AI_Skills_Collection-repo--maintenance-board-lifecycle`
- This Plan does not itself authorize execution.

## 1. Planner disposition

```text
BOARD-TRACKING-LOCATOR-01 = ACCEPT
```

v0.3 的 execution architecture 保持不变。本版只补齐 approved architecture 已经要求、但 v0.3 allowed-file scope 漏掉的 durable source backlink：

```text
canonical TODO entry
<-> tracking: #<issue-number>
<-> top-level tracking Issue / Project item
```

`TODO_COVERAGE.md` 仍然只是一轮 bootstrap completeness evidence，不承担长期 mapping registry。

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

Before any Project/Issue mutation:

1. resolve the relative worktree locator from the canonical repo root to one absolute sibling path;
2. record it in `results/repo--maintenance-board-lifecycle/RESULT.md`;
3. create only the exact reviewed branch/worktree after the user sends the Critic-approved Kickoff.

If the Host/sandbox cannot legally create this exact worktree, stop before Project/Issue mutation. Do not substitute `/tmp`, a dirty canonical checkout, another branch, or another path.

A sanctioned existing bounded worktree primitive may execute the same exact locator if already available; this Plan does not authorize Bridge Kit changes.

## 4. Project identity, fields, views

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

## 5. GitHub bootstrap route

Keep the previously reviewed GitHub-native route:

- supported `gh project` commands for project/item operations where available;
- documented Projects API/GraphQL where required;
- built-in Project workflow / auto-add configuration via the supported GitHub Project UI when no supported mutation API exists;
- actual readback after setup;
- authenticated identity + `project` scope preflight.

Do not invent nonexistent `gh project` subcommands.

If a required built-in workflow setting is UI-only and the Executor has no supported browser surface, request one minimal HUMAN_ONLY GitHub action, then resume the same Goal after real readback. This is one-time bootstrap, not recurring maintenance.

## 6. BOARD-01 — false-DONE prevention

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

## 7. Human-readable Issue contract

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

## 8. Clear Writing hard requirement

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

## 9. Full-inbox bootstrap

Scan every current canonical maintenance inbox formally declared by kickoff-time root `TODO.md`, including:

- current central `docs/plugin-todos/*.md` inboxes listed there;
- current standalone `docs/skill-todos/*.md` inboxes listed there;
- any other canonical maintenance inbox explicitly declared there at execution time.

For every current entry with maintenance meaning, assign one disposition:

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

A valid central raw `NEW` may become Project TODO without changing source maturity.

Do not mechanically create one Issue per Markdown heading. Dedupe only where the evidence clearly represents the same top-level idea.

If merging two entries requires substantive genericity judgment, do not guess merely to reduce card count.

## 10. Durable tracking locator — BOARD-TRACKING-LOCATOR-01

### 10.1 Canonical source backlink

For every canonical source entry whose bootstrap disposition is:

- `TRACKED`, or
- `MERGED_INTO_TRACKING_ISSUE`,

the same maintenance action must write or update exactly one durable backlink in that source entry:

```text
tracking: #<issue-number>
```

Rules:

- independent entry -> its own top-level tracking Issue;
- duplicate/merged source entries -> multiple source entries may point to the same top-level Issue;
- reused existing Issue -> write the actual reused Issue number;
- rebind/merge to a different current Issue -> update the source entry to the actual current Issue;
- raw NEW admitted to Project remains maturity `NEW`.

### 10.2 Locator-only mutation boundary

For the purpose of this bootstrap/steady-state binding, canonical inbox edits are **locator-only**.

Writing/updating `tracking: #N` must not change:

- `status` / source maturity;
- problem;
- evidence;
- project-specific context;
- target layer;
- candidate action;
- promotion gate;
- any other source substantive field;
- Project lifecycle Status.

Do not copy `TODO / DOING / ADAPTING / DONE` into Markdown.

Do not promote `NEW` merely because a Project item exists.

Do not add a tracking locator to a non-tracked disposition merely for completeness.

If the existing source entry already contains a different tracking locator and the correct current mapping is not unambiguous, stop that entry and route the conflict to Planner; do not silently guess/rebind.

### 10.3 Steady-state contract

The canonical board doc must state:

```text
create / bind / reuse tracking Issue
-> in the same maintenance action write or update source tracking: #N

Issue merge / rebind
-> update every affected canonical source entry to the actual current Issue
```

This backlink maintenance is routine board sync. It must not require the user to manually edit TODO files.

## 11. TODO_COVERAGE remains one-time evidence

Create:

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

For every relevant source entry record:

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
- replacement for `tracking: #N` in canonical TODO entries.

Steady-state durable mapping is the canonical source entry's own tracking locator.

## 12. Allowed central repository modifications

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
- **canonical maintenance inbox files formally listed by kickoff-time root `TODO.md`**, but only for `tracking: #N` locator maintenance:
  - listed `docs/plugin-todos/*.md`;
  - listed `docs/skill-todos/*.md`;
  - any future canonical inbox explicitly listed by root `TODO.md` at execution time, same locator-only boundary.

This does **not** authorize arbitrary edits to every file matching those directory globs. The authority applies only to root-TODO-declared canonical inbox entries and only to their tracking locator.

Forbidden:

- `skills/` production source;
- generated Marketplace/plugin payload;
- profile exposure;
- ai-skills-repository-maintainer production source;
- machine-update-orchestrator source;
- Bridge Kit;
- server/local-machine/Host state;
- paid API;
- force/destructive Git.

## 13. One canonical policy and short consumer locators

Create one full canonical policy:

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

Other surfaces contain short trigger/locator/consumer rules only.

### AGENTS

Require AI_Skills TODO / Planner / Critic / adaptation / closure work to consume the canonical board doc, reconcile without user reminders, and use Clear Writing for reader-facing board copy.

### Planner Role Contract

For formal AI_Skills maintenance:

- triage into tracking scope -> create/bind/reuse tracking Issue or exact pending mutation;
- in the same maintenance action write/update source `tracking: #N`;
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

## 14. ChatGPT Project-instructions one-time setup

After the canonical board doc is integrated to `main`, add this exact short trigger/locator once to AI Research Stack Project instructions:

```text
AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步，并在 canonical source entry 回写/更新 tracking: #N。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。
```

If the execution surface cannot modify Project instructions, request one HUMAN_ONLY exact-text Project-settings action after main integration and resume the same Goal after truthful confirmation.

Do not ask again during routine sync.

## 15. No-tool pending mutation

A GPT/Planner/Critic surface without Project mutation capability remains semantic owner.

It must:

1. update any Issue/source evidence it can legitimately update;
2. preserve/update the canonical source `tracking: #N` if it has repo write access and the binding is known;
3. emit an exact pending Project mutation;
4. not claim the Project has already been synchronized;
5. not ask the user to drag cards or manually add source locators.

The next Project-capable maintenance action verifies freshness before applying.

## 16. Two-level completion truth

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

## 17. Required logical consumers

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

## 18. AI Skills Maintainer scope

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

## 19. Per-consumer completion mutation and final DONE

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

## 20. This board task's stages

This board is itself a machine-consumed shared maintenance mechanism.

### Central stage

Central implementation is complete only after:

- canonical board policy exists;
- AGENTS + Planner/Critic short consumer rules exist;
- TODO ownership docs exist;
- every TRACKED/MERGED canonical source entry has the correct durable `tracking: #N`;
- private Project is configured;
- full-inbox bootstrap complete;
- actual Project surface passes qualitative review;
- independent implementation review passes;
- reviewed repository changes are integrated to main;
- one-time ChatGPT Project-instructions trigger is installed.

Then:

```text
CENTRAL_IMPLEMENTATION_COMPLETE = YES
PROJECT_STATUS = ADAPTING
OVERALL_GOAL_ACHIEVED = NO
```

### Downstream stage

Resolve/freeze the five exact consumers and adapt each later under per-consumer authority.

The initial v0.4 central Kickoff does not authorize machine mutation.

## 21. Bounded external GitHub effects

The future approved central Kickoff may:

- inspect/create/reconcile the one private Project;
- link only `YuukiAS/AI_Skills_Collection`;
- configure approved fields/views/workflows;
- create/reuse `maintenance-track`;
- create/reuse/update tracking Issues required by full-inbox coverage;
- add/update eligible Issues in the Project;
- create/update this board task's tracking Issue;
- write non-closing task/PR/commit/review/evidence locators;
- perform full-inbox backfill/disposition;
- write/update `tracking: #N` in the exact canonical source entries represented by those tracking Issues.

It may not close unrelated backfilled Issues, mark this top-level task DONE, mutate server/local consumers, publish the Project, or disable repository-wide auto-close.

## 22. One-time UI gates

If no supported automation surface exists:

- GitHub Project workflow setup may require one minimal HUMAN_ONLY action before backfill, followed by real readback.
- ChatGPT Project instructions may require one minimal HUMAN_ONLY exact-text action after main integration.

Neither is recurring routine maintenance.

## 23. Verification gates

### B1 — Project structure

Verify actual Project identity, Status values, Area, Resolution commit, and four views.

### B2 — BOARD-01

Verify actual workflow state, issue-only auto-add, PR-merged -> Done disabled, final issue-close semantics, and live non-closing reference discipline.

### B3 — full-inbox coverage + durable source backlinks

Verify:

- every current canonical inbox declared by root TODO was scanned;
- every current meaningful entry has a disposition in `TODO_COVERAGE.md`;
- every `TRACKED` source entry contains the correct `tracking: #N`;
- every `MERGED_INTO_TRACKING_ISSUE` source entry contains the correct shared `tracking: #N`;
- reused existing Issues are written back with their actual Issue number;
- multiple duplicate source entries may correctly share one Issue locator;
- non-tracked dispositions are not forced to receive a locator;
- raw NEW source maturity remains NEW;
- no Project lifecycle Status is copied back into Markdown;
- locator-only edits did not change problem/evidence/project-specific context/target layer/candidate action/promotion gate;
- `TODO_COVERAGE.md` is not used as steady-state lookup/runtime mapping.

### B4 — normal entry / idempotency

Use this board task's own tracking Issue to verify one-time admission, Area=repo, DOING during central work, supported CLI/API list/update, no duplicates, Clear Writing, and correct source backlink when the task has a canonical source entry.

### B5 — human-facing surface

Independent Reviewer inspects actual Board, By area, this task Issue, and every new/materially rewritten tracking Issue top summary.

No field/string/API receipt proxy PASS.

### B6 — consumer locator + steady-state source-binding contract

Verify:

- one canonical board policy;
- AGENTS short locator;
- Planner/Critic short consumption rules;
- TODO/plugin-todo ownership docs;
- create/bind/reuse -> same-action `tracking: #N` writeback;
- merge/rebind -> source locator update;
- no-tool pending mutation;
- no manual user Kanban/source-locator sync;
- no duplicate full policy.

### B7 — independent central implementation review

Reviewer inspects real Project configuration/surface, repo diff, TODO_COVERAGE, source backlinks, BOARD-01, Clear Writing result, and role-consumer behavior.

Executor summary alone cannot PASS.

### B8 — central integration / ChatGPT trigger

After B7 PASS, integrate approved changes to main with ordinary non-force Git, verify remote main, perform README closure, install one-time Project-instructions trigger, record truthful setup evidence, and reconcile this task to ADAPTING.

### B9 — final five-consumer closure

Not executed by the initial central Kickoff. Later closure verifies five exact consumers PASS/N/A, current evidence, Resolution commit, completed close, and actual DONE.

## 24. Failure recovery

- Missing `project` scope -> stop before Project mutation; request one bounded auth refresh.
- Exact worktree unavailable -> stop before Project/Issue mutation.
- Clear Writing unavailable -> stop reader-facing copy mutation.
- GitHub workflow UI-only -> one minimal HUMAN_ONLY setup + readback.
- ChatGPT Project instructions user-only -> one exact-text setup after main integration.
- Ambiguous TODO dedupe -> preserve separate tracking or return Planner.
- Ambiguous/stale source tracking locator -> do not guess/rebind; return Planner for that entry.
- Semantic main drift -> return Planner/Critic.
- Stale pending mutation -> regenerate from current truth.
- Maintainer not production-ready -> stay ADAPTING.
- Exact machine identity requires new access -> request only that per-consumer bounded authority.
- One consumer PASS -> never aggregate-DONE.

## 25. No new board/control-plane component

Do not create:

- standalone board/Kanban skill;
- `kanban-sync` skill;
- new plugin/profile;
- board-specific MCP/service;
- cross-machine controller;
- machine registry/inventory service;
- watcher/daemon;
- central credential broker;
- GitHub Action/database/ledger/controller;
- new cross-machine state machine.

## 26. Version / README

```text
Repository bump decision: NONE
Reason: central task changes maintenance docs/contracts, canonical TODO locator metadata, and GitHub Project metadata only.

Affected plugins:
- all: NO_BUMP
  Reason: no plugin production source/runtime/package change.
```

Adding/updating `tracking: #N` in maintenance TODO inboxes is maintenance metadata and does not change plugin runtime behavior.

README closure is mandatory.

Expected:

```text
README checked: no update required
```

unless implementation creates a real public entry.

## 27. Completion statement

Central implementation may truthfully report only:

```text
CENTRAL_IMPLEMENTATION_COMPLETE = YES
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

No earlier stage may claim overall completion.
