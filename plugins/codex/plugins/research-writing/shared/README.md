# Research Writing Shared Contracts

For every non-trivial student-facing Homework, Project, milestone, policy, template or oral-brief task, read these files in full and in this order:

1. `student-assessment-end-to-end-pre-execution-runbook.md`
2. `student-assessment-cumulative-acceptance-contract.md`
3. `student-assessment-hw1-nonrecurrence-amendment-v1.md`

The third file is a binding amendment derived from the first full STAT5060 HW1 replay. It adds positive-baseline, authority-coherence, relational-invariant, feasibility, validator-calibration, task-proportionality and incident-escalation requirements.

No task-local prompt may weaken these contracts. Course-specific authority may add stricter requirements.

A task must not begin production until it can report:

```text
RUNBOOK_READ = YES
CUMULATIVE_ACCEPTANCE_CONTRACT_READ = YES
NONRECURRENCE_AMENDMENT_READ = YES
```

If any file conflicts with a later explicitly versioned shared contract, stop and resolve the shared-contract version rather than choosing locally.
