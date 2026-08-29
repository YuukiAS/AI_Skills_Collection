---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 041_research_presentation_frozen_four_paper_generalization_batch
executor: Codex
implementation_commit: 9bd69e5b54e7968ec731e00a3c9794c6fad21672
status: WAITING_FOR_CI
ci_status: PENDING
---

# Result: 041 Frozen Four-Paper Generalization Batch

Implementation commit: `9bd69e5b54e7968ec731e00a3c9794c6fad21672`

## Batch-level verdict

The strict frozen 4/4 batch failed locally before CI and after consuming the only permitted frozen quality-loop evidence for the two rendered decks.

All four paper identities were audited together before acquisition, all four source bundles were frozen before any successful render, and the frozen normal `research-presentations` production entrypoint was used without production-code, gold, layout, prompt, validator, quality-loop, generated-TeX, image, or source-bundle repair.

Two decks generated and rendered mechanically, then consumed the current Terra evidence through the shipped single-cycle quality-loop consumer:

- `biostatistics_deseq2`
- `medical_cardiac_ultrasound`

Two decks failed before render:

- `statistics_tmb`
- `medical_retfound`

Both failures are the same normal-selector failure:

```text
ValueError: no compatible gold composition record
```

The frozen consumer selected no repair directive for either rendered deck. Both fail closed as `UNSAFE_REPAIR_MAPPING / QUALITY_LOOP_FAIL_NO_WINNER`, because the current structured findings did not uniquely map to a frozen safe repair family.

Per the frozen batch rules, no paper was replaced, no source bundle was edited after rendered output existed, and no output was hand-patched to chase a pass. Because any one deck failing makes the full batch fail, this 041 batch is recorded as `FAIL_TWO_PRE_RENDER_SELECTOR_FAILURES_AND_TWO_QUALITY_LOOP_FAIL_CLOSED`. All four papers are consumed holdouts.

## Frozen eligibility and source acquisition

Pre-acquisition eligibility audit:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/batch_eligibility.json
```

Production freeze verification:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/production_freeze_verification.json
```

Frozen bundle manifest:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/batch_source_bundle_freeze_manifest.json
```

The four public PDFs were downloaded to `/tmp/rh041_sources`, converted to text for full-paper reading, and used to build task-local source notes, inventories, real article figure/table page pixels, and source bundles.

PDF hashes:

- TMB: `956c23742c544fa839525e3108cfbbc28936ff711c5f9f1018aef73e79aee85e`, 21 pages.
- DESeq2: `96af759d0ffad2df06af8860e7ea7ae1ce380ce6e22843ad2519b801bc1999bb`, 21 pages.
- cardiac ultrasound: `bbb31b8d206c142d4d659c5ebb9d2fb1a190fd5c175f0a8963e914474cf078e9`, 13 pages.
- RETFound: `fe4cdfb0aaa4fb539b89bfb0280731f2619820c2dc97440360e1bf74f3bee798`, 26 pages.

Source-bundle hashes:

- TMB: `7da33f5f7cd497a1e7a6d65f5b2701e56c68be6781d34dede3143adae4261c0e`
- DESeq2: `52f58af783041ca3b4316141818db9bd781b1d63c7d2e16fa99b8493d798a962`
- cardiac ultrasound: `4e62035d6aa495832ad7b3b8235e71ed3ffaf29e0338c0e556985112210f2243`
- RETFound: `6e54dd6f960c8188b20dfcc7ab1988e988d69b85015f2cad049d35c935f55147`

The audit recorded TMB and cardiac-ultrasound 040 mentions as non-consuming historical Planner-only mentions. It also recorded DESeq2 hits in existing PyDESeq2 skill/domain material as non-presentation references, not `research-presentations` source/gold/tuning/render consumption.

## Per-paper production evidence

### statistics_tmb

Paper: Kristensen et al. (2016), `TMB: Automatic Differentiation and Laplace Approximation`, DOI `10.18637/jss.v070.i05`.

Frozen source artifacts:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/statistics_tmb/source/source.md
results/041_research_presentation_frozen_four_paper_generalization_batch/statistics_tmb/source_inventory.json
results/041_research_presentation_frozen_four_paper_generalization_batch/statistics_tmb/source_bundle.json
```

