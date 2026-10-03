# slurm-workflows — Long-Term TODO

Maintenance inbox for the standalone `slurm-workflows` skill.

This skill is not one of the central Marketplace plugins, so its real-use failures should not be forced into an unrelated plugin TODO. This file stays under `docs/` so maintenance history is not shipped as ordinary skill runtime payload. For new real-project feedback, follow the same evidence-first `status: NEW` discipline described in `docs/plugin-todos/README.md`: record the failure and current evidence first; do not pre-decide the implementation architecture or release.

## Open candidates

No open candidates.

## Recently promoted

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
