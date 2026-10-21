# Critic prompt — Slurm protected-cancel G4 resource amendment v3.1

You are the independent Critic for the existing task `hpc--slurm-cancel-production-closure`.

This is a narrow amendment review, not a redesign.

Read current AI_Skills_Collection main contracts required by the project, then read:

- parent approved execution package: `e84be726d6a7aaefe62d27c7fd2a0410e7f1498b`;
- current candidate evidence on `reviewed/hpc--slurm-cancel-production-closure`, especially `SESSION_AB_EVIDENCE.md`, `EXECUTION_EVIDENCE.md`, and candidate `a8765b97b69c319304cb51dbd271d57ed8492c34`;
- amendment:
  `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_G4_RESOURCE_AMENDMENT_V3_1_2026-10-20.md`.

Verified facts to preserve:

- stale Desktop session snapshot was the G4 harmless-probe root cause;
- fresh Desktop thread consumed the final Hook and blocked `scancel --help` before process start;
- Hook architecture remains valid;
- current candidate changed only the fresh-session/reload contract; enforcement bytes stayed identical;
- the one authorized CPU-only submission produced no JobId and failed with `QOSMinGRES`;
- read-only site evidence shows every allowed `htzhulab` QoS requires `gres/gpu=1`;
- no Slurm Job has yet been created or mutated.

Review only this semantic delta:

```text
CPU-only/no-GPU G4 test Job
->
one exact held + future-dated pending htzhulab Job requesting the site-required minimum gres/gpu=1,
never released and cancelled before it can execute
```

Return only PASS or REVISE.

PASS requires all of the following:

1. the change is the minimum necessary response to an impossible CPU-only fixture and does not reopen the product architecture;
2. one-GPU GRES is required only to make the Job schedulable in `htzhulab`, not to perform GPU computation;
3. `--hold` plus BeginTime >= 24h keeps the Job ineligible to run during the acceptance;
4. post-submit read-only verification requires PENDING, current owner, `htzhulab`, no allocated node, and hold/future eligibility protection before any cancellation interaction;
5. failure of that verification stops without creating a second Job;
6. the same exact Job is used for retain then confirm/cancel;
7. no explicit H100 request is used unless the site rejects generic `gres/gpu=1` and an exact type is strictly required;
8. G1-G3/G5, Hook architecture, fresh-session behavior, branch/worktree/task identity, DII/CARE, `slurm_routing.py`, version policy and release closure remain unchanged;
9. no new Gate, wrapper, daemon, database, Direct mode or Codex patch is introduced;
10. this PASS approves only the amended G4 test-resource contract; it does not itself execute a Job or authorize unrelated Slurm mutation.

If PASS, state:

```text
AMENDMENT_V3_1=PASS
G4_RESOURCE_FIX=APPROVED
READY_TO_REVISE_TASK_PLAN=YES
```

and provide a short Planner handoff telling the existing task-local Planner to:
- revise only the G4 resource fixture in `PLAN.md`;
- increment the one available `plan_revision`;
- restore `PLAN_FROZEN`;
- resume the same Codex task with candidate `a8765b97b69c319304cb51dbd271d57ed8492c34`;
- create at most the one amended pending Job;
- continue G4 -> independent implementation review -> G5 if it passes.

REVISE only for a concrete safety/execution flaw in this amendment. Do not reopen Hook/Code Mode/runtime architecture or require another general design round.
