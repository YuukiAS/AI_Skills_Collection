# Slurm protected cancel portable runtime — Proposal v3

Status: DESIGN_PASS  
Date: 2026-10-19

## Active Design Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-cancel-production-closure`
- source_branch_or_ref: `main@23f51b0bebd8a32f49d899f7fae1ee0e5f17e4cd`
- proposal_path_and_version: this file / v3
- historical failed candidate: `work/hpc--slurm-protected-partition-chat-confirmation-v2-1@1b8df2c1f2b93de1605d571f5125cd4aaa99fd20`
- historical candidate relation to current main: diverged, ahead 12 / behind 23
- execution branch/worktree: not created in this Planner round

This file records the already independently approved Proposal v3. It does not reopen architecture, authorize implementation, install anything into a live `CODEX_HOME`, run Slurm, create a test Job, or publish a release.

## User problem and positive outcome

The user wants one simple invariant: when Codex is about to cancel a Slurm Job that is currently in a user-configured protected partition, the original cancellation must not happen until the current root interactive Codex chat receives the user's fresh confirmation for that exact Job.

For Longleaf the current private policy is expected to include `htzhulab`, but that site value is machine-private and must not be hard-coded into the public Skill.

The positive outcome is therefore:

1. every supported exact Codex `scancel` path reaches one user-level global Hook boundary before the Bash command starts;
2. an unprotected Job keeps ordinary Codex execution without a protected-cancel prompt;
3. a protected Job's first cancellation attempt performs zero Slurm mutation and produces the native choices `确认取消` / `保留 Job`;
4. only `确认取消` in the current root interactive turn can lead to one re-resolved exact cancellation;
5. headless protected cancellation fails closed;
6. Hook-runtime failure itself cannot silently turn into permission to execute the underlying Bash command.

The maximum claim is Codex normal-entry enforcement plus explicitly adapted consumers. This proposal does not claim same-UID operating-system isolation and does not restrict the user's ordinary SSH terminal.

## Verified root cause

The architecture failure was not a Code Mode bypass. Runtime investigation established that the real nested shell path reached:

`functions.exec -> tools.exec_command -> ExecCommandHandler -> Bash PreToolUse -> global user Hook`.

The Hook then failed before its Python code ran. The installed command had frozen an HPC Python interpreter whose executable existed, but whose required `libpython3.12.so.1.0` was outside the dynamic loader search path inherited by the Desktop remote app-server. The Hook child exited `127`. Codex 0.160.1 treated that ordinary Hook process failure as non-blocking, so the original Bash command continued.

Therefore the defect is the portable Hook runtime and launcher failure semantics, not Slurm routing, matcher selection, Hook trust, `CODEX_HOME`, nested Code Mode dispatch, DII/CARE logic, or OpenAI Codex lifecycle.

## Five-pass preflight summary

### Product

The normal user experience is unchanged except for protected cancellation. The user does not opt into a new command, wrapper, profile, daemon, or PATH layout. Codex continues to issue ordinary exact `scancel`; the user-level Hook is the enforcement boundary.

### Reality

Current formal `main` and `release` both ship repository `5.5.0` and `slurm-workflows 0.4`, which contain routing, resource-contract, persistent-capacity, race and Job-safety behavior but no released protected-cancel runtime. The failed v2.1 candidate contains useful Hook business logic and tests but is not current source and must not be continued as the release candidate.

### Alternatives considered

- **Skill-only cooperation:** rejected because it cannot enforce cancellation across Codex execution paths.
- **`scancel` wrapper / PATH shim:** rejected because it creates a second command surface and is avoidable now that the real Bash Hook path is proven.
- **Direct tool mode / model-catalog override:** rejected because GPT-5.6 Sol is currently delivered through Code Mode and nested Bash Hook dispatch is already proven.
- **OpenAI Codex patch:** rejected because the actual nested Hook lifecycle works; the fault is local launcher/runtime deployment.
- **Longleaf-only `LD_LIBRARY_PATH` patch:** rejected as the product fix because the Skill must install portably across machines. A machine-private minimal loader environment remains allowed only when that machine has no self-contained compatible interpreter.
- **User-level global Hook with portable runtime qualification and fail-closed launcher:** selected.

### Counterevidence

The design must fail if the outer Hook boundary cannot return a valid event-specific deny when the Python child is unavailable, if a final Codex `scancel --help` probe still starts the real `scancel`, if activation cannot preserve unrelated `config.toml` content and Hook trust, or if the final release candidate differs from the candidate that passed production gates.

### Execution viability

Implementation is bounded to the existing standalone Skill, its protected-cancel installer/runtime, focused tests, release metadata and one real Longleaf acceptance Job. No daemon, database, new controller, Code Mode patch, Direct-mode override, PATH interception or new cross-repo workflow is required.

## Frozen architecture

### 1. One global enforcement boundary

The enforcement boundary remains one user-level global Hook declaration set under the selected `CODEX_HOME`:

- `PreToolUse` on `^Bash$`: primary pre-execution gate;
- `PermissionRequest` on `^Bash$`: second protected-cancel check before an ordinary permission approval can bypass the protected policy;
- `PostToolUse` on `^request_user_input$`: receives the canonical native confirmation event, re-resolves the exact target and owns the single protected mutation.

Project-local Hook copies, Slurm-specific permission profiles, PATH interception, `scancel` wrappers and next-shell confirmation-token flows remain forbidden.

### 2. Portable runtime selection

The installer must not freeze `sys.executable` merely because it is running successfully during installation.

Installation Python and Hook runtime Python are separate identities. Candidate runtime selection is deterministic:

1. explicit machine-local override, when configured;
2. stable system Python;
3. resolved `python3` from the sanitized installation environment;
4. the installer interpreter only as the last candidate.

A candidate is accepted only after it starts in the same final sanitized minimal environment intended for production and can load the formal Hook plus its required standard library and process a harmless synthetic Hook event.

The public Skill stores no Longleaf path, protected partition, loader path or secret. Machine-private runtime data stores the selected interpreter identity, allowlisted environment needed to launch it, absolute `scontrol` / `scancel` identities, protected partitions and content hashes.

The protected policy moves from TOML to JSON so the Hook can target Python 3.9+ rather than requiring Python 3.11 only for `tomllib`.

If a machine has no self-contained compatible Python but a candidate becomes valid with a small machine-specific loader environment, that minimal environment may be frozen privately after qualification. The installer must not capture the whole interactive shell/module environment and must not persist credentials or unrelated environment values.

### 3. The config declaration is the fail-closed root

The trusted `config.toml` declaration is the root of failure closure. It must bind the expected external supervisor identity from trusted generated configuration; the supervisor must never obtain its own expected hash from writable runtime state.

The declaration invokes a small event-aware supervisor. This supervisor is Hook infrastructure only; it is not a `scancel` wrapper and is not a user or project command entry.

The supervisor:

- preserves the Hook event input;
- verifies frozen identities needed to trust the external supervisor/Hook/runtime;
- runs the qualified Python Hook in the final sanitized minimal environment;
- enforces an internal deadline shorter than the host Hook timeout;
- captures the child output;
- accepts only valid event-appropriate Hook JSON.

For `PreToolUse` and `PermissionRequest`, interpreter absence, dynamic-loader failure, exit `127`, other nonzero exit, signal, internal timeout, missing/corrupt Hook/runtime, hash mismatch, empty output or malformed/invalid output must become a valid deny response and a successful Hook completion. The underlying Bash call must not start.

If the full checker is unavailable, the current Bash tool call is denied as a whole. The supervisor must not grow a second partial shell parser that guesses whether an arbitrary command is safe.

For `PostToolUse`, infrastructure failure must never create a new Slurm mutation or fall back to shell `scancel`.

### 4. Protected cancellation semantics

The existing v2.1 business logic may be selectively ported, not blindly merged.

For supported exact cancellation:

1. resolve each exact Job with frozen absolute `scontrol`;
2. verify exact Job identity, current owner and cancellable state;
3. reject unsupported selectors, ranges, parent arrays, heterogeneous targets, steps, non-default signals/options or ambiguous command forms;
4. if no target belongs to the private protected-partition set, add no protected-cancel confirmation;
5. if any target is protected, deny the original command with zero mutation and return the canonical native question;
6. only a genuine root interactive `request_user_input` answer `确认取消` is eligible;
7. re-resolve JobId / Partition / Owner / State immediately before mutation;
8. reserve the one-time confirmation identity before any possible `scancel` invocation;
9. invoke frozen absolute `scancel` once;
10. never automatically retry after an ambiguous post-invocation outcome; perform read-only scheduler reconciliation and report the result honestly.

`保留 Job`, empty/timeout/other text, mismatched question/answer, changed target, subagent/headless context, duplicate or replay all produce zero protected mutation.

### 5. Existing routing remains separate

`slurm_routing.py` is not part of the planned change. It may only be touched if implementation proves a direct unavoidable dependency and supplies focused regression evidence. Protected cancellation must not change routing order, resource contracts, persistent capacity, duplicate-race eligibility or scientific workload semantics.

## Consumer scope

Current default-branch searches of `YuukiAS/Distributed_Imaging_Inference` found no active production code path containing direct `scancel`; matches are historical/results text and the installed Skill copy. Current `YuukiAS/CARE` default branch search found no `scancel` matches.

Therefore DII and CARE are **NO CHANGE** in this plan. Execution may only reopen minimal consumer adaptation if current formal source at implementation time proves a real direct protected-cancel execution path. No consumer may copy protected-partition policy or confirmation parsing.

## Capability Gate Matrix

The five approved gates are deliberately distinct.

