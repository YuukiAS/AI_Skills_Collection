# Slurm Workflows Routing Refactor — Critic Prompt v0.6

你继续作为 AI Research Stack 的独立 Critic。

这是同一个 task key 的 architecture re-review v0.6。

不是 execution-ready review。
不要重新打开已经关闭的 finding，除非 v0.6 自己直接回归了对应语义。

## Active Review Context

Target repository:

`YuukiAS/AI_Skills_Collection`

Target:

standalone Skill / HPC / `slurm-workflows`

Design topic / task key:

`hpc--slurm-workflows-routing-refactor`

Review stage:

`ARCHITECTURE_REVIEW_V0_6`

Proposal v0.6:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md`

Proposal commit:

`ad3e60988f5581dd0d0c194e13907baaa446c413`

Previous Proposal v0.5:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_5_2026-09-24.md`

v0.5 commit:

`376d03f0d1f9cde2e425bdba62e53942ec5063c6`

Previous Critic review v0.5:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_5_2026-09-24.md`

Critic review commit:

`3a5d7dec1bd0eeda20ed22b42a0d5cdbdb499377`

Stable finding state before this review:

```text
SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2-A = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED
SWR-PORT-B1 = CLOSED
SWR-VER-B1 = OPEN
```

The first and only open blocker to recheck is:

`SWR-VER-B1 — repository release direction`

Future execution locators remain NOT_CREATED:

```text
branch:
reviewed/hpc--slurm-workflows-routing-refactor

worktree:
/tmp/ai-skills-hpc-slurm-workflows-routing-refactor
```

## 1. Required read

First actually read current latest main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

Then read:

- Proposal v0.6;
- Proposal v0.5;
- Critic review v0.5;
- current `VERSION`.

Read current Slurm production source only if needed to verify the version-class premise.

Do not perform execution-ready review.

## 2. Recheck SWR-VER-B1 first

Planner disposition:

`ACCEPT`

v0.6 now states:

### architecture/design docs themselves

No version bump.

### if the complete approved capability ships

Repository bump decision:

`MINOR`

Reason:

The collection's shared environment/install path gains a normal scenario that current production cannot support:

```text
third-party Slurm site
+ no committed site profile
+ live Slurm discovery
-> environment detect / plan / apply / doctor
-> installed normal slurm-workflows
```

Current production source instead requires a committed site profile for environment apply.

If release-time VERSION remains:

`5.1.0`

then release:

`5.1.0 -> 5.2.0`

If VERSION changes before release:

compute the next MINOR from the actual release-time VERSION.

Examples:

`5.1.4 -> 5.2.0`

`5.2.3 -> 5.3.0`

Standalone Skill:

`slurm-workflows 0.1 -> 0.2`

only after implementation + same-final-candidate gates + final review.

Central Plugins:

all `NO_BUMP`

Bridge Kit:

`NO CHANGE`

No new version infrastructure.

Please decide:

`SWR-VER-B1 = CLOSED | OPEN`

## 3. Version policy check

Use the current canonical:

`docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

Check whether the full v0.6 capability fits repository MINOR because it adds a repository-level install/environment scenario that the current collection cannot normally support.

Do not classify it by file count, test count, or Slurm Skill version alone.

If current source already supports no-profile generic Slurm environment apply in the normal path, identify direct evidence before rejecting MINOR.

## 4. Keep all approved Slurm architecture closed

v0.6 explicitly preserves v0.5:

- live Slurm facts as generic runtime base;
- optional public hard-policy overlays;
- local_site_id / policy_overlay_id separation;
- unknown no-profile Slurm site plan/apply;
- fact != policy != preference;
- no deployment-specific generic constants;
- sticky resource contracts / G7;
- workload batch/persistent/debug modes;
- persistent capacity lifecycle;
- one-time family enrollment / G8;
- JobId/dependency safety;
- duplicate-race authority;
- Bridge Kit NO CHANGE;
- G1/G6 portability extensions.

