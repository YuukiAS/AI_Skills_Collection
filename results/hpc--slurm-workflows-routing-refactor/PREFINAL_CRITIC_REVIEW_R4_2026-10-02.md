# Slurm Workflows — Pre-final Critic Review R4

Date: 2026-10-02  
Role: AI Research Stack Independent Critic  
Review stage: PRE_FINAL_IMPLEMENTATION_REVIEW_R4

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `reviewed/hpc--slurm-workflows-routing-refactor`
- Planner R3 handoff: `results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R3_2026-10-02.md`
- previous Critic review: `results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R3_2026-10-02.md` @ `3006227a139e8b21fd416540a335ff8dea2d3340`
- exact product candidate: `0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d`
- RESULT handoff commit before this review: `76cb3bc321910069734fc8461d83e11248204d94`
- current main observed during review: `98721a202bc557c0b9c0800e66e50cab466bfba2`
- current formal release observed during review: `a7028195f3e97d32d51c32ef8c87f658f92048e5`

The candidate contains current main. No post-candidate Slurm production/source/test/version drift was found.

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

The R3 repair correctly fixes family-local wall-clock recurrence, UTC/local conversion, DST offset changes, explicit-aware first occurrences, and invalid/unavailable timezone fail-closed behavior.

PF5 remains open for one direct clause of the frozen R3 handoff: ambiguous or nonexistent local wall-clock times are still silently interpreted instead of failing closed.

---

## SWR-PF5 — still OPEN: fold/gap local times do not fail closed

### Frozen requirement

Planner R3 states:

> “本轮不新增更大的 ambiguous/nonexistent-local-time 配置体系；如果实现遇到无法安全解释的 timezone/local-time 情况，应 fail closed，而不是猜测并继续 mutation。”

This is part of the exact bounded PF5 repair contract.

### What is now correct

Candidate `slurm_routing.py`:

- uses standard-library `zoneinfo.ZoneInfo`;
- converts invocation `now` into the family timezone;
- reconstructs each weekly recurrence from family-local date + wall-clock time;
- therefore changes UTC offset across DST instead of copying a fixed offset;
- preserves an explicit aware first occurrence as an absolute instant;
- returns `read_only_proposal` for invalid/unavailable timezone keys.

The current G8 cases credibly prove those behaviors.

### Remaining source defect

`_recurrence_datetime()` currently does only:

```python
datetime.combine(local_date, parsed_time, tzinfo=ZoneInfo(...))
```

There is no check for a local wall-clock time that lies:

- in a fall-back fold, where the same local time maps to two real instants; or
- in a spring-forward gap, where that local time does not exist.

Python's timezone model intentionally allows such datetime objects to be constructed. A fold defaults to one reading unless `fold` is explicitly chosen, and a gap can also produce an invalid local datetime; constructors do not automatically reject these cases.

Therefore a recurrence such as a DST-transition Sunday around 01:xx/02:xx can reach successor planning with a silently chosen/nonexistent instant.

### Causal risk

The product contract is a generic open-source calendar-capacity mechanism, not a Monday-09:00-only implementation.

At a timezone transition, a user's recurring capacity target can be shifted to the wrong real instant or to a nonexistent local time, while the planner still reports a valid calendar target and may authorize a recurring successor mutation.

That directly violates the frozen fail-closed requirement.

### Minimum closure

Do not add a calendar framework or policy selector.

Add one small local-time validity check around recurrence datetime construction:

1. detect whether the requested local wall-clock maps to no real instant (gap) or more than one real instant (fold);
2. for either case, return a stable calendar error to reconciliation;
3. `capacity_reconcile` must return `read_only_proposal`, `successor_mutation=False`;
4. ordinary unambiguous local times keep current behavior;
5. add deterministic G8 regressions using a timezone/date/time that crosses a known fold and gap.

A round-trip check through UTC and/or explicit comparison of `fold=0` versus `fold=1` is sufficient; no third-party dependency is needed.

Owner: `slurm-workflows` PF5 calendar validation.

---

## PF1-PF4 and the rest of PF5

No prior blocker is reopened.

### PF1 — CLOSED
Timezone remains bound into the durable enrollment digest; changing it invalidates old authorization.

### PF2 — CLOSED
Explicit current occurrence continues to later recurrences; one-off explicit targets remain one-off.

### PF3 — CLOSED
Installed persistent-capacity G6 evidence remains present.

### PF4 — CLOSED
Repo-targeted identity privacy remains protected.

### PF5 — partial closure accepted
The following R3 requirements are accepted:

- `ZoneInfo` usage;
- UTC invocation + New York local 09:00;
- DST offset transition;
- explicit aware first occurrence;
- invalid/unavailable timezone fail closed.

Only ambiguous/nonexistent local-time handling remains open.

---

## Gates / versions / tracking

Recorded validation is candidate-bound and otherwise coherent:

- PF5/G8 targeted: PASS;
- full G1-G8: PASS, 13 tests;
- `tests.test_skill_update`: PASS, 11 tests;
- validate/audit: PASS;
- generated Marketplace parity: PASS;
- full suite: PASS, 320 tests.

The current tests simply do not exercise the fold/gap fail-closed clause, so these passes cannot close the remaining PF5 subcase.

Version direction remains accepted:

```text
Repository = 5.4.1
slurm-workflows = 0.3
central Plugins = NO_BUMP
Bridge Kit = NO CHANGE
```

Issue #95 is current, remains the single open top-level tracking item, and its body is anchored to candidate `0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d`. Project lifecycle should remain `DOING`.

No real Slurm mutation is required for this repair.

---

## External standards check

Python's official timezone documentation confirms that `ZoneInfo` handles IANA timezone offsets and DST transitions. PEP 495 additionally states that ambiguous local times use the `fold` attribute, while missing times in a forward clock jump can still be constructed and do not represent a valid real instant; constructors do not perform strict validity checking automatically.

This directly supports fail-closed detection in the application layer rather than assuming `datetime.combine(..., tzinfo=ZoneInfo(...))` validates a local wall-clock.

Slurm calendar semantics remain unchanged and do not require architecture changes.

References:

- https://docs.python.org/3/library/zoneinfo.html
- https://peps.python.org/pep-0495/
- https://slurm.schedmd.com/sbatch.html

## Final fields

```text
RESULT = REVISE
FINAL_CANDIDATE = 0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d

SWR-PF1 = CLOSED
SWR-PF2 = CLOSED
SWR-PF3 = CLOSED
SWR-PF4 = CLOSED
SWR-PF5 = OPEN

PF5_FAMILY_TIMEZONE = PASS
PF5_DST_OFFSET_UPDATE = PASS
PF5_EXPLICIT_AWARE_SEED = PASS
PF5_INVALID_ZONE_FAIL_CLOSED = PASS
PF5_FOLD_GAP_FAIL_CLOSED = FAIL

VERSION_CLOSURE = PASS
TRACKING_ISSUE = PASS
CURRENT_MAIN_DRIFT = NONE_RELEVANT
REAL_SLURM_MUTATION_REQUIRED_FOR_REPAIR = NO
BRIDGE_CHANGE_REQUIRED = NO
READY_FOR_INTEGRATION = NO
```

This review does not authorize main integration, formal release advancement, real Slurm mutation, or a new task/branch/worktree.
