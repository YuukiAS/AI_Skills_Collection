---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: infra_paid_review_safety_migration_20260903
implementation_commit: 119dc40e50beb1c50c1bc9c4a896975902f5c405
---

# Codex Result

## Implemented

Current status: AWAIT_HUMAN_DECISION.

Implementation/evidence tip: `119dc40e50beb1c50c1bc9c4a896975902f5c405`.
Latest main used: `7b08b6a24c7a371cc137a99297a8f40ca573c5fd`.
Bridge Kit paid-review commit: `dfb453e77829b8e868de9bf48c9cedc22e6365ea`.

### Branch hygiene

The superseded writing-style branch cleanup completed before implementation work.

Archived tags:

- archive/044-local-snapshot-20260903 -> 5f808d6bce51da7f97a5ddf6bded7935da6390f5
- archive/044-writing-style -> e8daa62607064a006618f1780eb78a497f0617ea
- archive/047-writing-style -> 1b0028e5f1553f0151d257b174f8c9a35f8de69d
- archive/048-writing-style -> 035ef2311319dff56a3da0973f3e45ca9691ef3c
- archive/049-writing-style -> 78084359678d53a83fde42dfac3bc4b5514022cf
- archive/obsolete-044-blocked-ccbe247 -> ccbe2475e51c61b360da1a0fbed7694b019f5870

Deleted superseded remote branches:

- reviewed/044_writing_style_deep_research_chinese_replay
- reviewed/047_writing_style_scientific_rewrite_architecture
- reviewed/048_writing_style_product_cutover_and_readable_report
- reviewed/049_writing_style_multistage_production_runtime

Deleted local branches:

- reviewed/044_writing_style_deep_research_chinese_replay
- reviewed/047_writing_style_scientific_rewrite_architecture
- reviewed/049_writing_style_multistage_production_runtime
- codex/obsolete-044-blocked-ccbe247

No local reviewed/048 branch was present. The 049 archival tag preserves the final committed tip that records SUPERSEDED_BY_050; the Terra-per-stage 049 implementation was not merged or restored.

The 044 dirty working tree contained 14 paths spanning source skills, generated plugin mirrors, tests, task result evidence, and one untracked local replay artifact. Because these were not all provably duplicated/generated-stale, they were preserved in snapshot commit 5f808d6bce51da7f97a5ddf6bded7935da6390f5 and tag archive/044-local-snapshot-20260903 before the branch was removed.

Remote heads after cleanup:

- main -> 7b08b6a24c7a371cc137a99297a8f40ca573c5fd
- reviewed/050_writing_style_host_codex_runtime -> 65ff3a9bfd4e6e925038855088785a5168ddbb99
- reviewed/infra_paid_review_safety_migration_20260903 -> 5972a302721759354859bafc99dd7459143b17b2 after the first implementation/handoff publication

## Migration implemented

- Generic Text Review and Visual Review no longer have paid `push` triggers.
- Generic paid review workflows now require explicit `workflow_dispatch` input and fail closed on missing manifest/output/secret.
- The `OPENAI_REVIEW_API_KEY || OPENAI_VISUAL_REVIEW_API_KEY` fallback was removed.
- Text Review keeps `OPENAI_REVIEW_API_KEY`; Visual Review keeps `OPENAI_VISUAL_REVIEW_API_KEY`.
- Text and Visual Review production model resolution is pinned to `gpt-5.6-terra` in workflow env, not stale repository variables.
- All paid review workflows pin Bridge Kit commit `dfb453e77829b8e868de9bf48c9cedc22e6365ea` and set `AI_BRIDGE_PAID_REVIEW_GIT_RESERVE=1`.
- Presentation-specific paid visual workflows were migrated to manual-only, no generic `OPENAI_API_KEY` mapping, and the same paid campaign reservation guard.
- Codex Marketplace full workflow is now a PR/manual integration gate, not an ordinary push workflow.
- Codex Marketplace CI is read-only and no longer commits/pushes generated marketplace payload.
- Historical visual packet workflow is manual-only.
- Planner, Executor, AGENTS, paid review policy, and docs now distinguish local development tests from explicit final GitHub integration/release CI.
- Presentation v13/v14 pseudo-plugin TODO inboxes were reviewed, unique feedback was consolidated into `docs/plugin-todos/presentations.md`, and the extra inbox files were deleted.

