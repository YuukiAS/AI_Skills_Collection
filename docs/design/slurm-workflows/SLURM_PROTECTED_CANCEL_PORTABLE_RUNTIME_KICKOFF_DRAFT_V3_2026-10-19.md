# Slurm protected cancel portable runtime — Kickoff Draft v3

Status: DRAFT_ONLY_NOT_AUTHORIZED  
Date: 2026-10-19

This file is the future user-to-Codex kickoff draft for the same task
`hpc--slurm-cancel-production-closure`.

It is **not** current authorization. It becomes executable only after an independent Critic gives execution-ready PASS on the same v3 Proposal/Execution Plan/Goal/Kickoff package and the user then sends the approved short handoff.

## Approved package locators

- Proposal:
  `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md`
- Execution Plan:
  `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_PLAN_V3_2026-10-19.md`
- Canonical Goal:
  `docs/goals/hpc--slurm-cancel-production-closure-goal-v3.md`
- source design base:
  `main@23f51b0bebd8a32f49d899f7fae1ee0e5f17e4cd`

## Intended execution identity

After approval, use exactly:

- repository: `YuukiAS/AI_Skills_Collection`
- canonical Longleaf checkout R:
  `/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
- branch:
  `reviewed/hpc--slurm-cancel-production-closure`
- worktree W:
  `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure`
- task key:
  `hpc--slurm-cancel-production-closure`

The failed historical branch
`work/hpc--slurm-protected-partition-chat-confirmation-v2-1`
is read-only selective-port evidence only.

Before creating anything, fetch current `origin/main` and verify repo/origin/clean ownership, exact branch absence, exact worktree-path absence and semantic compatibility with the approved v3 package. If any of these fail, stop before mutation and return to Planner/Critic. Do not invent an alternate branch, worktree, clone, `/tmp` path or successor task.

Use the current Bridge Kit Reviewed Handoff normal entry rather than raw branch/worktree/push operations.

## Frozen implementation instruction

Implement the approved v3 package exactly. Do not redesign it.

The architecture is:

`ordinary Codex scancel -> global user Hook -> protected target deny -> native current-chat confirmation -> PostToolUse re-resolution -> exact scancel once`.

Keep:

- user-level `PreToolUse`, `PermissionRequest`, `PostToolUse`;
- the trusted `config.toml` declaration as the fail-closed root;
- a small event-aware Hook supervisor whose expected content identity is bound by trusted declaration;
- portable production-Python discovery/qualification in the final sanitized minimal environment;
- machine-private runtime/policy identities;
- one-time reservation before possible protected mutation;
- no automatic retry after ambiguous post-invocation outcome.

Do not add:

- `scancel` wrapper;
- PATH shim/interception;
- project-local protected-cancel Hook;
- terminal confirmer or next-shell token;
- Direct mode/model override;
- Codex patch;
- daemon/database/broker;
- new Gate;
- successor task.

`slurm_routing.py` is NO CHANGE unless direct necessity is proven and the existing plan's regression contract is satisfied.

DII and CARE are NO CHANGE unless current formal source itself proves a live direct protected-`scancel` bypass.

## Maintenance execution requirements

Use:

- `workflow-core` for the execution/review workflow;
- installed/enabled `ai-skills-core` for AI Skills maintenance preflight;
- standalone `slurm-workflows` as domain owner.

Do not treat reading the maintenance source Skill as proof that the installed production maintenance capability was invoked.

## Authorization envelope if the user sends the approved handoff

The later user-sent handoff authorizes only this bounded task:

### Repository effects

- create/use the exact approved task branch/worktree above through the normal reviewed entry;
- edit only files required by Proposal/Plan v3;
- ordinary task-owned commits and bounded non-force publication through the approved workflow;
- after all gates/review/acceptance, perform the repository's normal compatible formal release closure.

No force push, reset/clean of unrelated work, alternate branch, unrelated repository mutation or successor task is authorized.

### Live Longleaf `CODEX_HOME` effects

Target:

`/users/a/e/aereinh/.codex`

Allowed only after G1-G3 and real Hook-normal-entry fault injection pass:

- back up the current task-owned protected-cancel configuration/runtime;
- change only the task-owned protected-cancel declaration block in
  `/users/a/e/aereinh/.codex/config.toml`;
- change only
  `/users/a/e/aereinh/.codex/slurm-protected-cancel/`;
- preserve unrelated Hooks, permissions, trust state and other user config;
- perform only the necessary final trust/reload action after final declaration bytes are frozen;
- restore previous task-owned state if the harmless live probe fails.

Do not modify global shell startup, PATH, model catalog, Direct mode, OpenAI Codex binaries or other machines.

### Slurm effects

Only after the harmless `scancel --help` probe proves valid Hook deny and that the real `scancel` process did not start:

- create exactly one minimal CPU-only, no-GPU, harmless `htzhulab` Job;
- set BeginTime at least four hours in the future;
- use the same exact Job for both acceptance interactions;
- first choose `保留 Job` and verify it remains pending;
- then choose `确认取消`, re-resolve, and cancel that exact Job once;
- no other existing Job may be cancelled, updated, signalled or otherwise mutated.

No GPU/H100 allocation is authorized.

## Gate execution order

Run the approved five gates only:

1. G1 portable install and atomic activation;
2. G2 infrastructure failure fails closed, including one real Codex Hook normal-entry fault injection with valid deny and Bash launch count zero;
3. G3 protected/unprotected semantics and full existing Slurm regression;
4. G4 harmless live probe then exactly one real Longleaf Job retain/confirm acceptance;
5. G5 same-candidate formal release/install identity.

Cheap deterministic evidence precedes real Slurm mutation.

Do not use fake-Slurm or CI as a substitute for G4.

Do not combine evidence from different candidates.

## Version closure

Immediately before release, re-read current version sources and
`docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`.

If the formal line remains repository `5.5.0` and Skill `0.4`, release repository `5.5.1` with `slurm-workflows 0.5`.

If it moved, calculate the next valid compatible release from current formal source.

If README changes, the installed Clear Writing capability must actually review the affected reader-facing region before final release.

## Tracking-board boundary

Do not invent a tracking Issue or Project state during bootstrap.

The current package records a pending maintenance mutation because this Planner surface lacked both the required Clear Writing mutation path and GitHub Project mutation surface. A later Project-capable + Clear-Writing-capable maintenance entry must bind the same task to one tracking Issue, set DOING, and backfill `tracking: #N`; the user must not be asked to maintain the board manually.

## Stop rules

Stop before further mutation and return to Planner/Critic if:

- latest-main semantic drift changes the approved architecture;
- exact branch/worktree identity cannot be safely created;
- config-root/supervisor cannot return a valid deny with Python unavailable;
- the real Codex Hook fault injection reports ordinary Hook failure or launches Bash;
- task-owned live config cannot be changed/restored without touching unrelated config;
- `scancel --help` starts real `scancel`;
- the single real Job cannot be created under the exact low-impact contract;
- implementation requires wrapper/PATH interception/Direct mode/Codex patch/new daemon/new Gate.

Ordinary implementation bugs and deterministic test failures inside the approved scope are not reasons to ask the user to redesign the task; repair them within the frozen package.

## Completion condition

Do not say the plugin is complete until the same final candidate has:

- passed G1-G3;
- passed real Hook-normal-entry fail-closed evidence;
- passed G4 with the single real Job;
- passed required independent implementation review;
- completed G5 formal release/install identity verification.

No current action is authorized merely by this draft.
