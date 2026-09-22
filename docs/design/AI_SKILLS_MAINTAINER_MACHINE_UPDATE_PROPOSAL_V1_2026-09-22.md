# AI Skills Maintainer machine update orchestration — Proposal / Plan V1

Date: 2026-09-22
Status: PLANNER_PROPOSAL_FOR_CRITIC
Task key: ai-skills-core--machine-update-orchestration
Repository: YuukiAS/AI_Skills_Collection
Normal user entry: AI Skills Maintainer
Compatibility slug: ai-skills-core

## 1. Product conclusion

AI Skills Maintainer should become the only user-facing entry for updating the AI Research Stack on one machine, while remaining a thin orchestrator. The user supplies only a target such as “update presentations”, “update workflow-core”, “update AI Skills”, or “sync this machine”. The plugin discovers machine and installation state, resolves the latest formal release, chooses the required internal route, delegates mutations to existing owners, validates the result, and returns a short report.

The selected architecture is not a new update engine. It adds one machine-update orchestration skill inside ai-skills-core, plus small internal route references. It reuses:

- the official Codex plugin / Marketplace CLI for Marketplace refresh and plugin installation;
- the existing AI_Skills CLI and managed install manifests for project/profile consumers;
- Bridge Kit canonical CLI for Host Policy and Bridge-owned project/runtime behavior;
- workflow-core for complex-task delivery semantics;
- target domain plugins for domain correctness.

No top-level plugin, daemon, watcher, inventory database, machine registry, ledger, second authorization system, or adaptation state machine is introduced.

## 2. Reality check

Current repository release is 5.0.7. AI Skills Maintainer is ai-skills-core 0.4, workflow-core is 0.3, and Bridge Kit is 0.8.5.

The current ai-skills-core generated payload contains three skills: project-skill-installer, ai-skills-repository-maintainer, and skill-library-analysis. The repository maintainer is explicitly scoped to maintaining AI_Skills_Collection itself. The project installer is explicitly scoped to project-local profile installation. Neither currently owns machine-wide stack synchronization.

Existing AI_Skills CLI already supplies useful lower-level mechanisms. In particular, ai-skills update can reapply a prior managed install from .ai-skills-collection-manifest.json and can scan caller-specified bounded roots with a depth limit. That capability should be reused rather than reimplemented.

Bridge Kit already owns machine Host Policy through ai-bridge host install/status/validate, project Lite through ai-bridge init/validate, Review through reviewed-handoff install/validate, and other optional runtime layers through their own canonical commands. It also exposes ai-bridge where and production plugin replay. Maintainer must call those surfaces rather than reproduce their logic.

A critical current gap is formal-release addressing. AI_Skills currently has no semantic release tags for 5.x; its tags are archival. Bridge semantic tags stop before the current 0.8.5 release. Meanwhile AI_Skills README currently configures the Codex Git marketplace from main. This cannot satisfy the requested rule that normal “update” must never consume unreleased main commits.

The current formal release commits are identifiable from closure evidence today (AI_Skills 5.0.7 at ae294c6093054b78c3e6f590f562bf06aaefb1f6; Bridge 0.8.5 release commit d27259d6706dee951dc0c0ede8c9b03c65f55ca3), but a daily updater must not depend on historical closure-document archaeology.

## 3. External reality check

Current OpenAI Codex plugin tooling supports:

- codex plugin list, including JSON output and installed version/source information;
- codex plugin marketplace add/list/upgrade/remove;
- Git-backed marketplace sources pinned to a Git ref;
- codex plugin add for installing or reinstalling a plugin from a configured marketplace.

OpenAI documentation also states that installed local-marketplace plugins are materialized into the Codex plugin cache rather than loaded directly from the marketplace source. OpenAI’s current plugin update reference therefore refreshes the marketplace/source, reinstalls the plugin, and uses a new thread/session as the safe boundary for loading the updated plugin.

Codex instruction discovery is also session-bound: global and project AGENTS instructions are assembled when a run/session starts. Updated global instructions therefore require a new run/session to be guaranteed active.

Sources checked:

- https://developers.openai.com/zh-Hans/plugins/build/plugins
- https://developers.openai.com/zh-Hans/docs/agent-configuration/agents-md
- https://github.com/openai/codex/blob/main/codex-rs/cli/src/plugin_cmd.rs
- https://github.com/openai/codex/blob/main/codex-rs/cli/src/marketplace_cmd.rs
- https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/installing-and-updating.md

