# 056 Final Integration / Release — Critic Review Package v0.2

Review stage: `FINAL_INTEGRATION_AND_RELEASE_EXECUTION_READY_PACKAGE_V0_2`

## Review object

Plan:
`docs/design/056_FINAL_INTEGRATION_RELEASE_PLAN_V0_2_2026-09-22.md`

Goal:
`docs/goals/056_FINAL_INTEGRATION_RELEASE_CLOSURE_GOAL_V0_2.md`

Kickoff:
`docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md`


## C056-F1-APPROVED-KICKOFF-SELF-BLOCKS — v0.2 closure

Planner disposition: **ACCEPT**.

No integration/release mechanism changed. v0.2 changes only the execution-authorization presentation that the Executor will actually consume.

The exact user-sent object after Critic PASS is the complete contents of:

`docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md`

Its authorization header now begins with:

```text
# 056 Final Integration / Release Kickoff v0.2

Status: READY_FOR_USER_AUTHORIZATION

Critic PASS approves this execution package but does not execute it. The user sends this exact Kickoff only after that PASS.

If this exact Kickoff is present as the current user message, that current message itself is the current-user-visible bounded authorization for every effect explicitly listed below.
```

The canonical Kickoff file contains no `DRAFT_NOT_AUTHORIZED` marker and does not require the Executor to locate a repo-local Critic PASS artifact.

The Canonical Goal uses `Status: READY_FOR_USER_AUTHORIZATION` and separately states that the Goal itself is not authorization; the user's exact Kickoff message is.

Executor consumer rule:
- current exact Kickoff message = authorization for the enumerated frozen effects;
- Plan/Goal/Review historical metadata cannot override that current-user authorization;
- same frozen effect does not re-prompt later;
- new target/scope/destructive/provider/account/credential/cost effect still requires a fresh gate.

No new PASS receipt, schema, database, state machine, ledger, watcher, Gate or production rule is introduced.

Critic should first verify this exact self-block closure, then only inspect whether the wording accidentally expands the already-approved v0.1 authorization boundary.

## Facts the Planner verified

AI:
- current planning main `7a6d247e...`;
- reviewed final evidence `b6f67586...`;
- approved production candidate `33c30bbe...`;
- main/reviewed diverged from `9f1c0d32...`;
- exact main/reviewed changed-file overlap is only `docs/plugin-todos/workflow-core.md`;
- no current-main production/version/release-slot overlap;
- production candidate -> final evidence HEAD changes only task evidence plus its focused evidence test.

Bridge:
- current main `9d2da9f...`;
- candidate `96a8ea1b...`;
- main is direct ancestor, ahead-by-candidate=3, behind=0;
- no integration conflict.

Final real-user review state supplied by the independent Critic:
- G1 PASS;
- G2-G8 PASS;
- Source Discovery PASS;
- real-user HUMAN_ONLY exact-once resume PASS;
- Plan-mode non-regression PASS;
- agent-resolvable no-false-prompt PASS;
- Host restore PASS;
- source defect NO.

## Main questions for Critic

1. Is the AI merge strategy minimal and safe?
   - preserve both histories with merge commit;
   - only one audited TODO conflict;
   - all current-main newer TODOs preserved;
   - no production source conflict resolution.

2. Is Gate reuse valid?
   - integrated production tree must be byte-equivalent to approved candidate;
   - if equivalent, only mechanical parity/normal-main identity checks run;
   - any semantic conflict returns Planner/Critic for affected minimal replay.

3. Is the Bridge fast-forward + docs-only release commit sufficient?
   - no main drift;
   - no reason to rerun 372 tests/live G1 after byte-equivalent candidate integration.

4. Is “formal release” correctly scoped?
   - both repos currently have no GitHub Release objects;
   - repo contracts already record releases through integrated main/version/changelog/README/generated identity;
   - package intentionally does not invent a first tag/GitHub Release/package-publish mechanism.

5. Does the final Kickoff provide adequate current-user-visible authorization for:
   - exact main pushes;
   - exact normal Bridge upgrade;
   - permanent exact CODEX_HOME Host install;
   - exact two reviewed-branch deletions only after closure?

6. Is the permanent Host behavior correct?
   - pre-release candidate already passed final real-user G1;
   - after integrated normal 0.8.5, run permanent host install/validate;
   - successful final Host state remains installed;
   - do not repeat live G1 when bytes are equivalent.

7. Are release metadata closures sufficient?
   - AI CHANGELOG stale “Host pending” text must be corrected;
   - Bridge README candidate wording must be formalized;
   - README/version/changelog/generated parity explicit;
   - final closure RESULT/evidence after permanent Host PASS.

## Do not reopen

Without new direct evidence do not reopen architecture, G1-G8 design, least-privilege, version choices, C056-E1/E2/E3/I1, Terra decision or deferred follow-ups.

## PASS meaning

PASS only approves this final integration/release execution package. It does not execute merge/install/branch deletion. User sending the approved Kickoff creates the bounded authorization.

If PASS, output the exact Kickoff verbatim and `NEXT_HANDOFF=CODEX`.

If REVISE, use stable blockers only for direct integration/release/authorization risk and automatically generate the full Planner prompt.
