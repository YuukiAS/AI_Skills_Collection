# Slurm Workflows Routing Refactor — Execution-ready Critic Review v0.6

日期：2026-09-24  
角色：AI Research Stack Independent Critic  
审查阶段：EXECUTION_READY

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- approved_proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md` @ `ad3e60988f5581dd0d0c194e13907baaa446c413`
- architecture_critic_pass: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_6_2026-09-24.md` @ `63a80b33e51c2eaf7fb5bc662a8ef87f3cdeede8`
- execution_plan: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_6_2026-09-24.md` @ `8a73c8edd82b2a02749a1cff884d06122874fac3`
- canonical_goal: `docs/goals/SLURM_WORKFLOWS_ROUTING_REFACTOR_GOAL_V0_6.md` @ `f44f8b09004019222dbd1dc649ca14db04202bb9`
- kickoff: `docs/operations/prompts/SLURM_WORKFLOWS_ROUTING_REFACTOR_KICKOFF_V0_6.md` @ package tip `c4df32fd1778b216aaa459a80c117283ad318ad8`
- future execution branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- future worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Package tip -> review-start latest main contains only the execution-ready Critic prompt. There is no relevant semantic drift in the Proposal/Plan/Goal/Kickoff or production Slurm source.

The future reviewed branch does not currently exist.

## Result

```text
RESULT = PASS
READY_FOR_CODEX = YES
```

```text
PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PACKAGE_V0_6

PASS_SCOPE =
execution-ready Plan + Goal + Kickoff only; actual execution begins only after user sends approved v0.6 Kickoff
```

This PASS approves the exact v0.6 execution package. It does not itself create the branch/worktree, mutate Slurm, modify production, bump a version, enroll a capacity family, or start Executor. Those effects begin only when the user sends the approved Kickoff.

---

## Closure of the execution-ready review

The package faithfully converts the approved architecture into a bounded implementation contract.

### Architecture equivalence

The Plan/Goal/Kickoff preserve:

- bounded live Slurm discovery;
- optional public hard-policy overlays rather than a supported-server registry;
- `local_site_id` / optional `policy_overlay_id` separation;
- no-profile environment detect/plan/apply/doctor;
- fact != policy != preference;
- no deployment-specific generic routing constants;
- sticky workload resource contracts and accepted G7 hysteresis;
- batch / persistent allocation / debug interactive modes;
- persistent reusable capacity lifecycle;
- one active / at most one intended successor;
- one-time bounded capacity-family enrollment;
- same-scope recurring maintenance without weekly re-prompt;
- unrelated CPU-only work not activating an enrolled GPU family;
- JobId/dependency/array/running-transition safety;
- duplicate-race explicit site authority;
- G1-G8 including portability extensions;
- Bridge Kit NO CHANGE.

No architecture finding is weakened or expanded.

### Execution identity and source scope

The future execution identity is exact and bounded:

```text
branch:
reviewed/hpc--slurm-workflows-routing-refactor

