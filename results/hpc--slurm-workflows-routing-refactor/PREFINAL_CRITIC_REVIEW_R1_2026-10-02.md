# Slurm Workflows — Pre-final Critic Review R1

Date: 2026-10-02  
Role: AI Research Stack Independent Critic  
Review stage: PRE_FINAL_IMPLEMENTATION_REVIEW

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `reviewed/hpc--slurm-workflows-routing-refactor`
- reviewed branch tip before this review: `ea976a729e302434de94c4dead86d2b78feac35d`
- exact product candidate: `a2b511ebaca3abebb0515cd9acec8c35b58ec1d6`
- current main observed during review: `1c7ff0d5d2037e7a0ef2ba4bf44bdb829d3c26e6`
- current formal release observed during review: `a7028195f3e97d32d51c32ef8c87f658f92048e5`

Current main has advanced after the frozen candidate only through Project Instructions Editor docs/TODO work. No new Slurm production/source/test semantic drift was found in that post-candidate main movement.

## Result

```text
RESULT = REVISE
READY_FOR_INTEGRATION = NO
```

Version closure, tracking Issue #95, source backlink, Clear Writing receipts, central-plugin no-bump boundary, and no-real-Slurm-mutation boundary are acceptable.

The candidate still has four direct blockers against the already-approved v0.4/v0.6 capacity/enrollment contract and the v0.6 execution Gate Matrix.

---

## SWR-PF1 — Enrollment digest does not bind the full authorized mutation scope

### Requirement

Proposal v0.4 §7.2 freezes at least:

- site;
- capacity family;
- activation scope;
- accepted resource contract;
- allowed resource envelope;
- recurrence / target availability window;
- max intended successor;
- successor-submit permission;
- optional lifecycle-owned stale-successor cancel/retarget permission.

The digest exists specifically so a material mutation-scope change invalidates the old enrollment.

### Direct source evidence

`skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py:662-672` hashes only:

- `local_site_id`;
- `capacity_family_id`;
- `activation_scope`;
- `accepted_resource_contract`;
- `allowed_resource_envelope`;
- `recurrence`;
- constant `max_successor=1`.

It does **not** bind the separate calendar scope fields consumed by `next_capacity_window`, including `target_ready_by`, `successor_lead_time`, `minimum_useful_duration`, `latest_useful_end/cutoff`. It also does not bind the authorized action scope such as successor submission / stale-successor retarget authorization.

The current G8 test at `tests/test_slurm_workflows.py:184-274` checks missing digest and an arbitrary wrong digest, but does not mutate these omitted scope fields after enrollment and prove the old digest becomes invalid.

### Causal risk

An enrollment can remain valid after a material calendar/availability scope change that the approved architecture says must require fresh authorization. That weakens the durable recurring-mutation boundary.

### Minimum closure

Normalize one mutation-relevant scope object and compute the digest from every field that can materially expand recurring mutation authority. Add tests proving that changing calendar/window scope or authorized actions invalidates the old digest while unchanged same-scope recurrence stays valid.

Owner: implementation / `slurm-workflows`.

---

## SWR-PF2 — Capacity reconciliation stops at the first covered occurrence instead of maintaining the earliest uncovered target

### Requirement

The approved lifecycle is:

```text
at most one compatible active allocation
+
at most one lifecycle-owned intended successor
```

If an active allocation covers the current/next target, the system must advance to the **earliest uncovered recurrence** and reconcile a successor for that target when authorized.

This is the original product reason for not treating a dated weekly job as the lifecycle identity.

### Direct source evidence

`slurm_routing.py:604-611` computes one `window` and immediately returns `reuse_active` when a compatible running allocation covers that window.

It never advances recurrence and asks whether the next recurrence is now the earliest uncovered target.

The G8 test at `tests/test_slurm_workflows.py:207-215` explicitly accepts this early return and does not cover:

```text
active allocation covers occurrence N
+ no successor for occurrence N+1
+ valid enrollment
-> maintain exactly one successor for N+1
```

There is an additional edge in `next_capacity_window` at lines 542-545: once the recurring start time has passed, it always advances seven days, even when the current occurrence may still be inside its useful window. That is not yet demonstrated to match the approved “earliest uncovered target” semantics.

### Causal risk

The user's original weekly-GPU problem can recur in a different form: a long-running allocation covering the immediate target causes reconciliation to stop, leaving the first actually uncovered future target without a successor.

### Minimum closure

Make reconciliation reason over the earliest uncovered occurrence, not just one computed next-start occurrence. Add deterministic cases for:

1. active capacity covers occurrence N -> inspect/maintain N+1;
2. active + existing successor for N+1 -> no duplicate;
3. an ongoing current window whose start is already in the past;
4. at most one lifecycle-owned successor invariant.

Owner: implementation / `slurm-workflows`.

---

## SWR-PF3 — Required G6 persistent-capacity installed normal entry is missing

### Requirement

Execution Plan v0.6 §10.3 explicitly requires:

> Installed Skill/helper consumes a user-local enrolled capacity fixture, reuses compatible capacity, and plans exactly one missing successor only for a matching workload.

G6 is not satisfied by helper/unit tests alone.

