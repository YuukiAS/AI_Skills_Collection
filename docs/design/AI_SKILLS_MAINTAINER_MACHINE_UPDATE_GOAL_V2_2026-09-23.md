# AI Skills Maintainer machine update orchestration — Canonical Goal V2

Date: 2026-09-23  
Status: PLANNER_DRAFT_FOR_CRITIC  
Task key: `ai-skills-core--machine-update-orchestration`

Proposal / Plan:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_2026-09-23.md`

Planner response to V1 Critic:
`docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PLANNER_RESPONSE_V2_2026-09-23.md`

## Goal

Make the existing `ai-skills-core` plugin, displayed as **AI Skills Maintainer**, the single normal user entry for updating and adapting the AI Research Stack on the current Codex machine/server.

The normal user should only need to say, for example:

- `update presentations`
- `update workflow-core`
- `update research-writing`
- `update AI Skills`
- `update Bridge Kit`
- `sync this machine`

The user must not need to supply:

- current/target version;
- repository release;
- commit/SHA;
- `CODEX_HOME`;
- AI_Skills checkout;
- Bridge checkout;
- local repo inventory;
- adaptation template;
- Bridge/Host/repo-local routing decisions.

## Required internal architecture

Keep the public plugin and slug unchanged:

- display name: `AI Skills Maintainer`
- compatibility slug: `ai-skills-core`

Inside the existing plugin, use owner-separated maintenance capabilities:

1. new `machine-update-orchestrator`
   - normal entry;
   - discovery;
   - formal release resolution;
   - route/scope composition;
   - Human Gate classification;
   - delegation;
   - verification/report.

2. existing `ai-skills-repository-maintainer`
   - AI_Skills repository/plugin release maintenance;
   - AI_Skills release-channel production.

3. existing `project-skill-installer`
   - AI_Skills manifest/profile/managed consumer update.

4. new `bridge-kit-maintainer`
   - Bridge Kit version/source/distribution maintenance;
   - Bridge formal release-channel maintenance;
   - canonical checkout/editable-install refresh;
   - runtime version/path verification;
   - delegation to the existing `ai-bridge` runtime/Host/consumer commands.

5. existing `skill-library-analysis`
   - overlap/merge/structure decisions only.

Do not create a new top-level plugin.

## Ownership boundary

AI Skills Maintainer may maintain/adapt:

- AI_Skills skills/profiles/managed consumers;
- AI_Skills central plugins/repository release;
- Bridge Kit distribution/version/source identity.

AI Skills Maintainer does **not** absorb:

- Bridge Host Policy implementation;
- Lite/Review/Control/Persistent Run implementation;
- Bridge Human Gate/plugin replay runtime;
- workflow-core delivery semantics;
- target domain scientific/product judgment.

Actual Bridge runtime mutation must continue through Bridge canonical CLI.

## Formal release truth

Normal `update` must use a stable formal release channel and must not silently consume arbitrary `main`.

V2 requires a fast-forward-only Git branch:

`release`

for AI_Skills_Collection and Bridge Kit.

Normal updater is read-only with respect to `release`.

Only formal release closure may advance it.

Producer owners:

- AI_Skills release -> `ai-skills-repository-maintainer`;
- Bridge release -> `bridge-kit-maintainer`.

Advancement must:

- target the exact formally closed release commit;
- be fast-forward-only;
- verify origin and ancestry;
- verify the remote ref after push;
- fail closed on mismatch/non-fast-forward;
- not move for later docs/evidence/main commits.

The canonical producer contract lives in AI Skills Maintainer. Bridge may receive only a minimal pointer if required for discoverability; do not build another release engine in Bridge.

## Authoritative update impact

Cross-layer scope expansion must come from formal release metadata, not arbitrary diff inference.

From the first capability-bearing release onward:

- the exact formal `release` ref is the release identity;
- the matching root `CHANGELOG.md` release entry is the authority for update impact;
- cross-layer releases use a small `### Update impact` subsection naming required companions and required managed-consumer refresh;
- absence of the subsection means isolated by default;
- component/plugin changelogs may only clarify detail inside the root-declared scope;
- contradictory metadata fails closed.

Legacy current 5.0.7 / Bridge 0.8.5 may use 056 final closure only as a bounded bootstrap compatibility source.

## Three update routes

Keep only:

- Route A — isolated AI_Skills plugin/profile;
- Route B — formal cross-layer stack/workflow composition;
- Route C — Bridge Kit distribution/runtime update.

`sync this machine` is a composition request, not a fourth engine.

## One-time legacy bootstrap

Current pre-capability installs may use AI_Skills Marketplace ref `main`.

The first capability-bearing release must support one explicit bootstrap migration per Codex identity.

Bootstrap must:

1. discover exact Marketplace name/source/ref/sparse paths/config owner and installed plugin state;
2. require the expected AI_Skills Git source at `main`;
3. verify remote `release` and the capability-bearing Maintainer payload before removal;
4. preserve exact legacy metadata for recovery;
5. use official Codex Marketplace commands to replace the user-owned source with the same source at `release`;
6. reinstall ai-skills-core and the requested target;
7. restore the exact old source if the source replacement fails;
8. fail closed if the Marketplace is owned by a non-user/system layer the current authority cannot mutate;
9. require a fresh session.

Do not claim ai-skills-core 0.4 already has this updater. Bootstrap is the one-time exception permitted by the product requirement.

After bootstrap, Maintainer self-update is the normal path.

## Selective repo adaptation

Automatic mutation is allowed only on ownership-proven surfaces:

- AI_Skills manifest/managed block;
- Bridge canonical managed consumer/template/block;
- exact migration targets named by formal release impact with an ownership locator.

Unmanaged repo-authored `AGENTS.md`, copied rules, science/safety/privacy/Figma/design/deployment/device/server rules are diagnosis-only.

If an unowned rule genuinely conflicts, return `REPO_OWNED_CONFLICT` with exact repo/path/reason and ask for one bounded repo-owned decision/task. Do not rewrite it automatically.

A normal unaffected repo remains byte-for-byte unchanged.

## Discovery and dirty work

Inherit 056 Source Discovery.

Maintainer must discover, rather than ask for:

- host/user/HOME/CODEX_HOME;
- Codex executable/version;
- Marketplace source/ref/config owner;
- installed plugin versions;
- canonical AI_Skills checkout when needed;
- Bridge executable/root/version/Host state when relevant;
- bounded managed consumer candidates.

Do not scan all disks/HOME/network mounts for repos.

Prefer existing canonical checkouts, verify origin/ref/freshness/ancestry, preserve unrelated dirty work, allow safe non-overlapping fast-forward, never stash/reset/restore/remap remote, never use reviewed/temporary worktrees as normal production install sources.

Development checkouts ahead/diverged from `release` must not be silently downgraded.

## Human Gate

Ordinary update mechanics are `AGENT_RESOLVABLE`.

Use one minimal `HUMAN_ONLY` gate only for genuinely new:

- credential/account/provider;
- private external transfer;
- destructive operation;
- production deployment/live-global effect outside the update request;
- unresolved user-owned dirty overlap;
- unmanaged repo rule conflict needing a product/repo decision;
- irreducible product semantics.

Do not ask for discoverable versions/paths/commits/components.

Do not repeat a gate after the bounded effect was already authorized.

## Self-update truthfulness

After bootstrap, Maintainer may update/reinstall its newer formal release.

It must not claim the current session hot-reloaded.

Return `UPDATED_RELOAD_REQUIRED`.

Release acceptance must prove a genuinely fresh Codex process/session loads the released target through the normal installed plugin path.

Source SKILL reading or generated parity alone is not sufficient.

## Acceptance gates

Use exactly G1–G5 from Proposal V2:

- G1 — short request + formal release/update-impact routing;
- G2 — legacy main->release bootstrap + install/self-update + fresh session;
- G3 — Bridge Kit maintenance + canonical Bridge delegation;
- G4 — selective managed consumers + source/dirty safety;
- G5 — failure/recovery/Human Gate/should-not-change.

Do not add new gates merely to mirror the four V1 Critic blockers.

Release-critical evidence must be from the same final candidate.

Platform claims are limited to environments actually exercised.

## Version decision under review

Conditional on implementation and gate success:

Repository bump decision: `MINOR`  
Repository: `5.0.7 -> 5.1.0`

Affected plugin:

- `ai-skills-core: 0.4 -> 0.5`

No planned bump:

- `workflow-core`;
- domain plugins;
- Bridge Kit, provided Bridge runtime production behavior is unchanged.

Any Bridge production behavior change requires return to Planner/Critic and a separate Bridge version decision.

README closure is mandatory.

## Non-goals

No:

- cross-machine controller;
- central repo inventory;
- update daemon/watcher;
- machine registry/database/ledger;
- second authorization system;
- adaptation state machine;
- all-repo AGENTS rewrite;
- automatic install of every plugin/Bridge optional layer;
- ordinary update Planner/Critic loop;
- ordinary update full Capability Gates;
- stable update from arbitrary main;
- claimed current-session hot reload.

## Current phase boundary

This Goal is still design-only.

No production source, generated payload, version, Marketplace identity, Bridge source/runtime, Host state, implementation branch/worktree or `release` ref may be changed until:

1. independent Critic PASSes this V2 package; and
2. the user sends a future implementation kickoff that binds the actual execution worktree and bounded release-channel bootstrap authority.
