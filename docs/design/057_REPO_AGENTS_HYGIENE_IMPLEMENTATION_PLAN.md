# 057 Repo AGENTS Hygiene — Implementation Plan

- Execution package version: `v0.2`
- Task key: `057_repo_agents_hygiene`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Approved design authority: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Bounded new user amendment pending this execution review: `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- Prior execution package: v0.1 at `57f58821deecf56ee69a6504f85145ce3bdfb11e`, Critic `REVISE`
- Canonical Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.2
- Kickoff Draft: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` v0.2
- Relationship to 056: finish 057 first; then bounded 056 source-drift revalidation/package amendment; do not redesign v6 unless 057 invalidates a frozen 056 assumption.

This file only revises the execution contract. It does not authorize execution. No product-repo edit, Bridge Kit production change, task branch/worktree, version bump, or 056 implementation may begin until independent Critic reviews this exact v0.2 Plan + Goal + Kickoff, including the bounded versioning amendment, returns `READY_FOR_CODEX=YES`, and the user then sends the approved Kickoff.

## 0. Critic blocker disposition

### C057-E1-BOBBIO-AUTHORITY-OWNER-SCOPE — ACCEPT

Direct source confirms the conflict: `docs/design/FIGMA_HANDOFF.md` says Figma is the canonical visual source for subsequent production implementation, while `docs/PRODUCT_DESIGN_BRIEF.md` still says the brief plus `images/Bobbio_Design_*.png` are the primary visual basis.

v0.2 closes this by adding `docs/PRODUCT_DESIGN_BRIEF.md` to the Bobbio mutation scope, but only for source-of-truth / visual-authority wording. Final authority must read consistently across all three surfaces:

- Figma = current canonical visual design/components/screen composition;
- Product Design Brief = durable product/interaction constraints;
- `images/Bobbio_Design_*.png` = historical/supporting visual references, not parallel production authority.

No Figma, product code, runtime, schema, or unrelated design-brief rewrite is allowed.

### C057-E2-SEMINARARC-AUTHORITY-INVERSION — ACCEPT

Direct source confirms `docs/DEVICE_TESTING.md` currently says complete physical-device constraints are owned by root `AGENTS.md`, which would become stale/circular after 057 moves detailed mechanics out of root.

v0.2 explicitly changes the owner wording so that:

- root `AGENTS.md` owns the impossible-to-miss physical-device safety summary + locator;
- `docs/DEVICE_TESTING.md` owns detailed device/environment/test mechanics, command restrictions, volatile inventory and historical incident evidence.

Root must still prominently retain Emulator-first, protected-device not generic connected-test target, no automatic transport reset/recovery, explicit verified serial + pre/postflight for authorized physical writes, physical-channel failure not blocking independent WSL/headless/Emulator work, and PIN/secret non-disclosure.

No third device/environment manual is created.

### C057-E3-SELF-REFERENTIAL-FINAL-CANDIDATE — ACCEPT

v0.1 incorrectly required a tracked result artifact to contain the SHA of the commit that contains itself. v0.2 replaces that with a two-stage non-self-referential closure:

**Stage A — evidence/result commit `E`**

Commit finalized task evidence:

- `RESULT.md`
- `SEMANTIC_PRESERVATION.md`
- `SIZE_REPORT.md`
- H1–H9 evidence/locators

Tracked content does not attempt to write `E`'s own SHA.

**Stage B — manifest closure commit `M`**

Only finalize `MANIFEST.md`. It records:

- `AI_SKILLS_RESULT_COMMIT=E`
- `BRIDGE_CANDIDATE_COMMIT`
- `BRIDGE_VERSION`
- `BOBBIO_CANDIDATE_COMMIT`
- `LUCERNA_CANDIDATE_COMMIT`
- `MICA_CANDIDATE_COMMIT`
- `ASTERIA_CANDIDATE_COMMIT`
- `SEMINARARC_CANDIDATE_COMMIT`
- `CUHK_DATE_INSPECTED_REF`
- H1–H9 status/evidence locators

