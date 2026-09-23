# AI Skills Maintainer machine update orchestration — Planner response V2.1

Date: 2026-09-23  
Task key: `ai-skills-core--machine-update-orchestration`  
Review stage: V2 Critic minimal revision after V1 blocker closure

## Source revalidation

AI_Skills_Collection latest `main` is still `52468056b76ea45f5f76b6b10ba245a5bdb54440`, the V2 Critic-prompt commit. No production source or governing contract drift occurred after the reviewed V2 package.

Bridge latest `main` is `b76a7da0fdbb4f92205b0b168241c084c1489c6f`. A targeted read of Bridge `AGENTS.md` confirms there is currently no `AI Skills Maintainer`, `bridge-kit-maintainer`, formal-distribution owner, or release-ref owner locator. This directly supports the remaining Critic discoverability finding.

No new external capability assumption is introduced in this minimal revision. The current Codex Marketplace/session semantics already independently checked in V2 are unchanged and are not re-litigated here.

## Finding status

- `MU-B001 = CLOSED` — unchanged.
- `MU-B003 = CLOSED` — unchanged.
- `MU-B004 = CLOSED` — unchanged.
- `MU-B002 = ACCEPT / closed by mandatory Bridge AGENTS locator + G3 producer evidence`.

## MU-B002 minimal closure

The centralized producer architecture remains exactly as accepted:

- AI_Skills formal `release` owner = `ai-skills-repository-maintainer`;
- Bridge formal `release` owner = `bridge-kit-maintainer`;
- full fast-forward-only producer contract remains single-sourced in AI Skills Maintainer;
- Bridge runtime / Host / Lite / Review / Control / Persistent Run / plugin replay implementation remains owned by Bridge.

The only new frozen implementation requirement is discoverability from a Bridge-native maintenance/release entry.

Future implementation must add exactly one minimal tracked locator to:

`YuukiAS/GPT_Codex_AI_Bridge_Kit/AGENTS.md`

Required semantics:

1. Bridge runtime/Host/Lite/Review/Control/Persistent Run implementation authority remains in Bridge Kit.
2. Formal Bridge distribution/version closure, including the moving `release` ref, is owned by AI Skills Maintainer (`ai-skills-core` -> internal `bridge-kit-maintainer`).
3. A Bridge formal release must hand off to that owner before it is distribution-complete.
4. The canonical producer contract remains in AI_Skills_Collection; Bridge does not receive a duplicate release engine/policy/state machine.

Do not duplicate the locator across Bridge README/QUICKSTART/CHANGELOG.

The future user kickoff may authorize only this Bridge tracked-file write for the locator. It does not authorize Bridge runtime source changes.

## G3 amendment

No new gate is created.

G3 now proves both directions:

- consumer: `update Bridge Kit` through AI Skills Maintainer;
- producer: normal Bridge formal-release maintenance entry -> Bridge AGENTS locator -> AI Skills Maintainer / `bridge-kit-maintainer`.

Release-critical G3 evidence must additionally prove:

- only the exact formally closed Bridge commit can advance `release`;
- advancement is fast-forward-only;
- remote ref is verified after write;
- later ordinary docs/TODO/main commits do not advance the ref;
- non-fast-forward or inconsistent target/ref fails closed;
- runtime implementation continues to execute through canonical Bridge/`ai-bridge` ownership.

A deterministic presence test for the locator is allowed as cheap regression evidence, but string presence alone cannot PASS G3.

## Naming

No naming change is made in V2.1. Existing internal names remain valid. The Critic's naming suggestions remain non-blocking implementation cleanup only; if retained, skill descriptions must clearly state their owner boundary.

## Version and all other architecture

Unchanged:

- public display: `AI Skills Maintainer`;
- slug: `ai-skills-core`;
- exactly three routes;
- `sync this machine` is composition;
- legacy Marketplace bootstrap;
- `Update impact` authority;
- managed-surface-only adaptation;
- repository planned `5.0.7 -> 5.1.0`;
- ai-skills-core planned `0.4 -> 0.5`;
- workflow-core/domain plugins NO_BUMP;
- Bridge Kit NO_BUMP while production runtime behavior remains unchanged.

This Planner round remains design-only and does not modify Bridge, production source, release refs, Marketplace, Host state, branch/worktree, paid API or automation.
