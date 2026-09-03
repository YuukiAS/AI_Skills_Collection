# Final Report

## What this task solved

This task completed the infrastructure migration for paid review and CI lifecycle safety, including deterministic validation, bounded live Text/Visual smoke, and explicit full Marketplace CI.

This report records the migration branch evidence immediately before integration to latest `main` and the follow-on 050 unblocking step.

## What changed

- Superseded writing-style branches were archived with lightweight tags before deletion.
- The dirty 044 local working tree was preserved in snapshot commit `5f808d6bce51da7f97a5ddf6bded7935da6390f5`.
- AI_Skills paid review workflows were migrated to explicit manual invocation only.
- Cross-secret fallback was removed.
- Paid review workflows now pin Bridge Kit `b185c1f3bd96f26c3e8af80a741e96775eca8e78`.
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
- After user-confirmed funding, Text live smoke run 33748456926: PASS, reused call 1, actual model cost `0.002362`.
- Visual live smoke run 33748612726: PASS, used call 2, actual model cost `0.002730`.
- Shared campaign reservation: `results/infra_paid_review_safety_migration_20260903_live_smoke/paid_review_budget.json`, 2 reservations, cumulative worst-case reserved cost `0.099337`, total verified actual model cost `0.005092`, campaign ceiling `0.500000`, per-call ceiling `0.250000`, automatic paid retries 0.


Local evidence:

- AI_Skills full unittest suite passed: 172 tests.
- Marketplace generation/validation/path budget check passed.
- `scripts/skills.py validate` passed.
- `scripts/skills.py audit --all` passed.
- Bridge Kit pinned-commit companion tests passed: 42 tests.
- Explicit GitHub `Codex Marketplace` integration gate run 33749066096 passed on branch `reviewed/infra_paid_review_safety_migration_20260903`, head `44dbe927e4dda98c6a2f6183559b693ebb4c92a1`, event `workflow_dispatch`.

Required recovery path:

1. Integrate the migration to latest `main`.
2. Only then unblock `reviewed/050_writing_style_host_codex_runtime`.
3. Stop there; do not execute 050 writing rewrite or private smoke.

## Technical appendix

- status: AWAIT_HUMAN_DECISION / PLANNER_DECISION after live-smoke and CI gates passed
- reason: LIVE_TEXT_VISUAL_SMOKE_AND_FULL_CI_GATE_PASS
- implementation_evidence_tip: `44dbe927e4dda98c6a2f6183559b693ebb4c92a1`
- latest_main_used: `7b08b6a24c7a371cc137a99297a8f40ca573c5fd`
- first_published_handoff_tip: `5972a302721759354859bafc99dd7459143b17b2`
- bridge_kit_paid_review_commit: `b185c1f3bd96f26c3e8af80a741e96775eca8e78`
- result artifact: `results/infra_paid_review_safety_migration_20260903/RESULT.md`