Normal production invocation failed before render:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/statistics_tmb/production_attempt_failure.log
```

No PDF, rendered page PNG, contact sheet, Terra PASS, or quality-loop repair is claimed for TMB.

### biostatistics_deseq2

Paper: Love, Huber, and Anders (2014), `Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2`, DOI `10.1186/s13059-014-0550-8`.

Generated artifacts:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/
```

Key identities:

- PDF: `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/cuhk_production_build/main.pdf`
- PDF SHA256: `70413e6d480f20bc54e78a7edd3b1eac28a7b292ebaf59afec906ebe92a269c7`
- render-input identity: `ac79e2bf664eaca1984a01d8689c1d60ced785a45a9e6c6d2a2fa50b95efd87e`
- rendered-pixel identity: `5b8b8596996f9589e09f64a495b9f0b98fbffb2be5ec8f4bc582a9628ff77bd9`
- contact sheet SHA256: `13a925ca7d505dd9621be69270a7d0580600acf5ba83dc2a97b7dbc2e97078ab`
- quality-loop state: `UNSAFE_REPAIR_MAPPING`, `final_decision=QUALITY_LOOP_FAIL_NO_WINNER`, `repair_cycle_count=0`
- consumed repair evidence: `results/041_research_presentation_frozen_four_paper_generalization_batch/visual_review/biostatistics_deseq2_repair_evidence.json`
- repair evidence SHA256: `e27057fcb83dd9a1cbe19480d7a19801ec5ecef746c754790d4c70d3c323b0c4`
- selected repair directives: none
- rendered-pixel identity changed by quality loop: `false`

### medical_cardiac_ultrasound

Paper: Ferreira et al. (2025), `Self-supervised learning for label-free segmentation in cardiac ultrasound`, DOI `10.1038/s41467-025-59451-5`.

Generated artifacts:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/
```

Key identities:

- PDF: `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/cuhk_production_build/main.pdf`
- PDF SHA256: `a7fcd52ac88e2783a85e0610f5935a0f0b27b153bacfa55cf1d93e825026cb18`
- render-input identity: `427322503d37fbb586c5d3332b231448f55df502f9734d76ccb3af52dd37794d`
- rendered-pixel identity: `5d482b290887882819458dfbd09e5d5ba9351625259dbec59f3de61a2b4a4fc6`
- contact sheet SHA256: `1792084d006f5a718c2f96197ec538ebf16cfb531d00edd9ba542b23171cfec7`
- quality-loop state: `UNSAFE_REPAIR_MAPPING`, `final_decision=QUALITY_LOOP_FAIL_NO_WINNER`, `repair_cycle_count=0`
- consumed repair evidence: `results/041_research_presentation_frozen_four_paper_generalization_batch/visual_review/medical_cardiac_ultrasound_repair_evidence.json`
- repair evidence SHA256: `d2dcb25b193049d81b83d59975e199dc116ea826ab4d1c54aab34de1871a8166`
- selected repair directives: none
- rendered-pixel identity changed by quality loop: `false`

The deck uses real article echocardiography figure page pixels from the cardiac-ultrasound paper. No generated or substitute medical image pixels were introduced.

### medical_retfound

Paper: Zhou et al. (2023), `A foundation model for generalizable disease detection from retinal images`, DOI `10.1038/s41586-023-06555-x`.

Frozen source artifacts:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/medical_retfound/source/source.md
results/041_research_presentation_frozen_four_paper_generalization_batch/medical_retfound/source_inventory.json
results/041_research_presentation_frozen_four_paper_generalization_batch/medical_retfound/source_bundle.json
```

