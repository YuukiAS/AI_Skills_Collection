---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 025_research_presentation_gold_scientific_composition_library
implementation_commit: d6fafda2819d406c88a2f363a22bdfd9564989cf
---

# 025 Research Presentation Gold Scientific Composition Library — Result

## Summary

Implemented the revised Stage 2 gold scientific composition library from the existing inspected reference corpus. The current library is a production subset admitted only by 025 item-level pixel evidence, with explicit source/render identity, rights boundaries, scientific-job compatibility metadata, selector traces, renderer-neutral recipe output, and deterministic probes that verify selected gold records are actually consumed.

Implementation commit:

```text
d6fafda2819d406c88a2f363a22bdfd9564989cf
```

## Gold Coverage

The gold index contains 9 records, not a blanket promotion of all 019 composition records:

- `GSC-004`: method / experiment design (`RRL-019`)
- `GSC-008`: medical sample introduction (`RRL-013`)
- `GSC-011`: motivation / research question (`RRL-009`)
- `GSC-012`: method / experiment design (`RRL-011`)
- `GSC-013`: mathematical / theorem-like comparison (`RRL-015`)
- `GSC-014`: biostatistics quantitative result (`RRL-016`)
- `GSC-015`: biostatistics quantitative result alternate (`RRL-017`)
- `GSC-016`: negative result / uncertainty comparison (`RRL-020`)
- `GSC-017`: medical / task visual comparison (`RRL-021`)

The index preserves composition-only reuse boundaries and keeps source pixels, logos, and donor branding out of the reusable payload.

## Rejected Candidates

The admission report records all 025 admission and bounded-recovery item-level decisions. Rejected candidates remain ordinary inspected references and were not promoted for coverage. The bounded existing-corpus screen did not admit a discussion / next-experiment page at the production gold threshold.

The full admission artifact is:

```text
docs/audits/research_presentation_gold_composition_library/gold_admission_report.json
```

## Runtime Consumption Evidence

The runtime probe artifact is:

```text
docs/audits/research_presentation_gold_composition_library/runtime_probe_traces.json
```

It contains two deterministic probes:

- `statistics_estimator_identity`: selected `GSC-014`, compared against compatible alternate `GSC-015`.
- `medical_aligned_prediction_error`: selected `GSC-008`, compared against compatible alternate `GSC-004`.

Both probes verify:

- `runtime_selected = true`
- `alternate_runtime_selected = true`
- `alternate_is_distinct = true`
- `alternate_has_compatibility_reasons = true`
- `actually_consumed = true`
- `output_affected = true`
- `primary_bbox_changed = true`
- `composition_family_available = true`

The recipe builder consumes these source-derived fields from the selected gold record:

- `primary_bbox`
- `visual_hierarchy`
- `alignment_groups`
- `reading_flow`
- `annotation_legend_caption_panel_relations`
- `content_capacity`

This proves `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` at the renderer-neutral recipe layer required by the frozen Plan.

## Changed Files

Added the source gold library contract and runtime tooling:

- `skills/tools/documents-media/presentations/shared/references/research_gold_composition.schema.json`
- `skills/tools/documents-media/presentations/shared/references/research_gold_composition_index.json`
- `skills/tools/documents-media/presentations/shared/scripts/validate_gold_compositions.py`
- `skills/tools/documents-media/presentations/shared/scripts/select_gold_compositions.py`
- `skills/tools/documents-media/presentations/shared/scripts/build_gold_composition_recipe.py`
- `skills/tools/documents-media/presentations/shared/scripts/generate_gold_composition_probe_artifacts.py`

Added generated/plugin mirror copies for the same schema, index, and scripts under:

```text
plugins/codex/plugins/presentations/shared/
```

Added deterministic audit artifacts:

- `docs/audits/research_presentation_gold_composition_library/gold_admission_report.json`
- `docs/audits/research_presentation_gold_composition_library/runtime_probe_traces.json`

Updated regression coverage in:

- `tests/test_presentations.py`

## Validation

Executed successfully:

```text
python skills/tools/documents-media/presentations/shared/scripts/validate_gold_compositions.py
python skills/tools/documents-media/presentations/shared/scripts/generate_gold_composition_probe_artifacts.py
python -m unittest tests.test_presentations
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
PYTHONPATH=/home/yuukias/GPT_Codex_AI_Bridge_Kit python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
git diff --check
```

