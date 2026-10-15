# ER-02 isolation evidence

## Decision

`BLOCKED_BY_ISOLATION`

The current test process is not an isolated offline executor suitable for dangerous cancellation replay.

Observed before any dangerous simulation:

- real Slurm cancellation binary visible: `/usr/bin/scancel`;
- real Slurm allocation binary visible: `/usr/bin/salloc`;
- real SSH client visible: `/usr/bin/ssh`;
- SSH agent socket: absent, which is insufficient by itself to establish isolation;
- current process PID namespace: `pid:[4026534141]`;
- PID 1 namespace: `pid:[4026534141]`.

Because the process can see real mutation binaries and shares the host PID namespace, the Plan's same-process isolation conditions are not met. No fake or real `scancel`, no Python/shell/SSH cancellation endpoint, no Slurm API mutation, no batch/array cancellation replay, and no signal/tmux/allocation-holder replay was run. A fake `PATH`, dry-run flag, prompt assertion, or monkeypatch would not cure this isolation failure.

Only pure-function, static source, installation-copy, and read-only consumer inventory checks are eligible in this Stage A execution environment.
