# AI Skills Maintainer machine update orchestration — Canonical Goal V1

Date: 2026-09-22
Status: PLANNER_DRAFT_FOR_CRITIC
Task key: `ai-skills-core--machine-update-orchestration`
Repository: `YuukiAS/AI_Skills_Collection`
Proposal: `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V1_2026-09-22.md`

## Goal

Turn the existing `ai-skills-core` plugin, shown to users as **AI Skills Maintainer**, into the single normal user entry for updating the AI Research Stack on the current Codex machine or server.

After the capability is formally released and bootstrapped once, the user should be able to invoke AI Skills Maintainer with a short request such as:

- `update presentations`
- `update workflow-core`
- `update AI Skills`
- `sync this machine`
- `把这台 server 的 AI Research Stack 更新一下`

without supplying repository paths, plugin versions, release numbers, commits, Bridge paths, `CODEX_HOME`, repo inventories, or adaptation templates.

## Required product behavior

The Maintainer must:

1. discover the current machine/Codex identity and relevant installed/runtime state;
2. resolve the newest **formal released** target, not arbitrary current `main`;
3. classify the request into the minimum required internal update route;
4. delegate actual mutations to the existing canonical owner:
   - official Codex plugin/Marketplace tooling for installed central plugins;
   - existing AI_Skills CLI/manifests for managed AI_Skills consumers;
   - Bridge Kit CLI for Bridge runtime, Host Policy, Lite/Review/Persistent Run and other Bridge-owned consumers;
5. adapt only consumers proven stale or release-required;
6. protect unrelated dirty user work and repo-specific rules;
7. ask the user only for a genuine `HUMAN_ONLY` dependency;
8. verify that the next normal fresh Codex session actually consumes the target release;
9. report the result concisely.

## Formal-release requirement

Normal `update` must use a stable formal-release Git channel and must not silently consume unreleased `main`, candidate branches, reviewed branches, or evidence-only commits.

V1 proposes a lightweight `release` branch in AI_Skills_Collection and Bridge Kit. It advances only during formal release closure and is fast-forward-only. The first implementation must establish/validate that channel before the new Maintainer capability can be declared production-ready.

Explicit user requests for current `main`/development builds are a separate development mode and must be reported as such.

## Ownership boundaries

AI Skills Maintainer owns discovery, formal-release resolution, route selection, bounded adaptation planning, delegation, verification and reporting.

It must not absorb:

- Bridge Host/runtime implementation;
- workflow-core delivery semantics;
- domain judgment from presentations, writing, statistics, medical imaging, bioinformatics or other target plugins;
- a second update engine, state machine, daemon, watcher, inventory database, machine registry, ledger or authorization system.

## Internal route model

Keep exactly three mutation routes unless implementation evidence proves a genuinely independent fourth capability:

- Route A: isolated central plugin/profile update;
- Route B: formal release whose dependency delta genuinely crosses stack/workflow layers;
- Route C: Bridge/Host/runtime update delegated to Bridge.

`sync this machine` is a composition/scope request over the installed/participating stack, not a fourth mutation engine.

## Selective repository adaptation

Do not mass-migrate repositories.

Only mutate a local repo when evidence shows a stale managed pin/consumer, an obsolete Bridge consumer explicitly covered by the release, a stale/broken locator, a copied generic rule conflicting with central behavior, an override that defeats the new global behavior, or a formal release requirement.

A normal repo that naturally consumes the update through Host Policy plus the installed central plugin must remain untouched and be reported as `NO_REPO_ADAPTATION_REQUIRED`.

## Source and dirty-work safety

Inherit 056 Product Delivery Discipline Source Discovery:

- prefer existing canonical source;
- verify origin, ref, freshness and ancestry;
- do not treat unrelated dirty work as an automatic blocker;
- do not stash/reset/restore/switch away user work or remap remotes;
- use fast-forward-only formal-release advancement when safe;
- do not install normal production from temporary/reviewed worktrees;
- clone only when no usable local source exists.

For an intentionally ahead/diverged development checkout, do not downgrade or pretend it is the formal runtime. Report the development-source condition or use an independent formal installation path where available.

## Self-update and reload truthfulness

The first capability-bearing Maintainer release may require one bootstrap install because current `ai-skills-core 0.4` does not contain this orchestration.

After that bootstrap, an old loaded Maintainer must be able to discover and install the newer formal Maintainer release, but it must not claim that the current session hot-reloaded. It must return a reload-required state and release acceptance must prove the new version through a genuinely fresh Codex process/session.

## Human Gate boundary

Ordinary discovery, public-source fetch, release resolution, safe plugin reinstall, required dependency synchronization and validation are `AGENT_RESOLVABLE`.

A single bounded Human Gate is allowed only for genuine new authority, credentials/account/provider, private external transfer, destructive/live-global effect outside the update request, unresolved dirty-work ownership, or irreducible product semantics. Do not ask the user for machine facts that can be discovered.

## Acceptance

The final candidate must pass the Gate Matrix frozen in Proposal V1:

- G1 short-request/formal-release routing;
- G2 Marketplace/install/self-update/fresh-session consumption;
- G3 cross-layer Bridge/Host delegation;
- G4 selective consumer adaptation and dirty/source safety;
- G5 failure/recovery/authorization/should-not-change.

The same final candidate must supply the release-critical evidence. Platform claims must be limited to environments actually exercised.

## Release decision to review

Conditional on Critic approval and successful implementation/gates:

- repository: `5.0.7 -> 5.1.0` (MINOR);
- `ai-skills-core: 0.4 -> 0.5`;
- `workflow-core`: NO_BUMP;
- domain plugins: NO_BUMP unless their production behavior is actually changed;
- Bridge Kit: NO_BUMP if implementation only establishes the formal release ref and reuses unchanged canonical Bridge behavior; any Bridge production-source behavior change requires amended scope and its own version decision.

README closure is mandatory.

## Explicit non-goals

No cross-machine controller, no global repo inventory, no remote deployment system, no all-repo AGENTS rewrite, no automatic installation of every plugin/optional Bridge layer, no current-main default, no per-update Planner/Critic, no routine full Capability Gates, and no claimed hot reload.

## Current phase boundary

This Goal is not execution authorization.

The current phase may create only design/review artifacts in AI_Skills_Collection. Production source, generated payload, version files, Marketplace source configuration, Host state, Bridge runtime/source and remote release refs remain unchanged until:

1. an independent Critic gives PASS on this V1 package; and
2. the user explicitly authorizes the implementation kickoff, including any one-time cross-repo release-ref bootstrap effect.
