# Slurm Workflows Routing Refactor Prefinal Repair Result R2

RESULT = READY_FOR_FINAL_CRITIC
TASK = hpc--slurm-workflows-routing-refactor
BRANCH = reviewed/hpc--slurm-workflows-routing-refactor
WORKTREE = /tmp/ai-skills-hpc-slurm-workflows-routing-refactor
START_MAIN = 72f43c4e135ec8d0a88348a126ec10faeacb965f
FORMAL_RELEASE_BASELINE = a7028195f3e97d32d51c32ef8c87f658f92048e5
PRE_R2_REVIEWED_REMOTE = 3a64a8e8d8915ea60183e96972ec4720376e87ac
RECONCILED_MAIN_MERGE = fcdffa01
PREVIOUS_PRODUCT_CANDIDATE = ed48521941f82eeedcfc490c55fa175780db64c9
FINAL_CANDIDATE = 569f85dde6f676fb2c249f89062c3f81168cac9e

## Scope And Drift

- Existing worktree was recoverable at `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`.
- `origin/main` was fetched and had advanced to `72f43c4e135ec8d0a88348a126ec10faeacb965f`.
- Local reviewed branch was fast-forwarded to `origin/reviewed/hpc--slurm-workflows-routing-refactor` at `3a64a8e8d8915ea60183e96972ec4720376e87ac`.
- Diff from R2 handoff main `ee852eff9278fda18952f687dda12bd787f01f72` to latest `origin/main` showed no Slurm production source/test/version/generated semantic drift. The new main commits were Project Instructions Editor docs/TODO only.
- Latest compatible `origin/main` was merged into the existing reviewed branch with ordinary non-force merge commit `fcdffa01`.
- No rebase, force-push, main integration, release advancement, successor task, new branch, or new worktree occurred.

## R2 Blockers

SWR-PF1 = PASS
- The existing normalized enrollment scope now includes durable top-level `timezone` through `_scope_window_contract(family)`.
- `_scope_digest()`, `_valid_enrollment()`, and CLI `scope-digest` continue to share the same normalized object.
- Same durable recurrence/window/action scope with the same timezone remains valid when only occurrence date changes.
- Changing only top-level `timezone` invalidates the old digest and returns reconciliation to `read_only_proposal`.

SWR-PF2 = PASS
- Explicit `target_occurrence` is now treated as the first capacity window.
- If the family also has the existing weekly recurrence contract, later windows continue from that recurrence after the explicit first occurrence.
- Active capacity covering explicit N now continues to earliest uncovered N+1/N+k; an existing lifecycle successor for that uncovered occurrence is kept without duplication.
- Explicit one-off target without recurrence remains single-window and returns `reuse_active` when active allocation covers that window.

SWR-PF3 = CLOSED / REGRESSION PASS
- Installed persistent-capacity G6 normal-entry coverage remains intact.
- The installed helper path still persists/reloads capacity state and validates missing successor, existing successor, and unrelated CPU/batch read-only behavior.

SWR-PF4 = CLOSED / REGRESSION PASS
- Runtime/raw site identity remains separated from repo-targeted tracked identity.
- Repo-targeted generated reference/manifest still do not contain raw or normalized private `ClusterName`; explicit local alias behavior remains stable.

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
- Clear Writing run id: `20261002T080321Z-060417b9d5e3`.
- Issue body now anchors current product candidate `569f85dde6f676fb2c249f89062c3f81168cac9e`, R2 progress, and next action.

PROJECT_STATUS = DOING
- `gh issue view 95 --json projectItems` reported Project `AI Skills Maintenance` status `DOING`.
- Labels remain `maintenance-track`, `kind:regression`, `scope:standalone-skill`, `area:standalone-skill`.
- Resolution commit remains intentionally empty before final Critic and integration/release closure.

INTEGRATED_TO_MAIN = NO
FORMAL_RELEASE_ADVANCED = NO
FINAL_CRITIC = PENDING

## Gate Evidence

All final gate evidence below is bound to product candidate `569f85dde6f676fb2c249f89062c3f81168cac9e`.

- `python -m py_compile skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py tests/test_slurm_workflows.py` -> PASS.
- PF1/PF2/G8 targeted: `python -m unittest tests.test_slurm_workflows.SlurmWorkflowsRoutingTests.test_g8_modes_capacity_reuse_successor_and_enrollment` -> PASS, 1 test, 0.040s.
- Full G1-G8: `python -m unittest tests.test_slurm_workflows` -> PASS, 13 tests, 2.380s.
- `python -m unittest tests.test_skill_update` -> PASS, 11 tests, 7.367s.
- `python scripts/skills.py validate` -> PASS, 154 active skills, 18 profiles.
- `python scripts/skills.py audit --all` -> PASS, exit 0; output contained profile/domain budget advice only.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS, `plugins=10`, `active_skills=29`, `source_snapshots=72`, `over_budget=0`.
- `python -m unittest discover -s tests` -> PASS, 320 tests, 170.999s.

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
569f85dde6f676fb2c249f89062c3f81168cac9e
```

Read:

- `results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R2_2026-10-02.md`
- `results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R2_2026-10-02.md`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`
- changed source and tests in candidate `569f85dde6f676fb2c249f89062c3f81168cac9e`
- tracking artifacts under `results/hpc--slurm-workflows-routing-refactor/tracking/`
- Issue #95 and `docs/skill-todos/slurm-workflows.md` as needed

Independently verify whether the bounded R2 prefinal repair contract is satisfied:

- SWR-PF1: durable top-level `timezone` is included in the existing normalized enrollment digest scope; same timezone with occurrence date changes stays valid; changing only timezone invalidates the old digest and returns to read-only; `_valid_enrollment` and CLI `scope-digest` still use the same normalized object.
- SWR-PF2: explicit `target_occurrence` is the first window; recurring families continue to N+1/N+k after the explicit first occurrence; active covering explicit N plans one missing successor for N+1; existing lifecycle successor for N+1 is kept without duplication; explicit one-off target without recurrence remains single-window `reuse_active`.
- SWR-PF3/PF4 remain closed with regression coverage: installed persistent-capacity G6 normal-entry still passes, and repo-targeted tracked identity still does not leak raw or normalized private `ClusterName` while explicit aliases remain stable.
- Latest compatible `origin/main` was merged into the existing reviewed branch without rebase/force-push and without relevant Slurm semantic conflict.
- PF1/PF2/G8 targeted test, complete G1-G8, generated parity, and full suite are credible and bound to product candidate `569f85dde6f676fb2c249f89062c3f81168cac9e`.
- Versions remain repository `5.4.1`, standalone `slurm-workflows 0.3`, central Plugins `NO_BUMP`, Bridge Kit `NO CHANGE`.
- Issue #95 remains the single top-level maintenance tracking issue, remains `DOING`, keeps classification/Area/source backlink/empty Resolution commit, and its body has been updated through Clear Writing to the current candidate and next action.
- `REAL_SLURM_MUTATION = NO`; no main integration, release advancement, or self-approval occurred.

Return `PASS` only if the product candidate can proceed to integration/release closure. Otherwise return `REVISE` with concrete file/line findings.
