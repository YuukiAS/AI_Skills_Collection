---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 038_research_presentation_two_real_paper_holdouts
executor: Codex
implementation_commit: be001f2d29a308a4cadeb9b841fcc9cfe239ea3b
status: WAITING_FOR_CI
ci_status: PENDING
---

# Result: 038 Research Presentation Two Real Paper Holdouts

Implementation commit: `be001f2d29a308a4cadeb9b841fcc9cfe239ea3b`

Control-plane commit: pending at time of writing this file.

## Outcome

The two real-paper holdouts were acquired, audited, staged into frozen source bundles, and generated through the normal `research-presentations` production entrypoint. Both decks rendered to exact-CUHK Beamer PDF/PNG artifacts and have task-local visual-review inputs.

No final quality PASS is claimed. Round-1 Terra returned `REVISE` with seven blocking findings. The only authorized action was the already shipped bounded quality loop, so I created deck-specific task-local adapters for the Terra findings and passed them to the normal production entrypoint using `--review-evidence`.

The existing quality-loop consumer failed closed for both decks: the Terra findings contain no supported `repair_intent`, so the current mapping cannot safely select a source-faithful automatic repair. Both decks are now recorded as `QUALITY_LOOP_FAIL_NO_WINNER`, with `repair_cycle_count=0`, no selected directives, no source-bundle rewrite, no generated-TeX edit, no production code change, and no manual repair.

Because `ci_required=true`, `CURRENT.ci_status` remains `PENDING` and the task is left in `WAITING_FOR_CI` for watcher/GitHub CI publication.

## Statistics Holdout

Paper: Paul-Christian Buerkner, "brms: An R Package for Bayesian Multilevel Models Using Stan", Journal of Statistical Software 80(1), 2017, DOI `10.18637/jss.v080.i01`.

Source and eligibility evidence:

- Published source: `https://www.jstatsoft.org/article/view/v080i01`
- Untracked local PDF cache: `/tmp/rh038_sources/brms_v080i01.pdf`
- PDF SHA256: `35757e85ffb002fcb6c5dc34fec0daa6a84302d552e7555f2551838c4599fffb`
- PDF pages: 28
- Eligibility audit: `results/038_research_presentation_two_real_paper_holdouts/holdout_eligibility.json`
- Source inventory: `results/038_research_presentation_two_real_paper_holdouts/statistics/source_inventory.json`

Frozen bundle and render evidence:

- Source notes: `results/038_research_presentation_two_real_paper_holdouts/statistics/source/source.md`
- Frozen bundle: `results/038_research_presentation_two_real_paper_holdouts/statistics/source_bundle.json`
- Bundle SHA256: `32d1a9d1241ff8b4c77b6a98fe5b20b5b88ed04f3d60b0b10f9897304f15421b`
- PDF: `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/cuhk_production_build/main.pdf`
- PDF SHA256: `8ff60c23d263fa15977fa96a4db8424707178fbc49597d72b84e5be36dac798a`
- Rendered pages: `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/cuhk_production_build/rendered/`
- Contact sheet: `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/deck_contact_sheet.png`
- Contact sheet SHA256: `722ccd6b2ba90fde592692e18a6478a850eaeb0f8fe9eb9a5d8fb7f5751bbf76`
- Render-input identity: `49faee5a773e73807b46b026b62c95cebdb9f5566de18dcc96e03fbfc02dacc7`
- Rendered-pixel identity: `43b45471bbdf47f02232bab4be023356b7e325b33b3524c78318c63c302260c8`
- Source-fidelity map: `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/source_fidelity_map.json`

Production behavior:

- Initial statistics invocation failed before render at selector compatibility, with no slide/render/Terra output generated or inspected. Evidence: `results/038_research_presentation_two_real_paper_holdouts/statistics/production_attempt_initial_failure.log`.
- Final frozen-bundle invocation exited 0 with `MECHANICAL_PASS` and `render_status=ok`.
- Bounded quality-loop review evidence: `results/038_research_presentation_two_real_paper_holdouts/visual_review/statistics_quality_loop_review.json`
- Quality loop consumed review evidence, selected no repair directives, applied 0 repairs, and failed closed with `unsupported repair intent: <missing>`.
- Quality-loop status: `QUALITY_LOOP_FAIL_NO_WINNER`

