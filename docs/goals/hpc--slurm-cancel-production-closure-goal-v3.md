# Canonical Goal v3 — hpc--slurm-cancel-production-closure

Status: EXECUTION_READY_REVIEW_PENDING  
Date: 2026-10-19

## Canonical locators

- task_key: `hpc--slurm-cancel-production-closure`
- target repo: `YuukiAS/AI_Skills_Collection`
- source design base: `main@23f51b0bebd8a32f49d899f7fae1ee0e5f17e4cd`
- approved Proposal:
  `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md`
- Execution Plan:
  `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_PLAN_V3_2026-10-19.md`
- historical failed candidate, read-only selective-port source:
  `work/hpc--slurm-protected-partition-chat-confirmation-v2-1@1b8df2c1f2b93de1605d571f5125cd4aaa99fd20`

This Goal is not implementation authorization by itself. Codex may execute it only after an independent execution-ready Critic PASS over the same v3 Proposal/Plan/Goal/Kickoff package and after the user sends the approved handoff.

## Goal

Finish and formally release portable protected cancellation for the existing standalone `slurm-workflows` Skill without changing its routing architecture.

The finished behavior is:

- all supported exact Codex `scancel` calls pass through one user-level global Hook boundary;
- unprotected Jobs keep ordinary Codex behavior;
- a protected Job's first cancellation is denied with zero mutation;
- the current root interactive chat asks `确认取消` / `保留 Job`;
- only fresh explicit confirmation for the exact target can lead to one re-resolved exact `scancel`;
- headless protected cancellation fails closed;
- Hook runtime failure cannot silently become permission to run the underlying Bash command.

The public Skill must stay portable. No public Longleaf path, `htzhulab`, loader path or machine secret may be embedded in source.

## Frozen implementation decisions

Do not redesign these decisions:

1. Keep user-level global `PreToolUse`, `PermissionRequest`, `PostToolUse`.
2. The trusted `config.toml` declaration is the fail-closed root.
3. The external event-aware supervisor is Hook infrastructure only, not a `scancel` wrapper.
4. The declaration binds the supervisor's expected content identity; the supervisor cannot obtain its own expected hash from writable runtime state.
5. Installation must discover and qualify the production Hook interpreter independently from the installer interpreter.
6. Qualification uses the final sanitized minimal environment before activation.
7. Machine-specific minimal loader variables are allowed only in private runtime state after qualification.
8. Private protected-partition policy uses JSON and the Hook targets Python 3.9+ unless a proven unavoidable requirement forces Planner re-entry.
9. PreToolUse/PermissionRequest child-runtime failure, exit 127, timeout, corruption or invalid output must become a valid deny with underlying Bash launch count zero.
10. PostToolUse reserves before any possible `scancel`; ambiguous post-invocation outcomes are never automatically retried and recover only through read-only scheduler reconciliation.
11. `slurm_routing.py` is default NO CHANGE.
12. DII and CARE are default NO CHANGE; only new direct-source evidence can reopen minimal adaptation.

## Explicitly forbidden substitutions

Do not add or switch to:

- `scancel` wrapper;
- PATH interception/shim;
- project-local Hook copies;
- terminal confirmer;
- persisted next-shell confirmation token;
- daemon/broker/database;
- Direct mode/model-catalog override;
- OpenAI Codex patch;
- second task/successor;
- additional real Slurm Jobs to chase a PASS.

## Required workflow identity after approval

Intended execution identity:

- R: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
- branch: `reviewed/hpc--slurm-cancel-production-closure`
- W: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure`

Before mutation, reverify R/origin/clean state/current `origin/main`/branch absence/worktree-path absence. Material semantic drift or identity conflict returns to Planner/Critic before branch/worktree creation. No alternate path or branch is authorized.

Use the current Reviewed Handoff normal entry and current Bridge Kit contract; do not build another orchestration layer.

## Required maintenance owners

- workflow: `workflow-core`
- AI Skills maintenance: `ai-skills-core`
- domain: standalone `slurm-workflows`

## Required gates

The exact five release gates from Proposal/Plan v3 are mandatory and must be passed by one final candidate:

- G1 portable installation + atomic activation;
- G2 infrastructure failure fails closed, including at least one real Codex Hook normal-entry fault injection with valid deny and underlying Bash launch count zero;
- G3 protected/unprotected semantics + full should-not-change Slurm regression;
- G4 Longleaf production normal entry: harmless `scancel --help`, then exactly one future CPU-only `htzhulab` Job retained once and confirmed/cancelled once;
- G5 formal release/install identity is the same final candidate.

Do not add a sixth gate merely to restate the same capability.

## Live mutation boundary after approved user handoff

Only the later user-sent, Critic-approved handoff may authorize these effects:

- task branch/worktree creation at the exact identities above;
- task-owned edits in the target repository;
- bounded changes to
  `/users/a/e/aereinh/.codex/config.toml`
  limited to the protected-cancel declaration block;
- bounded changes under
  `/users/a/e/aereinh/.codex/slurm-protected-cancel/`;
- required backup/restore of those task-owned live surfaces;
- one fresh/reloaded Desktop remote session when required to load the frozen Hook declaration;
- exactly one minimal CPU-only future-BeginTime `htzhulab` test Job;
- cancellation of that exact task-created Job only after the approved confirmation flow;
- ordinary non-force task publication and, only after all gates/review/acceptance, normal formal repository release closure.

No other existing Slurm Job may be mutated. No GPU/H100 test allocation is authorized.

## Version closure

At execution time, re-read current formal version sources.

If formal versions are still:

- repository `5.5.0`
- `slurm-workflows 0.4`

then the planned release is:

- repository `5.5.1`
- `slurm-workflows 0.5`

Repository bump decision: PATCH.  
Affected central Marketplace plugins: all NO_BUMP.

If versions moved, compute the next valid compatible release under the current policy; do not reuse stale numbers.

## Maintenance-board pending work

Tracking/Project mutation is still pending because this Planner surface cannot both invoke the required Clear Writing mutation path and mutate GitHub Project state. Do not ask the user to maintain it manually.

The next Project-capable + Clear-Writing-capable maintenance entry must create/bind the single tracking Issue for this same task, set `Status=DOING`, apply the approved standalone-skill labels, and backfill the canonical `tracking: #N`.

This pending board mutation is bookkeeping; it does not authorize implementation or weaken product gates.

## Completion

Positive completion requires:

`same final candidate -> portable install -> real fail-closed Hook proof -> complete deterministic regressions -> one-Job Longleaf retain/confirm proof -> independent implementation review -> formal release/install identity verification`.

Do not claim completion from tests, CI, Hook trust, file presence or a historical candidate alone.
