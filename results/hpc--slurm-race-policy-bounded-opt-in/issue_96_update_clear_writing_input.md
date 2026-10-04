Issue #96 progress update draft:

Implementation is complete on reviewed branch `reviewed/hpc--slurm-race-policy-bounded-opt-in`.

Current reviewed product candidate:
`5a3dc447da2ea429ba2d229b0301c378be9e8018`

What changed:
- `slurm-workflows` is bumped to `0.4`.
- Repository target is `5.4.4` from formal release baseline `5.4.3`.
- Duplicate race remains off by default.
- Explicit user/local opt-in is required.
- Explicit site prohibition blocks race even when the user opts in.
- Missing, `UNKNOWN`, `disabled_by_default`, and `explicit_user_opt_in` site policy can proceed only with opt-in, no known prohibition, exactly two candidates, full matching workload/scientific contract, hard resource compatibility, distinct routes, and frozen winner/loser cancellation.
- The low-level `duplicate_race_decision()` helper is now eligibility-only; final race authorization must come from the complete bounded gate.
- The bounded gate now fails closed for unenumerated scientific-field mismatch, `workload_scope_digest` mismatch, memory/CPU/GPU/walltime hard-resource mismatch, repeated same-route candidates, and unsupported cancellation rules such as `keep_both`.
- Installed normal-entry smoke now loads the installed `slurm-workflows` helper and exercises the full bounded race gate.

Validation:
- Race policy truth table: PASS.
- Full scientific contract identity: PASS.
- Hard resource contract: PASS.
- Cancellation policy validation: PASS.
- Installed normal-entry race smoke: PASS.
- Full local suite: PASS (`python -m unittest discover -s tests`, 331 tests).
- GitHub CI: PASS, run `37187784359`, head_sha `5a3dc447da2ea429ba2d229b0301c378be9e8018`.

Project / issue state:
- Keep Issue #96 open.
- Keep Project Status `DOING`.
- Keep Resolution commit empty.
- Next action: independent Final Critic review.
- `REAL_SLURM_MUTATION = NO`.