Observed results:

- gold validator: `validated 9 gold scientific composition records`
- runtime probes: `status = PASS`, `probe_count = 2`
- targeted Presentation tests: 25 tests passed
- full unittest discovery: 121 tests passed
- skills validation: 149 active skills, 18 profiles, templates, and trigger eval scaffolds passed
- marketplace validation/path report: passed
- Reviewed Handoff validation: passed
- whitespace check: passed

`python scripts/build_codex_marketplace.py --write --validate --check --path-report` was not rerun during Revision 1 because the broader write command was not approved in the current executor environment. The source/plugin mirror files were mechanically synchronized for the changed schema/index/scripts, and the non-writing marketplace validation/check/path-report passed afterward.

## Scope Boundaries

This task did not:

- expand the reference corpus;
- run a new Source Scout;
- implement Stage 3 renderer/layout macros;
- modify the canonical CUHK template;
- modify or recover 023;
- run final statistical or medical-imaging holdouts;
- modify Terra core / Bridge Kit reviewer semantics;
- declare `ONE_SHOT_QUALITY_PASS` or `PROGRAM_MATURE`.

## Remaining Limitations

This is the first production gold subset from the existing inspected corpus. It proves gold admission, selection, and recipe consumption for Stage 2, but it is not the final executable layout system or a real-paper holdout result. Source pixels remain evidence only and are not reusable runtime assets.

## Revision 1 Evidence And Planner Escalation

REVIEW_1 correctly identified that the original 10-record gold index did not have per-record pixel-level mature-bar admission evidence, and that the statistics runtime probe used `force_gold_id` to bypass semantic compatibility for its alternate record.

Executor prepared a bounded gold-admission visual packet from existing inspected reference renders only:

```text
results/025_research_presentation_gold_scientific_composition_library/visual_review/gold_admission/visual_inputs.json
results/025_research_presentation_gold_scientific_composition_library/visual_review/gold_admission/review_identity_map.json
```

The packet included the 10 original gold candidates plus the three previously reported rejected examples, for 13 total reference-render inputs. No source corpus was expanded.

GitHub Actions executed one live `gpt-5.6-terra` review:

```text
run: https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/32708205168
evidence: results/025_research_presentation_gold_scientific_composition_library/visual_review/gold_admission/VISUAL_REVIEW.json
evidence_id: visual-review-025_research_presentation_gold_scientific_composition_library-1b0ba053dfa0
```

Item-level gold-admission decisions:

- `RRL-019`: `PASS`
- `RRL-013`: `PASS`
- `RRL-001`: `REVISE`
- `RRL-028`: `REVISE`
- `RRL-014`: `REVISE`
- `RRL-030`: `REVISE`
- `RRL-041`: `REVISE`
- `RRL-022`: `REVISE`
- `RRL-005`: `REVISE`
- `RRL-023`: `REVISE`
- `RRL-034`: `REVISE`
- `RRL-031`: `REVISE`
- `RRL-002`: `REVISE`

This creates a Planner-level conflict that Executor cannot resolve without changing the frozen Plan:

- Keeping the rejected records would violate REVIEW_1's instruction not to force low-maturity pages into gold for coverage.
- Reducing the gold set to the two newly admitted records would fail the frozen Stage 2 coverage and runtime-probe requirements, including the required statistics/biostatistics probe.
- Reusing old 021 evidence for `RRL-028` now conflicts with the newer, admission-specific 025 Terra evidence that directly judged the same page below the production gold bar.
- Expanding the corpus or running a new Source Scout is explicitly out of scope for 025.

Therefore this revision is routed to `NEEDS_GPT_PLANNER` rather than continuing with a fabricated PASS or an out-of-scope corpus expansion.

Minimal Planner question:

```text
Given the 025 gold-admission Terra evidence admits only RRL-019 and RRL-013 from the existing candidate packet, should 025 be revised to:
1. accept a smaller gold set and record Stage 2 coverage gaps for a follow-up acquisition task;
2. allow a targeted in-corpus re-screen beyond the original 13 packet;
3. authorize targeted new source scouting for missing statistics/result/negative/discussion mature gold pages; or
4. explicitly allow older 021 evidence to override the 025 admission-specific REVISE for RRL-028?
```

