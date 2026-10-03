# Slurm Workflows — Parallel Release / Integration Recovery Critic Review

Date: 2026-10-02  
Role: AI Research Stack Independent Critic  
Review stage: PARALLEL_RELEASE_INTEGRATION_RECOVERY

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `reviewed/hpc--slurm-workflows-routing-refactor`
- recovery plan: `results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_PLAN_2026-10-02.md`
- recovery plan commit: `1da7ac5e334531a15a0d8863c99593c172007b86`
- Slurm semantic candidate: `d9da1dde5731f27f029dc1507a457a39b510d610`
- pre-recovery Slurm handoff: `97f53a14abe24e2fc1813b8003a9162d815c2c94`
- current main/release reviewed: `4ce1946ba047ea200c4ab41ae824de999ef535ed`
- current formal repository version: `5.4.1`
- current workflow-core: `0.5`
- Slurm target: `0.3`

## Result

```text
RESULT = REVISE
READY_FOR_RECOVERY_EXECUTION = NO

PRI-B1 = OPEN
```

The recovery direction is otherwise correct. The only blocking omission is the formal-release GitHub CI gate on the exact combined candidate.

## Accepted recovery judgments

### 1. Repository version recomputation

PASS.

Current formal `main == release == 4ce1946...` and `VERSION == 5.4.1`. The Slurm work is a compatible repair of the already-shipped standalone capability, so the current concrete repository target is:

```text
5.4.1 -> 5.4.2
slurm-workflows 0.2 -> 0.3
workflow-core remains 0.5
```

This concrete number is late-bound. If another formal release advances before the combined candidate freeze, recompute again from the then-current formal release baseline instead of mechanically keeping `5.4.2`.

### 2. Conflict ownership

PASS.

The current main-side changes since the common base are workflow-core production/release work and shared repository release metadata. No current-main Slurm production/source/test semantic change was found.

The recovery ownership split is correct:

- preserve Slurm task-owned source/test semantics from `d9da1dde...`;
- preserve workflow-core `0.5` and all other current-main production/release truth;
- recompute shared repository release surfaces from the combined truth;
- regenerate registry/catalog/generated outputs rather than choosing one side wholesale;
- use current main for the unrelated `tests/test_candidate_plugin_replay.py` timing behavior.

Two additional consistency tests are mixed/late-bound surfaces and must follow the same combined-truth rule during execution:

- `tests/test_standalone_skill_baselines.py` must end with repository `5.4.2`, `slurm-workflows 0.3`, and `workflow-core 0.5`;
- `tests/test_central_plugin_icon_assets.py` currently asserts repository `5.4.1` and must move with the combined repository version.

This is not a separate blocker because the plan already requires version consistency plus the full suite; it is an explicit execution interpretation of that requirement.

### 3. Combining workflow-core 0.5 with Slurm 0.3

PASS.

The product source ownership is independent. Current main changed workflow-core source/generated payload and related workflow-core tests; Slurm reviewed work changed the standalone Slurm source, shared environment path, and Slurm tests. There is no evidence that preserving one requires reverting the other.

The combined release dashboard and generated metadata must therefore represent both simultaneously.

### 4. Abort the conflicted merge first

PASS, with a fail-closed precondition.

The plan is correct not to continue hand-editing the already-conflicted worktree. Before `git merge --abort`, Executor must verify that:

- `MERGE_HEAD` corresponds to the unfinished latest-main merge;
- all R4 semantic work is already committed/published in the reviewed lineage;
- no pre-merge or post-conflict local task-owned change exists that would be lost by abort.

If that proof fails, stop rather than abort/reset/restore.

After abort, fetch and fast-forward to the current `origin/reviewed/hpc--slurm-workflows-routing-refactor`. The plan's textual expected tip `97f53a14...` is already historical because the recovery plan itself advanced the remote reviewed branch to `1da7ac5e...`; the plan already contains the correct rule to use the newly observed remote tip instead of resetting to an old SHA.

### 5. Full combined-candidate gates

PASS in principle, but see PRI-B1 below.

All Slurm semantic gates must be rerun after main integration because the release object is no longer `d9da1dde...`. The new exact combined candidate must carry:

- PF5/G8;
- complete G1-G8;
- `tests.test_skill_update`;
- repository validate/audit;
- generated parity;
- full unittest suite;
- version/README/changelog consistency;
- relevant install/normal-entry smoke.

