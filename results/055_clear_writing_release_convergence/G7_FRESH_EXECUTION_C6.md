# G7 Fresh Execution Evidence for C6

Task: `055_clear_writing_release_convergence`

Date: `2026-09-16`

Status: `G7_3_OF_3_PASS`

## Candidate Identity

```text
FINAL_CANDIDATE_COMMIT = 79d620a0c60cdd086dd5828c8686bac843291cda
candidate label = C6
plugin = writing-style
plugin id used by replay = writing-style@ai-skills-candidate
plugin version = 0.3
runtime = codex-cli 0.153.4
```

This G7 batch used the exactly-three public-safe sources frozen in:

```text
results/055_clear_writing_release_convergence/G7_FRESH_BATCH_MANIFEST.md
```

No fresh item was replaced, added, edited after output, or used to tune the
candidate.

## Source Hashes

```text
G7_F1_NOISY_CODE_REPRO
source = results/055_clear_writing_release_convergence/g7_fresh_batch/sources/noisy_code_reproduction_source.md
sha256 = 9c9f3d32e04ab47466fc2d7dd90b740fe694907727911a7416443e03ebcc65ef

G7_F2_FORMULA_TABLE
source = results/055_clear_writing_release_convergence/g7_fresh_batch/sources/formula_table_structured_source.md
sha256 = 85cec2d4ca030db4c7c5c50b1213059cf2e903df85ae03f32e4bb46df99f7ca5

G7_F3_LONG_FUTURE_LIMITATIONS
source = results/055_clear_writing_release_convergence/g7_fresh_batch/sources/long_future_limitations_source.md
sha256 = 690cc84c8c70c895ba8d604a1050be932fb280b3795aba440a9db066bedcf2d3
```

## Replay Evidence

All three items were generated through the canonical candidate plugin replay
helper with:

```text
--candidate-commit 79d620a0c60cdd086dd5828c8686bac843291cda
```

### F1 Replay

```text
run id = .local-runtime/candidate-plugin-replay/runs/20260916T153835Z-1139772
run artifact = results/055_clear_writing_release_convergence/g7_fresh_batch/F1_noisy_code_repro/artifacts/run.json
run.json sha256 = f77a8b4fce02620496b652b66b64ccb28ffadf70f47dc5d81f802f0d399823d8
candidate output = results/055_clear_writing_release_convergence/g7_fresh_batch/F1_noisy_code_repro/artifacts/g7_f1_noisy_code_repro.md
candidate output sha256 = 32e6352d0d37c5c3e65fa8ee4e1108c74764893f703ad35d87dd330aa2b89454
actual_consumption.proven = true
actual_consumption.event_type = item.started
actual_consumption.line_index = 4
```

### F2 Replay

```text
run id = .local-runtime/candidate-plugin-replay/runs/20260916T154010Z-1144688
run artifact = results/055_clear_writing_release_convergence/g7_fresh_batch/F2_formula_table/artifacts/run.json
run.json sha256 = 0b682639855bbfd8c132e7e813df2d5d1998e69e394a0fe693e74a76ed060588
candidate output = results/055_clear_writing_release_convergence/g7_fresh_batch/F2_formula_table/artifacts/g7_f2_formula_table.md
candidate output sha256 = 1b7153b9030cf8c1bcb6aea6455f02c8cf620e3d947d23c38db09174179684c3
actual_consumption.proven = true
actual_consumption.event_type = item.started
actual_consumption.line_index = 4
```

### F3 Replay

```text
run id = .local-runtime/candidate-plugin-replay/runs/20260916T154156Z-1147198
run artifact = results/055_clear_writing_release_convergence/g7_fresh_batch/F3_long_future_limitations/artifacts/run.json
run.json sha256 = aa6709e43c7801d305208e615e6224b30bae5860ad755494ebd445ddbd997792
candidate output = results/055_clear_writing_release_convergence/g7_fresh_batch/F3_long_future_limitations/artifacts/g7_f3_long_future_limitations.md
candidate output sha256 = 6fa5b88712c42607abec07c5196ae802c26c59e9e2135f94d8cd3746f5675d74
actual_consumption.proven = true
actual_consumption.event_type = item.started
actual_consumption.line_index = 4
```

## Render Evidence

F1 did not require render.

F2 and F3 were rendered through Pandoc + XeLaTeX using:

```text
/overflow/htzhu/mingcheng_new/render_resources/chinese_math_pdf/scripts/render_markdown_pdf.sh
```

### F2 Render

```text
pdf = results/055_clear_writing_release_convergence/g7_fresh_batch/F2_formula_table/render/g7_f2_formula_table.pdf
pdf sha256 = cd15f8ad9736ac36b86c167b8a929f6bef7d709ae142f344a0ecbce8a4eed3dd
page count = 1
page preview = results/055_clear_writing_release_convergence/g7_fresh_batch/F2_formula_table/render/g7_f2_formula_table_page-1.png
page preview sha256 = 237aaa073ceb00c3dc105a02dd94568b2f8423bd1cedb1b7a34d15921172c0cb
text extraction = results/055_clear_writing_release_convergence/g7_fresh_batch/F2_formula_table/render/g7_f2_formula_table.extracted.txt
fonts = embedded/subset NotoSerifSC-Regular, NotoSerifSC-Bold, TeXGyreTermes-Regular, TeXGyreTermesMath-Regular
visual QA = PASS; formula is visible, table columns are intact, no clipping, no mojibake, no browser/header/footer artifact
```

