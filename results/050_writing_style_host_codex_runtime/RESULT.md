---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 050_writing_style_host_codex_runtime
implementation_commit: bac6bf37ee22b52a2894c90a385dd6ab0e8f0292
---

# 050 Writing Style Host-Codex Runtime — STYLE_REJECT repair handoff

## Status

First A/B/C smoke: `STYLE_REJECT`.

Repair implementation: `PROCESS_MECHANICAL_PASS`.

Second A/B/C smoke: `STYLE_REJECT`.

Third A/B/C smoke: `AWAITING HUMAN STYLE DECISION`.

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

## Round-2 Repair Implementation

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

## Round-3 Repair Implementation

Implementation commit:
`bac6bf37ee22b52a2894c90a385dd6ab0e8f0292`.

The second repair promoted Reader Plan and Chinese reader-pass gates into the
host-Codex scientific rewrite contract:

- every rewrite now has a `reader_plan.json` bound to the document-map hash;
- source spans are organized by reader question, including non-contiguous
  bundles where that reduces reader effort;
- each bundle declares its information shape, including formula walkthroughs,
  tables, short lists and technical traces;
- English spans are classified as exact identity, useful recognition or
  ordinary reasoning before reader-facing Chinese is accepted;
- the terminal Chinese reader pass is candidate-only and checks answerability,
  reader effort, formula context and epistemic boundaries;
- deterministic receipt validation now rejects missing Reader Plan,
  disconnected stage dataflow and missing Chinese reader-pass evidence.

Updated production/runtime areas:

- `skills/writing/core/scientific-rewrite/scripts/rewrite_support.py`
- `skills/writing/core/scientific-rewrite/SKILL.md`
- `skills/writing/core/scientific-rewrite/references/meaning-card-and-fidelity-ledger.md`
- `skills/writing/core/scientific-rewrite/references/positive-style-contract.md`
- `skills/writing/core/scientific-rewrite/references/seed-transformations.json`
- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- generated `plugins/codex/plugins/writing-style/...`
- `profiles/codex-writing-style.json`
- `scripts/codex_marketplace_config.json`
- `tests/test_scientific_rewrite.py`

## Third Smoke Evidence

Private reader package root:
`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_round3_20260904`

Combined private reader Markdown:
`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_round3_20260904/STYLE_SMOKE_A_B_C_ROUND3.md`

Combined private reader PDF preview:
`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_round3_20260904/STYLE_SMOKE_A_B_C_ROUND3.noto_visual_checked_v5.pdf`

Page 6 preview:
`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_round3_20260904/noto_visual_pages_v5/page_06.png`

Individual private candidates:

- SMOKE-A:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_round3_20260904/SMOKE-A/final_candidate.md`
- SMOKE-B:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_round3_20260904/SMOKE-B/final_candidate.md`
- SMOKE-C:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_round3_20260904/SMOKE-C/final_candidate.md`

| Smoke | Source segment SHA-256 | Candidate SHA-256 | Units | Stages | Exact literals | Exact | Dataflow | Reader Plan | Chinese reader pass |
|---|---|---|---:|---:|---:|---|---|---|---|
| SMOKE-A | `3e18bea855cc4afccacc47b7ed60600ef637cbffd7ea412fcb54fe4b0575a5db` | `2525b958e468767162ada1b26b52e457768bb3987f0ca9e64bc08bb269903fc7` | 2 | 14 | 27 | PASS | PASS | PASS | PASS |
| SMOKE-B | `20161b96ba82a610d3669d49aae01eeff32f98eeb1737438c892a869b5660e88` | `b62fbafae4e5ecd486fb7c8c0caadbd9219d633c2132eac9d32f1f0b7db19302` | 4 | 22 | 18 | PASS | PASS | PASS | PASS |
| SMOKE-C | `22eacc455a07341d24f52666e911dea1f0e8edd46d8bbaeed896a5fc2f973a48` | `f33a3a9be56de01bea2e647524fbd966661d4939a9dcd94cd4e123bb559c6002` | 8 | 38 | 33 | PASS | PASS | PASS | PASS |

Public evidence paths:

- `results/050_writing_style_host_codex_runtime/style_reject_round3_smoke_inputs/`
- `results/050_writing_style_host_codex_runtime/style_reject_round3_private_smoke/`
- `results/050_writing_style_host_codex_runtime/style_reject_round3_render_qa.json`

This smoke is stopped at the required human style gate. It is not Product PASS.

## Round-3 PDF Render QA

The local PDF skills were used for the requested combined A/B/C reader PDF:

- `pdf`
- `render-chinese-math-pdf`

The strict skill route is
`Markdown -> Pandoc -> XeLaTeX -> PDF`. On this host that route is
`blocked_missing_dependency`: `kpsewhich` could not find `xeCJK.sty`,
`luatexja.sty`, `ctex.sty`, or `CJKutf8.sty`. The first XeLaTeX attempt also
needed task-local `TEXMFHOME`, `TEXMFVAR` and `TEXMFCONFIG` because the default
TeX cache under `$HOME` was not writable.

Three generated fallback PDFs were rejected during QA:

- ReportLab fallback: visual text scattering;
- CID font fallback: Chinese boxes in preview;
- Droid CJK fallback: insufficient Chinese glyph coverage.

The reader PDF is therefore explicitly marked `partial_complete`, not strict
render completion. An intermediate fallback was:

`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_round3_20260904/STYLE_SMOKE_A_B_C_ROUND3.noto_visual_checked_v3.pdf`

That v3 file was rejected after direct page-6 inspection because inline math
still exposed raw `hat{theta}` fragments. A v4 regeneration was also rejected
because Unicode combining-hat/subscript inline math produced missing-glyph
boxes. The current preview is:

`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke_round3_20260904/STYLE_SMOKE_A_B_C_ROUND3.noto_visual_checked_v5.pdf`

It is a 14-page image-only visual PDF rendered with local Noto Serif CJK fonts
and matplotlib mathtext formula images. Page 6 was visually inspected after
regeneration; Chinese text and display formulas are visible and not mojibake,
and inline math in prose is rendered as stable ASCII identifiers rather than raw
LaTeX fragments or missing-glyph boxes.
Because the file is image-only, `pdftotext` extraction is intentionally not a
pass criterion for this fallback artifact.

Root cause assessment:

- The PDF skill itself was not the root defect: it correctly requires strict
  XeLaTeX and says to report `blocked_missing_dependency` when that route is
  unavailable.
- My first PDF handoff was the defect: it used a weak fallback and did not do
  page-level formula QA before presenting the file.
- The issue could still appear after reading the skill because the current host
  lacks the strict CJK LaTeX package dependency. Once the skill was applied
  fully, the correct state became: strict renderer blocked, visual fallback
  available only as `partial_complete`.

Prevention:

- never present a generated PDF as complete until page-count, first-page visual
  preview and formula-heavy page previews have been inspected;
- when `render-chinese-math-pdf` is used, record whether the output is strict
  XeLaTeX or an explicit fallback;
- if XeLaTeX CJK dependencies are missing, report the missing packages instead
  of silently treating another renderer as equivalent;
- include at least one equation-heavy page PNG path in the public render QA
  receipt for future checks.

## Round-3 Local Validation

- `python3 -m unittest tests.test_scientific_rewrite` — PASS, 28 tests.
- `python3 scripts/build_codex_marketplace.py --write --validate --check --path-report` — PASS.
- `python3 -m unittest tests.test_codex_marketplace` — PASS, 36 tests.
- `python3 -m unittest tests.test_paid_review_workflows` — PASS, 5 tests.
- `python3 scripts/skills.py validate` — PASS, 150 active skills and 18 profiles.
- `python3 scripts/skills.py audit --all` — PASS.
- `python3 -m unittest discover -s tests` — PASS, 201 tests.

## Version Decision

Repository bump decision: `NONE`.

Affected plugins:

- `writing-style`: `NO_BUMP`
  Reason: 050 is still stopped at the human style gate; final release
  acceptance has not occurred.
