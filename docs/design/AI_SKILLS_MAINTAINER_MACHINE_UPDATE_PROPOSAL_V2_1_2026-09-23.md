# AI Skills Maintainer machine update orchestration — Proposal / Plan V2.1

Date: 2026-09-23  
Status: PLANNER_PROPOSAL_FOR_CRITIC  
Task key: `ai-skills-core--machine-update-orchestration`  
Repository: `YuukiAS/AI_Skills_Collection`  
Normal user entry: **AI Skills Maintainer**  
Compatibility slug: `ai-skills-core`

V1 Critic result: `REVISE`  
Planner response: `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PLANNER_RESPONSE_V2_1_2026-09-23.md`

## 1. Product conclusion

AI Skills Maintainer should become the only user-facing entry for updating/adapting the AI Research Stack on one current Codex machine/server.

The normal user input stays short:

- `update presentations`
- `update workflow-core`
- `update research-writing`
- `update AI Skills`
- `update Bridge Kit`
- `sync this machine`

The user does not supply versions, commits, checkout paths, `CODEX_HOME`, Bridge root, local repo inventory, adaptation templates, or a component dependency list.

Maintainer discovers the machine/runtime state, resolves the latest formal release, chooses the minimum required route, delegates actual mutations to existing owners, selectively updates only managed affected consumers, verifies the next real normal entry, and returns a short report.

The architecture remains deliberately thin. It does not create another package manager, workflow engine, daemon, watcher, inventory database, machine registry, ledger, authorization system, or adaptation state machine.

## 2. Current verified baseline

AI_Skills_Collection latest main was revalidated at `338add2d7ac002a0201a924be3a0ec2818b777c7`.

Production baseline remains:

- repository release: `5.0.7`;
- `ai-skills-core`: `0.4`;
- `workflow-core`: `0.3`;
- display name: `AI Skills Maintainer`;
- current generated ai-skills-core payload contains:
  - `project-skill-installer`;
  - `ai-skills-repository-maintainer`;
  - `skill-library-analysis`.

Current AI_Skills CLI already has manifest-driven `update` and bounded `--scan-root/--scan-depth` support. V2 reuses it rather than implementing a second consumer installer.

Bridge Kit latest main was revalidated at `b76a7da0fdbb4f92205b0b168241c084c1489c6f`; runtime/package version remains `0.8.5`. Formal release commit is `d27259d6706dee951dc0c0ede8c9b03c65f55ca3`; subsequent main commits are docs/TODO-only.

Bridge continues to own:

- `ai-bridge host install/status/validate`;
- Host Policy generation/validation;
- `ai-bridge init/validate` for Lite;
- Review/Persistent Run/other Bridge consumer install/validate;
- plugin replay/runtime implementation.

## 3. External reality check

Current OpenAI Codex behavior was rechecked on 2026-09-23.

Verified from official docs/current openai/codex source:

- Git Marketplace supports a pinned `--ref`;
- Marketplace exposes `add/list/upgrade/remove`;
- plugin management exposes `plugin add` and `plugin list --json --available`;
- changing the Git source/ref is not the same operation as ordinary marketplace refresh;
- marketplace removal fails closed when another enabled config layer owns the same marketplace;
- OpenAI's plugin update guidance uses reinstall and a **new thread/session** as the safe boundary for consuming the updated plugin;
- AGENTS/instruction discovery is assembled at run/session start, so updated global/project instructions also require a fresh run/session for guaranteed consumption.

References checked:

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/api/docs/guides/latest-model
- https://github.com/openai/codex/blob/main/codex-rs/cli/src/plugin_cmd.rs
- https://github.com/openai/codex/blob/main/codex-rs/cli/src/marketplace_cmd.rs
- https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/marketplace_remove.rs
- https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/installing-and-updating.md

Design implication: use official Codex Marketplace/plugin commands and an explicit fresh-session acceptance boundary; do not mutate Codex config files directly as the normal update path.

