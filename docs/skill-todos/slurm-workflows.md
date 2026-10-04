# slurm-workflows — Long-Term TODO

Maintenance inbox for the standalone `slurm-workflows` skill.

This skill is not one of the central Marketplace plugins, so its real-use failures should not be forced into an unrelated plugin TODO. This file stays under `docs/` so maintenance history is not shipped as ordinary skill runtime payload. For new real-project feedback, follow the same evidence-first `status: NEW` discipline described in `docs/plugin-todos/README.md`: record the failure and current evidence first; do not pre-decide the implementation architecture or release.

## Open candidates

## Recently promoted

### Bounded duplicate-race opt-in when no site prohibition is known
status: PROMOTED
tracking: #96
source: Reviewed Handoff task `hpc--slurm-race-policy-bounded-opt-in`
evidence: `results/hpc--slurm-race-policy-bounded-opt-in/RESULT.md`; Final Critic PASS in `results/hpc--slurm-race-policy-bounded-opt-in/FINAL_CRITIC_REVIEW_R3_2026-10-04.md`; GitHub CI run `37187784359`; product candidate `5a3dc447da2ea429ba2d229b0301c378be9e8018`; central release closure evidence in `results/hpc--slurm-race-policy-bounded-opt-in/CENTRAL_RELEASE_CLOSURE_2026-10-04.md`
target layer: routing / policy / qa
problem:
- `slurm-workflows 0.3` required a site profile to explicitly allow duplicate race before a user/local opt-in could matter.
- That was too strict for missing, `UNKNOWN`, `disabled_by_default`, and `explicit_user_opt_in` policy states when no site prohibition is known and the user has explicitly opted in.
project-specific context: This entry is scoped to public standalone Slurm Workflows behavior and deterministic fake-Slurm/read-only evidence. It does not authorize real `sbatch`, `salloc`, `scancel`, duplicate GPU race execution, weekly GPU enrollment, DII installation/adaptation, Bridge Kit changes, or central plugin topology changes.
current behavior: Repository `5.4.4` formally ships standalone `slurm-workflows 0.4`. Duplicate race remains off by default; final race authorization requires explicit user/local opt-in, no explicit site prohibition, exactly two distinct candidate routes, full workload/scientific contract identity, hard resource compatibility, and a frozen safe winner/loser cancellation policy. Central Plugins remain `NO_BUMP`; Bridge Kit remains `NO CHANGE`; `REAL_SLURM_MUTATION = NO`.
promotion gate: CLOSED by product candidate `5a3dc447da2ea429ba2d229b0301c378be9e8018`, GitHub CI run `37187784359`, Final Critic PASS, and formal release commit `06d135d8a6ee62cd41abb40fc5771fcef7f8db25`. Issue #96 remains open for DII consumer adaptation.

### Slurm routing and capacity maintenance closure regression
status: PROMOTED
tracking: #95
source: Reviewed Handoff task `hpc--slurm-workflows-routing-refactor`
evidence: `results/hpc--slurm-workflows-routing-refactor/RESULT.md`; Final Critic PASS in `results/hpc--slurm-workflows-routing-refactor/FINAL_CRITIC_REVIEW_2026-10-03.md`; GitHub CI run `37131439668`; product candidate `9042c6eb210a519a03fcfa127d4d59cd8197ed78`; final integration/release closure evidence in `results/hpc--slurm-workflows-routing-refactor/INTEGRATION_RELEASE_CLOSURE_2026-10-03.md`
target layer: routing / qa / distribution
problem:
- The Slurm Workflows repair had to be restored and carried through final integration after main/release advanced beyond the original candidate assumptions.
- The final release preserves sticky state persistence, calendar-aware capacity lifecycle semantics, exact enrollment `scope_digest` fail-closed behavior, cleanup of obsolete race defaults, site-aware doctor requiredness, true installed G6 normal-entry coverage, and public-safe generated artifacts.
project-specific context: This entry is scoped to the public standalone `slurm-workflows` skill and deterministic fake-Slurm/read-only evidence. It does not authorize real Slurm mutation, real weekly GPU enrollment, Bridge Kit changes, central plugin topology changes, main integration, or release advancement.
current behavior: Repository `5.4.2` formally ships standalone `slurm-workflows 0.3`; `workflow-core` remains `0.5`; central Plugins remain `NO_BUMP`; Bridge Kit remains `NO CHANGE`. The reviewed product candidate passed PF5/G8, complete G1-G8, full local validation, generated parity, exact-SHA GitHub CI, and independent Final Critic review. `REAL_SLURM_MUTATION = NO`.
promotion gate: CLOSED by product candidate `9042c6eb210a519a03fcfa127d4d59cd8197ed78`, GitHub CI run `37131439668`, Final Critic PASS, and final integration/release closure.
