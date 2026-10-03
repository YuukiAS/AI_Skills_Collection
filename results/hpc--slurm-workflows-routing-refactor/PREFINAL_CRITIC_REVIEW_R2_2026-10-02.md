# Slurm Workflows — Pre-final Critic Review R2

Date: 2026-10-02  
Role: AI Research Stack Independent Critic  
Review stage: PRE_FINAL_IMPLEMENTATION_REVIEW_R2

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `reviewed/hpc--slurm-workflows-routing-refactor`
- Planner repair handoff: `results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R1_2026-10-02.md` @ `133c2f7f68cd6209df9f8db616f12c69eeb9bd66`
- previous Critic review: `results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R1_2026-10-02.md` @ `f59b8f35793f661bde454a85291fee65e9fa53c4`
- exact product candidate: `ed48521941f82eeedcfc490c55fa175780db64c9`
- RESULT handoff commit before this review: `ab5a5cae37353036dc1ab01c34f123075ada6cf9`
- current main observed during review: `ee852eff9278fda18952f687dda12bd787f01f72`
- current formal release observed during review: `a7028195f3e97d32d51c32ef8c87f658f92048e5`

The candidate is a descendant of current main. No post-candidate Slurm production/source/test drift was found.

## Result

```text
RESULT = REVISE
READY_FOR_INTEGRATION = NO

SWR-PF1 = OPEN
SWR-PF2 = OPEN
SWR-PF3 = CLOSED
SWR-PF4 = CLOSED
```

The R1 repair materially improved the candidate. PF3 and PF4 are now closed. PF1 and PF2 remain open because two direct parts of the exact Planner repair contract are still not implemented/tested.

---

## SWR-PF1 — OPEN

### Requirement

The R1 Planner handoff explicitly requires one normalized enrollment scope to bind:

- local site id;
- capacity family;
- activation scope;
- accepted resource contract;
- allowed resource envelope;
- durable recurrence **and timezone**;
- durable availability-window fields;
- max successor;
- successor-submit permission;
- optional stale-successor cancel/retarget permission.

Changing any durable scope field must invalidate the old digest; same recurring occurrence under unchanged scope must remain valid.

### What improved

Candidate `slurm_routing.py` now has one shared digest path:

- `_scope_window_contract()`;
- `_scope_action_contract()`;
- `_scope_digest()`;
- `_valid_enrollment()`;
- CLI `scope-digest` also calls the same `_scope_digest()`.

The digest now covers recurrence, target readiness, lead time, minimum/latest useful window fields, calendar-bound submission, and action scope. Tests show window/action changes invalidate the old digest.

### Remaining direct gap

The normalized scope does **not** bind top-level family `timezone`.

In `_scope_window_contract()`, the returned scope contains recurrence and window fields but no `family.get("timezone")`.

The G8 fixture contains no timezone and therefore cannot prove that changing the durable timezone invalidates enrollment.

This is not a new requirement: the Planner R1 handoff explicitly listed “durable recurrence / timezone”, and the approved capacity-family architecture freezes timezone as part of the family scope.

### Concrete risk

A weekly 09:00 capacity family can be moved from one timezone to another without changing the existing digest. That changes the real target window while preserving durable recurring mutation authority.

### Minimum closure

Add timezone to the normalized digest scope and one deterministic G8 regression:

```text
same family + same recurrence/window + timezone A
-> digest A

change only durable timezone to B
-> old digest invalid / read-only
```

No new architecture or config system is needed.

Owner: `slurm-workflows` implementation.

---

## SWR-PF2 — OPEN

### Requirement

The R1 Planner handoff requires reconciliation to find the **earliest uncovered recurrence** and specifically covers:

- current occurrence N still inside its useful window;
- active allocation covers N -> continue to N+1;
- active spans multiple recurrences -> continue until the first uncovered occurrence;
- existing successor for that uncovered occurrence -> no duplicate;
- invariant remains at most one compatible active + one lifecycle-owned intended successor.

### What improved

The candidate now:

- produces a bounded sequence of recurrence windows;
- keeps the current occurrence when its start has passed but its useful window is still active;
- scans across windows covered by one active allocation;
- plans N+1/N+k rather than returning immediately;
- fails closed on multiple compatible active allocations or multiple lifecycle-owned successors.

The new G8 cases cover these recurrence-derived scenarios.

### Remaining direct gap

`capacity_windows()` has a separate explicit-target path:

```python
start = target_occurrence.start / target_start
if start is not None:
    return [one_window_only]
```

When a recurring family receives an explicit current `target_occurrence`, reconciliation therefore has only one window.

If the active allocation covers that occurrence, the loop exhausts that one-element list and returns `reuse_active`; it never advances using the family's recurrence to N+1.

