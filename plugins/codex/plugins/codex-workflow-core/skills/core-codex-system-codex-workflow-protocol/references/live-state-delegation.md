# Live-State and Delegation Supervision

Use this reference for tmux, Slurm, watchdogs, tunnels, frontend previews, long-running jobs, daemon processes, child Codex sessions, and sub-agents.

## Rule

Starting a session, submitting a job, launching a child agent, or seeing an old status file is not completion. Verify current live state and the requested final output.

## Check by surface

- `tmux`: list sessions/windows, confirm active command, inspect recent pane output, and distinguish attached shell continuity from task progress.
- `Slurm`: check job state, node, elapsed time, stdout/stderr paths, exit status, and final output files.
- `watchdog`: compare process state, watchdog state file, timestamps, and latest logs.
- `tunnels`: verify tunnel process and client-visible behavior; a healthy tunnel message is not enough if SSH/browser clients fail.
- `frontend preview`: check dev server/build logs, browser console, rendered page, production/export output when relevant, and stale build artifacts.
- `long-running jobs`: record owner, budget, stop condition, polling plan, logs, and final artifact path.
- `child Codex/sub-agent`: define scope, forbidden actions, expected artifact, and verification owner before launch.

## Drift and stale-artifact checks

- Compare timestamps of logs, state files, and produced artifacts against the current run.
- Confirm a child agent changed the intended files and did not overwrite unrelated user work.
- Main agent must perform final integration and acceptance. Do not forward a child response as final without checking artifacts, diffs, and gates.

## Final report

Report process/job IDs, node or host when relevant, log paths, status files, artifact paths, current state, and unverified boundaries.
