# slurm-workflows — Long-Term TODO

Maintenance inbox for the standalone `slurm-workflows` skill.

This skill is not one of the central Marketplace plugins, so its real-use failures should not be forced into an unrelated plugin TODO. This file stays under `docs/` so maintenance history is not shipped as ordinary skill runtime payload. For new real-project feedback, follow the same evidence-first `status: NEW` discipline described in `docs/plugin-todos/README.md`: record the failure and current evidence first; do not pre-decide the implementation architecture or release.

## Open candidates

### Slurm routing and capacity maintenance closure regression
status: PROMOTE_NOW
tracking: #95
source: Reviewed Handoff task `hpc--slurm-workflows-routing-refactor`
evidence: `results/hpc--slurm-workflows-routing-refactor/CODEX_POST_INTEGRATION_REPAIR_PROMPT.md`; `results/hpc--slurm-workflows-routing-refactor/RESULT.md`; branch `reviewed/hpc--slurm-workflows-routing-refactor`; candidate repair lineage from `20c47de1c2569b32f2b3aff2181fbc55bd179d94`
target layer: routing / qa / distribution
problem:
- The already implemented Slurm Workflows repair must be restored on the existing reviewed branch after main/release advanced to repository `5.4.0` and standalone `slurm-workflows 0.2`.
- The final candidate must preserve sticky state persistence, calendar-aware capacity lifecycle semantics, exact enrollment `scope_digest` fail-closed behavior, cleanup of obsolete race defaults, site-aware doctor requiredness, true installed G6 normal-entry coverage, and public-safe generated artifacts.
- Prior result evidence was bound to old release assumptions (`5.3.0`, `slurm-workflows 0.2`, `NO_BUMP`) and cannot be reused as final evidence for the reconciled candidate.
project-specific context: This entry is scoped to the public standalone `slurm-workflows` skill and deterministic fake-Slurm/read-only evidence. It does not authorize real Slurm mutation, real weekly GPU enrollment, Bridge Kit changes, central plugin topology changes, main integration, or release advancement.
candidate action: Reconcile latest compatible `origin/main` into the existing reviewed branch without rebase or force-push; update repository/standalone version metadata to `5.4.1` / `0.3`; regenerate registry/catalog/generated parity; rerun G1-G8 and full tests on one exact candidate; update durable result evidence and hand off to independent final Critic.
promotion gate: One exact candidate on `reviewed/hpc--slurm-workflows-routing-refactor` passes G1-G8, `tests.test_slurm_workflows`, `tests.test_skill_update`, repository validation/audit, Marketplace generation check, and full `python -m unittest discover -s tests`, with no real Slurm mutation and with branch pushed for final Critic review.
