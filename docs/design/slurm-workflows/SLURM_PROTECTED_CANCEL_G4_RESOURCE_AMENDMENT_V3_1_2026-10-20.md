# Slurm protected cancel G4 resource amendment v3.1

Date: 2026-10-20  
Task: `hpc--slurm-cancel-production-closure`  
Parent package: `e84be726d6a7aaefe62d27c7fd2a0410e7f1498b`  
Current implementation candidate: `a8765b97b69c319304cb51dbd271d57ed8492c34`

## Why this amendment exists

The protected-cancel architecture is no longer the blocker.

A same-backend A/B run proved that an old Desktop thread retained a stale `sess.hooks()` snapshot while a fresh thread consumed the final Hook declaration. The fresh thread then blocked the harmless normal-entry `scancel --help` probe before the real process started. Candidate `a8765b97b69c319304cb51dbd271d57ed8492c34` adds only the required fresh-session/reload instruction; Hook, supervisor and private runtime enforcement bytes remain unchanged. Thirty-nine focused/existing Slurm regressions passed.

The remaining G4 blocker is purely the test Job resource fixture. The frozen v3 package required one CPU-only/no-GPU `htzhulab` Job. The one authorized submission attempt was rejected with `QOSMinGRES` and produced no JobId. Read-only scheduler policy evidence shows every QoS available for `htzhulab` requires `MinTRES=gres/gpu=1`. Therefore a CPU-only Job cannot legally exist in that protected partition.

## Minimal semantic change

Change only G4's real test Job fixture.

Old requirement:

```text
exactly one minimal CPU-only, no-GPU, future-BeginTime htzhulab Job
```

New requirement:

```text
exactly one minimal pending htzhulab Job that requests the site-required minimum gres/gpu=1,
is submitted on hold and with a future BeginTime, and is cancelled before it can become eligible to run
```

This Job is a scheduler record for cancellation acceptance only. It must never execute a workload or receive an allocated node/GPU.

## Frozen low-impact job contract

Before submission, use read-only scheduler inspection to select one QoS currently allowed for the user on `htzhulab` and confirm that its minimum GPU requirement is exactly or compatibly satisfied by one GPU request. Do not infer a QoS from history.

Submit exactly one Job with:

- partition: `htzhulab`;
- QoS: one currently authorized value discovered read-only;
- `gres/gpu=1` or the smallest exact syntax required by the current site;
- one CPU and minimum legal memory;
- walltime no more than five minutes unless the site enforces a larger minimum;
- `--hold`;
- BeginTime at least 24 hours in the future;
- harmless payload such as `sleep 30`;
- unique task-owned name;
- no explicit H100 request unless the current site rejects a generic one-GPU request and an exact type is required to satisfy the same minimum policy.

Immediately after submission, acceptance may continue only if read-only inspection proves:

- exactly one JobId was created;
- owner is the current user;
- partition is `htzhulab`;
- state is `PENDING`;
- no node is allocated;
- the Job is held and/or not eligible before the future BeginTime.

If any of those conditions fail, do not create a replacement Job. Stop and return to Planner with the exact scheduler state.

The Job must remain pending for the whole acceptance. Do not release it.

## G4 acceptance remains the same

Use that one exact Job twice:

1. request cancellation through the normal fresh Desktop Codex thread;
2. protected Hook denies the original cancellation with zero mutation;
3. choose `保留 Job`;
4. read-only verify the exact Job still exists and remains pending;
5. request cancellation again through the same normal entry;
6. choose `确认取消`;
7. PostToolUse reserves the confirmation identity, re-resolves JobId / partition / owner / state, and invokes exact `scancel` once;
8. read-only verify the Job is cancelled and no other Job changed.

No second Job may be created.

## What does not change

This amendment does not change:

- the global user Hook architecture;
- `config.toml` as fail-closed root;
- portable runtime selection;
- supervisor identity binding;
- fresh-session requirement;
- G1, G2, G3 or G5;
- the number of gates;
- PostToolUse reservation/reconciliation semantics;
- `slurm_routing.py` NO CHANGE;
- DII / CARE NO CHANGE;
- wrapper/PATH/Direct mode/Codex patch prohibitions;
- repository/Skill version policy;
- branch/worktree/task identity;
- normal non-force release closure.

## Authorization delta

The only new high-impact effect compared with approved v3 is permission to submit one pending protected-partition test Job carrying the site-required minimum one-GPU GRES request.

The user is not authorizing GPU computation. The Job must be held and future-dated, must never be released, and must be cancelled during the same acceptance run before it can become eligible to execute.

Because the previous approved package explicitly prohibited GPU/H100 test allocation, this amendment requires a narrow independent Critic PASS before the task-local Plan is revised and execution resumes.
