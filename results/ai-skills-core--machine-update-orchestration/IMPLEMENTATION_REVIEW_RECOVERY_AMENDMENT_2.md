# Implementation Review Recovery Amendment 2

Task: `ai-skills-core--machine-update-orchestration`  
Stage: `INDEPENDENT_IMPLEMENTATION_REVIEW_REVISE_2`  
Date: 2026-09-24  
Reviewed remote task tip: `f0cb3e41ced59ec247b30f3076edb0d42aeda629`  
Reviewer result relayed by user: `REVISE`

This is the same implementation-review recovery. It does not create a successor task and does not reopen the Critic-PASSed V2.1 architecture.

## Current Finding Disposition

- `IR-B001`: `CLOSED`
- `IR-B002`: `STILL_OPEN`
- `IR-B003`: `STILL_OPEN`
- `IR-B004`: `NEW_FROM_LATEST_MAIN_DRIFT`

## Source State Rechecked

The repair must start by rereading latest AI_Skills `main`, the exact reviewed task branch, and the mandatory Planner/Critic/Gate/version contracts:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

User-verified drift baseline:

- AI_Skills `main`: `67e0bd4a09bcc120dd397cb55c78592f4ab34a73`
- repository version on that baseline: `5.1.1`
- `workflow-core`: `0.4`
- reviewed task branch: `reviewed/ai-skills-core--machine-update-orchestration`
- reviewed task tip: `f0cb3e41ced59ec247b30f3076edb0d42aeda629`
- task candidate remains: repository `5.2.0`, `ai-skills-core 0.5`

During this amendment drafting, current remote `origin/main` was observed at `403a4457d17169d91f4a7fa10df2b46662eb75a7`, one commit after `67e0bd4`. That additional drift was inspected as icon/test-only (`Refresh domain plugin icons`) and did not change `VERSION`, `workflow-core`, or `ai-skills-core` release semantics. Executor should still begin from latest `origin/main`; after integrating the real `5.1.1` / `workflow-core 0.4` production baseline, do not chase later unrelated docs/icon/evidence drift unless it again touches production/version/release overlap semantics.

## IR-B002 Minimum Closure

The source design direction for dynamic Bridge discovery is acceptable, but the release-critical G3 replay was not acceptable because `candidate_replay/public_machine_state.md` gave the candidate the answer:

- latest formal Bridge release SHA/version;
- current release SHA/version;
- `relation = LAGGING`;
- how to interpret `LAGGING`.

The next G3 evidence must prove that the final candidate itself performs read-only discovery from real Bridge source:

- Bridge `AGENTS.md`;
- canonical version source;
- `CHANGELOG.md`;
- formal closure evidence;
- `refs/heads/release`;
- current `main`.

The replay input may provide only:

- Bridge repository identity and allowed read scope;
- no-mutation boundary.

The replay input must not provide:

- latest formal release answer;
- relation/classification answer;
- expected `LAGGING` result.

The candidate must derive one of:

- `ALIGNED`
- `LAGGING`
- `AHEAD/INCONSISTENT`
- `FORMAL_RELEASE_NOT_PROVABLE`

Do not advance the real Bridge `release` ref. Do not chase unrelated future Bridge versions. A new Bridge commit/version alone is not a blocker unless it materially changes the AGENTS owner locator, release producer semantics, formal release evidence contract, canonical `ai-bridge` ownership/delegation, or this task's actual Bridge dependency.

## IR-B003 Minimum Closure

The previous repair partially closed the old harness-self-PASS problem because the candidate child really modified fixtures. It still does not satisfy release-critical G4/G5 because the task/prompt over-told expected final states, and G5 evidence explicitly stated:

`No official Marketplace command or global state mutation executed.`

That cannot prove the frozen Marketplace recovery owner path.

The next repair must use:

- task-owned fixture repositories under `private/exports/ai-skills-core--machine-update-orchestration/fixtures/`;
- a temporary isolated Codex identity / `CODEX_HOME` for Marketplace recovery evidence;
- official Codex Marketplace/plugin commands for Marketplace semantics inside that isolated identity;
- the canonical AI_Skills owner/update path for managed-consumer cases;
- bounded failure injection;
- before/after hashing and Git state capture by the harness only.

The fixture harness may setup/reset fixtures, inject bounded failure, hash/capture state, assert invariants, and collate evidence. It must not implement the business logic under test and must not manufacture semantic statuses.

The prompt to the candidate must not directly tell it the final expected status for each case. It may provide the fixture layout, the allowed no-mutation boundary, and the task objective.

Required G4/G5 proof on the same final candidate:

- stale managed consumer is updated by candidate/owner path;
- unaffected repo is no-op;
- unmanaged apparent conflict returns `REPO_OWNED_CONFLICT` with unowned file hash unchanged;
- dirty non-overlap proceeds while preserving unrelated dirty hash;
- dirty overlap emits one bounded Human Gate and leaves overlapping user file unchanged;
- bounded Marketplace failure after an earlier safe step returns `PARTIAL_UPDATE`;
- exact legacy source restoration occurs through the production-owned recovery path in isolated temporary Marketplace state;
- fresh-discovery rerun converges;
- unrelated project-owned content remains unchanged.

## IR-B004 Minimum Closure

Latest accepted `main` has real overlap with the old task candidate:

- repository `5.1.1`;
- `workflow-core 0.4`;
- changed `VERSION`, root `CHANGELOG.md`, README release table, Marketplace config, generated plugin payload, registry/catalog and workflow-core changelog surfaces.

Therefore the old candidate must not wait until Reviewer PASS to be merged over stale `main`.

Before the next independent review, Executor must safely reconcile latest accepted `main` into the current reviewed branch:

- preserve `workflow-core 0.4` from `main`;
- preserve task-owned `ai-skills-core 0.5`;
- keep repository candidate version at `5.2.0` because the V2.1 Maintainer machine-update capability is still a new repository-level user capability;
- rebuild the `5.2.0` changelog on top of the real `5.1.1` baseline;
- regenerate the canonical generated layer;
- run full deterministic regression;
- rerun G1/G3/G4/G5 on the reconciled final candidate;
- bind all release-critical evidence to one new candidate SHA.

Do not lower the task version to `5.1.x`; do not bump workflow-core again; do not bump domain plugins.

## Boundaries That Remain Unchanged

- Do not redesign V2.1.
- Do not create a successor task.
- Do not add Route D.
- Do not rename skills.
- Do not add daemon/watcher/database/ledger/machine registry/state machine/updater engine.
- Do not change Bridge runtime/source.
- Do not advance Bridge `release`.
- Do not execute G2 before repaired Independent Reviewer PASS.
- Do not fast-forward AI_Skills `release`.
- Do not mutate the real production Marketplace.
- Do not reinstall production `ai-skills-core 0.5`.
- Do not run released smoke.
- No paid API.
- No automation.
- No force/rebase/reset/stash/clean.

G2 remains `SEQUENCED WAITING`.

## Required Handoff After Repair

After repair, Executor must:

1. freeze one reconciled final candidate SHA;
2. rerun source/generated parity, focused regressions and full deterministic tests;
3. rerun G1/G3/G4/G5 evidence on that same SHA;
4. update candidate replay evidence, public machine state, fixture evidence, implementation evidence, completion audit, Reviewer handoff and Independent Reviewer prompt;
5. commit only the bounded repair/evidence;
6. push `reviewed/ai-skills-core--machine-update-orchestration`;
7. verify remote task tip equals intended local HEAD;
8. stop at Independent Reviewer handoff.

NEXT_HANDOFF after successful repair: `INDEPENDENT_REVIEWER`
