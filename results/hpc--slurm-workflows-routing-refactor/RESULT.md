# Slurm Workflows Routing Refactor Prefinal Repair Result

RESULT = READY_FOR_FINAL_CRITIC
TASK = hpc--slurm-workflows-routing-refactor
BRANCH = reviewed/hpc--slurm-workflows-routing-refactor
WORKTREE = /tmp/ai-skills-hpc-slurm-workflows-routing-refactor
START_MAIN = ee852eff56a755a8d4dfd226fb9607b733fdc1df
FORMAL_RELEASE_BASELINE = a7028195f3e97d32d51c32ef8c87f658f92048e5
PRE_REPAIR_REVIEWED_REMOTE = 133c2f7f68cd6209df9f8db616f12c69eeb9bd66
RECONCILED_MAIN_MERGE = 4ab88662
FINAL_CANDIDATE = ed48521941f82eeedcfc490c55fa175780db64c9

## Scope And Drift

- Existing worktree was recoverable at `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`.
- `origin/main` was fetched and had advanced to `ee852eff56a755a8d4dfd226fb9607b733fdc1df`.
- The new `origin/main` commits were Project Instructions Editor documentation/review commits and showed no Slurm production source/test/version semantic drift.
- Local reviewed branch was first fast-forwarded to `origin/reviewed/hpc--slurm-workflows-routing-refactor` at `133c2f7f68cd6209df9f8db616f12c69eeb9bd66`, then latest compatible `origin/main` was merged with ordinary non-force merge commit `4ab88662`.
- No rebase, force-push, main integration, release advancement, successor task, new branch, or new worktree occurred.

## Prefinal Blockers

SWR-PF1 = PASS
- Enrollment digest scope now binds durable calendar/window/action contract fields, including recurrence/window shape, target readiness, lead time, minimum/latest useful window fields, calendar-bound submission, max successor, submit-successor authority, and stale successor cancel/retarget authority.
- `_valid_enrollment` and CLI `scope-digest` both use the same `_scope_digest(family)` normalized contract.
- Same recurrence across occurrence dates remains valid; changing durable window/action fields invalidates an old digest.

SWR-PF2 = PASS
- `capacity_reconcile` now scans recurrence windows to the first uncovered target instead of returning immediately when the current window is covered by an active allocation.
- Covered cases include current occurrence already started but still useful, active allocation covering current N then planning N+1, active + lifecycle successor for N+1 without duplicate planning, active spanning multiple recurrences then planning the first uncovered later recurrence, fail-closed multiple compatible active allocations, fail-closed multiple lifecycle successors, and activation mismatch/read-only unrelated workload behavior.
- No daemon, watcher, new registry, new gate, or state machine was added.

SWR-PF3 = PASS
- Added installed normal-entry G6 coverage for persistent capacity state.
- The test materializes the installed `slurm-workflows` skill, loads the installed helper from the installed skill path, persists a capacity family with exact enrollment digest to a temp state path, reloads state, reuses a compatible active allocation while planning exactly one missing successor, keeps an existing lifecycle successor without duplication, and keeps unrelated CPU/batch input read-only.

SWR-PF4 = PASS
- Runtime/local identity and repo-targeted tracked identity are separated.
- Explicit local aliases remain stable; raw discovered `ClusterName` values are represented in repo-targeted generated reference/manifest fields as non-reversible `local-slurm-<sha256-prefix>` aliases.
- Regression checks assert the lower-cased generated reference and manifest do not contain `privateclustersecret`.

## Required Fields

STICKY_STATE_PERSISTENCE = PASS
- Candidate keeps the `~/.config/ai-skills/slurm-workflows.toml` state contract for accepted workload contracts, capacity families, enrollments, and optional evidence locators.
- `tests.test_slurm_workflows.test_g7_sticky_contract_and_right_sizing_hysteresis` proves save/load/reload reuse across independent loads.

CALENDAR_CAPACITY_COVERAGE = PASS
- Candidate computes recurring capacity windows from recurrence/target occurrence, successor lead time, minimum useful duration, latest useful end/cutoff, and target readiness.
- Running allocations and lifecycle successors are evaluated against the first uncovered useful target window.