Preserved blocker evidence:

- `statistics/generated/cuhk_production_build/main.tex` contains an audience-facing annotation that says `Stage 4 clustered-calibration fixture`.
- Terra BF-01 through BF-04 remain preserved as holdout failure evidence. Per 038 evaluation-only rules, they were not repaired in-place or hidden by bundle/TeX edits.

## Medical Holdout

Paper: Jun Ma, Yuting He, Feifei Li, Lin Han, Chenyu You, and Bo Wang, "Segment anything in medical images", Nature Communications 15:654, 2024, DOI `10.1038/s41467-024-44824-z`.

Source and eligibility evidence:

- Published source: `https://www.nature.com/articles/s41467-024-44824-z`
- Untracked local PDF cache: `/tmp/rh038_sources/medsam_s41467-024-44824-z.pdf`
- PDF SHA256: `78925a99aaf7f17d728bc1e4e4c262fc234d33f4319d258d9f6b2080b42ded2b`
- PDF pages: 9
- Supplementary information SHA256: `b66b5d825586d4cb5fc6e92635656422733b82b64d7b1dcd3587a20c4090f1c3`
- Source data XLSX SHA256: `93f5e882d37e110bb747209bf18d24bae1874ff45dc5461a25c93820a40885a9`
- Eligibility audit: `results/038_research_presentation_two_real_paper_holdouts/holdout_eligibility.json`
- Source inventory: `results/038_research_presentation_two_real_paper_holdouts/medical/source_inventory.json`

Frozen bundle and render evidence:

- Source notes: `results/038_research_presentation_two_real_paper_holdouts/medical/source/source.md`
- Frozen bundle: `results/038_research_presentation_two_real_paper_holdouts/medical/source_bundle.json`
- Bundle SHA256: `fef82966184d4db938d4bfdd12101d289ebdca80bf246a3ed7c9fb72f42fa33b`
- Real MedSAM figure assets: `results/038_research_presentation_two_real_paper_holdouts/medical/assets/`
- PDF: `results/038_research_presentation_two_real_paper_holdouts/medical/generated/cuhk_production_build/main.pdf`
- PDF SHA256: `975d8bd725c4228c8881fa89524b762399277c0dd93c941adb6456af0a2b3409`
- Rendered pages: `results/038_research_presentation_two_real_paper_holdouts/medical/generated/cuhk_production_build/rendered/`
- Contact sheet: `results/038_research_presentation_two_real_paper_holdouts/medical/generated/deck_contact_sheet.png`
- Contact sheet SHA256: `5332d9f81e87882dc2df810e6eb5319049dc85631e8a1cfc0ef00ce451408ac4`
- Render-input identity: `dafce2787c90bb12f542b3124c1556bdbf5bfe959fb1506bab47e2da4a3f9116`
- Rendered-pixel identity: `21e4c10f254650e5bbc83b79295d0d219da82a03b7bef6d31637c307dd2e72bf`
- Source-fidelity map: `results/038_research_presentation_two_real_paper_holdouts/medical/generated/source_fidelity_map.json`

Production behavior:

- Normal medical invocation exited 0 with `MECHANICAL_PASS` and `render_status=ok`.
- Bounded quality-loop review evidence: `results/038_research_presentation_two_real_paper_holdouts/visual_review/medical_quality_loop_review.json`
- Quality loop consumed review evidence, selected no repair directives, applied 0 repairs, and failed closed with `unsupported repair intent: <missing>`.
- Quality-loop status: `QUALITY_LOOP_FAIL_NO_WINNER`
- The medical deck uses real article Figure 3 and Figure 4c medical-image segmentation pixels. No fabricated CT/MR/ultrasound/endoscopy pixels, masks, ROI, or overlays were introduced by hand.

Preserved blocker evidence:

- Terra BF-05 through BF-07 remain preserved as holdout failure evidence.
- The allowed quality loop could not safely repair architecture-footer overlap, limitation-slide collisions, or the overlay legend obstruction because no supported repair intent was provided.

## Combined Visual Review Handoff

Task-local visual manifest:

```text
results/038_research_presentation_two_real_paper_holdouts/visual_review/visual_inputs.json
```

