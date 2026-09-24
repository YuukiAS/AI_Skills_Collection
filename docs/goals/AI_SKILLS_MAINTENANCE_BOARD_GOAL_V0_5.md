# AI Skills 维护看板 — Canonical Goal v0.5

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
- Implementation Plan: `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_5_2026-09-24.md`
- Supersedes for execution: all v0.4 execution-package files
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`

This Goal becomes executable only after an independent Critic passes the exact v0.5 Plan + Goal + Kickoff and returns `READY_FOR_CODEX=YES`, and the user then sends the approved Kickoff.

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

## 3. Frozen kickoff-base canonical inbox allowlist

Before any task content mutation or Project/Issue backfill:

1. fetch kickoff-time latest `origin/main`;
2. record it as `KICKOFF_BASE_COMMIT`;
3. read root `TODO.md` at that exact unmodified commit;
4. parse only the structured navigation entries that formally declare canonical maintenance inboxes;
5. verify each declared path exists at the same base;
6. freeze the exact path set;
7. create the exact reviewed branch/worktree from the same base;
8. make the first task-content evidence write:

`results/repo--maintenance-board-lifecycle/FROZEN_CANONICAL_INBOX_ALLOWLIST.md`

This evidence must include at least:

```text
KICKOFF_BASE_COMMIT = <sha>
ROOT_TODO_BLOB_SHA = <sha>
FROZEN_INBOX_COUNT = <N>
FROZEN_CANONICAL_INBOX_PATHS =
- <path>
...
```

This file is task evidence only, not a registry or service.

The frozen path set is the only locator-write authority for this task.

## 4. Task-mutated root TODO cannot expand authority

Later changes made by this task to root `TODO.md` do not change the frozen allowlist.

Even if the task branch adds a new inbox declaration:

- that path does not gain locator-write authority in this task;
- the task must not recompute authority from its mutated root TODO;
- a renamed/removed declaration does not silently retarget authority.

If kickoff-base parsing is ambiguous, fail closed before locator writes/backfill.

## 5. Post-kickoff upstream drift

If upstream `main` later declares a new canonical inbox:

- do not auto-add it to this task's allowlist;
- do not silently include it in this task's full-inbox claim;
- if it is necessary for this task to remain semantically complete, return Planner/user for scope expansion;
- otherwise defer it to later maintenance and record that fact.

No watcher or dynamic allowlist service is added.

## 6. Project identity and fields

Create or reconcile one private Project:

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

No fifth state, maturity field, machine-registry field, or new board schema.

## 7. Full-inbox bootstrap over frozen allowlist

Scan exactly the frozen kickoff-base inbox paths.

Every current meaningful source entry in those paths receives one disposition:

```text
TRACKED
MERGED_INTO_TRACKING_ISSUE
NON_CENTRAL_PROJECT_LOCAL
REJECTED_OR_SUPERSEDED
HISTORICAL_RESOLVED
```

Create:

`results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md`

Each row records:

```text
source inbox + heading
-> disposition
-> tracking Issue if any
-> Area
-> initial lifecycle Status if tracked
```

A valid central raw `NEW` may become Project TODO while source maturity remains `NEW`.

Do not mechanically create one Issue per heading.

Completeness is claimed only for the frozen kickoff-base inbox allowlist.

## 8. Durable source tracking locator

For every source entry with disposition:

- `TRACKED`
- `MERGED_INTO_TRACKING_ISSUE`

the same maintenance action must write/update:

```text
tracking: #<issue-number>
```

Rules:

- independent entry -> own top-level Issue;
- duplicate/merged entries may share one Issue;
- reused existing Issue -> actual reused number;
- merge/rebind -> update every affected source entry to current real Issue;
- raw NEW maturity remains `NEW`.

### Locator-only boundary

The locator write must not change:

- source maturity/status;
- problem;
- evidence;
- project-specific context;
- target layer;
- candidate action;
- promotion gate;
- any other substantive TODO field;
- Project lifecycle Status.

Do not write Project Status into Markdown.

Do not add locator to non-tracked dispositions merely for completeness.

Ambiguous existing locator conflict -> fail closed and return Planner for that entry.

## 9. TODO_COVERAGE is not the steady-state mapping

`TODO_COVERAGE.md` is bootstrap completeness evidence only.

It must not become:

- runtime lookup source;
- long-term source-to-Issue registry;
- Project status source;
- replacement for source `tracking: #N`.

Steady-state durable mapping comes from the canonical source entry itself.

## 10. User-readable Project surface

Every tracking Issue title is natural and concise.

Every Issue begins with:

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

Detailed evidence follows below.

Every DOING/ADAPTING item has a current valid anchor.

