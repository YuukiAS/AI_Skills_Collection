# Reviewed Handoff Request — hpc--slurm-race-policy-bounded-opt-in

## Objective

Bounded Slurm Workflows race policy opt-in repair: repo 5.4.4, slurm-workflows 0.4, no real Slurm mutation, stop at READY_FOR_FINAL_CRITIC.

## User-provided inputs

- Repository: `YuukiAS/AI_Skills_Collection`
- Task key: `hpc--slurm-race-policy-bounded-opt-in`
- Reviewed branch: `reviewed/hpc--slurm-race-policy-bounded-opt-in`
- Worktree: `/tmp/ai-skills-hpc-slurm-race-policy-bounded-opt-in`
- Formal release baseline at execution: repository `5.4.3`, standalone `slurm-workflows 0.3`
- Target: repository `5.4.4`, standalone `slurm-workflows 0.4`

## User constraints

- Implement only the frozen bounded race-policy repair.
- Do not create successor tasks, alternate branches, alternate worktrees, daemons, watchers, registries, databases, or state machines.
- Do not modify Bridge Kit, central Marketplace plugin versions, or DII consumer repositories.
- Do not execute real `sbatch`, `salloc`, `scancel`, duplicate GPU race, or weekly GPU enrollment.
- Stop at `READY_FOR_FINAL_CRITIC`; do not integrate main, advance release, close Issue #96, or self-approve.