Old Slurm candidate evidence is provenance only and cannot be reused as final release evidence.

### 6. Parallel development / serialized release / late-bound version

PASS as the correct long-term direction.

The minimal sustainable model is:

```text
independent reviewed branches
-> parallel implementation/review
-> relevant semantic drift checks
-> short serialized integration against latest formal/main truth
-> late-bind concrete repository version
-> rebuild shared generated/release surfaces
-> exact combined-candidate gates
-> final release closure
```

This avoids unnecessary repeated main merges during isolated implementation while still respecting the fact that `main` and `release` are one linear repository history.

A later AI_Skills_Collection governance amendment may encode this rule in repository-owned workflow/version guidance. Do not mix that governance implementation into the current Slurm recovery.

Bridge Kit does not own repository release numbering or AI_Skills shared metadata composition, so `Bridge Kit = NO CHANGE` is correct.

---

## PRI-B1 — Formal-release GitHub CI is missing from the recovery gate

### Requirement

The current AI Skills Maintainer release contract states that a formal release requires, in addition to local/full validation:

- relevant install/upgrade smoke;
- version/changelog/README consistency;
- generated-layer parity;
- **required GitHub CI**.

Current `.github/workflows/codex-marketplace.yml` does not run on ordinary reviewed-branch pushes; it runs on pull requests or `workflow_dispatch`.

### Direct evidence in the recovery plan

The recovery plan's final combined-candidate validation list contains local tests, generated parity, consistency checks and normal-entry smoke, but no required GitHub CI step.

The plan also forbids release advancement until final Critic PASS. Without an explicit CI step, the next final Critic could otherwise be handed a candidate that satisfies every listed local gate but still lacks the repository's formal-release CI requirement, including the Windows sparse-checkout lane.

### Causal risk

A formal `5.4.2` release could be approved from local evidence alone even though repository policy requires CI and the CI workflow exercises an environment not covered by the local Linux/server full suite.

### Minimum closure

Amend the recovery plan to require GitHub CI on the exact combined candidate before final release authorization.

A valid bounded sequence is:

1. construct and locally validate the combined candidate;
2. commit/publish that exact candidate as the reviewed branch tip;
3. run the repository's required GitHub CI for that reviewed ref using the existing approved CI path (for example the existing `workflow_dispatch` path; do not create a PR solely for this);
4. require all required CI jobs PASS and record their exact candidate/ref identity;
5. only then hand the same candidate to final Critic for release/integration closure.

If the candidate changes after CI, CI is stale and must be rerun.

No new workflow, Action, branch, queue, lock service, daemon, registry, or state machine is needed.

Owner: Planner / release-recovery execution contract.

---

## Non-blocking execution notes

1. When recomputing `5.4.2`, derive the concrete version from the then-current formal release baseline. If `main` and `release` no longer agree at preflight, stop and classify the in-progress release state rather than guessing.
2. Treat `VERSION`, root CHANGELOG, README dashboard, generated registry/catalog, and their deterministic consistency/baseline tests as one late-bound integration layer.
3. Preserve the workflow-core `5.4.1` changelog section exactly as historical release truth; add a distinct `5.4.2` Slurm section.
4. Final release ref movement remains fast-forward-only and is outside this Critic approval.

## Final fields

```text
RESULT = REVISE
PASS_OBJECT = PARALLEL_RELEASE_INTEGRATION_RECOVERY_PLAN_2026-10-02
PASS_OBJECT_COMMIT = 1da7ac5e334531a15a0d8863c99593c172007b86

VERSION_RECOMPUTE_5_4_2 = PASS_CURRENT_BASELINE
CONFLICT_OWNERSHIP = PASS
WORKFLOW_CORE_0_5_PRESERVATION = PASS
ABORT_AND_CLEAN_RECOVERY = PASS_WITH_FAIL_CLOSED_PREFLIGHT
COMBINED_FULL_GATES = PASS_WITH_PRI_B1
PARALLEL_MAINTENANCE_DIRECTION = PASS
BRIDGE_CHANGE_REQUIRED = NO

PRI-B1 = OPEN
READY_FOR_RECOVERY_EXECUTION = NO
REAL_SLURM_MUTATION_REQUIRED = NO
INTEGRATION_AUTHORIZED = NO
RELEASE_ADVANCEMENT_AUTHORIZED = NO
```