Board / By area show title + Area + Status.

History shows Resolution commit for DONE.

## 11. Clear Writing

Codex must actually invoke installed Clear Writing (`writing-style`) before creating/materially rewriting reader-facing Project/Issue copy.

Clear Writing must not change:

- source maturity;
- lifecycle truth;
- Area;
- `tracking: #N`;
- required-consumer truth;
- exact locators;
- Resolution commit;
- evidence meaning.

If unavailable, stop that reader-facing mutation and report `CLEAR_WRITING_UNAVAILABLE`.

Actual Project-surface qualitative review is authoritative.

## 12. BOARD-01

Keep all false-DONE protections:

- lifecycle item only = `maintenance-track` Issue
- issue-only auto-add
- PR merged -> Done disabled
- no early auto-closing link/keyword
- repository-wide auto-close unchanged
- final issue-close -> Done only after full closure
- rejected/superseded/duplicate/not-planned items do not appear DONE

## 13. One canonical board policy

Create one full policy:

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

Other surfaces contain only short trigger/locator/consumer rules.

The canonical policy must state:

```text
create / bind / reuse tracking Issue
-> same maintenance action write/update source tracking: #N

Issue merge / rebind
-> update affected canonical source entries to actual current Issue
```

Routine sync must not make the user maintain locators manually.

## 14. Normal-entry consumers

### ChatGPT Project instructions

After the canonical board doc is on `main`, install once:

```text
AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步，并在 canonical source entry 回写/更新 tracking: #N。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。
```

If user-only, one HUMAN_ONLY exact-text setup is allowed after main integration. Resume the same Goal and do not ask again routinely.

### AGENTS

Short Codex locator only: board-policy consumption, proactive sync, Clear Writing, no early DONE.

### Planner Role Contract

For formal AI_Skills maintenance:

- triage -> create/bind/reuse Issue or exact pending mutation;
- same action -> maintain source `tracking: #N` under the applicable canonical-inbox authority;
- first substantive Plan -> DOING + anchor;
- handoff -> next action/evidence;
- central implementation complete + consumers pending -> ADAPTING;
- no Project tool -> exact pending mutation.

### Critic Role Contract

Formal review reconciles review locator / next action / lifecycle truth. PASS/REVISE does not mechanically change Status. Reviewer PASS leads to ADAPTING only after required central closure. No-tool surface emits exact pending mutation. Critic does not become Planner/Executor.

## 15. Allowed central repo changes

Only:

- `AGENTS.md`
- root `TODO.md`
- `docs/plugin-todos/README.md`
- new `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `README.md` only if closure check proves necessary
- `results/repo--maintenance-board-lifecycle/**`
- ordinary task control/evidence required by current workflow
- **only paths listed in `FROZEN_CANONICAL_INBOX_ALLOWLIST.md`**, only for `tracking: #N` locator maintenance

Root TODO edits cannot expand this list.

Forbidden:

- substantive TODO edits under locator-only authority
- locator writes outside frozen list
- `skills/` production source
- generated Marketplace/plugin payload
- profile exposure
- ai-skills-repository-maintainer source
- machine-update source
- Bridge Kit
- machine/Host state
- paid API
- destructive/force Git

## 16. Two-level completion

```text
execution-ready Critic PASS
-> implementation
-> independent implementation review PASS
-> canonical integration/release closure when required
= central implementation complete
```

Execution-ready PASS, Executor self-report, or Reviewer PASS without required canonical closure remains DOING.

For machine-consumed workflow/shared maintenance mechanism:

```text
central implementation complete
-> ADAPTING
```

## 17. Current required logical consumers

For machine-consumed workflow/shared maintenance mechanisms:

### Server / remote Codex
1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`

### Local
4. `Workstation`
5. `Legion`

Resolve/freeze exact current identities only at ADAPTING cutover under per-consumer authority.

If identity resolution needs machine access, obtain that bounded authority first.

Future optional consumers do not retroactively enlarge old DONE.

N/A requires durable frozen reason.

## 18. AI Skills Maintainer scope

AI Skills Maintainer remains a **per-current-consumer adaptation executor**.

It is not a cross-machine controller, five-machine orchestrator, machine registry owner, or credential broker.

Each consumer is adapted from its current Codex environment or a separately approved existing remote route preserving the per-consumer boundary.

Maintainer handles only that consumer's discovery, update/adaptation, installed/loaded identity, fresh-session/normal-entry verification, durable evidence, and PASS/truthful blocker.

Five-consumer aggregate truth belongs to the tracking Issue / Project.

## 19. Initial v0.5 authorization boundary

The v0.5 Kickoff authorizes central implementation only.

It does not authorize server/local-machine mutation.

At ADAPTING cutover:

- resolve exact consumer identities under per-consumer authority;
- generate exact per-consumer handoffs;
- request only newly required machine/credential/remote authorization.

Project remains ADAPTING until downstream closure.

## 20. Final DONE

A single consumer PASS never closes the top-level Issue.

Final machine-consumed DONE requires:

```text
all required consumers PASS/N/A
+ durable evidence
+ Resolution commit
+ completed close
+ issue-closed workflow -> DONE
```

## 21. Verification

Central candidate must prove:

### V1 Frozen allowlist provenance

- `KICKOFF_BASE_COMMIT` equals the unmodified kickoff-time base used for task branch;
- `ROOT_TODO_BLOB_SHA` matches root TODO at that base;
- frozen path set exactly equals formal canonical inbox declarations in that unmodified root TODO;
- every frozen path existed at that base;
- first task-content evidence write is the frozen allowlist artifact.

### V2 Scope non-expansion

- every locator edit path is inside frozen allowlist;
- no locator edit occurred outside it;
- task-mutated root TODO did not expand authority;
- post-kickoff newly declared inboxes were not silently added.

### V3 Full coverage + locator integrity

- every meaningful entry in frozen inboxes has disposition;
- every TRACKED entry has correct locator;
- every MERGED entry has correct shared locator;
- reused Issue locator is correct;
- non-tracked entry not forced to get locator;
- raw NEW maturity unchanged;
- substantive fields unchanged by locator-only edits;
- Project Status not copied to Markdown;
- TODO_COVERAGE not used as steady-state mapping.

### V4 Project / BOARD-01 / surface

Actual Project config/workflows, issue-only admission, false-DONE guardrails, Clear Writing, actual Board/By-area/Issue qualitative review.

### V5 Consumer contracts / idempotency

One canonical policy, short consumer locators, proactive sync, same-action source backlink, no-tool pending mutation, no duplicate Project/Issue/item.

### V6 Independent central review and integration

Reviewer inspects real Project/config, repo diff, frozen allowlist, TODO_COVERAGE, source backlinks, Clear Writing result, and scope non-expansion. After PASS, integrate to main, verify remote, README closure, install one-time Project trigger, then move this task to ADAPTING.

## 22. This board task's truthful central completion

Central implementation may report only after all central conditions:

```text
CENTRAL_IMPLEMENTATION_COMPLETE = YES
FROZEN_INBOX_ALLOWLIST_VERIFIED = YES
SOURCE_TRACKING_LOCATORS_VERIFIED = YES
PROJECT_STATUS = ADAPTING
OVERALL_GOAL_ACHIEVED = NO
```

Overall DONE waits for five-consumer aggregate closure.

## 23. Failure recovery

- missing `project` scope -> bounded auth refresh before Project mutation
- exact worktree unavailable -> stop
- kickoff-base inbox parsing ambiguous -> stop before locator writes/backfill
- Clear Writing unavailable -> stop reader-facing mutation
- GitHub workflow UI-only -> one minimal setup + readback
- ChatGPT Project settings user-only -> one exact-text setup after main integration
- ambiguous TODO dedupe -> do not guess
- ambiguous/stale source locator -> do not guess/rebind
- required post-kickoff new inbox -> return Planner/user for scope expansion
- semantic main drift -> Planner/Critic
- stale pending mutation -> regenerate
- Maintainer not production-ready -> stay ADAPTING
- exact consumer identity needs access -> obtain per-consumer authority
- one consumer PASS -> never aggregate-DONE

## 24. No new control plane

Do not create standalone Kanban skill, `kanban-sync` skill, new plugin/profile, board-specific MCP/service, cross-machine controller, machine registry, watcher/daemon, allowlist service, credential broker, GitHub Action/database/ledger/controller, or new cross-machine state machine.

## 25. Version / README

```text
Repository bump decision: NONE
Reason: maintenance docs/contracts, canonical TODO tracking metadata, frozen task evidence, and GitHub Project metadata only.

Affected plugins:
- all: NO_BUMP
  Reason: no plugin production source/runtime/package change.
```

README closure is mandatory. Expected: `README checked: no update required` unless a real public entry is created.

## 26. Overall completion boundary

Only final five-consumer closure may report:

```text
FIVE_CONSUMER_AGGREGATE_VERIFIED = YES
RESOLUTION_COMMIT = <canonical closure commit>
TRACKING_ISSUE_CLOSED_COMPLETED = YES
PROJECT_STATUS = DONE
OVERALL_GOAL_ACHIEVED = YES
```

No earlier stage may claim overall completion.
