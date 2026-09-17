# 057 Repo AGENTS Hygiene — Same-task Implementation Repair Prompt

TASK_KEY = `057_repo_agents_hygiene`

Stage: independent implementation review -> bounded same-task repair

This prompt repairs the already-approved 057 implementation. It does **not** redesign 057, create a successor, start 056, create new branch names, merge `main`/`develop`, or authorize paid APIs.

## Frozen authority

Keep the approved v0.2 Plan/Goal, repo dispositions, H1–H9, task-branch isolation, Bridge scaffold direction, Bridge `0.8.3` candidate direction, and sequence:

`057 repair -> independent implementation review -> separately approved integration -> bounded 056 source-drift revalidation`.

Historical failed tuple must remain immutable evidence:

- AI_Skills manifest M: `0a7198277dd9575010904f05b642deefffd00009`
- AI_Skills evidence/result E: `519c7da37979c8aa23aa98069c146b5cea1dd81c`
- Bridge: `a5c4fe61dc9ab0e228822e854ace5c7e50a4d967`
- Bobbio: `dd977705a2cdfecaa2d4e09127ab4464ae898b32`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829`
- Mica: `7afb2277cd1001204e77e4987d9fcaa447e7c675`
- Asteria: `b34f6c5d27dd9ac7b1193826ac878fca4a953fb5`
- SeminarArc: `c3fc5a64a3abaec7860808fbcb4082b95d2a0302`
- CUHK Date inspected ref: `711fab75f044b7ad31e5ff8610c076f902ccc949`

Continue only on the existing `reviewed/057_repo_agents_hygiene` branches/worktrees. Do not create a new task/successor/branch name. Before edits, verify each existing worktree/branch still points to the expected 057 task lineage and preserve unrelated dirty work.

## 1. Bridge — close H8 byte preservation

Repair the existing `install_agents_snippet()` path; do not add a migration engine or alternate init path.

Current defect: existing-root append/replace uses `rstrip()` / `lstrip()`, so bytes outside the managed marker span are not preserved exactly.

Required behavior:

1. Existing `AGENTS.md` without managed block:
   - preserve the original project-owned text exactly as the prefix;
   - append only the minimum deterministic separator plus canonical managed block;
   - do not strip/normalize project-owned whitespace.
2. Existing `AGENTS.md` with managed block + `--force`:
   - replace only the bytes/text from `<!-- ai-bridge-kit:start -->` through `<!-- ai-bridge-kit:end -->` and the managed block's own canonical newline handling;
   - project-owned content before and after the marker span must remain exactly unchanged.
3. Normal second init remains idempotent and must not duplicate the block.

Add focused regression fixtures with project prose **before and after** the managed block plus deliberately irregular blank lines/trailing whitespace. Compare pre/post project-owned segments exactly, not `startswith(existing.rstrip())`.

Re-run H8 through the real normal and `--force` CLI path.

## 2. Bridge — version closure and Lite versioning amendment

Keep Bridge at candidate `0.8.3`; this repair is still part of the same unreleased candidate, so do **not** mechanically bump to `0.8.4`.

Required repair:

- synchronize README current version to `0.8.3` candidate while making no GitHub release/tag/main-merge claim;
- keep `__version__`, `pyproject.toml`, CHANGELOG, README and package/user-facing identity consistent for the final candidate;
- in canonical `templates/prompts/AGENT_RULES.md`, retain the approved fallback versioning rules and add the two missing explicit boundaries:
  1. docs/TODO/test-only changes that do not alter a user-consumable release normally do not require a version bump;
  2. intermediate implementation commits may remain unreleased; bump when forming the next actual user-consumable candidate/release according to the repo-local contract.

Preserve all already-approved rules:

- explicit repo-local version policy wins;
- otherwise fallback `MAJOR.MINOR.PATCH`;
- prerelease `alpha` / `beta` / `rc` / preview/date labels are opt-in only;
- do not reuse one formal version for two different user-consumable candidates;
- version/source/changelog/package/user-facing identity must agree before release-ready status.

Do not copy this versioning policy into root `AGENTS_TEMPLATE.md`.

Add focused tests/inspection that prove a fresh real Lite init consumes the **complete** fallback semantics, including the two new boundaries; do not treat grep for `MAJOR.MINOR.PATCH` alone as H7 evidence. Then rerun Bridge full regression once on the stable repaired candidate.

## 3. Mica — actually consolidate the testing ladder

Modify only the existing 057-authorized `AGENTS.md`; do not change runtime/version.

The current candidate only renamed headings. Replace the overlapping `Development testing budget` / `Test tiers` / `Focused iteration before full E2E` prose with one coherent ladder:

`impact audit + smallest focused checks -> npm test -> Tier 2 full E2E only when indicated -> stress only when indicated -> final manual authenticated real-site acceptance`.

Remove duplicated statements rather than keeping all three blocks with new headings.

Must preserve explicitly:

- same focused failure twice -> inspect source/fixture/validator before another rerun;
- privacy-safe built-in diagnostics;
- fail-open behavior for unstable ChatGPT DOM/private endpoints;
- typing hot-path constraints;
- stable `dist/mica-dev` identity;
- automated authenticated ChatGPT regression remains forbidden;
- final real long-conversation check is manual authenticated acceptance.

## 4. Asteria — complete the map conversion

Stay within existing 057 files:

- `AGENTS.md`
- `docs/operations/development/RUNTIME_OPERATIONS.md`

Do not modify `prompts/AGENT_RULES.md`.

Required repair:

1. Move the remaining root `## Dev Server` startup/port/background/Windows fallback mechanics into the single `RUNTIME_OPERATIONS.md` owner.
2. Root keeps only stable dev/runtime locator and true project-wide invariant.
3. Collapse the root Browser section to:
   - canonical `UI_BLACKBOX_BROWSER_CONTRACT.md` locator;
   - stable requirement that the canonical contract must be inlined into GPT Work prompts when that remains the project contract;
   - essential invariant `可以自动操作页面；不能绕过页面`.
   Detailed fallback/browser-tool/timeout/contamination/result mechanics remain in the canonical Browser contract, not duplicated in root.