### Direct source evidence

`tests/test_slurm_workflows.py` contains installed-path G6 coverage for environment discovery/routing, but no installed-path persistent-capacity test.

The only capacity/enrollment test is `test_g8_modes_capacity_reuse_successor_and_enrollment`, which loads the source helper directly.

The branch `RESULT.md` lists four G6 tests, none covering Execution Plan §10.3.

### Causal risk

The release would claim the installed normal path provides the persistent-capacity lifecycle even though that part of the product has only helper-level evidence. This is exactly the Capability Gate failure mode the repository policy forbids.

### Minimum closure

Add one installed-normal-entry G6 fixture that materializes the exact candidate Skill/helper and consumes a user-local capacity/enrollment state through the installed path. It must prove:

- matching persistent workload can reuse compatible capacity;
- one missing successor is planned only with valid enrollment;
- unrelated workload remains read-only;
- state/digest behavior is the installed candidate's behavior, not the source helper imported directly.

Owner: implementation / Gate G6.

---

## SWR-PF4 — Repo-targeted “public-safe” site identity still leaks a raw ClusterName-derived identifier

### Requirement

The approved privacy contract says private/raw cluster identity that is unsuitable for tracked output must remain local or be represented by a safe local alias/hash.

The repair prompt explicitly required tests with obviously private fake values.

### Direct source evidence

`slurm_routing.py:65-74` implements `_safe_id` by lower-casing/sanitizing the ClusterName and only hashes when the string is longer than 48 characters.

`scripts/skills.py:1200-1204` adopts that live `local_site_id`, and `scripts/skills.py:1271` plus manifest lines 1373-1375 write it into repo-targeted generated artifacts.

The privacy fixture at `tests/test_slurm_workflows.py:310-363` uses `ClusterName=PrivateClusterSecret`, then explicitly expects:

```text
plan["local_site_id"] == "privateclustersecret"
```

and only asserts that the case-sensitive string `PrivateClusterSecret` is absent. The lower-cased raw identity is therefore still allowed into tracked output.

### Causal risk

A cluster/site identifier that was intentionally treated as private can be committed to a project merely because sanitization changed its case/punctuation. The generated artifact is not actually public-safe under the frozen privacy contract.

### Minimum closure

Separate runtime/local identity from tracked public-safe identity. For repo-targeted generated output, use an explicit local alias when provided; otherwise use a stable non-reversible alias/hash when the discovered ClusterName is not approved as public. Update the regression so the normalized raw token (for example `privateclustersecret`) is also forbidden from the tracked reference/manifest.

Owner: shared environment/install path + G1/G6 privacy coverage.

---

## Accepted / non-blocking findings

### Version closure

Candidate metadata is internally consistent:

- repository `5.4.0 -> 5.4.1` PATCH;
- standalone `slurm-workflows 0.2 -> 0.3`;
- central Plugins: NO_BUMP;
- Bridge Kit: NO CHANGE.

This matches the current repository patch-release rule for an improvement to an existing standalone capability.

### Tracking

Issue #95 exists, is open, and has exactly:

- `maintenance-track`;
- `kind:regression`;
- `scope:standalone-skill`;
- `area:standalone-skill`.

Candidate `docs/skill-todos/slurm-workflows.md` contains `tracking: #95`.

Clear Writing receipts are present before reader-facing Issue copy creation/update.

The user/Executor reports Project Status `DOING` / Area `standalone-skill`; this connector surface does not independently expose private GitHub Project field readback. No evidence reviewed here contradicts that lifecycle state.

### Main drift after candidate freeze

Current main moved after candidate freeze only through unrelated Project Instructions Editor docs/TODO files. No Slurm semantic conflict was found. This is not a blocker by itself; integration preflight still must reconcile current main without altering reviewed Slurm production/release bytes.

### External Slurm semantics

SchedMD official documentation was independently rechecked:

- `sbatch --test-only` validates/estimates without submitting a job;
- `--deadline` removes a job when it can no longer finish by the deadline;
- `--time-min` permits backfill to lower the allocation time limit before allocation, not after;
- `salloc --no-shell` creates an active allocation/JobId with no task, and later `srun --jobid` can use it.

These facts support the approved architecture; the blockers above are implementation/evidence defects, not a need to redesign Slurm behavior.

Official sources:
- https://slurm.schedmd.com/sbatch.html
- https://slurm.schedmd.com/salloc.html
- https://slurm.schedmd.com/srun.html

---

## Review conclusion

```text
RESULT = REVISE
FINAL_CANDIDATE = a2b511ebaca3abebb0515cd9acec8c35b58ec1d6

SWR-PF1 = OPEN
SWR-PF2 = OPEN
SWR-PF3 = OPEN
SWR-PF4 = OPEN

VERSION_CLOSURE = PASS
TRACKING_ISSUE = PASS
CURRENT_MAIN_DRIFT = UNRELATED / NON_BLOCKING
REAL_SLURM_MUTATION_REQUIRED_FOR_REPAIR = NO
BRIDGE_CHANGE_REQUIRED = NO
READY_FOR_INTEGRATION = NO
```

This review does not authorize main integration, release advancement, real Slurm mutation, or a new task/branch.
