Title:
Slurm Workflows race policy should allow bounded opt-in when there is no known site prohibition

Body:
Slurm Workflows 0.3 is too strict for duplicate race routing. It only allows race when the site policy explicitly says race is allowed. That blocks safe local opt-in cases where the site policy is missing, UNKNOWN, disabled_by_default, or explicit_user_opt_in, even when there is no known prohibition.

This tracking item covers one bounded standalone-skill repair:

- kind: regression
- scope: standalone-skill
- area: standalone-skill
- task key: hpc--slurm-race-policy-bounded-opt-in
- target repository release: 5.4.4
- target standalone skill: slurm-workflows 0.4
- Project Status: DOING
- Resolution commit: empty until formal release closure

The desired behavior is:

- duplicate race stays off by default;
- explicit user or local opt-in is always required;
- explicit site prohibition always blocks race;
- site policy values missing, UNKNOWN, disabled_by_default, and explicit_user_opt_in may proceed only with opt-in and no known prohibition;
- race is limited to exactly two candidate routes;
- both routes must preserve the same workload and scientific contract;
- both routes must satisfy hard resource requirements;
- winner and loser cancellation behavior must be frozen before submission;
- if the scheduler rejects duplicate submission, fail closed and do not bypass the policy with another command form.

Current action:
Implement the bounded policy in Slurm Workflows, add deterministic regression tests, bump slurm-workflows to 0.4, and stop at reviewed-branch final critic readiness. No real sbatch, salloc, scancel, duplicate GPU race, or weekly GPU enrollment is authorized.