4. Keep GPT Work-before-human acceptance gate prominent.
5. Keep visual self-QA / scientific graph / generic-fix locators discoverable through the existing delegated rules.

Re-run H1/H2/H3/H5/H6 by semantic inspection, not line-count alone.

## 5. SeminarArc — complete the map conversion

Stay within:

- `AGENTS.md`
- `docs/DEVICE_TESTING.md`

Do not create a third device/environment manual and do not change Android/runtime/product source.

Root must become the prominent **safety summary + locator**, not the full historical/device manual. Keep these items visibly in root:

- Emulator-first;
- protected physical device is not a generic connected/instrumentation target;
- agent must not automatically reset/recover ADB/USB/usbipd/transport;
- any specifically authorized physical write uses explicit verified serial plus preflight/postflight;
- physical-device channel failure does not block independent WSL/headless/Emulator work;
- PIN/secret never enters repo/task/result/log/screenshot/commit.

Move detailed environment inventory, exact SDK/JDK/cache mechanics, mixed-inventory procedure, command-ban detail, historical disconnect evidence, harness/transport mechanics into existing `docs/DEVICE_TESTING.md`. Preserve all unique safety semantics there; do not weaken them while shortening root.

Keep root project-skill locators, product/0.1.x hard invariants, internal-dogfood boundary and Compose architecture rules.

Re-run H1/H2/H3/H5/H6.

## 6. Bobbio — complete the approved consolidation

Do **not** alter the already-correct three-way visual authority closure.

Within the existing authorized Bobbio instruction/doc files, perform the originally approved minimal substantial reorganization:

- consolidate repeated general GUI/human-gate/pre-user-review/anti-blocking mechanics;
- where `docs/DEVELOPMENT_WORKFLOW.md` or `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md` already owns detailed mechanics, root keeps the Bobbio-specific hard invariant + locator rather than duplicating the long procedure;
- preserve all Zotero isolation/update safety, native acceptance, knowledge/provenance, version/roadmap, and iPad/Pencil hard rules.

Do not change Figma, product design semantics, runtime, schema or app version.

## 7. Lucerna / CUHK Date

No new blocker.

- Lucerna remains LIGHT_EDIT only; keep Windows/tray, real provider, matching regression, screenshot helper and Longleaf as distinct invariants. If the added meta-summary is pure repetition, it may be simplified only when discoverability is not reduced.
- CUHK Date remains inspect-only at `711fab75f044b7ad31e5ff8610c076f902ccc949`; no root `AGENTS.md` creation.

## 8. Evidence and new final tuple

Do not rewrite or amend old failed `E` / `M` or their candidate commits.

After semantic repairs:

1. create new commits on the **existing** 057 branches for every affected repo;
2. run `git diff --check` for every final candidate;
3. rerun affected H1–H9; H5 needs qualitative semantic review, not existence of `SIZE_REPORT.md`;
4. H7/H8 must use real normal-entry Bridge CLI behavior;
5. run the Bridge full test suite once on the stable repaired candidate;
6. create new AI_Skills evidence/result commit `E2` containing finalized `RESULT.md`, `SEMANTIC_PRESERVATION.md`, `SIZE_REPORT.md` and H1–H9 evidence, without self-reference;
7. create new manifest-only closure commit `M2` binding `E2`, every exact final candidate commit, CUHK Date inspected ref, Bridge candidate version and H1–H9 evidence locators;
8. do not write `M2`'s own SHA inside tracked `MANIFEST.md`; report `AI_SKILLS_MANIFEST_COMMIT=M2` only in the Executor handoff.

Stop at the same legal implementation-review handoff. Do not integrate, merge, release Bridge, start 056, create H10, create state/ledger/controller/watcher, or call paid APIs.

## 9. Final handoff

Report at least:

- new Bridge/Bobbio/Lucerna(if changed)/Mica/Asteria/SeminarArc candidate commits;
- unchanged CUHK Date inspected ref;
- Bridge version candidate;
- H1–H9 outcomes with direct evidence locators;
- Bridge focused/full tests and real H7/H8 behavior;
- new `E2` and `M2`;
- confirmation old `E`/`M` remain historical failed candidates;
- any remaining unverified boundary.

`RESULT = EXECUTED_UNAUDITED | BLOCKED`

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`