Adopted implication: use official Codex plugin commands and a new session boundary; do not hand-edit Marketplace config as the normal updater implementation.

## 4. Alternatives considered

### A. Expand ai-skills-repository-maintainer only

Rejected as the main route. It is currently source-authoritative for maintaining the central repository and formal plugin refinement. Making it also own arbitrary machine synchronization would collapse two distinct triggers and encourage a giant skill.

### B. Expand project-skill-installer

Rejected. It is intentionally project-local, currently operates on profiles and repo-local AGENTS/skills, and has no authority over Marketplace, Bridge, Host Policy, or formal repository releases.

### C. Add a new machine/environment update skill and implement all mechanics there

Partially adopted, but only as a thin entry skill. A monolithic implementation would duplicate official Codex plugin management, AI_Skills CLI logic, and Bridge Host logic.

### D. Thin Maintainer orchestrator delegating to canonical owners

Selected. One new internal machine-update skill supplies discovery, release resolution, route selection, authorization classification, ordered delegation, and reporting. Existing owner CLIs perform the actual mutations.

### E. Documentation-only templates around existing commands

Rejected as too weak. The user would still have to discover versions, paths, component lists, and adaptation templates. That fails the required normal entry.

## 5. Capability ownership

AI Skills Maintainer owns:

- interpreting the short update request;
- discovering current-machine state;
- resolving the latest formal release channel;
- deciding which existing owner must act;
- planning a bounded mutation set;
- invoking canonical owner commands;
- checking should-not-change surfaces;
- reporting completed, partial, reload-required, no-op, or unsupported states.

AI Skills Maintainer does not own:

- Bridge Host implementation or Bridge project runtime implementation;
- workflow-core task-delivery semantics;
- domain correctness of presentations, writing, statistics, medical imaging, bioinformatics, and similar plugins;
- a new persistence/state service.

Bridge Kit continues to own Host Policy and Bridge runtime behavior. workflow-core continues to own complex task delivery. Target plugins continue to own professional/domain behavior.

## 6. Proposed plugin structure

Add exactly one new source skill inside ai-skills-core, tentatively named ai-research-stack-updater. The name is internal; the user continues to invoke AI Skills Maintainer.

The new skill contains the common algorithm:

1. normalize the requested target;
2. discover machine/Codex/plugin/source state;
3. resolve formal release;
4. classify route;
5. preflight mutations, dirty work, and authorization;
6. delegate to canonical owners;
7. verify;
8. produce a concise report.

Keep route-specific detail in three internal references bundled with that skill:

- single-plugin update;
- major stack/workflow update;
- Bridge/Host update.

Do not create three independently triggered update skills. That would add routing ambiguity without creating three independent user capabilities.

Existing project-skill-installer and ai-skills-repository-maintainer remain in the plugin and keep their current direct responsibilities. Their descriptions may receive only the minimal boundary clarification required to prevent overlap.

The generated ai-skills-core payload and Marketplace config must expose the new skill and update the default prompts so “Update presentations”, “Sync this machine”, and “Update AI Skills” are first-class normal-entry examples.

## 7. Formal release resolution

### 7.1 Stable release channel

Normal update requires a canonical Git ref that advances only when a formal release is closed. V1 proposes a lightweight release branch named release for both AI_Skills_Collection and Bridge Kit.

Properties:

- main remains the development/integration branch;
- release points to the newest formally released commit;
- advancing release is fast-forward-only and is performed by formal release closure, never by daily Maintainer update;
- evidence-only, reviewed-branch, candidate, or unreleased main commits never advance release;
- normal Codex Marketplace installation tracks the release ref, not main;
- development updates are allowed only when the user explicitly asks for main/development.

This is one Git pointer, not a release database or state machine.

Bootstrap anchors for the first implementation are the already closed releases listed in section 2. No release branch is created by this Planner task.

### 7.2 Why not infer release from VERSION on main

VERSION alone is insufficient. A version can be set before final release closure, and later unreleased commits can keep the same version. Likewise, a dated changelog heading does not provide a durable source ref by itself. The updater must have an addressable release source.

### 7.3 Version truth at the release ref

At the resolved release ref, Maintainer verifies internal agreement among:

- repository VERSION, setup/package version, registry and README where applicable;
- scripts/codex_marketplace_config.json plugin versions;
- target plugin changelog latest released entry;
- generated plugin payload version;
- Bridge package version and CHANGELOG for Bridge updates.

If these disagree, fail closed as RELEASE_METADATA_INCONSISTENT. Do not ask the user to choose a version.

## 8. Discovery strategy

Discovery is machine-local and bounded.

Always discover without user input:

- hostname / platform;
- current user;
- HOME;
- CODEX_HOME from explicit environment/configured identity, otherwise canonical default;
- codex executable and version;
- configured Marketplace roots/sources through codex plugin marketplace list --json;
- installed/available plugin identity and versions through codex plugin list --json --available.

AI_Skills source discovery:

- prefer the configured Marketplace snapshot and installed plugin metadata for plugin updates;
- discover a canonical local AI_Skills checkout only when source/CLI/repository adaptation is actually needed;
- validate Git origin, current ref, ancestry/freshness and dirty paths;
- do not ask for a path until bounded discovery proves no usable source exists.

Bridge discovery only when the selected route needs it:

- locate ai-bridge executable;
- use ai-bridge where to identify the runtime/import root;
- verify package version;
- identify a canonical Git source only when Bridge source update is necessary;
- read host status and use host validate for Host truth.

Potential project consumers are discovered only when the release delta says consumer adaptation may be required. Allowed bounded sources are:

- current project/repository;
- existing AI_Skills managed manifests;
- already known workspace roots supplied by real Codex/project or Bridge state when available;
- canonical Git checkouts reachable from those known roots;
- Git worktrees of an already identified repository.

Do not scan /, an entire home directory, network mounts, or every filesystem for repositories.

## 9. Update routing

There are three mutation routes. “Sync this machine” is a scope/composition mode, not a fourth mutation engine.

### Route A — single plugin

Used when the target release delta is isolated to a central plugin/profile.

Actions:

- refresh the formal AI_Skills Marketplace release channel;
- resolve the target plugin’s latest released version;
- reinstall/update that target plugin only through official Codex plugin management;
- update a relevant profile only if the release contract requires it;
- do not mutate Bridge, Host, unrelated plugins, or project repos by default.

Refreshing the Marketplace catalog may expose newer available versions of other plugins, but they must not be reinstalled unless the request or dependency contract requires them.

### Route B — major stack/workflow

Used when the formal release delta explicitly crosses layers, for example workflow-core plus Bridge/Host or release-required consumer refresh.

Maintainer reads the formal release delta before mutation, expands the component set only to declared/necessary companions, preflights all effects, then delegates in dependency order.

“Update workflow-core” does not automatically mean Route B. It becomes Route B only when the formal release being installed has an actual cross-layer requirement.

### Route C — Bridge / Host

Maintainer remains the user entry. Bridge-owned mutations are executed through Bridge’s canonical implementation:

- package/source update uses the formal Bridge release source and existing safe Git/source rules;
- Host changes use ai-bridge host install and ai-bridge host validate;
- Lite/Review/Persistent Run/other project consumers use their corresponding ai-bridge install/validate commands only when the release delta requires them.

Maintainer never copies Host Policy generation or validation logic.

### Machine sync composition

“Sync this machine” reconciles the currently participating stack plus required companions. It does not install every domain plugin or every optional Bridge layer. It updates what is installed/consumed on this Codex identity and what a formal release requires.

## 10. Selective repository adaptation

Repository adaptation is opt-in by evidence, not by enumeration.

A candidate repo is mutated only if at least one condition is proven:

- stale AI_Skills managed profile/plugin pin;
- tracked obsolete Lite/Reviewed Handoff/other Bridge consumer that the release explicitly requires refreshing;
- repo-local copied/forked generic rule now conflicting with central behavior;
- stale or broken locator;
- repo AGENTS override that defeats the newly released global behavior;
- explicit formal release requirement for consumer refresh.

For AI_Skills managed consumers, prefer the existing manifest-driven ai-skills update operation against the exact discovered manifest. Do not regenerate project configuration from memory.

For Bridge consumers, call the corresponding Bridge canonical install/validate command.

