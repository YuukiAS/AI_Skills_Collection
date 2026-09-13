# 054 Fresh Holdout Batch Status

Status: PASS for Gate D exactly-3 fresh holdout batch.

Candidate commit: `245127e1bb46f860ea1976b1669c467c7a9f763d`

Fresh batch manifest: `results/054_clear_writing_release_closure/fresh_holdouts/fresh_holdout_batch_manifest.md`

Batch audit: `results/054_clear_writing_release_closure/fresh_holdouts/fresh_holdout_batch_audit.json`

## Batch Integrity

- Exactly 3 public-safe holdouts were frozen before generation: H1 noisy scikit-learn RST docs, H2 Chinese confusion-matrix wiki material, and H3 long-form Pumpkin Book neural-network material.
- No H4, replacement, or adaptive sample was added.
- All three replay runs consumed the installed candidate plugin from the official local marketplace/cachebuster/reinstall/fresh-session route.
- All three `run.json` files bind to candidate commit `245127e1bb46f860ea1976b1669c467c7a9f763d` and plugin tree `ca4d23cfeb4937313d588a04eee966c262a1cadc`.

## H1 Noisy scikit-learn RST Docs

- Replay run: `20260913T043901Z-2700709`
- Candidate Markdown: `results/054_clear_writing_release_closure/fresh_holdouts/h1_noisy_sklearn_docs/replay/feature-hashing-zh.md`
- Local audit: `results/054_clear_writing_release_closure/fresh_holdouts/h1_noisy_sklearn_docs/replay/local_audit.json`
- Rendered PDF: `results/054_clear_writing_release_closure/render_qa/fresh_holdouts/h1_noisy_sklearn_docs/feature-hashing-zh.pdf`
- Rendered pages: `results/054_clear_writing_release_closure/render_qa/fresh_holdouts/h1_noisy_sklearn_docs/page-1.png`, `results/054_clear_writing_release_closure/render_qa/fresh_holdouts/h1_noisy_sklearn_docs/page-2.png`
- Result: PASS.

Checks:

- RST wrapper syntax such as anchors, `:class:`, `:ref:`, dropdown/rubric markup, and source packaging was removed.
- Required technical identities remain: `FeatureHasher`, `Feature hashing`, `MurmurHash3`, `signed 32-bit`, `alternate_sign`, `scipy.sparse`, and `HashingVectorizer`.
- Four fenced blocks are Python code examples required by the source task; no formula-like `text` or `plain` fenced block is present.
- PDF render produced a 2-page unencrypted A4 PDF with embedded CJK, TeX Gyre Termes, monospaced, and math fonts.
- Visual inspection of pages 1 and 2 found readable Chinese prose, readable code examples, no clipping, no missing-glyph issue, and no raw source markup leakage.

## H2 Chinese Confusion-Matrix Material

- Replay run: `20260913T044041Z-2704773`
- Candidate Markdown: `results/054_clear_writing_release_closure/fresh_holdouts/h2_confusion_matrix_zhwiki/replay/混淆矩阵.md`
- Stage receipt: `results/054_clear_writing_release_closure/fresh_holdouts/h2_confusion_matrix_zhwiki/replay/stages/stage_receipt.json`
- Semantic audit: `results/054_clear_writing_release_closure/fresh_holdouts/h2_confusion_matrix_zhwiki/replay/stages/semantic_audit.json`
- Local audit: `results/054_clear_writing_release_closure/fresh_holdouts/h2_confusion_matrix_zhwiki/replay/local_audit.json`
- Rendered PDF: `results/054_clear_writing_release_closure/render_qa/fresh_holdouts/h2_confusion_matrix_zhwiki/混淆矩阵.pdf`
- Rendered pages: `results/054_clear_writing_release_closure/render_qa/fresh_holdouts/h2_confusion_matrix_zhwiki/page-1.png`, `results/054_clear_writing_release_closure/render_qa/fresh_holdouts/h2_confusion_matrix_zhwiki/page-2.png`
- Result: PASS.

Checks:

- Heavy route receipt reports ordinary `writing-style` route selection to `scientific-rewrite`, 8 source anchors, 6 meanings, 14 exact items, 1 excluded source-context item, semantic audit PASS, exact verification PASS, and candidate representation PASS.
- Raw wiki/template/ref/category/archive markup was removed.
- Confusion-matrix table meaning, cat/dog counts, binary TP/FN/FP/TN framing, imbalance example, F1 relation, and Youden's J relation remain present.
- PDF render produced a 2-page unencrypted A4 PDF with embedded CJK, TeX Gyre Termes, and math fonts.
- Visual inspection of both pages found readable tables and formulas with no clipping or raw markup leakage.

## H3 Pumpkin Book Long-Form Neural-Network Material

- Replay run: `20260913T044513Z-2716369`
- Candidate Markdown: `results/054_clear_writing_release_closure/fresh_holdouts/h3_pumpkin_book_longform/replay/神经网络：从感知机到深度学习.md`
- Stage receipt: `results/054_clear_writing_release_closure/fresh_holdouts/h3_pumpkin_book_longform/replay/stages/stage_receipt.json`
- Semantic audit: `results/054_clear_writing_release_closure/fresh_holdouts/h3_pumpkin_book_longform/replay/stages/semantic_audit.json`
- Local audit: `results/054_clear_writing_release_closure/fresh_holdouts/h3_pumpkin_book_longform/replay/local_audit.json`
- Rendered PDF: `results/054_clear_writing_release_closure/render_qa/fresh_holdouts/h3_pumpkin_book_longform/神经网络：从感知机到深度学习.pdf`
- Rendered pages: `results/054_clear_writing_release_closure/render_qa/fresh_holdouts/h3_pumpkin_book_longform/page-1.png` through `results/054_clear_writing_release_closure/render_qa/fresh_holdouts/h3_pumpkin_book_longform/page-7.png`
- Result: PASS.

Checks:

- Heavy route receipt reports ordinary `writing-style` route selection to `scientific-rewrite`, 106 source anchors, 8 meanings, 30 exact items, 1 excluded source-context item, semantic audit PASS, exact verification PASS, and candidate representation PASS.
- Required long-form concepts remain: neuron, perceptron, multilayer network, misclassification, loss function, gradient, backpropagation, local/global minima, deep learning, and LeCun/Bengio/Hinton attribution.
- No raw wiki/source markup, workflow leakage, source-process framing, or formula-like fenced text is present. Earlier brace-based `{{` / `}}` raw-markup detections were false positives from LaTeX math braces, not template leakage.
- PDF render produced a 7-page unencrypted A4 PDF with embedded CJK, TeX Gyre Termes, and math fonts.
- Visual inspection of pages 1, 4, and 7 found readable long-form Chinese structure, readable mathematical derivations, no clipping, and no raw markup leakage.

## Gate D Decision

Gate D passes as an exactly-3 complete batch. The next authorized gate is the single final `gpt-5.6-terra` Text Review described by the canonical 054 Goal and frozen Plan.