## 4. Alternatives and ownership decision

### A. Expand only `ai-skills-repository-maintainer`

Rejected as the single implementation. It is already the central AI_Skills source/release maintainer. Making it also own current-machine Marketplace migration, Bridge distribution, Host delegation, consumer discovery and session reload would make it a giant skill with mixed trigger semantics.

### B. Expand only `project-skill-installer`

Rejected. Its canonical owner boundary is AI_Skills-managed project/profile installation. It should remain the lower-level owner for manifest-managed consumers.

### C. One new updater skill containing every mechanic

Rejected as too heavy. It would duplicate existing Codex, AI_Skills and Bridge implementations.

### D. Thin orchestrator + owner-specific internal maintenance skills

Selected.

The `ai-skills-core` plugin contains the user-facing maintenance capability, but the internal responsibilities are separated:

1. **new `machine-update-orchestrator`**
   - short request interpretation;
   - discovery;
   - formal release resolution;
   - scope/route composition;
   - authorization classification;
   - ordered delegation;
   - final verification/reporting.

2. **existing `ai-skills-repository-maintainer`**
   - AI_Skills repository/plugin release/source maintenance;
   - generated parity;
   - versions/changelogs;
   - AI_Skills formal `release` ref production.

3. **existing `project-skill-installer`**
   - AI_Skills manifest/profile/managed-block installation and refresh.

4. **new `bridge-kit-maintainer`**
   - Bridge Kit source/distribution/version maintenance;
   - Bridge formal release resolution/channel maintenance;
   - canonical checkout and editable-install refresh;
   - runtime identity/version verification;
   - delegation of Host/Lite/Review/Persistent Run behavior to the existing `ai-bridge` CLI.

5. **existing `skill-library-analysis`**
   - skill/plugin overlap and library-structure analysis only.

This satisfies the user's new requirement that the same plugin can adapt **skills/profiles, central plugins, and Bridge Kit version** without making Bridge Kit itself a second maintenance control plane.

### E. Put full Bridge release/update machinery into Bridge Kit

Rejected. Bridge should stay focused on runtime/Host/handoff implementation. The Maintainer may call Bridge's canonical implementation, but distribution/version orchestration belongs in AI Skills Maintainer.

## 5. Public UX and normal entry

Normal entry is always explicit:

`Use AI Skills Maintainer. <short target>`

Examples and expected interpretation:

- `update presentations` -> isolated target unless formal release metadata declares companions;
- `update workflow-core` -> isolated unless the formal release declares cross-layer impact;
- `update Bridge Kit` -> Bridge distribution/version route; Host/project consumers only when the Bridge release impact requires them;
- `update AI Skills` -> central repository/Marketplace/Maintainer path;
- `sync this machine` -> reconcile the **currently participating installed stack** plus required companions; do not install every plugin or every optional Bridge layer.

The user never selects Route A/B/C.

## 6. Internal route model

There remain exactly three mutation routes.

### Route A — isolated AI_Skills plugin/profile

For central plugins such as presentations, writing-style, research-writing, statistical-modeling, medical-imaging.

Default mutation scope:

- formal AI_Skills Marketplace source;
- requested plugin;
- relevant AI_Skills managed profile/consumer only if required.

Default non-scope:

- Bridge;
- Host Policy;
- unrelated plugins;
- arbitrary project repos.

### Route B — cross-layer stack/workflow composition

Used only when authoritative formal release metadata explicitly declares required companions or managed-consumer refresh.

Possible owners may include:

- AI_Skills central plugins;
- Bridge Kit distribution;
- Bridge Host;
- Bridge managed consumers;
- AI_Skills managed consumers.

The route composes existing owners; it does not create a new cross-stack runtime.

### Route C — Bridge Kit distribution/runtime update

The new `bridge-kit-maintainer` owns Bridge **maintenance/distribution**.

It may:

- locate `ai-bridge`;
- identify runtime/import/source root;
- resolve current/formal version;
- safely fast-forward the canonical Bridge checkout to the formal release when ancestry/dirty ownership permit;
- refresh the editable package/entry point from that source;
- verify the runtime path/version;
- call canonical Bridge install/validate surfaces when the formal release impact requires them.

It may not reimplement Host Policy, Lite, Review, Human Gate, plugin replay or other Bridge runtime logic.

`sync this machine` is a composition over these three routes, not a fourth route.

## 7. Formal release channel

### 7.1 Consumer contract

Normal update must not use arbitrary `main`.

V2 retains a moving, fast-forward-only Git branch named:

`release`

in:

- `YuukiAS/AI_Skills_Collection`;
- `YuukiAS/GPT_Codex_AI_Bridge_Kit`.

Normal update resolves from `release`.

Explicit `main`/development update is allowed only when the user asks for a development build, and the result is labeled as development.

### 7.2 Producer contract

The Critic correctly identified that V1 only defined the consumer.

V2 centralizes the producer contract in AI Skills Maintainer rather than duplicating a second maintenance implementation in Bridge.

Canonical producer owners:

- AI_Skills `release` -> `ai-skills-repository-maintainer`;
- Bridge `release` -> `bridge-kit-maintainer`.

Only formal release closure may advance a `release` ref.

Required conditions:

1. target is the exact formally closed release commit;
2. source repo identity/origin is verified;
3. target is a fast-forward descendant of current `release` if the ref exists;
4. no reviewed/candidate/evidence-only commit is accepted as target merely because it is newer;
5. remote `release` is verified after push;
6. later main docs/evidence commits do not move `release`;
7. ordinary machine updater is read-only with respect to `release`;
8. non-fast-forward or metadata mismatch fails closed.

No release daemon/watcher/registry/ledger is added.

A Bridge-side locator is a **mandatory implementation requirement**. It must be added only to `YuukiAS/GPT_Codex_AI_Bridge_Kit/AGENTS.md`, because that is the existing repository entry automatically consumed by Codex during Bridge maintenance/release work.

The locator must state, in minimal natural language, all of the following and nothing broader:

- Bridge runtime / Host / Lite / Review / Control / Persistent Run implementation authority remains in Bridge Kit;
- formal Bridge distribution/version closure, including advancement of the moving `release` ref, is owned by **AI Skills Maintainer** (`ai-skills-core` -> internal `bridge-kit-maintainer`);
- a Bridge formal release is not distribution-complete until it has handed off to that owner for formal distribution closure;
- the canonical fast-forward-only producer contract remains single-sourced in AI_Skills_Collection and is **not** duplicated into Bridge.

Do not duplicate this locator into Bridge README, QUICKSTART or CHANGELOG merely for redundancy. Do not add a Bridge-side updater, release engine, state machine, watcher or second policy copy.

## 8. Authoritative update impact

V1's phrase “release delta explicitly requires” was underspecified.

From the first capability-bearing Maintainer release onward, the authoritative formal release entry is:

`<formal release ref>/CHANGELOG.md -> matching release section`.

Cross-layer effects are declared by a small existing-document subsection only when needed:

### Update impact

- Required companions: ...
- Required managed consumer refresh: ...

Rules:

- absence of `Update impact` = isolated by default;
- root release entry owns mutation-scope expansion;
- component/plugin changelogs may explain detail but may not enlarge the root-declared scope;
- Bridge root changelog owns Bridge release impact on Host/Bridge managed consumers;
- a coordinated AI_Skills stack release may name a Bridge version/Host requirement in the AI_Skills root release entry;
- arbitrary diffs, commit messages, TODOs, comments or model inference cannot authorize cross-layer mutation;
- contradictory release metadata fails closed as `RELEASE_METADATA_INCONSISTENT`.

Legacy current 5.0.7 / Bridge 0.8.5 are a bounded bootstrap compatibility case backed by 056 final closure. Future releases follow this contract.

