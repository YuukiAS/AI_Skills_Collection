# Slurm Workflows Routing Refactor — Critic Review v0.4

日期：2026-09-24  
角色：AI Research Stack Independent Critic  
审查阶段：ARCHITECTURE_REVIEW_V0_4

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_4_2026-09-24.md`
- proposal_commit: `bdc33f27df89c6facf9214ce14e43a7afb8097cf`
- previous_proposal: v0.3 @ `f9c0e3abbffaa6677c1f0acec510c47106d66aa1`
- previous_critic_review: v0.3 @ `9e63c443ab9204cbf7619b8f0fdd8a81effbafc2`
- review-start latest main: `38f6b9e407b0467c5adb35da4c0b854feec9dc07`
- execution branch/worktree: NOT_CREATED

Proposal commit -> review-start main drift is unrelated plugin/TODO/Lucerna evidence work; no relevant Slurm production or proposal semantic drift was found.

## Result

```text
RESULT = REVISE

SWR-ER-B2-A = CLOSED

SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED

SWR-PORT-B1 = OPEN
```

v0.4 successfully closes the only previously open authorization blocker. The one-time capacity-family enrollment is sufficiently bounded, avoids weekly repeat prompts, and does not turn a plain preference boolean into generic Slurm mutation authority.

However, the user's current clarification adds a new product requirement that directly matters to this open-source Skill:

> this is an open-source repository; Longleaf is only one current deployment. Other users may use their own Slurm clusters, and the same user may later use CUHK Central Cluster. Server names, partition names, GPU labels, hostnames, and similar site facts must not be hard-coded. The Skill should inspect the live Slurm site and derive what it can.

Current source still has a real portability gap: the installed environment path recognizes only committed `site-profiles/*.json` and refuses `environment apply` when no known profile is detected. The Skill text says “ask for or detect” site facts, but the architecture does not yet freeze a generic live-discovery path for an arbitrary Slurm cluster.

This is new direct user intent, so opening `SWR-PORT-B1` is not moving an old goalpost.

---

## Required source actually read

Latest main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- Proposal v0.4
- Proposal v0.3
- Critic review v0.3
- current `skills/tools/hpc/slurm-workflows/SKILL.md`
- relevant current `scripts/skills.py` environment detection/apply path
- current Longleaf/CUHK site profiles

No execution branch/worktree exists. No production source was modified in this review.

---

# SWR-ER-B2-A — CLOSED

v0.4 closes the previous authorization problem with the right amount of machinery.

The approved semantics are now:

```text
preference != authorization
```

A plain:

```text
auto_maintain_successor=true
```

is inert for mutations until the user explicitly enrolls the exact capacity family.

## Why the one-time enrollment is sufficiently bounded

The enrollment freezes:

- site;
- capacity-family identity;
- activation scope;
- accepted resource contract;
- allowed resource envelope;
- recurrence / target availability window;
- max intended successor = 1;
- successor-submit permission;
- optional lifecycle-owned stale-successor cancel/retarget permission.

Material changes invalidate the enrollment and require a new explicit authorization.

The current TOML stores only the current declarative authorization scope plus a digest used to detect scope mismatch. It is not an approval-history database, credential, signing system, append-only ledger, daemon, watcher, or state machine.

That is proportionate.

## Activation scope is correctly narrowed

v0.4 no longer says “any Slurm activity on this site reconciles every enrolled family.”

A family can be activated only by:

1. explicit current workload/Goal reference to that `capacity_family`; or
2. an enrollment that explicitly allows compatible-resource matching and a current resolved workload contract that actually matches the capacity family's resource/accelerator envelope.

Therefore a CPU-only AI_Skills_Collection or Bridge Kit maintenance task on Longleaf does not trigger an enrolled GPU capacity family merely because it happens on the same server.

This is the correct least-privilege trigger and does not require project-name blacklists.

## Site hard authority is preserved

Current Longleaf/CUHK profiles contain:

```text
do_not_submit_without_user_confirmation = true
```

v0.4 does not remove or weaken that value.

Its interpretation is now bounded:

- explicit one-time family enrollment = the user's confirmation for recurring same-scope maintenance;
- plain preference = not authorization;
- scope change = reauthorize;
- future stronger site/admin evidence requiring per-submission confirmation would override the enrollment.

No current repo/site source was found that gives the boolean the stronger meaning “every individual occurrence must always receive a fresh human prompt.”

Therefore this closes the earlier tension without creating a generic `scancel`/submit permission.

## G8 authority cases are sufficient

G8-A through G8-E correctly cover:

- enrolled same-scope recurring mutation;
- unenrolled read-only behavior;
- unrelated workload should-not-change behavior;
- material scope invalidation;
- stale/tampered enrollment fail-closed behavior.

No G9 is needed.

---

# Previously closed findings remain closed

## SWR-B1 = CLOSED
No regression to JobId/dependency/array/running-transition safety.

## SWR-B2 = CLOSED
No regression to duplicate-race site authority.

## SWR-ER-B1 = CLOSED
Sticky resource contract and hysteresis remain unchanged.

Carry forward the prior non-blocking implementation clarifications:

- OOM increase after rounding must actually exceed the current accepted memory;
- completed-job `sacct Comment` may be unavailable when site accounting does not store job comments;
- ambiguous historical matching cannot trigger automatic right-sizing.

## SWR-ER-B2 = CLOSED
The capacity lifecycle and its recurring mutation authority are now both architecturally complete.

## SWR-ER-B3 = CLOSED
Workload-mode routing and Bridge ownership remain unchanged.

```text
BRIDGE_CHANGE_REQUIRED = NO
```

---

# NEW BLOCKER — SWR-PORT-B1: generic open-source site discovery is not yet a production contract

## Requirement

`slurm-workflows` is an open-source generic Slurm Skill, not a Longleaf-specific tool with a CUHK exception.

Longleaf and CUHK may have public-safe site profiles, but a user on another Slurm cluster must not need the repository to already know their server, hostname, partition names, GPU partition names, account names, or node names.

The generic path must inspect the live scheduler for discoverable site facts and then combine those facts with optional site policy / local user configuration.

No server-specific partition or hostname may become a generic constant.

## Direct source / official evidence

Current production source does not yet meet that requirement.

### Current environment detection is registry-like

`scripts/skills.py::environment_detect_profile()` only compares the local hostname/path with committed profiles from `site-profiles/*.json`.

If `--site` is explicitly supplied but is not already in those profiles:

```text
unknown site profile: <site>
```

If automatic detection finds no known profile, `environment_apply_plan()` ultimately stops with:

```text
no site profile detected; rerun with --site
```

But `--site` itself must name an existing committed profile.

So the real environment/materialization path is currently not portable to an arbitrary Slurm installation without adding repository source.

### Current Skill prose is weaker than a production discovery contract

`SKILL.md` says that if no site profile is installed, it should “ask for or detect” minimum site facts.

That is directionally correct, but the architecture does not define which facts must be live-discovered, which command is authoritative, how discovery degrades under site privacy restrictions, or how a generated/local site reference is produced for an unknown cluster.

### SchedMD already exposes appropriate read-only discovery sources

Official Slurm documentation confirms that generic discovery is feasible without knowing site names in advance:

- `sinfo` reports partitions, nodes, partition availability, CPU counts, memory, GRES, features, time limits and default partition information.
- `scontrol show partition` reports detailed live partition configuration such as MaxTime, allowed accounts/QOS, priority tier, node sets and memory limits, subject to site `PrivateData` restrictions.
- `scontrol show config` exposes live controller configuration such as scheduler type and other site configuration.
- `sacctmgr show assoc` can expose the current user's account/partition/QOS associations when SlurmDBD/site permissions allow it.

Sources:

- https://slurm.schedmd.com/sinfo.html
- https://slurm.schedmd.com/scontrol.html
- https://slurm.schedmd.com/quickstart.html
- https://slurm.schedmd.com/sacctmgr.html

## Causal user-visible risk

Without an explicit live-discovery path:

1. the open-source Skill can still accidentally become “Longleaf + CUHK profiles with generic wording” rather than a real generic Slurm capability;
2. a third-party user can have a perfectly normal Slurm cluster yet fail environment apply because their site is not in the repository;
3. future CUHK/other-cluster use encourages adding more committed site/partition constants instead of inspecting the scheduler;
4. routing/resource logic can be driven by stale documentation or remembered partition names instead of current scheduler state;
5. renamed/new partitions or changed GPU features can silently make old configuration wrong.

This directly contradicts the current user requirement.

## Minimum closure condition

Do not build another discovery service or central cluster registry.

The next Proposal revision only needs to freeze a small **generic live-site discovery contract**.

At minimum:

### 1. Committed site profiles become optional policy overlays, not the supported-site registry

Known profiles may continue to provide:

- public hard policy;
- safe site detection hints;
- explicit restrictions that cannot be inferred from Slurm;
- documentation/default safety behavior.

But absence of a committed profile must not make the generic Skill unusable.

### 2. Unknown/current site can produce a local runtime site context

When Slurm is reachable and no known profile exists, the normal entry should create/refresh a user-local/generated runtime site context from read-only scheduler inspection.

It must not require committing a new JSON profile merely to use the Skill.

A stable local site identity may be derived from live Slurm cluster identity when safely available, or explicitly assigned locally. It must not require hard-coded hostnames.

### 3. Discover what Slurm can actually report

Use live read-only evidence where available, for example:

- visible/default partitions and partition state: `sinfo`;
- partition time/resource/features/GRES constraints: `sinfo` and/or `scontrol show partition`;
- scheduler/config capability relevant to behavior: `scontrol show config`;
- user account/QOS association: `sacctmgr show assoc user=$USER` or equivalent when permitted;
- live job/accounting information from existing approved read-only Slurm commands.

Do not hard-code `htzhulab`, `a100`, H100, CUHK partition names, Longleaf hostnames, or another user's site names into generic source.

Those values may appear only in site-specific local config, public profile examples/tests, or live-discovered evidence.

### 4. Fail closed when a site hides information

SchedMD allows sites to restrict some `scontrol`/accounting information through `PrivateData` or database permissions.

If a fact cannot be safely discovered:

- do not guess;
- use an explicit user/local override or site documentation;
- treat unknown hard authority conservatively.

For example, unknown duplicate-race authority remains disabled.

### 5. Site-specific preference still belongs locally

Live discovery answers “what exists / what is legal or visible.”

It does **not** invent the user's preference.

A Longleaf user may locally prefer one discovered partition over another; a CUHK or third-party user may choose different preferences.

### 6. Gate coverage

Do not add a new gate unless necessary.

This belongs naturally inside existing G1/G6:

- G1 should prove no site/partition leakage and generic unknown-site discovery/overlay separation;
- G6 should prove the installed normal entry can operate on a Slurm site that has no committed repository profile by consuming a live/local generated site context.

A deterministic fake Slurm fixture can prove most of this without a real third-party cluster.

## Scope discipline

This blocker does **not** require:

- a cloud server inventory;
- a central registry of universities;
- scraping cluster documentation automatically;
- SSH host management;
- daemon/watcher;
- administrator access;
- automatic account/QOS mutation;
- storing raw hostnames/partitions in public repo state.

The architecture should remain small.

---

# Complexity assessment

With the portability amendment, the architecture can remain:

```text
live Slurm discovery
+ optional public site hard-policy overlay
+ user-local site facts/preferences

-> workload intent
-> sticky resource contract
-> capacity lifecycle
-> routing / widening / fail closed
```

This is not a new control plane.

The important ownership distinction is:

```text
live scheduler facts != site hard policy != user preference
```

That distinction should be explicit in the next proposal.

---

# Version / execution status

Architecture docs: NO BUMP.

Future release direction remains:

- `slurm-workflows 0.1 -> 0.2`;
- repository next PATCH from actual release-time `VERSION`;
- central plugins all NO_BUMP;
- Bridge Kit NO CHANGE.

No execution branch/worktree may be created yet.

This is still architecture review, not execution-ready review.

---

## Final fields

```text
RESULT = REVISE

SWR-ER-B2-A = CLOSED

SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED

SWR-PORT-B1 = OPEN

PASS_OBJECT = NOT_APPLICABLE
PASS_SCOPE = NOT_APPLICABLE

PROPOSAL_COMMIT = bdc33f27df89c6facf9214ce14e43a7afb8097cf
BRIDGE_CHANGE_REQUIRED = NO
EXECUTION_READY_REVIEW = NOT_REQUESTED
```
