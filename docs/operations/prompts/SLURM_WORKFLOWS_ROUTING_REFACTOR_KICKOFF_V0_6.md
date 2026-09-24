# Slurm Workflows Routing Refactor — Kickoff v0.6

直接执行已获架构 Critic PASS、并在 execution-ready Critic 对本 exact package 给出 `READY_FOR_CODEX=YES` 后批准的 Slurm Workflows routing refactor。不要重新设计架构，不要创建 successor task。

Repository:

`YuukiAS/AI_Skills_Collection`

Exact task:

`hpc--slurm-workflows-routing-refactor`

Exact branch to create/use:

`reviewed/hpc--slurm-workflows-routing-refactor`

Exact task-owned worktree:

`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Canonical authority:

- Proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md`
- Architecture Critic PASS: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_6_2026-09-24.md`
- Execution Plan: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_6_2026-09-24.md`
- Canonical Goal: `docs/goals/SLURM_WORKFLOWS_ROUTING_REFACTOR_GOAL_V0_6.md`

Use the repository maintenance contract from `workflow-core` + `ai-skills-core`, with `slurm-workflows` as the HPC/domain owner. Do not let maintenance helpers redesign the approved routing/resource/capacity semantics.

## 1. Kickoff-time preflight

Start from kickoff-time latest compatible `origin/main`.

Before creating the branch/worktree:

1. verify the exact v0.6 Proposal, architecture PASS, Plan, Goal and this Kickoff are present;
2. inspect relevant drift in Slurm Workflows, environment/site code, gate policy and version policy;
3. if relevant semantic drift exists, stop and return to Planner/Critic;
4. unrelated docs/review drift is not a blocker.

Then create exactly the authorized branch/worktree above.

No other branch/worktree is authorized.

## 2. Implement the approved product only

Implement all frozen v0.6 capabilities:

- generic bounded live Slurm discovery;
- optional public hard-policy overlays, not a supported-server registry;
- `local_site_id` / optional `policy_overlay_id`;
- no-profile Slurm environment detect/plan/apply/doctor;
- fact != policy != preference;
- no deployment-specific generic constants;
- sticky workload resource contracts with approved hysteresis;
- batch / persistent allocation / debug interactive workload modes;
- reusable persistent-capacity lifecycle;
- one-active / one-successor logic;
- one-time bounded capacity-family enrollment;
- same-scope recurring successor maintenance without weekly repeat prompt;
- unrelated CPU-only workload does not activate an enrolled GPU family;
- JobId/dependency/array/running-transition safety;
- duplicate-race explicit site authority;
- G1-G8 including G1/G6 no-profile portability;
- Bridge Kit remains unchanged.

Do not implement a daemon, watcher, scheduler service, history DB, central cluster registry, SSH manager, university-doc scraper, dependency-remap system, administrator path, or automatic account/QOS mutation.

## 3. Generic discovery requirements

Prefer explicit `sinfo -o/-O` field whitelists and the minimum required controller RPCs.

Do not treat raw `sinfo --json/--yaml` as automatically privacy-minimal.

Do not persist raw discovery dumps into tracked project source.

If private/raw ClusterName is unsuitable for tracked output, use a safe local alias.

Hidden/unavailable facts remain UNKNOWN; never invent account/QOS/partition policy.

No-profile third-party Slurm sites must work without adding a committed site profile.

## 4. Resource and preference requirements

Same comparable workload + no new evidence -> reuse the exact accepted resource contract.

Carry forward:

- OOM memory increase after rounding must be strictly greater than current accepted request;
- unavailable completed-job `sacct Comment` -> conservative family matching;
- ambiguous history -> no automatic right-size;
- CPU stable-first;
- GPU count/type is not silently downgraded for scheduling convenience.

Local partition/accelerator preference is allowed only from local/live context.

A local explicitly preferred partition may rank first. Remaining legal compatible routes may be ordered by a user-local accelerator preference. Exact deployment partition names and GPU-to-partition mappings must never become generic production defaults.

A hard accelerator requirement cannot be downgraded as a preference.

## 5. Capacity lifecycle and enrollment

`auto_maintain_successor=true` without valid enrollment remains read-only.

Valid one-time family enrollment may authorize same-scope recurring successor maintenance without a weekly repeat prompt.

Activation must be bounded to the matching family/resource intent. Merely working on the same cluster does not activate an enrolled GPU family.

During this implementation task:

- do NOT enroll the user's real weekly GPU capacity family;
- do NOT submit/cancel/retarget the user's real weekly successor jobs;
- test enrollment/capacity behavior using deterministic fixtures only.

## 6. Real Slurm authorization in this Kickoff

By sending this exact approved Kickoff, I authorize only the following **conditional capability probes**, and only if deterministic/read-only evidence shows they are still needed.

No other real Slurm mutation is authorized.

### Probe class A — one held/no-op batch probe, maximum one

May be used to combine calendar-bound request validation and pending Partition-update validation.

Limits:

- at most one new task-owned probe job;
- held from submission/start;
- obvious probe-only name;
- no scientific/research payload;
- trivial no-op command;
- minimal resource request;
- requested walltime <= 5 minutes;
- may inspect/update only this probe JobId;
- never intentionally release it to RUNNING;
- may validate controller-visible calendar fields and in-place Partition semantics;
- cancel it and confirm it is inactive.

