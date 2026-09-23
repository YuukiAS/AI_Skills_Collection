# AI Skills Maintainer machine update orchestration — Kickoff Draft V2.1

Date: 2026-09-23  
Status: DRAFT_ONLY_NOT_AUTHORIZED  
Task key: `ai-skills-core--machine-update-orchestration`

Proposal / Plan:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md`

Canonical Goal:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md`

Planner response to V1 Critic:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PLANNER_RESPONSE_V2_1_2026-09-23.md`

This file is a future user-to-Codex kickoff draft. It is not current authorization to implement, create branches/worktrees, mutate Marketplace/Host state, create `release` refs, call paid APIs, or start automation.

## Future execution identity

Repository:

`YuukiAS/AI_Skills_Collection`

Proposed exact task branch:

`reviewed/ai-skills-core--machine-update-orchestration`

Exact task-owned worktree:

`/home/yuukias/AI_Skills_Collection-ai-skills-core-machine-update-orchestration`

Before the user sends the final approved kickoff, Codex must discover the canonical local AI_Skills checkout on that machine and replace the locator above with one exact task-owned worktree. Do not guess a path from historical Linux/Windows/macOS machines.

## Frozen implementation objective

Implement the Critic-approved V2.1 capability so the normal user workflow becomes:

`AI Skills Maintainer + short update target`

including:

- `update presentations`
- `update workflow-core`
- `update AI Skills`
- `update Bridge Kit`
- `sync this machine`

The normal user must not need to supply versions, commits, checkout paths, `CODEX_HOME`, repo inventories, adaptation templates, or dependency/component lists.

## Approved source scope after V2 PASS

Within AI_Skills_Collection, the bounded implementation may:

1. add one new internal `machine-update-orchestrator` skill to `ai-skills-core`;
2. add one new internal `bridge-kit-maintainer` skill to `ai-skills-core`;
3. package three internal route references for:
   - isolated AI_Skills plugin/profile update;
   - cross-layer stack/workflow composition;
   - Bridge Kit distribution/runtime update;
4. make minimal trigger/boundary updates to:
   - `ai-skills-repository-maintainer`;
   - `project-skill-installer`;
   - only if needed to prevent overlap with the new skills;
5. extend/reuse existing AI_Skills CLI helpers only where the approved normal-entry contract cannot be implemented through current Codex/AI_Skills/Bridge surfaces;
6. update `scripts/codex_marketplace_config.json`;
7. regenerate the existing generated plugin/Marketplace layer through the canonical generator;
8. add/update tests and evidence for G1–G5;
9. update release/version/TODO/changelog/README/install guidance required by the approved release;
10. add the canonical formal-release/update-impact contract inside the AI Skills Maintainer source/reference layer.

Do not refine unrelated domain plugin behavior.

## Bridge Kit source scope

Bridge Kit remains the runtime implementation owner.

This task may consume/read/test the current canonical Bridge implementation and may, **only after explicit current-user authorization in the final kickoff**:

- create/bootstrap the exact remote `release` branch for `YuukiAS/GPT_Codex_AI_Bridge_Kit` from the latest verified formally closed Bridge release commit;
- maintain that formal release ref only under the new central Maintainer release contract;
- modify exactly one tracked Bridge file for producer-owner discoverability: `YuukiAS/GPT_Codex_AI_Bridge_Kit/AGENTS.md`.

The Bridge `AGENTS.md` write is mandatory but narrowly bounded. It may add only a minimal locator stating:

- Bridge runtime / Host / Lite / Review / Control / Persistent Run implementation authority remains in Bridge Kit;
- formal Bridge distribution/version closure, including the moving `release` ref, is owned by AI Skills Maintainer (`ai-skills-core` -> internal `bridge-kit-maintainer`);
- a Bridge formal release must hand off to that owner before distribution completion;
- the canonical producer contract remains single-sourced in AI_Skills_Collection and is not duplicated into Bridge.

Do not modify Bridge README, QUICKSTART, CHANGELOG or runtime source for this locator.

This task may not:

- modify Bridge Host Policy implementation;
- modify Lite/Review/Control/Persistent Run implementation;
- modify Human Gate/plugin replay runtime;
- add a Bridge updater/daemon/watcher/state machine;
- bump Bridge version merely for the central maintenance contract.

If Bridge production runtime/source behavior must change, stop and return to Planner/Critic.

## New internal Bridge maintenance skill

`bridge-kit-maintainer` must own only Bridge maintenance/distribution concerns:

- discover resolved `ai-bridge` executable;
- identify `ai-bridge where` runtime/source root;
- verify package/runtime version;
- resolve the formal Bridge `release` ref;
- safely update a canonical Bridge checkout when ancestry and dirty ownership permit;
- refresh the existing editable package/entry point from that formal source;
- verify runtime version/path after update;
- during a future formal Bridge release closure, verify closure/version/changelog evidence and advance the Bridge `release` ref;
- delegate Host/project-consumer mutation back to canonical `ai-bridge` commands.

It must not copy Bridge runtime logic into AI_Skills.

## Formal release-channel bootstrap authority

The final user-sent kickoff, after Critic PASS, is expected to authorize the bounded one-time creation/bootstrap of exactly two remote refs if absent:

- `YuukiAS/AI_Skills_Collection:refs/heads/release`
- `YuukiAS/GPT_Codex_AI_Bridge_Kit:refs/heads/release`

Before any write:

1. re-read latest main and formal closure evidence;
2. identify the latest formally closed release commit for each repo;
3. verify repo/origin identity;
4. verify an existing `release` ref, if present, can only fast-forward to the target;
5. do not reuse stale SHAs from the design documents without revalidation.

Authorized ref behavior in the future final kickoff:

- create if absent at the exact formal release commit;
- fast-forward only;
- no force;
- no tag creation/deletion;
- no other branch creation/deletion/rename;
- no remote/upstream changes;
- verify remote ref after write.

Daily machine update must never advance these refs.

## AI Marketplace legacy bootstrap

The final implementation must support a one-time migration from a real legacy AI_Skills Marketplace configured at `main`.

Before mutation, discover and record:

- Marketplace name;
- Git source URL;
- ref;
- sparse paths;
- owning config layer;
- installed/enabled AI_Skills plugin state.

Proceed only when:

- source is the expected AI_Skills repository;
- ref is `main`;
- sparse paths match expected generated Marketplace/payload paths;
- the source is user-owned/mutable;
- remote `release` is verified.

Use only official Codex Marketplace/plugin commands.

If removing the old source is necessary:

- retain exact old source metadata for restoration;
- add the same source at `release`;
- verify the new source;
- reinstall ai-skills-core and the requested target;
- restore the old source if replacement fails;
- do not invent a second permanent Marketplace identity;
- do not directly hand-edit Codex config.

If another config layer owns the source, fail closed and report the exact layer.

The old 0.4 plugin is not claimed to already implement this path. The first rollout is an explicit bootstrap exception.

## Authoritative Update impact contract

Formal release scope expansion must use:

`release ref -> matching root CHANGELOG release section -> optional ### Update impact`

