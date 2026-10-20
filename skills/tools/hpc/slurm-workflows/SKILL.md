---
name: slurm-workflows
description: Plan, submit, monitor, diagnose, and safely iterate Slurm jobs with live Slurm discovery, optional public policy overlays, sticky resource contracts, workload modes, and guarded capacity lifecycle semantics.
status: active
version: "0.4"
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-13
profile_tags:
  - hpc
  - server
  - slurm
recommended_scope: user
display_name: Slurm Workflows
short_description: Portable Slurm planning, routing, monitoring, and capacity lifecycle.
icon_small: assets/slurm-workflows.svg
icon_large: assets/slurm-workflows.svg
default_prompt:
  - Plan and monitor this Slurm workload using live Slurm context and local policy.
---
# Slurm Workflows

## Trigger Boundary

Use this skill for Slurm or HPC batch work that needs resource planning, script generation, submission review, job arrays, queue/status interpretation, log triage, failed-job diagnosis, or safe resubmission.

Do not use it for generic shell scripting or non-Slurm schedulers. Do not invent site-specific partition, account, QOS, hostname, node, reservation, or GPU-route values.

## Site Context

Before giving final Slurm commands, read the generated site context reference when present:

`references/_generated/site-profile.md`

If no generated reference exists, derive a bounded runtime `SiteContext` from current Slurm facts and local configuration. Public `site-profiles/*.json` are optional hard-policy overlays; they are not a supported-server registry. A third-party Slurm site with no committed profile is valid when live Slurm commands or explicit local facts provide enough context.

Keep these layers separate:

- live scheduler facts: what the current user can see now;
- profile policy: public hard policy that can restrict but not invent a route;
- local facts/preferences: private account, QOS, paths, partition preference, accelerator preference and local site id;
- workload contract: CPU, memory, GPU and walltime/availability accepted for this workload family.

Unknown account, QOS, partition, association, hidden partition or site policy fields stay `UNKNOWN`. Do not guess them.

Use `scripts/slurm_routing.py` for deterministic SiteContext normalization, routing order, resource-contract hysteresis, JobId safety checks, duplicate-race authority and bounded-contract checks, and persistent-capacity reconciliation.

## Workflow

1. Identify workload family and mode: finite batch, persistent reusable allocation, or short debug interactive shell.
2. Resolve the sticky resource contract. Reuse the accepted CPU, memory, GPU and walltime/availability request for the same comparable family unless an explicit override or approved accounting evidence justifies a change.
3. Discover current legal routes with bounded read-only Slurm inspection. Prefer explicit `sinfo -o/-O` fields, `scontrol show partition`, selected `scontrol show config` fields and optional `sacctmgr show assoc user=$USER`. Do not persist raw discovery dumps into tracked project source.
4. Filter candidates by hard resource needs and site policy. Apply local partition preference first, then local accelerator preference among remaining legal compatible routes. A hard accelerator requirement cannot be downgraded as a preference.
5. Use `sbatch --test-only` only as advisory evidence. If parsing fails or scheduler facts are hidden, fail closed instead of inventing a route.
6. Preserve JobId/dependency/array safety. Use native multi-partition widening when available; in-place partition updates require target-site/job-class evidence; cancel+resubmit is only for replaceable pending jobs after old-job inactivity is confirmed.
7. For persistent mode, reuse a compatible running allocation first. Maintain at most one lifecycle-owned intended successor for the earliest uncovered target window.
8. Monitor with bounded cadence and current scheduler/log evidence; distinguish queued, running, failed, cancelled, timed out, out-of-memory, dependency-held and completed states.
9. On failure, classify the cause and propose the smallest safe retry without silently shrinking resources for queue convenience.

## Resource Contract Hysteresis

Comparable workload family includes project identity, entrypoint/job family, workload class, material scale signature and accelerator requirement. Dates, seeds, output folders and route choice do not create a new family.

Precedence:

1. explicit current user/project request;
2. project-owned accepted contract;
3. user-local accepted workload-family contract;
4. initial estimate only when no accepted contract exists.

Accounting evidence must be comparable. OOM or trustworthy high-water memory can increase memory; an OOM increase after rounding must be strictly greater than the current accepted request. One low-memory run never decreases memory; at least three comparable successful low-memory runs are needed for a decrease candidate. Ambiguous history, unavailable completed-job comments, multi-node MaxRSS ambiguity, or low CPU efficiency alone must not auto-right-size. CPU is stable-first, batch TIMEOUT can support walltime increase, persistent availability duration is not derived from batch elapsed time, and GPU count/type is never silently downgraded.

## Persistent Capacity

`auto_maintain_successor=true` is only a preference. Automatic recurring mutation requires one-time bounded capacity-family enrollment that freezes local site id, family id, activation scope, accepted resource envelope, recurrence/window, max successor = 1 and allowed actions. Same-scope future occurrences do not re-prompt; material scope expansion requires new authorization.

An enrolled GPU family activates only for matching family/resource intent. A CPU-only workload on the same cluster must not maintain that GPU successor.

## Race Policy

Race execution means submitting two alternative jobs for the same workload and cancelling the loser after a winner is selected. It is off by default.

Use duplicate race only when all of the following are true:

- no site policy explicitly forbids duplicate submissions or race execution;
- the user or local machine configuration explicitly opts in to the extra resource cost;
- the race has exactly two candidate routes;
- both routes satisfy the same workload and scientific contract;
- both routes independently meet hard resource requirements;
- winner selection, loser cancellation, and near-simultaneous RUNNING behavior are frozen before submission.