Keep these findings CLOSED unless v0.6 itself directly regresses them:

```text
SWR-B1
SWR-B2
SWR-ER-B1
SWR-ER-B2-A
SWR-ER-B2
SWR-ER-B3
SWR-PORT-B1
```

## 5. Non-blocking local preference clarification

The user additionally clarified a current Longleaf preference.

v0.6 records it only as local preference semantics:

- an explicitly preferred PI-owned partition can be highest priority;
- among remaining live-discovered legal GPU routes, a user-local accelerator preference can rank classes such as newer accelerator > older accelerator;
- exact Longleaf partition names and GPU-route mappings remain local/live, never generic production constants;
- if accelerator type is a hard workload requirement rather than a preference/equivalence class, routing cannot downgrade it.

This should remain a non-blocking implementation clarification under already-approved local-preference semantics.

Do not create a new architecture blocker merely because the user's local Longleaf ranking exists.

If you find that this sentence materially conflicts with the already-closed portability/resource/routing architecture, identify the exact regression; otherwise keep it non-blocking.

## 6. Carry-forward implementation notes

These remain NON_BLOCKING for architecture:

- prefer explicit `sinfo -o/-O` field whitelists;
- raw `sinfo --json/--yaml` is not automatically privacy-minimal;
- raw discovery dumps never persist into tracked project source;
- bound controller RPCs to the minimum needed;
- OOM increase after rounding must exceed current accepted memory;
- unavailable `sacct Comment` -> conservative family matching;
- local partition/accelerator preference comes from local config/live facts, not generic defaults.

Do not reopen architecture for these implementation details.

## 7. Scope / complexity

v0.6 does not add:

- new Slurm mechanism;
- new gate;
- new config system;
- new scheduler service;
- daemon/watcher;
- central server registry;
- new version infrastructure;
- Bridge Kit change.

It only corrects the release class and carries one local-preference clarification.

If you find another blocker, it must be caused by a direct v0.6 regression or a newly discovered release-contract contradiction.

## 8. Result

Return:

`RESULT = PASS`

or

`RESULT = REVISE`

First state:

`SWR-VER-B1 = CLOSED | OPEN`

Then state the full finding set:

```text
SWR-B1 =
SWR-B2 =
SWR-ER-B1 =
SWR-ER-B2-A =
SWR-ER-B2 =
SWR-ER-B3 =
SWR-PORT-B1 =
SWR-VER-B1 =
```

If REVISE, every blocker must include:

- requirement;
- direct source evidence;
- concrete release/user risk;
- minimum closure condition.

Do not perform execution-ready review.

If PASS:

```text
PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6

PASS_SCOPE =
amended architecture/design + release direction only; no execution authorization
```

## 9. Review record

You are authorized only to write:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_6_2026-09-24.md`

to current main.

Commit + ordinary non-force push only that review document.

Do NOT:

- modify production source/tests;
- update execution package yet;
- create execution branch/worktree;
- execute real Slurm mutation;
- modify Bridge Kit;
- bump version;
- start Executor;
- call paid API.

Finally report:

```text
RESULT =
SWR-VER-B1 =
SWR-B1 =
SWR-B2 =
SWR-ER-B1 =
SWR-ER-B2-A =
SWR-ER-B2 =
SWR-ER-B3 =
SWR-PORT-B1 =
REVIEW_PATH =
REVIEW_COMMIT =
PROPOSAL_COMMIT = ad3e60988f5581dd0d0c194e13907baaa446c413
REPOSITORY_RELEASE_CLASS = MINOR | OTHER
STANDALONE_SLURM_WORKFLOWS_RELEASE = 0.1 -> 0.2 | OTHER
CENTRAL_PLUGIN_BUMPS = NONE | OTHER
BRIDGE_CHANGE_REQUIRED = NO
EXECUTION_READY_REVIEW = NOT_REQUESTED
```
