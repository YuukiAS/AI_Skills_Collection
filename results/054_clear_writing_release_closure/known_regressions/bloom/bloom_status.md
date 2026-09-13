# 054 Bloom Raw-Markup Known Regression

Status: PASS for the 054 Gate B Bloom known-regression slice.

Candidate commit: `245127e1bb46f860ea1976b1669c467c7a9f763d`

Replay run: `20260913T034241Z-2550815`

## Evidence

- Candidate Markdown: `results/054_clear_writing_release_closure/known_regressions/bloom/bloom_filter_rewritten.md`
- Replay metadata: `results/054_clear_writing_release_closure/known_regressions/bloom/run.json`
- Stage receipt: `results/054_clear_writing_release_closure/known_regressions/bloom/stage_receipt.json`
- Meaning map: `results/054_clear_writing_release_closure/known_regressions/bloom/meaning_map.json`
- Reader plan: `results/054_clear_writing_release_closure/known_regressions/bloom/reader_plan.json`
- Semantic audit: `results/054_clear_writing_release_closure/known_regressions/bloom/semantic_audit.json`
- Local deterministic audit: `results/054_clear_writing_release_closure/known_regressions/bloom/local_audit.json`
- Rendered PDF: `results/054_clear_writing_release_closure/render_qa/bloom/bloom_filter_rewritten.pdf`
- PDF text extraction: `results/054_clear_writing_release_closure/render_qa/bloom/bloom_filter_rewritten.txt`
- First-page PNG: `results/054_clear_writing_release_closure/render_qa/bloom/page-1.png`

## Checks

- Actual candidate plugin consumption is proven in `run.json`.
- `stage_receipt.json` records `schema = SCIENTIFIC_REWRITE_HEAVY_ROUTE_RECEIPT_V2`, `paid_generation_used = false`, and `external_api_call_count = 0`.
- The Bloom source-context path was exercised: `source_context_item_count = 1` and `excluded_source_context_item_count = 1`.
- `candidate_representation.ok = true`.
- `exact_verification.ok = true`.
- `semantic_audit.decision = PASS`.
- Local deterministic audit found no raw wiki/template/HTML/ref/comment syntax, no source-process framing, no workflow leakage, no internal engineering framing, no malformed table, and no unrendered math.
- Required technical facts remain present, including Bloom Filter / 布隆过滤器, Burton Howard Bloom, 1970, `O(n)`, `O(log n)`, `O(1)`, `O(k)`, `m = 18`, `k = 3`, false positives, and no false negatives.
- Pandoc -> XeLaTeX render produced a 1-page unencrypted A4 PDF with embedded subset Noto Serif SC, TeX Gyre Termes, and TeX Gyre Termes Math fonts.
- Visual first-page inspection found readable Chinese layout with no obvious clipping, missing glyphs, raw markup leakage, or code-fence formula.
