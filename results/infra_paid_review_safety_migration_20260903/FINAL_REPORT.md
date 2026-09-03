# Final Report

## What this task solved

This task completed the deterministic infrastructure migration for paid review and CI lifecycle safety. It now stops at a project billing/credit handoff after the first live Text Review call failed closed.

This is not a PASS, release, or integration closure. It is a credential/account handoff required by the frozen paid-review safety plan.

## What changed

- Superseded writing-style branches were archived with lightweight tags before deletion.
- The dirty 044 local working tree was preserved in snapshot commit `5f808d6bce51da7f97a5ddf6bded7935da6390f5`.
- AI_Skills paid review workflows were migrated to explicit manual invocation only.
- Cross-secret fallback was removed.
- Paid review workflows now pin Bridge Kit `dfb453e77829b8e868de9bf48c9cedc22e6365ea`.
- Text/Visual review model resolution is pinned to `gpt-5.6-terra`.
- Presentation-specific paid visual workflows now use the shared persistent paid-review reservation guard.
- Codex Marketplace full CI is an explicit PR/manual integration gate and no longer writes commits.
- Historical visual packet workflow is manual-only.
- The v13/v14 Presentation pseudo-plugin TODO inboxes were consolidated into `docs/plugin-todos/presentations.md` and removed.

## New capabilities / behavior

Paid Text Review and Visual Review can still be invoked, but only as explicit bounded manual gates. Ordinary push and ordinary CI no longer trigger paid OpenAI review. Full Marketplace CI is now an explicit PR/manual integration or release gate and cannot self-push generated payload.

## Deliberately not adopted / unchanged

050 remains blocked until this migration is integrated. The 049 Terra-per-stage implementation remains superseded. Secret names remain `OPENAI_REVIEW_API_KEY` and `OPENAI_VISUAL_REVIEW_API_KEY`; missing secrets fail closed instead of using fallback behavior.

## Example usage

For this migration, the next valid usage is an explicit GitHub workflow dispatch after the user confirms the review secrets are new `AI_Research_Review` project keys. The campaign must run one tiny public-safe Text Review and one tiny public-safe Visual Review, sharing max 2 calls and no more than USD 0.50 reserved budget.

## Regression and remaining limitations

Live OpenAI status:

- Secret metadata was checked as PRESENT/MISSING only; values were not read or printed.
- OPENAI_REVIEW_API_KEY: PRESENT
- OPENAI_VISUAL_REVIEW_API_KEY: PRESENT
- Text input-token-only preflight run 33746261805: PASS, `/v1/responses/input_tokens` returned input_tokens 10; `/v1/responses` skipped.
- Visual input-token-only preflight run 33746397708: PASS, `/v1/responses/input_tokens` returned input_tokens 10; `/v1/responses` skipped.
- Text live smoke run 33746976670 reserved one campaign slot and then failed closed on `/v1/responses`: `HTTP 429 (credit_balance_exhausted; zero paid retry)`.
- Existing shared campaign reservation: `results/infra_paid_review_safety_migration_20260903_live_smoke/paid_review_budget.json`, call 1, worst-case reserved cost `0.049760`.
- Visual live smoke was not dispatched after the Text credit failure.


Local evidence:

- AI_Skills full unittest suite passed: 171 tests.
- Marketplace generation/validation/path budget check passed.
- `scripts/skills.py validate` passed.
- `scripts/skills.py audit --all` passed.
- Bridge Kit pinned-commit companion tests passed: 37 tests.

Required recovery path:

1. Fix `AI_Research_Review` project credit/billing for the new restricted keys.
2. Resume the frozen smoke from shared campaign `infra_paid_review_safety_migration_20260903_live_smoke` without deleting existing reservation evidence or broadening model capability.
3. Complete one Text Review and one Visual Review image-input smoke within max calls 2, campaign budget <= $0.50, and per-request worst case <= $0.25.
4. Dispatch the full Codex Marketplace integration gate explicitly.
5. Integrate the migration to latest `main` only after live smoke and full gate PASS.
6. Only then unblock `reviewed/050_writing_style_host_codex_runtime`.

## Technical appendix

- status: AWAIT_HUMAN_DECISION
- reason: AI_RESEARCH_REVIEW_PROJECT_CREDIT_BALANCE_EXHAUSTED_DURING_TEXT_LIVE_SMOKE
- implementation_evidence_tip: `119dc40e50beb1c50c1bc9c4a896975902f5c405`
- latest_main_used: `7b08b6a24c7a371cc137a99297a8f40ca573c5fd`
- first_published_handoff_tip: `5972a302721759354859bafc99dd7459143b17b2`
- bridge_kit_paid_review_commit: `dfb453e77829b8e868de9bf48c9cedc22e6365ea`
- result artifact: `results/infra_paid_review_safety_migration_20260903/RESULT.md`