## 9. One-time Marketplace bootstrap

Current documented AI_Skills Marketplace installations use the Git ref `main`. Changing that source identity to `release` is not an ordinary marketplace upgrade.

V2 therefore freezes a one-time per-Codex-identity bootstrap for pre-capability installs.

### Eligibility

Bootstrap applies only when:

- installed Maintainer is pre-capability (current baseline 0.4);
- configured Marketplace is the expected AI_Skills Git repository;
- its ref is `main`;
- sparse paths match the known generated Marketplace/payload paths;
- the owning config layer is user-mutable.

Any mismatch is diagnosed; it is not silently rewritten.

### Preflight

Before removal:

- list configured marketplaces as structured data;
- capture exact Marketplace name/source/ref/sparse paths/config owner;
- capture installed/enabled AI_Skills plugin state;
- verify remote `release` exists;
- verify the formal release payload contains the capability-bearing Maintainer;
- record the exact legacy source metadata needed for recovery.

### Mutation

Use official Codex commands:

1. remove the exact legacy user-owned Marketplace source;
2. add the same AI_Skills Marketplace source at `release` with the same sparse paths;
3. verify Marketplace identity/ref;
4. reinstall `ai-skills-core`;
5. reinstall the explicitly requested target when applicable;
6. verify previously installed unrelated plugin state was not lost solely by the Marketplace migration.

If another installed plugin loses prior installed state as a direct side effect of source replacement, restoring that prior installed state is part of bootstrap recovery; this is not permission to upgrade unrelated plugins opportunistically.

### Recovery

If the new source cannot be installed after removal:

- restore the exact captured `main` source;
- verify restoration;
- report `PARTIAL_UPDATE`;
- do not edit config.toml directly, do not invent another Marketplace name, and do not continue with a half-migrated identity.

If the source is owned by a non-user/system/config layer and current authority cannot remove it, return an exact unsupported/authority result and do not mutate.

### Bootstrap boundary

The old 0.4 plugin is not claimed to possess this new capability.

The first rollout is an explicit one-time bootstrap installation/migration step per Codex identity. From the first capability-bearing release onward, normal self-update is handled by AI Skills Maintainer itself.

## 10. Discovery strategy

Discovery is machine-local, bounded and route-sensitive.

Always discover:

- platform/hostname;
- current user;
- HOME;
- current CODEX_HOME;
- Codex executable/version;
- configured Marketplace source/ref/owning layer;
- installed and available plugin identities/versions.

Discover AI_Skills canonical source only when source/CLI/profile adaptation requires it.

Verify:

- origin;
- current branch/ref;
- remote freshness;
- ancestry;
- dirty-path ownership.

Discover Bridge only when Bridge is requested or an authoritative update impact requires it:

- resolved `ai-bridge` executable;
- `ai-bridge where`;
- runtime/import root;
- package/runtime version;
- canonical Git checkout when applicable;
- Host state only when Host is relevant.

Potential project consumers are discovered only when a release requires consumer adaptation.

Allowed discovery roots:

- current project;
- exact known managed-manifest project roots;
- Bridge-known target paths/state;
- explicit workspace roots already present in the current Codex/project environment;
- Git worktrees of an already identified repo.

Do not recursively inventory `/`, all of HOME, network mounts, or every disk.

## 11. Selective repository adaptation

Automatic mutation requires ownership provenance.

Allowed automatic mutation:

1. AI_Skills manifest-managed installs and exact AI_Skills managed blocks;
2. Bridge canonical managed consumer/templates/blocks;
3. exact migration surfaces named by the authoritative release impact with an ownership locator.

Unmanaged project text is diagnosis-only.

Do not automatically rewrite:

- unmarked project `AGENTS.md`;
- manually copied/forked rules;
- scientific rules;
- safety/privacy rules;
- Figma/design authority;
- deployment constraints;
- device/server rules;
- other project-owned text.