Independent implementation review targets `M`. `AI_SKILLS_MANIFEST_COMMIT=M` is reported in the Executor handoff, not written inside `M` itself.

No ledger/schema/state/controller is added.

## 0.1 New user amendment — Lite versioning default

The user additionally requires version discipline to be part of **Lite Handoff**, so fresh repositories do not invent arbitrary versioning conventions.

This is a bounded Bridge Lite amendment, not a new H10 and not a rewrite of existing repo histories. If Critic approves it in this v0.2 review, Bridge Kit may additionally update canonical `templates/prompts/AGENT_RULES.md` with the fallback contract in `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`.

Key rules:

- explicit current repo-local versioning policy wins;
- otherwise default formal version is `MAJOR.MINOR.PATCH`;
- PATCH = compatible repair; MINOR = compatible user-visible capability; MAJOR = incompatible contract/migration and needs explicit Planner/user approval;
- `0.y.z` may represent initial development; `1.0.0` is an explicit stability/default-use decision;
- `alpha` / `beta` / `rc` / `preview` / date or arbitrary prerelease suffixes are **opt-in only** when an approved repo lifecycle or explicit user/frozen task authorizes them;
- never reuse the same formal version for two different user-consumable runtime candidates;
- build labels/commit SHAs supplement identity but never substitute for the formal version when one is required;
- docs/TODO/test-only changes normally do not bump a release version;
- release-ready version/source/changelog parity must be truthful.

The root scaffold must not duplicate this policy; it only points to Lite and leaves room for a project-specific override.

## 1. Completion target

057 is complete only when two observable outcomes hold:

1. target repositories have internally coherent, navigable instruction surfaces with duplicate/stale ownership removed while important project-specific invariants remain discoverable;
2. Bridge Kit normal entry can initialize a fresh repo with a concise project-owned root AGENTS scaffold and canonical Lite rules, while existing project-owned root prose is not silently migrated or overwritten.

A shorter file, nicer headings, a template file merely existing, or grep-based rule presence is not completion.

## 2. Current drafting source refs

These are evidence locators only. Kickoff must re-check current authority before execution.

- `AI_Skills_Collection main@98d3bbb60d2d49181a6b77c4177afb7f90b1a362` at v0.2 drafting start; current main may advance with this package itself
- `GPT_Codex_AI_Bridge_Kit main@cb77b1cc5a1fce097a38066d2db452291e359852`, version `0.8.2`
- `Bobbio develop@0811116ac7197590f0af773f3c6296d4ca41db80`
- `Lucerna main@760931ae8a1f0edffefe41c83c1667c7190c3014`
- `Mica-for-ChatGPT main@aa4ce52581fff2e207d1f93600becbb3018b0efc`
- `Asteria main@166791c27752c70255043f026dcbda4deb693c04`
- `SeminarArc main@71c59d39f4d7e9cd3a3d813ad55d5cf6a38a4b11`
- `CUHK_Date main@711fab75f044b7ad31e5ff8610c076f902ccc949` — inspect only

Lucerna/CUHK Date advancing since v0.1 is treated as drafting-ref refresh only. Execution still performs kickoff-time authority checks; these ref movements do not by themselves reopen 057 design.

## 3. External basis

Current OpenAI evidence still supports progressive disclosure for project instructions. Semantic Versioning 2.0.0 supplies the conventional MAJOR/MINOR/PATCH meaning and makes prerelease labels optional extensions. 057 uses those numeric semantics only as the Lite fallback; local approved repo policy remains higher priority.

## 4. Mutation scope

### May modify after approved Kickoff

