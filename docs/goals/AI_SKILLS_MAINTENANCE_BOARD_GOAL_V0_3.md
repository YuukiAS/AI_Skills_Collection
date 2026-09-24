# AI Skills 维护看板 — Canonical Goal v0.3

- Human label: AI Skills 维护看板与完成语义
- Task key: repo--maintenance-board-lifecycle
- Repository: YuukiAS/AI_Skills_Collection
- Package version: v0.3
- Approved design: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_PROPOSAL_2026-09-24.md
- Approved design commit: d14565e152b9b953c76c0722ad6e6343850335a7
- Design Critic PASS: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V5_CRITIC_REVIEW_2026-09-24.md
- Design Critic review commit: 012a43c7edefddd7f071d43425f7be937453f73a
- Implementation Plan: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_IMPLEMENTATION_PLAN_V0_3_2026-09-24.md
- Supersedes for execution: all v0.2 execution-package files
- Status: READY_FOR_EXECUTION_CRITIC_REVIEW

This Goal is not executable until an independent Critic passes this exact v0.3 Plan + Goal + Kickoff package and returns READY_FOR_CODEX=YES, and the user then sends the approved Kickoff.

## 1. Exact execution identity

Repository: YuukiAS/AI_Skills_Collection
Task key: repo--maintenance-board-lifecycle
Branch: reviewed/repo--maintenance-board-lifecycle
Worktree: ../AI_Skills_Collection-repo--maintenance-board-lifecycle
Base: kickoff-time latest origin/main

The sibling worktree path is exact relative to the canonical repository root. Resolve it to one absolute path and record it before creation. No alternate branch, path, /tmp fallback, dirty-checkout substitution, task-key substitution, force push, or history rewrite is authorized.

## 2. Required lifecycle

The maintenance Project must use exactly:

TODO -> DOING -> ADAPTING -> DONE

Semantics:

- Project item = one top-level tracking Issue.
- Plugin/skill TODO = failure, evidence, and maturity inbox.
- Planner–Critic / Reviewed Handoff / Executor task = execution evidence.
- WAITING/BLOCKED are not fifth lifecycle states.
- Resolution commit is required for DONE.
- Project lifecycle status is distinct from plugin TODO maturity.

A raw NEW may be visible as Project TODO while remaining NEW in the source inbox.

## 3. Required Project surface

Create or reconcile exactly one private Project:

Owner: YuukiAS
Title: AI Skills Maintenance
Linked repository: YuukiAS/AI_Skills_Collection
Tracking label: maintenance-track

Required fields:

- Status: TODO, DOING, ADAPTING, DONE
- Area: workflow-core, ai-skills-core, each central domain plugin, standalone-skill, repo, cross-plugin
- Resolution commit: text

Required views:

- Board
- Active
- By area
- History

Do not add a fifth lifecycle state, maturity field, machine-registry field, or new board schema.

## 4. Full-inbox bootstrap

The initial bootstrap must scan every current canonical maintenance inbox named by root TODO.md, including current central plugin and standalone-skill TODO inboxes.

Every current meaningful entry must receive exactly one bootstrap disposition:

- TRACKED
- MERGED_INTO_TRACKING_ISSUE
- NON_CENTRAL_PROJECT_LOCAL
- REJECTED_OR_SUPERSEDED
- HISTORICAL_RESOLVED

Create:

results/repo--maintenance-board-lifecycle/TODO_COVERAGE.md

For every relevant source entry, record:

source inbox + heading
-> disposition
-> tracking Issue if any
-> Area
-> initial lifecycle Status if tracked

TODO_COVERAGE.md is one-time completeness evidence only. It must not become a long-term registry, ledger, or status source.

A valid central raw NEW may become a Project TODO. Its source maturity remains NEW unless a later Planner separately promotes it.

Do not mechanically create one Issue per Markdown heading. Dedupe only where the evidence clearly describes the same top-level idea.

## 5. Human-readable board contract

The Project is a user-facing artifact.

Every tracking Issue title must be natural and concise. Task keys, hashes, branches, paths, or internal status strings may be locators but must not be the title's main content.

Every tracking Issue begins with a short top section containing, in this order:

问题：
当前进度：
当前执行锚点：
下一步：

Detailed evidence/history follows below.

Every DOING or ADAPTING item must have at least one current valid execution anchor.

Board and By area must directly show human-readable title + Area + Status.

History must directly show Resolution commit for DONE items.

## 6. Clear Writing hard requirement

