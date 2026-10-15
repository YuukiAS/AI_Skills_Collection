# AI Skills Maintainer preflight

Perform a read-only maintenance preflight for the attached frozen Reviewed Handoff Plan.

Report only:

- the canonical source files and generated surfaces affected by the Plan;
- the minimum regression and parity gates required before Reviewer handoff;
- the frozen repository and standalone-skill version decisions;
- any scope or ownership conflict that would require Planner re-entry.

Do not edit any repository file. Do not implement the Plan. Do not run Slurm commands,
resource allocation, cancellation, remote deployment, paid review, or consumer writes.