If an unowned rule genuinely blocks the new central behavior, report:

`REPO_OWNED_CONFLICT`

with exact repo/path/reason and request one bounded repo-owned decision or separate authorized repo task.

A normal repo that consumes the update via central plugin + Host Policy remains byte-for-byte untouched and is reported as:

`NO_REPO_ADAPTATION_REQUIRED`

within the bounded discovery scope.

## 12. Bridge Kit maintenance boundary

The new `bridge-kit-maintainer` exists because Bridge is part of the AI Research Stack being updated, but it does not make AI_Skills the owner of Bridge runtime semantics.

It owns:

- Bridge release/version discovery;
- Bridge formal distribution channel;
- safe current-machine Bridge source update;
- editable package refresh;
- runtime/version parity check;
- Bridge release-ref production at formal release closure;
- deciding which canonical Bridge command to delegate to based on authoritative update impact.

It does not own:

- implementation of Host Policy;
- Lite/Review/Control/Persistent Run behavior;
- Human Gate transport;
- plugin replay implementation;
- Bridge scientific/product semantics.

This lets the user say `update Bridge Kit` through the same Maintainer entry without adding a second updater inside Bridge.

## 13. Dirty work and source safety

Inherit 056 Source Discovery.

- prefer existing canonical checkout;
- verify origin/ref/freshness/ancestry;
- dirty does not automatically mean block or reclone;
- safe fast-forward may proceed when changed upstream paths do not overlap user-owned dirty paths;
- never stash/reset/restore/checkout-away user work;
- never remap remote;
- never use temporary/reviewed worktree as normal production installation source;
- network clone only when no usable local source exists.

If overlap produces real ownership ambiguity, ask one bounded HUMAN_ONLY question naming the exact paths.

If a canonical source is intentionally ahead/diverged for development, do not downgrade it to `release`. Use an independent formal Marketplace/runtime source where possible, otherwise report `DEVELOPMENT_SOURCE_PRESENT`.

## 14. Human Gate boundary

The user's short update request authorizes ordinary bounded update mechanics for that target.

AGENT_RESOLVABLE:

- environment/source discovery;
- public network fetch;
- release resolution;
- safe Marketplace refresh/reinstall;
- safe fast-forward within the requested formal update;
- required dependency/companion update explicitly declared by release impact;
- validation;
- managed-consumer refresh.

HUMAN_ONLY only for:

- new provider/account/credential;
- private external transfer;
- destructive operation;
- new production deployment/live-global effect not reasonably contained by the update request;
- unresolved user-owned dirty overlap;
- unowned repo rule conflict requiring a product/repo decision;
- two irreducible product meanings not resolvable from formal release metadata.

Do not ask for versions, commits, checkout paths, Bridge path, CODEX_HOME, machine repo list or obvious required companions.

Once a bounded effect is authorized, do not ask again in the same update.

## 15. Self-update and reload

After the one-time bootstrap, an old loaded capability-bearing Maintainer may:

1. refresh the `release` Marketplace;
2. resolve a newer formal ai-skills-core version;
3. reinstall ai-skills-core through official Codex plugin management;
4. verify installed cache/catalog identity.

It must not claim the current session hot-reloaded.

Return:

`UPDATED_RELOAD_REQUIRED`

and require a fresh Codex process/session.

Release acceptance must prove a fresh normal entry actually loads the target released Maintainer. Bridge plugin replay may be used when available, but source-tree SKILL reading or generated parity alone is not sufficient.

## 16. Failure and recovery

Do a full bounded preflight before mutation:

- target formal release;
- source/ref/config ownership;
- route;
- authoritative update impact;
- candidate managed consumers;
- dirty conflicts;
- authorization;
- should-not-change set.

Then execute owner operations in dependency order.

No transaction database is added.

Every owner operation should be idempotent or safely re-discoverable.

If a later step fails:

- keep already valid released updates;
- do not destructive-rollback with reset/stash;
- restore only the exact Marketplace source when the special bootstrap replacement itself failed;
- report `PARTIAL_UPDATE` with the failed owner/step;
- rerun starts from fresh discovery.

## 17. User-visible result

Primary report is concise.

Examples:

> Presentations 已从 0.3 更新到 0.4。中央安装已同步；在本次受限 discovery 范围内没有发现需要额外 adaptation 的 managed local consumer。请开启新的 Codex session 加载新版。

or:

> Workflow update 已完成。workflow-core 0.3 -> 0.4，Bridge Kit 0.8.5 -> 0.8.6，Host Policy 已由 Bridge canonical CLI 更新并验证。2 个旧 managed Lite consumer 已同步；其余已检查 repo 未修改。

Semantic result states:

- `UPDATED`
- `UPDATED_RELOAD_REQUIRED`
- `ALREADY_CURRENT`
- `PARTIAL_UPDATE`
- `DEVELOPMENT_SOURCE_PRESENT`
- `RELEASE_METADATA_INCONSISTENT`
- `REPO_OWNED_CONFLICT`
- `UNKNOWN_OR_UNRELEASED_TARGET`
- exact unsupported/authority result when Marketplace layer cannot be changed.

Do not dump internal audit logs as the primary response.

## 18. Capability Gate Matrix V2

The five gates remain because their failure semantics are distinct.

### G1 — Short request + formal-release/impact routing

Normal entry starts from a short Maintainer request.

Must cover:

- isolated single-plugin update;
- already-current no-op;
- unknown/unreleased target;
- `main` newer than `release` without leakage;
- isolated workflow release with **no** Update impact staying isolated;
- explicit cross-layer Update impact selecting only declared companion owners;
- conflicting release metadata failing closed;
- ordinary facts resolved without Human Gate.

Failure if route/scope depends on user-supplied version/path/component decisions or arbitrary diff inference.

### G2 — Legacy bootstrap + installed plugin/self-update + fresh-session consumption

Must start from a realistic legacy state:

- ai-skills-core 0.4;
- expected AI_Skills Git Marketplace pinned to `main`;
- installed plugin state recorded.

Prove:

- source identity/config owner discovery;
- formal `release` preflight;
- bounded `main -> release` migration with recovery;
- system/non-user-owned Marketplace fails closed;
- capability-bearing Maintainer installation;
- stale Marketplace/install correction;
- self-update after bootstrap;
- current session reports reload-required;
- a genuinely fresh Codex process/session loads the final released Maintainer.

Unrelated installed plugin state must not be opportunistically upgraded.

### G3 — Bridge Kit maintenance + formal-release producer routing + canonical Bridge delegation

Must prove both the consumer and producer directions on the same final candidate:

- `update Bridge Kit` works through AI Skills Maintainer;
- Bridge release/version/source is discovered by `bridge-kit-maintainer`;
- safe formal source/package update succeeds;
- runtime path/version is verified;
- no Bridge runtime implementation is duplicated into AI_Skills;
- explicit Bridge Update impact triggers exactly the required canonical `ai-bridge` Host/consumer commands;
- no impact declaration leaves Host/optional consumers unchanged;
- already-current Bridge is no-op;
- starting from the **normal Bridge repository formal-release maintenance entry**, the mandatory Bridge `AGENTS.md` locator routes formal distribution/version closure to AI Skills Maintainer / `bridge-kit-maintainer`;
- only the exact formally closed Bridge commit is eligible to advance Bridge `release`;
- advancement is fast-forward-only and the remote ref is verified after the write;
- ordinary docs/TODO/main commits after a formal release do not advance `release`;
- non-fast-forward or inconsistent target/ref state fails closed;
- Bridge runtime implementation remains owned/executed by canonical Bridge/`ai-bridge` code.

A deterministic test may verify the locator is present, but locator-string presence alone is not release-critical evidence. G3 must include normal-entry routing plus Git behavior evidence, bound to the same final candidate.

