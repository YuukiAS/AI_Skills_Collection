---
schema: AI_SKILLS_053_FRESH_HOLDOUT_STATUS_V1
task_key: 053_clear_writing_release_quality_hardening
candidate_commit: d4570c764326cd10b63eae5e605cc8ff885bd7f2
status: FAIL
recorded_at: 2026-09-12T17:01:40Z
---

# 053 Fresh Holdout Status

Overall fresh gate status: FAIL

The frozen two-item public-safe fresh holdout batch was executed exactly once
per source against the frozen production candidate commit:

```text
d4570c764326cd10b63eae5e605cc8ff885bd7f2
```

The batch manifest remains:

```text
results/053_clear_writing_release_quality_hardening/fresh_holdouts/fresh_holdout_batch_manifest.json
```

No third holdout was selected, no replacement was made, and no production tuning
was performed after the batch started.

## H1 - Karatsuba Raw Wikitext

Status: FAIL

Replay evidence:

```text
run = .local-runtime/candidate-plugin-replay/runs/20260912T164653Z-2816518/
actual candidate SKILL consumption = PASS
candidate_commit = d4570c764326cd10b63eae5e605cc8ff885bd7f2
cleanup = PASS
```

Markdown/local audit evidence:

```text
candidate_representation = PASS
raw wiki/template/ref/math-tag leakage = 0
formula_text_fences = 0
unrendered_math = 0
source_process_framing = 0
workflow_trace = false
required_literals = PASS
```

Rendered artifact QA:

```text
pdf = results/053_clear_writing_release_quality_hardening/fresh_holdouts/h1_karatsuba_wikitext/h1_karatsuba.pdf
page_image = results/053_clear_writing_release_quality_hardening/fresh_holdouts/h1_karatsuba_wikitext/page-1.png
decision = FAIL
failure_class = reader_visible_missing_glyph
```

The H1 PDF render emitted missing-character warnings for Cyrillic glyphs, and
visual inspection of page 1 confirmed a reader-visible blank in the sentence
containing the Russian title after `俄文名称为`. This is a true rendered-artifact
failure under the 053 Plan because file existence/render exit success cannot
substitute for reader-visible PDF quality.

## H2 - D2L Self-Attention And Positional Encoding

Status: PASS

Replay evidence:

```text
run = .local-runtime/candidate-plugin-replay/runs/20260912T165409Z-2884781/
actual candidate SKILL consumption = PASS
candidate_commit = d4570c764326cd10b63eae5e605cc8ff885bd7f2
cleanup = PASS
```

Markdown/local audit evidence:

```text
candidate_representation = PASS
reader_visible_markup_count = 0
formula_text_fences = 0
unrendered_math = 0
overwide_tables = 0
source_process_framing = 0
workflow_trace = false
required_literals = PASS
semantic_audit = PASS
stage_receipt = PASS
```

Rendered artifact QA:

```text
pdf = results/053_clear_writing_release_quality_hardening/fresh_holdouts/h2_d2l_self_attention/h2_d2l_self_attention.pdf
pages = 2
page_size = A4
encrypted = no
visual_inspection = PASS for page-1.png and page-2.png
```

H2 rendered with readable formulas, a real table, normal Chinese prose, and no
visible source-format or workflow leakage in the inspected pages.

## Gate Consequence

Under the frozen Plan, any true failure in the exactly-two fresh holdout batch
fails the whole fresh gate. The legal next state is Planner-owned review of the
fresh-holdout render QA failure. Terra Text Review, release CI, production
smoke, GPT Reviewer handoff, final user acceptance, and latest-main integration
must not start from this failed fresh gate.