If read-only `sbatch --test-only` is enough for calendar semantics, do not create extra mutation for duplicate evidence.

### Probe class B — one minimal persistent-allocation probe, maximum one

May be used only if needed to validate the candidate persistent allocation caller/attach/cleanup lifecycle.

Limits:

- prefer the cheapest live legal CPU-only allocation; do not consume a GPU merely to test lifecycle;
- no scientific/research payload;
- requested walltime <= 5 minutes;
- at most one trivial `srun --jobid` step;
- use a bounded wait/immediate mechanism only after confirming the site's supported semantics;
- never wait indefinitely;
- cleanup only the task-owned allocation and confirm it is inactive.

If a cheap bounded probe is not available, leave that backend unverified/fail-closed rather than escalating resources.

### Global probe limits

Across the entire task:

- maximum one Probe A + one Probe B;
- combine conceptual questions whenever safely possible;
- no automatic retry after a failed/ambiguous probe;
- no pre-existing user job may be modified;
- no real weekly successor may be submitted;
- no real capacity-family enrollment may be created;
- no duplicate-job race;
- no research GPU computation;
- no account/QOS/association/partition/reservation/admin mutation.

If cleanup cannot be confirmed, stop all further Slurm mutation and report the exact task-owned probe JobId.

Raw private/site-specific probe output must remain under:

`private/exports/hpc--slurm-workflows-routing-refactor/real-site-probes/`

Public-safe redacted evidence belongs under:

`results/hpc--slurm-workflows-routing-refactor/real-site-probes/`

## 7. Tests and gates

Run deterministic focused tests first, then current full repository validation.

G1-G8 must follow the exact Execution Plan.

In particular:

- G1 proves site isolation + live discovery + hidden-fact fail-closed behavior;
- G2 proves local preference without changing the resource contract;
- G3 proves native widening + JobId/dependency/array/transition safety;
- G4 proves duplicate-race authority or records the capability disabled/NOT_APPLICABLE;
- G5 proves bounded monitoring/replacement;
- G6 must exercise the actually installed production Skill on both known-profile and no-profile fake Slurm sites;
- G7 proves sticky resource stability/right-sizing;
- G8 proves batch/persistent/debug mode, capacity reuse, one successor, and enrollment authority.

Helper-only tests are insufficient for G6.

## 8. Final-candidate and release procedure

After implementation/dev tests and any authorized probes:

1. fetch current `origin/main`;
2. stop on relevant semantic drift;
3. reconcile compatible release/docs drift before final freeze;
4. compute release versions from actual release-time baseline;
5. apply release metadata;
6. freeze one exact final candidate SHA;
7. run G1-G8 and full tests on that exact versioned candidate;
8. request independent pre-final Critic review;
9. do not change production/release bytes after Critic PASS.

Release class is frozen:

```text
Repository: MINOR

If actual baseline remains 5.1.0:
5.1.0 -> 5.2.0

Otherwise:
next MINOR from actual release-time VERSION

Standalone slurm-workflows:
0.1 -> 0.2

Central Plugins:
all NO_BUMP

Bridge Kit:
NO CHANGE
```

Use existing version infrastructure only.

Update README, root CHANGELOG, VERSION/package parity, standalone Skill version, and existing registry/catalog/generated parity as required.

## 9. Git and integration authority

Ordinary non-force commit/push to the exact reviewed branch is authorized.

No force push.

After G1-G8 and independent pre-final Critic PASS, ordinary non-force integration of the exact reviewed final candidate to `main` is authorized only if main has no relevant conflicting semantic drift.

If the required next MINOR or production bytes change during integration preflight, reconcile and rerun affected final gates/review rather than silently integrating stale metadata.

Do not modify Bridge Kit, Longleaf_Bridge, unrelated project product logic, central Plugin production behavior, or central Plugin versions.

## 10. Final report

Return at least:

```text
RESULT = PASS | REVISE
TASK = hpc--slurm-workflows-routing-refactor
BRANCH =
WORKTREE =
START_MAIN =
FINAL_CANDIDATE =

G1 =
G2 =
G3 =
G4 =
G5 =
G6 =
G7 =
G8 =

NO_PROFILE_SITE_NORMAL_ENTRY =
RESOURCE_CONTRACT_STABILITY =
PERSISTENT_CAPACITY_LIFECYCLE =
ENROLLMENT_AUTHORITY =

REAL_PROBE_A = NOT_NEEDED | PASS | FAIL | BLOCKED
REAL_PROBE_B = NOT_NEEDED | PASS | FAIL | BLOCKED
PROBE_CLEANUP = NOT_APPLICABLE | PASS | BLOCKED

SLURM_WORKFLOWS_VERSION =
REPOSITORY_RELEASE_CLASS = MINOR
REPOSITORY_VERSION =
CENTRAL_PLUGIN_BUMPS = NONE
BRIDGE_CHANGE = NO

README_CHECK =
CHANGELOG_CHECK =
FULL_TEST_SUITE =
FINAL_CRITIC =
INTEGRATED_TO_MAIN = YES | NO
REMOTE_MAIN =
```

Stop with `REVISE` rather than expanding scope if the approved architecture cannot be implemented safely.
