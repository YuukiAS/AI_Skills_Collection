# AI Skills 维护看板 — Canonical Goal v0.4

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
- Implementation Plan: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_4_2026-09-24.md`
- Supersedes for execution: all v0.3 execution-package files
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`

This Goal becomes executable only after an independent Critic passes the exact v0.4 Plan + Goal + Kickoff and returns `READY_FOR_CODEX=YES`, and the user then sends the approved Kickoff.

## 1. Exact execution identity

```text
repo = YuukiAS/AI_Skills_Collection
task_key = repo--maintenance-board-lifecycle
branch = reviewed/repo--maintenance-board-lifecycle
worktree = ../AI_Skills_Collection-repo--maintenance-board-lifecycle
base = kickoff-time latest origin/main
```

No alternate branch, worktree, `/tmp` fallback, dirty-checkout substitution, task-key substitution, force push, or history rewrite is authorized.

## 2. Required lifecycle

```text
TODO -> DOING -> ADAPTING -> DONE
```

- Project item = top-level tracking Issue.
- Plugin / standalone-skill TODO = failure/evidence/maturity inbox.
- Planner–Critic / Reviewed Handoff / Executor task = execution evidence.
- WAITING/BLOCKED are not fifth lifecycle states.
- DONE requires Resolution commit.
- `Project lifecycle status != plugin TODO maturity status`.

A source `status: NEW` entry may be a Project `TODO` without changing source maturity.

## 3. Project identity and minimum surface

Create or reconcile exactly one private Project:

```text
owner = YuukiAS
title = AI Skills Maintenance
linked repo = YuukiAS/AI_Skills_Collection
tracking label = maintenance-track
```

Required fields:

- Status = TODO / DOING / ADAPTING / DONE
- Area
- Resolution commit

Required views:

- Board
- Active
- By area
- History

No fifth state, machine-registry field, maturity field, or new board schema.

## 4. Full-inbox bootstrap

Scan every current canonical maintenance inbox formally declared by kickoff-time root `TODO.md`.

Each current meaningful source entry receives one disposition:

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

Create one-time completeness evidence:

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

Each relevant row records:

```text
source inbox + heading
-> disposition
-> tracking Issue if any
-> Area
-> initial lifecycle Status if tracked
```

A valid central raw `NEW` may become Project TODO while its source maturity remains `NEW`.

Do not mechanically create one Issue per heading.

## 5. Durable source-to-Issue backlink — BOARD-TRACKING-LOCATOR-01

For every canonical source entry with disposition:

- `TRACKED`, or
- `MERGED_INTO_TRACKING_ISSUE`,

the same maintenance action must write/update:

```text
tracking: #<issue-number>
```

Rules:

- independent entry -> its own top-level Issue;
- duplicate/merged entries may share one Issue number;
- reused existing Issue -> write the actual reused Issue number;
- merge/rebind -> update every affected canonical source entry to the real current Issue;
- raw NEW remains `NEW` in source maturity.

`tracking: #N` is the steady-state durable mapping. `TODO_COVERAGE.md` is not.

### Locator-only edit boundary

The bootstrap/steady-state locator write must not change:

- source maturity/status;
- problem;
- evidence;
- project-specific context;
- target layer;
- candidate action;
- promotion gate;
- any other substantive TODO field;
- Project lifecycle Status.

Do not copy TODO/DOING/ADAPTING/DONE into Markdown.

Do not add tracking locators to non-tracked dispositions merely for completeness.

If an existing locator conflicts and the correct mapping is ambiguous, stop that entry and return Planner rather than guessing.

## 6. Allowed canonical inbox modifications

Central execution may modify canonical maintenance inbox files formally declared by kickoff-time root `TODO.md`, only for tracking-locator maintenance.

This includes the currently listed:

- `docs/plugin-todos/*.md`
- `docs/skill-todos/*.md`

and any future canonical maintenance inbox explicitly listed by root `TODO.md` at execution time.

This authority is **locator-only** and does not authorize arbitrary edits to every file matching a directory glob.

## 7. User-readable Project surface

Tracking Issue titles must be natural and concise.

Every tracking Issue begins with:

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

Detailed history/evidence follows below.

Every DOING/ADAPTING item has a current valid anchor.

Board / By area directly show title + Area + Status.

History directly shows Resolution commit for DONE.

## 8. Clear Writing hard requirement

Whenever Codex creates or materially rewrites reader-facing Project/Issue copy, it must actually invoke installed Clear Writing (`writing-style`) before mutation.

Clear Writing must not change:

- source maturity;
- Project Status;
- Area;
- `tracking: #N`;
- required-consumer truth;
- exact locators;
- Resolution commit;
- evidence strength.

If unavailable, stop that reader-facing mutation and report `CLEAR_WRITING_UNAVAILABLE`.

Actual Project-surface qualitative review is the final quality authority.

## 9. BOARD-01

Keep all false-DONE protections:

