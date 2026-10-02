# Slurm Workflows Routing Refactor Prefinal Repair Result R3

RESULT = READY_FOR_FINAL_CRITIC
TASK = hpc--slurm-workflows-routing-refactor
BRANCH = reviewed/hpc--slurm-workflows-routing-refactor
WORKTREE = /tmp/ai-skills-hpc-slurm-workflows-routing-refactor
START_MAIN = 98721a202bc557c0b9c0800e66e50cab466bfba2
FORMAL_RELEASE_BASELINE = a7028195f3e97d32d51c32ef8c87f658f92048e5
PRE_R3_REVIEWED_REMOTE = a9e60d6519b00f57d5e4a7a5d21854b38cec1a06
RECONCILED_MAIN_MERGE = fc09c632
PREVIOUS_PRODUCT_CANDIDATE = 569f85dde6f676fb2c249f89062c3f81168cac9e
FINAL_CANDIDATE = 0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d

## Scope And Drift

- Existing worktree was recoverable at `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`.
- `origin/main` was fetched and observed at `98721a202bc557c0b9c0800e66e50cab466bfba2`.
- Local reviewed branch was fast-forwarded to `origin/reviewed/hpc--slurm-workflows-routing-refactor` at `a9e60d6519b00f57d5e4a7a5d21854b38cec1a06`.
- Diff from prior merged main `72f43c4e` to latest `origin/main` showed no Slurm production source/test/version/generated semantic drift. The new main commits were Project Instructions Editor review documentation and Bridge consumer-run evidence only.
- Latest compatible `origin/main` was merged into the existing reviewed branch with ordinary non-force merge commit `fc09c632`.
- No rebase, force-push, main integration, release advancement, successor task, new branch, or new worktree occurred.

## R3 Blocker

SWR-PF5 = PASS
- Recurrence-derived capacity windows now use Python standard-library `zoneinfo.ZoneInfo` when `family["timezone"]` is present.
- Invocation `now` is converted to the family timezone before current/next useful occurrence selection.
- Weekly `weekday` / `start_time` are interpreted as family-local wall-clock time.
- Weekly follow-on occurrences are rebuilt from family-local date + local start time, so DST offset changes are applied by `ZoneInfo`; the implementation does not copy the first occurrence's fixed UTC offset forward.
- Explicit aware `target_occurrence` remains the first window and preserves its absolute instant; follow-on recurrence after that explicit seed uses the family timezone.
- Invalid or unavailable timezone returns `read_only_proposal` with reason `invalid_or_unavailable_timezone` and `successor_mutation = False`; mutation planning is not reached through an empty-window fallback.

PF5 deterministic G8 evidence:
- UTC invocation + `America/New_York` Monday `09:00` produces `2026-09-28T09:00:00-04:00`, not `09:00+00:00`.
- DST boundary evidence proves `2026-10-26T09:00:00-04:00` followed by `2026-11-02T09:00:00-05:00`.
- Explicit aware UTC seed for New York local 09:00 remains the first absolute occurrence, while N+1 is generated as family-local New York Monday 09:00 across DST.
- Invalid timezone uses a digest matching the invalid timezone scope and still fails closed/read-only.

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
- Clear Writing run id: `20261002T083100Z-9e4a47d173ce`.
- Issue body now anchors product candidate `0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d`, R3 progress, and next action.

PROJECT_STATUS = DOING
- `gh issue view 95 --json projectItems` reported Project `AI Skills Maintenance` status `DOING`.
- Labels remain `maintenance-track`, `kind:regression`, `scope:standalone-skill`, `area:standalone-skill`.
- Resolution commit remains intentionally empty before final Critic and integration/release closure.

INTEGRATED_TO_MAIN = NO
FORMAL_RELEASE_ADVANCED = NO
FINAL_CRITIC = PENDING

## Gate Evidence

All final gate evidence below is bound to product candidate `0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d`.

- `python -m py_compile skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py tests/test_slurm_workflows.py` -> PASS.
- PF5/G8 targeted: `python -m unittest tests.test_slurm_workflows.SlurmWorkflowsRoutingTests.test_g8_modes_capacity_reuse_successor_and_enrollment` -> PASS, 1 test, 0.127s.
- Full G1-G8: `python -m unittest tests.test_slurm_workflows` -> PASS, 13 tests, 2.654s.
- `python -m unittest tests.test_skill_update` -> PASS, 11 tests, 3.399s.
- `python scripts/skills.py validate` -> PASS, 154 active skills, 18 profiles.
- `python scripts/skills.py audit --all` -> PASS, exit 0; output contained profile/domain budget advice only.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS, `plugins=10`, `active_skills=29`, `source_snapshots=72`, `over_budget=0`.
- `python -m unittest discover -s tests` -> PASS, 320 tests, 127.424s.

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
0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d
```

Read:

- `results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R3_2026-10-02.md`
- `results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R3_2026-10-02.md`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`
- changed source and tests in candidate `0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d`
- tracking artifacts under `results/hpc--slurm-workflows-routing-refactor/tracking/`
- Issue #95 and `docs/skill-todos/slurm-workflows.md` as needed

Independently verify whether the bounded R3 prefinal repair contract is satisfied:

- SWR-PF5: family `timezone` is parsed with standard-library `zoneinfo.ZoneInfo`; recurrence `weekday` / `start_time` are interpreted in family-local wall-clock time; invocation `now` is converted into family timezone before current/next useful occurrence decisions; weekly follow-on occurrences do not carry a fixed UTC offset across DST; explicit aware target occurrences remain first and preserve their absolute instant; follow-on recurrence after explicit seed uses family timezone; invalid/unavailable timezone fails closed/read-only without successor mutation.
- PF5 G8 coverage includes UTC invocation + America/New_York 09:00, DST offset change, explicit aware N + N+1 across timezone semantics, and invalid timezone with matching digest.
- SWR-PF1/PF2/PF3/PF4 remain closed with regression coverage.
- Latest compatible `origin/main` was merged into the existing reviewed branch without rebase/force-push and without relevant Slurm semantic conflict.
- PF5/G8 targeted test, complete G1-G8, generated parity, and full suite are credible and bound to product candidate `0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d`.
- Versions remain repository `5.4.1`, standalone `slurm-workflows 0.3`, central Plugins `NO_BUMP`, Bridge Kit `NO CHANGE`.
- Issue #95 remains the single top-level maintenance tracking issue, remains `DOING`, keeps classification/Area/source backlink/empty Resolution commit, and its body has been updated through Clear Writing to the current candidate and next action.
- `REAL_SLURM_MUTATION = NO`; no main integration, release advancement, or self-approval occurred.

Return `PASS` only if the product candidate can proceed to integration/release closure. Otherwise return `REVISE` with concrete file/line findings.
