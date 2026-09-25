# Codex Executor Repair Prompt 2 - ai-skills-core machine update orchestration

Repository:

`YuukiAS/AI_Skills_Collection`

Exact task branch:

`reviewed/ai-skills-core--machine-update-orchestration`

Previously reviewed remote task tip:

`f0cb3e41ced59ec247b30f3076edb0d42aeda629`

Independent Reviewer result for that exact tip:

`REVISE`

Finding status:

- `IR-B001 = CLOSED`
- `IR-B002 = STILL_OPEN`
- `IR-B003 = STILL_OPEN`
- `IR-B004 = NEW_FROM_LATEST_MAIN_DRIFT`

This is the same implementation-review recovery. Do not create a successor. Do not redesign the Critic-PASSed V2.1 architecture.

## 0. First: Synchronize Identity And Read Contracts

Before editing:

1. `git fetch origin main`.
2. Fetch/verify the exact task branch `reviewed/ai-skills-core--machine-update-orchestration` using the repository's allowed/canonical command shape where possible. If sandbox blocks `.git/worktrees/.../FETCH_HEAD`, use the minimal approved/escalated fetch needed only for this exact branch.
3. Verify:
   - origin is `YuukiAS/AI_Skills_Collection`;
   - current worktree is `/home/yuukias/AI_Skills_Collection-ai-skills-core-machine-update-orchestration`;
   - current branch is `reviewed/ai-skills-core--machine-update-orchestration`;
   - remote task branch contains `f0cb3e41ced59ec247b30f3076edb0d42aeda629`;
   - no user-owned dirty overlap blocks the exact repair paths.
4. Do not rebase, reset, stash, clean, force push, change remotes, or change arbitrary branches.

Read first:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `results/ai-skills-core--machine-update-orchestration/IMPLEMENTATION_REVIEW_RECOVERY_AMENDMENT_2.md`
- current implementation evidence, completion audit, candidate replay evidence, fixture evidence, Reviewer handoff and Independent Reviewer prompt.

Use latest `origin/main` as the real integration baseline. User-verified baseline was:

- `67e0bd4a09bcc120dd397cb55c78592f4ab34a73`
- repository `5.1.1`
- `workflow-core 0.4`

During amendment drafting, `origin/main` was also observed at `403a4457d17169d91f4a7fa10df2b46662eb75a7`, which was inspected as icon/test-only drift after `67e0bd4`. Start from whatever latest `origin/main` is now, but after integrating the real `5.1.1` / `workflow-core 0.4` production baseline, do not chase later unrelated docs/icon/evidence drift unless it again touches production/version/release overlap semantics.

## 1. Scope

Repair only:

- `IR-B002`;
- `IR-B003`;
- `IR-B004`.

`IR-B001` is closed. Preserve that closure unless the main reconciliation creates a direct documentation/test conflict.

Do not reopen V2.1 architecture. Do not rename skills. Do not add Route D. Do not add daemon/watcher/database/ledger/machine registry/state machine/Bridge updater engine/duplicated Bridge release policy.

No paid API. No automation.

Do not execute G2. Do not advance AI_Skills `release`. Do not migrate the real Marketplace. Do not reinstall production `ai-skills-core 0.5`. Do not run released smoke. Do not advance Bridge `release`. Do not modify Bridge runtime/source.

## 2. IR-B004 - Reconcile Latest Main Before Review

Safely integrate latest accepted AI_Skills `main` into the reviewed branch before rerunning evidence.

Minimum semantic requirements:

- preserve main's accepted repository baseline `5.1.1`;
- preserve main's accepted `workflow-core 0.4`;
- preserve task-owned `ai-skills-core 0.5`;
- keep the repaired task candidate as repository `5.2.0`;
- rebuild root `CHANGELOG.md` so `5.2.0` is based on the real `5.1.1` baseline;
- keep workflow-core/domain plugins unchanged from latest main unless a direct generated parity consequence requires regeneration;
- regenerate canonical generated layer from source;
- do not overwrite unrelated accepted main changes.

If integration produces a real semantic conflict in version/release/source ownership that cannot be resolved under these rules, stop and return to Planner/Critic with exact files and conflict.

## 3. IR-B002 - Candidate Must Dynamically Discover Bridge Release State

The source/reference design direction may be kept, but the release-critical replay must no longer hand the answer to the candidate.

Repair G3 so the final candidate itself performs read-only discovery from the real Bridge source:

- Bridge `AGENTS.md`;
- canonical version source;
- `CHANGELOG.md`;
- formal closure evidence;
- `refs/heads/release`;
- current `main`.

The replay input may provide only:

- Bridge repo identity and allowed read scope;
- no-mutation boundary.

The replay input must not provide:

- latest formal release SHA/version;
- current formal/release relation;
- expected `LAGGING` result;
- instructions telling the candidate how to classify the observed case.

The candidate must derive one of:

- `ALIGNED`
- `LAGGING`
- `AHEAD/INCONSISTENT`
- `FORMAL_RELEASE_NOT_PROVABLE`

The latest formal release must be supported by the existing formal version/changelog/closure-evidence contract. It must not be inferred from newest main SHA, highest-looking version string alone, changelog heading alone, arbitrary docs/TODO/evidence drift, or model intuition.

Required real-world G3 behavior:

