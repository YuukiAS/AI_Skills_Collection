# Slurm protected cancel portable runtime — Execution Plan v3

Status: EXECUTION_READY_REVIEW_PENDING  
Date: 2026-10-19

## Authority and scope

This plan implements, without redesign, the independently approved:

`docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md`

Task identity remains:

`hpc--slurm-cancel-production-closure`

No successor task is created.

Current source:

- repository: `YuukiAS/AI_Skills_Collection`
- approved design base: `main@23f51b0bebd8a32f49d899f7fae1ee0e5f17e4cd`
- current repository release: `5.5.0`
- current standalone Skill: `slurm-workflows 0.4`
- failed historical candidate: `work/hpc--slurm-protected-partition-chat-confirmation-v2-1@1b8df2c1f2b93de1605d571f5125cd4aaa99fd20`
- historical candidate relation: diverged, ahead 12 / behind 23

The historical candidate is read-only source material for selective porting and regression recovery. Its `RESULT.md`, installed production configuration, branch state and stale runtime identities are not current authority.

This Planner round does not create the execution branch/worktree, install Hooks, mutate live `CODEX_HOME`, run Slurm, create a Job or publish a release.

## Execution identity after execution-ready PASS

When and only when an independent Critic gives execution-ready PASS and the user sends the resulting Codex handoff, the intended execution identity is:

- canonical Longleaf repo root R: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
- task branch: `reviewed/hpc--slurm-cancel-production-closure`
- task worktree W: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure`
- task key: `hpc--slurm-cancel-production-closure`

Before any branch/worktree mutation, Codex must re-resolve R, origin, clean/ownership state, current `origin/main`, branch absence and worktree-path absence. If R is not the canonical repo, the exact branch/path is already occupied, or current main has semantic drift in the approved surface, stop before mutation and return to Planner/Critic. Do not invent a second clone, alternate branch, `/tmp` fallback or successor task.

The approved package may be rebased only semantically by a new Planner/Critic decision; Codex may not silently rebase the product contract when source drift is material.

## Required maintenance companions

This is a formal production refinement of a standalone AI Skills capability.

- workflow owner: `workflow-core`
- maintenance companion: `ai-skills-core`
- domain owner: standalone `slurm-workflows`

Codex must use the actual installed/enabled maintenance capability as required by repository policy before editing production source. Reading the source `SKILL.md` alone is not invocation proof.

## Frozen implementation semantics

The following are non-substitutable.

### A. One global Hook boundary

Keep one user-level global `PreToolUse` / `PermissionRequest` / `PostToolUse` protected-cancel boundary. Do not replace it with:

- `scancel` wrapper;
- PATH shim/interception;
- project-local Hook copies;
- terminal confirmer;
- next-shell token consumption;
- daemon/broker/database;
- Direct-mode switch;
- model-catalog override;
- OpenAI Codex patch.

### B. `config.toml` inline layer is the fail-closed root

The task-owned trusted declaration in `config.toml` is the last layer that must remain capable of returning a valid deny even when external runtime pieces fail.

The declaration must bind the external supervisor's expected immutable content identity. The supervisor must not read its own expected hash from machine-writable `runtime.json` or another runtime file and thereby self-authorize changed bytes.

The inline layer may remain small, but it must be sufficient to:

- dispatch the event-aware supervisor only at the frozen identity;
- detect failure to invoke/validate that layer;
- emit an event-appropriate valid deny instead of returning an ordinary Hook process error.

### C. Portable runtime qualification

Installation Python and Hook runtime Python are different concepts.

The installer must evaluate candidate interpreters in the final sanitized minimal environment. Qualification must be performed before activation and must include:

- interpreter starts;
- required standard library imports;
- final Hook bytes load;
- final private runtime/policy loads;
- frozen absolute `scontrol` and `scancel` identities are executable;
- synthetic harmless event yields valid Hook JSON;
- no inherited secret or broad interactive-shell/module environment is required.

Candidate order follows Proposal v3. Machine-specific minimal loader variables are allowed only in machine-private runtime data after qualification.

The public Skill must not contain Longleaf-specific paths or protected partitions.

### D. Policy portability

Replace the task-private protected partition policy format with JSON and keep the Hook compatible with Python 3.9+ unless implementation proves an unavoidable standard-library requirement and returns to Planner before broadening the runtime contract.

### E. Failure closure

For `PreToolUse` / `PermissionRequest`, any infrastructure failure after the Hook was selected must produce valid deny and must prevent the underlying Bash process from starting:

- interpreter missing;
- dynamic-loader failure;
- exit `127`;
- other nonzero exit;
- signal;
- internal timeout;
- missing/corrupt Hook/runtime;
- supervisor/Hook hash mismatch;
- empty, malformed or event-incompatible output.

The supervisor's internal timeout must be shorter than the host Hook timeout, so Codex does not become the first layer to observe a raw timeout.

Do not add a partial second shell parser merely to keep unrelated Bash commands running while the full checker is unavailable. If the checker cannot establish policy safely, deny that current Bash tool call and retry from a healthy runtime on the next call.

### F. Post-confirmation mutation semantics

The one-time reservation must be durably created before any possible protected `scancel` invocation.

If `scancel` may have started but the Hook cannot determine the result, mark the reservation as an ambiguous/unknown outcome, do not automatically retry the mutation, and use only read-only scheduler reconciliation to determine current state.

This must remain distinct from a pre-invocation failure, which has zero mutation.

### G. Routing separation

`skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py` is default NO CHANGE. Modify it only if a direct unavoidable dependency is discovered and the same change is supported by focused regression evidence. Such a discovery does not authorize a redesign of routing, race, resource-contract or capacity behavior.

## Planned source changes

Expected central files are bounded to:

- `skills/tools/hpc/slurm-workflows/SKILL.md`
- `skills/tools/hpc/slurm-workflows/scripts/setup_protected_cancel.py` or its current-main equivalent
- `skills/tools/hpc/slurm-workflows/scripts/slurm_cancel_hook.py`
- one small task-owned supervisor asset if the approved implementation cannot keep the supervisor entirely inside generated config without sacrificing reviewability
- focused protected-cancel tests
- generated/registry/release metadata required by the repository's normal standalone-Skill release
- `CHANGELOG.md`
- README only if user-facing version/capability documentation needs changing
- `docs/skill-todos/slurm-workflows.md` only for truthful tracking/release closure

The implementation should selectively port only still-correct business logic and regression cases from the failed historical candidate. Do not cherry-pick its old result/control/production configuration wholesale.

## Development order

### Phase 0 — Source and authority preflight

After user handoff:

1. verify exact R/origin/branch/worktree identities;
2. fetch latest `origin/main`;
3. compare the approved package against current main for semantic drift;
4. read current `AGENTS.md`, Goal, Proposal, this Plan, current Skill, version/release policy, maintenance-board policy and directly affected tests/generators;
5. initialize the approved Reviewed Handoff task using the existing Bridge normal entry, not raw branch/worktree creation, if the current Bridge runtime supports that exact branch/worktree contract;
6. if that formal path is unavailable, stop before topology mutation rather than invent a replacement workflow;
7. invoke required maintenance companion preflight.

No production code edit occurs before Phase 0 is clean.

### Phase 1 — Selective source recovery

Recover only:

- exact Job parsing/resolution;
- protected partition decision;
- canonical native question;
- root-interactive validation;
- one-time reservation;
- exact re-resolution;
- exact one-shot cancellation;
- focused regressions that still match Proposal v3.

Remove assumptions that bind production Hook runtime to installer `sys.executable`, obsolete project-local/global migration remnants, stale production receipts and old branch identities.

### Phase 2 — Portable runtime and supervisor

Implement runtime discovery/qualification, JSON policy, final sanitized environment, trusted supervisor identity and fail-closed event behavior.

Use task-owned fake executables and disposable isolated `CODEX_HOME` fixtures for development.

Do not touch live Longleaf `CODEX_HOME` in this phase.

### Phase 3 — Cheap deterministic regression bank

Run G1-G3 deterministic evidence first. Fix only generic failures under the frozen plan. Do not create a real Slurm Job yet.

When the candidate changes, rerun affected G1-G3 checks before proceeding.

### Phase 4 — Freeze final implementation candidate

Once G1-G3 pass:

- freeze one final candidate commit;
- record exact source and generated identities;
- run full relevant local repository validation;
- explicitly dispatch required full/integration CI on the task branch only after candidate freeze;
- do not use ordinary development pushes as repeated full-CI gates.

If CI changes the product candidate, G1-G3 evidence for the prior candidate no longer supports release.

### Phase 5 — G2 real Codex Hook fault-injection proof

Before any real Slurm Job, perform at least one **real Codex Hook normal-entry** failure injection using the final candidate and an isolated/disposable Hook runtime.

The test must prove:

- Codex selected the real Hook declaration;
- the supervised child was made to fail in a controlled way equivalent to an infrastructure failure;
- Codex received a syntactically valid deny;
- Hook completion was not reported as an ordinary raw process failure;
- the underlying Bash launch count was exactly zero.

Directly invoking the supervisor or Python script is insufficient for this required G2 evidence.

This fault injection must not use live Slurm mutation or an existing real Job.

### Phase 6 — Controlled live installation and harmless probe

Only after G1-G3 and Phase 5 pass, install the exact frozen candidate into the authorized Longleaf `CODEX_HOME`.

Authorization scope for later user handoff is limited to:

- `/users/a/e/aereinh/.codex/config.toml`: task-owned protected-cancel declaration block only;
- `/users/a/e/aereinh/.codex/slurm-protected-cancel/`: task-owned runtime only;
- required backup/restore of those task-owned surfaces;
- no unrelated Hook, permission or user configuration changes.

Activation sequence:

1. back up exact task-owned live state;
2. stage and qualify final machine runtime before changing the active declaration;
3. atomically activate final declaration/runtime;
4. preserve unrelated Hook declarations and existing trusted state;
5. perform at most the necessary final trust action after declaration bytes are frozen;
6. start a genuinely fresh Desktop remote thread if required by Hook reload semantics;
7. run `scancel --help`.

The harmless probe must prove:

- `PreToolUse` started from the user-level declaration;
- Hook completed normally with a valid deny;
- the real `scancel` process did not start.

If the probe fails, restore the previous task-owned state and stop before creating a Slurm Job. Do not switch architecture.

### Phase 7 — G4 single real Longleaf Job

Only after the harmless probe passes, create exactly one test Job:

- partition: `htzhulab`;
- CPU-only;
- minimum practical CPU/memory/walltime;
- harmless payload;
- BeginTime at least four hours in the future;
- unique task-owned name;
- no GPU/H100;
- this exact JobId is the only Slurm Job the task may cancel.

Acceptance uses the same Job twice:

1. verify exact JobId / partition / owner / `PENDING` / BeginTime;
2. normal Codex cancellation request;
3. original `scancel` denied with zero mutation;
4. user selects `保留 Job`;
5. read-only verify it remains pending;
6. request cancellation again;
7. user selects `确认取消`;
8. PostToolUse reserves before mutation and re-resolves exact Job;
9. exact frozen `scancel` executes once;
10. read-only verify terminal cancellation state;
11. verify no other Job was mutated.

No second Job is created to make the gate pass.

### Phase 8 — Independent implementation review

After implementation/runtime evidence is complete, publish the clean task branch through the approved bounded publisher and enter the existing independent Reviewed Handoff review path.

Reviewer must inspect the real final candidate, G1-G4 evidence, final diff and should-not-change evidence. Reviewer PASS on process alone cannot substitute for G4 normal-entry proof.

If Reviewer requires a product change, the candidate changes and affected gates must be rerun. Do not stitch evidence across candidates.

### Phase 9 — Release closure G5

After required Reviewer PASS and any explicit human gate defined by the frozen package:

1. fetch latest main/release and check semantic/integration drift;
2. integrate only if ordinary preflight is clean;
3. re-read `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`;
4. if formal line is still repository `5.5.0` / Skill `0.4`, release repository `5.5.1` and `slurm-workflows 0.5`;
5. otherwise calculate the next valid repository patch and the next one-step standalone-Skill version from current formal source;
6. update source/generated/version/changelog/README surfaces required by actual change;
7. if README changes, run the installed Clear Writing capability on affected reader-facing regions before finalizing;
8. run final exact-candidate release CI;
9. perform formal install/upgrade smoke from the release bytes;
10. in a fresh session verify `hooks/list` and harmless normal-entry consumption use the released bytes, not the worktree;
11. only then advance formal release identity through the repository's normal non-force release path.

G5 fails if any release-critical evidence came from a different product candidate.

## Capability Gate Matrix

This plan implements exactly the five gates approved by Proposal v3 and does not add a sixth gate.

### G1 — Portable installation and atomic activation

Evidence:
- sanitized runtime discovery;
- candidate qualification;
- staging before activation;
- task-owned config diff only;
- old working state remains recoverable;
- failed candidate leaves formal config unchanged.

Failure:
- blind `sys.executable` binding;
- ambient environment capture;
- half-active install;
- unrelated config/trust mutation.

### G2 — Infrastructure failure fails closed

Evidence:
- deterministic missing interpreter, loader failure/127, nonzero, signal, timeout, missing/corrupt identity and malformed output;
- at least one real Codex Hook normal-entry fault injection;
- valid deny;
- underlying Bash launch count = 0.

Failure:
- raw Hook failure lets Bash proceed.

### G3 — Protected/unprotected and should-not-change

Evidence:
- fake Slurm protected/unprotected/unsupported/changed/replay cases;
- retain and confirmation semantics;
- one-shot mutation;
- full existing routing/resource-contract/persistent-capacity/race regressions;
- unrelated Bash behavior healthy when the Hook runtime is healthy.

Failure:
- semantic weakening or unrelated Slurm regression.

### G4 — Longleaf production normal entry

Evidence:
- final-candidate live `scancel --help` deny-before-process;
- exactly one future CPU-only `htzhulab` Job;
- same Job retained once and confirmed/cancelled once;
- exact mutation count one;
- zero unrelated Job mutation.

Failure:
- any real command starts before required deny, missing prompt, retain mutates, duplicate cancellation or other Job mutation.

### G5 — Formal release identity

Evidence:
- same candidate identity across released source/generated bytes, installed Hook/supervisor/runtime, release CI and fresh-session normal entry.

Failure:
- evidence stitching or worktree-only runtime.

## Consumer decision

DII = NO CHANGE.  
CARE = NO CHANGE.

The Planner checked current default-branch source searches. No active production direct `scancel` path was found. Execution may reopen this decision only if current formal source changes and provides direct evidence of a protected-cancel bypass. Such adaptation must remain minimal and may not copy central policy or confirmation logic.

## Version plan

If formal versions remain unchanged at closure:

```text
Repository bump decision: PATCH
Reason: compatible user-visible protected-cancel improvement to an existing standalone Skill.
Affected standalone skills:
- slurm-workflows: 0.4 -> 0.5
Affected central plugins:
- all: NO_BUMP
```

Version numbers are recalculated from current formal source immediately before release.

## Maintenance-board pending mutation

No tracking Issue/Project mutation is performed in this Planner round because the required reader-facing Clear Writing mutation path and GitHub Project mutation surface are not both available.

The next Project-capable + Clear-Writing-capable maintenance entry must, before implementation closure bookkeeping:

1. run installed Clear Writing on the Issue title/body;
2. create/bind one Issue for this task;
3. apply `maintenance-track`, `kind:new-capability`, `scope:standalone-skill`, `area:standalone-skill`;
4. set Project `Status=DOING`, `Area=standalone-skill`, Resolution commit empty;
5. set current anchor to this v3 execution package and next action to its execution-ready Critic review;
6. write the resulting `tracking: #N` back to the canonical `docs/skill-todos/slurm-workflows.md` entry without changing its maturity as a locator-only side effect.

Until that occurs, Project sync remains pending and must not be claimed complete. The user is not asked to perform this manually.

## Stop conditions

Stop without changing architecture if:

- the config-root/supervisor design cannot produce a valid deny with Python completely unavailable;
- Codex rejects the event-specific deny response;
- task-owned `config.toml` mutation cannot be made atomically without damaging unrelated config;
- final harmless `scancel --help` still launches the real process;
- semantic drift in latest main invalidates the approved v3 contract;
- the single authorized real Job cannot be created within the frozen low-impact contract.

Do not respond by adding wrapper/shim, Direct mode, Codex patch, daemon/database, alternate task or extra real Jobs.

## Positive completion

The task is complete only when the exact final release candidate:

- installs portably without assuming the installer Python is the production Hook Python;
- fails closed through the real Codex Hook entry when its child runtime fails;
- preserves existing Slurm Workflows behavior;
- passes the one-Job Longleaf retain/confirm acceptance;
- receives the required independent implementation review;
- is released and formally installed with source/generated/runtime identity aligned.

Tests or CI alone cannot establish this completion.
