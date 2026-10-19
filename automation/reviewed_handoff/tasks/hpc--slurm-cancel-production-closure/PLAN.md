---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: hpc--slurm-cancel-production-closure
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

Implement and formally release the independently approved protected-cancel portable runtime v3 package at `e84be726d6a7aaefe62d27c7fd2a0410e7f1498b` for the existing standalone `slurm-workflows` Skill.

The user-visible outcome is that an exact Codex `scancel` targeting a configured protected partition cannot mutate Slurm until the current root interactive chat receives fresh confirmation for that exact Job. Hook-runtime failure must deny rather than silently allow the underlying Bash command.

This task-local Plan is a mechanical Reviewed Handoff mapping of these frozen authorities and does not redesign them:

- `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md`
- `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_PLAN_V3_2026-10-19.md`
- `docs/goals/hpc--slurm-cancel-production-closure-goal-v3.md`
- `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_KICKOFF_DRAFT_V3_2026-10-19.md`

## Frozen decisions

- Workflow owner: `workflow-core`.
- Maintenance companion: `ai-skills-core`.
- Domain owner: standalone `slurm-workflows`.
- Keep one user-level global `PreToolUse` / `PermissionRequest` / `PostToolUse` Hook boundary.
- The trusted protected-cancel declaration block in `config.toml` is the fail-closed root and binds the expected external supervisor identity.
- The supervisor is Hook infrastructure, not a `scancel` wrapper or alternate user command.
- Discover and qualify the production Hook interpreter independently from the installer interpreter in the final sanitized minimal environment.
- Keep protected partitions, machine paths, loader variables, executable identities and secrets out of public source; private policy uses JSON and the Hook targets Python 3.9+.
- For `PreToolUse` and `PermissionRequest`, missing interpreter, loader failure/127, nonzero exit, signal, timeout, corruption, identity mismatch, empty output or invalid output must become a valid deny with underlying Bash launch count zero.
- `PostToolUse` reserves the one-time identity before any possible `scancel`; an ambiguous post-invocation outcome is never automatically retried and is reconciled read-only.
- `slurm_routing.py` is NO CHANGE unless a direct unavoidable dependency is proven with focused regression evidence.
- DII and CARE are NO CHANGE unless current formal source proves a live direct protected-cancel bypass.
- Use exactly gates G1-G5; do not add a sixth gate.
- Repository bump decision: PATCH. Reason: compatible user-visible protected-cancel improvement inside the existing standalone Slurm Workflows capability.
- Affected standalone Skill: `slurm-workflows` `0.4 -> 0.5` if the formal line is unchanged at release; otherwise calculate the next single compatible step from current formal source.
- Affected central Marketplace plugins: all `NO_BUMP`.

## Positive completion

The same final candidate must prove all of the following:

1. portable installation and atomic activation without blindly binding installer `sys.executable`;
2. deterministic fail-closed infrastructure behavior plus one real Codex Hook normal-entry fault injection yielding valid deny and Bash launch count zero;
3. protected/unprotected behavior, retain/confirm/replay/race safety and full existing Slurm should-not-change regression;
4. Longleaf production normal entry: harmless `scancel --help` deny-before-process followed by exactly one held, future-dated, pending `htzhulab` Job that requests only the site-required minimum `gres/gpu=1`; the same exact Job is retained once and then confirmed/cancelled once before it can become eligible to run, with no allocated node and no other Job mutation;
5. independent implementation review and formal release/install identity aligned to the same candidate.

The maximum claim is enforcement through supported normal Codex execution entries plus explicitly adapted consumers. It does not claim same-UID operating-system isolation and does not restrict the user's ordinary SSH terminal.

Tests, CI, Hook trust, file presence, helper success, fake Slurm, or historical evidence alone cannot establish completion.

## Non-substitutable semantics

- The execution entry remains ordinary Codex `scancel -> global Hook -> native current-chat confirmation -> PostToolUse re-resolution -> exact scancel once`.
- Do not replace the Hook boundary with a wrapper, PATH shim/interception, project-local Hook, terminal confirmer, persisted next-shell token, daemon, broker, database, Direct mode/model override or OpenAI Codex patch.
- A protected first attempt performs zero Slurm mutation and presents the exact native choices `确认取消` / `保留 Job`.
- Only fresh `确认取消` from the current root interactive turn for the exact re-resolved target may permit one mutation.
- `保留 Job`, timeout, empty/other answer, changed target/partition/owner/state, mismatch, replay, duplicate or headless/subagent context produces zero protected mutation.
- G4 cannot be replaced by fake Slurm or CI, and no second real Job may be created to chase a PASS.
- Evidence from different product candidates may not be stitched together.

## Implementation scope

Selective source recovery is limited to still-correct exact Job parsing/resolution, protected partition decision, native question, root-interactive validation, one-time reservation, re-resolution, one-shot cancellation and matching regressions from the rejected historical candidate.

Expected source surfaces are bounded to:

- `skills/tools/hpc/slurm-workflows/SKILL.md`;
- `skills/tools/hpc/slurm-workflows/scripts/setup_protected_cancel.py` or the current-main equivalent;
- `skills/tools/hpc/slurm-workflows/scripts/slurm_cancel_hook.py`;
- at most one small task-owned event-aware supervisor asset;
- focused protected-cancel tests;
- generated/registry/version/changelog/release metadata required for the normal standalone-Skill release;
- `CHANGELOG.md` and the standalone Skill changelog/TODO closure;
- README only if actual user-facing release documentation requires it.

Development order is frozen:

1. selectively recover valid business logic and regressions;
2. implement portable runtime qualification, JSON policy, sanitized environment, trusted supervisor identity and fail-closed event behavior using fake executables and disposable `CODEX_HOME` fixtures;
3. pass deterministic G1-G3 before any live install or real Job;
4. freeze one candidate and run relevant full local validation and required final-candidate CI;
5. prove real Codex Hook normal-entry fault injection before any real Job;
6. only then back up and atomically install within the authorized protected-cancel live surfaces and run harmless `scancel --help`;
7. only after the harmless probe passes create exactly one authorized test Job for G4;
8. obtain independent implementation review;
9. perform G5 release and formal install/upgrade identity closure.

## Acceptance and regression gates

### G1 — Portable installation and atomic activation

Require sanitized runtime discovery, final-environment qualification, staging before activation, exact task-owned config diff, recoverability, and no partial activation. Reject blind `sys.executable` binding, ambient environment capture, unrelated config/trust mutation or half-active state.

### G2 — Infrastructure failure fails closed

Cover missing interpreter, loader failure/127, other nonzero exit, signal, internal timeout shorter than host timeout, missing/corrupt identities and malformed/event-incompatible output. At least one real Codex Hook normal-entry injection must show Hook selected, valid deny, normal Hook completion and underlying Bash launch count exactly zero.

### G3 — Protected/unprotected behavior and should-not-change

Fake scheduler coverage must include protected/unprotected exact targets and sets, unsupported selectors/forms, retain, timeout, confirmation, changed target/partition/owner/state, replay and exactly-once mutation. Run full existing routing, resource-contract, persistent-capacity and race regressions plus unrelated healthy Bash behavior.

### G4 — Longleaf production normal entry

The final candidate must deny harmless `scancel --help` before the real process starts. Then, under the independently approved `SLURM_PROTECTED_CANCEL_G4_RESOURCE_AMENDMENT_V3_1_2026-10-20.md`, create exactly one minimal pending `htzhulab` Job using one currently authorized QoS discovered read-only, the site-required minimum `gres/gpu=1`, one CPU, minimum legal memory, `--hold`, a BeginTime at least 24 hours ahead, and a harmless payload. Do not release it and do not request an explicit H100 unless the site rejects generic one-GPU GRES and an exact type is strictly required to satisfy the same minimum policy. Immediately after submission, continue only if read-only inspection proves exactly one JobId, current owner, `partition=htzhulab`, `state=PENDING`, no allocated node, and hold/future protection; otherwise stop and create no replacement Job. Use that same exact Job for the retain interaction, verify it remains pending, then use the confirm interaction, re-resolve and cancel it exactly once, verify terminal cancellation and zero unrelated Job mutation.

### G5 — Formal release identity

Released source/generated/version bytes, installed Hook/supervisor/runtime, final CI, fresh-session `hooks/list` and harmless normal-entry behavior must all identify the same candidate. Worktree-only or cross-candidate evidence fails.

Development-local tests precede final GitHub integration/release CI; full CI is a final-candidate phase gate, not a per-commit loop. Reviewer must inspect the final candidate, G1-G4 evidence, final diff and should-not-change results. Process PASS cannot substitute for G4 product/runtime evidence.

## Natural-language usage / routing expectations

- A user asks Codex to cancel an exact unprotected Slurm Job: normal Codex execution continues without a protected-cancel confirmation.
- A user asks Codex to cancel an exact Job currently in a configured protected partition: the first command is denied with zero mutation and the current root chat asks `确认取消` / `保留 Job`.
- Selecting `保留 Job` leaves the exact Job unchanged.
- Selecting `确认取消` causes immediate identity/state re-resolution and at most one exact cancellation.
- Headless or broken Hook-runtime paths fail closed instead of cancelling.

## Out of scope

- Redesigning Slurm routing, resource contracts, persistent capacity or duplicate-race behavior.
- Wrapper/shim/PATH interception, Direct mode, model-catalog changes, Codex patches, daemon/broker/database or a successor task.
- Public Longleaf paths, `htzhulab`, loader paths, accounts, secrets or machine policy.
- DII/CARE changes without new direct source evidence.
- More than one real Slurm test Job, any release or execution of the G4 test Job, GPU computation, explicit H100 request except the amendment's strict site-required fallback, or mutation of any pre-existing Job.
- New gates, generalized OS-level enforcement, unrelated Hook/config/trust changes, or unrelated repository cleanup.