### G4 — Selective managed consumers + source/dirty safety

Same final candidate must prove:

1. one genuinely stale **managed** consumer updates;
2. one normal unaffected repo remains byte-for-byte unchanged;
3. one apparently conflicting **unmanaged** AGENTS/project rule is diagnosed but remains byte-for-byte unchanged without repo authority;
4. unrelated dirty canonical checkout safely proceeds when no overlap;
5. overlapping user-owned dirty paths trigger exactly one bounded Human Gate;
6. repo-specific science/safety/privacy/Figma/device/server rules are preserved.

### G5 — Failure/recovery/authorization/should-not-change

Inject a bounded failure after at least one safe successful step.

Prove:

- truthful `PARTIAL_UPDATE`;
- no blind/destructive rollback;
- exact bootstrap source restoration when the source-swap itself fails;
- rerun converges from discovery;
- no repeated question for an already-authorized bounded effect;
- unrelated plugins/Bridge layers/repos remain unchanged;
- concise final report.

### Platform coverage

Exercise the same contract on representative:

- Windows/WSL;
- macOS;
- Linux/server/HPC login host.

Platform-specific path/discovery mechanics may differ.

Do not claim an unexercised platform as verified.

## 19. Version and release decision

This remains a new repository-level user capability.

After V2 release, AI_Skills_Collection can perform a normal task that 5.0.x cannot: from one Maintainer short request, discover and synchronize the current machine's participating AI Research Stack, including Bridge Kit version/distribution and selective managed adaptation, without user-supplied versions/paths/components/templates.

Conditional release decision:

Repository bump decision: **MINOR**  
Repository: `5.0.7 -> 5.1.0`

Affected plugins:

- `ai-skills-core: 0.4 -> 0.5`
  - new normal machine update/orchestration and Bridge maintenance capability.

- `workflow-core: NO_BUMP`
  - existing delivery semantics are consumed unchanged.

- domain plugins: `NO_BUMP`
  - no domain production behavior changes are planned.

Bridge Kit:

- `NO_BUMP` in this task if Bridge runtime implementation remains unchanged;
- release-channel ownership, the mandatory minimal Bridge `AGENTS.md` owner locator, and current-machine distribution maintenance do not themselves change Bridge runtime behavior;
- any Bridge production behavior change must return to Planner/Critic and receive its own version decision.

README closure is mandatory and must replace normal `main`-pinned stable update guidance with the formal release channel while clearly separating explicit development/main mode.

## 20. Should-not-change

- compatibility slug `ai-skills-core`;
- display name **AI Skills Maintainer**;
- workflow-core ownership;
- target domain plugin ownership;
- Bridge runtime/Host implementation ownership;
- current project-skill-installer direct project use;
- skill-library-analysis role;
- unrelated plugin versions in Route A;
- unowned repo text;
- repo-specific scientific/safety/privacy/Figma/deployment/device/server rules;
- no new top-level plugin;
- no daemon/watcher/inventory database/machine registry/ledger/second auth/state machine;
- no Planner/Critic/full release gates for ordinary daily updates.

## 21. Non-goals

- cross-machine orchestration;
- centralized workstation/server repo inventory;
- remote deployment control plane;
- rewriting every repo AGENTS;
- automatic installation of all domain plugins;
- automatic installation of all optional Bridge layers;
- using current main as the default stable target;
- claiming current-session hot reload;
- replacing Git/Codex Marketplace/pip/Bridge CLI.

## 22. Execution boundary

V2 is still design/review only.

This Planner round does not:

- implement production source;
- regenerate plugins;
- change versions;
- create implementation branch/worktree;
- create/advance either `release` ref;
- migrate a real Marketplace;
- update a real Bridge install;
- mutate Host state;
- call paid API;
- start automation.

Implementation requires independent Critic PASS on this V2.1 package and a later current-user kickoff that binds the actual execution worktree and bounded cross-repo release-channel bootstrap authority.
