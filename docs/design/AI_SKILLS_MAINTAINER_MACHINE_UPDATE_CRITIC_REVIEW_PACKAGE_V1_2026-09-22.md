# AI Skills Maintainer machine update orchestration — Critic Review Package V1

Date: 2026-09-22  
Review stage: architecture + execution-package design review  
Target repo: `YuukiAS/AI_Skills_Collection`  
Target plugin/domain: `ai-skills-core` / AI Skills Maintainer  
Task key: `ai-skills-core--machine-update-orchestration`  
Source branch/ref: `main`

## Review object

Please review these V1 files as one package:

1. Proposal / Plan  
   `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V1_2026-09-22.md`
2. Canonical Goal  
   `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V1_2026-09-22.md`
3. Kickoff Draft  
   `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_KICKOFF_DRAFT_V1_2026-09-22.md`

The current package is design-only. No production source, generated payload, plugin/repository version, Marketplace source configuration, Bridge runtime/source, Host Policy, remote release ref, paid API, automation, Executor or Reviewed Handoff implementation branch has been changed/started by this Planner round.

## User capability being reviewed

The user wants one stable normal entry on every actual Codex machine/server:

`AI Skills Maintainer + short update target`

Examples:

- `update presentations`
- `update workflow-core`
- `update AI Skills`
- `sync this machine`

The user should no longer need to supply versions, commits, repository paths, Bridge paths, `CODEX_HOME`, local repo inventories, or adaptation templates.

The Maintainer should discover the current machine, resolve the latest formal release, select the minimum required update route, delegate to existing owners, selectively adapt only affected local consumers, verify the next normal Codex entry, and return a short user-facing report.

## Current verified baseline

From AI_Skills_Collection current main:

- repository release: `5.0.7`
- `ai-skills-core`: `0.4`
- `workflow-core`: `0.3`
- compatibility slug remains `ai-skills-core`
- display name remains `AI Skills Maintainer`
- current generated ai-skills-core payload contains:
  - `project-skill-installer`
  - `ai-skills-repository-maintainer`
  - `skill-library-analysis`
- current `project-skill-installer` is project-local and still asks for the central checkout path if its narrow discovery fails;
- current repository maintainer owns central-repo/plugin refinement closure, not machine-wide stack update;
- current AI_Skills CLI already has manifest-driven `update` and bounded `--scan-root/--scan-depth` support that V1 proposes to reuse.

056 final closure verifies the released stack baseline and the normal Bridge/Host identity used there.

From Bridge Kit latest main:

- package/runtime version source is `0.8.5`;
- Host Policy is owned by `ai-bridge host install/status/validate`;
- Lite is owned by `ai-bridge init/validate`;
- Review and other optional consumers have their own canonical install/validate surfaces;
- `ai-bridge where` provides the installed kit path;
- production plugin replay exists for bounded fresh Codex plugin evidence;
- Bridge source/Host implementation is not to be copied into AI_Skills.

## Key source reality that drove V1

The central technical problem is not merely prompt routing. The desired stable-update semantics currently lack a durable addressable "latest formal release" channel.

Observed repository reality:

- AI_Skills current 5.x formal releases are represented by VERSION/changelog/closure commits, but the repository does not currently have semantic 5.x release tags;
- existing AI_Skills tags are archival task tags;
- Bridge semantic tags do not reach the current 0.8.5 release;
- AI_Skills README currently tells users to configure the Git Marketplace at ref `main`;
- therefore ordinary `marketplace upgrade` against `main` cannot guarantee "formal release only" once main advances beyond the release commit.

V1 solves this with one lightweight moving Git ref, `release`, in each of AI_Skills and Bridge. It is advanced only by formal release closure and is fast-forward-only. Normal updates track this ref; development updates use main only on explicit request.

Critic should challenge this choice if a simpler or more mature current mechanism can provide the same stable semantics without creating another operational failure mode.

## External reality check performed by Planner

Planner independently checked current OpenAI/Codex sources on 2026-09-22.

Verified:

- official plugin packaging docs support adding Git Marketplace sources with `--ref`, and expose `marketplace list/upgrade/remove`;
- current Codex CLI source exposes `codex plugin add`, `codex plugin list --json --available`, and Marketplace add/list/upgrade/remove;
- the official plugin-creator update reference instructs reinstalling a changed plugin and using a new thread/session as the safe boundary for picking up the updated plugin;
- official AGENTS.md docs state the instruction chain is rebuilt once per run / at the start of each TUI session.

Planner sources:

- `https://developers.openai.com/plugins/build/plugins`
- `https://learn.chatgpt.com/docs/agent-configuration/agents-md`
- `https://github.com/openai/codex/blob/main/codex-rs/cli/src/plugin_cmd.rs`
- `https://github.com/openai/codex/blob/main/codex-rs/cli/src/marketplace_cmd.rs`
- `https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/installing-and-updating.md`

Adopted implication: official Codex plugin/Marketplace commands should perform installed-plugin mutations, and V1 must require a fresh-session verification boundary instead of claiming hot reload.

## Planner route comparison

V1 explicitly compared:

- expanding `ai-skills-repository-maintainer`;
- expanding `project-skill-installer`;
- a new machine update skill with all mechanics embedded;
- a thin Maintainer orchestrator delegating to canonical owner CLIs;
- docs/templates only.

Selected architecture:

- one new internal update orchestration skill inside the existing ai-skills-core plugin;
- three internal route references, not three competing user-triggered skills;
- official Codex CLI + existing AI_Skills CLI + Bridge canonical CLI do the actual lower-level work.

This is intended to be the minimum production path that satisfies the zero-detail user request.

## Five-pass precheck summary

### Product

The new real capability is that a user can update one machine's participating AI Research Stack from one short Maintainer request, without doing component/version/path/adaptation triage manually.

A successful implementation must prove the next normal fresh Codex entry actually consumes the target release, not merely that Git/config files changed.

### Reality

Current lower-level mechanics already exist across Codex plugin management, AI_Skills manifests and Bridge CLI. The main missing layer is orchestration plus formal-release resolution and selective-consumer logic.

### Alternatives

The simpler docs/template-only route was rejected because it leaves the user doing the discovery and routing. Reimplementing all owners inside one skill was rejected as over-heavy.

### Red-team

V1 explicitly tries to prevent:

- main/evidence commits silently becoming update targets;
- Marketplace refreshed but plugin not reloaded;
- self-update claiming current-session success;
- Bridge Host logic duplicated into AI_Skills;
- mass AGENTS rewrites;
- dirty tree causing unnecessary clone/stash;
- unrelated plugin upgrades during a single-plugin request;
- consumer discovery turning into full-disk inventory;
- static test/parity PASS replacing fresh-session normal-entry proof;
- daily update accidentally invoking Planner/Critic/full release gates.

### Execution contract

Proposal, Goal and Draft Kickoff freeze the ownership boundaries, three-route model, release-channel requirement, dirty/Human Gate behavior, Gate Matrix, version decision and stop conditions.

One execution locator is intentionally not invented in this design round: the exact local worktree path must be resolved on the actual execution machine before the user sends the implementation kickoff. The proposed exact task branch is `reviewed/ai-skills-core--machine-update-orchestration`.

## Capability Gate Matrix under review

V1 consolidates the user's requested scenarios into five failure-semantic gates:

- **G1 — Short request / target / formal-release routing**  
  Includes isolated plugin, no-op, unknown/unreleased target, and main-newer-than-release behavior.
- **G2 — Marketplace/install/self-update/fresh-session consumption**  
  Includes stale Marketplace, stale install, Maintainer self-update, reload-required truthfulness, and real new-session loading.
- **G3 — Cross-layer Bridge/Host delegation**  
  Proves automatic scope expansion only when release delta truly requires it and proves Bridge owns actual runtime/Host mutation.
- **G4 — Selective consumers + source/dirty safety**  
  Requires one stale consumer to adapt, one normal repo to remain untouched, and dirty safe/overlap cases.
- **G5 — Failure/recovery/authorization/should-not-change**  
  Proves truthful partial failure, idempotent recovery, one-time Human Gate behavior, concise reporting and no collateral mutation.

Cross-platform behavior is a coverage dimension across gates, not a separate route/gate.

## Version decision under review

Planner proposes:

`Repository: 5.0.7 -> 5.1.0` — MINOR

Reason: the collection gains a repository-level installation/environment/distribution capability that 5.0.x cannot do through the normal user entry: one Maintainer request can synchronize the current machine and route required adaptations without user-supplied versions/paths/components/templates.

Affected plugin:

`ai-skills-core: 0.4 -> 0.5`

Reason: this is a new user-facing Maintainer workflow/capability.

Proposed no-bump:

- `workflow-core`: unchanged owner behavior;
- target domain plugins: unchanged;
- Bridge Kit: unchanged if implementation only consumes existing Bridge behavior and establishes the release ref.

Any actual Bridge production-source behavior change must return to Planner/Critic with a separate version decision.

## Specific Critic questions

Please independently decide:

1. Is the thin-orchestrator ownership split correct, or is there an even simpler current implementation that still gives the user a true zero-detail normal entry?
2. Is a moving fast-forward-only `release` ref the right minimal formal-release contract for both repos, or should V1 use another current source of formal-release truth?
3. Is the three-route model sufficient without hiding a genuinely distinct fourth user capability?
4. Is `sync this machine` correctly treated as a composition scope rather than a new route?
5. Does bounded consumer discovery avoid both under-discovery and machine-wide inventory creep?
6. Is the self-update/reload design honest about old-session limitations and strong enough to prove the new normal entry?
7. Are the Human Gate and dirty-work rules faithful to 056?
8. Are G1-G5 distinct and sufficient, or are any redundant/missing?
9. Is the proposed repository MINOR and ai-skills-core `0.4 -> 0.5` decision correct under the version policy?
10. Does the Kickoff Draft preserve user authorization boundaries rather than pre-authorizing unknown live-global effects?
11. Does anything in V1 accidentally create a second update engine/state machine or duplicate Bridge ownership?
12. Does the plan preserve existing project-skill-installer/repository-maintainer behavior and unrelated plugins/repos?

## Critic response requested

Give exactly one formal design-stage result:

- `PASS`, if the V1 Proposal/Goal/Kickoff are coherent enough to freeze for implementation after current-user kickoff; or
- `REVISE`, with stable blocker IDs, direct source evidence, causal risk and minimum closing condition.

A PASS here does not authorize implementation, creation of the execution branch/worktree, creation of remote `release` refs, Host mutation, paid API, automation, or deployment. Those remain future user-authorized execution effects.
