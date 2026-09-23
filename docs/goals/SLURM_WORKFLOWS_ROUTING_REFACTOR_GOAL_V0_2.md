# Slurm Workflows Routing Refactor — Canonical Goal v0.2

Target repository: `YuukiAS/AI_Skills_Collection`  
Task key: `hpc--slurm-workflows-routing-refactor`  
Approved architecture: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_2_2026-09-24.md`  
Executable Plan: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_2_2026-09-24.md`

Exact execution branch after approved Kickoff:

`reviewed/hpc--slurm-workflows-routing-refactor`

Exact task-owned worktree:

`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

This Goal is not execution authorization until the exact v0.2 execution package receives independent execution-ready Critic PASS and the user then sends the approved Kickoff.

## Goal

Ship a verified `slurm-workflows 0.2` whose normal installed entry safely routes jobs on managed Slurm clusters without leaking Longleaf-specific partition constants into generic source.

The release must implement the approved contract:

```text
generic Slurm Skill
+ site hard authority
+ local preference
+ generated site reference
```

and:

```text
prefer
-> advisory probe
-> native single-job widening
-> guarded duplicate fallback only when explicitly site-authorized
```

## Required outcomes

1. Generic source/template contains no Longleaf-specific partition names or universal race-delay constants.
2. Installed generated site reference exposes the site hard constraints/policy that the Skill must obey.
3. Local preference supports ordered partition preference without becoming site authority.
4. `--test-only` is advisory and fails closed when its output cannot be safely interpreted.
5. Single-job multi-partition widening is treated as native widening, not as a latency guarantee.
6. Automatic in-place Partition widening is used only for target site/job classes with real probe evidence.
7. cancel+resubmit is limited to replaceable pending jobs and uses state-safe cancellation plus old-job-inactive confirmation.
8. Identity-sensitive array/dependency/external-JobId workflows never receive unsafe automatic JobId replacement.
9. Duplicate submissions require both explicit site allow and user/local opt-in.
10. Current Longleaf/CUHK `disabled_by_default` cannot be widened by local opt-in.
11. Doctor requiredness comes from site hard constraints, not global guessed required fields.
12. G1-G6 are satisfied on one final candidate; G4 may remain disabled/NOT_APPLICABLE if duplicate fallback is not implemented.
13. No daemon, watcher, database, dependency remapper, scheduler predictor, or new control plane is added.
14. Future capabilities remain out of scope: resource-feasibility, pending-reason-aware, restartability/preemption-aware, deadline-aware routing.
15. Release closure:
    - `slurm-workflows 0.1 -> 0.2`;
    - repository next PATCH from actual release-time `VERSION`;
    - all central Plugins `NO_BUMP`.

## Allowed execution effects after the user sends approved Kickoff

- create/use exact reviewed branch and exact task-owned worktree;
- modify only the Plan-approved source/tests/release files;
- run deterministic local/repo tests and existing CI/validation;
- ordinary commit and non-force push to the exact reviewed branch;
- if and only if needed for Longleaf in-place widening evidence, execute the one bounded held/no-op probe defined in the Plan;
- after required Critic/final gates pass, perform ordinary non-force integration of the exact reviewed candidate to main and verify remote parity.

## Real Slurm probe authorization boundary

Sending the approved Kickoff authorizes at most one new held/no-op Longleaf test job solely for validating in-place Partition update behavior.

It does not authorize touching any pre-existing user job, running research computation, releasing the probe to run, performing duplicate-job race, or repeating the probe after a failed/ambiguous attempt.

The probe must be cleaned up before normal completion; cleanup failure is a blocker and must be reported with the probe JobId.

## Completion

The Goal is complete only when:

- implementation matches approved Proposal/Plan;
- required deterministic and normal-installed-entry evidence passes;
- any authorized real site probe is cleaned up and truthfully reported;
- independent pre-final Critic review has no open blocker;
- version/release closure is complete;
- reviewed final candidate is integrated to main without unreviewed semantic drift;
- remote main/version/README/generated parity is verified.

A local branch, passing unit tests, or a submitted job is not completion.