Normal production invocation failed before render:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/medical_retfound/production_attempt_failure.log
```

No PDF, rendered page PNG, contact sheet, Terra PASS, or quality-loop repair is claimed for RETFound.

## Combined visual-review handoff

Task-local manifest:

```text
results/041_research_presentation_frozen_four_paper_generalization_batch/visual_review/visual_inputs.json
```

It contains the two rendered decks only: six substantive pages plus contact sheet for DESeq2, and six substantive pages plus contact sheet for cardiac ultrasound. The manifest also records TMB and RETFound as failed decks with failure-log hashes, and it records that the two rendered decks consumed the available quality-loop evidence and failed closed with no repair directive. A visual-only PASS on the rendered subset cannot be interpreted as 4/4 batch PASS.

No `VISUAL_REVIEW.json` was fabricated locally. The existing Terra output remains the source evidence consumed by the frozen quality-loop consumer; the unified manifest is updated for the new implementation commit so any subsequent task-local visual review can detect whether fresh evidence is required.

## Local verification

Passed locally:

```text
python -m json.tool results/041_research_presentation_frozen_four_paper_generalization_batch/batch_eligibility.json
python -m json.tool results/041_research_presentation_frozen_four_paper_generalization_batch/batch_source_bundle_freeze_manifest.json
python -m json.tool results/041_research_presentation_frozen_four_paper_generalization_batch/production_invocations.json
python -m json.tool results/041_research_presentation_frozen_four_paper_generalization_batch/local_acceptance.json
python -m json.tool results/041_research_presentation_frozen_four_paper_generalization_batch/visual_review/visual_inputs.json
python -m json.tool results/041_research_presentation_frozen_four_paper_generalization_batch/visual_review/biostatistics_deseq2_repair_evidence.json
python -m json.tool results/041_research_presentation_frozen_four_paper_generalization_batch/visual_review/medical_cardiac_ultrasound_repair_evidence.json
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/source_bundle.json --out-dir results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated --task-key 041_research_presentation_frozen_four_paper_generalization_batch --review-evidence results/041_research_presentation_frozen_four_paper_generalization_batch/visual_review/biostatistics_deseq2_repair_evidence.json
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/source_bundle.json --out-dir results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated --task-key 041_research_presentation_frozen_four_paper_generalization_batch --review-evidence results/041_research_presentation_frozen_four_paper_generalization_batch/visual_review/medical_cardiac_ultrasound_repair_evidence.json
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
python -m unittest discover -s tests -p 'test_presentations.py' -k test_research_presentation_one_call_production_entry
python -m unittest discover -s tests
ai-bridge reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
ai-bridge visual-review preflight --target /home/yuukias/AI_Skills_Collection
pdfinfo results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/cuhk_production_build/main.pdf
pdfinfo results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/cuhk_production_build/main.pdf
git diff --check
```

Observed results:

- targeted presentation unittest: `Ran 1 test`, `OK`
- full unittest: `Ran 146 tests`, `OK`
- `scripts/skills.py validate`: validated 149 active skills and 18 profiles
- marketplace validate/check/path-report: passed; Windows path budget overage count `0`
- Reviewed Handoff validation passed
- visual-review preflight passed and listed task 041
- DESeq2 PDF: 7 pages, render status `ok`
- cardiac-ultrasound PDF: 7 pages, render status `ok`
- quality-loop fail-closed identity check: `PASS`
- `git diff --check`: passed

Known non-PASS local evidence:

- TMB normal production invocation failed before render with `ValueError: no compatible gold composition record`.
- RETFound normal production invocation failed before render with `ValueError: no compatible gold composition record`.
- DESeq2 quality-loop consumer returned `UNSAFE_REPAIR_MAPPING / QUALITY_LOOP_FAIL_NO_WINNER`; no repair directive was selected and the rendered-pixel identity remained `5b8b8596996f9589e09f64a495b9f0b98fbffb2be5ec8f4bc582a9628ff77bd9`.
- cardiac-ultrasound quality-loop consumer returned `UNSAFE_REPAIR_MAPPING / QUALITY_LOOP_FAIL_NO_WINNER`; no repair directive was selected and the rendered-pixel identity remained `5d482b290887882819458dfbd09e5d5ba9351625259dbec59f3de61a2b4a4fc6`.
- The strict production-entry validator remains non-holdout-aware for these real-paper decks; it reports 031 task-key mismatch and still asserts engineering-fixture phrases such as `Coverage by ICC under imbalanced clusters` and `Same-case ROI zoom`. It rejected the two rendered holdout decks on that basis, so I did not use it to claim holdout acceptance.
- Local contact-sheet inspection found nonblank exact-CUHK Beamer output for the two rendered decks, but Terra already recorded repeated scale and overflow blockers.

## Remaining gates

GitHub CI is required and is not claimed locally. Per protocol, `ci_status` remains `PENDING` and this task is left in `WAITING_FOR_CI` for watcher validation/publication and real GitHub checks.

Because the batch already failed 4/4 locally, any subsequent Planner/Reviewer decision must preserve the frozen-batch failure semantics: no replacement paper, no post-output source rewrite, no hand TeX/image patch, and no declaration of 041 generalization PASS from the two successful renders.