Whenever Codex creates or materially rewrites reader-facing Project/Issue copy, it must actually invoke the installed Clear Writing plugin, writing-style, before the GitHub mutation.

This applies to Issue titles, top summaries, backfill copy, reader-facing card text, and closure/history copy.

Clear Writing may improve wording but must not change lifecycle truth, source maturity, Area, required-consumer truth, exact locators, Resolution commit, or evidence strength.

If Clear Writing is unavailable, stop the reader-facing mutation and report CLEAR_WRITING_UNAVAILABLE.

Actual Project-surface qualitative review remains authoritative; a Clear Writing invocation record alone cannot PASS.

## 7. BOARD-01 guardrails

The implementation must preserve all of the following:

- lifecycle item only = maintenance-track Issue
- auto-add at least = is:issue label:maintenance-track
- implementation/design PR is not a lifecycle item
- Project pull request merged -> Done is disabled
- before true DONE, no Development/manual relationship may auto-close the tracking Issue
- before true DONE, PR body / commit message may not use closing keywords against the tracking Issue
- repository-wide linked-PR auto-close remains unchanged
- issue closed -> Done is retained only as the final mechanical mapping after the complete closure contract
- rejected/superseded/duplicate/not-planned items must not appear as DONE

## 8. One canonical policy and normal-entry consumers

Create one full canonical policy:

docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md

No other surface may duplicate the whole policy.

Central implementation must add only short trigger/locator/consumer rules to:

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- TODO.md / docs/plugin-todos/README.md as appropriate

The existing ai-skills-repository-maintainer remains a central-maintenance owner by architecture, but this board task must not modify its production skill source. Any later production-source locator belongs to a separate normal plugin refinement/release decision.

## 9. ChatGPT Project-instructions one-time setup

After the canonical board doc is integrated to main, AI Research Stack Project instructions must receive this exact short addition once:

AI_Skills 维护看板：当本 Project 任意 thread 要向 YuukiAS/AI_Skills_Collection 的 plugin/skill TODO 记录、triage、规划、Critic review、adaptation 或 closure 时，读取并遵循 main 的 docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md。raw NEW 先写 canonical inbox；进入 tracking scope 后主动维护 tracking Issue、Status、当前执行锚点与下一步。若当前 ChatGPT surface 不能修改 GitHub Project，输出 exact pending Project mutation 给下一 Project-capable Codex / AI Skills Maintainer；不要要求用户手工拖 Kanban，也不要声称已同步。

If the execution surface cannot modify Project instructions, the approved Kickoff may request one HUMAN_ONLY exact-text Project-settings action after main integration. Resume the same Goal after completion. Do not ask again during routine sync.

## 10. Planner / Critic proactive sync

Planner Role Contract must require, for formal AI_Skills maintenance:

- triage into tracking scope -> create/bind tracking Issue or exact pending mutation
- first substantive Plan/design -> reconcile DOING + current anchor
- handoff -> reconcile next action/evidence
- central implementation complete + required machine consumers pending -> ADAPTING + freeze exact consumer locators
- no Project mutation surface -> exact pending mutation
- no manual user Kanban sync

Critic Role Contract must require:

- formal review -> review locator + next action + lifecycle-truth reconciliation
- PASS/REVISE alone does not mechanically change Status
- implementation Reviewer PASS may lead to ADAPTING only after required canonical central closure also holds
- no Project mutation surface -> exact pending mutation
- Critic still does not edit Planner Proposal, advance Reviewed Handoff CURRENT, or impersonate Executor

## 11. No-tool pending mutation

A GPT/Planner/Critic surface without Project mutation capability remains the semantic owner.

It must update any Issue evidence it can legitimately update, emit an exact pending Project mutation, and never claim the Project is already synchronized.

The next Project-capable maintenance action must verify that the pending mutation still belongs to the current tracking Issue and remains current before applying it.

Routine sync must not make the user drag cards manually.

## 12. Two-level completion truth

Central implementation complete means:

execution-ready Critic PASS
-> Codex implementation
-> independent implementation review PASS
-> canonical owner integration/release closure when required by the frozen Goal
= central implementation complete

Execution-ready PASS alone remains DOING.

Executor self-report remains DOING.

Reviewer PASS without required canonical integration/release closure remains DOING.

For a machine-consumed workflow/shared maintenance mechanism:

central implementation complete
-> ADAPTING

Non-machine-consumed work follows its own frozen completion contract and does not automatically inherit five-machine rollout.

## 13. Current required logical consumers

For machine-consumed workflow/shared maintenance mechanisms, the current default required logical consumers are:

Server / remote Codex:
1. Longleaf_Codex
2. Longleaf_Backup_Codex
3. CUHK_Workstation_WSL_Codex

Local:
4. Workstation
5. Legion

When the item enters ADAPTING, resolve and freeze each logical consumer to its exact current identity/locator for that item.

Do not permanently hard-code hostname, SSH alias, CODEX_HOME, checkout, account, credential, or private local path into the board policy.

Future optional consumers do not retroactively enlarge the frozen contract.

N/A requires a durable reason in the frozen completion contract.

## 14. AI Skills Maintainer is per-consumer only

AI Skills Maintainer is a per-current-consumer adaptation executor.

It is not:

- a cross-machine controller
- a five-machine orchestrator
- a machine registry owner
- a central credential broker

When the independent machine-update capability is production-ready, each required consumer is handled from that consumer's current Codex environment, or through a separately approved existing remote route that preserves the same per-consumer boundary.

For the current consumer only, Maintainer may handle:

- discovery
- adaptation/update
- installed/loaded identity verification
- fresh-session / normal-entry verification
- durable evidence
- current-consumer PASS or truthful blocker

Maintainer does not own five-consumer aggregate truth.

## 15. Consumer completion mutation

If the current Maintainer can mutate the Project, it may update that consumer's evidence/checklist.

If any required consumer remains pending, Status stays ADAPTING.

If Maintainer lacks Project mutation capability, it must emit an exact completion mutation including at least:

- tracking Issue
- consumer
- exact current consumer identity
- PASS or N/A
- adaptation evidence
- normal-entry evidence
- current lifecycle truth
- next action

Before applying it, the next Project-capable maintenance action must verify the tracking Issue, exact frozen consumer identity, evidence freshness, and lifecycle compatibility.

The user is not the five-consumer aggregator.

## 16. Final DONE for machine-consumed work

The tracking Issue / Project lifecycle is the aggregate owner.

Detailed ADAPTING evidence tracks all five consumers as PENDING, PASS, or N/A(frozen reason), with exact resolved identity and durable evidence for each non-pending row.

A single consumer PASS never closes the top-level Issue.

Final DONE requires:

all required consumers PASS/N/A
+ durable evidence complete
+ Resolution commit recorded
+ tracking Issue closed as completed
+ issue-closed workflow sets DONE

## 17. This maintenance-board task is itself machine-consumed

The board changes normal maintenance behavior consumed by GPT/Codex environments, so this Goal has a central stage and a downstream adaptation stage.

Central implementation is complete only after:

- canonical board policy exists
- AGENTS + Planner/Critic consumption rules exist
- TODO ownership docs are updated
- private GitHub Project is configured
- full-inbox coverage is complete
- actual Project surface passes qualitative review
- independent implementation review passes
- approved repository changes are integrated to main
- the one-time ChatGPT Project-instructions trigger is installed

Then the truthful state is:

CENTRAL_IMPLEMENTATION_COMPLETE = YES
PROJECT_STATUS = ADAPTING
OVERALL_GOAL_ACHIEVED = NO

The five required logical consumers must then be resolved and adapted before final DONE.

## 18. Initial v0.3 Kickoff authorization boundary

The v0.3 Kickoff authorizes only the central implementation stage.

It does not authorize server/local-machine mutation.

At ADAPTING cutover, exact current consumer identities, environment authority, credentials, and production-ready Maintainer availability must be resolved. Then produce exact per-consumer handoff(s) for current-user authorization.

This is a new external machine effect, not routine Kanban sync.

The Project remains ADAPTING while those downstream handoffs execute.

## 19. Allowed central repository modifications

Only:

- AGENTS.md
- TODO.md
- docs/plugin-todos/README.md
- new docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- README.md only if the required closure check finds a real public-facing change
- results/repo--maintenance-board-lifecycle/**
- ordinary task-control/evidence files required by the current Reviewed Handoff contract

Forbidden:

- skills/ production source
- Marketplace/plugin generated payload
- profile exposure
- AI Skills Maintainer source
- machine-update-orchestrator source
- Bridge Kit
- server/local-machine/Host state
- paid API
- force/destructive Git

## 20. Authorized central GitHub effects after approved Kickoff

The future approved Kickoff may authorize:

- inspect/create/reconcile the single private Project
- link only YuukiAS/AI_Skills_Collection
- configure approved fields/views/workflows
- create/reuse maintenance-track
- create/reuse/update tracking Issues required by full-inbox coverage
- add/update eligible Issues in the Project
- create/update this board task's own tracking Issue
- write non-closing task/PR/commit/review/evidence locators
- perform full-inbox backfill/disposition

It may not:

- close unrelated backfilled Issues
- mark this board task DONE
- mutate any server/local consumer
- publish the Project
- disable repository-wide auto-close

## 21. One-time UI gates

If no supported automation surface exists:

1. GitHub Project workflow configuration may require one minimal HUMAN_ONLY action before backfill, followed by real readback.
2. ChatGPT Project instructions may require one minimal HUMAN_ONLY exact-text action after main integration.

Neither is recurring routine maintenance.

## 22. Central-stage validation

The same central candidate must prove:

- actual Project structure, fields, views, workflow states, issue-only auto-add, PR-merged -> Done disabled
- live BOARD-01 link discipline
- complete TODO_COVERAGE for all current canonical inboxes
- raw NEW visibility without maturity promotion
- Clear Writing used for Codex board copy
- actual Board / By area / Issue qualitative readability
- one canonical board policy with only short consumer locators elsewhere
- Planner/Critic proactive-sync rules
- no-tool pending-mutation rule
- reconcile/idempotency does not create duplicate Project/Issue/items
- no plugin production source/version change
- independent implementation review of real Project configuration/surface and repo diff

Executor summary, field presence, keyword scan, API receipt, or Clear Writing invocation alone cannot PASS.

## 23. Central integration and cutover

After independent implementation review PASS:

1. fetch latest main
2. semantic overlap -> return Planner/Critic
3. otherwise ordinary non-force integration to main
4. verify remote main
5. perform README closure check
6. install the exact ChatGPT Project-instructions trigger once
7. record truthful completion evidence
8. reconcile this task's tracking Issue to ADAPTING
9. resolve/freeze the five exact consumers and generate downstream handoffs

Do not set Resolution commit or close the top-level Issue yet.

## 24. Downstream final closure

The initial v0.3 Kickoff does not execute machine adaptation.

Later, each consumer is handled per the approved per-consumer route.

Overall DONE requires an independent aggregate closure check confirming all five PASS/N/A with current durable evidence, then:

- create or identify the canonical closure/evidence Resolution commit
- write Resolution commit to Project + Issue
- close tracking Issue as completed
- verify issue-closed workflow sets DONE
- verify History shows Resolution commit

Only then:

FIVE_CONSUMER_AGGREGATE_VERIFIED = YES
PROJECT_STATUS = DONE
OVERALL_GOAL_ACHIEVED = YES

## 25. Failure recovery

- Missing project scope -> stop before Project mutation; request one bounded auth refresh.
- Exact worktree unavailable -> stop before Project/Issue mutation.
- Clear Writing unavailable -> stop reader-facing copy mutation.
- GitHub workflow UI-only -> one minimal HUMAN_ONLY setup, then readback.
- ChatGPT Project instructions user-only -> one exact-text setup after main integration, then resume.
- Ambiguous TODO dedupe -> preserve separate tracking or return Planner; do not guess.
- Semantic main drift -> return Planner/Critic.
- Stale pending mutation -> do not apply; regenerate from current truth.
- Maintainer unavailable/not production-ready -> stay ADAPTING.
- New machine/credential/remote authority -> request only that exact bounded authorization at ADAPTING time.
- One consumer PASS -> never treat as aggregate DONE.

## 26. No new board/control-plane component

Do not create:

- standalone Kanban/board skill
- kanban-sync skill
- new plugin/profile
- board-specific MCP/service
- cross-machine controller
- machine registry/inventory service
- watcher/daemon
- central credential broker
- GitHub Action/database/ledger/controller
- new cross-machine state machine

## 27. Version / README

Repository bump decision: NONE.
Reason: this central task changes maintenance docs/contracts and GitHub Project metadata only.

Affected plugins: all NO_BUMP.
Reason: no plugin production source/runtime/package change.

README closure is mandatory.

Expected result: README checked: no update required, unless implementation creates a real public entry.

## 28. Completion statement

Central implementation may truthfully report:

CENTRAL_IMPLEMENTATION_COMPLETE = YES
PROJECT_STATUS = ADAPTING
OVERALL_GOAL_ACHIEVED = NO

Only final five-consumer closure may report:

FIVE_CONSUMER_AGGREGATE_VERIFIED = YES
RESOLUTION_COMMIT = <canonical closure commit>
TRACKING_ISSUE_CLOSED_COMPLETED = YES
PROJECT_STATUS = DONE
OVERALL_GOAL_ACHIEVED = YES

No earlier stage may claim overall completion.