- lifecycle item only = `maintenance-track` Issue
- issue-only auto-add
- implementation/design PR not lifecycle item
- Project PR merged -> Done disabled
- no early auto-closing Development/manual links
- no early closing keywords against tracking Issue
- repository-wide auto-close unchanged
- final issue-close -> Done only after full closure
- rejected/superseded/duplicate/not-planned items do not appear DONE

## 10. Canonical board policy and steady-state source binding

Create the only full board policy at:

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

It must explicitly require:

```text
create / bind / reuse tracking Issue
-> in the same maintenance action write/update source tracking: #N

Issue merge / rebind
-> update every affected canonical source entry to the actual current Issue
```

Routine sync must not require the user to manually edit TODO locators.

Other surfaces only contain short trigger/locator/consumer rules.

## 11. Normal-entry consumers

### ChatGPT Project instructions

After the canonical board doc is on `main`, install this exact short trigger once:

```text
AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步，并在 canonical source entry 回写/更新 tracking: #N。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。
```

If Project settings are user-only, request one HUMAN_ONLY exact-text setup after main integration, then resume the same Goal. Do not repeat during routine sync.

### AGENTS

Add only a short Codex locator requiring board-policy consumption, proactive reconciliation, Clear Writing for board copy, and no early DONE.

### Planner Role Contract

For formal AI_Skills maintenance:

- tracking-scope triage -> create/bind/reuse Issue or exact pending mutation;
- same action -> write/update source `tracking: #N`;
- first substantive Plan/design -> DOING + current anchor;
- handoff -> next action/evidence;
- central implementation complete + consumers pending -> ADAPTING + freeze exact consumer locators;
- no Project mutation tool -> exact pending mutation.

### Critic Role Contract

For formal AI_Skills review:

- reconcile review locator / next action / lifecycle truth;
- PASS/REVISE alone does not mechanically change Status;
- implementation Reviewer PASS may lead to ADAPTING only after required canonical central closure;
- no Project mutation tool -> exact pending mutation;
- no Planner/Executor role violation.

## 12. No-tool pending mutation

A GPT/Planner/Critic surface without Project mutation capability remains semantic owner.

It must:

- update any canonical source `tracking: #N` it can legitimately update when the binding is known;
- update any Issue evidence it can legitimately update;
- emit an exact pending Project mutation;
- not claim synchronization already occurred;
- not ask the user to drag cards or manually insert source locators.

The next capable action verifies freshness before applying.

## 13. Two-level completion truth

```text
execution-ready Critic PASS
-> Codex implementation
-> independent implementation review PASS
-> canonical owner integration/release closure when required
= central implementation complete
```

Execution-ready PASS alone remains DOING.

Executor self-report alone remains DOING.

Reviewer PASS without required canonical closure remains DOING.

For machine-consumed workflow/shared maintenance mechanism:

```text
central implementation complete
-> ADAPTING
```

Non-machine-consumed work uses its own frozen completion contract.

## 14. Current five required logical consumers

For machine-consumed workflow/shared maintenance mechanisms:

### Server / remote Codex

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

### Local

4. `Workstation`
5. `Legion`

At ADAPTING cutover, resolve/freeze each exact current identity/locator under per-consumer authority.

If exact identity resolution requires machine access, obtain that consumer's bounded authorization first. Do not guess.

Future optional consumers do not retroactively enlarge the frozen contract.

N/A requires a durable frozen reason.

## 15. AI Skills Maintainer remains per-consumer

AI Skills Maintainer is a **per-current-consumer adaptation executor**, not a cross-machine controller, five-machine orchestrator, machine registry owner, or credential broker.

When its independent machine-update capability is production-ready, each consumer is adapted in its current Codex environment or through a separately approved existing remote route preserving the same per-consumer boundary.

Maintainer only handles that current consumer's discovery, update/adaptation, installed/loaded identity, fresh-session/normal-entry verification, durable evidence, and PASS/truthful blocker.

Five-consumer aggregate truth remains in the tracking Issue / Project.

## 16. Consumer completion mutation and final DONE

If Maintainer can mutate Project, it may update that consumer's evidence/checklist. If any consumer remains pending, Status stays ADAPTING.

If it cannot mutate Project, it emits an exact completion mutation containing:

- tracking Issue
- consumer
- exact current consumer identity
- PASS/N/A
- adaptation evidence
- normal-entry evidence
- lifecycle truth
- next action

The next capable action verifies tracking Issue, frozen consumer identity, evidence freshness, and lifecycle compatibility before applying.

A single consumer PASS never closes the top-level Issue.

Final DONE requires:

```text
all required consumers PASS/N/A
+ durable evidence
+ Resolution commit
+ completed close
+ issue-closed workflow -> DONE
```

## 17. This board task has central and downstream stages

Central implementation is complete only after:

- canonical board policy exists;
- AGENTS + Planner/Critic rules exist;
- TODO ownership docs exist;
- every TRACKED/MERGED canonical source entry has the correct `tracking: #N`;
- private Project configured;
- full-inbox bootstrap complete;
- actual surface qualitative review passes;
- independent implementation review passes;
- approved repo changes integrated to main;
- one-time ChatGPT Project trigger installed.

