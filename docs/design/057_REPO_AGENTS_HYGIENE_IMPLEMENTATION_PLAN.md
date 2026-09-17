# 057 Repo AGENTS Hygiene — Implementation Plan

- Execution package version: `v0.1`
- Task key: `057_repo_agents_hygiene`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Approved design authority: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Design review decision relayed by user: `RESULT=PASS`, `READY_FOR_EXECUTION_PLAN=YES`
- Canonical Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.1
- Kickoff Draft: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` v0.1
- Relationship to 056: finish 057 first; then bounded 056 source-drift revalidation/package amendment; do not redesign v6 unless 057 invalidates a frozen 056 assumption.

This file freezes the approved 057 design into an implementation contract. It does not authorize execution. No branch/worktree, product-repo edit, Bridge Kit production change, version bump, or 056 implementation may begin until an independent Critic reviews this exact Plan + Goal + Kickoff and returns `READY_FOR_CODEX=YES`, and the user then sends the approved Kickoff.

## 1. User value and completion target

057 is complete only when the instruction surfaces become easier to consume without losing important project knowledge.

The implementation must produce two observable outcomes:

1. existing target repositories have internally coherent, navigable `AGENTS.md` / delegated rule surfaces with duplicate or stale wording removed, current authorities made explicit, and all important project-specific invariants preserved;
2. Bridge Kit can initialize a **fresh** repository with a concise project-owned root-AGENTS scaffold through the normal `ai-bridge init` path, while existing repositories remain untouched outside the managed Bridge block.

A smaller line count, prettier headings, or a template file existing on disk is not completion.

## 2. Current source identities at package drafting

These are evidence locators, not immutable execution bases. Kickoff execution must re-check current remote authority and stop if relevant semantics drift.

- `AI_Skills_Collection main@5a92e30e2933d286f6f884ba7fb9c18bc1dbe534`
- `GPT_Codex_AI_Bridge_Kit main@cb77b1cc5a1fce097a38066d2db452291e359852`, version `0.8.2`
- `Bobbio develop@0811116ac7197590f0af773f3c6296d4ca41db80`
- `Lucerna main@461dcea4015434f90d50922d9b7ae054286c98bc`
- `Mica-for-ChatGPT main@aa4ce52581fff2e207d1f93600becbb3018b0efc`
- `Asteria main@166791c27752c70255043f026dcbda4deb693c04`
- `SeminarArc main@71c59d39f4d7e9cd3a3d813ad55d5cf6a38a4b11`
- `CUHK_Date main@57dd5432c744ef16ec614e1e10b1b3f21564c7ba` — inspect only

Current Bridge reality relevant to 057:

- `ai_bridge_kit/cli.py::install_agents_snippet()` creates a fresh root `AGENTS.md` containing only the managed Bridge block when no root file exists;
- existing root `AGENTS.md` is preserved except for append/update of the managed block;
- `codex/AGENTS_SNIPPET.md` owns that managed block;
- `templates/prompts/AGENT_RULES.md` owns the long-lived Lite/execution surface;
- current Bridge version is `0.8.2`.

## 3. External reality check used for execution design

Planner rechecked current official OpenAI evidence before freezing this package:

- OpenAI's 2026 Harness Engineering guidance reports that a monolithic `AGENTS.md` failed in practice and that a short root file should act as a map into deeper repository knowledge;
- current Codex source/config uses a default `project_doc_max_bytes = 32768` aggregate project-instruction budget.

Implication: 057 optimizes **instruction ownership and discoverability**, not cosmetic uniformity. Safety-critical project facts may remain long when necessary; volatile procedures should move behind explicit locators when a canonical owner exists.

## 4. Absolute scope boundaries

### Repositories that may be modified

1. `YuukiAS/GPT_Codex_AI_Bridge_Kit`
2. `YuukiAS/Bobbio`
3. `YuukiAS/Lucerna`
4. `YuukiAS/Mica-for-ChatGPT`
5. `YuukiAS/Asteria`
6. `YuukiAS/SeminarArc`
7. `YuukiAS/AI_Skills_Collection` only for 057 result/evidence/control artifacts

### Inspect-only

- `YuukiAS/CUHK_Date` — do not create a root `AGENTS.md`; no production/project-policy mutation in 057.

### Explicitly out of scope

- CARE Challenge
- Server/VPS repositories
- EAT Research
- product/runtime code in Bobbio/Lucerna/Mica/Asteria/SeminarArc
- 056 production implementation
- central AI_Skills plugins
- paid APIs/Terra
- new workflow state machines/controllers/ledgers/watchers

057 is an instruction-surface hygiene task plus a bounded Bridge fresh-repo scaffold change. It is not a product refactor.

## 5. Git/source strategy after approved Kickoff

All task branches/worktrees described below are **future authorization candidates only** until the user sends the approved Kickoff.

### AI_Skills_Collection

- branch: `reviewed/057_repo_agents_hygiene`
- base: kickoff-time latest `origin/main` containing the approved package without relevant semantic drift
- purpose: task evidence/result/manifest only; no central plugin production change

### GPT_Codex_AI_Bridge_Kit

- branch: `reviewed/057_repo_agents_hygiene`
- base: kickoff-time latest `origin/main`
- use a task-owned clean worktree from the canonical local checkout when available

### Bobbio

- branch: `reviewed/057_repo_agents_hygiene`
- base: kickoff-time current `origin/develop`
- temporary isolation is justified because the task rewrites a repo-wide instruction authority; do not push directly to `develop` before independent implementation review

### Lucerna / Mica-for-ChatGPT / Asteria / SeminarArc

- branch in each repo: `reviewed/057_repo_agents_hygiene`
- base: kickoff-time latest `origin/main`
- use canonical local checkout/worktree first; unrelated dirty work stays untouched

### Source discovery

Before branch/worktree creation in each repo:

- locate existing canonical checkout/worktree/clone;
- verify repository identity, origin, intended base branch/ref, freshness and dirty ownership;
- protect unrelated dirty work; dirty does not mean abandon the repo;
- use the exact authorized task branch/worktree only;
- network clone only when no usable local source exists;
- do not remap Git remotes, force push, delete branches/tags, or rewrite history.

If the exact task branch already exists with ambiguous ownership, stop that repo and report it rather than inventing a new branch name.

## 6. Phase 0 — Inventory and semantic-preservation baseline

Before editing any target repo, create the central evidence directory in the AI_Skills task branch:

`results/057_repo_agents_hygiene/`

At minimum produce:

- `RESULT.md`
- `SEMANTIC_PRESERVATION.md`
- `SIZE_REPORT.md`
- `MANIFEST.md`

`SEMANTIC_PRESERVATION.md` must have a section per mutable repo with this table before edits:

| Current rule/invariant | Current owner/location | Keep in root / move / merge | New canonical location | Evidence/reason |
| --- | --- | --- | --- | --- |

Every hard rule, source locator, safety boundary, user-data boundary, release/branch invariant and delegated rule surface that is changed or moved must be accounted for.

The baseline also records:

- exact source commit;
- root `AGENTS.md` bytes/lines;
- delegated `prompts/AGENT_RULES.md` identity when present;
- Bridge managed-block hash/text identity where present;
- canonical docs used to resolve authority.

No edit may begin in a repo until its preservation table is sufficiently complete to explain every planned deletion/move/merge.

## 7. Phase 1 — Bridge Kit reusable AGENTS scaffold

### 7.1 New source template

Add:

`templates/repo/AGENTS_TEMPLATE.md`

It is the **project-owned root scaffold**, not another Lite rules file.

Recommended concise structure:

1. Purpose / authority / precedence
2. Read first / canonical locators
3. Project scope and hard invariants
4. Environment / source / Git boundaries
5. Safety / data / authority boundaries
6. Testing / acceptance / human boundary
7. Design / UI / domain rules
8. Version / release / integration
9. Deeper docs / ownership

The template must say clearly that irrelevant sections may be removed. It must not fabricate project facts, credentials, branches, machines, providers, or design authorities.

It must point to `prompts/AGENT_RULES.md` as the long-lived execution/Lite owner and must not copy Lite rules into root.

### 7.2 Normal `ai-bridge init` behavior

Modify `ai_bridge_kit/cli.py` without adding a new migration engine or CLI mode:

- if root `AGENTS.md` does not exist, create it from the canonical project scaffold plus exactly one managed Bridge block generated from `codex/AGENTS_SNIPPET.md`;
- if root `AGENTS.md` already exists, keep current fail-safe behavior: preserve project-owned prose and only append/update the managed block;
- `--force` must not replace/reformat the project-owned remainder with the scaffold;
- `--no-agents`/existing opt-out semantics, if present, remain unchanged.

The managed block remains owned by `codex/AGENTS_SNIPPET.md`. The scaffold must not manually duplicate/fork it.

### 7.3 Bridge tests

Add focused tests through the real `init_workspace` / CLI path, preferably in the existing CLI test area or one small dedicated test file.

Required cases:

- fresh directory without `AGENTS.md` -> scaffold + exactly one managed block + `prompts/AGENT_RULES.md` locator;
- `ai-bridge validate` succeeds on the initialized workspace;
- second normal init is idempotent;
- custom existing root -> project-owned content preserved byte-for-byte outside the managed block;
- force init -> project-owned content still preserved; only managed/generated targets refresh according to existing semantics;
- existing root with managed block -> no duplicate block;
- fresh scaffold contains no copied Lite baseline / second execution-policy authority;
- no fabricated project-specific invariant appears.

Run focused CLI tests first, then the Bridge canonical full test suite once the candidate is stable.

### 7.4 Bridge version/release candidate

Because normal `ai-bridge init` behavior changes compatibly for fresh repos, target Bridge patch candidate is:

`0.8.2 -> 0.8.3`

Only bump after focused/full tests and H7–H9 pass. Synchronize `__version__`, README/current behavior documentation and CHANGELOG according to current Bridge release policy. Do not alter historical records to pretend older versions had the scaffold.

If 057 integrates `0.8.3`, later 056 source-drift revalidation must not attempt to reuse the same version slot; 056 will choose its next valid Bridge version based on then-current main.

## 8. Phase 2 — Bobbio substantial reorganization

Allowed files:

- `AGENTS.md`
- `docs/DEVELOPMENT_WORKFLOW.md` only if a unique moved detail needs a canonical owner
- `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md` only if a unique moved acceptance detail needs a canonical owner

Do not change Figma, product code, schemas or runtime version.

Required outcomes:

- frontend/Product Design conditional reads include `docs/design/FIGMA_HANDOFF.md`;
- authority is explicit:
  - Figma handoff = current canonical visual source;
  - `docs/PRODUCT_DESIGN_BRIEF.md` = durable product/interaction constraints;
  - `images/Bobbio_Design_*.png` = historical/supporting references, not a parallel production authority;
- merge duplicate general GUI/human-gate/anti-blocking/pre-user-review prose into one coherent section or root invariant + canonical locator;
- keep Zotero authority/isolation, update safety, native Windows acceptance, knowledge/provenance semantics, versioning, roadmap order and iPad/Pencil constraints discoverable;
- do not replace Bobbio-specific safety with generic 056 wording.

## 9. Phase 3 — Lucerna light normalization

Allowed file:

- `AGENTS.md`

Bridge-managed block must remain byte-identical to the current canonical generated block.

Keep distinct project owners for:

- actual Windows release/tray lifecycle;
- live provider truth and no mock release evidence;
- matching regression requirement;
- canonical screenshot helper/evidence budget;
- Longleaf source/permission boundary.

Only normalize order/headings and remove exact/near-exact duplicate local prose. Do not move these project-specific protections into generic language and do not introduce new 056 sections.

## 10. Phase 4 — Mica testing consolidation

Allowed file:

- `AGENTS.md`

Required outcomes:

- merge repeated `Development testing budget`, `Test tiers`, and `Focused iteration before full E2E` prose into one coherent testing ladder;
- keep the rule that repeated focused failure triggers source/fixture/validator inspection before another rerun;
- clarify that the real long-conversation check is the final/manual authenticated acceptance path, while automated authenticated ChatGPT regression remains forbidden;
- preserve fail-open behavior, unstable DOM/private-endpoint assumption, privacy-safe built-in diagnostics, stable `dist/mica-dev`, runtime version identity and typing hot-path budget;
- do not add generic 056 wording that duplicates stronger Mica-specific rules.

No extension/runtime source change or version bump.

## 11. Phase 5 — Asteria map conversion

Allowed files:

- `AGENTS.md`
- new `docs/operations/development/RUNTIME_OPERATIONS.md`

Do not modify product/runtime code or `prompts/AGENT_RULES.md` unless implementation discovers a direct contradiction that cannot be resolved by root locators; such a discovery is a stop condition requiring Planner review rather than silent scope expansion.

Move volatile detailed runtime/tunnel/dev-server commands and dated operational mechanics from root into `RUNTIME_OPERATIONS.md` while preserving them verbatim or semantically equivalently.

Root keeps concise hard invariants/locators:

- fixed public URL must not be silently replaced;
- canonical black-box browser contract locator and essential invariant `可以自动操作页面；不能绕过页面`;
- GPT Work-before-human acceptance gate;
- locator to `prompts/AGENT_RULES.md` for developer visual self-QA / scientific graph / generic-fix rules;
- Git/version/release boundaries that are truly project-wide;
- locator to runtime operations.

Do not duplicate the canonical browser contract in root.

## 12. Phase 6 — SeminarArc map conversion with safety preservation

Allowed files:

- `AGENTS.md`
- `docs/DEVICE_TESTING.md`

Do not modify Android/runtime/product code.

Before shortening root, ensure every unique device/environment/safety detail removed from root survives in `docs/DEVICE_TESTING.md` or another already-existing canonical authority. For 057, prefer updating `docs/DEVICE_TESTING.md`; do not create another environment manual unless the current source makes preservation impossible, in which case stop and return to Planner.

Root must retain a prominent non-negotiable summary:

- Emulator-first;
- protected physical device is never a generic connected/instrumentation target;
- no automatic transport recovery/reset;
- explicit serial plus pre/postflight for any specifically authorized physical write;
- physical-device channel failure does not block independent WSL/headless/Emulator work;
- secrets/PIN never enter repo/log/result.

Move long dated environment snapshots, exact SDK/JDK/cache inventories, command ban lists and historical incident narrative into `docs/DEVICE_TESTING.md` while keeping clear locators.

Preserve project skills, 0.1.x product invariants, internal dogfood authorization and Compose architectural rules when they remain current.

## 13. Phase 7 — CUHK Date inspection-only confirmation

Read current `docs/design/prototype/AGENTS.md` and confirm it remains short/coherent.

Do not create root `AGENTS.md` and do not copy the Bridge scaffold into this existing repository merely for symmetry.

Record `NO_CHANGE` in 057 evidence unless a new direct contradiction is discovered. A new contradiction is evidence for Planner, not authorization for Executor to expand scope.

## 14. H1–H9 acceptance matrix

### H1 — Semantic preservation

Evidence: completed per-repo preservation table, final diff and independent review.

PASS only if every changed/moved hard rule has a surviving owner/locator. A shorter file with an unaccounted safety/product invariant is FAIL.

### H2 — No internal contradiction

Evidence: direct comparison of final root and delegated current authorities.

Must close known cases such as Bobbio Figma vs legacy images and Mica manual real-site acceptance vs automated authenticated-loop prohibition without inventing new product semantics.

### H3 — Discoverability

Evidence: start from final root `AGENTS.md` and follow only its explicit locators for current design/safety/testing/runtime authorities.

PASS if a new agent can locate the current owner without reading historical incident logs or guessing filenames.

### H4 — Managed-block integrity

Evidence: base/final hash or exact-byte comparison for existing repo Bridge-managed blocks, plus Bridge source-generated fresh block test.

Product-repo cleanup must not hand-edit/fork managed Bridge blocks.

### H5 — Context quality

Evidence: before/after bytes and lines for Bobbio, Mica, Asteria and SeminarArc; Lucerna also reported even if reduction is small.

No numeric target. PASS requires meaningful removal/reorganization of duplication/volatile detail where approved, while H1/H6 remain green.

### H6 — Repo-specific regression review

Directly verify the final instruction surface still exposes:

- Bobbio: Zotero isolation/authority, Figma authority, native pre-user review, knowledge/iPad constraints;
- Lucerna: Windows release, real providers, tray, screenshot helper, Longleaf boundaries;
- Mica: account safety, diagnostics, typing hot path, focused testing and final manual real-site acceptance;
- Asteria: fixed public URL, black-box contract, GPT Work-before-human, visual/scientific-rule locator;
- SeminarArc: physical-device safety, Emulator-first, dogfood boundary, project-skill locators;
- CUHK Date: existing prototype semantics unchanged.

### H7 — Fresh Bridge scaffold normal entry

Use a clean temporary repo with no root `AGENTS.md` and run real `ai-bridge init` then `ai-bridge validate`.

PASS requires scaffold + one managed block + Lite locator + no fabricated invariants.

### H8 — Existing-repo should-not-change

Use a temporary repo with custom project-owned `AGENTS.md`; run normal init and force init.

PASS requires project-owned text preserved byte-for-byte outside managed block and no automatic scaffold migration.

### H9 — No Lite duplication

Inspect generated fresh root and installed `prompts/AGENT_RULES.md`.

PASS if root points to Lite owner but does not copy its execution-policy content or create a second long-lived authority.

## 15. Final-candidate identity

Before independent implementation review, freeze a cross-repo candidate manifest in AI_Skills `results/057_repo_agents_hygiene/RESULT.md`:

```text
AI_SKILLS_RESULT_COMMIT=<sha>
BRIDGE_CANDIDATE_COMMIT=<sha>
BRIDGE_VERSION=<0.8.3 candidate if gates pass>
BOBBIO_CANDIDATE_COMMIT=<sha>
LUCERNA_CANDIDATE_COMMIT=<sha>
MICA_CANDIDATE_COMMIT=<sha>
ASTERIA_CANDIDATE_COMMIT=<sha>
SEMINARARC_CANDIDATE_COMMIT=<sha>
CUHK_DATE_INSPECTED_REF=<sha>
H1..H9=<status/evidence locator>
```

Any later semantic edit to an instruction surface invalidates the affected H1/H2/H3/H6 evidence and requires re-freeze for that repo.

## 16. Should-not-change

057 must not:

- change product/runtime behavior;
- change scientific/product architecture;
- modify Bridge Host Policy or 056 Default prompt transport;
- copy 056 Lite rules into root scaffold;
- auto-migrate existing repos to the scaffold;
- bulk-translate repos solely for style consistency;
- delete safety rules because they are long;
- create new workflow states/controllers/ledgers;
- create root `AGENTS.md` in CUHK Date merely for symmetry;
- modify CARE/Server/EAT;
- execute 056.

## 17. Recovery and failure handling

- If preservation mapping reveals an unresolved authority conflict, stop that repo at `EVIDENCE_NEEDED`; do not choose the prettier wording.
- If a managed Bridge block differs from canonical source for reasons not explained by current repo state, do not hand-edit it; report the drift.
- If an existing repo has unrelated dirty edits to instruction files, protect them and stop that repo rather than overwrite/stash/reset.
- If Bridge scaffold tests would require a migration engine or a new state machine, stop and return to Planner; the approved design is intentionally simpler.
- If Bridge 0.8.3 candidate fails H7/H8/H9, keep current 0.8.2 baseline; do not bump version to manufacture closure.
- If any repo cleanup fails H1/H6, keep its pre-057 source as the integration baseline and report the specific missing invariant.

## 18. Implementation handoff and integration boundary

Executor may commit/push only the exact authorized task branches after approved Kickoff. It stops at `EXECUTED_UNAUDITED` / equivalent implementation handoff with the final manifest and H1–H9 evidence.

No task branch may be merged into product base branches or Bridge main under this Kickoff. Independent implementation review must inspect the actual final diffs and semantic-preservation evidence first.

After implementation review PASS, a separate bounded integration step may merge the approved 057 commits. Only after 057 integration is complete does Planner return to 056 for source-drift revalidation.

## 19. Bounded 056 source-drift revalidation after 057 integration

This is a later Planner step, not Executor-owned work inside 057.

Planner must compare then-current 056 v0.2 package against integrated 057 source and only amend overlaps/locators/version slots, expected examples:

- remove Bobbio Figma-locator work if 057 already completed it;
- account for Bridge root scaffold ownership;
- if Bridge `0.8.3` was consumed by 057, select the next valid 056 Bridge patch candidate according to current release policy;
- refresh exact refs/commits.

Do not redesign v6, W1–W5, F-A–F-C or G1–G8 unless 057 introduced direct evidence that a frozen 056 assumption is false.

## 20. Research/adoption record

Adopted:

- OpenAI's short-AGENTS-as-map practice as evidence supporting progressive disclosure;
- current Codex instruction-budget reality as a reason to remove duplication/volatile detail.

Not adopted:

- a fixed 100-line target;
- automatic migration of existing repos;
- identical section sets across projects;
- a new policy engine for AGENTS hygiene.

`NEXT_HANDOFF = CRITIC`
