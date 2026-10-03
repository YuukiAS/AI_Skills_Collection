# Slurm Workflows — Pre-final Critic Review R3

Date: 2026-10-02  
Role: AI Research Stack Independent Critic  
Review stage: PRE_FINAL_IMPLEMENTATION_REVIEW_R3

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `reviewed/hpc--slurm-workflows-routing-refactor`
- Planner R2 handoff: `results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R2_2026-10-02.md`
- previous Critic review: `results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R2_2026-10-02.md` @ `c4a8ef9df090840562107a06f2ab378cbb36dd71`
- exact product candidate: `569f85dde6f676fb2c249f89062c3f81168cac9e`
- RESULT handoff commit before this review: `1e8dc15180fd499a0dcefc241edc4aceb258592b`
- current main observed during review: `98721a202bc557c0b9c0800e66e50cab466bfba2`
- current formal release observed during review: `a7028195f3e97d32d51c32ef8c87f658f92048e5`

Current main has only two post-candidate changes relative to the candidate merge base: one Project Instructions Editor review document and one Bridge consumer-run evidence file. No Slurm production/source/test/version semantic drift was found.

## Result

```text
RESULT = REVISE
READY_FOR_INTEGRATION = NO

SWR-PF1 = CLOSED
SWR-PF2 = CLOSED
SWR-PF3 = CLOSED
SWR-PF4 = CLOSED
SWR-PF5 = OPEN
```

R2 successfully closes every previously open finding. One omitted calendar-semantics defect is now directly visible because the repaired candidate finally carries a real `timezone` field through the capacity-family contract.

This is not an architecture redesign and does not reopen PF1-PF4.

---

## Prior blockers closure

### SWR-PF1 — CLOSED

The normalized enrollment scope now includes top-level `timezone`.

`_scope_digest()`, `_valid_enrollment()`, and CLI `scope-digest` continue to share the same normalized scope.

The G8 regression proves:

- same durable scope and same timezone remain authorized when only occurrence dates move;
- changing only timezone invalidates the old digest and returns reconciliation to read-only.

### SWR-PF2 — CLOSED

Explicit `target_occurrence` is now the first window and, when recurrence exists, the helper continues to later weekly occurrences.

The G8 regression proves:

- active capacity covering explicit N continues to N+1;
- existing lifecycle successor for N+1 is kept without duplication;
- one-off explicit target without recurrence remains single-window `reuse_active`.

### SWR-PF3 — CLOSED

Installed persistent-capacity G6 remains present and uses the materialized installed helper plus persisted/reloaded user-local capacity state.

### SWR-PF4 — CLOSED

Repo-targeted generated reference/manifest continues to use a non-reversible tracked site identity for discovered private ClusterName, while explicit local aliases remain stable. The lower-cased private token is explicitly rejected by regression coverage.

---

## SWR-PF5 — capacity-family timezone is authorization metadata but is not used to compute recurring windows

### Requirement

The already-approved capacity-family contract in Proposal v0.3/v0.4 and Execution Plan v0.6 binds:

```text
recurrence / timezone / target availability window
```

The purpose of the capacity family is to express when reusable capacity should be available. Timezone is therefore part of the calendar semantics, not only part of the authorization digest.

### Direct source evidence

Candidate `slurm_routing.py` now hashes timezone at `_scope_window_contract()`, but recurrence computation does not consume it.

`capacity_windows()`:

- parses `now` and otherwise defaults to `datetime.now(timezone.utc)`;
- builds recurring wall-clock starts with `tzinfo=now.tzinfo`;
- for explicit occurrences, follow-on recurrence uses `tzinfo=start.tzinfo`.

There is no lookup or application of `family["timezone"]`.

The current G8 fixture makes the mismatch observable:

```text
family["timezone"] = "America/New_York"
recurrence start_time = "09:00"
invocation now = ... +00:00
expected target_window start in the test = 09:00 +00:00
```

