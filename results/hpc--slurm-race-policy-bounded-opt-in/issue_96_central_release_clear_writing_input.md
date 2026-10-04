Issue #96 central release update draft:

Central release is complete for `hpc--slurm-race-policy-bounded-opt-in`.

Released central versions:

- Repository: `5.4.4`
- `slurm-workflows`: `0.4`
- Central Plugins: `NO_BUMP`
- Bridge Kit: `NO_CHANGE`

Release evidence:

- Product candidate: `5a3dc447da2ea429ba2d229b0301c378be9e8018`
- Final Critic PASS: `06d135d8a6ee62cd41abb40fc5771fcef7f8db25`
- GitHub CI: PASS, run `37187784359`, head SHA `5a3dc447da2ea429ba2d229b0301c378be9e8018`
- Main integration commit: `f2fbf49ac2203a377106891fd36ddfc901b98ed3`
- Formal release commit: `06d135d8a6ee62cd41abb40fc5771fcef7f8db25`

Release isolation:

- The formal `5.4.4` release uses the Final Critic PASS reviewed line.
- It does not include the unrelated Presentations production development that is present on current `main`.
- `origin/release` is an ancestor of `origin/main`.

What is now shipped centrally:

- Duplicate race remains off by default.
- Explicit user/local opt-in is required.
- Explicit site prohibition blocks race.
- Final race authorization requires the complete bounded gate: two distinct routes, full workload/scientific contract identity, hard resource compatibility, and a safe frozen cancellation policy.

Tracking state:

- Keep Issue #96 open.
- Move Project Status to `ADAPTING`.
- Keep Resolution commit empty.
- Next action: DII consumer adaptation only.
- `REAL_SLURM_MUTATION = NO`.

Do not run real Slurm mutation during the remaining DII adaptation. DII should install/load the formal `slurm-workflows 0.4` release and run read-only/synthetic verification.