- `YuukiAS/GPT_Codex_AI_Bridge_Kit`
- `YuukiAS/Bobbio`
- `YuukiAS/Lucerna`
- `YuukiAS/Mica-for-ChatGPT`
- `YuukiAS/Asteria`
- `YuukiAS/SeminarArc`
- `YuukiAS/AI_Skills_Collection` only for 057 evidence/result/manifest/control artifacts

### Inspect only

- `YuukiAS/CUHK_Date`; no root AGENTS creation or project mutation

### Out of scope

- CARE Challenge, Server/VPS, EAT Research
- target product/runtime code
- 056 implementation
- central AI_Skills production plugins
- Bridge Host Policy / 056 Default prompt transport
- paid APIs/Terra
- new workflow states/controllers/ledgers/watchers

## 5. Git/source strategy after approved Kickoff

Exact temporary task branch in each mutable repo:

`reviewed/057_repo_agents_hygiene`

Bases:

- AI_Skills / Bridge / Lucerna / Mica / Asteria / SeminarArc: kickoff-time latest authorized `origin/main`
- Bobbio: kickoff-time current `origin/develop`

Use existing canonical local source first, inspect identity/origin/base/freshness/dirty ownership, protect unrelated dirty work, and create only the exact authorized isolation. Network clone only when no usable local source exists. No remote remap, force push, history rewrite, branch/tag deletion, PR, or main/develop merge.

Bobbio's temporary task branch is an approved isolation exception because this task rewrites repo-wide instruction authority; integration into `develop` still waits for independent implementation review and later integration approval.

## 6. Phase 0 — semantic-preservation baseline

Before editing any mutable repo, create in AI_Skills task branch:

- `results/057_repo_agents_hygiene/RESULT.md`
- `results/057_repo_agents_hygiene/SEMANTIC_PRESERVATION.md`
- `results/057_repo_agents_hygiene/SIZE_REPORT.md`
- `results/057_repo_agents_hygiene/MANIFEST.md`

Before a repo edit, its semantic-preservation table must map each changed/moved/merged hard rule to its surviving owner and evidence. Record source commit, root bytes/lines, delegated rule identity, managed-block identity where present, and canonical authority docs.

No rule may disappear merely because the resulting file is shorter.

## 7. Phase 1 — Bridge Kit scaffold + Lite default versioning

### 7.1 Root scaffold

Add `templates/repo/AGENTS_TEMPLATE.md` as a short project-owned structural scaffold with optional sections:

1. purpose/authority/precedence
2. read first/canonical locators
3. project scope/hard invariants
4. environment/source/Git
5. safety/data/authority
6. testing/acceptance/human boundary
7. design/UI/domain when applicable
8. version/release/integration
9. deeper docs/ownership

It must not fabricate project facts and must point to `prompts/AGENT_RULES.md` rather than copying Lite rules.

### 7.2 Lite versioning owner

If this v0.2 amendment passes Critic, update Bridge canonical `templates/prompts/AGENT_RULES.md` with a concise `Versioning default` section implementing §0.1. Existing explicit repository-local versioning policy remains higher priority. The fresh root scaffold contains only the locator/override concept, not a second copy.

### 7.3 Normal init behavior

Modify the existing `ai_bridge_kit/cli.py` path only:

- fresh repo without root AGENTS -> scaffold + exactly one canonical managed block;
- existing root -> preserve project-owned prose; only append/update managed block;
- `--force` must not migrate/reformat project-owned root content;
- existing opt-out semantics remain unchanged;
- no new migration mode or migration engine.

### 7.4 Bridge tests

Focused tests through real init/validate behavior:

- fresh directory -> scaffold + one managed block + `prompts/AGENT_RULES.md` locator;
- generated Lite rule surface contains the approved fallback versioning contract if amendment passes;
- `ai-bridge validate` succeeds;
- second init is idempotent;
- custom existing root remains byte-for-byte preserved outside managed block under normal and force init;
- no duplicate managed block;
- root contains no copied Lite/versioning policy;
- no fabricated project invariant.

