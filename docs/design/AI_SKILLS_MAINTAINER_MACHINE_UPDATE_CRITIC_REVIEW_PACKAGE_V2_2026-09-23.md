# AI Skills Maintainer machine update orchestration — Critic Review Package V2

Date: 2026-09-23  
Review stage: V1 REVISE closure + architecture/execution-package review  
Target repo: `YuukiAS/AI_Skills_Collection`  
Target plugin/domain: `ai-skills-core` / AI Skills Maintainer  
Task key: `ai-skills-core--machine-update-orchestration`  
Source branch/ref: `main`

## Review object

Review these V2 files as one package:

1. Planner response to V1 Critic  
   `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PLANNER_RESPONSE_V2_2026-09-23.md`

2. Proposal / Plan V2  
   `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_2026-09-23.md`

3. Canonical Goal V2  
   `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_2026-09-23.md`

4. Kickoff Draft V2  
   `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_KICKOFF_DRAFT_V2_2026-09-23.md`

The package remains design-only.

## Current revalidated baseline

AI_Skills latest main at Planner revision start:

`338add2d7ac002a0201a924be3a0ec2818b777c7`

Relevant production baseline is unchanged from V1:

- repository `5.0.7`;
- `ai-skills-core 0.4`;
- `workflow-core 0.3`;
- current ai-skills-core payload still contains only project installer, repository maintainer and skill-library-analysis.

Bridge latest main at Planner revision start:

`b76a7da0fdbb4f92205b0b168241c084c1489c6f`

Bridge runtime/package remains `0.8.5`; formal release commit is still `d27259d6706dee951dc0c0ede8c9b03c65f55ca3`; newer commits are docs/TODO-only.

This preserves the key V1 premise that `main` may legitimately be newer than the formal released runtime.

## V1 Critic blockers and V2 closure

### MU-B001 — accepted and closed in design

V2 now freezes a real legacy Marketplace bootstrap:

- real configured marketplace/source/ref/sparse/config-layer discovery;
- expected-source verification;
- release-ref preflight before source removal;
- exact legacy metadata capture for restoration;
- official Codex CLI only;
- same source identity moved from `main` to `release`;
- requested Maintainer/target reinstall;
- system/non-user-owned config layer fail-closed;
- restore legacy source if the source-swap itself fails;
- fresh-session requirement;
- explicit statement that 0.4 does not already possess the new updater.

G2 now starts from `0.4 + main-pinned Marketplace`.

### MU-B002 — need accepted, location partially rebutted

V2 accepts the need for a durable producer contract but rejects duplicating the full contract into both repos.

New user requirement explicitly assigns Bridge Kit maintenance/version adaptation to AI Skills Maintainer.

V2 therefore adds an internal `bridge-kit-maintainer` and centralizes release-channel production inside ai-skills-core:

- AI release ref owner: `ai-skills-repository-maintainer`;
- Bridge release ref owner: `bridge-kit-maintainer`.

Bridge remains runtime implementation owner.

V2 permits only a minimal Bridge-side pointer if evidence shows a Bridge-only release task otherwise cannot discover the central release owner. It does not require a second release engine or duplicated contract in Bridge.

Critic should specifically decide whether this centralized owner satisfies the original lifecycle risk. If not, identify the minimum Bridge-side locator required without moving runtime/release machinery into Bridge.

### MU-B003 — accepted and closed in design

V2 defines authoritative cross-layer scope:

`formal release ref -> matching root CHANGELOG release entry -> optional ### Update impact`

Absence means isolated.

Only root release metadata can expand mutation scope. Component changelogs may clarify but not broaden. Arbitrary diffs/TODOs/commit prose/model inference cannot authorize Host/Bridge expansion. Conflict fails closed.

G1/G3 directly test isolated-vs-declared cross-layer behavior.

### MU-B004 — accepted and closed in design

Automatic repo adaptation is now ownership-proven only:

- AI_Skills manifest/managed block;
- Bridge canonical managed consumer/template/block;
- exact formal release migration with ownership locator.

Unmanaged AGENTS/copied/scientific/safety/privacy/Figma/deployment/device/server text is diagnosis-only.

G4 now requires an apparently conflicting unmanaged AGENTS case to remain byte-for-byte unchanged.

## User-requested architecture amendment

