# Slurm Workflows Routing Refactor — Execution-ready Critic Review v0.2

日期：2026-09-24  
角色：AI Research Stack Independent Critic  
审查阶段：EXECUTION_READY

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- approved_architecture: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_2_2026-09-24.md` @ `b1d516c173ce838fd5eb9f39ae0a117bcb7f517e`
- architecture_critic_pass: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_2_2026-09-24.md` @ `08c598f748903ec48c07b96fd1b35dc96561699d`
- execution_plan: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_2_2026-09-24.md` @ `1309628e5a6fd7be4f81cbd9997b18720244983b`
- goal: `docs/goals/SLURM_WORKFLOWS_ROUTING_REFACTOR_GOAL_V0_2.md` @ `aeec366f95dd59e24a760444d1413a91f2583eaa`
- kickoff: `docs/operations/prompts/SLURM_WORKFLOWS_ROUTING_REFACTOR_KICKOFF_V0_2.md` @ package tip `8a489d1cf21298eada472e185d820efdac83671c`
- current main at review start: `985e2059e90475bde7464364175c7ade33529edb`
- execution branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- execution worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Package-tip -> review-start main drift is one Critic-prompt document only; no production or execution-package semantics changed.

## Result

```text
RESULT = REVISE
READY_FOR_CODEX = NO
```

The v0.2 Plan / Goal / Kickoff are internally faithful to the architecture that previously received PASS. If the user's intent had remained exactly at that earlier scope, this package would be execution-ready.

However, the user has now supplied new direct production evidence and explicitly clarified three product requirements that the package currently excludes:

1. stable, evidence-based CPU / memory / walltime recommendations for the same workload across repeated runs;
2. a recurring GPU-availability objective (e.g. usable by Monday afternoon) that must not be implemented as a pile of fixed-duration future `--begin` jobs whose late starts spill into the next week;
3. persistent/interactive workloads, including Bridge Kit Persistent Run consumers, must route to a reusable allocation mode rather than blindly treating every workload as a batch `sbatch` job.

These are not stylistic additions. They change what “Slurm routing” must decide before submission and therefore alter the approved non-goals and acceptance surface. The current execution package explicitly leaves resource-feasibility and deadline-aware routing out of scope and contains no persistent-vs-batch execution-mode decision. Starting Codex now would knowingly implement a partial behavior that the user has just said is insufficient.

The previous architecture blockers remain closed. This REVISE is caused by new user requirements and new real queue evidence, not by moving the old goalposts.

---

# Package areas that already PASS

## Architecture equivalence

The package faithfully preserves the approved v0.2 architecture:

- generic Skill + site hard authority + local preference + generated site reference;
- no generic Longleaf partition constants;
- ordered preference -> advisory `--test-only` -> native single-job widening;
- probe parse failure fails closed;
- site/job-class evidence required before automatic in-place Partition widening;
- replaceable-pending-only cancel+resubmit;
- state-safe cancellation + old-job inactive confirmation;
- identity-sensitive array/dependency/external JobId fail closed;
- duplicate race requires explicit site allow + user/local opt-in;
- current Longleaf/CUHK `disabled_by_default` remains fail-closed;
- duplicate fallback may remain disabled;
- no daemon/watcher/database/control plane.

## Execution identity and authorization

The package correctly freezes only:

- branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Creation begins only after the user sends the exact approved Kickoff.

It does not authorize arbitrary `reviewed/*`, arbitrary repos, force push, unrelated production changes, or unbounded Slurm mutations.

## Existing real-Slurm probe boundary

The one-probe Longleaf authorization is well bounded:

- at most one new held/no-op probe;
- no research payload;
- at most five minutes requested walltime;
- inspect/update/cancel only that probe JobId;
- no deliberate release to RUNNING;
- no pre-existing user job touched;
- no duplicate race;
- ambiguous update/cleanup -> stop;
- no second probe without new authorization;
- raw private evidence stays under `private/exports`.

This boundary is not a blocker.

## Existing G1–G6

For the previously approved routing scope, G1–G6 are coherent and adequately tied to installed normal entry / final-candidate identity.

## Version / integration mechanics

The package's release mechanics remain consistent with the existing version policy:

- execution package itself: no bump;
- standalone `slurm-workflows 0.1 -> 0.2` only after final-candidate gates;
- repository next PATCH from actual release-time `VERSION`;
- central plugins: NO_BUMP;
- no new version infrastructure;
- reviewed-branch-only development pushes;
- exact reviewed candidate + no relevant drift before ordinary non-force integration to main.

These mechanics may remain after the architecture amendment, subject to the normal release-time recomputation.

---

# BLOCKERS

## SWR-ER-B1 — Stable workload resource contract / recommendation is missing

### Requirement

For the same workload family, CPU, memory, GPU count/type, and walltime must not oscillate arbitrarily from week to week. The Skill must recommend resources conservatively enough to avoid OOM/timeout/CPU starvation, while avoiding systematic over-requesting that makes the job harder to schedule.

This is also a prerequisite for routing: comparing P1/P2 or deciding whether one multi-partition job is valid only makes sense if the job's resource contract is stable and explicit.

### Direct evidence

Current `slurm-workflows/SKILL.md` already claims generic resource estimation and requires workload shape including CPU/GPU, memory, walltime and restartability.

But the execution Plan explicitly lists `resource-feasibility preflight` as a non-goal and freezes no rule for how a normal job's resource contract is chosen or kept stable. The only concrete resource wording in the execution package is the “minimal common resource contract” for the one no-op probe.

The user has now explicitly reported the undesired behavior: the same task should not request 8 GB one week and 16 GB the next without evidence.

SchedMD `sacct` already exposes the data needed for a lightweight evidence path without a new database: `ReqMem`, `MaxRSS`, `AllocCPUS`, `TotalCPU`, `Elapsed`, `Timelimit`, `ReqTRES`, `AllocTRES`, state / OOM / timeout information, and optional TRES usage. SchedMD also documents memory as a consumable scheduling resource; over-requesting memory can restrict which nodes can satisfy a job.

External references:

- https://slurm.schedmd.com/sacct.html
- https://slurm.schedmd.com/sbatch.html
- https://slurm.schedmd.com/cpu_management.html
- https://slurm.schedmd.com/cons_tres_share.html

### Concrete causal risk

Without a stable resource contract:

- under-requested memory can OOM or fail training;
- under-requested CPU can starve preprocessing/data loading or elongate runtime;
- over-requested memory/CPU reduces the set of allocatable nodes and may increase queue delay;
- `sbatch --test-only` comparisons can change solely because the Skill randomly changed the resource request;
- a “same” weekly job can no longer be meaningfully compared over time.

### Minimal closure condition

Planner must amend the architecture/package with a **small sticky resource-contract policy**, not a resource-prediction service.

Minimum semantics:

1. Define a comparable **workload family** (project/job family + entrypoint/workload class + relevant scale/GPU requirement). Do not mix unrelated jobs merely because they use the same partition.
2. Once a resource contract is accepted for a workload family, **reuse it by default**. New weekly invocations do not re-pick CPU/memory from scratch.
3. User/project explicit values remain authoritative.
4. Historical accounting may recommend a change only from comparable runs; no separate queue-history database is needed.
5. Memory / CPU / walltime changes require evidence and hysteresis, so values do not flap.
6. GPU count/type is not silently reduced just to get scheduled sooner.
7. Routing uses the frozen/recommended resource contract; it must not silently shrink resource needs to make a preferred partition appear feasible.
8. The current “resource-feasibility is wholly a future non-goal” statement must be narrowed: full site-wide resource prediction may remain future work, but basic resource-contract formation and candidate compatibility are part of current routing.

### Critic-recommended initial heuristic for Planner to evaluate

This is a proposed shape, not yet approved architecture:

**Memory**

- keep the current accepted request unless evidence crosses a boundary;
- immediate increase after OOM or a comparable run whose observed high-water mark is close to the request;
- reasonable starting trigger: `MaxRSS >= 0.85 * requested memory`;
- next recommendation: approximately `1.25 * recent comparable high-water mark`, rounded upward to a site-appropriate unit/granularity;
- do not decrease from one low run;
- consider decrease only after at least 3 comparable successful runs whose high-water marks remain below roughly 50% of the current request; use a conservative target such as `1.5 * recent high-water mark`;
- otherwise keep the exact previous value.

This directly prevents 8 GB -> 16 GB -> 8 GB oscillation.

**CPU**

- start from declared parallelism / existing accepted `cpus-per-task`, not a generic “more is better” default;
- use accounting only as evidence, not as a sole optimizer;
- a useful efficiency diagnostic is roughly `TotalCPU / (Elapsed * AllocCPUS)`, but GPU-/I/O-bound jobs must not be downsized from that number alone;
- only raise CPU when the workload actually has parallel work and repeated evidence shows CPU saturation / loader bottleneck;
- only lower after several comparable runs show sustained large over-allocation and no throughput/loader requirement;
- otherwise keep the accepted CPU count unchanged.

**Walltime**

- batch compute may use recent comparable elapsed time with bounded headroom;
- timeout is immediate evidence to increase;
- persistent/availability allocations must use an explicit availability-window policy instead of deriving walltime from training-history quantiles.

No universal `8G`, `16G`, `4 CPU` constants should be embedded in generic source.

Owner: Planner; requires architecture amendment because current Proposal/Goal explicitly exclude this behavior.

---

## SWR-ER-B2 — Weekly GPU availability is modeled as calendar-named future jobs rather than a reusable capacity lifecycle

### Requirement

The product should support the user's real objective:

> from roughly Monday afternoon onward, have a usable GPU allocation available for the week's work, without a late-start previous allocation causing the next week's capacity request to become useless.

The Skill must distinguish “calendar availability” from “run this batch job after date X”.

### Direct evidence

The user's current queue shows:

- one `weekly-h100-20260920` allocation RUNNING;
- multiple future `weekly-h100-YYYYMMDD` jobs pending with reason `BeginTime`;
- each uses a fixed `5-14:10:00` time limit.

The reported failure is that the previous weekly allocation waited so long to start that its full fixed time limit extended close to / past the next week's target window, while the next weekly job remained unable to provide the intended fresh capacity.

SchedMD documents:

- `--begin` means **defer eligibility until the specified time**; it is not a reservation or guaranteed dispatch time.
- Under multifactor priority, age normally reflects time waiting while **eligible**; future begin time does not automatically buy queue age unless the site explicitly configures `PriorityFlags=ACCRUE_ALWAYS`.
- `--deadline` can remove a job when it can no longer finish by a deadline.
- `squeue --start` is only an expected start estimate when backfill scheduling supports it.
- A true advanced reservation is the scheduler feature designed to reserve future resources, and creation of reservations is an administrator/SlurmUser operation.

External references:

- https://slurm.schedmd.com/sbatch.html
- https://slurm.schedmd.com/priority_multifactor.html
- https://slurm.schedmd.com/job_reason_codes.html
- https://slurm.schedmd.com/squeue.html
- https://slurm.schedmd.com/reservations.html

### Concrete causal risk

If the Skill continues generating many calendar-labeled long jobs with future `BeginTime`:

- a late start shifts the entire fixed runtime window forward;
- old and new “weeks” overlap semantically;
- the scheduler sees jobs, not the user's concept of “Monday capacity”;
- months-ahead jobs with future begin times may not gain useful eligible-age priority;
- the user can hold an actually usable GPU in the previous running allocation while simultaneously waiting for a differently named successor;
- the queue can accumulate stale future jobs without guaranteeing any Monday start.

This is exactly the real failure the user has now reported.

### Minimal closure condition

Planner must replace “weekly job == independent dated sbatch” with a minimal **persistent capacity lifecycle**.

At minimum:

1. Treat the object as a **resource family / capacity allocation**, not a disposable calendar-week job name.
2. Before requesting a new allocation, inspect whether a compatible allocation is already RUNNING and reusable. If yes and it has sufficient remaining useful time, reuse/attach to it rather than waiting for a new dated allocation.
3. If a compatible successor is already PENDING, do not blindly add another.
4. Keep a bounded horizon such as one active + at most one intended successor; do not pre-create months of weekly jobs by default.
5. Represent user intent as a target availability window, e.g. “usable by Monday afternoon through the chosen week cutoff”, with a configurable lead time.
6. `--begin` may be used only as earliest eligibility; the Skill must never describe it as a reservation/guarantee.
7. Avoid late-start allocations spilling indefinitely into the next target window. Planner must choose a bounded calendar-end mechanism appropriate to site semantics (for example submission-time deadline / bounded time semantics, or a verified ability to shorten the allocation end after grant). Do not invent an automatic `EndTime` mutation without verifying the target site and authority.
8. If the requirement is a **guarantee** of Monday GPU availability rather than best effort, the Skill must say that a user-level `--begin` job cannot guarantee this; a site/lab advanced reservation or equivalent administrator policy is the correct mechanism.
9. No new daemon is required. The lifecycle can be evaluated on normal Persistent Run / Slurm invocation and on resume.

The exact target window / lead time is a user-local preference, not generic source.

Owner: Planner; this reopens the previously excluded deadline/availability part of the design.

---

## SWR-ER-B3 — Persistent / interactive workload mode is not part of routing

### Requirement

When the workload intent is persistent / interactive / reusable allocation, the Skill should not blindly emit the same batch submission strategy used for unattended finite batch computation.

The user's explicit expectation is that Bridge Kit Persistent Run consumers should “know” that they need an interactive/reusable Slurm allocation, with the exact duration/site resource policy remaining configurable.

### Direct evidence

The current execution Plan has no workload-mode decision and explicitly forbids Bridge Kit changes.

The current Bridge Kit source provides important ownership evidence:

`YuukiAS/GPT_Codex_AI_Bridge_Kit/docs/design/0.8.0_persistent_run.md` states that a real long research goal can **reuse an existing interactive Slurm allocation**, while also stating that resource budget/semantics remain owned by the original Goal/task/workflow rather than Bridge Kit.

That means the correct reusable boundary is not “put Slurm scheduling policy into Bridge Kit”. Bridge Kit provides persistent execution semantics; the Slurm/domain layer should decide what kind of allocation is appropriate when the upstream Goal says persistent execution is required.

SchedMD documents:

- `sbatch` is a batch script submitted for later execution;
- `salloc` obtains a resource allocation and then runs a command/shell;
- `salloc --no-shell` can create an allocation that remains active and can later receive `srun --jobid=...` steps;
- interactive-shell behavior can be provided via `salloc`/interactive steps when the site is configured for it.

External references:

- https://slurm.schedmd.com/quickstart.html
- https://slurm.schedmd.com/salloc.html
- https://slurm.schedmd.com/faq.html

### Concrete causal risk

A persistent GPU workspace/service submitted as an ordinary batch job can be difficult to reuse, attach to, or treat as ongoing capacity. That makes a still-running old allocation effectively useless to a new Persistent Run and causes unnecessary waiting for a new job.

At the same time, blindly replacing `sbatch` with `salloc` would also be wrong: **interactive allocation does not inherently receive faster scheduling priority**. If the site has no special interactive partition/QOS, `salloc` can wait just like a batch allocation.

So the missing capability is workload-mode routing, not “always use interactive because it is faster”.

### Minimal closure condition

Planner must add a small workload-mode decision:

- finite unattended batch computation -> batch mode (`sbatch` or site-approved equivalent);
- persistent / reusable workspace or Persistent Run capacity -> allocation mode (`salloc` / site-approved interactive allocation semantics);
- short debugging shell -> interactive shell mode.

Additional boundaries:

1. Do not hard-code a Longleaf `interact` partition or assume an interactive QOS exists.
2. Partition/QOS remains site/local configuration.
3. Prefer reuse/attach to an already compatible running allocation before requesting another.
4. `salloc --no-shell` + later `srun --jobid` is a reasonable candidate for a persistent allocation contract, but it must be validated against Longleaf's actual site behavior and the lifecycle of the caller before production use.
5. Bridge Kit itself does not need to own Slurm policy. If its current Persistent Run contract already exposes persistent intent, Slurm Workflows can consume that intent. A Bridge code change should only be proposed if Planner proves the current consumer cannot communicate that intent.
6. Do not claim allocation mode bypasses the scheduler or guarantees Monday readiness.

Owner: Planner; this is a new product capability and needs architecture review before execution.

---

# Complexity assessment after new evidence

The answer is **not** to build a scheduler service.

A still-small architecture can cover the new requirements:

```text
workload intent
    -> batch | persistent allocation | debug interactive

stable resource contract
    -> CPU / memory / GPU / walltime

site authority + local preferences
    -> legal partitions / QOS / feature preferences / availability target

current allocation state
    -> reuse existing compatible allocation
       or request one bounded successor

scheduler evidence
    -> advisory probe / expected start / fail-closed widening
```

This remains a Skill-level decision system. No queue-history database, watcher, daemon, dependency remapper, or custom scheduler is required.

The user has supplied enough real evidence that keeping all resource/availability/mode concerns as future NON_GOALS would now be **too simple**.

---

# Gate implications for the Planner amendment

Do not mechanically multiply gates, but the new requirements have genuinely distinct failure semantics.

A revised architecture should likely add at most two distinct capabilities rather than hiding everything inside G2/G3:

- **Resource-contract stability / right-sizing**: same workload keeps a stable request unless accounting evidence justifies a change; OOM/timeout/over-allocation cases are covered.
- **Persistent-capacity lifecycle**: persistent intent selects reusable allocation mode; existing compatible allocation is reused; at most one successor is queued; `BeginTime` is not treated as reservation; Monday-availability claim is truthfully best-effort unless a real reservation exists.

Existing G1–G6 should not be rewritten unless necessary.

---

# Required next step

Because these new requirements change previously explicit NON_GOALS, this is not a small execution-package wording fix.

Planner should return to a **bounded architecture amendment** for the same task key, preferably a v0.3 Proposal, rather than start Executor and immediately create a second refinement task.

The amendment should:

1. preserve all v0.2 architecture decisions and the already closed SWR-B1 / SWR-B2;
2. add stable resource-contract semantics;
3. add persistent/batch execution-mode routing;
4. add recurring GPU capacity lifecycle / availability-window semantics;
5. keep advanced-reservation guarantees distinct from best-effort user scheduling;
6. verify ownership against Bridge Kit Persistent Run without modifying Bridge Kit unless a real integration gap is proven;
7. keep no-daemon/no-database/no-custom-scheduler boundaries;
8. then regenerate Plan / Goal / Kickoff and return for Critic review.

Do not create the execution branch/worktree until that revised package is independently approved.

---

## Final fields

```text
RESULT = REVISE
READY_FOR_CODEX = NO
PASS_OBJECT = NOT_APPLICABLE
PASS_SCOPE = NOT_APPLICABLE

PACKAGE_TIP = 8a489d1cf21298eada472e185d820efdac83671c
EXECUTION_BRANCH = reviewed/hpc--slurm-workflows-routing-refactor
EXECUTION_WORKTREE = /tmp/ai-skills-hpc-slurm-workflows-routing-refactor

REAL_SLURM_AUTH_BOUNDARY = PASS
VERSION_CLOSURE = PASS
```

The existing probe authorization and version mechanics are well bounded. They are not why execution is blocked. Execution is blocked because current user intent now requires resource-stability and persistent-capacity routing capabilities that the package explicitly excludes.
