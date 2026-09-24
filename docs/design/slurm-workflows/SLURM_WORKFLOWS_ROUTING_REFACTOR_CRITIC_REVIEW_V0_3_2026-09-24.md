# Slurm Workflows Routing Refactor — Critic Review v0.3

日期：2026-09-24  
角色：AI Research Stack Independent Critic  
审查阶段：ARCHITECTURE_REVIEW_V0_3

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_3_2026-09-24.md`
- proposal_commit: `f9c0e3abbffaa6677c1f0acec510c47106d66aa1`
- previous approved architecture: v0.2 @ `b1d516c173ce838fd5eb9f39ae0a117bcb7f517e`
- previous architecture PASS: `08c598f748903ec48c07b96fd1b35dc96561699d`
- execution-ready REVISE introducing new requirements: `b211db38bdcff8772c1be493d81b95a5b04a9059`
- review_stage: `ARCHITECTURE_REVIEW_V0_3`
- execution branch/worktree: NOT_CREATED

Preflight: v0.3 proposal commit -> review-start latest main has only the Critic prompt document as drift. There is no relevant production or proposal semantic drift.

## Result

```text
RESULT = REVISE
SWR-ER-B1 = CLOSED
SWR-ER-B2 = OPEN
SWR-ER-B3 = CLOSED
```

Previous v0.2 blockers remain closed:

```text
SWR-B1 = CLOSED
SWR-B2 = CLOSED
```

v0.3 is materially better and still small. It correctly adds sticky resource contracts, persistent-capacity lifecycle, and workload-mode routing without creating a history database, scheduler predictor, daemon, watcher, dependency remapper, or custom scheduler.

Only one blocker remains. It is not a new scheduler-design objection: the automatic successor mechanism has not yet reconciled its mutation authority with the repository's existing site hard constraint `do_not_submit_without_user_confirmation=true`.

---

## Source actually read

AI_Skills_Collection latest main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- Proposal v0.3
- Proposal v0.2
- v0.2 architecture Critic PASS
- execution-ready Critic REVISE v0.2
- `skills/tools/hpc/slurm-workflows/SKILL.md`
- current Longleaf/CUHK site profiles
- current local override docs/source context needed to assess authority/config feasibility

Bridge Kit current main, read-only:

- `docs/design/0.8.0_persistent_run.md`
- `templates/persistent_run/CONTRACT_TEMPLATE.md`
- `templates/persistent_run/AGENTS_SNIPPET.md`

No Bridge source was modified.

---

# SWR-ER-B1 — CLOSED

## Judgment

The sticky resource-contract design is proportionate and sufficient to stop week-to-week resource flapping without building a local scheduler/history system.

### Why the new TOML is justified

`~/.config/ai-skills/slurm-workflows.toml` has a distinct owner from the existing local override:

- site profile = public site authority;
- `local-overrides.toml` = site/user account, partition, QOS and private paths;
- `slurm-workflows.toml` = workload-family accepted resource contracts and persistent-capacity preferences.

That separation is cleaner than stuffing project/workload state into site configuration.

The file is not a disguised history database because v0.3 stores only current accepted contracts/preferences and an optional last-adjustment evidence locator. Historical metrics remain in Slurm accounting and are queried on demand.

### Workload-family identity is sufficiently conservative

The family key uses project identity + entrypoint/job family + workload class + material scale signature + accelerator requirement. Dates, seeds, output folders and partition route do not create new families.

An explicit stable `workload_family` wins. If the Skill cannot determine comparability, it does not merge accounting evidence. That fail-closed rule is more important than inventing a perfect automatic fingerprint.

### Memory semantics are correctly guarded

SchedMD documents `ReqMem` as allocation-request memory, while Max/Ave/Min accounting fields are derived over tasks/steps; specifically, `MaxRSS` is the maximum resident memory observed for one task of the step. Therefore v0.3 is correct not to treat one MaxRSS number as whole-allocation memory for arbitrary multi-task/multi-node jobs.

The 85% / 1.25x / three-run / 50% / 1.5x values are acceptable as initial hysteresis heuristics because:

- they are only automatic when request and accounting semantics are actually comparable;
- explicit project/user contracts take precedence;
- incomparable evidence means no resize;
- one low run cannot cause a decrease.

This is sufficient architecture for stability. It does not need a scheduler ML model.

### CPU should remain stable by default

Keeping accepted `cpus-per-task` unchanged unless there is repeated comparable evidence plus known adjustable parallelism is the correct default.

`TotalCPU/(Elapsed*AllocCPUS)` is useful as a diagnostic but is not a safe generic autotuner, especially for GPU-bound or I/O-bound work. v0.3 correctly refuses to auto-cut CPU merely from low accounting efficiency.

### Non-blocking implementation notes

1. OOM handling should produce an actual increase, not merely satisfy a lower numeric floor. In the execution package, encode the OOM candidate so it is strictly above the accepted current request after rounding.
2. Slurm `Comment` is a good family marker for live jobs, but completed-job `sacct Comment` persistence requires site accounting to store job comments (SchedMD documents `AccountingStoreFlags=job_comment`). If unavailable, family matching must use the already-defined conservative fallback and must not auto-right-size from ambiguous history.

These are implementation clarifications, not reasons to keep SWR-ER-B1 open.

---

# SWR-ER-B2 — OPEN

## Blocker SWR-ER-B2-A — automatic successor submission authority is unresolved

### Requirement

The user explicitly wants the persistent-capacity lifecycle to stop requiring a weekly manual “is next Monday queued?” check.

That is compatible with a one-time durable opt-in. It is **not** compatible with an architecture where a normally read-only `monitor/diagnose` invocation silently gains generic permission to submit or cancel Slurm jobs merely because a boolean exists somewhere.

The architecture must reconcile automatic successor maintenance with the current site hard authority and with the repository's existing authorization model.

### Direct source / official evidence

Current public site profiles for both Longleaf and CUHK contain:

```json
"do_not_submit_without_user_confirmation": true
```

v0.3 §8 states that when:

```text
auto_maintain_successor = true
```

every normal Slurm Workflows:

- submit;
- allocation request;
- attach/resume;
- monitor/diagnose

performs reconciliation, and if the earliest uncovered target has no successor, **that invocation automatically submits one successor request**.

v0.3 also permits state-safe cancellation/retarget of a lifecycle-owned replaceable pending successor when it becomes stale/redundant.

But v0.3 does not define:

- what exact action establishes the user's durable permission for those future mutations;
- whether `auto_maintain_successor=true` itself is an authorization record or only a preference;
- the bounded scope of that authorization;
- what happens when the preference exists but the required authorization evidence does not.

This matters because the repository's own role/authorization rules distinguish reusable preferences from external side-effect authorization; a repo/config statement cannot silently stand in for unspecified current-user permission.

### Causal user-visible / resource risk

Without closing this boundary, implementation has two bad outcomes:

1. **Too permissive:** a read-oriented monitor/diagnose call can unexpectedly submit a long GPU successor allocation or cancel/retarget a pending allocation. That creates real shared-cluster resource side effects the user did not necessarily authorize for that family/scope.

2. **Too restrictive:** Executor obeys `do_not_submit_without_user_confirmation` literally and asks again before every successor. That reproduces exactly the manual weekly maintenance burden the user asked the Skill to eliminate.

This is not theoretical. The entire value of the new lifecycle is durable one-active/one-successor maintenance.

### Minimum closure condition

Do not add a ledger, daemon or new state machine.

v0.4 only needs to freeze a **one-time family enrollment / durable authorization contract** using the existing small current-state config or the project/Goal contract.

At minimum:

1. `auto_maintain_successor=true` is inert until the user has explicitly enrolled that exact capacity family for automatic maintenance.
2. The durable authorization scope records enough non-secret facts to bound side effects, at least:
   - site;
   - capacity-family id;
   - accepted resource contract / allowed resource envelope;
   - recurrence / target availability window;
   - maximum one intended successor;
   - whether lifecycle-owned state-safe stale-successor cancellation/retarget is authorized.
3. One explicit user action may grant this bounded recurring authorization. After that, normal Slurm Workflows activity may reconcile within the same scope without weekly re-asking.
4. A normal `monitor/diagnose` call may mutate Slurm state only for a family with that valid enrollment. For an unenrolled family it stays read-only and may only report the missing successor / proposed action.
5. Material scope changes — site, capacity family, resource envelope, recurrence, or a broader cancellation right — require a new explicit authorization.
6. Existing pre-v0.3 jobs remain outside the lifecycle-owned mutation scope unless separately proven/authorized under the already-approved replaceable-job rules.

This closes the conflict while preserving the user's low-friction goal.

No weekly human check is required after enrollment; no hidden global Slurm mutation permission is created.

### Other SWR-ER-B2 semantics

Apart from this authority gap, the lifecycle design is sound:

- stable capacity-family identity instead of dated job name;
- reuse compatible running allocation even if display name says “last week”;
- one active + at most one intended successor;
- no duplicate successor if one is already pending;
- actual coverage determines the earliest uncovered recurrence;
- `--begin` is earliest eligibility, not reservation;
- future BeginTime is not claimed to gain age unless site config enables `PriorityFlags=ACCRUE_ALWAYS`;
- BEST_EFFORT is distinguished from a real reservation guarantee;
- unsupported calendar-bounded semantics fail closed instead of recreating the drifting weekly-job design.

SchedMD confirms the proposed calendar primitives:

- `--deadline` removes a pending job when an end before the deadline is no longer possible;
- `--time-min` allows backfill to lower the allocation time limit no lower than the minimum, before allocation, and does not keep changing it after allocation;
- `--begin` only defers eligibility;
- advanced-reservation creation is root/SlurmUser authority.

The proposed `--begin + --deadline + --time + --time-min` combination is therefore a legitimate **candidate** for a calendar-bounded best-effort request, subject to the target-site probe already required by v0.3. It is not a guarantee.

---

# SWR-ER-B3 — CLOSED

## Bridge Kit ownership check

Planner's ownership interpretation is correct.

Current Bridge Kit source explicitly states:

- a real Persistent Run consumer may reuse an existing interactive Slurm allocation;
- Persistent Run owns execution lifetime/persistence, not the scientific task or resource budget;
- resources remain owned by the original Goal/task/workflow;
- the contract has an explicit Resource Boundary;
- Bridge does not globally preauthorize `sbatch`, `salloc`, `srun` or `scancel`.

Therefore:

```text
BRIDGE_CHANGE_REQUIRED = NO
```

Slurm Workflows can consume persistent intent and the Goal's resource boundary without moving Slurm scheduling policy into Bridge Kit.

## Backend architecture is not too ambiguous

The product-level mode distinction is sufficiently frozen:

- finite unattended compute -> batch;
- persistent reusable workspace/capacity -> persistent allocation;
- short debugging shell -> debug interactive.

SchedMD confirms:

- `salloc --no-shell` leaves an active Slurm allocation with a JobId and no running command/task;
- later `srun --jobid=<id>` can create a job step inside that allocation.

v0.3 correctly does **not** claim that this already works for Longleaf's desired detached successor lifecycle. It requires a bounded site capability probe before automatic production use.

It also defines the acceptable semantic fallback: a site-approved capacity-holder backend may acquire/hold the allocation if `salloc --no-shell` cannot support the caller/disconnect lifecycle, but scientific payload must remain separate from the holder.

That is a bounded site-specific implementation choice, not an unresolved product architecture.

The proposal also correctly refuses to claim that `salloc` bypasses the scheduler or has better queue priority.

---

# Complexity review

v0.3 remains a small architecture:

```text
workload intent
-> workload mode

