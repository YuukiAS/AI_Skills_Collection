# Reviewed Handoff Request — 005_research_presentation_corpus_integrity

## Objective

修复 `v4.4.1` research presentation hardening 中两类会污染长期 corpus/QA 的问题：伪 page-level reference metadata，以及没有实际看 rendered PNG 就自动给出的 academic visual PASS。完成后建立第一轮可信的三层参考库边界和可供独立 GPT/人工视觉审阅的真实 regression evidence。

## Current evidence

- `skills/tools/documents-media/presentations/shared/references/build_reference_metadata.py` 当前通过 `PAGE_FUNCTIONS` 轮转和 source metadata 自动生成 72 条 `research_slide_reference_index.csv` 记录，并把 `page_number` 写成 `metadata page-function record N`。
- `tests/fixtures/presentations/research_group_meeting/review_research_group_meeting_regression.py` 当前只确认 PNG 数量与 manifest 中 `expected_scientific_objects` 非空，然后把十项视觉 criteria 全部写成 `PASS`；它没有读取/分析 PNG 像素内容，却被 `v4.4.1` release acceptance 作为 independent scientific visual PASS。
- 最新长期合同：`automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`。

## User constraints

- Planner/Reviewer 只审查和路由，不替 Executor 下载来源或生成 page records。
- 不按数量凑 corpus；真实检查一页才允许增加一条 inspected page record。
- 不降低 `PPTX -> presentation engine -> PDF -> PNG` 真实渲染门槛。
- 本 round 的 PASS 不代表 program mature，也不要求新的大版本发布。
