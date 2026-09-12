# 053 Known Regression Status

Status: PARTIAL_PASS_K1_K2_K3_PENDING

Candidate commit: `fcb20edbe2a738db39e3a9d9ed8c6b451ec66526`

## K1 Bloom raw-wikitext

Status: PASS for Markdown candidate, stage receipt, candidate consumption, and public PDF render QA.

Evidence:

- Candidate Markdown: `results/053_clear_writing_release_quality_hardening/known_regressions/bloom/bloom_filter_rewritten.md`
- Stage receipt: `results/053_clear_writing_release_quality_hardening/known_regressions/bloom/stage_receipt.json`
- Semantic audit: `results/053_clear_writing_release_quality_hardening/known_regressions/bloom/semantic_audit.json`
- Route selection: `results/053_clear_writing_release_quality_hardening/known_regressions/bloom/route_selection.json`
- Replay metadata: `results/053_clear_writing_release_quality_hardening/known_regressions/bloom/run.json`
- Cleanup evidence: `results/053_clear_writing_release_quality_hardening/known_regressions/bloom/cleanup.json`
- Rendered PDF: `results/053_clear_writing_release_quality_hardening/render_qa/bloom/bloom_filter_rewritten.pdf`
- Render text extraction: `results/053_clear_writing_release_quality_hardening/render_qa/bloom/bloom_filter_rewritten.txt`
- First-page PNG: `results/053_clear_writing_release_quality_hardening/render_qa/bloom/page-1.png`

Checks:

- Actual candidate `SKILL.md` consumption proven from child JSONL.
- `candidate_representation.ok = true`.
- `exact_verification.ok = true`.
- `semantic_audit.ok = true`.
- No raw wiki/template/HTML/ref/comment syntax found in reader-facing Markdown or PDF text extraction.
- No source-process or workflow-wrapper leakage found in reader-facing Markdown or PDF text extraction.
- PDF rendered through Pandoc -> XeLaTeX; `pdfinfo` reported 1 page, unencrypted, A4.
- `pdffonts` reported embedded subset Noto Serif SC and TeX Gyre Termes fonts.
- Visual page inspection found no obvious clipping, missing glyphs, code-fence formula, or raw markup leakage.

## K2 FFT math

Status: PASS for Markdown candidate, stage receipt, candidate consumption, and public PDF render QA.

Evidence:

- Candidate Markdown: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/fft_wikipedia.md`
- Stage receipt: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/stage_receipt.json`
- Semantic audit: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/semantic_audit.json`
- Route selection: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/route_selection.json`
- Replay metadata: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/run.json`
- Cleanup evidence: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/cleanup.json`
- Rendered PDF: `results/053_clear_writing_release_quality_hardening/render_qa/fft/fft_wikipedia.pdf`
- Render text extraction: `results/053_clear_writing_release_quality_hardening/render_qa/fft/fft_wikipedia.txt`
- First-page PNG: `results/053_clear_writing_release_quality_hardening/render_qa/fft/page-1.png`

Checks:

- Actual candidate `SKILL.md` consumption proven from child JSONL.
- `candidate_representation.ok = true`.
- `exact_verification.ok = true`.
- `semantic_audit.ok = true`.
- Candidate uses display math for the DFT formula, not a fenced `text` block.
- Candidate preserves the DFT definition, `O(N^2)`, `O(N log N)`, `(N/2)\log_2 N`, the Cooley-Tukey power-of-two condition, the numerical-accuracy caveat, and historical attribution.
- No raw wiki/template/HTML/ref/comment syntax found in reader-facing Markdown or PDF text extraction.
- No source-process or workflow-wrapper leakage found in reader-facing Markdown or PDF text extraction.
- PDF rendered through Pandoc -> XeLaTeX; `pdfinfo` reported 1 page, unencrypted, A4.
- `pdffonts` reported embedded subset Noto Serif SC, TeX Gyre Termes, LM Mono, and TeX Gyre Termes Math fonts.
- Visual page inspection found the DFT summation rendered as centered math with no clipping or code fence.

## K3 complete private Deep Research

Status: PENDING_USER_APPROVAL_FOR_PROVIDER_TRUST_SCOPE

K3 source and comparison baselines were located by path, byte size, and SHA-256 only. Private plaintext was not printed, committed, or pushed.

The first K3 candidate replay attempt was not executed because Auto-review rejected the escalation before process creation. The reviewer reason was that sending the private Deep Research document to the current Codex/model provider requires explicit user approval after the risk is stated, because the transcript did not prove that provider as a tenant pre-trusted destination.

No candidate marketplace/plugin/cache residue was observed after the rejected attempt.

K3 remains mandatory before fresh holdouts, Terra review, release CI, production smoke, Reviewer, final user acceptance, and latest-main integration.
