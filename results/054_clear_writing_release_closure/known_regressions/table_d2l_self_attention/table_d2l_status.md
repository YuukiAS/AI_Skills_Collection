# 054 Table / Formula-Rich Known Regression

Status: PASS for the 054 Gate B table/formula-rich stress slice.

Candidate commit: `245127e1bb46f860ea1976b1669c467c7a9f763d`

Replay run: `20260913T035703Z-2589051`

Input family: `053` public D2L self-attention / positional-encoding stress case, reused only as a 054 known/stress regression, not as a 054 fresh holdout.

## Evidence

- Candidate Markdown: `results/054_clear_writing_release_closure/known_regressions/table_d2l_self_attention/h2_d2l_self_attention.md`
- Replay metadata: `results/054_clear_writing_release_closure/known_regressions/table_d2l_self_attention/run.json`
- Cleanup evidence: `results/054_clear_writing_release_closure/known_regressions/table_d2l_self_attention/cleanup.json`
- Local deterministic audit: `results/054_clear_writing_release_closure/known_regressions/table_d2l_self_attention/local_audit.json`
- Rendered PDF: `results/054_clear_writing_release_closure/render_qa/table_d2l_self_attention/h2_d2l_self_attention.pdf`
- PDF text extraction: `results/054_clear_writing_release_closure/render_qa/table_d2l_self_attention/h2_d2l_self_attention.txt`
- First-page PNG: `results/054_clear_writing_release_closure/render_qa/table_d2l_self_attention/page-1.png`
- Second-page PNG: `results/054_clear_writing_release_closure/render_qa/table_d2l_self_attention/page-2.png`

## Checks

- Actual candidate plugin consumption is proven in `run.json`.
- `local_audit.json` records `candidate_representation.ok = true`, 5 Markdown table rows, 88 math spans, no malformed or overwide table, no formula text fence, no unrendered math, no Simplified/Traditional mismatch, and no workflow trace.
- Required technical identities and facts remain present: 自注意力, 位置编码, CNN, RNN, self-attention, positional encoding, `\mathcal{O}(n^2d)`, `\mathcal{O}(1)`, 最大路径长度, `p_{i,2j}`, `p_{i,2j+1}`, `10000`, `\delta`, Vaswani, and 练习.
- No raw wiki/template/HTML/ref/comment syntax, source-process framing, workflow leakage, or internal engineering framing was found in reader-facing Markdown or PDF text extraction.
- Pandoc -> XeLaTeX render produced a 2-page unencrypted A4 PDF with embedded subset Noto Serif SC, TeX Gyre Termes, TeX Gyre Termes Math, and NewCMMath fonts.
- Visual inspection covered both pages. Page 1 contains the CNN/RNN/self-attention comparison table inside page bounds with readable columns and no raw pipe table. Page 2 contains the positional-encoding formulas and matrix derivation without clipping, missing glyphs, or formula fences.
- PDF text extraction represents some math as Unicode math text, such as `𝒪(𝑛2 𝑑)` and `𝛿𝜔𝑗`; visual inspection confirms these are rendered mathematical symbols rather than lost operators.