If a normal repo already consumes the behavior through Host Policy and the central installed plugin, record NO_REPO_ADAPTATION_REQUIRED and leave it byte-for-byte untouched. Preserve all repo-specific scientific, safety, privacy, deployment, design/Figma, and device/server rules.

## 11. Dirty work and Git behavior

Inherit 056 Source Discovery.

- prefer existing canonical checkout;
- fetch and verify origin/ref/freshness before deciding;
- unrelated dirty files do not automatically block update;
- if a safe fast-forward does not overlap dirty paths, proceed without stash/reset/restore;
- never stash, reset, checkout-away, or restore user work;
- never remap remote;
- never install normal production from a reviewed/temporary worktree;
- clone only when no usable local source exists.

If dirty overlap creates genuine ownership ambiguity, ask one bounded HUMAN_ONLY question identifying the exact conflicting paths and the minimal decision. Do not turn every dirty tree into a gate.

If a checkout is intentionally on a development ref ahead of the formal release, do not downgrade/reset it. Prefer the independent formal Marketplace/runtime source where available; otherwise report the exact development-source condition rather than pretending a formal update occurred.

## 12. Self-update and session reload

The current ai-skills-core 0.4 does not contain this orchestration capability, so the first release requires one bootstrap migration. That bootstrap may configure the formal release Marketplace channel and install the first capability-bearing Maintainer release.

After that release:

1. the old loaded Maintainer session resolves the newer formal release;
2. it refreshes the release Marketplace and reinstalls ai-skills-core through official Codex plugin management;
3. it verifies the installed cache/catalog version;
4. it does not claim the current session hot-reloaded;
5. it returns UPDATED_RELOAD_REQUIRED and instructs the user to open a new Codex session;
6. release acceptance uses a genuinely fresh Codex process/session to prove that the new Maintainer payload loads.

When Bridge production plugin replay is available, use it as the strongest automated fresh-process evidence. If it is not available on a daily machine, installed-cache verification plus an explicit reload-required state is truthful; the current session must not claim normal-entry activation.

## 13. Authorization boundary

Normal discovery, public-source fetch, formal release resolution, Marketplace refresh/reinstall, required dependency update, and safe bounded validation are AGENT_RESOLVABLE within the user’s explicit “update <target>” request.

Use one minimal HUMAN_ONLY gate only for:

- new provider/account/credential;
- private external transfer;
- destructive operation;
- a new production deployment or other live-global mutation outside the reasonable update scope;
- dirty user work with unresolved ownership/overlap;
- two genuinely different product semantics that release/source contracts cannot resolve.

Do not ask for paths, versions, commits, CODEX_HOME, Bridge location, obvious required dependencies, or whether an ordinary central plugin should be reinstalled.

## 14. Ordered execution and recovery

Do a complete preflight before mutation: target release, routes, candidate consumers, dirty conflicts, permissions, and should-not-change set.

Then execute in dependency order:

1. formal AI_Skills release-channel refresh and required central plugin installation;
2. Bridge formal update and Bridge-owned Host validation when required;
3. exact selective repo adaptations;
4. installed-version and should-not-change checks;
5. fresh-session verification when available;
6. concise report.

Do not add transactional state machinery. Each owner command should remain idempotent. If a later step fails, preserve already valid released updates, report PARTIAL_UPDATE with the failed owner/step, and rerun from discovery. Do not automatically roll back with reset/stash.

## 15. User-visible states

Primary output should be short and semantic:

- UPDATED
- UPDATED_RELOAD_REQUIRED
- ALREADY_CURRENT
- PARTIAL_UPDATE
- DEVELOPMENT_SOURCE_PRESENT
- RELEASE_METADATA_INCONSISTENT
- UNKNOWN_OR_UNRELEASED_TARGET

Internal audit detail may be retained in normal command output/evidence, but the user should see version deltas, components changed, repo adaptation count, Host validation outcome, and reload requirement.

Never say “all repos are current” if bounded discovery did not establish that scope. Prefer “No known affected local consumer required adaptation within the bounded discovery scope.”

## 16. Capability Gate Matrix

The gates are grouped by independent failure semantics, not by the number of scenarios.

### G1 — Short request, target and formal-release routing

Proves one normal AI Skills Maintainer invocation can handle:

- a single-plugin short request;
- a no-op already-current request;
- unknown/unreleased target;
- main newer than formal release without leaking main into the update;
- workflow target that stays isolated unless the release delta requires Route B.