There is no G8 case using `target_occurrence`; the current test bank only exercises recurrence-derived windows.

### Concrete risk

A normal caller that supplies the current occurrence explicitly can reproduce the same original lifecycle defect:

```text
explicit occurrence N
+ active covers N
+ recurrence defines N+1
+ valid enrollment
+ no successor for N+1
-> candidate returns reuse_active
-> N+1 remains uncovered
```

### Minimum closure

Keep the explicit occurrence as the first window, then continue subsequent windows from the durable recurrence when recurrence exists. Add one deterministic G8 test for:

```text
explicit current target_occurrence N
+ active covers N
+ valid recurrence/enrollment
+ no successor
-> plan exactly one successor for N+1
```

Also retain one-off behavior when there is an explicit target but no recurrence.

No daemon/watcher/state machine is needed.

Owner: `slurm-workflows` implementation.

---

## SWR-PF3 — CLOSED

Execution Plan v0.6 §10.3 required installed persistent-capacity normal-entry evidence.

The candidate now includes `test_g6_installed_persistent_capacity_state_normal_entry`, which:

1. materializes the Skill through the real environment path;
2. loads `slurm_routing.py` from the installed Skill;
3. creates persisted capacity/enrollment state at a temporary user-local state path;
4. reloads that state using the installed helper;
5. passes a matching persistent workload with active capacity and verifies planning of exactly one missing successor;
6. verifies an existing successor is kept without duplication;
7. verifies unrelated CPU/batch work remains read-only.

This is the installed-path evidence missing in R1. No real Slurm mutation is used.

---

## SWR-PF4 — CLOSED

The candidate now separates runtime identity from tracked identity:

- raw/live `local_site_id` remains available for runtime/local binding;
- `tracked_site_id` hashes discovered ClusterName when it is not an explicit alias;
- repo-targeted reference/manifest uses the tracked identity;
- the fake `PrivateClusterSecret` regression rejects both the original string and normalized `privateclustersecret` from tracked reference/manifest output;
- explicit local aliases remain stable through the existing known-profile/distinct-local-id path.

This closes the privacy failure from R1 without hiding the runtime identity needed for local routing/state.

---

## Gates / version / tracking

### G6/G8 and candidate identity

The branch RESULT records:

- affected G6/G8: PASS, 6 tests;
- full `tests.test_slurm_workflows`: PASS, 13 tests;
- `tests.test_skill_update`: PASS, 11 tests;
- repository validate/audit: PASS;
- generated Marketplace parity: PASS;
- full suite: PASS, 320 tests.

Those results are explicitly bound to product candidate `ed48521941f82eeedcfc490c55fa175780db64c9`.

PF1/PF2 remain blockers because the gate bank omits the exact cases above, not because the recorded commands are untrusted.

### Version

Still accepted:

```text
Repository = 5.4.1
slurm-workflows = 0.3
central Plugins = NO_BUMP
Bridge Kit = NO CHANGE
```

Current main/release remain `5.4.0`; the candidate is the prepared patch release and must not advance release before final PASS.

### Tracking

Issue #95 remains the single open top-level Slurm Workflows regression item with the correct labels. Project lifecycle remains expected at `DOING`.

Its reader-facing body still points to the previous candidate `a2b511...`. Because this R2 remains REVISE, the next repair handoff should update the Issue's current anchor/next action through the existing Clear Writing-required path; this is a maintenance-truth update, not a new product blocker.

---

## External semantics check

Current SchedMD documentation remains consistent with the frozen design:

- `--begin` defers allocation eligibility until the specified time and does not guarantee exact dispatch;
- `sbatch` submission does not imply immediate resources;
- `salloc --no-shell` / `srun --jobid` semantics remain compatible with the previously approved persistent-allocation design.

No external evidence requires architecture change.

References:

- https://slurm.schedmd.com/sbatch.html
- https://slurm.schedmd.com/salloc.html
- https://slurm.schedmd.com/srun.html

## Final fields

```text
RESULT = REVISE
FINAL_CANDIDATE = ed48521941f82eeedcfc490c55fa175780db64c9

SWR-PF1 = OPEN
SWR-PF2 = OPEN
SWR-PF3 = CLOSED
SWR-PF4 = CLOSED

G6_INSTALLED_PERSISTENT_PATH = PASS
TRACKED_IDENTITY_PRIVACY = PASS
VERSION_CLOSURE = PASS
TRACKING_ISSUE = PASS_WITH_STALE_ANCHOR_TO_REFRESH
REAL_SLURM_MUTATION_REQUIRED_FOR_REPAIR = NO
BRIDGE_CHANGE_REQUIRED = NO
READY_FOR_INTEGRATION = NO
```

This review does not authorize main integration, formal release advancement, real Slurm mutation, or a new task/branch/worktree.
