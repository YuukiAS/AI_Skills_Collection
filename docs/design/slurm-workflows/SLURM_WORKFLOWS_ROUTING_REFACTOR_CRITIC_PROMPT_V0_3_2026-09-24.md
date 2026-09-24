# Slurm Workflows Routing Refactor — Critic Prompt v0.3

你继续作为 AI Research Stack 的独立 Critic。

这是同一个 task key 的 architecture re-review，不是 successor task，也不是 execution-ready review。

## Active Review Context

Target repository:

`YuukiAS/AI_Skills_Collection`

Target:

standalone Skill / HPC / `slurm-workflows`

Design topic / task key:

`hpc--slurm-workflows-routing-refactor`

Review stage:

`ARCHITECTURE_REVIEW_V0_3`

New Proposal:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_3_2026-09-24.md`

Proposal commit:

`f9c0e3abbffaa6677c1f0acec510c47106d66aa1`

Previous approved Proposal v0.2:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_2_2026-09-24.md`

v0.2 commit:

`b1d516c173ce838fd5eb9f39ae0a117bcb7f517e`

Previous architecture Critic PASS:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_2_2026-09-24.md`

PASS commit:

`08c598f748903ec48c07b96fd1b35dc96561699d`

Execution-ready Critic REVISE that introduced the new requirements:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-24.md`

REVISE commit:

`b211db38bdcff8772c1be493d81b95a5b04a9059`

Old architecture blockers remain closed and MUST NOT be reopened without new contradictory evidence:

- SWR-B1 = CLOSED
- SWR-B2 = CLOSED

Current new blockers under review:

- SWR-ER-B1 — stable resource contract
- SWR-ER-B2 — persistent/weekly GPU capacity lifecycle
- SWR-ER-B3 — workload-mode routing: batch vs persistent allocation vs debug interactive

No execution branch/worktree exists.

Future locators remain only future locators:

```text
branch:
reviewed/hpc--slurm-workflows-routing-refactor

worktree:
/tmp/ai-skills-hpc-slurm-workflows-routing-refactor
```

## 1. Required source read

First actually read latest main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

Then read:

- Proposal v0.3
- Proposal v0.2
- v0.2 architecture PASS
- latest execution-ready REVISE

Read only the necessary current production source needed to check feasibility:

- `skills/tools/hpc/slurm-workflows/SKILL.md`
- relevant `scripts/skills.py` environment/local config path
- current site profiles/local override docs/tests as needed

## 2. Bridge Kit must be independently checked read-only

Repository:

`YuukiAS/GPT_Codex_AI_Bridge_Kit`

At least read current main:

- `docs/design/0.8.0_persistent_run.md`
- `templates/persistent_run/CONTRACT_TEMPLATE.md`
- `templates/persistent_run/AGENTS_SNIPPET.md`

Do not modify Bridge Kit.

Check whether Planner is correct that:

- Bridge Persistent Run already exposes persistent execution intent;
- Bridge can reuse an existing interactive Slurm allocation;
- Bridge does not own scientific/resource budget;
- the original Goal/task/workflow owns resource semantics;
- therefore Slurm allocation/resource policy belongs in Slurm Workflows unless a real consumer proves Bridge cannot convey intent.

If current Bridge source contradicts that, report it as a real blocker.

## 3. Recheck only the three new blockers

### SWR-ER-B1

Planner disposition:

`PARTIAL_ACCEPT`

v0.3 adds:

- comparable workload family:
  project + entrypoint/job family + workload class + material scale signature + accelerator requirement;
- explicit family id preferred;
- stable family marker via user-settable Slurm Comment for new jobs;
- a small current-state config:
  `~/.config/ai-skills/slurm-workflows.toml`;
- no history DB; historical evidence is queried from `sacct`;
- once accepted, resource contract is reused unchanged by default;
- user/project explicit resources override;
- route choice cannot silently change resource contract;
- memory hysteresis:
  - OOM immediate increase eligibility;
  - trustworthy >=85% high-water allows increase candidate;
  - target about 1.25x comparable high-water;
  - no one-run decrease;
  - >=3 comparable successful runs all <50% allow decrease candidate;
  - decrease target about 1.5x recent high-water;
  - MaxRSS cannot be blindly used as total allocation memory for multi-task/multi-node cases;
