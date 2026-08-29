---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 038_research_presentation_two_real_paper_holdouts
executor: Codex
implementation_commit: 1e376b51d703f42324f111b06b6bf4e2d062b8e6
status: WAITING_FOR_CI
ci_status: PENDING
---

# Result: 038 Research Presentation Two Real Paper Holdouts

Implementation commit: `1e376b51d703f42324f111b06b6bf4e2d062b8e6`

Control-plane commit: pending at time of writing this file.

## Outcome

The two real-paper holdouts were acquired, audited, staged into frozen source bundles, and generated through the normal `research-presentations` production entrypoint. Both decks rendered to exact-CUHK Beamer PDF/PNG artifacts and have task-local visual-review inputs.

No final quality PASS is claimed. Local visual QA found blocking/risk evidence after the one-shot render, so no post-render bundle rewrite, generated-TeX edit, production code change, or manual repair was applied.

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
- PDF SHA256: `7b592c2bd35621880fbec9b5a5a42fa15b622917e5ba00cbc0b74e90918f1d91`
- Rendered pages: `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/cuhk_production_build/rendered/`
- Contact sheet: `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/deck_contact_sheet.png`
- Contact sheet SHA256: `722ccd6b2ba90fde592692e18a6478a850eaeb0f8fe9eb9a5d8fb7f5751bbf76`
- Render-input identity: `49faee5a773e73807b46b026b62c95cebdb9f5566de18dcc96e03fbfc02dacc7`
- Rendered-pixel identity: `43b45471bbdf47f02232bab4be023356b7e325b33b3524c78318c63c302260c8`
- Source-fidelity map: `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/source_fidelity_map.json`

Production behavior:

- Initial statistics invocation failed before render at selector compatibility, with no slide/render/Terra output generated or inspected. Evidence: `results/038_research_presentation_two_real_paper_holdouts/statistics/production_attempt_initial_failure.log`.
- Final frozen-bundle invocation exited 0 with `MECHANICAL_PASS` and `render_status=ok`.
- Quality loop consumed no review evidence and applied 0 repairs.

Local visual QA blocker:

- `statistics/generated/cuhk_production_build/main.tex` contains an audience-facing annotation that says `Stage 4 clustered-calibration fixture`.
- This was found after rendered output inspection. Per 038 evaluation-only rules, it was not repaired in-place or hidden by bundle/TeX edits.

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
- PDF SHA256: `45d854a8e1d870902c7ea93ca2cb4031a9fc5625f8d527dd21064be2d13fa36f`
- Rendered pages: `results/038_research_presentation_two_real_paper_holdouts/medical/generated/cuhk_production_build/rendered/`
- Contact sheet: `results/038_research_presentation_two_real_paper_holdouts/medical/generated/deck_contact_sheet.png`
- Contact sheet SHA256: `5332d9f81e87882dc2df810e6eb5319049dc85631e8a1cfc0ef00ce451408ac4`
- Render-input identity: `dafce2787c90bb12f542b3124c1556bdbf5bfe959fb1506bab47e2da4a3f9116`
- Rendered-pixel identity: `21e4c10f254650e5bbc83b79295d0d219da82a03b7bef6d31637c307dd2e72bf`
- Source-fidelity map: `results/038_research_presentation_two_real_paper_holdouts/medical/generated/source_fidelity_map.json`

Production behavior:

- Normal medical invocation exited 0 with `MECHANICAL_PASS` and `render_status=ok`.
- Quality loop consumed no review evidence and applied 0 repairs.
- The medical deck uses real article Figure 3 and Figure 4c medical-image segmentation pixels. No fabricated CT/MR/ultrasound/endoscopy pixels, masks, ROI, or overlays were introduced by hand.

Local visual QA risks:

- The limitation/take-home slide appears dense.
- The CT same-case comparison page has crowded ROI labels.
- These were not repaired after render; see `results/038_research_presentation_two_real_paper_holdouts/local_visual_qa.json`.

## Combined Visual Review Handoff

Task-local visual manifest:

```text
results/038_research_presentation_two_real_paper_holdouts/visual_review/visual_inputs.json
```

It contains 12 visual inputs: five substantive statistics pages plus statistics contact sheet, and five substantive medical pages plus medical contact sheet. The manifest binds both source-bundle SHA values, build manifests, source-fidelity maps, render-input identities, rendered-pixel identities, PDF SHA values, and contact-sheet SHA values.

Expected Terra evidence path remains:

```text
results/038_research_presentation_two_real_paper_holdouts/visual_review/VISUAL_REVIEW.json
```

No `VISUAL_REVIEW.json` exists yet in this local implementation commit.

## Local Acceptance and Regression Checks

Passed:

- `python -m json.tool results/038_research_presentation_two_real_paper_holdouts/statistics/source_bundle.json`
- `python -m json.tool results/038_research_presentation_two_real_paper_holdouts/medical/source_bundle.json`
- selector compatibility check for all statistics and medical `page_jobs`
- `python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle results/038_research_presentation_two_real_paper_holdouts/statistics/source_bundle.json --out-dir results/038_research_presentation_two_real_paper_holdouts/statistics/generated --task-key 038_research_presentation_two_real_paper_holdouts`
- `python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle results/038_research_presentation_two_real_paper_holdouts/medical/source_bundle.json --out-dir results/038_research_presentation_two_real_paper_holdouts/medical/generated --task-key 038_research_presentation_two_real_paper_holdouts`
- local mechanical/source-freeze assertion for both generated decks
- combined visual manifest consistency check
- `python -m unittest discover -s tests -p 'test_presentations.py' -k test_research_presentation_one_call_production_entry`
- `git diff --check`
- `ai-bridge reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection`

Known failures or non-PASS evidence:

- The direct module-form unittest command `python -m unittest tests.test_presentations.PresentationSharedTests.test_research_presentation_one_call_production_entry` failed because `tests` is not importable as a package in this environment; the same test passed through `unittest discover`.
- Local visual QA found a blocking audience-facing internal text leak in the statistics deck and additional visual density risks. No quality PASS is claimed.
- GitHub CI has not run locally and is not claimed as PASS.
- Terra has not yet produced task-local `VISUAL_REVIEW.json`.
- Planner has not yet reviewed this one-shot evidence.

## Out of Scope Preserved

No production files under `skills/`, `plugins/`, validators, selectors, layouts, gold/reference rules, tests, CI workflow semantics, shared quality-loop logic, `REQUEST.md`, `PLAN.md`, previous review artifacts, `FINAL_REPORT.md`, or Reviewed Handoff schemas/prompts/templates were modified. No branch, PR, push, provenance graph, receipt graph, or Agent-Flow artifact was created.
