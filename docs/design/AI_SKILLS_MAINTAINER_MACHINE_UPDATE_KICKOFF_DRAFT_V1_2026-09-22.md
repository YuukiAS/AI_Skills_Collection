# AI Skills Maintainer machine update orchestration — Kickoff Draft V1

Date: 2026-09-22  
Status: DRAFT_ONLY_NOT_AUTHORIZED  
Task key: `ai-skills-core--machine-update-orchestration`

Proposal / Plan:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V1_2026-09-22.md`

Canonical Goal:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V1_2026-09-22.md`

This is a future Codex/Executor kickoff draft. It is not authorization to implement now.

## Future execution identity

Repository:

`YuukiAS/AI_Skills_Collection`

Execution branch proposed by this package:

`reviewed/ai-skills-core--machine-update-orchestration`

Exact task-owned worktree:

Must be resolved from the canonical local AI_Skills checkout on the actual execution machine at user kickoff. This design package does not guess a Linux/macOS/Windows path and does not create the branch/worktree. Before execution begins, the current user-visible kickoff must replace this locator with the exact resolved worktree and thereby authorize that exact branch/worktree.

## Frozen objective

Implement the Critic-approved V1 capability inside the existing `ai-skills-core` plugin so that the normal user workflow becomes:

`AI Skills Maintainer + a short update target`

Examples:

- `update presentations`
- `update workflow-core`
- `update AI Skills`
- `sync this machine`

The user must not need to provide repository paths, versions, commits, Bridge paths, `CODEX_HOME`, local repo inventories, or adaptation templates.

The implementation must remain a thin orchestrator over existing owners, not a new update engine.

## Approved implementation scope if Critic passes V1

Within `AI_Skills_Collection`, implementation may modify only the areas required by the frozen Proposal/Goal:

- add one internal machine/environment update orchestration skill to the existing `ai-skills-core` plugin;
- add the three internal route references for isolated plugin update, major stack/workflow update, and Bridge/Host update;
- make minimal trigger/boundary clarification to existing `ai-skills-repository-maintainer` and/or `project-skill-installer` only if required to prevent overlap;
- update `scripts/codex_marketplace_config.json` and regenerate the existing generated Marketplace/plugin payload;
- reuse or minimally extend existing AI_Skills CLI/discovery helpers only where the frozen capability cannot be expressed through the current implementation;
- add tests/evidence for the approved Capability Gate Matrix;
- close `docs/plugin-todos/ai-skills-core.md`, `docs/plugin-changelogs/ai-skills-core.md`, repository changelog/version/README and generated parity according to the version policy;
- keep all task evidence/artifacts inside the repository.

Do not refine unrelated domain plugins.

## Existing owners that must be reused

- Official Codex plugin/Marketplace commands own installed central-plugin mutation and Marketplace refresh.
- Existing AI_Skills CLI/manifests own AI_Skills-managed profile/consumer installation.
- `YuukiAS/GPT_Codex_AI_Bridge_Kit` owns Bridge runtime, Host Policy, Lite/Review/Persistent Run and other Bridge-owned project consumers.
- `workflow-core` owns complex delivery semantics.
- Target domain plugins own domain correctness.

Do not copy Bridge Host/runtime implementation into AI_Skills.

## Formal release-channel bootstrap

V1 requires a stable formal-release Git ref named `release` for both:

- `YuukiAS/AI_Skills_Collection`
- `YuukiAS/GPT_Codex_AI_Bridge_Kit`

This is a one-time cross-repository Git/release-channel effect, not ordinary daily update behavior.

The future user kickoff must explicitly authorize creation/advancement of those exact `release` refs if they do not yet exist. Immediately before doing so, re-read current formal release evidence and verify the latest closed release commit. Do not blindly reuse historical SHA locators from this draft if main has advanced.

Required properties:

- `release` may move only by fast-forward to a later formally closed release;
- daily Maintainer update never advances `release`;
- do not create/delete/rename other branches or tags;
- do not change remotes/upstreams;
- do not rewrite history or force-push.

