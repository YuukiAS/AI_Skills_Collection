---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 024_research_presentation_product_contract_reset
implementation_commit: 01886bd84841a388f034f504ca8e3b640f267796
---

# 024 Research Presentation Product Contract Reset — Result

## Summary

Stage 1 product-contract reset is implemented. The default unspecified research presentation route now points to exact CUHK Beamer / source-editable `.tex` plus rendered PDF, using `skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/` as the canonical source.

Explicit PowerPoint, `.pptx`, editable, Slides, Google Slides, or later manual editing requests still route to editable Presentation/Slides. Explicit Beamer / LaTeX / `.tex` / academic PDF requests still route to the LaTeX route. Business, teaching, operations, marketing, and executive defaults were not changed.

## What changed

- Updated `research-presentations/SKILL.md` to remove the old no-format research default to editable Presentation/Slides and replace it with the exact CUHK Beamer/PDF default.
- Updated `shared/template-routing.md` and `shared/ppt-skill-routing.md` so shared routing documents match the Program Goal and preserve explicit PPTX/Slides overrides.
- Changed `shared/scripts/markdown_to_deck_plan.py` so the normal research adapter default is `output="tex"` with `editability="source-editable"`.
- Updated the expected deck-plan fixture to the new default route.
- Updated presentation tests to cover the new default, explicit PPTX override, explicit TeX behavior, exact CUHK canonical-source wording, and source/generated mirror consistency.
- Updated the presentations marketplace source config and regenerated the generated Codex plugin mirror.

## Scope boundaries

This task did not modify or recover `023_research_presentation_deck_design_system_integration`. It did not add new scientific layouts/macros, expand the reference corpus, change 019-022 mechanisms, run holdouts, modify Terra or Bridge Kit reviewer semantics, or declare `ONE_SHOT_QUALITY_PASS`.

## Compatibility note

Reviewed Handoff validation initially rejected the 024 Planner artifact because `PLAN.md` used `## Acceptance gates` while the current validator requires `## Acceptance and regression gates`. Commit `87d3fd4` made a heading-only, semantics-preserving compatibility repair before the implementation commit.

## Validation

Commands run:

```bash
python -m unittest tests.test_presentations
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python scripts/build_codex_marketplace.py --validate --check --path-report
PYTHONPATH=/home/yuukias/GPT_Codex_AI_Bridge_Kit python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
git diff --check
```

Results:

- `tests.test_presentations`: PASS, 24 tests.
- Full unittest discovery: PASS, 120 tests.
- `scripts/skills.py validate`: PASS, 149 active skills, 18 profiles, templates, and trigger eval scaffolds.
- Marketplace write/validate/check/path-report: PASS, 10 plugins, 25 active skills, 63 source snapshots, no path-budget overages.
- Marketplace validate/check/path-report after generation: PASS.
- Reviewed Handoff validation: PASS, 24 tasks.
- `git diff --check`: PASS.

`python scripts/build_codex_marketplace.py --write --validate --check --path-report` required non-sandbox execution because the Codex sandbox mounts `.agents/` read-only; the command completed successfully and wrote only the repository marketplace/generated layer.

## Handoff

Implementation commit: `01886bd84841a388f034f504ca8e3b640f267796`.

Because `ci_required=true`, `CURRENT.ci_status` remains `PENDING` and the task is handed off as `WAITING_FOR_CI`. Scheduled Planner should wait for real CI before review.