It contains 12 visual inputs: five substantive statistics pages plus statistics contact sheet, and five substantive medical pages plus medical contact sheet. The manifest binds both source-bundle SHA values, build manifests, source-fidelity maps, render-input identities, rendered-pixel identities, PDF SHA values, contact-sheet SHA values, and the post-review quality-loop status for both decks.

Round-1 Terra evidence consumed by the bounded quality loop is preserved at:

```text
results/038_research_presentation_two_real_paper_holdouts/visual_review/VISUAL_REVIEW_1ce506ed08d5_REVIEW_1_USED.json
```

The active evidence path remains reserved for any future fresh evidence:

```text
results/038_research_presentation_two_real_paper_holdouts/visual_review/VISUAL_REVIEW.json
```

Fresh post-repair Terra is not requested from this Executor run because no repair was selected or applied; the existing shipped quality loop reached `QUALITY_LOOP_FAIL_NO_WINNER`.

## Local Acceptance and Regression Checks

Passed:

- `python -m json.tool results/038_research_presentation_two_real_paper_holdouts/statistics/source_bundle.json`
- `python -m json.tool results/038_research_presentation_two_real_paper_holdouts/medical/source_bundle.json`
- `python -m json.tool results/038_research_presentation_two_real_paper_holdouts/visual_review/statistics_quality_loop_review.json`
- `python -m json.tool results/038_research_presentation_two_real_paper_holdouts/visual_review/medical_quality_loop_review.json`
- `python -m json.tool results/038_research_presentation_two_real_paper_holdouts/production_invocations.json`
- `python -m json.tool results/038_research_presentation_two_real_paper_holdouts/visual_review/visual_inputs.json`
- selector compatibility check for all statistics and medical `page_jobs`
- `python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle results/038_research_presentation_two_real_paper_holdouts/statistics/source_bundle.json --out-dir results/038_research_presentation_two_real_paper_holdouts/statistics/generated --task-key 038_research_presentation_two_real_paper_holdouts --review-evidence results/038_research_presentation_two_real_paper_holdouts/visual_review/statistics_quality_loop_review.json`
- `python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle results/038_research_presentation_two_real_paper_holdouts/medical/source_bundle.json --out-dir results/038_research_presentation_two_real_paper_holdouts/medical/generated --task-key 038_research_presentation_two_real_paper_holdouts --review-evidence results/038_research_presentation_two_real_paper_holdouts/visual_review/medical_quality_loop_review.json`
- local mechanical/source-freeze assertion for both generated decks
- combined visual manifest consistency check
- `python -m unittest discover -s tests -p 'test_presentations.py' -k test_research_presentation_one_call_production_entry`
- `python -m unittest discover -s tests -p 'test_presentations.py' -k test_research_presentation_deck_quality_loop_consumes_review_and_fails_closed`
- `git diff --check`
- `ai-bridge reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection`

Known failures or non-PASS evidence:

- The direct production-entry validator is not holdout-aware and still contains 031 engineering-fixture assertions. It failed on the statistics deck for missing `MEDICAL_IMAGE_COMPARISON`, missing `Coverage by ICC under imbalanced clusters`, missing `Same-case ROI zoom`, and the already-known `fixture` / `workflow` leakage. It failed on the medical deck for missing `NEGATIVE_RESULT` and missing `Coverage by ICC under imbalanced clusters`.
- Round-1 Terra visual review remains `BLOCKED`; no quality PASS is claimed.
- The bounded quality loop consumed the review evidence and reached `QUALITY_LOOP_FAIL_NO_WINNER` for both decks due to missing supported `repair_intent`.
- GitHub CI has not run locally and is not claimed as PASS.
- Planner has not yet reviewed this fail-closed bounded-repair evidence.

## Out of Scope Preserved

No production files under `skills/`, `plugins/`, validators, selectors, layouts, gold/reference rules, tests, CI workflow semantics, shared quality-loop logic, `REQUEST.md`, `PLAN.md`, previous review artifacts, `FINAL_REPORT.md`, or Reviewed Handoff schemas/prompts/templates were modified. No branch, PR, push, provenance graph, receipt graph, or Agent-Flow artifact was created.