`allowed` site policy is not enough without user opt-in. `missing`, `UNKNOWN`, `disabled_by_default`, and `explicit_user_opt_in` site policy are not default permission, but they can enter bounded race when the user opts in and there is no known prohibition. If a site policy says `forbidden`, `prohibited`, `disabled`, `disallowed`, or an equivalent hard no, fail closed even when the user opts in.

Treat site-policy plus user-opt-in checks as eligibility only. Final duplicate-race authorization must come from the complete bounded gate that validates workload identity, hard resources, two distinct routes, and the cancellation contract.

Do not change data, split, model, endpoint, GPU count, per-candidate walltime, training budget, or other scientific semantics to make a race possible. If a workload requires H100, do not race it on A100 unless the workload contract explicitly says both accelerator types are valid for the same result. If the scheduler or site rejects duplicate submission, fail closed and do not try another command form to bypass that policy.

## Protected cancellation

Failure isolation is part of this boundary. The command declarations contain a stable scope parser using a separately qualified system Python and a minimal environment. Before checking any mutable Slurm supervisor, runtime or policy identity, definitely unrelated Bash returns `{}`. Possible `scancel` tokens, paths, escaped/quoted spellings, and the harmless sentinel retain strict fail-closed handling. The parallel MCP handler also returns for unrelated commands before private runtime validation. After installation, use normal `config/batchWrite` with no edits and `reloadUserConfig=true` to refresh all loaded tasks, including unrelated projects; opening only a new Slurm chat is insufficient recovery for older declarations.

When the machine has installed the user-level protected-cancel contract, keep cancellation on the ordinary Codex `scancel` entry. Do not substitute a wrapper, PATH shim, terminal confirmation, daemon, or project-local Hook.

The installed contract applies a global `PreToolUse` / `PermissionRequest` boundary across working directories. The existing trusted command supervisor and a trusted `mcp_tool` handler match the same Bash `PreToolUse` event. The command guard always denies the original protected `scancel`; the MCP handler uses a local stdio MCP server to display a required single-select form in the owning root chat. Its only options are `确认取消` and `保留 Job`, with no Other or free-text alternative. Do not call `request_user_input` for cancellation authorization, and do not transport an answer through another chat. The old request-user-input `PostToolUse` binder is not installed by the production MCP route.

Install or render the private runtime with `scripts/setup_protected_cancel.py`. Production installation requires `--mcp-python` pointing to a separately qualified interpreter with the official MCP SDK 1.30.0; `--mcp-runtime-env KEY=VALUE` accepts only required loader variables. This SDK environment must be durable, not a `/tmp` probe. The independent guard still uses a qualified Python 3.9+ interpreter in its minimal environment; `--hook-python` and `--runtime-env KEY=VALUE` are its bounded overrides. The guard declaration binds its supervisor SHA256 and converts missing runtime, loader/127, nonzero exit, signal, timeout, corrupt identity, empty output, and invalid output into a valid deny. MCP failure cannot override this guard. Private policy and runtime identity remain JSON under `$CODEX_HOME/slurm-protected-cancel/`; public source must not contain site partitions, machine paths, accounts, or loader values.

The installer stages and qualifies the exact candidate before atomically replacing the task-owned private directory, writes `config.toml` last, preserves a recoverable private backup, and changes only the protected-cancel declaration and MCP-server blocks. Existing trust values, permission rules, unrelated configuration, and other Hooks stay unchanged. When a repair changes the guard and MCP binding, native review must re-trust only this product's changed `PreToolUse` command, `PreToolUse` MCP, and `PermissionRequest` command handlers; never trust all.

The MCP input template references only guaranteed Hook fields, never optional `agent_id` or `agent_type`. The command guard receives the complete original event, rejects explicit subagent context, and atomically creates an expiring pending identity with a private random nonce, session/turn/tool identity, exact target set, partition, owner, state, and operation. The MCP server requires its host-injected concrete `metadata.threadId` to equal the Hook's root `session_id`, then waits at most two seconds for that same pending identity; it cannot create one. A missing, mismatched, expired, or consumed pending never opens a form or grants cancellation. Headless or disconnected clients cannot replace a real elicitation response.

After native review, use the client's supported configuration reload and verify actual command/MCP Hook and elicitation events in the chat the user is using. A separate `hooks/list` read is not proof that the executing chat loaded the handler. Do not create an invisible chat to satisfy this check. The harmless diagnostic command `printf '__SLURM_PROTECTED_CANCEL_CARD_PROBE__\n'` requests the two-option form but never queries or mutates Slurm and is itself blocked. `scancel --help` must be denied before process launch without requesting cancellation authorization.

Retain, close, timeout, malformed answers, changed identity/partition/owner/state, replay and duplicate calls perform no protected mutation. Confirmation is bound to the Hook event and its automatically attached owning-chat identity. After a real `确认取消`, re-resolve the exact targets, durably reserve the one-shot identity, re-resolve once more, and invoke only the frozen absolute `scancel` path once. Keep durable audit records. Treat an ambiguous post-invocation outcome as consumed, reconcile it read-only, and never retry automatically.

## Outputs

Return the job script or commands, expected log paths, monitoring commands, stop conditions, and final verification checks. Submission is not completion; completion requires current job state and final output validation.