So the candidate proves that changing timezone invalidates authorization, but the actual weekly target calculation still follows the invocation/default timezone rather than the capacity-family timezone.

### Causal user risk

This can shift recurring availability by hours when the caller/process timezone differs from the frozen capacity-family timezone.

That is a direct failure of the weekly reusable-capacity product contract: a family configured for a local Monday time can be reconciled against a different absolute time while still reporting calendar lifecycle PASS.

It is especially relevant to the generic open-source requirement because the Skill must not depend on whatever timezone the current login process happens to use.

### Minimum closure

Keep the current architecture and state model.

Use the standard timezone identity already frozen in `family["timezone"]` when constructing recurrence-derived windows.

Minimum behavior:

1. if a family timezone is present, recurrence weekday/start-time is interpreted in that timezone;
2. invocation `now` is compared in the family timezone for deciding current/next useful occurrence;
3. explicit aware `target_occurrence` remains the explicit first occurrence, but follow-on recurrence uses the family timezone;
4. DST/offset changes are handled by a timezone-aware standard-library implementation rather than a fixed numeric offset;
5. missing timezone may retain the existing documented fallback if that is the intended contract;
6. invalid/unavailable timezone must fail closed for calendar mutation planning rather than silently reinterpret the schedule in UTC.

Add deterministic G8 coverage with an invocation timestamp whose offset differs from the family timezone and prove that the produced recurrence window represents the family-local wall-clock target.

No daemon, watcher, new state machine, new gate, real Slurm probe, Bridge Kit change, or new release version is needed.

Owner: `slurm-workflows` calendar reconciliation implementation.

---

## Gate / tracking / version findings

The R2 gate evidence is otherwise coherent and candidate-bound:

- targeted PF1/PF2/G8: PASS;
- full `tests.test_slurm_workflows`: PASS, 13 tests;
- `tests.test_skill_update`: PASS, 11 tests;
- validate/audit: PASS;
- generated Marketplace parity: PASS;
- full suite: PASS, 320 tests.

Those passes do not close PF5 because the current G8 assertion encodes the incorrect timezone behavior rather than testing the frozen timezone semantics.

Version direction remains accepted:

```text
Repository = 5.4.1
slurm-workflows = 0.3
central Plugins = NO_BUMP
Bridge Kit = NO CHANGE
```

Issue #95 is current, remains open, carries the correct regression/standalone-skill/area labels, and now points to candidate `569f85dde6f676fb2c249f89062c3f81168cac9e`.

Project lifecycle should remain `DOING` while PF5 is open.

No real Slurm mutation is needed to close PF5.

---

## External semantics check

Current SchedMD documentation remains consistent with the frozen Slurm boundary:

- `--begin` makes a job eligible no earlier than the specified time and does not guarantee exact dispatch;
- `--deadline` removes a job when it can no longer finish before the deadline;
- `--time-min` may let backfill reduce the allocation time limit before allocation;
- `salloc --no-shell` remains an allocation mechanism, not a queue bypass.

No external evidence requires changing the approved architecture. PF5 is entirely a local calendar interpretation defect.

## Final fields

```text
RESULT = REVISE
FINAL_CANDIDATE = 569f85dde6f676fb2c249f89062c3f81168cac9e

SWR-PF1 = CLOSED
SWR-PF2 = CLOSED
SWR-PF3 = CLOSED
SWR-PF4 = CLOSED
SWR-PF5 = OPEN

G6_INSTALLED_PERSISTENT_PATH = PASS
TRACKED_IDENTITY_PRIVACY = PASS
VERSION_CLOSURE = PASS
TRACKING_ISSUE = PASS
CURRENT_MAIN_DRIFT = UNRELATED / NON_BLOCKING
REAL_SLURM_MUTATION_REQUIRED_FOR_REPAIR = NO
BRIDGE_CHANGE_REQUIRED = NO
READY_FOR_INTEGRATION = NO
```

This review does not authorize main integration, formal release advancement, real Slurm mutation, or a new task/branch/worktree.
