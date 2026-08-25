---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 027_research_presentation_executable_cuhk_scientific_layout_system
executor: Codex
implementation_commit: 7dadb5e027013253c23025a847bae5d3e3039bd7
status: WAITING_FOR_CI
---

# 027 Executable CUHK Scientific Layout System - Revision Result

## Implementation Commit

`7dadb5e027013253c23025a847bae5d3e3039bd7`

## Repair Summary

This revision addresses REVIEW_1's five visual-maturity blockers without redesigning the frozen Plan or changing Stage 2 gold admission.

- Quantitative result pages now allocate a larger projection-scale result figure region, apply bounded figure trim, and add native readable red/teal method binding beside the plot.
- Experiment-design pages now emit a scientific-factor diagram with centers `G=8,20,50`, ICC levels, cluster balance, generated units, interval procedures, and coverage/width/bias endpoints, instead of the previous generic four-box sequence.
- Negative-result pages now split the evidence figure from the diagnostic explanation/caption column; emitted audience text regions are validated as non-overlapping.
- Medical-image pages now use a full-width same-case image band with larger Input / GT / Prediction / Error panels and an explicit same-case error zoom/callout relation.
- Discussion / next-experiment pages still consume `GSC-018`, but now show current limit, batch-query strategy variation, CR2/wild-bootstrap comparator setup, and an explicit coverage/width decision criterion.

The accepted statistical-model page was kept structurally stable except for regenerated render identity.

## Updated Evidence

Regenerated Stage 3 artifacts are under:

```text
docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/
```

Current generated evidence records:

- real canonical CUHK source copy and file hashes;
- six resolved page-job layouts with selected gold IDs `GSC-016`, `GSC-014`, `GSC-004`, `GSC-012`, `GSC-008`, and `GSC-018`;
- mutation regression status `PASS` for source `primary_bbox` affecting resolved/emitted geometry;
- capacity failure contract status `SPLIT_REQUIRED` with no generic fallback;
- real `xelatex` compile status `COMPILED`;
- real PDF-to-PNG render status `ok`, `png_count=7`;
- mechanical QA status `MECHANICAL_PASS`;
- updated task-local visual input manifest at `results/027_research_presentation_executable_cuhk_scientific_layout_system/visual_review/visual_inputs.json`.

The new visual input manifest has new rendered PNG SHA values. The existing `VISUAL_REVIEW.json` belongs to the pre-repair identity `6e2e6dab29b0688cc0fde5fe6d68925c5043339fc07df522edb966dc11a44ca1` and is stale for the repaired pixels. Because this Codex run must not push, the new task-local Terra review cannot be truthfully triggered against the repaired commit from GitHub yet; watcher/GitHub Actions must publish and review the new manifest through the repository-secret path.

## Validation Performed

Passed locally:

```text
python skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py --write-result-visual-inputs
python skills/tools/documents-media/presentations/shared/scripts/validate_cuhk_scientific_layout_stage3.py --out-dir docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated
python -m unittest tests.test_presentations.PresentationSharedTests.test_cuhk_scientific_layout_stage3_contract
python -m unittest tests.test_presentations
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
PYTHONPATH=/home/yuukias/GPT_Codex_AI_Bridge_Kit python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
git diff --check
pdftotext docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/cuhk_stage3_build/main.pdf - | rg -n "RRL-|SRC-|GSC-|Reference retrieval|EVIDENCE_MANIFEST|Diagram contract|QA|repo path|run ID|implementation commit|review target|fixture|workflow"
```

Observed results:

- strict Stage 3 rendered contract validation: PASS;
- 027 targeted test: PASS, 1 test;
- Presentation targeted tests: PASS, 26 tests;
- full unittest discovery: PASS, 122 tests;
- `scripts/skills.py validate`: PASS, 149 active skills, 18 profiles, templates, and trigger eval scaffolds;
- marketplace validate/check/path-report: PASS, 10 plugins, 25 active skills, 63 source snapshots, no path-budget overages;
- Reviewed Handoff validation: PASS, 27 tasks;
- `git diff --check`: PASS;
- PDF audience-text leak grep: no matches.

`python scripts/build_codex_marketplace.py --write --validate --check --path-report` could not be completed in this Codex process: sandbox execution hit read-only `.agents/plugins/marketplace.json`, and the sandbox-external retry was rejected by the active safety policy because it would write marketplace outputs outside the task-owned repair. The read-only marketplace validation/check passed after the source/plugin mirror was synchronized.

## Current Routing

This is not a 027 PASS claim and not a Stage 4 entry. Because `ci_required=true`, `CURRENT.ci_status` is `PENDING` and the task is handed off as `WAITING_FOR_CI`. GitHub CI and new task-local Terra item/page-level review must be established through the watcher/GitHub path before Scheduled GPT Reviewer adjudication.
