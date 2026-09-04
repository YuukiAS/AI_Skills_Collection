---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 050_writing_style_host_codex_runtime
implementation_commit: ca9d6651def3672ae7cd09c257e7294c845fce2c
---

# 050 Writing Style Host-Codex Runtime — STYLE_REJECT repair handoff

## Status

First A/B/C smoke: `STYLE_REJECT`.

Repair implementation: `PROCESS_MECHANICAL_PASS`.

Second A/B/C smoke: `AWAITING HUMAN STYLE DECISION`.

This is not Product PASS. The user remains the style authority and must return
`STYLE_ACCEPT` or `STYLE_REJECT` before any full private report generation.

## Reconciled Starting State

The local task branch preserved the first 050 smoke implementation/evidence and
merged the remote STYLE_REJECT analysis commit `3cae59ccdf4cb3a7904d26e884268aa399bbc6be`.
No reset or candidate reuse was performed.

Starting local-only commits before the repair:

- `dc959899992dcb8a7d9c500ffb266c8b348c0ee2`
- `508639ae9f4007d311b6f2646fa201ae4dd20bbe`
- `b2467347198cca5f8bb65ec27a04dfe152f55ce0`

Remote rejection evidence:

- `results/050_writing_style_host_codex_runtime/STYLE_REJECT_ANALYSIS_2026-09-04.md`

## Repair Implementation

Implementation commit:
`ca9d6651def3672ae7cd09c257e7294c845fce2c`.

Promoted generic manual-rewrite capabilities into production:

- structural rewrite may reorder headings, paragraphs, sections and tables while preserving the content/evidence graph;
- non-contiguous source spans may be grouped when they answer the same scientific reader question;
- evidence classes remain distinct: project fact, literature fact, research interpretation, candidate method, and still-unverified item;
- ordinary reasoning language should become natural Chinese while exact formal names remain recognizable;
- formulas require local intuition, exact formula, symbol meaning and implication;
- method comparisons should answer a decision question before listing full detail;
- bounded conclusion may come before nearby qualification when the source supports it.

Updated production contracts:

- `skills/writing/core/scientific-rewrite/SKILL.md`
- `skills/writing/core/scientific-rewrite/references/meaning-card-and-fidelity-ledger.md`
- `skills/writing/core/scientific-rewrite/references/positive-style-contract.md`
- `skills/writing/core/scientific-rewrite/references/seed-transformations.json`
- `skills/writing/core/writing-fidelity/SKILL.md`
- generated `plugins/codex/plugins/writing-style/...`

Updated runtime/tests:

- `skills/writing/core/scientific-rewrite/scripts/rewrite_support.py`
- generated `plugins/codex/plugins/writing-style/skills/scientific-rewrite/scripts/rewrite_support.py`
- `tests/test_scientific_rewrite.py`

## Runtime Boundary

The normal heavy route remains host-Codex owned. The deterministic helper can
prepare source spans, inventory exact items, validate IDs/schema/coverage,
select generic positive transformations, verify exact literals, validate
host-produced stage dataflow and emit privacy-safe receipts.

It cannot generate reader-facing Chinese prose, manufacture Meaning Cards from
source-copy fallback, call `/v1/responses`, call Terra, use `text-transform`
generation, append missing exact literals to the candidate, or satisfy
`inline-critical` items through an appendix.

`writing-fidelity` now recognizes
`STRUCTURAL_REWRITE_AUTHORIZED_BY_TASK`: for explicit heavy scientific rewrite,
headings and source order are not protected by default; the protected invariant
is the content/evidence graph.

## Second Smoke Evidence

Private reader package root:
`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_repair_20260904`

Combined private reader file:
`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_repair_20260904/STYLE_SMOKE_FOR_USER.md`

Individual private candidates:

- SMOKE-A:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_repair_20260904/SMOKE-A/final_candidate.md`
- SMOKE-B:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_repair_20260904/SMOKE-B/final_candidate.md`
- SMOKE-C:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_repair_20260904/SMOKE-C/final_candidate.md`

| Smoke | Source segment SHA-256 | Candidate SHA-256 | Units | Stages | Exact literals | Exact | Dataflow | Argument coverage | Global reorder |
|---|---|---|---:|---:|---:|---|---|---|---|
| SMOKE-A | `3e18bea855cc4afccacc47b7ed60600ef637cbffd7ea412fcb54fe4b0575a5db` | `ced7677668531c114fe700329cddfde178381bc03c53f4332f4abb42a8b91f6d` | 2 | 11 | 59 | PASS | PASS | PASS | PASS |
| SMOKE-B | `20161b96ba82a610d3669d49aae01eeff32f98eeb1737438c892a869b5660e88` | `a2cfe9f8ff9b131cdb38e067669b59419d2da937742508164c1bcb7d43996854` | 4 | 19 | 49 | PASS | PASS | PASS | PASS |
| SMOKE-C | `22eacc455a07341d24f52666e911dea1f0e8edd46d8bbaeed896a5fc2f973a48` | `5acbcf43c030b06814c5a0b01fa5c398f606623669e1e1279d3323d2028f13d5` | 8 | 35 | 109 | PASS | PASS | PASS | PASS |

Public evidence paths:

- `results/050_writing_style_host_codex_runtime/style_reject_repair_smoke_inputs/`
- `results/050_writing_style_host_codex_runtime/style_reject_repair_private_smoke/`
- `results/050_writing_style_host_codex_runtime/style_reject_repair_reader_check.json`

## Candidate-Only Reader Check

Host-Codex candidate-only check status:
`HOST_CODEX_CANDIDATE_ONLY_CHECK_PASS_AWAITING_USER_STYLE_DECISION`.

Checked generic properties:

- first paragraph states the bounded scientific point;
- ordinary reasoning language is natural Chinese;
- proper names remain recognizable;
- formulas have local intuitive explanation;
- evidence, interpretation, candidate proposal and unverified items remain distinguishable;
- important caveats remain near the claims they limit;
- comparison structure answers a scientific decision question;
- document/unit order differs from source where that reduces reader effort;
- no token-dump appendix;
- no `inline-critical` item is satisfied only by appendix;
- no internal workflow/audit language carries the scientific narrative.

This check is not final style authority.

## Local Validation

- `python3 -m unittest tests.test_scientific_rewrite` — PASS, 25 tests.
- `python3 -m unittest tests.test_scientific_rewrite tests.test_codex_marketplace` — PASS, 61 tests.
- `python3 -m unittest tests.test_skill_runtime_text_audit tests.test_paid_review_workflows` — PASS, 10 tests.
- `python3 -m unittest tests.test_scientific_rewrite tests.test_codex_marketplace tests.test_skill_runtime_text_audit tests.test_paid_review_workflows` — PASS, 71 tests.
- `python3 -m unittest discover -s tests` — PASS, 198 tests.
- `python3 scripts/build_codex_marketplace.py --write` — PASS.
- `python3 scripts/build_codex_marketplace.py --validate` — PASS.
- `python3 scripts/build_codex_marketplace.py --check` — PASS.
- `python3 scripts/build_codex_marketplace.py --path-report` — PASS.
- `python3 scripts/skills.py validate` — PASS.
- `python3 scripts/skills.py audit --all` — PASS.

Reviewed-handoff validator still reports only the known 049/050 frozen-Plan
old-template section mismatch. `PLAN.md` was not edited.

## No Live Spend / Privacy

No OpenAI `/v1/responses`, `/v1/responses/input_tokens`, Terra call, paid
workflow, GitHub Actions dispatch, or full private report generation occurred.

No private plaintext source, candidate, Meaning Card, or stage artifact was
committed. Public Git evidence contains only hashes, counts, statuses and
machine-local private locators.

## Version Decision

Repository bump decision: `NONE`.

Affected plugins:

- `writing-style`: `NO_BUMP`
  Reason: 050 is still stopped at the human style gate; final release
  acceptance has not occurred.