- CPU stable by default; TotalCPU/(Elapsed*AllocCPUS) is diagnostic only;
- batch walltime uses similar sticky/hysteresis logic;
- persistent availability duration does not use batch elapsed history;
- GPU count/type never silently reduced for routing.

Please decide whether SWR-ER-B1 is CLOSED.

Attack both sides:

- Is this too much configuration/state for the actual problem?
- Is it still too weak to stop resource flapping or over/under-requesting?
- Is the workload-family definition stable enough?
- Is a current-state TOML justified vs abusing site local-overrides?
- Are the memory heuristics safe given actual `sacct` semantics?
- Does the Plan avoid pretending MaxRSS means total job memory?
- Should CPU remain stable rather than be auto-tuned?

Do not require a queue-history DB or ML predictor merely for comfort.

### SWR-ER-B2

Planner disposition:

`ACCEPT`

v0.3 replaces independent calendar-named weekly jobs with:

`persistent capacity family + target availability window + one-active/one-successor reconciliation`.

Key contract:

- stable capacity family, not dated job name, is identity;
- compatible RUNNING allocation is reused even if its name says “last week”;
- next target occurrence is considered satisfied if current allocation covers target_ready_by + minimum useful duration;
- at most one lifecycle-owned intended successor;
- existing compatible pending successor -> no duplicate;
- if current active now covers next target, successor target advances to the earliest uncovered recurrence;
- stale/redundant lifecycle-owned replaceable pending successor may use already-approved state-safe cancellation contract;
- pre-existing/identity-sensitive jobs are not auto-cancelled;
- no daemon;
- when `auto_maintain_successor=true`, every normal Slurm Workflows submit / allocation / attach-resume / monitor entry performs one bounded reconciliation;
- if earliest uncovered target has no successor, that invocation creates exactly one successor;
- therefore the user should not need a manual weekend “is next week queued?” check as long as they are using Slurm Workflows normally;
- no activity -> no background magic; this is best-effort.

Calendar semantics:

- target_ready_by is desired availability, not guarantee;
- successor becomes eligible at target_ready_by - lead_time;
- submitting the BeginTime job earlier does not falsely claim priority age before eligibility;
- preferred bounded-end candidate:
  `--begin + --deadline + --time + --time-min`
  only after target-site capability validation;
- if unsupported/ambiguous, fail closed rather than return to drifting fixed-duration weekly jobs;
- no post-grant TimeLimit mutation/cron/daemon is silently introduced;
- ordinary Longleaf user semantics are BEST_EFFORT;
- advanced reservation is mentioned only as the true guarantee boundary and is explicitly NOT a solution this user will seek/create.

Please decide whether SWR-ER-B2 is CLOSED.

Critically assess whether the “on every Slurm activity reconcile one successor” design is actually the simplest useful answer to the user's request, or whether it creates hidden repeated side effects / excess queue load.

Also check whether `--deadline + --time-min` is being used only within what SchedMD actually promises.

### SWR-ER-B3

Planner disposition:

`ACCEPT`

v0.3 adds workload mode:

- finite unattended compute -> batch
- persistent reusable workspace/capacity -> persistent allocation
- short debugging shell -> debug interactive

Persistent mode:

- reuse compatible RUNNING allocation first;
- allocation semantics are separate from scientific command;
- `salloc --no-shell + srun --jobid` is a preferred candidate backend, not yet claimed as Longleaf-verified;
- caller/disconnect/attach/cleanup semantics must be validated before automatic production use;
- if that backend cannot support detached successor acquisition, a site-approved allocation-holder backend may be researched, but it must remain a capacity lease backend rather than reverting all scientific work to batch mode;
- no hardcoded interact partition/QOS;
- no claim that salloc bypasses queue;
- Bridge Kit remains unchanged because its existing contract already exposes persistent intent/resource ownership.

Please decide whether SWR-ER-B3 is CLOSED.

Check especially whether the candidate backend section is too ambiguous for architecture approval, or appropriately leaves site implementation behind a bounded probe.

## 4. Independent SchedMD web check required

Do not only trust Planner's external research.

At minimum independently check current SchedMD official docs for:

- `sacct`: ReqMem / MaxRSS / ReqCPUS / AllocCPUS / TotalCPU / Elapsed / Timelimit / ReqTRES / AllocTRES / Comment semantics;
- `sbatch`: `--comment`, `--begin`, `--deadline`, `--time-min`;
- priority age and `PriorityFlags=ACCRUE_ALWAYS`;
- `salloc --no-shell`;
- later `srun --jobid`;
- advanced reservation authority.

