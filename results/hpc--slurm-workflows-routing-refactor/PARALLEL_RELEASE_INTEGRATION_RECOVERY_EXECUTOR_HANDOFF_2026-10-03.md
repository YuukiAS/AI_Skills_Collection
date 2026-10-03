# Slurm Workflows — Recovery Executor Handoff

Date: 2026-10-03  
Task: `hpc--slurm-workflows-routing-refactor`  
Repository: `YuukiAS/AI_Skills_Collection`  
Branch: `reviewed/hpc--slurm-workflows-routing-refactor`  
Existing worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Authority:

- Recovery Plan v2:
  `results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_PLAN_V2_2026-10-03.md`
  @ `86318691fee8411c77d6eedce91eea397c08a35d`
- Critic R2 PASS:
  `results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_CRITIC_REVIEW_R2_2026-10-03.md`
  @ `b211eddc732ff62e0d13a17d7455b849ee0743bd`

Current observed repository state at handoff creation:

- `main = c4018d25c98c85611321c59246ace2979c6c1cf4`
- `release = 4ce1946ba047ea200c4ab41ae824de999ef535ed`
- main/release `VERSION = 5.4.1`
- current formal release baseline = `5.4.1`
- current concrete next patch, if unchanged at execution preflight = `5.4.2`
- Slurm standalone target = `0.3`
- workflow-core must remain `0.5`
- Issue #95 remains `DOING`
- real Slurm mutation remains forbidden

## Execute now

Do not create a successor, new branch, or new worktree.

1. Enter the existing worktree and inspect the current conflict state.
2. Before aborting anything, prove:
   - `MERGE_HEAD` belongs to the unfinished latest-main merge;
   - all R4 Slurm semantic work is already committed/published in the reviewed lineage;
   - there is no uncommitted task-owned work that would be lost.
3. If and only if those checks pass, `git merge --abort`.
4. Fetch current `origin/main`, `origin/release`, and the reviewed branch. Fast-forward the local reviewed worktree to the current remote reviewed tip.
5. Re-read formal release baseline and `VERSION`.
   - If formal release advanced, late-bind the next PATCH from that new release.
   - If main/release version truth is ambiguous or another release closure is mid-flight, stop and report the exact blocker.
6. Check current main for Slurm/shared-runtime substantive drift.
   - Unrelated docs/TODO/plugin work is not a blocker.
   - New Slurm/shared-runtime semantic drift is a Planner stop.
7. Construct the combined candidate using ordinary non-force integration:
   - preserve current-main production truth including `workflow-core 0.5`;
   - preserve task-owned Slurm source/test semantics from the accepted R4 candidate lineage;
   - use current-main truth for unrelated shared tests such as `tests/test_candidate_plugin_replay.py`;
   - recompute shared release surfaces from combined truth;
   - regenerate generated outputs using canonical generators, never ours/theirs hand-edit generated JSON.
8. If the formal baseline is still 5.4.1, the combined release target is:
   - Repository `5.4.2`
   - `slurm-workflows 0.3`
   - `workflow-core 0.5`
   - other central Plugins `NO_BUMP`
   - Bridge Kit `NO CHANGE`
9. Preserve the historical `5.4.1` workflow-core changelog entry and add a distinct Slurm patch entry for the new repository release.
10. Update all version-dependent consistency tests/surfaces, including:
    - `tests/test_standalone_skill_baselines.py`
    - `tests/test_central_plugin_icon_assets.py`
    - README dashboard
    - VERSION
    - registry/catalog/generated outputs
    - root CHANGELOG

## Local gates

Before freezing the combined candidate, run all of:

- PF5/G8 targeted test;
- full `tests.test_slurm_workflows`;
- `python -m unittest tests.test_skill_update`;
- `python scripts/skills.py validate`;
- `python scripts/skills.py audit --all`;
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report`;
- `python -m unittest discover -s tests`;
- version/README/changelog/registry/catalog/generated consistency;
- relevant install/normal-entry smoke.

All must PASS on the same combined working tree.

## Freeze and GitHub CI

After local gates PASS:

1. Commit one exact combined candidate `C`.
2. Ordinary non-force publish the reviewed branch and verify remote tip == `C`.
3. Dispatch existing `.github/workflows/codex-marketplace.yml` using `workflow_dispatch` against this reviewed branch/ref.
4. Verify the workflow run `head_sha == C`.
5. Require successful conclusions for:
   - `codex-marketplace`
   - `windows-sparse-checkout`
   - `editable-install-smoke` / Ubuntu
   - `editable-install-smoke` / Windows
6. Record run id/URL, ref, head_sha, and required job conclusions in task evidence.
7. If any release-critical commit is added after that CI run, mark the old CI stale and rerun CI on the new exact candidate.

If the current environment cannot dispatch `workflow_dispatch` through its available GitHub authority, do not create a PR or new workflow as a workaround. Preserve the exact published candidate and report only that bounded CI-dispatch blocker.

## Tracking and stop point

After exact candidate + exact-SHA CI PASS:

- use the existing Clear Writing path before updating Issue #95;
- update Issue #95 to the exact candidate/current progress/next action;
- keep Issue #95 `DOING`;
- do not fill Resolution commit;
- do not integrate main;
- do not advance release;
- do not execute real `sbatch` / `salloc` / `scancel`;
- stop at `READY_FOR_FINAL_CRITIC`;
- provide one complete independent Final Critic prompt.

This execution is already approved by the recovery Critic. Do not ask for another Planner/Critic decision unless one of the explicit fail-closed conditions above occurs.
