# 049 Public Evidence Report

Date: 2026-09-02

This report contains only public task evidence. It does not include private source plaintext, private candidate plaintext, API keys, auth material, or full private stage packets.

## Implementation Scope

- Added the AI_Skills repository execution clarification in `AGENTS.md` and pushed it as commit `8ad7974` (`Clarify isolated central plugin replay policy`).
- Implemented `scientific-rewrite.multistage.v1` as a runtime helper under the existing `writing-style` plugin.
- Added generated marketplace payload exposure for `writing-style/skills/scientific-rewrite`.
- Added `scientific-rewrite` to the `codex-writing-style` profile.
- Kept repository and plugin version decisions unchanged:
  - Repository bump decision: `NONE`
  - Affected plugins:
    - `writing-style`: `NO_BUMP`
- Did not modify presentations or unrelated plugin source areas.

## Runtime Responsibilities

The staged runtime records separate responsibilities for:

- document map;
- per-unit Meaning Card / Fidelity Ledger;
- per-unit bounded example selection;
- per-unit writer packet;
- exact literal and semantic audit;
- targeted repair hook when exact/semantic audit fails;
- candidate-only reader review with `source_visible=false`;
- final assembly coherence check without whole-document free rewrite.

The OpenAI Responses driver is implemented as a stage driver with `store=false`. Unit tests use a fake caller to verify that this path makes observable calls for document map, meaning card, writer, audit, candidate-only reader review, and final assembly without requiring network access.

## Public Regression Receipts

### rewrite_needed_scientific_trace

- source path: `results/049_writing_style_multistage_production_runtime/public_regression/sources/rewrite_needed_scientific_trace.md`
- candidate path: `results/049_writing_style_multistage_production_runtime/public_regression/candidates/rewrite_needed_scientific_trace_candidate.md`
- receipt path: `results/049_writing_style_multistage_production_runtime/public_regression/receipts/rewrite_needed_scientific_trace.stage_receipt.json`
- source sha256: `5693f6f152765be631a4623ad55fb9dff622723e63c2f49549eb675b529afca6`
- candidate sha256: `952d4a249d5dcf904170cfb64f5594cd7ad0f7df4330e9c7b8ca356fd785e4fa`
- unit count: `2`
- stage count: `11`
- whole-document writer call: `false`
- max examples per unit: `4`
- full seed library injected: `false`
- private plaintext committed: `false`

### should_not_fix_fidelity

- source path: `results/049_writing_style_multistage_production_runtime/public_regression/sources/should_not_fix_fidelity.md`
- candidate path: `results/049_writing_style_multistage_production_runtime/public_regression/candidates/should_not_fix_fidelity_candidate.md`
- receipt path: `results/049_writing_style_multistage_production_runtime/public_regression/receipts/should_not_fix_fidelity.stage_receipt.json`
- source sha256: `ea377cd0c2ef4add1674e85a96eac9819f9000f5e20e3e30174715f1a79a70ee`
- candidate sha256: `45184542db3d00f60aae6597798717adfaabe51920ed43f3f850daf92d1ced8d`
- unit count: `1`
- stage count: `7`
- whole-document writer call: `false`
- max examples per unit: `4`
- full seed library injected: `false`
- private plaintext committed: `false`

## Generated Payload Smoke

The generated plugin payload entrypoint was run directly from:

`plugins/codex/plugins/writing-style/skills/scientific-rewrite/scripts/rewrite_support.py`

Receipt:

`results/049_writing_style_multistage_production_runtime/production_entrypoint_smoke/generated_payload_stage_receipt.json`

Summary:

- source sha256: `5693f6f152765be631a4623ad55fb9dff622723e63c2f49549eb675b529afca6`
- candidate sha256: `952d4a249d5dcf904170cfb64f5594cd7ad0f7df4330e9c7b8ca356fd785e4fa`
- unit count: `2`
- stage count: `11`
- whole-document writer call: `false`
- max examples per unit: `4`
- full seed library injected: `false`
- private plaintext committed: `false`

## Isolated Installed Entrypoint Evidence

Installed production-entrypoint validation was performed in a task-local isolated Codex home:

`/tmp/codex-049-isolated`

The isolated home started without a live global marketplace binding. The 049 worktree was added as a local marketplace source, and `writing-style` was installed from the generated payload into:

`/tmp/codex-049-isolated/plugins/cache/yuukias-ai-skills/writing-style/0.1`

No live global `yuukias-ai-skills` marketplace or plugin cache was modified.

### Heavy scientific-rewrite request

A fresh isolated Codex session invoked the installed `writing-style` plugin for a public long-form scientific rewrite request and used the installed `scientific-rewrite` runtime from:

`/tmp/codex-049-isolated/plugins/cache/yuukias-ai-skills/writing-style/0.1`

Evidence:

- session id: `01a062a1-d048-7953-8978-e04ddb5f7510`
- last message: `results/049_writing_style_multistage_production_runtime/production_entrypoint/isolated_heavy_last_message.txt`
- candidate path: `results/049_writing_style_multistage_production_runtime/production_entrypoint/isolated_heavy_candidate.md`
- receipt path: `results/049_writing_style_multistage_production_runtime/production_entrypoint/isolated_heavy_stage_receipt.json`
- summary path: `results/049_writing_style_multistage_production_runtime/production_entrypoint/isolated_heavy_summary.json`
- runtime: `scientific-rewrite.multistage.v1`
- unit count: `2`
- stage count: `12`
- whole-document writer call: `false`
- max examples per unit: `4`
- full seed library injected: `false`
- candidate-only reader review `source_visible`: `false`
- exact verifier: `ok`

The installed runtime was also executed directly from the isolated plugin cache:

`/tmp/codex-049-isolated/plugins/cache/yuukias-ai-skills/writing-style/0.1/skills/scientific-rewrite/scripts/rewrite_support.py`

Receipt:

`results/049_writing_style_multistage_production_runtime/production_entrypoint/isolated_installed_runtime_stage_receipt.json`

Summary:

- source sha256: `5693f6f152765be631a4623ad55fb9dff622723e63c2f49549eb675b529afca6`
- candidate sha256: `952d4a249d5dcf904170cfb64f5594cd7ad0f7df4330e9c7b8ca356fd785e4fa`
- unit count: `2`
- stage count: `11`
- whole-document writer call: `false`
- max examples per unit: `4`
- full seed library injected: `false`
- private plaintext committed: `false`

### Light and fidelity routing

A separate fresh isolated Codex session validated that non-heavy requests do not enter the multistage runtime:

- summary path: `results/049_writing_style_multistage_production_runtime/production_entrypoint/isolated_light_fidelity_summary.json`
- light Chinese polish selected: `writing-style:chinese-prose`
- numeric/formula/citation preservation check selected: `writing-style:writing-fidelity`
- heavy runtime invoked: `false`
- heavy receipt created: `false`

## Private Style Smoke Status

The three fixed samples from `STYLE_SMOKE_MANIFEST.md` still need fresh V2 generation through the 049 structured multistage runtime. The committed `SMOKE-A` / `SMOKE-B` / `SMOKE-C` files from commit `24adeb8` are historical V1 evidence only:

- schema: `SCIENTIFIC_REWRITE_MULTISTAGE_RECEIPT_V1`
- unit count: `1`
- stage count: `7`
- no V2 `dataflow_validation`
- no explicit V2 stage list covering document map, argument segmentation, Meaning Cards, source-to-card coverage, example selection, unit writer, literal/semantic audit, candidate-only reader review, and final assembly/coherence

Those V1 outputs must not be used for the current 049 style gate.

The required V2 secure transport path remains:

```text
private local segment
-> age encryption
-> GitHub Actions ephemeral decrypt
-> generated scientific-rewrite multistage runtime
-> OpenAI Responses API store=false
-> encrypted output
-> local decrypt
```

The secure transport was retried on the current V2 runtime without changing the frozen private path, global marketplace, prefix rules, or Bridge Kit:

- run `33696731870`: failed during private transform with `HTTP 429`
- run `33699978179`: failed on `SMOKE-A` document map with `HTTP 429`
- run `33703155683`: failed on `SMOKE-A` document map with `type=insufficient_quota`, `code=credit_balance_exhausted`

The last run proves:

- GitHub Actions received the configured OpenAI secret.
- The age-encrypted private artifact transport reached the OpenAI Responses API path.
- The current failure is an external OpenAI credit/billing resource failure for that configured API credential, not a missing local shell key, not a request to use Codex identity, and not a reason to mutate the live global marketplace/plugin cache.

## Current Status

Implemented and verified so far:

- AI_Skills `AGENTS.md` isolated central plugin replay policy: commit `8ad7974`
- V2 structured runtime and generated payload: current implementation commit `e44a4b201dc7de3a21add210a2b9bc3b4e90ef7f`
- isolated installed-entrypoint evidence: `production_entrypoint_v2/isolated_installed_runtime_stage_receipt.json`
- public regression receipts: `public_regression/receipts/*.stage_receipt.json`
- local tests: `python3 -m pytest tests/test_scientific_rewrite.py tests/test_codex_marketplace.py -q` passed with `66 passed`
- generator/parity: `python3 scripts/build_codex_marketplace.py --write --validate --check --path-report` passed

Still required before the human style gate:

- rerun fixed `SMOKE-A`, `SMOKE-B`, and `SMOKE-C` after the configured OpenAI API credential has available credits;
- confirm each private smoke receipt is V2, uses `openai-responses`, records `store=false`, has `dataflow_validation.ok=true`, has multiple model calls, and records the required stage responsibilities;
- only then move `CURRENT.json` to `AWAIT_HUMAN_DECISION` with `next_action=WAIT_FOR_USER_STYLE_ACCEPTANCE`.