Then run canonical Bridge full tests once stable.

### 7.5 Bridge release candidate

Combined fresh-scaffold + approved Lite versioning fallback remains a compatible PATCH candidate `0.8.2 -> 0.8.3`, only after H7–H9/full regression pass. Synchronize canonical version, README and CHANGELOG under current Bridge release policy. Do not rewrite historical versions.

## 8. Phase 2 — Bobbio authority closure + reorganization

Allowed files:

- `AGENTS.md`
- `docs/PRODUCT_DESIGN_BRIEF.md` — **only** visual/source-of-truth wording required by C057-E1
- `docs/DEVELOPMENT_WORKFLOW.md` only when a unique moved detail needs its canonical owner
- `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md` only when a unique moved acceptance detail needs its canonical owner

No Figma/product/runtime/schema/version change.

Required final authority:

- Figma = canonical visual design/components/screen composition;
- Product Design Brief = durable product/interaction constraints;
- old Bobbio design PNGs = historical/supporting references.

`AGENTS.md` must read `FIGMA_HANDOFF.md` for frontend/Product Design work and consolidate duplicated general GUI/human/pre-user acceptance text without weakening Zotero isolation/authority, native Windows acceptance, knowledge/provenance, roadmap/versioning or iPad/Pencil constraints.

H2 directly compares final `AGENTS.md`, `FIGMA_HANDOFF.md`, and `PRODUCT_DESIGN_BRIEF.md`; locator existence alone cannot PASS.

## 9. Phase 3 — Lucerna light normalization

Allowed: project-owned `AGENTS.md` only. Managed Bridge block stays canonical/unchanged.

Keep separate project-specific owners for Windows release/tray lifecycle, live provider truth/no mock release evidence, matching regression, screenshot helper/evidence budget, and Longleaf source/permission boundaries. Only remove true local duplication/reorder headings.

## 10. Phase 4 — Mica testing consolidation

Allowed: `AGENTS.md` only.

Merge repeated development-testing-budget/test-tier/focused-iteration prose into one testing ladder while preserving real-failure reproduction, privacy-safe diagnostics, fail-open ChatGPT DOM behavior, authenticated-account safety, typing hot path, stable `dist/mica-dev`, runtime-version identity, and final manual authenticated long-conversation acceptance. Automated authenticated ChatGPT regression remains forbidden.

No runtime/version change.

## 11. Phase 5 — Asteria map conversion

Allowed:

- `AGENTS.md`
- new `docs/operations/development/RUNTIME_OPERATIONS.md`

Move volatile tunnel/server/dev-server mechanics into the single runtime owner. Root retains fixed public-entry invariant, canonical browser-contract locator + `可以自动操作页面；不能绕过页面`, GPT Work-before-human gate, locator to `prompts/AGENT_RULES.md` for visual/scientific/generic-fix rules, stable Git/version boundaries and runtime-operations locator.

Do not modify product/runtime or `prompts/AGENT_RULES.md`; a real delegated-rule contradiction is a stop/Planner condition.

## 12. Phase 6 — SeminarArc owner closure + map conversion

Allowed:

- `AGENTS.md`
- `docs/DEVICE_TESTING.md`

No product/Android/runtime changes and no third environment/device manual.

Final ownership:

- root AGENTS = prominent safety summary + locator;
- DEVICE_TESTING = detailed device/environment/test mechanics, command restrictions, volatile inventory, mixed-inventory process and historical incident evidence.

Update the stale `DEVICE_TESTING -> AGENTS contains complete rules` wording accordingly.

Root must visibly retain:

- Emulator-first;
- protected physical device not a generic connected/instrumentation target;
- no agent automatic transport reset/recovery;
- authorized physical writes use explicit verified serial + preflight/postflight;
- physical-device failure does not block independent WSL/headless/Emulator work;
- PIN/secrets never enter repo/task/result/log/screenshot/commit.

