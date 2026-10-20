---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: hpc--slurm-cancel-production-closure
implementation_commit: ac6a380c00b416ef7a5c4c46591fd0cfe9b6770a
---

# Codex Result

## Current MCP implementation checkpoint (supersedes earlier execution surface)

Latest direct user authority replaces request-user-input cancellation transport with the existing fail-closed command guard plus one trusted PreToolUse MCP-tool handler and a local official-SDK stdio server. The user explicitly authorizes installation and native trust of only that new handler. PLAN revision remains 1; no Planner/Critic/successor or second Job was created.

`FINAL_CANDIDATE_PRE_TRUST=ac6a380c00b416ef7a5c4c46591fd0cfe9b6770a`.

Current stop: native trust of the exact new handler passed, but the current-chat harmless vertical probe returned actual Bash stdout without a form or installed MCP audit entry, despite successful supported config reload and a connected MCP server. `MCP_VERTICAL_EVIDENCE.md` records direct observations and their limits. Per the user's explicit stop condition, no alternate architecture or further real-Job step was attempted. The installed trusted candidate is retained, not rolled back. `KEEP_TEST=NOT_RUN`, `CONFIRM_CANCEL_TEST=NOT_RUN`, `EXACT_CANCEL_COUNT=0`, `COMPLETE=NO`.

- Original command guard source, supervisor, runtime, policy, declarations and trust hashes remain identical. The production route removes only this product's old PostToolUse answer binder, preserving unrelated config and all trust state.
- Official MCP SDK 1.30.0 is in a durable machine-local environment, not `/tmp`. Real SDK stdio/fake-Slurm elicitation transport smoke passed; this is NOT a Desktop card PASS.
- Focused original/new regression passed; latest new MCP regression is 14 tests PASS, covering strict two-option enum, retain/close/malformed zero mutation, ownership/thread binding, reservation ordering, drift/replay, unprotected behavior, runtime/policy digests, and rejection of altered guard top-level code before any side effect.
- Independent source review of exact `ac6a380c00b416ef7a5c4c46591fd0cfe9b6770a`: PASS, after repairing findings in earlier pre-trust candidates. This is a source review, not a G4 or release PASS.
- Prior all-Slurm run: 57 PASS before the last two added identity regressions. Skill validation/audit and Marketplace validation/freshness passed. An initial full suite ran 389 tests with three unrelated missing-python-pptx environment failures; dependency corrected in the task-owned environment. Final candidate full suite/CI remain pending, not relabeled from old results.
- Job 5693449 was rechecked PENDING/JobHeldUser, current owner, htzhulab, unallocated, never released. Exact real cancellation count remains zero; no other Job mutation.

Real current-chat MCP card, native trust, final-candidate full tests/CI, retain/confirm, G5 and formal release remain required. The installation receipt and SDK smoke are under durable `private/exports/hpc--slurm-cancel-production-closure/`. No historical candidate's UI/G4 evidence is counted for this MCP candidate. README checked: no update required.

## Implemented

Implemented the approved portable protected-cancel candidate, then the user's explicitly authorized minimal fresh-session boundary clarification. The installer reports `fresh_session_required=true`; the Skill requires actual fresh-thread Hook consumption evidence. The clarification does not change rendered enforcement bytes.

The same-backend A/B experiment confirmed `STALE_SESSION_HOOK_SNAPSHOT`. The original Desktop session continued consuming its old declaration; a new session consumed the final user-level Hook and blocked harmless `scancel --help` before command launch. Details, source references and exact thread/turn/call identities are in `SESSION_AB_EVIDENCE.md`.

## Verification

- Final source candidate: `a8765b97b69c319304cb51dbd271d57ed8492c34`, published through the normal bounded Bridge helper.
- 39 focused/existing Slurm tests passed, including CLI fresh-session output and unchanged enforcement-identity regression.
- Original G2 real CLI runtime-failure injection and CI are recorded in `EXECUTION_EVIDENCE.md`; original CI is not relabeled as CI for the new commit.
- Hook/supervisor/runtime/policy installed hashes match the original candidate exactly. Declaration trust was completed by the user through the normal flow; no bypass or trust rewrite was used.
- Final-candidate fresh Desktop harmless probe: native PreToolUse started/completed, status `blocked`, valid unsupported-option deny, command-start count zero.
- `slurm_routing.py`, DII, CARE, Bridge Kit, permission settings and unrelated configuration were unchanged.
- The task-specific Bridge transition plan reports `valid=true` in `NEEDS_GPT_PLANNER`. Repository-wide validation reports unrelated historical task-name/Plan/RESULT issues; it reported no error for this task, and those unrelated tasks were not modified.

PROCESS PASS is limited to the checks above. Full PRODUCT / ARTIFACT PASS is not achieved: retain/confirm acceptance, independent implementation review, G5, and release are incomplete.

## Deviations / blockers

The single authorized CPU-only/no-GPU `htzhulab` submission attempt returned `QOSMinGRES` and no JobId. Read-only policy evidence proves that both allowed partition QoS values require `MinTRES=gres/gpu=1`. Exact-name scheduler lookup returned no Job. No retry, GPU allocation, alternate partition, cancellation, or other Job mutation occurred.

This was the original plan's explicit resource stop condition. The user subsequently approved resource amendment v3.1 and Planner froze revision 1. That resource blocker is resolved; its historical evidence is retained, not rewritten.

