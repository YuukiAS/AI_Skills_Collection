# Slurm Workflows Routing Refactor — Critic Review v0.6

日期：2026-09-24  
角色：AI Research Stack Independent Critic  
审查阶段：ARCHITECTURE_REVIEW_V0_6

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md`
- proposal_commit: `ad3e60988f5581dd0d0c194e13907baaa446c413`
- previous_proposal: v0.5 @ `376d03f0d1f9cde2e425bdba62e53942ec5063c6`
- previous_critic_review: v0.5 @ `3a5d7dec1bd0eeda20ed22b42a0d5cdbdb499377`
- review_stage: `ARCHITECTURE_REVIEW_V0_6`
- execution branch/worktree: NOT_CREATED

Proposal commit -> review-start latest main contains only the v0.6 Critic prompt as related drift. No relevant production/proposal semantic drift was found.

## Result

```text
RESULT = PASS

SWR-VER-B1 = CLOSED

SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2-A = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED
SWR-PORT-B1 = CLOSED
```

```text
PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6

PASS_SCOPE =
amended architecture/design + release direction only; no execution authorization
```

This PASS approves only Proposal v0.6 architecture/design and its release-class decision. It does not authorize production edits, creation of the reviewed branch/worktree, real Slurm mutation, version bump, Executor start, Bridge Kit modification, or release.

---

## SWR-VER-B1 — CLOSED

The v0.6 release direction now matches the repository's canonical version policy.

Current source confirms `VERSION = 5.1.0`.

The current production environment path still requires a known committed site profile for successful environment apply. The approved v0.6 capability changes the shared collection-level environment/install path so that:

```text
third-party Slurm site
+ no committed site profile
+ live Slurm discovery
-> environment detect / plan / apply / doctor
-> installed normal slurm-workflows
```

The current Versioning Policy explicitly reserves repository MINOR for a new repository-level user capability and specifically includes a new install/environment/distribution capability that enables a normal scenario the collection previously could not support.

Therefore the approved release direction is:

```text
Architecture/design docs:
NO BUMP

If the complete approved capability ships:
Repository bump decision: MINOR

Current baseline if unchanged:
5.1.0 -> 5.2.0

If VERSION changes before release:
compute the next MINOR from the actual release-time VERSION

Standalone:
slurm-workflows 0.1 -> 0.2

Central Plugins:
all NO_BUMP

Bridge Kit:
NO CHANGE
```

No new version infrastructure is needed.

---

## Previously closed architecture remains closed

v0.6 does not regress the accepted v0.5 architecture.

### SWR-B1 = CLOSED

Pending widening still preserves the approved JobId/dependency/array/running-transition safety contract.

### SWR-B2 = CLOSED

Duplicate-job race still requires explicit site authority plus user/local opt-in.

### SWR-ER-B1 = CLOSED

Sticky resource contracts, comparable workload families and hysteresis remain unchanged.

CPU remains stable-first rather than becoming a generic autotuner. GPU count/type remains a workload contract and cannot be silently downgraded for scheduling convenience.

### SWR-ER-B2-A = CLOSED

One-time bounded capacity-family enrollment still separates preference from durable same-scope mutation authorization.

### SWR-ER-B2 = CLOSED

Persistent capacity lifecycle, one-active/one-successor reconciliation, BEST_EFFORT calendar availability and bounded recurring successor maintenance remain intact.

### SWR-ER-B3 = CLOSED

Batch / persistent allocation / debug interactive workload modes remain intact.

```text
BRIDGE_CHANGE_REQUIRED = NO
```

### SWR-PORT-B1 = CLOSED

The open-source portability contract remains intact:

- live Slurm facts are the generic runtime base;
- committed profiles are optional public hard-policy overlays, not a supported-server registry;
- `local_site_id` is independent of optional `policy_overlay_id`;
- no-profile third-party Slurm sites can use the normal environment/install path;
- deployment-specific partition/hostname/GPU-route constants do not belong in generic production source;
- G1/G6 cover no-profile installed normal-entry behavior.

---

## Local Longleaf accelerator preference clarification

The new Longleaf preference note does not conflict with portability or resource-contract architecture.

It is correctly modeled as local preference semantics:

1. an explicitly preferred PI-owned partition may rank first;
2. among remaining live-discovered legal GPU routes, local preference may rank accelerator classes such as newer accelerator > older accelerator;
3. exact Longleaf partition names and GPU-to-partition mappings remain local/live;
4. a hard workload accelerator requirement cannot be downgraded merely because a lower class queues faster.

This is a representative local policy, not a generic source default and not a new architecture finding.

---

## Carry-forward implementation notes

These remain non-blocking and should be preserved when the execution package is regenerated:

- prefer explicit `sinfo -o/-O` field whitelists for the generic discovery minimum;
- raw `sinfo --json/--yaml` should not be treated as automatically privacy-minimal;
- never persist raw discovery dumps into tracked project source;
- bound controller RPCs to the minimum required to form current SiteContext;
- if ClusterName/private site identity is unsuitable for tracked output, use a safe local alias;
- OOM memory increase after rounding must be strictly greater than the current accepted request;
- unavailable `sacct Comment` requires conservative family matching;
- local partition/accelerator preference comes from live/local context, not generic constants.

SchedMD current documentation was independently rechecked for this review. `sinfo` remains the normal user command for partition/node discovery, exposes explicit field formatting, and warns against repeated controller RPCs in loops. No new Slurm semantic introduced by v0.6 contradicts the already-approved architecture.

---

## Complexity assessment

v0.6 adds no new Slurm mechanism, gate, config system, service, watcher, registry, scheduler, Bridge capability or version infrastructure.

The architecture remains proportionate:

```text
live Slurm discovery
+ optional public policy overlay
+ local facts/preferences
-> workload mode
-> sticky resource contract
-> reusable capacity lifecycle
-> safe routing
```

No further architecture revision is required before Planner regenerates the execution package.

---

## Final fields

```text
RESULT = PASS

SWR-VER-B1 = CLOSED

SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2-A = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED
SWR-PORT-B1 = CLOSED

PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6

PASS_SCOPE =
amended architecture/design + release direction only; no execution authorization

PROPOSAL_COMMIT = ad3e60988f5581dd0d0c194e13907baaa446c413
REPOSITORY_RELEASE_CLASS = MINOR
STANDALONE_SLURM_WORKFLOWS_RELEASE = 0.1 -> 0.2
CENTRAL_PLUGIN_BUMPS = NONE
BRIDGE_CHANGE_REQUIRED = NO
EXECUTION_READY_REVIEW = NOT_REQUESTED
```