Executor did not modify the gold index, selector, recipe builder, tests, or workflow state beyond this routing escalation after the new evidence made the frozen repair impossible to complete safely.

## Revision 1 Bounded In-Corpus Recovery Implementation

Planner revised the frozen Plan to allow bounded in-corpus recovery without lowering the mature-pixel bar, expanding the source corpus, or using older evidence to override 025 admission-specific `REVISE` decisions.

Implementation commit:

```text
d6fafda2819d406c88a2f363a22bdfd9564989cf
```

The first admission packet remains authoritative for its 13 inputs:

```text
run: https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/32708205168
evidence_id: visual-review-025_research_presentation_gold_scientific_composition_library-1b0ba053dfa0
admitted: RRL-019, RRL-013
```

The revised Plan allowed one additional bounded packet from existing inspected/downloaded references only:

```text
run: https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/32714094088
evidence: results/025_research_presentation_gold_scientific_composition_library/visual_review/gold_recovery_1/VISUAL_REVIEW.json
evidence_id: visual-review-025_research_presentation_gold_scientific_composition_library-2fba9c5deb45
admitted: RRL-009, RRL-011, RRL-015, RRL-016, RRL-017, RRL-020, RRL-021
```

Final gold library:

```text
GSC-004 -> RRL-019
GSC-008 -> RRL-013
GSC-011 -> RRL-009
GSC-012 -> RRL-011
GSC-013 -> RRL-015
GSC-014 -> RRL-016
GSC-015 -> RRL-017
GSC-016 -> RRL-020
GSC-017 -> RRL-021
```

Every retained gold record now has item-level `PASS` evidence from the 025 gold-admission or bounded-recovery visual review packet, with `visual_review_item_id`, `visual_review_evidence_id`, `visual_review_path`, `identity_map_path`, and matching reviewer-input SHA. `RRL-028` and all other item-level `REVISE` pages remain ordinary inspected references and were not force-admitted.

Coverage limitation:

```text
No discussion / next-experiment page reached item-level PASS in the bounded existing-corpus screen.
```

Runtime probes were repaired to avoid fake compatible alternates:

```text
statistics_estimator_identity:
  baseline: GSC-014
  alternate: GSC-015

medical_aligned_prediction_error:
  baseline: GSC-008
  alternate: GSC-004
```

Both baseline and alternate records are selected by the normal semantic compatibility selector. The `force_gold_id` path now calls the same selector against the forced record and rejects incompatible requests with `forced gold composition is not compatible with query`; it no longer emits `score=999` or `forced compatible probe`.

The runtime artifact:

```text
docs/audits/research_presentation_gold_composition_library/runtime_probe_traces.json
```

records:

- `runtime_selected = true`
- `alternate_runtime_selected = true`
- `alternate_is_distinct = true`
- `alternate_has_compatibility_reasons = true`
- `actually_consumed = true`
- `output_affected = true`
- `primary_bbox_changed = true`
- `composition_family_available = true`

Validation executed successfully before handoff:

```text
python skills/tools/documents-media/presentations/shared/scripts/validate_gold_compositions.py
python skills/tools/documents-media/presentations/shared/scripts/generate_gold_composition_probe_artifacts.py
python -m unittest tests.test_presentations
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
PYTHONPATH=/home/yuukias/GPT_Codex_AI_Bridge_Kit python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
git diff --check
```

Observed results:

- gold validator: `validated 9 gold scientific composition records`
- runtime probes: `status = PASS`, `probe_count = 2`
- targeted Presentation tests: 25 tests passed
- full unittest discovery: 121 tests passed
- skills validation: 149 active skills, 18 profiles, templates, and trigger eval scaffolds passed
- marketplace validation/check/path report: passed
- Reviewed Handoff validation: passed
- whitespace check: passed

`python scripts/build_codex_marketplace.py --write --validate --check --path-report` was not rerun during this revision because the broader write command was not approved in the current executor environment. The source/plugin mirror files were mechanically synchronized for the changed schema/index/scripts, and the non-writing marketplace validation/check/path-report passed afterward.

Scope boundaries respected:

- no new source scout;
- no new downloads;
- no Stage 3 renderer/layout implementation;
- no 023 modification;
- no real statistical or medical-imaging holdout;
- no Terra core change;
- no `ONE_SHOT_QUALITY_PASS` or `PROGRAM_MATURE` declaration.