If `### Update impact` is absent, treat the release as isolated.

If present, only the declared companion components and managed consumer refreshes may enlarge scope.

Component changelogs can clarify but cannot independently broaden the mutation set.

Conflicts fail closed.

Do not infer Bridge/Host mutation from arbitrary Git diff, commit message, TODO, README prose or model intuition.

## Automatic repo adaptation boundary

Automatically mutate only:

- AI_Skills manifest-managed installs/managed blocks;
- Bridge canonical managed templates/blocks/consumers;
- exact release-declared migrations with a proven owner locator.

Do not auto-edit unowned project text.

An unmarked project AGENTS/rule that appears to conflict must remain byte-for-byte unchanged and be reported as `REPO_OWNED_CONFLICT` unless the user separately authorizes a repo-owned task.

## Source / Git / dirty-work rules

Apply 056 Source Discovery.

Required:

- existing canonical checkout first;
- verify origin/ref/freshness/ancestry;
- unrelated dirty work is not an automatic blocker;
- allow safe non-overlapping fast-forward;
- no stash/reset/restore/checkout-away;
- no remote remap;
- no normal installation from reviewed/temporary worktrees;
- clone only when no usable local source exists.

If development source is intentionally ahead/diverged, do not downgrade it to `release`. Prefer independent formal runtime/Marketplace source or report `DEVELOPMENT_SOURCE_PRESENT`.

If actual user-owned dirty overlap is ambiguous, ask one minimal Human Gate naming the exact path(s).

## Human Gate boundary

The final user kickoff authorizes ordinary bounded mechanics needed to implement and validate this approved task, including public-source reads, ordinary tests, generated parity, approved task-branch commit/push, and the explicitly bounded release-ref bootstrap described above.

The later approved kickoff must also bind the Bridge-side tracked write scope to **only** `GPT_Codex_AI_Bridge_Kit/AGENTS.md` for the locator above. No other Bridge tracked-file write is authorized by that locator scope.

It does not pre-authorize:

- new provider/account/credential;
- private external transfer;
- paid API;
- destructive Git;
- force push;
- arbitrary branch changes;
- unrelated production deployment;
- unrelated repo modification;
- Bridge production behavior changes.

During implementation, do not ask the user for discoverable versions/paths/commits/`CODEX_HOME`/Bridge location/obvious required companions.

## Required G1–G5

The implementation must pass the V2.1 Gate Matrix exactly as frozen in Proposal V2:

- G1 short request + formal-release/update-impact routing;
- G2 legacy main->release Marketplace bootstrap + install/self-update + fresh-session loading;
- G3 Bridge Kit maintenance + mandatory Bridge `AGENTS.md` producer-owner routing + formal-release Git behavior + canonical Bridge delegation;
- G4 selective managed consumers + dirty/source safety + unmanaged conflict preservation;
- G5 failure/recovery/Human Gate/should-not-change.

Do not replace normal-entry behavior with fixture-only/string/parity evidence.

All release-critical evidence must bind to the same final candidate.

## Version/release expectation

If the final implementation scope remains V2.1 and G1–G5 pass:

- repository `5.0.7 -> 5.1.0`;
- `ai-skills-core 0.4 -> 0.5`;
- `workflow-core`: no bump;
- domain plugins: no bump;
- Bridge Kit: no bump merely for the mandatory minimal `AGENTS.md` owner locator or `release` ref, unless Bridge production runtime behavior changes.

Re-read the version policy before closure.

README and installation guidance closure are mandatory.

## Delivery and handoff

Before claiming implementation complete:

- source/generated parity passes;
- relevant tests pass;
- installed production plugin path is used;
- the one-time legacy bootstrap is actually exercised;
- a fresh Codex process/session proves the final released Maintainer normal entry;
- Bridge route is exercised through `bridge-kit-maintainer` + canonical Bridge CLI;
- stale managed consumer adaptation and untouched/unmanaged repo cases are both demonstrated;
- final release candidate identity is single and consistent;
- task branch is committed/pushed and remote tip verified before handoff.

No paid API. No automation.

## Stop and return to Planner/Critic if

- current Codex Marketplace semantics invalidate the approved bootstrap;
- Bridge production code must change;
- a fourth independent user route becomes necessary;
- a database/daemon/watcher/registry/state machine becomes necessary;
- release metadata cannot determine cross-layer scope;
- fresh-session normal-entry verification cannot observe the released plugin;
- version semantics materially change;
- implementation requires authority outside this draft.
