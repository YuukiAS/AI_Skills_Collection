# Native question compatibility repair

Task: `hpc--slurm-cancel-production-closure`.
Planner recovery: `70fb0e5612834a99c7675af76a24aa7587267a05`.
Plan revision remains 1; PLAN.md and revision limits are unchanged.
New implementation candidate: `57837a90125fafa4faf4368f55cb9a3c42bb1cd9`.

## Bounded source repair

Only the Hook, the existing installer's supervisor output validator, and focused tests changed. The model receives the legal four-field question. Strict parsing also accepts the six-field platform-normalized form with exactly `isOther=true`, `isSecret=false`. Any other key/value or changed semantic content fails closed. Retain returns explicit zero mutation before reservation; Other/free text/empty/malformed answers never authorize cancellation. A final scheduler re-resolution follows the durable one-shot reservation before the exact scancel invocation; post-reservation drift consumes the identity without mutation.

`slurm_routing.py`, DII, CARE, Bridge Kit, PLAN and production architecture are unchanged. No second Job was created. Existing Job 5693449 was checked read-only before repair: current owner, htzhulab, PENDING/JobHeldUser, Priority 0, no node or AllocTRES, future EligibleTime, RunTime zero.

## Candidate-bound local verification

- Focused protected-cancel: 30 tests PASS.
- All Slurm: 45 tests PASS.
- Full repository: 377 tests in 173.590 seconds, PASS.
- Skill validation: 155 active skills, 18 profiles, PASS.
- Skill audit: PASS.
- Marketplace validation/freshness: 10 plugins, 29 active skills, 72 source snapshots, PASS.
- Generated palette/probe artifacts were unchanged after full tests.

Initial test attempts with the old `/usr/bin/python3` or a read-only W were corrected by using the existing Python 3.12 runtime and the authorized writable exact-worktree context. Those failed environmental attempts are not counted as product PASS and did not cause unrelated source repairs.

## Atomic live installation and genuine human boundary

The existing installer qualified and atomically installed the exact candidate, completed at epoch nanoseconds `1792429481505610261`. Recoverable backup:
`/users/a/e/aereinh/.codex/slurm-protected-cancel/backups/pre-v3-20261019T170441Z`.

Bytes outside the protected-cancel declaration block were checked identical, SHA256 `80c640afd58434ebd4584ba460ee746d1f2b23fbdc1b8ebda7d3e928a0676006`. The existing rule file was identity-checked, not modified. All rendered runtime hashes matched installed bytes. Durable private receipt:
`/overflow/htzhu/mingcheng_new/AI_Skills_Collection/private/exports/hpc--slurm-cancel-production-closure/native-schema-repair-57837a90/install-receipt.json`.

The existing Desktop backend at the same socket reported all three declarations `modified`, with no load errors/warnings:

- PreToolUse: `sha256:9d5c93aa86d25fafdd7f3790791e1a602b0324b72829439710d7fab10a56d759`.
- PermissionRequest: `sha256:d6a768d0d0846251ded6de19280c77c75623a06677c02b25b1132786fd0a83fc`.
- PostToolUse: `sha256:79496cda88d8ba0b82c8376d19d1dee6dfa8c3817f31e9365c42b3052e75e518`.

This catalog read establishes only the normal trust requirement, not session execution proof. No trust API, hash rewrite, ignore-config option or bypass was used. The old session subsequently denied an unrelated read command with `hook_runtime_failure` because it still binds the previous external supervisor identity. No shell was retried through an alternate executor. Publication of the local source commit and the updated task control/evidence remains pending normal trust/fresh-session continuation; this is not a claimed completed handoff or release.

Runtime working evidence remains at `/tmp/hpc-native-schema-repair.6aV7ISvY/` (`full-suite.log`, validation logs, installer receipt/helper, observer script/log). Keep these files until raw logs are copied to durable private evidence through the fresh trusted execution entry. Observer session 58574 is connected only to the existing backend and has not started a new thread yet; it can issue the official thread/start request after trust. No new session should be created before trust completion.

## Resume point

Normal native user trust is required once for the changed three declarations. Then create a genuinely fresh Desktop root thread on the same backend and CODEX_HOME; do not reuse any old execution session. Refresh task state/source identity, publish the exact task branch through the bounded Bridge helper, and preserve the exact new candidate binding. Prove the new candidate's harmless ordinary scancel --help deny with no process launch. Recheck existing Job 5693449 read-only and complete actual native retain/confirm choices, never answering for the user. Continue final candidate CI, independent review, G5 and formal release. No additional plan revision, Planner re-entry, replacement Job or architecture change is authorized or needed.

## Post-trust fresh-session continuation

The user completed normal native trust. An official hooks/list request to the same already-running Desktop backend then reported all three exact new declaration identities trusted, enabled, with no warnings/errors. Only afterward, the backend created fresh root thread `01a156d0-bab6-71b3-ab73-aaffd8cb33aa` (createdAt `1792457882`, model `gpt-6.1-sol`, source `vscode`, originator `Codex Desktop`, no parentThreadId, same W and USERS CODEX_HOME). No existing session was reused for shell execution.

New-candidate harmless probe:

- Turn: `01a156d1-36aa-76c1-8897-237314c7ab6d`.
- Exact normal command: `scancel --help`.
- Nested call: `exec-d96f9526-0da5-47d0-910a-154c34791a8e`.
- Native hook/started and hook/completed were captured; user config source, completion `blocked`, feedback `SLURM_CANCEL_DENIED reason=unsupported_scancel_target_or_option`.
- Dispatcher returned `Command blocked by PreToolUse hook`; no matching commandExecution start or real scancel process occurred.

`G4_HARMLESS_PROBE=PASS` for candidate `57837a90125fafa4faf4368f55cb9a3c42bb1cd9`. Retain/confirm remain NOT_RUN for this candidate; exact real cancellation count remains zero. No other Job mutation occurred. Earlier candidate PASS is not relabeled as new-candidate evidence.