sticky accepted resource contract
-> CPU / memory / GPU / walltime

site authority + local preference
-> legal route / availability target

live scheduler/allocation state
-> reuse or one intended successor

scheduler evidence
-> advisory probe / native widening / fail closed
```

The new `slurm-workflows.toml` is current declarative contract state, not a history DB or workflow state machine.

The proposal does not add:

- queue-history DB;
- scheduler predictor;
- custom scheduler;
- daemon/watcher;
- dependency remapper;
- hostname-ranking core.

No simplification beyond the remaining authorization fix is required.

---

# Gate review

G1–G6 remain valid.

G7 and G8 are justified as distinct new capabilities, not gate inflation:

- **G7** proves resource-contract stability/right-sizing; its failure is resource flapping, OOM/timeout under-sizing, or silent routing downgrade.
- **G8** proves workload-mode + reusable capacity lifecycle; its failure is batch-only handling, duplicate successor creation, false reservation guarantees, or failure to reuse compatible capacity.

The existing G8 cases are good, but after closing SWR-ER-B2-A it must also prove:

> enrolled auto-maintain family -> bounded successor mutation allowed without repeat prompt; unenrolled family -> monitor/diagnose remains read-only and cannot submit/cancel.

No G9 is needed for this authority distinction; it belongs inside G8.

---

# Site-validation boundary

The v0.3 principle is correct:

- P-A calendar semantics;
- P-B persistent allocation backend;
- P-C in-place Partition widening

are conceptual questions, not a mandate for three real jobs.

A later execution package must combine/minimize real probes where one harmless allocation can safely answer multiple questions and must separately authorize any real Slurm mutation.

No real probe is required for this architecture review.

---

# Version / scope

Architecture docs: NO BUMP.

If the amended architecture is later implemented and released on one final candidate:

- standalone `slurm-workflows`: `0.1 -> 0.2`;
- repository: next PATCH from actual release-time `VERSION`;
- central Plugins: all `NO_BUMP`;
- Bridge Kit: NO CHANGE.

---

# External sources independently checked

SchedMD official documentation checked 2026-09-24:

1. `sacct` — accounting fields, MaxRSS semantics, Comment storage caveat  
   https://slurm.schedmd.com/sacct.html
2. `sbatch` — `--comment`, `--begin`, `--deadline`, `--time`, `--time-min`  
   https://slurm.schedmd.com/sbatch.html
3. Multifactor Priority — eligible waiting age  
   https://slurm.schedmd.com/priority_multifactor.html
4. `slurm.conf` — `PriorityFlags=ACCRUE_ALWAYS`, `AccountingStoreFlags=job_comment`  
   https://slurm.schedmd.com/slurm.conf.html
5. `salloc` — `--no-shell`, `--comment`, deadline/time-min support  
   https://slurm.schedmd.com/salloc.html
6. `srun` — `--jobid` creates a step in an already allocated job  
   https://slurm.schedmd.com/srun.html
7. Advanced Reservations — creation/update/delete authority  
   https://slurm.schedmd.com/reservations.html
8. Sharing Consumable Resources — memory as scheduling consumable under relevant select configuration  
   https://slurm.schedmd.com/cons_tres_share.html

No external evidence contradicts v0.3's resource, calendar, or persistent-allocation direction. The remaining blocker comes from the interaction between v0.3's automatic mutation behavior and the repository's current site hard authority.

---

## Final fields

```text
RESULT = REVISE
SWR-ER-B1 = CLOSED
SWR-ER-B2 = OPEN
SWR-ER-B3 = CLOSED

PASS_OBJECT = NOT_APPLICABLE
PASS_SCOPE = NOT_APPLICABLE

BRIDGE_CHANGE_REQUIRED = NO
PROPOSAL_COMMIT = f9c0e3abbffaa6677c1f0acec510c47106d66aa1
```
