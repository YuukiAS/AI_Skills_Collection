# 053 Known Regression Status

Status: K1_K2_K3_K4_PASS_REFRESHED_ON_LATEST_CANDIDATE

Latest candidate commit: `d4570c764326cd10b63eae5e605cc8ff885bd7f2`

## K1 Bloom raw-wikitext

Status: PASS for Markdown candidate, stage receipt, candidate consumption, and public PDF render QA refreshed on latest candidate commit.

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
- Replay metadata records candidate commit `d4570c764326cd10b63eae5e605cc8ff885bd7f2`.
- `candidate_representation.ok = true`.
- `exact_verification.ok = true`.
- `semantic_audit.ok = true`.
- No raw wiki/template/HTML/ref/comment syntax found in reader-facing Markdown or PDF text extraction.
- No source-process or workflow-wrapper leakage found in reader-facing Markdown or PDF text extraction.
- PDF rendered through Pandoc -> XeLaTeX; `pdfinfo` reported 1 page, unencrypted, A4.
- `pdffonts` reported embedded subset Noto Serif SC and TeX Gyre Termes fonts.
- Visual page inspection found no obvious clipping, missing glyphs, code-fence formula, or raw markup leakage.

## K2 FFT math

Status: PASS for Markdown candidate, actual candidate consumption, deterministic literal/representation audit, and public PDF render QA refreshed on latest candidate commit.

Evidence:

- Candidate Markdown: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/fft_wikipedia.md`
- Latest deterministic audit: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/local_audit.json`
- Prior heavy-route stage receipt retained as historical evidence only: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/stage_receipt.json`
- Prior semantic audit retained as historical evidence only: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/semantic_audit.json`
- Prior route selection retained as historical evidence only: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/route_selection.json`
- Replay metadata: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/run.json`
- Cleanup evidence: `results/053_clear_writing_release_quality_hardening/known_regressions/fft/cleanup.json`
- Rendered PDF: `results/053_clear_writing_release_quality_hardening/render_qa/fft/fft_wikipedia.pdf`
- Render text extraction: `results/053_clear_writing_release_quality_hardening/render_qa/fft/fft_wikipedia.txt`
- First-page PNG: `results/053_clear_writing_release_quality_hardening/render_qa/fft/page-1.png`

Checks:

- Actual candidate `SKILL.md` consumption proven from child JSONL.
- Replay metadata records candidate commit `d4570c764326cd10b63eae5e605cc8ff885bd7f2`.
- `local_audit.required_literals_present = true`.
- `local_audit.candidate_representation.ok = true`, including `overwide_table_count = 0`.
- `local_audit.source_process_framing_count = 0`.
- `local_audit.workflow_trace = false`.
- Candidate uses display math for the DFT formula, not a fenced `text` block.
- Candidate preserves the DFT definition, `O(N^2)`, `O(N log N)`, `(N/2)\log_2 N`, the Cooley-Tukey power-of-two condition, the numerical-accuracy caveat, and historical attribution.
- No raw wiki/template/HTML/ref/comment syntax found in reader-facing Markdown or PDF text extraction.
- No source-process or workflow-wrapper leakage found in reader-facing Markdown or PDF text extraction.
- PDF rendered through Pandoc -> XeLaTeX; `pdfinfo` reported 1 page, unencrypted, A4.
- `pdffonts` reported embedded subset Noto Serif SC, TeX Gyre Termes, LM Mono, and TeX Gyre Termes Math fonts.
- Visual page inspection found the DFT summation rendered as centered math with no clipping or code fence.

## K3 complete private Deep Research

Status: PASS after one additional bounded recovery replay authorized by current workflow state.

K3 source and comparison baselines were located by path, byte size, and SHA-256 only. Private plaintext was not printed, committed, or pushed.

Provider-trust approval was recorded after Auto-review raised the private-provider boundary:

```text
results/053_clear_writing_release_quality_hardening/k3_provider_trust_approval.md
```

The canonical two K3 private candidate replays plus the one additional bounded
recovery replay have now been consumed.

Detailed non-secret evidence:

```text
results/053_clear_writing_release_quality_hardening/k3_deep_research_status.md
```

The third replay proved actual candidate `SKILL.md` consumption against
candidate commit `d4570c764326cd10b63eae5e605cc8ff885bd7f2` and produced a full
private Markdown/PDF. Candidate-level validation found no raw source markup,
formula-like text fences, unrendered math, malformed tables, overwide tables,
source-process framing, workflow leakage, or ordinary internal English framing.
Private PDF render QA used Pandoc -> XeLaTeX, produced a 12-page A4 PDF with
embedded Noto Serif SC / TeX Gyre Termes / math fonts, and visually confirmed
that the previously clipped page-7 wide table failure is closed.

K3 is now closed. K1, K2, and K4 were refreshed against the latest candidate
commit after the K3 table-width hardening.