## Plan revision 1 continuation

Planner commits `c11dc034001512dc8660648f9709ad9948103273` and `00bead37571634e6af5ad5eba85a261cece60a3c` were fast-forwarded on the same task branch. The candidate is unchanged. Read-only resource qualification, including one successful official `sbatch --test-only` that created no Job, preceded exactly one actual held/future submission. Test Job **5693449** is owned by the current user in `htzhulab`, requests one GPU and CPU, memory `1M`, time one minute, remains `PENDING / JobHeldUser`, has no allocated node, and has EligibleTime 25 hours after submission.

The fresh Desktop thread's first ordinary `scancel 5693449` was blocked by native PreToolUse with zero command launch and zero mutation. Execution then stopped before presenting the required native question: the Hook requires an exact six-key question with `isOther=false` and `isSecret=false`, whereas the exposed native schema permits only four keys; exact 0.160.1 source also normalizes `is_other=true`. No question was called, no user answer was fabricated, no unsupported field-dropping adaptation was attempted, and no second cancellation request was issued. The retain acceptance therefore failed before a real answer; confirmation was not run.

Full direct evidence and source locators: `AMENDED_G4_EVIDENCE.md`. This is the user's substantial-product-change stop condition, not a recurrence of the resolved snapshot or GPU fixture issue. No product change, new plan revision, replacement Job, Hook reinstall/trust, or alternate architecture was attempted. Job 5693449 remains safely held pending explicit recovery direction. Independent review, G5 and formal release remain incomplete.

Repository bump decision: NONE at this incomplete checkpoint.
Reason: no formal release is authorized before G4, independent review and G5.
Affected standalone Skill: `slurm-workflows`: NO_BUMP yet; approved release bump remains pending.
Affected central Marketplace plugins: all NO_BUMP.

## Executor implementation repair (same Plan revision)

Planner recovery commit `70fb0e5612834a99c7675af76a24aa7587267a05` classified the native question incompatibility as an ordinary implementation bug and restored `PLAN_FROZEN`, revision 1. No Plan edit, additional revision, successor, architecture investigation or second Job is part of this repair.

New implementation candidate: `57837a90125fafa4faf4368f55cb9a3c42bb1cd9`.

- Model-facing questions contain exactly `id/header/question/options`.
- Parsing accepts either that canonical shape or exactly six keys with strict `isOther=true/isSecret=false`; altered values, extra fields and altered semantic contents fail closed.
- Exact retain answers return explicit `retained`, `mutation_count=0`, with no cancellation reservation; free text, Other, empty or malformed answers never authorize cancellation.
- Supervisor validation accepts only zero-mutation retained results.
- Confirmation preserves one-shot reservation and performs a final exact scheduler re-resolution after the durable reservation, before the single scancel; drift consumes the identity without mutation.
- Focused protected-cancel regression: 30 tests PASS. Full Slurm regression: 45 tests PASS. Full repository suite: 377 tests PASS under the permitted writable exact-worktree context. Skill validation/audit and Marketplace validation/freshness PASS. Initial attempts with the old Python or read-only W are not reported as product passes; no unrelated source was changed to address those environment constraints.
- Existing Job 5693449 was read-only verified PENDING/JobHeldUser, Priority 0, unallocated and future-dated before repair. No Slurm mutation occurred during implementation/testing.

The exact candidate was installed atomically at epoch nanoseconds `1792429481505610261`, with backup `/users/a/e/aereinh/.codex/slurm-protected-cancel/backups/pre-v3-20261019T170441Z`. Bytes outside the protected-cancel declaration block were verified unchanged (SHA256 `80c640afd58434ebd4584ba460ee746d1f2b23fbdc1b8ebda7d3e928a0676006`). Installed source hashes match the frozen commit. Hook/supervisor/runtime hashes changed as expected; no trust state was rewritten by Executor.

The old execution session now correctly fails closed against the changed external runtime identity. No shell command is retried through an alternate executor. New trust and a genuinely fresh execution thread are required before further shell verification or Job interactions. The candidate source commit exists locally; publishing it and committing the updated control/evidence files remain pending that normal-entry boundary.

New-candidate trust, fresh-thread harmless/retain/confirm evidence, final CI, independent review, G5 and release remain separate required acceptance steps. Earlier candidate runtime PASS is not relabeled as new-candidate PASS.

The user subsequently completed native trust. A genuinely new root Desktop thread on the same backend and USERS CODEX_HOME then proved this new candidate's ordinary `scancel --help` deny: native PreToolUse started/completed as blocked, dispatcher deny, no underlying command launch. See `NATIVE_SCHEMA_REPAIR_EVIDENCE.md` for exact thread/turn/call identities. Retain/confirm still require actual user selections and are not counted as passed.

`TEST_JOB_ID=5693449`
`QUESTION_SCHEMA_FIX=PASS`
`G4_HARMLESS_PROBE=PASS`
`KEEP_TEST=NOT_RUN_FOR_NEW_CANDIDATE`
`CONFIRM_CANCEL_TEST=NOT_RUN`
`EXACT_CANCEL_COUNT=0`
`OTHER_JOB_MUTATION=NO`
`NEXT_ACTION=CONTINUE_AFTER_NATIVE_TRUST_IN_FRESH_SESSION`