Then truthfully report:

```text
CENTRAL_IMPLEMENTATION_COMPLETE = YES
SOURCE_TRACKING_LOCATORS_VERIFIED = YES
PROJECT_STATUS = ADAPTING
OVERALL_GOAL_ACHIEVED = NO
```

The five downstream consumers are adapted later.

## 18. Initial v0.4 authorization boundary

The v0.4 Kickoff authorizes the central implementation stage only.

It does not authorize server/local-machine mutation.

At ADAPTING cutover:

- resolve/freeze exact consumers under per-consumer authority;
- generate exact per-consumer handoff(s);
- obtain any newly required machine/credential/remote authorization.

The Project remains ADAPTING until five-consumer closure.

## 19. Allowed central repo changes

Only:

- `AGENTS.md`
- root `TODO.md`
- `docs/plugin-todos/README.md`
- new `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `README.md` only if closure check proves a public update is needed
- `results/repo--maintenance-board-lifecycle/**`
- ordinary task-control/evidence required by existing workflow
- root-TODO-declared canonical maintenance inbox files, **only for `tracking: #N` locator edits**

Forbidden:

- substantive TODO-field edits under the locator-only authority
- `skills/` production source
- generated Marketplace/plugin payload
- profile exposure
- ai-skills-repository-maintainer source
- machine-update source
- Bridge Kit
- server/local machine/Host state
- paid API
- force/destructive Git

## 20. Authorized central GitHub effects after approved Kickoff

May:

- create/reconcile one private Project;
- link only AI_Skills repo;
- configure approved fields/views/workflows;
- create/reuse `maintenance-track`;
- create/reuse/update tracking Issues needed by full-inbox coverage;
- add/update eligible Issues;
- write non-closing evidence locators;
- backfill/disposition;
- write/update correct `tracking: #N` backlinks in represented canonical source entries.

May not:

- close unrelated backfilled Issues;
- mark this task DONE;
- mutate machines;
- publish Project;
- disable repository-wide auto-close.

## 21. Verification

Central candidate must prove:

### C1 Project configuration
Actual Project identity/fields/views/workflows.

### C2 BOARD-01
Actual issue-only admission and false-DONE protections.

### C3 Full coverage + source backlinks
- every current meaningful inbox entry has a disposition;
- every TRACKED entry has correct `tracking: #N`;
- every MERGED entry has correct shared `tracking: #N`;
- reused Issue numbers are correctly written back;
- non-tracked entries are not forced to get a locator;
- source maturity is unchanged by admission;
- locator-only edits did not change substantive TODO fields;
- TODO_COVERAGE is not a runtime/steady-state mapping source.

### C4 Normal entry / idempotency
No duplicate Project/Issue/item and correct source backlink behavior.

### C5 Human-facing surface
Actual Board/By area/Issue qualitative review.

### C6 Consumer contracts
One canonical policy, short locators, proactive sync, same-action source-backlink update, no-tool pending mutation, no manual source-locator sync.

### C7 Independent implementation review
Actual Project, repo diff, coverage, source backlinks, BOARD-01, Clear Writing, consumer contracts.

### C8 Central integration
Ordinary non-force main integration, remote verification, README closure, one-time ChatGPT Project trigger, then ADAPTING cutover.

### C9 Final five-consumer closure
Later, outside initial central Kickoff.

## 22. Failure recovery

- missing `project` scope -> bounded auth refresh before Project mutation;
- exact worktree unavailable -> stop;
- Clear Writing unavailable -> stop reader-facing mutation;
- GitHub workflow UI-only -> one minimal HUMAN_ONLY setup + readback;
- ChatGPT Project settings user-only -> one exact-text setup after main integration;
- ambiguous TODO dedupe -> do not guess;
- ambiguous/stale source tracking locator -> do not guess/rebind;
- semantic main drift -> Planner/Critic;
- stale pending mutation -> regenerate;
- Maintainer not production-ready -> stay ADAPTING;
- exact consumer identity needs machine access -> obtain that per-consumer authorization first;
- one consumer PASS -> never aggregate-DONE.

## 23. No new control plane

Do not create:

- standalone Kanban/board skill
- `kanban-sync` skill
- new plugin/profile
- board-specific MCP/service
- cross-machine controller
- machine registry/inventory service
- watcher/daemon
- central credential broker
- GitHub Action/database/ledger/controller
- new cross-machine state machine

## 24. Version / README

```text
Repository bump decision: NONE
Reason: maintenance docs/contracts, canonical TODO tracking metadata, and GitHub Project metadata only.

Affected plugins:
- all: NO_BUMP
  Reason: no plugin production source/runtime/package change.
```

README closure is mandatory. Expected: `README checked: no update required`, unless a real public entry is created.

## 25. Completion boundary

Central stage may report only:

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

No earlier milestone may claim overall completion.
