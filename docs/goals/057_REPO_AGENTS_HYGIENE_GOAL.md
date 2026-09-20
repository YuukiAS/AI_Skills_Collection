# 057 Repo AGENTS Hygiene — Canonical Goal

- Execution package version: `v0.2`
- Task key: `057_repo_agents_hygiene`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Plan: `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.2
- Kickoff: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` v0.2
- Approved design authority: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Bounded amendment pending this review: `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`

This Goal is not executable until independent Critic reviews this exact v0.2 Plan + Goal + Kickoff, including the bounded Lite versioning amendment, returns `READY_FOR_CODEX=YES`, and the user then sends the approved Kickoff.

## 0. Positive target

Clean the target repositories' own instruction surfaces without losing important project-specific rules, add a reusable Bridge Kit root-AGENTS scaffold for future fresh repositories, and—if the bounded amendment is approved—put a stable fallback version-number policy in Lite Handoff so new repos do not invent arbitrary version schemes.

Completion requires behavior/evidence, not shorter Markdown:

- duplicate/stale/conflicting authority inside each target repo is resolved or explicitly retained as evidence-needed;
- every moved/deleted hard rule has a surviving owner;
- Bobbio and SeminarArc authority ownership is internally consistent;
- Bridge real `ai-bridge init` consumes the scaffold for fresh repos while existing project-owned root prose remains preserved;
- root does not duplicate Lite execution/versioning authority;
- H1–H9 pass on the same final candidate tuple;
- final candidate identity uses the non-self-referential `E -> M` closure.

## 1. Authorized scope after approved Kickoff

### AI_Skills_Collection

Only 057 task evidence/result/manifest/control artifacts on exact branch:

`reviewed/057_repo_agents_hygiene`

No central plugin production change and no 056 implementation.

### GPT_Codex_AI_Bridge_Kit

Exact branch:

`reviewed/057_repo_agents_hygiene`

Implement only:

- `templates/repo/AGENTS_TEMPLATE.md`;
- real fresh/existing root-AGENTS init behavior in current `ai-bridge init` path;
- tests/docs/changelog/version candidate;
- if Critic approves the bounded amendment, concise fallback versioning rules in canonical `templates/prompts/AGENT_RULES.md`.

Do not modify Bridge Host Policy, 056 Default prompt transport, Review/Control state machines, or build a migration engine.

Bridge `0.8.3` remains only a candidate until H7–H9/full regression pass.

### Bobbio

Exact branch from kickoff-time `origin/develop`:

`reviewed/057_repo_agents_hygiene`

Allowed files:

- `AGENTS.md`
- `docs/PRODUCT_DESIGN_BRIEF.md` only for visual/source-of-truth wording
- `docs/DEVELOPMENT_WORKFLOW.md` only for a unique moved detail
- `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md` only for a unique moved acceptance detail

No Figma/product/runtime/schema/version change.

### Lucerna

Exact branch from kickoff-time `origin/main`:

`reviewed/057_repo_agents_hygiene`

Allowed: project-owned `AGENTS.md` only; managed Bridge block remains canonical.

### Mica-for-ChatGPT

Exact branch from kickoff-time `origin/main`:

`reviewed/057_repo_agents_hygiene`

Allowed: `AGENTS.md` only. No runtime/version change.

### Asteria

Exact branch from kickoff-time `origin/main`:

`reviewed/057_repo_agents_hygiene`

Allowed:

- `AGENTS.md`
- new `docs/operations/development/RUNTIME_OPERATIONS.md`

No product/runtime or `prompts/AGENT_RULES.md` change under this Goal.

### SeminarArc

Exact branch from kickoff-time `origin/main`:

`reviewed/057_repo_agents_hygiene`

Allowed:

- `AGENTS.md`
- `docs/DEVICE_TESTING.md`

No Android/runtime/product change and no third device/environment manual.

### CUHK Date

Inspect only. Do not create root `AGENTS.md` and do not modify the repo.

## 2. Source/dirty preflight

For every mutable repo:

- discover existing canonical local source first;
- verify repo identity/origin/base/freshness/dirty ownership;
- protect unrelated dirty work;
- create only the exact task branch/worktree authorized by Kickoff;
- network clone only when no usable local source exists;
- no remote remap, force push, history rewrite, branch/tag deletion, PR or main/develop merge.

If an exact task branch already exists with ambiguous ownership, stop that repo and report it rather than inventing a different branch.

## 3. Semantic-preservation contract

Before editing a repo, record its changed/moved hard rules in:

`results/057_repo_agents_hygiene/SEMANTIC_PRESERVATION.md`

For every rule record old owner, keep/move/merge decision, new canonical owner, and evidence for duplication/supersession. Safety/data/authority rules cannot disappear for size/style reasons.

## 4. Bridge Kit contract

### Fresh repo

Normal `ai-bridge init` with no root AGENTS must create:

- concise root from `templates/repo/AGENTS_TEMPLATE.md`;
- exactly one managed Bridge block from canonical source;
- locator to `prompts/AGENT_RULES.md`;
- no fabricated project facts;
- no copied Lite policy in root.

If versioning amendment is approved, generated `prompts/AGENT_RULES.md` must contain the generic fallback versioning contract while root only points to it.

### Existing repo

Normal and force init preserve project-owned root prose and only install/update canonical managed/generated Bridge content under existing semantics. No automatic scaffold migration/reformatting.

### Lite versioning fallback, if approved

Precedence:

1. current user/frozen task;
2. explicit current repo-local versioning policy;
3. Lite fallback.

Fallback:

- formal version `MAJOR.MINOR.PATCH`;
- PATCH = compatible repair;
- MINOR = compatible user-visible capability;
- MAJOR = incompatible contract/migration and requires explicit Planner/user approval;
- `0.y.z` allowed for initial development; `1.0.0` is an explicit stability/default-use decision;
- `alpha`/`beta`/`rc`/preview/date/arbitrary prerelease labels are not invented unless an approved repo lifecycle or explicit task/user authorization exists;
- one formal version cannot identify two different user-consumable runtime candidates;
- commit/build labels supplement but do not replace formal version;
- release-ready version/source/changelog parity must be truthful.

## 5. Per-repo outcome contract

### Bobbio

Final authority must be consistent in `AGENTS.md`, `FIGMA_HANDOFF.md`, and `PRODUCT_DESIGN_BRIEF.md`:

- Figma = current canonical visual design/components/screen composition;
- Product Design Brief = durable product/interaction constraints;
- old `Bobbio_Design_*.png` = historical/supporting references.

Add Figma handoff to frontend/Product Design required reads, consolidate repeated general GUI/human/pre-user wording, and preserve Zotero/native/knowledge/roadmap/iPad/Pencil constraints.

### Lucerna

Light normalization only. Preserve Windows release/tray, real-provider truth, matching regression, screenshot helper/evidence budget and Longleaf boundaries as distinct project-specific rules.

### Mica

Consolidate repeated testing prose into one ladder. Preserve real-failure reproduction, diagnostics/privacy, authenticated-account safety, fail-open behavior, typing hot path, stable build path/runtime identity and final manual authenticated long-conversation acceptance. Automated authenticated ChatGPT regression remains forbidden.

### Asteria

Root becomes map + hard invariants. Volatile runtime/tunnel/dev-server mechanics move to the single `RUNTIME_OPERATIONS.md` owner. Root keeps fixed public URL, browser-contract locator + `可以自动操作页面；不能绕过页面`, GPT Work-before-human gate, visual/scientific locator and stable Git/release boundaries.

### SeminarArc

Final ownership:

- root = prominent physical-device safety summary + locator;
- `docs/DEVICE_TESTING.md` = detailed device/environment/testing mechanics, command restrictions, volatile inventory and incident evidence.

Root must visibly retain Emulator-first, protected device not generic connected-test target, no automatic transport recovery/reset, explicit verified serial + pre/postflight for authorized physical writes, device-channel failure not blocking independent WSL/headless/Emulator work, and PIN/secret non-disclosure.

### CUHK Date

Inspect-only `NO_CHANGE` unless a new direct contradiction is found; no root AGENTS creation for symmetry.

## 6. H1–H9 gates

- H1 semantic preservation
- H2 no internal contradiction, including direct Bobbio three-way and SeminarArc owner comparison
- H3 discoverability from root to current canonical owners
- H4 managed-block integrity
- H5 context quality without numeric gaming
- H6 repo-specific regression protections
- H7 real fresh `ai-bridge init -> validate`, including Lite versioning fallback if amendment passes
- H8 real existing-root normal/force init preservation
- H9 no Lite/versioning duplication in root

Do not add H10.

## 7. Final candidate — two-stage identity

### Stage A: result/evidence commit `E`

Finalize:

- `RESULT.md`
- `SEMANTIC_PRESERVATION.md`
- `SIZE_REPORT.md`
- H1–H9 evidence/locators

Do not write `E`'s own SHA into tracked content in `E`.

### Stage B: manifest closure commit `M`

Update only `MANIFEST.md` with:

- `AI_SKILLS_RESULT_COMMIT=E`
- Bridge candidate commit/version
- Bobbio/Lucerna/Mica/Asteria/SeminarArc candidate commits
- CUHK Date inspected ref
- H1–H9 status/evidence locators

Commit as `M`. Do not write `M`'s own SHA into the tracked manifest. Executor handoff reports `AI_SKILLS_MANIFEST_COMMIT=M` externally. Independent implementation review targets the exact tuple bound by `M`.

## 8. Explicit non-goals

Do not:

- change application/runtime code;
- redesign products/science;
- change Bridge Host Policy or 056 transport;
- implement/edit 056;
- duplicate Lite rules into root scaffold;
- auto-migrate existing repos;
- modify target product repos' delegated `prompts/AGENT_RULES.md`;
- normalize existing repos' release histories/prerelease labels under 057;
- bulk-translate for cosmetic uniformity;
- create new states/controllers/watchers/ledgers;
- call paid APIs/Terra;
- mutate CUHK Date/CARE/Server/EAT.

## 9. Stop/recovery

Stop affected repo and preserve content when authority is unresolved, unrelated dirty work cannot be safely isolated, semantic-preservation mapping cannot prove a surviving owner, managed block is unexpectedly drifted, or cleanup would require product/runtime mutation.

Bridge H7/H8/H9 failure means no Bridge version bump/release claim.

## 10. Future all-repo adaptation

After both 057 and 056 are integrated, Planner will open a separate reviewed major round for complete adaptation of all active repos: Bridge/Lite identity, root/delegated AGENTS, versioning authority/parity, intentional local overrides/prerelease history, and final 056 consumption. This Goal does not mutate those additional repos now.

## 11. Handoff

Approved Kickoff may authorize ordinary commit/push only to exact temporary task branches. No integration/main/develop merge/release under this Goal.

After `M` is pushed, stop at implementation handoff (`EXECUTED_UNAUDITED` or legal equivalent) for independent review. Executor must not amend or execute 056.

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`