The user specifically asked whether Bridge Kit itself should be maintained through AI Skills Maintainer and suggested a separate internal skill rather than adding weight to Bridge.

V2 answers **yes** and adds:

`bridge-kit-maintainer`

inside existing `ai-skills-core`.

Its purpose is Bridge source/version/distribution maintenance and delegation.

It does not reimplement Bridge runtime.

Resulting internal maintenance ownership:

- machine update composition -> `machine-update-orchestrator`;
- AI_Skills repository/plugin release -> `ai-skills-repository-maintainer`;
- AI_Skills project/profile consumer -> `project-skill-installer`;
- Bridge version/distribution/release channel -> `bridge-kit-maintainer`;
- skill/library overlap -> `skill-library-analysis`.

The public entry remains **AI Skills Maintainer**.

## External reality recheck

Planner rechecked current OpenAI sources on 2026-09-23.

Relevant facts remain:

- Git Marketplace supports `--ref`;
- Marketplace has add/list/upgrade/remove;
- plugin has add/list JSON/available surfaces;
- changing source/ref is not ordinary refresh;
- Marketplace removal refuses mutation when another enabled config layer owns the marketplace;
- reinstall + new thread/session is the safe plugin update consumption boundary.

Planner sources:

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/api/docs/guides/latest-model
- https://github.com/openai/codex/blob/main/codex-rs/cli/src/plugin_cmd.rs
- https://github.com/openai/codex/blob/main/codex-rs/cli/src/marketplace_cmd.rs
- https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/marketplace_remove.rs
- https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/installing-and-updating.md

Critic must still do its own targeted external verification rather than relying only on this list.

## Gate Matrix V2

No new gates were added.

- G1 — short request + formal release/update-impact routing
- G2 — real legacy Marketplace bootstrap + installed plugin/self-update + fresh-session consumption
- G3 — Bridge Kit maintenance + canonical Bridge delegation
- G4 — selective managed consumers + dirty/source safety + unmanaged-conflict preservation
- G5 — failure/recovery/Human Gate/should-not-change

Critic should check that adding `bridge-kit-maintainer` does not secretly create a fourth route or duplicate Bridge runtime ownership.

## Version decision

Planner still proposes:

Repository: `5.0.7 -> 5.1.0` MINOR

Reason: one short Maintainer request becomes a new repository-level machine/environment/distribution workflow, now explicitly including Bridge Kit version/distribution.

Plugin:

`ai-skills-core 0.4 -> 0.5`

No planned bump:

- workflow-core;
- domain plugins;
- Bridge Kit if runtime production behavior stays unchanged.

If Critic believes adding a Bridge-side minimal release pointer itself requires a Bridge version bump, distinguish documentation/distribution-contract change from runtime production behavior and cite the governing Bridge version contract before blocking.

## Exact review questions

1. Are MU-B001, MU-B003 and MU-B004 now closed without unnecessary machinery?
2. Does the V2 centralized release producer contract close MU-B002, or is a minimal Bridge-side pointer mandatory?
3. Is the new `bridge-kit-maintainer` the correct place for Bridge source/version/distribution maintenance while Bridge runtime remains canonical?
4. Has V2 kept exactly three mutation routes?
5. Does `Update impact` provide a sufficiently authoritative scope source without creating a dependency schema/database?
6. Is the legacy Marketplace bootstrap recoverable and appropriately fail-closed?
7. Does selective adaptation now respect repo ownership?
8. Is self-update/fresh-session acceptance strong enough?
9. Is G1–G5 still sufficient and non-duplicative?
10. Does the proposed version decision remain correct?
11. Is the Kickoff Draft bounded enough for future current-user authorization without pretending the worktree is already known?

## Required Critic output

Return exactly one formal result:

`RESULT = PASS`

or

`RESULT = REVISE`

If REVISE:

- first recheck the old blocker IDs;
- do not rename/rephrase an already closed blocker merely to move the goalpost;
- any new blocker must come from a new fact, a previously missed direct risk, or the user-requested Bridge-maintenance amendment;
- provide user/contract requirement, direct evidence, causal risk, minimum closing condition and owner.

A design-stage PASS does not authorize implementation, branch/worktree creation, remote `release` writes, Marketplace migration, Host mutation, paid API, automation or deployment.