- begin from the real Bridge repo's normal formal-release maintenance entry;
- actually consume Bridge `AGENTS.md` owner locator;
- route to AI Skills Maintainer / `bridge-kit-maintainer`;
- classify the real snapshot without being told the expected relation;
- keep daily `update Bridge Kit` read-only with respect to Bridge `release`;
- allow Bridge `release` advancement only under formal producer closure;
- preserve canonical `ai-bridge` runtime ownership/delegation.

Do not advance the real Bridge `release` ref. Do not chase future unrelated Bridge versions.

Regenerate `results/ai-skills-core--machine-update-orchestration/candidate_replay/public_machine_state.md` so it is an input boundary, not an answer key. It may identify the Bridge repo/read scope/no-mutation boundary. It must not state latest formal Bridge release, current release version, relation/classification or the expected interpretation.

## 4. IR-B003 - Candidate/Owner Path Must Prove G4/G5, Including Isolated Marketplace Recovery

The fixture harness may:

- create/reset task-owned fixtures;
- create a temporary isolated Codex identity / `CODEX_HOME`;
- seed an isolated Marketplace/plugin state as a fixture;
- inject bounded failure;
- record before/after hashes and Git state;
- assert invariants;
- collate evidence.

The fixture harness must not:

- perform the managed-consumer update itself;
- perform Marketplace source replacement/restoration logic itself;
- fabricate `UPDATED`, `UPDATED_RELOAD_REQUIRED`, `REPO_OWNED_CONFLICT`, `HUMAN_ONLY` or `PARTIAL_UPDATE`;
- tell the candidate the final expected status for each case.

Managed-consumer cases must execute through the exact final candidate and the canonical AI_Skills owner/update path selected by it.

Marketplace failure/recovery must execute inside the isolated temporary `CODEX_HOME` through official Codex Marketplace/plugin commands. Do not touch the user's real production Marketplace, global plugin installation, real Codex config, or unrelated projects.

Required evidence on the same final candidate:

- stale managed consumer -> actual candidate/owner path updates it;
- unaffected repo -> actual candidate/owner path no-ops;
- unmanaged apparent conflict -> actual candidate returns `REPO_OWNED_CONFLICT`, unowned file hash unchanged;
- dirty non-overlap -> actual candidate proceeds safely, unrelated dirty hash preserved;
- dirty overlap -> actual candidate emits one bounded Human Gate, overlapping user file unchanged;
- bounded Marketplace failure after earlier safe step -> actual candidate returns `PARTIAL_UPDATE`;
- exact legacy source restoration occurs through the production-owned recovery path in isolated temporary Marketplace state;
- fresh-discovery rerun converges;
- unrelated project-owned content unchanged.

Record for every release-critical case:

- exact final candidate SHA;
- candidate/plugin/owner path consumed;
- actual returned state;
- before/after hashes;
- failure injection point;
- same-final-candidate identity.

Do not use unrelated real user repositories.

## 5. Validation After Repair

After source repair:

1. regenerate the canonical generated layer;
2. run source/generated parity and Marketplace build checks;
3. run focused Maintainer/install/release regressions;
4. run the required full repository test suite;
5. freeze one exact reconciled final candidate SHA;
6. rerun G1 because candidate identity changed;
7. rerun repaired G3 with dynamic Bridge discovery;
8. rerun repaired candidate-direct G4/G5 with isolated Marketplace recovery evidence;
9. verify no unrelated real project or real production Marketplace was mutated;
10. update:
    - `results/ai-skills-core--machine-update-orchestration/candidate_replay/CANDIDATE_REPLAY_EVIDENCE.md`
    - `results/ai-skills-core--machine-update-orchestration/candidate_replay/public_machine_state.md`
    - `results/ai-skills-core--machine-update-orchestration/fixture_execution/G4_G5_FIXTURE_EVIDENCE.md`
    - `results/ai-skills-core--machine-update-orchestration/fixture_execution/g4_g5_fixture_evidence.json`
    - `results/ai-skills-core--machine-update-orchestration/IMPLEMENTATION_EVIDENCE.md`
    - `results/ai-skills-core--machine-update-orchestration/COMPLETION_AUDIT.md`
    - `results/ai-skills-core--machine-update-orchestration/REVIEWER_HANDOFF.md`
    - `results/ai-skills-core--machine-update-orchestration/INDEPENDENT_REVIEWER_PROMPT.md`

All release-critical G1/G3/G4/G5 evidence must bind to the same reconciled final candidate SHA.

Do not claim G2 PASS.

## 6. Commit / Push / Handoff

Commit only the bounded repair and evidence.

Push the exact task branch:

`reviewed/ai-skills-core--machine-update-orchestration`

Verify remote tip equals intended local HEAD.

Then stop at Independent Reviewer handoff.

Do not self-declare full V2.1 Goal PASS.

## 7. Stop Conditions

Stop and return to Planner/Critic if this repair actually requires changing:

- V2.1 architecture;
- owner boundary;
- release producer contract;
- Bridge runtime behavior/source;
- authorization scope;
- Gate taxonomy;
- G2 sequencing;
- recovery semantics.

Also stop if current Codex Marketplace official commands cannot operate in isolated temporary `CODEX_HOME` sufficiently to prove G5 without touching real user Marketplace state.

NEXT_HANDOFF after successful repair:

`INDEPENDENT_REVIEWER`