### F3 Render

```text
pdf = results/055_clear_writing_release_convergence/g7_fresh_batch/F3_long_future_limitations/render/g7_f3_long_future_limitations.pdf
pdf sha256 = 486e3187a08ecbed6741d8103c9114da26eb5afdf35c08778d3d8fb237892178
page count = 1
page preview = results/055_clear_writing_release_convergence/g7_fresh_batch/F3_long_future_limitations/render/g7_f3_long_future_limitations_page-1.png
page preview sha256 = 4d6192ccca8d1a713e782e2827c958359bd0783185ea4c9d30efec36b33ea9c8
text extraction = results/055_clear_writing_release_convergence/g7_fresh_batch/F3_long_future_limitations/render/g7_f3_long_future_limitations.extracted.txt
fonts = embedded/subset NotoSerifSC-Regular, NotoSerifSC-Bold, TeXGyreTermes-Regular
visual QA = PASS; full one-page artifact is readable, section flow is preserved, no clipping, no broken glyphs
```

## Source-Aware Acceptance

### F1 -- Noisy Code / Reproduction Tokens

Result: `PASS`

Applied criteria: `G2,G3,G4,G5`

- A / G2 source fidelity: The candidate preserves the scope as a small
  scRNA-seq preprocessing QC script, the 6-donor and approximately 18,000-cell
  scope, the `--max-mito 0.25` versus `--max-mito 0.18` comparison, the
  additional 7% cell removal observation, and the warning that the stricter
  threshold is not proven to improve clustering.
- G3 code/path/reproducibility: The legitimate command remains present with
  `python scripts/prepare_scrna.py`, `data/raw/pbmc_merged.h5ad`,
  `data/processed/pbmc_qc.h5ad`, `--min-genes 300`, `--max-mito 0.18`, and
  `--batch-key donor_id`. The output also preserves the behavior that missing
  `donor_id` stops the script instead of silently collapsing batches.
- G4 wrapper/internal trace cleanup: Export navigation, sidebar/footer/cache
  noise, and non-reader wrappers are removed from the final prose.
- B / G5 qualitative reading: The output reads as a concise collaborator-facing
  technical note. It keeps future work as future work and avoids internal
  execution-log voice.

Failure attribution: `NONE`

### F2 -- Formula / Table Structured Content

Result: `PASS`

Applied criteria: `G2,G3,G5,G6`

- A / G2 source fidelity: The candidate preserves that epsilon `0.003` is a
  tradeoff rather than the lowest validation RMSE. It keeps the distinction
  between validation and test RMSE, the fixed `m = 5`, the numerical-stability
  role of `10^-8`, and the need for larger external-test confirmation.
- G3 formula/table integrity: The stopping criterion formula is retained with
  the same numerator, denominator, threshold comparison, and variables. The
  table keeps all rows and values: `0.010 -> 21.3 (3.1), 0.842 (0.018),
  0.861 (0.022)`; `0.003 -> 38.7 (4.5), 0.801 (0.011), 0.819 (0.015)`;
  `0.001 -> 64.0 (8.2), 0.795 (0.014), 0.833 (0.020)`.
- B / G5 qualitative reading: The explanation correctly says `0.003` is chosen
  because its test performance and training time are the more stable compromise,
  while `0.001` has slightly better validation RMSE but worse test stability.
- G6 render QA: The real PDF render was inspected. Formula and table are
  visible, extractable, and not clipped or corrupted.

Failure attribution: `NONE`

### F3 -- Long-form Future Work / Limitation / Attribution

Result: `PASS`

Applied criteria: `G2,G5,G6`

- A / G2 source fidelity: The candidate preserves the retrospective/internal
  nature of the evidence, 4 hospitals, 1,240 images, the A/B training split,
  C validation split, D internal-test split, U-Net baseline, lightweight
  attention module, Dice improvement from `0.781` to `0.806`, Hausdorff
  distance reduction from `9.4 mm` to `8.1 mm`, the approximate expert-label
  Dice `0.84`, and all three future-work items as not yet completed.
- B / G5 qualitative reading: The output is a coherent stage technical
  summary, not a task checklist. It keeps modality correct by saying external
  validation, stratified failure analysis, and reader-assist experiments remain
  future work.
- G6 render QA: The real PDF render was inspected. The one-page artifact is
  readable and complete, with no clipping, broken glyphs, wrapper trace, or
  layout corruption.

Failure attribution: `NONE`

## G7 Decision

```text
G7_F1_NOISY_CODE_REPRO = PASS
G7_F2_FORMULA_TABLE = PASS
G7_F3_LONG_FUTURE_LIMITATIONS = PASS
G7_RESULT = 3/3 PASS
```

No `PLUGIN_DEFECT`, `SOURCE_DEFECT`, `REVIEWER_RUBRIC_DEFECT`,
`ENVIRONMENT_DEFECT`, `WORKFLOW_DEFECT`, or `CONTRACT_AMBIGUITY` remains open
from this G7 batch.

Next authorized gate under the frozen Goal is the single bounded final Terra
Text Review. Terra was not run during G7.
