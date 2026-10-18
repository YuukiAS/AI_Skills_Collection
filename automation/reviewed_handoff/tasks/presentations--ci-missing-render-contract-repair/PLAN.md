---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: presentations--ci-missing-render-contract-repair
decision: PLAN_FROZEN
---

# Presentations CI missing-render contract repair — task-local frozen Plan

- Repository: `YuukiAS/AI_Skills_Collection`
- Task: `presentations--ci-missing-render-contract-repair`
- Execution branch: `reviewed/presentations--ci-missing-render-contract-repair`
- Approved design: `docs/design/presentations/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_V0_1_2026-10-18.md`
- Approved Goal: `docs/goals/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_GOAL_V0_1_2026-10-18.md`
- Approved Kickoff: `docs/operations/prompts/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_KICKOFF_V0_1_2026-10-18.md`
- Approved package commit: `3990ee71705fc0fda654b565e90d8038183cf82f`
- Critic PASS: `results/presentations--ci-missing-render-contract-repair/CRITIC_EXECUTION_READY_REVIEW_V0_1_2026-10-18.md@729fa6348c4e557bdbeba4c1a9f968a142963974`
- External purpose: unblock required full CI for `clear-writing--scientific-explanation-readability-repair`
- Maintenance companion: `ai-skills-core`
- Domain owner: `presentations`
- Execution protocol owner: `workflow-core`
- Plan revision: `0 / 1`
- Review round: `0 / 2`

## Objective and value

Repair one Presentations portability regression that currently blocks unrelated
full-repository CI, specifically Clear Writing required CI run `39097236717`.

The repair is limited to synchronizing the generator, explicit
`--allow-missing-render` validators, and regression tests around the newly
introduced typed state `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`.

This task does not improve or redesign Presentation content, layout, typography,
routing, templates, or visual quality. Its value is to restore a truthful,
portable non-render contract on minimal GitHub-hosted runners so unrelated
full-repository CI can complete without pretending the runner is a production
render host.

## Frozen decisions

- The three failing CI tests are a Presentations portability regression, not a
  Clear Writing product defect.
- The upstream regression source is commit
  `f717d28beef4dd1cbbb66cb491712769d1250aac`, which added canonical font
  resource binding and the typed state
  `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE` without fully synchronizing the
  older validator/test contract.
- When both TeX and canonical font resources are absent, primary compile-status
  classification must first report `BLOCKED_MISSING_TEX_ENGINE`; secondary
  dependency evidence may still record missing canonical fonts.
- When a TeX engine is available but the canonical font bundle is absent,
  `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE` remains the correct typed
  environmental state.
- Only explicit `--allow-missing-render` validation may accept
  `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE` as an environmental non-render
  state.
- Strict validation remains fail-closed for missing TeX/font resources.
- Product/source defects such as `BLOCKED_FONT_RESOURCE_TOKEN_MISSING`,
  unexpected fonts, missing source files, or other malformed generated content
  must not be added to the allow-missing-render allowlist.
- Do not install or vendor private canonical font resources or a full TeX
  environment merely to make this CI green.
- Do not skip/delete/allowlist the failing tests.
- Do not modify Clear Writing production source.
- Do not start or close Issue #98 broader shared-core / two-skin Presentations
  work. That broader development remains paused while Clear Writing is
  completed.
- Maintenance execution remains
  `workflow-core + ai-skills-core + presentations`; these owners do not
  substitute for each other.

## Positive completion

This bounded repair is complete only when the same final candidate proves all of
the following:

1. no-engine + no-font-resource deterministically yields primary compile status
   `BLOCKED_MISSING_TEX_ENGINE` while preserving secondary missing-font
   evidence;
2. engine-present + canonical-font-resource-absent deterministically yields
   `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`;
3. explicit `--allow-missing-render` accepts those environmental non-render
   states;
4. strict validation still rejects those same missing-render states;
5. source and generated Presentations mirrors remain identical through the
   official generator;
