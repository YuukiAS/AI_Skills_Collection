# Slurm Workflows Routing Refactor — Critic Review v0.5

日期：2026-09-24  
角色：AI Research Stack Independent Critic  
审查阶段：ARCHITECTURE_REVIEW_V0_5

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_5_2026-09-24.md`
- proposal_commit: `376d03f0d1f9cde2e425bdba62e53942ec5063c6`
- previous_proposal: v0.4 @ `bdc33f27df89c6facf9214ce14e43a7afb8097cf`
- previous_critic_review: v0.4 @ `14b885b8c272de4c0f2c1b66d8c792d6bed060cc`
- execution branch/worktree: NOT_CREATED

Proposal commit -> review-start latest main contains only unrelated Project Thread Handoff package work plus the v0.5 Critic prompt. No relevant Slurm production/proposal semantic drift was found.

## Result

```text
RESULT = REVISE

SWR-PORT-B1 = CLOSED

SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2-A = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED

SWR-VER-B1 = OPEN
```

v0.5 closes the open-source portability blocker. The architecture is now genuinely generic Slurm-first rather than “Longleaf/CUHK profiles with generic wording.”

The remaining blocker is not Slurm architecture. It is the release-version decision introduced by this amendment: v0.5 now creates a repository-level environment capability that the current Versioning Policy explicitly classifies as a possible MINOR, while Proposal §22 still freezes repository “next PATCH.”

That mismatch must be corrected before the architecture object can receive PASS.

---

## Required source actually read

Latest main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- Proposal v0.5
- Proposal v0.4
- Critic review v0.4
- current `skills/tools/hpc/slurm-workflows/SKILL.md`
- current `scripts/skills.py` environment detect/plan/apply path
- current local override docs/tests needed to assess portability

Current repository `VERSION` at review time: `5.1.0`.

No execution branch/worktree exists. No production source/test/site profile was modified by this review.

---

# SWR-PORT-B1 — CLOSED

## 1. Site profile role is now correct

v0.5 cleanly separates:

```text
live scheduler facts
!=
optional site hard-policy overlay
!=
user/project preference
```

`site-profiles/*.json` is now explicitly an optional public-policy overlay/detection-hint layer, not the supported-server registry.

That directly fixes the previous product-boundary problem.

A third-party Slurm deployment can have:

- a local runtime identity;
- live-discovered scheduler facts;
- user-local missing facts/preferences;

without adding a committed repository profile.

Longleaf/CUHK remain useful deployment examples and policy overlays, not product eligibility gates.

## 2. local_site_id / policy_overlay_id split is sufficient

The identity model is portable:

- existing local stable id first;
- otherwise safely readable Slurm `ClusterName` as a candidate;
- otherwise one-time locally chosen id;
- hostname is not the generic canonical identity.

This is enough to avoid a hostname registry.

A policy overlay may still use public-safe detection hints, but those hints do not determine whether the generic Skill supports a site.

## 3. Live discovery sources are appropriate and mature

Independent SchedMD review confirms the main sources selected by v0.5.

### sinfo

Official `sinfo` exposes partition/default-partition, availability, CPU counts, node memory, features, GRES, default/max time limits and partition priority fields. By default, hidden partitions and partitions unavailable to the user's group are not shown; `--all` expands visibility. v0.5 correctly refuses to use `--all` for generic discovery.

This is the right generic first-line discovery source.

### scontrol show partition

Official `scontrol show partition` exposes fields including:

- Allow/Deny Accounts;
- Allow/Deny QOS;
- Default;
- DefaultTime / MaxTime;
- node bounds;
- PriorityJobFactor / PriorityTier;
- ReqResv;
- PreemptMode;
- Def/Max memory;
- TRES.

SchedMD also documents that `scontrol show` commands are available to users by default, but when `PrivateData` restrictions apply, `show partition` may require privileged access.

v0.5 already handles this correctly:

> unreadable detailed partition facts -> UNKNOWN; do not fail the whole environment; do not escalate privileges.

### scontrol show config

Using only selected fields such as:

- ClusterName;
- SelectType / SelectTypeParameters;
- SchedulerType / relevant SchedulerParameters;
- PriorityType / PriorityFlags;
- PrivateData;
- accounting capability indicators

is reasonable.

v0.5 also correctly forbids propagating unrelated controller/database hostnames/paths to public tracked artifacts.

### sacctmgr show assoc

SchedMD's accounting model defines user associations by cluster/account/user and optional partition, and exposes account/cluster/QOS/default-QOS fields through association queries.

The query depends on Slurm accounting/SlurmDBD/site permissions, so v0.5 correctly treats it as optional:

> unavailable -> UNKNOWN, not environment failure.

No account/QOS mutation is introduced.

## 4. Fact provenance and PrivateData handling are sufficient

The provenance classes:

```text
LIVE_KNOWN
LOCAL_EXPLICIT
PROFILE_POLICY
UNKNOWN
```

are enough.

The key safety behavior is correct:

- missing live fact is not filled with a generic constant;
- local explicit data may fill a missing fact;
- local preference cannot relax known hard policy;
- unknown duplicate-race authority stays disabled;
- administrator-level capabilities never appear merely because discovery succeeded.

No extra site database or authority state machine is needed.

## 5. Environment CLI portability closes the real production gap

Current source still proves the old defect:

- explicit `--site` currently rejects unknown ids;
- no matched profile currently leaves `site_id=None`;
- `environment_apply_plan()` currently refuses no-profile apply.

v0.5 explicitly changes those semantics so that:

```text
no committed profile
+ usable live Slurm
-> GENERIC_LIVE_SLURM
-> local_site_id
-> plan/apply
-> installed slurm-workflows
-> live SiteContext
```

That is the correct normal-entry fix.

Unknown `--site <id>` becoming a local site id rather than a repository-profile lookup is also a good backward-compatible path.

## 6. Hard-coding boundary is now strong enough

Generic production source cannot contain deployment routing constants such as:

- `htzhulab`;
- Longleaf/CUHK partition names;
- site-specific H100/A100 route mappings;
- compute node names;
- account/QOS/hostname constants.

Generic code may understand arbitrary GPU/GRES/feature vocabulary, but site route mapping comes from live/local context.

That matches the open-source product requirement.

## 7. Gate coverage is sufficient

No G9 is needed.

The G1 extension now directly proves:

- no deployment leakage;
- no-profile third-party site works;
- live facts build a generic SiteContext;
- hidden/unavailable facts remain UNKNOWN;
- public profile acts as policy, not support matrix.

The G6 extension proves the installed production identity on a fake third-party site through:

```text
no committed profile
+ fake live Slurm CLI
+ local id/override
-> environment materialization
-> installed Skill
-> runtime discovery
-> resolved SiteContext
-> local preference
-> routing plan
```

That is the correct normal-entry evidence. A real third university is not required merely to prove portability.

---

# NON-BLOCKING IMPLEMENTATION NOTES

These should be carried into the execution package; they do not keep SWR-PORT-B1 open.

## N1 — Prefer explicit sinfo field whitelists over raw structured dumps

Current SchedMD documents that `sinfo --json` / `--yaml` dumps all available information for the selected result set and ignores normal formatting selections.

Therefore “structured output” should not automatically be treated as the most privacy-minimal path.

Preferred implementation:

- explicit `-o/-O` field whitelist for the generic discovery minimum; or
- if structured output is used, immediately project only the approved fields and never persist the raw dump.

This follows v0.5's existing data-minimization/privacy contract; it does not require an architecture change.

## N2 — Bound scheduler RPCs

SchedMD explicitly warns against tight-looping `sinfo`/other controller RPCs.

v0.5 already limits discovery to one bounded round per normal routing/planning invocation. Preserve that implementation behavior.

## N3 — local_site_id must remain public-safe when a repo target is materialized

v0.5 already states that ClusterName-derived identity stays local and private host/account/path facts must not enter tracked project source.

Execution tests should ensure that a private/raw ClusterName is not accidentally written into a tracked repo artifact when a local alias is required.

---

# NEW BLOCKER — SWR-VER-B1: repository release direction conflicts with the current version policy

## Requirement

The Proposal must obey:

`docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

for the release class it freezes.

The current policy says repository MINOR is appropriate when the entire collection gains a new repository-level user capability, and gives this explicit class of example:

> a new install / environment / distribution capability that lets the collection support a normal scenario it could not support before.

## Direct source evidence

Current source cannot environment-apply an unknown Slurm site:

- unknown explicit `--site` -> `unknown site profile`;
- no matching profile -> `site_id=None`;
- `environment_apply_plan()` then refuses with `no site profile detected`.

Proposal v0.5 deliberately changes the repository-level `environment detect/plan/apply/doctor` path so that:

```text
unknown third-party Slurm cluster
+ no committed profile
+ live Slurm
-> environment plan/apply works
-> installed normal Slurm workflow works
```

That is not merely a quality improvement inside one prompt.

It gives the collection's shared environment/install layer a class of normal deployments it previously could not support.

Yet Proposal §22 currently says:

```text
repository next PATCH from actual release-time VERSION
```

Current `VERSION` is `5.1.0`.

Under the repository's own version policy, this amendment fits the MINOR criterion substantially better than PATCH.

## Concrete risk

If the package proceeds with PATCH:

- the release metadata understates a repository-level environment capability;
- the eventual release Plan/RESULT would conflict with the repository's canonical version policy;
- execution/release closure would need to change the approved package late, forcing avoidable re-review or producing an internally inconsistent release.

This is a real release-contract defect introduced by v0.5's broader portability capability.

## Minimum closure condition

Do not reopen any Slurm architecture.

The next Proposal revision only needs to correct the release direction:

- architecture/design docs: NO BUMP;
- standalone `slurm-workflows`: still `0.1 -> 0.2` when the full bounded release ships;
- central Plugins: all `NO_BUMP`;
- Bridge Kit: NO CHANGE;
- repository release: **MINOR from the actual release-time repository VERSION** if the generic no-profile environment capability ships as part of this task.

With the current `5.1.0` baseline, that means `5.2.0`, not `5.1.1`.

If repository VERSION changes before release, recompute the next MINOR from that actual source.

Planner may rebut only with direct evidence that generic no-profile Slurm environment/install support already exists in the current normal production path. Current source read in this review does not support that rebuttal.

---

# Complexity review

Portability itself remains small:

```text
read-only live Slurm discovery
+ optional public policy overlay
+ local facts/preferences
-> local SiteContext
```

No central server registry, cloud inventory, SSH manager, web scraper, daemon, watcher, history DB, scheduler predictor, administrator path, or hard-coded node-ranking engine is introduced.

The architecture is not overbuilt.

---

# External sources independently checked

SchedMD official documentation checked 2026-09-24:

1. `sinfo` — partition/node/resource discovery, default hidden-partition behavior, format fields, controller-RPC warning  
   https://slurm.schedmd.com/sinfo.html
2. `scontrol` — show partition/config fields and PrivateData authorization behavior  
   https://slurm.schedmd.com/scontrol.html
3. `slurm.conf` — ClusterName and PrivateData semantics  
   https://slurm.schedmd.com/slurm.conf.html
4. `sacctmgr` — association fields including cluster/account/partition/QOS/default-QOS  
   https://slurm.schedmd.com/sacctmgr.html
5. Accounting and Resource Limits — SlurmDBD association model / permission context  
   https://slurm.schedmd.com/accounting.html

No external Slurm evidence contradicts the v0.5 portability design.

---

## Final fields

```text
RESULT = REVISE

SWR-PORT-B1 = CLOSED

SWR-B1 = CLOSED
SWR-B2 = CLOSED
SWR-ER-B1 = CLOSED
SWR-ER-B2-A = CLOSED
SWR-ER-B2 = CLOSED
SWR-ER-B3 = CLOSED

SWR-VER-B1 = OPEN

PASS_OBJECT = NOT_APPLICABLE
PASS_SCOPE = NOT_APPLICABLE

PROPOSAL_COMMIT = 376d03f0d1f9cde2e425bdba62e53942ec5063c6
BRIDGE_CHANGE_REQUIRED = NO
EXECUTION_READY_REVIEW = NOT_REQUESTED
```