Must show that ordinary facts are discovered without HUMAN_ONLY prompts.

### G2 — Marketplace/install/self-update and fresh-session consumption

Proves:

- stale Marketplace snapshot is refreshed from the formal release channel;
- target plugin is reinstalled while unrelated installed plugins remain unchanged;
- stale installed version is corrected;
- ai-skills-core can update itself after the bootstrap release;
- current session reports reload-required rather than fake hot reload;
- a fresh Codex process/session actually loads the final target release.

This gate must use the same final candidate that is released.

### G3 — Cross-layer Bridge/Host delegation

Proves a release delta that genuinely requires Bridge/Host:

- expands to the correct components automatically;
- invokes Bridge canonical source/runtime and host install/validate surfaces;
- does not duplicate Host implementation in AI_Skills;
- handles already-current Bridge/Host as a no-op;
- preserves unrelated optional Bridge layers.

### G4 — Selective consumers and source/dirty safety

Use at least two repos in the same test surface:

- one genuinely stale local consumer that must adapt;
- one normal repo that must remain untouched.

Also cover an unrelated dirty canonical checkout that can safely proceed and an overlapping dirty case that triggers exactly one bounded gate. Verify repo-specific AGENTS/scientific/privacy/design rules are unchanged.

### G5 — Failure, recovery, authorization and should-not-change

Inject a bounded failure after an earlier safe step and prove:

- truthful PARTIAL_UPDATE;
- no destructive rollback;
- rerun converges;
- no duplicate question after one bounded authorization;
- no unrelated plugin/profile/repo mutation;
- concise user-facing summary.

### Platform coverage

Run the same capability contract on representative Windows/WSL, macOS, and Linux/server environments. Platform-specific discovery commands/paths may differ; the behavioral contract must not. If a platform cannot be directly exercised before release, do not claim it as verified.

## 17. Version and release decision

This is not a maintenance-only patch. It creates a new normal repository-level user capability: one installed Maintainer entry can synchronize the machine stack without the user supplying versions, paths, component lists, or adaptation templates.

Planned release decision, conditional on Critic approval and final gates:

Repository bump decision: MINOR
Reason: new repository-level installation/environment/distribution capability that supports a previously unsupported normal user task.
Repository: 5.0.7 -> 5.1.0

Affected plugins:
- ai-skills-core: 0.4 -> 0.5
  Reason: new user-facing machine update/orchestration behavior.
- workflow-core: NO_BUMP
  Reason: consumed as an existing owner; no production behavior change is required by this plan.
- all domain plugins: NO_BUMP unless implementation changes their production behavior, which is outside this plan.

Bridge Kit: NO_BUMP under this plan if only a formal release-channel ref is established and existing canonical CLI behavior is reused. Any Bridge production-source change requires an explicit amended scope and its own version decision.

README closure is mandatory. The implementation release must update README to make AI Skills Maintainer + short target the normal update UX, replace main-based normal Marketplace update guidance with the formal release channel, document the one-time bootstrap, and state the new-session boundary.

## 18. Should-not-change

- compatibility slug ai-skills-core;
- display name AI Skills Maintainer;
- workflow-core ownership of task-delivery semantics;
- target domain plugin ownership;
- Bridge Host/runtime implementation;
- existing project-skill-installer direct project use;
- repo-specific AGENTS and local product/science/safety constraints unless an explicit stale managed block is proven;
- unrelated plugin installed versions during Route A;
- no new top-level plugin or background service;
- no routine Planner/Critic or full Capability Gates for daily machine updates.

## 19. Non-goals

- central inventory of all user machines or repos;
- automatic cross-machine orchestration;
- remote deployment of Codex environments;
- replacing package managers, Git, Codex plugin manager, or Bridge CLI;
- rewriting all repo AGENTS;
- automatically migrating every historical Bridge consumer;
- using current main as the default release target;
- silently hot-reloading the current Codex session.

## 20. Execution boundary

This V1 is design only. No production source, generated plugin payload, Marketplace source, Host state, Bridge runtime, release branch, plugin version, or repository version is changed by this Planner package.

Implementation may start only after an independent Critic PASS on this exact V1 package and a later user-authorized kickoff. If Critic rejects the release-channel design or identifies a simpler formal-release locator that satisfies the same semantics, Planner should amend this proposal before any implementation.