Verify that Planner does not overclaim:

- MaxRSS as total memory;
- BeginTime as reservation;
- early future submission as guaranteed age priority;
- deadline/time-min as future guarantee;
- salloc as queue bypass;
- ordinary user ability to create advanced reservation.

## 5. Complexity check

The user explicitly wants a small architecture.

Evaluate whether v0.3 still satisfies:

```text
workload intent
-> mode

sticky resource contract
-> resource request

site/local policy
-> legal route / availability preference

live allocation state
-> reuse or one successor

scheduler evidence
-> probe / widen / fail closed
```

and does NOT become:

- queue-history database;
- scheduler predictor;
- custom scheduler;
- daemon/watcher;
- dependency remapper;
- hostname ranking engine.

The new local TOML is allowed only if it is truly a declarative current-state contract, not a hidden history/state machine.

## 6. Gate review

Planner keeps G1-G6 from approved v0.2 and adds only:

### G7 — resource-contract stability/right-sizing

Check that it proves a distinct capability and includes:

- unchanged contract without evidence;
- user/project override;
- OOM/high-memory increase;
- one low run no decrease;
- >=3 comparable low runs decrease candidate;
- incomparable MaxRSS -> no auto resize;
- low CPU efficiency on GPU/IO-bound -> no auto cut;
- timeout walltime evidence;
- routing cannot silently downgrade contract.

### G8 — persistent mode/capacity lifecycle

Check that it proves a distinct capability and includes:

- batch vs persistent vs debug mode;
- reuse compatible running allocation;
- current allocation can satisfy next target regardless of calendar job name;
- one pending successor max;
- missing successor auto-maintained on normal Slurm activity;
- BeginTime != reservation;
- BEST_EFFORT vs GUARANTEED truth;
- unsupported calendar-bounded site semantics fail closed;
- Bridge intent consumed without Bridge modification;
- no interactive queue-bypass claim.

Do not add gates mechanically unless another truly distinct user capability is missing.

## 7. Site validation boundary

Proposal v0.3 does not execute real Slurm state.

It only says a later execution package may propose minimal bounded probes for:

- P-A calendar-bound request semantics;
- P-B persistent allocation backend;
- existing P-C in-place partition widening.

Critic should check the principle:

> later probes must be minimized/combined when possible; three conceptual questions do not justify three automatic real jobs.

Do not demand actual probe evidence at architecture-review stage.

## 8. Version/scope

Architecture docs do not bump version.

If eventually implemented/released:

- standalone `slurm-workflows: 0.1 -> 0.2`
- repository: next PATCH from actual release-time VERSION
- all central Plugins: NO_BUMP

No Bridge Kit version/change belongs to this task.

## 9. Result

Return:

`RESULT = PASS`

or

`RESULT = REVISE`

Explicitly return:

```text
SWR-ER-B1 = CLOSED | OPEN
SWR-ER-B2 = CLOSED | OPEN
SWR-ER-B3 = CLOSED | OPEN
```

If REVISE, every blocker must include:

- requirement;
- direct source/official evidence;
- causal user-visible/resource risk;
- minimum closure condition.

Do not reopen SWR-B1/SWR-B2 from v0.2 unless v0.3 directly regresses them.

If PASS, bind:

```text
PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_3

PASS_SCOPE =
amended architecture/design only; no execution authorization
```

## 10. Review record

You are authorized only to write your own v0.3 architecture review document on current main:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_3_2026-09-24.md`

Commit + ordinary non-force push only that review document.

Do NOT:

- modify production source/tests;
- create execution branch/worktree;
- execute real Slurm mutation;
- update the old execution package yet;
- modify Bridge Kit;
- bump version;
- start Executor;
- call paid API.

Finally report:

```text
RESULT =
SWR-ER-B1 =
SWR-ER-B2 =
SWR-ER-B3 =
REVIEW_PATH =
REVIEW_COMMIT =
PROPOSAL_COMMIT = f9c0e3abbffaa6677c1f0acec510c47106d66aa1
BRIDGE_CHANGE_REQUIRED = YES | NO
EXTERNAL_SOURCES_CHECKED =
```