H2/H3/H6 must directly validate this owner closure and preservation.

## 13. Phase 7 — CUHK Date inspect only

Read current prototype instruction surface and record current ref + `NO_CHANGE` unless a new direct contradiction appears. Do not create root AGENTS or copy the scaffold into the existing repo for symmetry.

## 14. H1–H9 acceptance matrix

- **H1 Semantic preservation:** every changed/moved hard rule has a surviving canonical owner.
- **H2 No internal contradiction:** directly compare final root/delegated authorities; mandatory Bobbio three-way and SeminarArc root/DEVICE_TESTING owner checks.
- **H3 Discoverability:** a new agent starting at root reaches current design/safety/testing/runtime owners without historical archaeology.
- **H4 Managed-block integrity:** product-repo managed blocks are not hand-forked; fresh block comes from canonical Bridge source.
- **H5 Context quality:** before/after bytes/lines are reported where meaningful; no numeric reduction can override H1/H6.
- **H6 Repo-specific regression:** Zotero/Bobbio design/native; Lucerna Windows/provider/Longleaf; Mica account/typing/testing; Asteria fixed URL/browser/visual; SeminarArc device safety; CUHK prototype semantics remain protected.
- **H7 Fresh Bridge normal entry:** real `ai-bridge init -> validate` proves scaffold, one managed block, Lite locator, no fake project facts, and—if versioning amendment passes—the generated Lite surface contains the approved fallback versioning contract.
- **H8 Existing-repo should-not-change:** real normal/force init fixture preserves custom project-owned root prose and does not auto-migrate it.
- **H9 No Lite duplication:** root does not copy Lite execution/versioning policy or create a second authority.

No H10 is added.

## 15. Final-candidate identity — two-stage closure

### Stage A: evidence/result commit `E`

After repo candidate commits and H1–H9 replays are stable, finalize `RESULT.md`, `SEMANTIC_PRESERVATION.md`, `SIZE_REPORT.md` and evidence locators in one AI_Skills commit `E`. Those files may describe candidate identities known before `E`, but do not contain a field requiring their own containing commit SHA.

### Stage B: manifest closure commit `M`

Then update only `MANIFEST.md` to record:

- `AI_SKILLS_RESULT_COMMIT=E`
- Bridge candidate commit/version
- Bobbio/Lucerna/Mica/Asteria/SeminarArc candidate commits
- CUHK Date inspected ref
- H1–H9 status + evidence locators

Commit that as `M`. Do not write `M`'s own SHA inside the tracked manifest. Executor handoff reports `AI_SKILLS_MANIFEST_COMMIT=M` externally.

Independent implementation review targets the exact tuple bound by `M`. Any semantic post-`E` change requires a new evidence commit and manifest closure; different candidates cannot be spliced together.

## 16. Recovery / should-not-change

- If authority cannot be resolved, preserve content and report `EVIDENCE_NEEDED`; do not delete by style preference.
- If unrelated dirty instruction work cannot be isolated, stop that repo rather than overwrite/stash/reset it.
- If moved safety content lacks a canonical surviving owner, restore/retain it and fail H1.
- If Bridge existing-repo init mutates project-owned root text, fail H8 and do not bump/release.
- No product runtime/version changes in target repos.
- No main/develop merge under this Goal.
- No 056 edit/execution.

## 17. Future all-active-repo adaptation

After 057 **and** 056 are integrated, Planner will open a separate reviewed major round for the user's requested complete adaptation of all currently active repositories. It will inventory Bridge/Lite identity, root/delegated AGENTS, version authority/parity, explicit local version-policy overrides, prerelease-history decisions, and final 056 consumption. 057 does not silently extend mutation scope to those repos now.

## 18. Commit/push and handoff

After an approved Kickoff, ordinary commits/push are allowed only to the exact temporary task branches. Stop at implementation handoff after `M` is pushed. No integration/release/main merge is implied.

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`