If Critic replaces this design with a simpler formal-release locator, follow the approved Critic/Planner revision instead.

## Bridge mutation boundary

No Bridge production behavior change is authorized by this V1 package.

For Bridge updates, consume the current canonical Bridge implementation:

- resolve the active `ai-bridge` executable;
- use `ai-bridge where` for its source/runtime identity;
- verify package/runtime version;
- use safe Git source discovery and fast-forward-only formal-release synchronization when ancestry and dirty ownership permit;
- refresh the editable package installation through the same environment/interpreter when required;
- use `ai-bridge host install/status/validate`;
- use the exact Bridge consumer install/validate command only when the formal release delta requires that consumer refresh.

If implementation proves that Bridge production source must change, stop and return to Planner/Critic. Do not broaden scope in the Executor run.

## Source and dirty-work rules

Apply 056 Source Discovery before mutation.

Required behavior:

- find existing canonical checkout first;
- verify origin/ref/freshness/ancestry;
- preserve unrelated dirty work;
- do not mechanically reclone because the tree is dirty;
- do not stash/reset/restore user work;
- do not remap remotes;
- do not use temporary/reviewed worktrees as normal production installation sources;
- use network clone only when no usable local source exists;
- if safe fast-forward and dirty files do not overlap, proceed;
- if overlap creates real ownership ambiguity, stop at one minimal HUMAN_ONLY question.

## Human Gate rules

Ordinary discovery, public-source fetch, formal-release resolution, required dependency synchronization, plugin reinstall and bounded validation are AGENT_RESOLVABLE.

Only stop for a genuine new authority boundary:

- new provider/account/credential;
- private external transfer;
- destructive operation;
- new deployment/live-global mutation not reasonably contained in the update request;
- unresolved dirty-work ownership;
- irreducible product-semantics choice.

Do not ask the user for paths, versions, commits, Bridge location, `CODEX_HOME`, repo inventory, or obvious required dependency updates.

## Required Gate Matrix

Use the Gate Matrix in Proposal V1, with the same final candidate for release-critical evidence:

1. G1 — short request + formal-release routing/no-op/unknown-unreleased behavior;
2. G2 — stale Marketplace/install + self-update + real fresh-session loading;
3. G3 — cross-layer Bridge/Host delegation through canonical Bridge implementation;
4. G4 — selective repo adaptation + untouched normal repo + dirty/source safety;
5. G5 — partial failure/recovery + Human Gate discipline + should-not-change.

Do not replace these gates with static string checks, source file presence, version file edits, or Marketplace JSON parity alone.

Platform claims must be restricted to environments actually exercised.

## Version/release expectation

The current V1 design proposes, conditional on successful gates:

- repository `5.0.7 -> 5.1.0`;
- `ai-skills-core 0.4 -> 0.5`;
- `workflow-core`: no bump;
- domain plugins: no bump unless their production behavior changes, which is outside this scope;
- Bridge Kit: no bump unless Bridge production source behavior is actually changed.

Re-read `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md` immediately before version closure. Do not bump based only on this draft if implementation scope changes.

README closure is mandatory.

## Validation and delivery

Before reporting complete:

- source/generated Marketplace parity passes;
- relevant repository tests pass;
- normal installed plugin path is used, not source `SKILL.md` as a substitute;
- the fresh-session normal entry loads the released target;
- should-not-change plugins/repos remain unchanged;
- remote task branch is pushed and remote tip is verified when the Reviewed Handoff execution actually starts;
- implementation/result/evidence are committed and pushed before handoff.

No paid API is authorized by this draft. No automation is authorized by this draft.

## Stop conditions

Stop and return to Planner/Critic if execution discovers:

- the formal-release channel design is not implementable with current Codex/Marketplace behavior;
- a Bridge production-source change is required;
- a fourth route is truly necessary as an independent user capability;
- the release requires a new credential/provider/deployment;
- normal fresh-session verification cannot observe the installed released plugin;
- the implementation would need a database/state machine/daemon/watcher/inventory registry;
- version/release semantics differ materially from V1.

Do not create a successor task automatically.
