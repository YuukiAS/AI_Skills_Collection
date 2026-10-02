# Slurm Workflows Routing Refactor Prefinal Repair Result R4

RESULT = READY_FOR_FINAL_CRITIC
TASK = hpc--slurm-workflows-routing-refactor
BRANCH = reviewed/hpc--slurm-workflows-routing-refactor
WORKTREE = /tmp/ai-skills-hpc-slurm-workflows-routing-refactor
START_MAIN = 98721a202bc557c0b9c0800e66e50cab466bfba2
FORMAL_RELEASE_BASELINE = a7028195f3e97d32d51c32ef8c87f658f92048e5
PRE_R4_REVIEWED_REMOTE = 765c1457fdde409dd6139d96592216bbbded4e1c
PREVIOUS_PRODUCT_CANDIDATE = 0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d
FINAL_CANDIDATE = d9da1dde5731f27f029dc1507a457a39b510d610

## Scope And Drift

- Existing worktree was recoverable at `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`.
- `origin/main` was fetched and observed at `98721a202bc557c0b9c0800e66e50cab466bfba2`.
- Local reviewed branch was fast-forwarded to `origin/reviewed/hpc--slurm-workflows-routing-refactor` at `765c1457fdde409dd6139d96592216bbbded4e1c`.
- `origin/main` is the merge base and an ancestor of the reviewed branch, so no additional main merge was required in R4.
- No new Slurm production/source/test/version/generated semantic drift was found.
- No rebase, force-push, main integration, release advancement, successor task, new branch, or new worktree occurred.

## R4 Blocker

SWR-PF5 = CLOSED
- Recurrence-derived family-local datetimes still use Python standard-library `zoneinfo.ZoneInfo`.
- Local recurrence construction now checks both `fold=0` and `fold=1`, round-trips each candidate through UTC and back to the family timezone, and treats ambiguous/nonexistent local wall-clock times as calendar errors.
- `America/New_York` Sunday `2026-03-08 02:30` spring-forward gap returns `read_only_proposal`, reason `nonexistent_recurrence_local_time`, and `successor_mutation = False`.
- `America/New_York` Sunday `2026-11-01 01:30` fall-back fold returns `read_only_proposal`, reason `ambiguous_recurrence_local_time`, and `successor_mutation = False`.
- Both fold/gap fixtures use enrollment digests generated from their own modified family scope, so the evidence does not depend on stale-digest rejection.
- Calendar errors are propagated into `capacity_reconcile`; they are not represented as empty windows that could fall through to mutation planning.
- Ordinary unique family-local times continue to plan normally.

PF5 deterministic G8 evidence:
- UTC invocation + `America/New_York` Monday `09:00` still produces `2026-09-28T09:00:00-04:00`, not `09:00+00:00`.
- DST boundary evidence still proves `2026-10-26T09:00:00-04:00` followed by `2026-11-02T09:00:00-05:00`.
- Explicit aware UTC seed remains the first absolute occurrence, while N+1 is generated as family-local New York Monday 09:00 across DST.
- Invalid timezone still uses a digest matching the invalid timezone scope and fails closed/read-only.
- Fold/gap recurrence wall-clock cases fail closed without successor mutation.

## Prior Blockers

SWR-PF1 = CLOSED / REGRESSION PASS
- Durable top-level `timezone` remains in the normalized enrollment digest scope.
- Same timezone with only occurrence date changes remains valid; changing timezone invalidates the old digest.

SWR-PF2 = CLOSED / REGRESSION PASS
- Explicit `target_occurrence` remains the first window.
- Recurring families continue to N+1/N+k after the explicit first occurrence.
- One-off explicit targets without recurrence remain single-window `reuse_active`.

SWR-PF3 = CLOSED / REGRESSION PASS
- Installed persistent-capacity G6 normal-entry coverage remains intact.

SWR-PF4 = CLOSED / REGRESSION PASS
- Repo-targeted tracked identity still does not leak raw or normalized private `ClusterName`; explicit local aliases remain stable.

## Required Fields

STICKY_STATE_PERSISTENCE = PASS
CALENDAR_CAPACITY_COVERAGE = PASS
ENROLLMENT_DIGEST_FAIL_CLOSED = PASS
LEGACY_CONFIG_CLEANUP = PASS
DOCTOR_SITE_AWARE = PASS
G6_TRUE_NORMAL_ENTRY = PASS
PUBLIC_SAFE_GENERATED_REFERENCE = PASS

REAL_SLURM_MUTATION = NO
- No `sbatch`, `salloc`, `scancel`, mutating `scontrol`, or real weekly GPU enrollment was run.
- Live-path evidence used deterministic fake Slurm commands on PATH only.

REPOSITORY_VERSION = 5.4.1
SLURM_WORKFLOWS_VERSION = 0.3
CENTRAL_PLUGINS = NO_BUMP
BRIDGE_KIT = NO_CHANGE

