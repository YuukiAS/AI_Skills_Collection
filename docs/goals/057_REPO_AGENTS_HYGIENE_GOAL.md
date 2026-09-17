# 057 Repo AGENTS Hygiene — Canonical Goal

- Execution package version: `v0.1`
- Task key: `057_repo_agents_hygiene`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Plan: `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.1
- Kickoff: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` v0.1
- Approved design authority: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`

This Goal is not executable until an independent Critic reviews the exact v0.1 Plan + Goal + Kickoff and returns `READY_FOR_CODEX=YES`, and the user then sends the approved Kickoff.

## 0. Positive target

Clean the target repositories' instruction surfaces without losing important project-specific rules, and add a reusable Bridge Kit root-AGENTS scaffold for future fresh repositories.

Completion requires real instruction-surface quality and real Bridge init behavior:

- duplicates/stale authority inside each target repo are resolved or explicitly preserved as `EVIDENCE_NEEDED`;
- every moved/deleted hard rule has a surviving canonical owner;
- root AGENTS become maps + hard project invariants rather than chronological incident manuals where the approved design calls for that change;
- Bridge `ai-bridge init` actually consumes the new scaffold for a fresh repo;
- existing custom AGENTS remain untouched outside the managed Bridge block, including under force init;
- no Lite execution policy is duplicated into root;
- H1–H9 pass on the same final candidate set.

A Markdown cleanup or line-count reduction alone is not completion.

## 1. Authorized implementation scope after approved Kickoff

### AI_Skills_Collection

Only 057 task evidence/result/control artifacts on branch:

`reviewed/057_repo_agents_hygiene`

No central plugin production change.

### GPT_Codex_AI_Bridge_Kit

Implement:

- `templates/repo/AGENTS_TEMPLATE.md`;
- fresh-repo scaffold consumption in the existing `ai-bridge init` path;
- existing-repo/force preservation behavior;
- focused/full tests;
- Bridge `0.8.3` candidate metadata/docs only after H7–H9 pass.

Branch after approved Kickoff:

`reviewed/057_repo_agents_hygiene`

### Bobbio

Branch from current `develop`:

`reviewed/057_repo_agents_hygiene`

Allowed instruction/doc files only:

- `AGENTS.md`
- `docs/DEVELOPMENT_WORKFLOW.md` if required for moved unique detail
- `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md` if required for moved unique detail

No product/Figma/runtime change.

### Lucerna

Branch from current `main`:

`reviewed/057_repo_agents_hygiene`

Allowed: `AGENTS.md` only.

### Mica-for-ChatGPT

Branch from current `main`:

`reviewed/057_repo_agents_hygiene`

Allowed: `AGENTS.md` only.

### Asteria

Branch from current `main`:

`reviewed/057_repo_agents_hygiene`

Allowed:

- `AGENTS.md`
- `docs/operations/development/RUNTIME_OPERATIONS.md`

No product/runtime or `prompts/AGENT_RULES.md` mutation under this Goal.

### SeminarArc

Branch from current `main`:

`reviewed/057_repo_agents_hygiene`

Allowed:

- `AGENTS.md`
- `docs/DEVICE_TESTING.md`

No Android/runtime/product change.

### CUHK Date

Inspect only. Do not create root `AGENTS.md` and do not modify the repo.

## 2. Source/dirty preflight

For every repo:

- locate existing canonical local source first;
- verify repo identity/origin/base ref/freshness/dirty ownership;
- preserve unrelated dirty work;
- create only the exact task branch/worktree authorized by the Kickoff;
- do not network clone when usable canonical local source exists;
- do not remap remotes, force push, rewrite history or delete branches/tags.

Source or instruction-file conflicts that cannot be isolated safely stop that repo and return evidence rather than overwriting user work.

## 3. Semantic-preservation contract

Before editing a repo, record its current hard rules in:

`AI_Skills_Collection/results/057_repo_agents_hygiene/SEMANTIC_PRESERVATION.md`

For every rule changed/moved/merged record:

- old owner/location;
- keep/move/merge decision;
- new canonical owner/location;
- evidence for supersession or duplication.

A rule can disappear from root only because it is a real duplicate, moved behind a clear canonical locator, superseded by evidenced current authority, or historical narrative reduced to a durable invariant with evidence preserved.

Never remove safety/data/authority rules merely to reduce size.

## 4. Bridge Kit contract

### Fresh repo

Normal `ai-bridge init` with no root `AGENTS.md` must create:

- concise project-owned scaffold from `templates/repo/AGENTS_TEMPLATE.md`;
- exactly one managed Bridge block generated from `codex/AGENTS_SNIPPET.md`;
- locator to `prompts/AGENT_RULES.md`;
- no fabricated project-specific facts;
- no copied Lite rule set.

### Existing repo

Normal and force init preserve project-owned root prose and only install/update managed/generated Bridge content according to existing semantics. No automatic scaffold migration/reformatting.

### Release candidate

If and only if focused/full tests plus H7–H9 pass, Bridge candidate becomes `0.8.3`. Otherwise remain on current baseline and report the failed behavior.

## 5. Per-repo outcome contract

### Bobbio

- `docs/design/FIGMA_HANDOFF.md` becomes explicit frontend/Product Design required read;
- Figma = current visual authority;
- Product Design Brief = durable product/interaction constraints;
- four old design PNGs = supporting/historical references only;
- consolidate repeated general GUI/human-gate/pre-user QA wording;
- preserve Zotero isolation/authority, Windows-native acceptance, knowledge/provenance, roadmap/versioning and iPad/Pencil constraints.

### Lucerna

Light normalization only. Preserve Windows release/tray, real-provider truth, matching regression, screenshot helper/evidence budget and Longleaf boundaries as distinct project rules. Managed Bridge block remains unchanged.

### Mica

Consolidate testing prose into one ladder while preserving real-failure reproduction, built-in diagnostics, authenticated-account safety, typing hot path, stable build path and final manual real-site long-conversation acceptance. Do not turn real-site acceptance into an automated authenticated loop.

### Asteria

Root becomes a concise map + hard invariants. Move volatile runtime/tunnel/dev-server mechanics into `docs/operations/development/RUNTIME_OPERATIONS.md`. Root retains fixed public-entry invariant, browser-contract locator + `可以自动操作页面；不能绕过页面`, GPT Work-before-human gate, visual/scientific-rule locator and stable Git/release boundaries.

### SeminarArc

Root retains prominent physical-device safety summary and project invariants. Long environment snapshots, command bans and historical incident detail move to `docs/DEVICE_TESTING.md` only after semantic preservation is proven. Emulator-first and protected-device safety must remain impossible to miss from root.

### CUHK Date

Inspect and record `NO_CHANGE` unless a new direct contradiction exists. No root file is created for symmetry.

## 6. H1–H9 gates

H1 Semantic preservation — every changed/moved hard rule has a surviving owner.

H2 No internal contradiction — final root/delegated authorities do not compete on current design/test/user-action authority.

H3 Discoverability — starting from root, a new agent can reach current design/safety/testing/runtime authority through explicit locators.

H4 Managed-block integrity — existing product-repo Bridge blocks are unchanged; fresh block comes from canonical Bridge source.

H5 Context quality — report before/after root bytes/lines; improvement is qualitative and may not trade away H1/H6.

H6 Repo-specific regression — all unique protections listed in Plan §14 remain directly discoverable.

H7 Fresh Bridge scaffold — real `ai-bridge init` + `validate` on a fresh temporary repo produces the approved scaffold behavior.

H8 Existing-repo should-not-change — normal and force init preserve custom project-owned AGENTS outside the managed block.

H9 No Lite duplication — root points to `prompts/AGENT_RULES.md` without copying its execution-policy authority.

Do not add H10 or another workflow gate merely because implementation is inconvenient.

## 7. Result artifacts and final candidate

AI_Skills task branch must contain:

- `results/057_repo_agents_hygiene/RESULT.md`
- `results/057_repo_agents_hygiene/SEMANTIC_PRESERVATION.md`
- `results/057_repo_agents_hygiene/SIZE_REPORT.md`
- `results/057_repo_agents_hygiene/MANIFEST.md`

Freeze exact candidate commits for Bridge, Bobbio, Lucerna, Mica, Asteria and SeminarArc, plus CUHK Date inspected ref and H1–H9 evidence.

Any semantic post-freeze edit invalidates affected instruction-quality evidence.

## 8. Explicit non-goals

Do not:

- change application/runtime code;
- redesign products/science;
- change Bridge Host Policy or 056 prompt transport;
- implement 056;
- copy 056 Lite rules into root template;
- auto-migrate existing repos;
- modify `prompts/AGENT_RULES.md` in product repos under 057;
- bulk-translate repos for cosmetic uniformity;
- create new workflow states/controllers/watchers/ledgers;
- call paid APIs/Terra;
- mutate CUHK Date root policy;
- mutate CARE/Server/EAT.

## 9. Stop/recovery conditions

Stop the affected repo and return evidence when:

- authority conflict cannot be resolved from current source;
- instruction file contains unrelated user-owned dirty edits that cannot be safely isolated;
- preservation mapping cannot prove where a removed hard rule survives;
- Bridge scaffold would require a migration engine/new state system;
- existing-repo init cannot preserve custom prose;
- managed Bridge block has unexplained drift;
- requested cleanup would require product/runtime changes.

Do not lower the preservation bar to make a shorter AGENTS file.

## 10. Commit/push and handoff

Approved Kickoff may authorize ordinary commits/push only to the exact task branches above. No merge into `main`/`develop` under this Goal.

After implementation/self-validation/H1–H9 evidence, stop at implementation handoff (`EXECUTED_UNAUDITED` or legal equivalent). An independent implementation review must inspect actual final diffs and preservation evidence before integration.

After 057 integration, Planner performs a separate bounded 056 source-drift revalidation. Executor must not amend or execute 056 itself.

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`
