---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: hpc--slurm-cancel-production-closure
implementation_commit: a8765b97b69c319304cb51dbd271d57ed8492c34
---

# Codex Result

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

`TEST_JOB_ID=5693449`
`G4=FAIL`
`KEEP_TEST=FAIL`
`CONFIRM_CANCEL_TEST=NOT_RUN`
`EXACT_CANCEL_COUNT=0`
`OTHER_JOB_MUTATION=NO`
`NEXT_ACTION=RETURN_TO_PLANNER`