TRACKING_ISSUE = #95
- URL: https://github.com/YuukiAS/AI_Skills_Collection/issues/95
- Existing maintenance tracking remains the single top-level Slurm Workflows regression item.
- Canonical source backlink remains `docs/skill-todos/slurm-workflows.md` with `tracking: #95`.
- Reader-facing body was updated after Clear Writing replay with installed `writing-style@yuukias-ai-skills`.
- Clear Writing run id: `20261002T112746Z-8baab7c9ee62`.
- Issue body now anchors product candidate `d9da1dde5731f27f029dc1507a457a39b510d610`, R4 progress, fold/gap fail-closed evidence, and next action.

PROJECT_STATUS = DOING
- `gh issue view 95 --json state,labels,projectItems,body,url` reported state `OPEN` and Project `AI Skills Maintenance` status `DOING`.
- Labels remain `maintenance-track`, `kind:regression`, `scope:standalone-skill`, `area:standalone-skill`.
- Resolution commit remains intentionally empty before final Critic and integration/release closure.

INTEGRATED_TO_MAIN = NO
FORMAL_RELEASE_ADVANCED = NO
FINAL_CRITIC = PENDING

## Gate Evidence

All final gate evidence below is bound to product candidate `d9da1dde5731f27f029dc1507a457a39b510d610`.

- `python -m py_compile skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py tests/test_slurm_workflows.py` -> PASS.
- PF5/G8 targeted: `python -m unittest tests.test_slurm_workflows.SlurmWorkflowsRoutingTests.test_g8_modes_capacity_reuse_successor_and_enrollment` -> PASS, 1 test, 0.072s.
- Full G1-G8: `python -m unittest tests.test_slurm_workflows` -> PASS, 13 tests, 2.982s.
- `python -m unittest tests.test_skill_update` -> PASS, 11 tests, 1.037s.
- `python scripts/skills.py validate` -> PASS, 154 active skills, 18 profiles.
- `python scripts/skills.py audit --all` -> PASS, exit 0; output contained profile/domain budget advice only.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS, `plugins=10`, `active_skills=29`, `source_snapshots=72`, `over_budget=0`.
- `python -m unittest discover -s tests` -> PASS, 320 tests, 102.555s.

## Version Decision

Repository bump decision: PATCH
Reason: repository remains on the current release repair line at `5.4.1`; this task does not add a new repository-level user capability beyond the already prepared patch release.

Affected standalone skills:
- `slurm-workflows`: `0.2` -> `0.3`
  Reason: the repair changes user-facing Slurm routing/capacity behavior and is ready for final Critic review on the existing `0.3` standalone-skill release candidate.

Affected central plugins:
- all central plugins: NO_BUMP
  Reason: no central Marketplace plugin production behavior changed.

Bridge Kit: NO CHANGE
Reason: this task did not modify Bridge Kit source, distribution, runtime, or release state.

## Independent Critic Prompt

Review `YuukiAS/AI_Skills_Collection` task `hpc--slurm-workflows-routing-refactor` on branch `reviewed/hpc--slurm-workflows-routing-refactor`.

Use product candidate:

```text
d9da1dde5731f27f029dc1507a457a39b510d610
```

Read:

- `results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R4_2026-10-02.md`
- `results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R4_2026-10-02.md`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`
- changed source and tests in candidate `d9da1dde5731f27f029dc1507a457a39b510d610`
- tracking artifacts under `results/hpc--slurm-workflows-routing-refactor/tracking/`
- Issue #95 and `docs/skill-todos/slurm-workflows.md` as needed

Independently verify whether the bounded R4 prefinal repair contract is satisfied:

- SWR-PF5: recurrence local datetime construction uses standard-library `ZoneInfo`; it checks `fold=0` and `fold=1` with UTC round-trip; ambiguous/fold and nonexistent/gap local wall-clock times both return `read_only_proposal` with `successor_mutation=False`; implementation does not default to either fold, does not map a gap to an instant, and does not route calendar errors through empty-window mutation planning.
- G8 coverage includes `America/New_York` 2026-03-08 Sunday `02:30` spring-forward gap and 2026-11-01 Sunday `01:30` fall-back fold, each with a valid matching enrollment digest.
- PF5 previously accepted behavior remains intact: UTC invocation + New York local 09:00, DST offset update across 2026-10-26 -> 2026-11-02, explicit aware first occurrence plus N+1 recurrence, invalid/unavailable timezone fail-closed, and explicit one-off behavior.
- SWR-PF1/PF2/PF3/PF4 remain closed with regression coverage.
- Latest compatible `origin/main` is contained in the reviewed branch without rebase/force-push and without relevant Slurm semantic conflict.
- PF5/G8 targeted test, complete G1-G8, generated parity, and full suite are credible and bound to product candidate `d9da1dde5731f27f029dc1507a457a39b510d610`.
- Versions remain repository `5.4.1`, standalone `slurm-workflows 0.3`, central Plugins `NO_BUMP`, Bridge Kit `NO CHANGE`.
- Issue #95 remains the single top-level maintenance tracking issue, remains `DOING`, keeps classification/Area/source backlink/empty Resolution commit, and its body has been updated through Clear Writing to the current candidate and next action.
- `REAL_SLURM_MUTATION = NO`; no main integration, release advancement, or self-approval occurred.

Return `PASS` only if the product candidate can proceed to integration/release closure. Otherwise return `REVISE` with concrete file/line findings.