| Gate | Capability / claim | Normal entry and evidence | Explicit failure | Regression boundary | Final candidate |
|---|---|---|---|---|---|
| G1 | Portable installation and atomic activation | Normal installer discovers a qualified Hook runtime in a sanitized environment, stages the candidate, proves rollback and changes only task-owned config/runtime after qualification | binds installer Python blindly, captures ambient shell state, half-activates, or changes unrelated config | existing user config, Hook trust and unrelated Hook declarations | required |
| G2 | Infrastructure failure fails closed | Real Hook-normal-entry fault injection plus deterministic cases for missing interpreter, loader failure/127, timeout, signal, hash mismatch, corrupt/malformed output; Codex receives valid deny and underlying Bash launch count stays zero | ordinary Hook failure is observed and Bash continues | unrelated non-Slurm behavior once runtime is healthy | required |
| G3 | Protected/unprotected behavior and should-not-change | Fake scheduler covers protected exact target/set, unprotected target, unsupported syntax/selector, retain, timeout, confirmation, changed target/partition/owner/state and replay; full Slurm routing/resource/capacity/race regression remains green | protected mutation without fresh confirmation, duplicate mutation, or existing routing regression | all existing `slurm-workflows 0.4` behavior | required |
| G4 | Longleaf production normal entry | First `scancel --help` proves live Hook deny before a real process starts; then exactly one minimal future-BeginTime CPU `htzhulab` test Job is retained once and later confirmed/cancelled once after re-resolution; no other Job changes | probe starts real scancel, prompt is missing, retain mutates, confirmed flow duplicates, or any unrelated Job changes | ordinary user terminal unaffected; no GPU/H100 use | required |
| G5 | Formal release identity | Released source/generated/version/install identity is exactly the candidate that passed G1-G4; fresh-session `hooks/list` and normal entry consume the formal release | evidence is stitched across different commits or worktree bytes remain active | repository/version/changelog/README/generated parity and install/upgrade behavior | required |

Regression-bank policy: known deterministic protected-cancel failures enter G1-G3 rather than creating new same-meaning gates. Cheap deterministic bank runs before G4. Because this change affects shared user-level Hook runtime and installation behavior, release uses broad repository regression/final release CI rather than a narrow unit-test-only claim.

No paid external model call is part of these gates.

## Release decision

Current formal source is:

- repository: `5.5.0`;
- standalone `slurm-workflows`: `0.4`.

This is a compatible user-visible improvement to an existing standalone Skill, not a new repository-level capability. If the formal release line is unchanged when release closure begins:

```text
Repository bump decision: PATCH
Reason: compatible protected-cancellation runtime/install improvement inside existing Slurm Workflows.
Affected standalone skills:
- slurm-workflows: 0.4 -> 0.5
Affected central Marketplace plugins:
- all: NO_BUMP
```

If `main` or `release` advances before execution/release, the Executor must re-read the canonical version policy and current formal source and calculate the next valid patch release instead of reusing `5.5.1` mechanically.

README must be checked at release time. Any reader-facing README modification requires an actual installed Clear Writing pass under repository rules.

## Maintenance-board state

The canonical TODO entry is already in tracking scope but still says `PENDING_CLEAR_WRITING`; no existing tracking Issue was found for this protected-cancel item.

This ChatGPT surface can write repository files and Issues but does not expose the required GitHub Project mutation surface, and it does not expose an executable Clear Writing mutation path that satisfies the board's requirement for reader-facing Issue copy. Therefore this Planner round does **not** create or rewrite a tracking Issue and does not invent a `tracking: #N` backlink.

Exact pending maintenance mutation for the next Project-capable + Clear-Writing-capable maintenance entry:

- run the installed Clear Writing capability on the proposed Issue title/body;
- create or bind exactly one Issue for this same task with labels:
  - `maintenance-track`
  - `kind:new-capability`
  - `scope:standalone-skill`
  - `area:standalone-skill`
- human title intent: “Slurm 受保护作业取消确认”;
- Project `AI Skills Maintenance`: `Status=DOING`, `Area=standalone-skill`, no Resolution commit yet;
- current execution anchor: Proposal/Execution Plan/Goal/Kickoff v3 for `hpc--slurm-cancel-production-closure`;
- next action: execution-ready Critic review of the v3 package;
- after the real Issue number exists, update only the canonical TODO locator to `tracking: #N` without changing its maturity/status as a locator side effect.

The Project is not claimed synchronized in this round. The user is not required to maintain it manually.

## User decisions frozen by this proposal

The user-visible choices are now settled:

- use one global Hook boundary, not a wrapper;
- protect configured partitions, with Longleaf's protected value private to that machine;
- fresh current-chat confirmation is required for protected cancellation;
- infrastructure failure denies rather than silently cancelling;
- no Direct-mode switch and no Codex patch;
- no DII/CARE change without new source evidence;
- one real Longleaf test Job only after all non-mutating gates pass;
- formal release follows the same final candidate that passed the gates.

No additional product decision is intentionally deferred to Codex.