6. focused Presentations dependency-state tests, full
   `tests/test_presentations.py`, full repository tests, Marketplace
   generation/check, clean second check, `git diff --check`, and required
   GitHub-hosted CI all PASS;
7. an independent Reviewer confirms this exact portability contract without
   expanding into broader Presentations work.

Maximum claim scope: PASS proves only that the Presentations missing-render
portability regression is repaired and the external Clear Writing CI blocker is
eligible to be removed. It does not prove Presentations visual quality, release
readiness, Issue #98 closure, or Clear Writing product PASS.

## Non-substitutable semantics

- Production render acceptance must remain strict: absent required TeX/font
  dependencies cannot be reported as a successful render.
- `--allow-missing-render` is a non-render contract path, not a production
  success mode.
- Primary dependency classification must be internally consistent:
  no TeX engine is the first sufficient blocker to compilation; font-resource
  absence remains independently observable as secondary evidence.
- A valid canonical-font-missing environmental state must not be confused with
  broken template/resource-token/source logic.
- The canonical Presentations font policy itself is unchanged.
- Renderer-owned resource ownership remains unchanged.
- The CI workflow remains a minimal portability/test host; this task does not
  turn it into a production renderer.
- No Clear Writing source, tests, regression bank, or user-facing behavior may
  be changed by this task.

## Implementation scope

Allowed production/source changes are strictly limited to:

1. `skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py`
2. `skills/tools/documents-media/presentations/shared/scripts/validate_cuhk_scientific_layout_stage3.py`
3. `skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py`
4. `tests/test_presentations.py`
5. the corresponding official generated Presentations mirrors produced by the
   existing Marketplace generator;
6. task-local Reviewed Handoff results/evidence.

Required implementation behavior:

- check/resolve the TeX engine before font materialization determines the
  primary compile status;
- retain font-resource status in dependency evidence;
- add only `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE` to the explicit
  allow-missing-render environmental state handling;
- add deterministic test seams/mocks for no-engine/no-font and
  engine-present/no-font states rather than depending on the host's accidental
  installed software;
- preserve source/generated parity via the official generator.

If latest main has a substantive conflicting change in these exact target files,
stop and return to Planner rather than choosing semantics locally.

## Acceptance and regression gates

Required gates on one final candidate:

- focused dependency-state regression tests PASS;
- full `tests/test_presentations.py` PASS;
- strict-mode missing-render rejection PASS;
- source/generated script parity PASS;
- full repository unit tests PASS;
- Marketplace `--write --validate --check --path-report` PASS;
- second Marketplace check clean/idempotent;
- `git diff --check` PASS;
- required GitHub-hosted runner CI PASS;
- independent Reviewer PASS.

The GitHub CI must pass without:
- adding private font bundles;
- installing a production render stack just to bypass the typed-state bug;
- skipping or deleting tests;
- widening the missing-render allowlist to product/source defects.

After independent Reviewer PASS and legal integration to current `main`, this
repair ends. Clear Writing then consumes that exact repaired main and reruns its
unchanged required full CI.

## Natural-language usage / routing expectations

This task has no new user-facing Presentation capability. Expected observable
behavior is diagnostic/CI behavior only:

- on a minimal host without TeX, Presentations records
  `BLOCKED_MISSING_TEX_ENGINE` as the primary compile blocker;
- on a host with TeX but without the canonical font bundle, it records
  `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`;
- an explicit non-render validation can still validate the remaining
  Presentation contract;
- a real strict render request remains blocked until the missing dependency is
  installed.

Clear Writing behavior and user-facing prose are outside this task.

## Out of scope

- Issue #98 broader shared Beamer core / two-skin implementation;
- deck visual redesign or artifact review;
- typography or canonical font-policy changes;
- new fonts or host-font substitutions;
- renderer resource-ownership changes;
- `.github/workflows/codex-marketplace.yml` redesign or TeX/font provisioning;
- routing/default-prompt/profile changes;
- README or changelog changes;
- Presentations release/version bump;
- Clear Writing source or behavior changes;
- Research Authoring changes;
- paid review;
- any new renderer, state machine, router, database, or persistent ledger.