worktree:
/tmp/ai-skills-hpc-slurm-workflows-routing-refactor
```

Creation requires both this `READY_FOR_CODEX=YES` and a later user message sending the approved Kickoff.

The implementation boundary is sufficient without being open-ended:

- Slurm Skill source/references;
- at most one small deterministic installed helper;
- shared environment/install path;
- local config example/docs;
- minimal schema/site-profile parity only when actually required;
- focused existing tests plus at most one focused Slurm test file;
- direct catalog/registry/generated parity;
- release files only as part of final release closure.

Bridge Kit, Longleaf_Bridge, scientific project logic, Host Policy, unrelated Skills and central Plugin behavior/topology remain out of scope.

### Generic discovery

The package is concrete enough for implementation:

- explicit `sinfo -o/-O` whitelists preferred;
- no `sinfo --all` visibility expansion;
- raw JSON/YAML not treated as automatically privacy-minimal;
- raw discovery output is not persisted into tracked project source;
- controller/database RPCs are bounded;
- optional `sacctmgr` failure degrades to UNKNOWN;
- private/raw ClusterName uses a safe local alias when necessary;
- no-profile live Slurm can complete environment materialization and normal installed routing.

The helper remains a deterministic normal-path component, not a registry/service/daemon.

### Resource contract

The package correctly freezes:

- comparable workload family identity;
- explicit/project/local accepted-contract precedence;
- exact resource reuse when no evidence justifies change;
- accepted memory hysteresis;
- OOM increase strictly above current memory after rounding;
- MaxRSS comparability guard;
- CPU stable-first;
- TIMEOUT as walltime increase evidence;
- persistent availability duration separate from batch elapsed-history sizing;
- no silent GPU count/type downgrade;
- conservative behavior when `sacct Comment` cannot support confident family matching.

Routing cannot silently alter resource requirements to make a candidate partition look easier to schedule.

### Local partition/accelerator preference

The package correctly keeps local deployment preference separate from generic source.

Hard resource requirements and live/site legality filter first. Only then can:

- an explicitly preferred local partition tier rank first;
- remaining legal routes follow a user-local accelerator-class preference.

No Longleaf/CUHK route name or GPU-to-partition mapping becomes a generic production default.

### Persistent capacity and enrollment

The package preserves the bounded recurring-authority model:

- compatible running capacity is reused first;
- at most one intended successor;
- plain `auto_maintain_successor=true` is read-only without enrollment;
- same-scope valid enrollment can authorize recurring maintenance without weekly re-prompt;
- unrelated CPU-only work cannot activate the GPU family;
- material scope changes reauthorize;
- stale enrollment fails closed;
- pre-existing jobs remain outside lifecycle mutation scope unless separately authorized and replaceable.

The implementation task is explicitly forbidden from enrolling or maintaining the user's real weekly GPU family.

### Existing routing safety

The package preserves:

- `--test-only` advisory-only semantics;
- parse failure fail-closed;
- native single-job widening;
- target-site/job-class evidence before in-place Partition widening;
- replaceable-pending-only cancel+resubmit;
- state-safe cancellation + confirmed old-job inactivity;
- identity-sensitive array/dependency/external JobId fail-closed;
- duplicate race only with explicit site allow + user/local opt-in;
- unknown site duplicate-race authority disabled.

### Development tests vs production gates

The development regression bank covers G1-G5/G7/G8 without needing live mutation.

G6 correctly requires the actual installed production path, including:

- known-profile site fixture;
- no-profile fake third-party Slurm site;
- installed helper/Skill consuming the live fake SiteContext and local preference;
- persistent-capacity normal entry.

Helper-only unit tests cannot satisfy G6.

### Real Slurm authorization boundary

The approved Kickoff's real-side-effect envelope is sufficiently small and executable.

Maximum live mutation for the entire implementation task is:

- Probe A: at most one task-owned held/no-op batch job, which may combine calendar-bound and pending Partition-update validation;
- Probe B: at most one minimal persistent-allocation lifecycle probe, only if still necessary.

Global boundaries:

- no existing user job touched;
- no real weekly successor;
- no real capacity-family enrollment;
- no duplicate race;
- no scientific/research payload;
- no research GPU computation;
- no account/QOS/association/partition/reservation/admin mutation;
- each probe walltime <= 5 minutes;
- Probe B prefers CPU-only;
- no indefinite wait;
- no automatic retry after failed/ambiguous probe;
- cleanup must be confirmed;
- cleanup uncertainty stops further mutation;
- private raw evidence stays under `private/exports/`;
- public evidence is redacted.

Official SchedMD semantics independently rechecked:

- `sbatch --hold` submits a job held at priority zero;
- `sbatch --test-only` validates/estimates without submission;
- `salloc --no-shell` leaves an active allocation with a JobId and no task;
- later `srun --jobid` can use that allocation;
- `salloc --immediate[=<seconds>]` can bound allocation waiting;
- `scancel --state=PENDING` restricts cancellation to the requested state.

The package correctly requires site validation rather than assuming every target deployment supports every desired lifecycle.

### Evidence, freeze, release and integration

The Plan correctly requires:

1. development implementation/tests;
2. any authorized bounded probes;
3. fetch/reconcile compatible main drift;
4. compute release target from the actual baseline;
5. apply release metadata;
6. freeze one exact candidate SHA;
7. run G1-G8/full suite/parity on that exact versioned candidate;
8. independent pre-final Critic review;
9. no production/release byte changes after that PASS;
10. ordinary non-force integration only of the exact reviewed candidate.

This prevents stitching release evidence across different commits.

---

## Release/version contract

Current source confirms:

```text
VERSION = 5.1.0
slurm-workflows = 0.1
```

The package correctly freezes:

```text
Architecture/package docs:
NO BUMP

Complete shipped capability:
Repository release class = MINOR

If baseline remains 5.1.0:
5.1.0 -> 5.2.0

If baseline changes:
next MINOR from actual release-time VERSION

Standalone:
slurm-workflows 0.1 -> 0.2

Central Plugins:
all NO_BUMP

Bridge Kit:
NO CHANGE
```

Release metadata is applied before final-candidate gates, so the exact candidate reviewed by G1-G8/full tests/final Critic is also the exact versioned release candidate.

No new version infrastructure is authorized.

---

## Final gate judgment

G1-G8 remain distinct and sufficient:

- G1: site isolation + live discovery/privacy/fail-closed portability;
- G2: local preference routing without resource mutation;
- G3: widening + JobId/dependency/array/transition safety;
- G4: duplicate-race authority or disabled capability;
- G5: bounded monitoring/replacement;
- G6: installed normal production identity, including no-profile site;
- G7: resource-contract stability/right-sizing;
- G8: workload mode + persistent capacity lifecycle + enrollment authority.

No G9 is needed.

---

## Final fields

```text
RESULT = PASS
READY_FOR_CODEX = YES

PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PACKAGE_V0_6

PASS_SCOPE =
execution-ready Plan + Goal + Kickoff only; actual execution begins only after user sends approved v0.6 Kickoff

PROPOSAL_COMMIT = ad3e60988f5581dd0d0c194e13907baaa446c413
ARCHITECTURE_PASS_COMMIT = 63a80b33e51c2eaf7fb5bc662a8ef87f3cdeede8
PLAN_COMMIT = 8a73c8edd82b2a02749a1cff884d06122874fac3
GOAL_COMMIT = f44f8b09004019222dbd1dc649ca14db04202bb9
KICKOFF_PACKAGE_TIP = c4df32fd1778b216aaa459a80c117283ad318ad8

EXECUTION_BRANCH = reviewed/hpc--slurm-workflows-routing-refactor
EXECUTION_WORKTREE = /tmp/ai-skills-hpc-slurm-workflows-routing-refactor

REAL_SLURM_AUTH_BOUNDARY = PASS
NO_PROFILE_PORTABILITY = PASS
RESOURCE_CONTRACT = PASS
CAPACITY_ENROLLMENT = PASS
VERSION_CLOSURE = PASS

REPOSITORY_RELEASE_CLASS = MINOR
STANDALONE_SLURM_WORKFLOWS_RELEASE = 0.1 -> 0.2
CENTRAL_PLUGIN_BUMPS = NONE
BRIDGE_CHANGE_REQUIRED = NO
```
