Issue #96 progress update draft:

Implementation is complete on reviewed branch `reviewed/hpc--slurm-race-policy-bounded-opt-in`.

Current reviewed product candidate:
`cf9bfe16d526811525395d66e05035736e6ecc23`

What changed:
- `slurm-workflows` is bumped to `0.4`.
- Repository target is `5.4.4` from formal release baseline `5.4.3`.
- Duplicate race remains off by default.
- Explicit user/local opt-in is required.
- Explicit site prohibition blocks race even when the user opts in.
- Missing, `UNKNOWN`, `disabled_by_default`, and `explicit_user_opt_in` site policy can proceed only with opt-in, no known prohibition, exactly two candidates, matching workload/scientific contract, hard resource compatibility, and frozen winner/loser cancellation.

Validation:
- Race policy truth table: PASS.
- Bounded two-route contract: PASS.
- Hard resource requirement regression: PASS.
- Loser cancellation contract regression: PASS.
- Normal-entry smoke: PASS.
- Full local suite: PASS (`python -m unittest discover -s tests`, 330 tests).
- GitHub CI: PASS, run `37185949083`, head_sha `cf9bfe16d526811525395d66e05035736e6ecc23`.

Project / issue state:
- Keep Issue #96 open.
- Keep Project Status `DOING`.
- Keep Resolution commit empty.
- Next action: independent Final Critic review.
- `REAL_SLURM_MUTATION = NO`.
