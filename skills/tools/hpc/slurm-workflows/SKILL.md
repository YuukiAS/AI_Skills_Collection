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

Treat cancellation as destructive when an agent cancels a job, exact array element or explicit exact job set through any command/API path, or intentionally terminates an allocation holder. Natural completion, read-only inspection and monitoring are not cancellation.

Project automation must report a cancellation intent with exact JobIds to the root interactive Codex instead of starting a cancellation subprocess. The root chat issues the ordinary `scancel <exact-job-id>` command shape; a trusted `PreToolUse` Host Hook intercepts it before the tool shell. Array parents/ranges, heterogeneous jobs, steps, selectors, federation/cluster switches and non-default signal/batch/full semantics fail closed.

The Host Hook resolves every target with its frozen absolute `scontrol`, verifies scheduler ownership and a PENDING/RUNNING state, and reads the private `protected_cancel_partitions` policy. An unprotected exact target keeps the task's existing cancellation authorization: the Hook invokes the frozen absolute `scancel` once and rewrites the original shell input to a harmless success message, so the raw command never runs. If any target is protected, the Hook performs zero mutation and denies the original tool call with `NEEDS_INTERACTIVE_CHAT_CONFIRMATION` plus the exact target metadata.

Only an interactive root Codex chat may show the canonical native question: `Job <id> 当前位于受保护分区 <partition>。确认取消这个 Job 吗？`, with `确认取消` and `保留 Job` as its two options. Protected mutation authority belongs only to the trusted synchronous `PostToolUse` Host Hook for `^request_user_input$`. One content-addressed Hook under the active user `$CODEX_HOME/slurm-protected-cancel/` is shared across repositories and bound by exact path and SHA-256 in the user-level declaration. Before one exact absolute-path `scancel`, it validates the genuine root-chat event, canonical question and response, one-time session/turn/tool/question identity, runtime identity, exact JobId/Partition/operation, a fresh absolute-path re-resolution, current protected status and an atomic consumed reservation.

Empty, timed-out, retained, free-text or mismatched answers do not cancel. A Goal, old race opt-in, assistant text, `auto_review`, UserPromptSubmit, subagent message, fabricated JSON, persisted confirmation token or later shell invocation never grants protected cancellation authority. Headless execution fails closed and requires an interactive root chat. User-level Codex permissions independently deny the private Hook runtime plus both the configured `scancel` path and its canonical realpath; user-level execpolicy also forbids raw and absolute `scancel`. Hook failure therefore cannot fall through to the real binary inside a Codex tool sandbox. These controls do not restrict a user's ordinary terminal outside Codex.

## Outputs

Return the job script or commands, expected log paths, monitoring commands, stop conditions, and final verification checks. Submission is not completion; completion requires current job state and final output validation.