## Deterministic evidence

AI_Skills tests and validation:

- `python3 -m unittest tests.test_paid_review_workflows` -> PASS
- `python3 -m unittest tests.test_reviewed_handoff_visual_target` -> PASS
- `python3 -m unittest tests.test_codex_marketplace.CodexMarketplaceTests.test_central_plugins_have_exactly_one_source_only_todo_inbox tests.test_codex_marketplace.CodexMarketplaceTests.test_codex_marketplace_full_ci_is_explicit_read_only_gate tests.test_codex_marketplace.CodexMarketplaceTests.test_historical_visual_packet_is_manual_only` -> PASS
- `python3 -m unittest tests.test_presentations.PresentationSharedTests.test_research_presentation_todo_consolidation_and_promotions` -> PASS
- `python3 -m unittest discover -s tests` -> PASS, 171 tests
- `python3 scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS
- `python3 scripts/skills.py validate` -> PASS
- `python3 scripts/skills.py audit --all` -> PASS

Bridge Kit pinned-commit companion evidence:

- Detached worktree at `dfb453e77829b8e868de9bf48c9cedc22e6365ea`
- `python3 -m unittest tests.test_paid_review tests.test_text_review tests.test_visual_review` -> PASS, 37 tests

Credential recovery and live-smoke evidence after user confirmed new project keys:

- GitHub secret metadata gate read names/status only; secret values were not read or printed.
- OPENAI_REVIEW_API_KEY: PRESENT
- OPENAI_VISUAL_REVIEW_API_KEY: PRESENT
- Text `/v1/responses/input_tokens` permission preflight on run 33746261805 -> PASS, input_tokens 10; `/v1/responses` step skipped.
- Visual `/v1/responses/input_tokens` permission preflight on run 33746397708 -> PASS, input_tokens 10; `/v1/responses` step skipped.
- Bridge Kit input-token endpoint compatibility fix pinned as `dfb453e77829b8e868de9bf48c9cedc22e6365ea`.
- Text live smoke run 33746772407 failed before any OpenAI token/budget call because the smoke manifest `task_key` did not match the requested output path.
- Text live smoke run 33746976670 passed local decrypt/path checks, reserved one shared campaign slot, counted 243 input tokens, then failed closed on `/v1/responses` with `HTTP 429 (credit_balance_exhausted; zero paid retry)`.
- Reservation evidence commit `119dc40e50beb1c50c1bc9c4a896975902f5c405` created `results/infra_paid_review_safety_migration_20260903_live_smoke/paid_review_budget.json`.
- Campaign state after the failed Text live smoke: 1 reservation, cumulative worst-case reserved cost `0.049760`, max paid calls 2, campaign ceiling `0.500000`, per-call ceiling `0.250000`.
- Visual live smoke was not dispatched after the Text `/v1/responses` credit failure.
- Full Marketplace CI, integration to `main`, and 050 branch unblocking were not performed.

## Verification

The deterministic verification evidence is listed above. It includes full AI_Skills unittest coverage, marketplace generation validation, skill validation/audit, and Bridge Kit pinned-commit companion tests.

## Deviations / blockers

The input-token permission gate passed for both new repository secrets, but the first real Text Review `/v1/responses` call failed closed with `HTTP 429 (credit_balance_exhausted; zero paid retry)`. This indicates the new `AI_Research_Review` project key can reach `/v1/responses/input_tokens`, but the project currently lacks usable credit/billing capacity for the live Responses call.

Required next actions:

1. Fix `AI_Research_Review` project credit/billing so `OPENAI_REVIEW_API_KEY` can complete a tiny `/v1/responses` call.
2. Resume from the same shared campaign `infra_paid_review_safety_migration_20260903_live_smoke`; do not delete or reset the existing reservation evidence.
3. Do not run automatic paid retries. The next execution should account for the existing Text reservation and continue only within max 2 calls, campaign budget <= $0.50, and per-request worst case <= $0.25.
4. Only after Text and Visual live smoke PASS and explicit full Marketplace gate PASS may this migration be integrated to latest `main`.
5. Only after this migration is integrated may `reviewed/050_writing_style_host_codex_runtime` be moved out of its paid-review migration wait state.