ENROLLMENT_DIGEST_FAIL_CLOSED = PASS
- Mutation-capable enrollment requires exact valid `scope_digest`.
- Missing, stale, or mismatched digest remains read-only.

LEGACY_CONFIG_CLEANUP = PASS
- Fresh generated local override sections emit blank race defaults.
- Legacy fields remain readable for compatibility.

DOCTOR_SITE_AWARE = PASS
- `environment doctor` derives requiredness from public profile constraints and local/live facts instead of universal account/partition/qos/scratch/module assumptions.

G6_TRUE_NORMAL_ENTRY = PASS
- Fake Slurm on PATH exercises detect -> plan -> apply -> doctor -> installed helper -> live discovery -> local preference -> route.
- Installed persistent-capacity state coverage uses the installed helper, not the source helper.

PUBLIC_SAFE_GENERATED_REFERENCE = PASS
- Repo-targeted generated site references and manifests use public-safe tracked identities and safe local override locators.

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

PROJECT_STATUS = DOING
- Issue #95 remains `DOING` pending independent Critic and later integration/release closure.

INTEGRATED_TO_MAIN = NO
FORMAL_RELEASE_ADVANCED = NO
FINAL_CRITIC = PENDING

## Gate Evidence

All commands below were run after the repair on the worktree that was committed as `ed48521941f82eeedcfc490c55fa175780db64c9`.

- `python -m py_compile skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py scripts/skills.py tests/test_slurm_workflows.py` -> PASS.
- Affected G6/G8 targeted command -> PASS, 6 tests, 1.884s.
- `python -m unittest tests.test_slurm_workflows` -> PASS, 13 tests, 1.913s.
- `python -m unittest tests.test_skill_update` -> PASS, 11 tests, 0.787s.
- `python scripts/skills.py validate` -> PASS, 154 active skills, 18 profiles.
- `python scripts/skills.py audit --all` -> PASS, exit 0; output contained profile/domain budget advice only.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS, `plugins=10`, `active_skills=29`, `source_snapshots=72`, `over_budget=0`.
- `python -m unittest discover -s tests` -> PASS, 320 tests, 132.368s.

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
ed48521941f82eeedcfc490c55fa175780db64c9
```

Read:

- `results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R1_2026-10-02.md`
- `results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R1_2026-10-02.md`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`
- changed source and tests in candidate `ed48521941f82eeedcfc490c55fa175780db64c9`
- version metadata, generated registry/catalog parity, tracking evidence, and canonical standalone-skill TODO as needed

Independently verify whether the bounded prefinal repair contract is satisfied:

- SWR-PF1: exact enrollment `scope_digest` covers durable calendar/window/action scope; same recurrence across occurrence dates remains valid; changing durable window/action fields invalidates old digest; `_valid_enrollment` and CLI `scope-digest` share the same normalized object.
- SWR-PF2: capacity lifecycle scans to the first uncovered recurrence; current useful window, N+1 successor maintenance, active spanning multiple recurrences, multiple active/successor fail-closed behavior, activation mismatch, and unrelated read-only behavior are covered without daemon/watcher/state-machine expansion.
- SWR-PF3: G6 installed normal-entry coverage uses an installed skill helper and persisted/reloaded capacity state, then validates active reuse plus one missing successor, existing successor no duplicate, and unrelated CPU/batch read-only behavior.
- SWR-PF4: repo-targeted generated references/manifests do not leak raw discovered `ClusterName`, including lower-cased `privateclustersecret`, while explicit local aliases remain stable.
- Latest compatible `origin/main` was merged into the existing reviewed branch without rebase/force-push and without relevant Slurm semantic conflict.
- G6/G8 targeted tests, complete G1-G8, generated parity, and full suite are credible and bound to product candidate `ed48521941f82eeedcfc490c55fa175780db64c9`.
- Versions remain repository `5.4.1`, standalone `slurm-workflows 0.3`, central Plugins `NO_BUMP`, Bridge Kit `NO CHANGE`.
- Issue #95 remains the single top-level maintenance tracking issue and remains `DOING`.
- `REAL_SLURM_MUTATION = NO`; no main integration, release advancement, or self-approval occurred.

Return `PASS` only if the product candidate can proceed to integration/release closure. Otherwise return `REVISE` with concrete file/line findings.
