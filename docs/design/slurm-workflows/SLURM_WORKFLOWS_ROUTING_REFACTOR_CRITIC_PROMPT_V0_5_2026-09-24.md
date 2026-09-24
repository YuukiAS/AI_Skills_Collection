# Slurm Workflows Routing Refactor — Critic Prompt v0.5

你继续作为 AI Research Stack 的独立 Critic。

这是同一个 task key 的 architecture re-review v0.5。

不是 execution-ready review。
不要重新打开已经关闭的 finding，除非 v0.5 自己直接回归了对应语义。

## Active Review Context

Target repository:

`YuukiAS/AI_Skills_Collection`

Target:

standalone Skill / HPC / `slurm-workflows`

Design topic / task key:

`hpc--slurm-workflows-routing-refactor`

Review stage:

`ARCHITECTURE_REVIEW_V0_5`

Proposal v0.5:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_5_2026-09-24.md`

Proposal commit:

`376d03f0d1f9cde2e425bdba62e53942ec5063c6`

Previous Proposal v0.4:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_4_2026-09-24.md`

v0.4 commit:

`bdc33f27df89c6facf9214ce14e43a7afb8097cf`

Previous Critic review v0.4:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_4_2026-09-24.md`

Critic review commit:

`14b885b8c272de4c0f2c1b66d8c792d6bed060cc`

Stable finding state before this review:

```text
SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2-A = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED
SWR-PORT-B1 = OPEN
```

The first and only open blocker to recheck is:

`SWR-PORT-B1 — generic open-source live-site discovery`

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

- Proposal v0.5;
- Proposal v0.4;
- Critic review v0.4.

Read only the necessary current production source needed to verify portability:

- `skills/tools/hpc/slurm-workflows/SKILL.md`
- relevant `scripts/skills.py` environment detect/plan/apply/doctor paths
- current site profiles/local override docs/tests as needed.

Do not convert this into an execution-ready review.

## 2. Recheck SWR-PORT-B1 first

Planner disposition:

`ACCEPT`

v0.5 now freezes:

> live Slurm facts are the generic runtime base; committed site profiles are optional hard-policy overlays, not a supported-server registry.

Please determine whether this closes the portability blocker without creating a new control plane.

## 3. Site profile role

v0.5 states:

`site-profiles/*.json`

is:

- optional public-safe hard-policy overlay;
- optional safe detection hints;
- place for documented policy not inferable from scheduler state.

It is NOT:

- the list of supported Slurm servers;
- a central university/cluster registry.

Absence of a committed profile must no longer block generic Slurm usage.

Check whether this distinction is clear enough to guide implementation and user-facing docs.

## 4. local_site_id vs policy_overlay_id

v0.5 separates:

### local_site_id

stable user-local identity for the actual Slurm deployment, used by:

- local overrides;
- workload/resource contracts;
- persistent capacity enrollment;
- runtime site context.

### policy_overlay_id

optional committed public profile identity.

Known Longleaf/CUHK deployments may use both.
A third-party cluster may have local_site_id but no policy_overlay_id.

Identity preference:

1. existing user-local id;
2. safely readable Slurm ClusterName;
3. one-time locally chosen id if ClusterName is unavailable/ambiguous.

Hostname is not the generic canonical identity.

Check whether this is portable and sufficiently stable without requiring a hostname registry.

## 5. Generic live discovery contract

v0.5 defines one bounded read-only discovery round per normal routing/planning invocation.

### sinfo

Discover user-visible:

- partition/default partition;
- availability/state;
- CPUs;
- memory;
- GRES;
- features;
- time limits;
- priority tier where exposed.

Do not use `--all` to expand beyond normal visibility.

### scontrol show partition

When readable, discover:

- State/Default;
- MaxTime/DefaultTime;
- node bounds;
- memory/TRES;
- Allow/Deny Accounts;
- Allow/Deny QOS;
- PriorityTier/PriorityJobFactor;
- ReqResv;
- relevant partition resource facts.

Do not treat partition-level AllowAccounts/AllowQOS as proof that the current user has a valid association.

### scontrol show config

Select only relevant fields such as:

- ClusterName;
- SelectType / SelectTypeParameters;
- SchedulerType / relevant SchedulerParameters;
- PriorityType / PriorityFlags;
- PrivateData;
- accounting capability/type indicators.

Do not propagate unrelated private controller/database host/path values into public artifacts.

### sacctmgr show assoc user=$USER

Optional only when SlurmDBD/site permissions allow.

May discover:

- Cluster;
- Account;
- Partition;
- QOS / DefaultQOS;
- directly relevant limits.

Failure/unavailability means UNKNOWN, not environment failure.

No account/QOS mutation is allowed.

Please independently assess whether these are mature Slurm-native read-only sources and whether the bounded set is sufficient without overcollecting.

## 6. Fact provenance and fail-closed behavior

v0.5 requires facts to be tagged conceptually as:

```text
LIVE_KNOWN
LOCAL_EXPLICIT
PROFILE_POLICY
UNKNOWN
```

UNKNOWN must not be filled with generic defaults.

Examples:

- scontrol detail hidden -> detail remains UNKNOWN;
- no SlurmDBD / sacctmgr access -> account/QOS association UNKNOWN;
- unknown duplicate-race authority -> duplicate race disabled;
- local override may supply missing account/QOS/preference;
- local preference may not weaken public hard policy.

Check whether this gives sufficient fail-closed behavior on PrivateData/private clusters.

## 7. Runtime SiteContext and public/private boundary

v0.5 deliberately does NOT add a site database.

Current scheduler facts are generated in-memory from live CLI each normal invocation.

Existing:

`references/_generated/site-profile.md`

remains only a generated locator/public-policy summary, not the canonical current scheduler-facts database.

It may contain:

- local_site_id;
- optional policy_overlay_id/revision;
- local override locator;
- public-safe hard-policy summary;
- discovery availability/ownership explanation.

It must not automatically materialize private:

- hostname;
- account;
- private path;
- controller/db host;
- private QOS;

into tracked project source.

Check whether this is simpler and safer than creating a persistent site inventory/cache.

## 8. Environment CLI portability

v0.5 changes future semantics:

### environment detect

Should report conceptually:

- local_site_id;
- scheduler availability;
- live discovery availability;
- optional policy_overlay_id;
- matched overlays.

### explicit --site

Backward-compatible:

- if it matches a known profile, that profile can still attach;
- if it does not match a committed profile, treat it as a local site id rather than erroring.

### no-profile + live Slurm

Must enter generic live mode rather than fail.

### no live scheduler

Must not pretend routing is ready.

Please check whether this is sufficient to repair the current registry-like environment path.

## 9. FACT != POLICY != PREFERENCE

v0.5 explicitly freezes:

```text
live scheduler facts
!=
site hard policy
!=
user/project preference
```

For example:

`sinfo` discovering p1/p2/gpu-x does NOT create a preference order.

`PriorityTier` is scheduler fact, not user preference.

A Longleaf user may locally rank its discovered partitions.
A CUHK/third-party user may rank different partitions.

Check whether merge precedence is correct:

1. live facts;
2. optional hard-policy overlay;
3. local explicit missing facts;
4. workload/project preferences.

Hard policy may restrict live facts but cannot invent a live route.
Local preference cannot widen hard policy.

## 10. Hard-coding rule

Generic production source must not contain deployment-specific routing constants such as:

- htzhulab;
- a100 used as a Longleaf route constant;
- Longleaf hostname;
- CUHK partition names;
- specific H100 route names;
- compute-node names;
- another site's account/QOS/partition constants.

Such values are allowed only in:

- user-local config;
- optional site-specific profile;
- tests/fixtures;
- clearly non-default examples;
- live discovery evidence.

Generic code may parse arbitrary GRES/GPU type strings but cannot hard-code type -> partition mapping.

Check whether this rule is strong enough without incorrectly banning generic hardware vocabulary.

## 11. Existing architecture must remain closed

v0.5 does NOT redesign:

- sticky resource contract / G7 hysteresis;
- persistent capacity lifecycle;
- one-time family enrollment / G8 authority;
- batch/persistent/debug workload modes;
- JobId/dependency safety;
- duplicate-race authority;
- Bridge ownership.

The only portability-related adjustment is that workload/capacity/enrollment site binding now uses local_site_id rather than requiring a committed profile id.

Keep these CLOSED unless v0.5 directly regresses them:

```text
SWR-B1
SWR-B2
SWR-ER-B1
SWR-ER-B2-A
SWR-ER-B2
SWR-ER-B3
```

## 12. Generic safety baseline on unknown policy

No profile does not mean “everything allowed”.

v0.5 proposes:

- ordinary user-owned submission requires current task authorization or a valid enrolled capacity-family authorization;
- account/QOS/resources are never guessed;
- duplicate race is disabled when site authority is unknown;
- admin-level actions remain prohibited;
- site hard policy, when known, can make the generic baseline stricter.

Check whether this is conservative enough while still allowing generic Slurm usage.

## 13. G1 / G6 only — no G9

Do not add G9.

G2-G5, G7, G8 remain as previously accepted.

### G1 extension

Must prove:

- no deployment partition leakage;
- a fake third-party Slurm site with no committed profile can derive/accept local_site_id;
- live CLI facts form a valid SiteContext;
- environment plan/apply does not require repo profile;
- hidden/unavailable facts remain UNKNOWN/fail-closed;
- optional policy overlay remains stricter authority rather than current-fact source;
- profile list is not a support matrix.

### G6 extension

Final installed normal entry must demonstrate:

```text
no committed profile
+ fake live Slurm CLI
+ local site id / local override
-> environment materialization
-> installed slurm-workflows
-> runtime discovery
-> resolved SiteContext
-> local preference
-> normal routing plan
```

Use deterministic fake Slurm CLI fixtures.
No real third-university mutation is required.

Check whether this is sufficient proof of open-source portability.

## 14. Complexity check

v0.5 must remain:

```text
read-only live discovery
+ optional public policy overlay
+ local override/preferences
```

It must NOT become:

- central cluster registry;
- cloud/server inventory service;
- SSH manager;
- automatic university-doc scraper;
- queue-history DB;
- custom scheduler;
- daemon/watcher;
- administrator path;
- automatic account/QOS mutation;
- hard-coded node-ranking system.

If you think the proposed SiteContext is becoming a hidden inventory/state service, identify direct evidence and the smallest simplification.

## 15. Independent official SchedMD check required

Independently verify current official SchedMD docs for:

- `sinfo` visible partitions/resources/features/GRES/time limits/default partition behavior;
- `scontrol show partition`;
- `scontrol show config`;
- `PrivateData` restrictions on show commands;
- `ClusterName`;
- `sacctmgr show assoc` / SlurmDBD dependency and association fields.

Confirm or correct Planner's interpretation.

Prefer:

- https://slurm.schedmd.com/sinfo.html
- https://slurm.schedmd.com/scontrol.html
- https://slurm.schedmd.com/slurm.conf.html
- https://slurm.schedmd.com/sacctmgr.html
- https://slurm.schedmd.com/quickstart.html

## 16. Result

Return:

`RESULT = PASS`

or

`RESULT = REVISE`

First state:

`SWR-PORT-B1 = CLOSED | OPEN`

Then state the full stable finding set:

```text
SWR-B1 =
SWR-B2 =
SWR-ER-B1 =
SWR-ER-B2-A =
SWR-ER-B2 =
SWR-ER-B3 =
SWR-PORT-B1 =
```

If REVISE, each blocker must include:

- requirement;
- direct source/official evidence;
- concrete user-visible portability or safety risk;
- minimum closure condition.

Do not perform execution-ready review.

If PASS:

```text
PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_5

PASS_SCOPE =
amended architecture/design only; no execution authorization
```

## 17. Review record

You are authorized only to write:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_5_2026-09-24.md`

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
SWR-PORT-B1 =
SWR-B1 =
SWR-B2 =
SWR-ER-B1 =
SWR-ER-B2-A =
SWR-ER-B2 =
SWR-ER-B3 =
REVIEW_PATH =
REVIEW_COMMIT =
PROPOSAL_COMMIT = 376d03f0d1f9cde2e425bdba62e53942ec5063c6
BRIDGE_CHANGE_REQUIRED = NO
EXECUTION_READY_REVIEW = NOT_REQUESTED
```
