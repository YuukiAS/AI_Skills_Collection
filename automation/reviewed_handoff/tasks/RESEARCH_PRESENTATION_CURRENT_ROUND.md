# Research Presentation Current Round

## Current Round

本轮是 `research_presentation_corpus_round_001`。范围固定为：

- `001_reference_integrity_cleanup`
- `002_source_tiering`
- `003_existing_cache_page_inspection`
- `004_statistics_primary_acquisition`
- `005_visual_reviewer_split`
- `006_four_slide_regression`
- `007_round_handoff`

## Coverage Matrix

| Area | Current evidence | State |
| --- | --- | --- |
| Fake page records | `metadata page-function record` count is 0；metadata rotation synthesis 已移除 | implementation direction accepted, record integrity needs repair |
| Inspected page library | 48 inspected page rows, 11 inspected decks, source/render hashes present, `inspection_date` / `inspection_means` present | READY_FOR_EXTERNAL_PLANNER_REVIEW：`RRL-020` corrected to `SRC-006` actual page 17 `Overall objective function` |
| Source tiers | `PRIMARY_RESEARCH_PRESENTATION`, `SECONDARY_TEACHING_REFERENCE`, `PRESENTATION_GUIDANCE`, `CANDIDATE_BACKLOG` | accepted for this round |
| Statistics/biostatistics sources | 30+ stats/biostats sources in manifest, 10 candidate backlog rows | sufficient for current round; no new scout needed |
| Visual reviewer | emits `MECHANICAL_VISUAL_REVIEW.json`, not scientific PASS | split accepted; academic visual decision remains NOT_ASSESSED |
| Four-slide regression | PPTX generated; LibreOffice PDF render produced 4 PNGs; reviewer says `MECHANICAL_PASS`; manifest now includes retrieval query/candidates/selected ids/reasons | ready for academic visual judgment, but mechanical review alone is not scientific PASS |
| Legacy visual transport | `011_round_handoff` GitHub Pages PDF + external Planner screenshot route reached `BLOCKED_EXTERNAL_VISUAL_ACCESS` in `results/011_round_handoff/PLANNER_REVIEW.md` | historical / provenance only; do not retroactively rewrite the old BLOCKED result |
| Current primary visual transport | `012_presentation_visual_adapter`: real PPTX render PNGs -> mechanical visual review -> Bridge Kit OpenAI Visual Review -> tracked `VISUAL_REVIEW.json` | `VISUAL_TRANSPORT_PASS`; current canonical visual evidence is `results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json` |
| Remote review | previous implementation commit `846e3d96c2037e3efc1bb9e325f61ea8097ae32d` reviewed on remote main; Executor revision commit `2c54c52f287be94c5919bc5886fb52804f94fc49` prepared; Pages transport commit `38d7bbc137fb8bbaa13d830bbfb1907be32066c6` deployed; Bridge Kit adapter commit `6c1039680768e5440eef1dd3e2dce26bef34f287` and evidence commit `81cabe4d451e1f29f542168cac7c3a446d0567df` are now tracked | waiting for external Presentation Corpus Planner to consume structured visual evidence, not to open the Pages PDF |

## Round History

- `2026-08-18`: Installed Lite Handoff templates without `.agents` writes; Reviewed Handoff validates after schema migration.
- `2026-08-18`: Rebuilt research presentation reference metadata from explicit inspected page specs instead of metadata-derived page rows.
- `2026-08-18`: Generated four regression PNGs through the real PPTX → LibreOffice → PDF → PNG chain; mechanical reviewer correctly stopped at `NOT_ASSESSED` for academic visual judgment.
- `2026-08-18`: External Planner independently reviewed the round and returned `REVISE` because inspected-page fidelity is not yet clean and the regression generator still uses hard-coded `RRL-*` lists instead of semantic retrieval with a trace.
- `2026-08-18`: Executor corrected `SRC-006/RRL-020`, added inspection evidence fields, implemented semantic inspected-page retrieval with trace, regenerated four golden PNGs, and passed local validation.
- `2026-08-18`: Executor added GitHub Pages transport for the same synthetic true-render PDF. Public URL validation returned HTTP 200, `Content-Type: application/pdf`, page count 4, and SHA-256 `ebb0cec2e4009a784989c4166a8dc335d8705b1c41f9ce6c3cba72644e888f0b`.
- `2026-08-21`: Bridge Kit Visual Review adapter `012_presentation_visual_adapter` was added at commit `6c1039680768e5440eef1dd3e2dce26bef34f287`, pinned to Bridge Kit commit `e915d04756490fafbd111eaa445295f0103b2c94`, and reused the existing four true-render PNGs without changing the old `011_round_handoff` history.
- `2026-08-21`: GitHub Actions run `32463908616` executed the Bridge Kit OpenAI Visual Review workflow with model `gpt-4.1-mini`; evidence commit `81cabe4d451e1f29f542168cac7c3a446d0567df` wrote tracked `results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json` with `overall_decision=PASS`, `blocking_findings=[]`, and four image SHA bindings matching `visual_inputs.json`.
- `2026-08-21`: The `81cabe4d451e1f29f542168cac7c3a446d0567df` evidence-only commit did not trigger another AI Bridge Visual Review run because `.github/workflows/ai-bridge-visual-review.yml` ignores `results/**/visual_review/**`. The workflow exposes only the secret name `OPENAI_VISUAL_REVIEW_API_KEY`; no API key value is tracked in repository files.

## Current State

`READY_FOR_EXTERNAL_PLANNER_REVIEW`

Legacy review: `results/011_round_handoff/PLANNER_REVIEW.md`.

Legacy immutable external visual review PDF:

`https://yuukias.github.io/AI_Skills_Collection/presentation-review/ff8ff1ddb48cb9c511b3e3fecc7f0c4964adab46/research_group_meeting_regression.pdf`

This Pages PDF route is retained as historical provenance and debugging / archival transport only. It is no longer the primary machine-consumption path for academic visual review.

Current canonical visual evidence:

`results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json`

Current evidence route:

```text
real PPTX render PNGs
-> mechanical visual review
-> Bridge Kit OpenAI Visual Review
-> tracked VISUAL_REVIEW.json
-> Scheduled Presentation Planner consumes structured visual evidence
```

The current Bridge Kit visual evidence records `overall_decision=PASS`, model `gpt-4.1-mini`, workflow run `32463908616`, adapter commit `6c1039680768e5440eef1dd3e2dce26bef34f287`, evidence commit `81cabe4d451e1f29f542168cac7c3a446d0567df`, Bridge Kit commit `e915d04756490fafbd111eaa445295f0103b2c94`, and four input image SHA bindings. This is a visual evidence producer result, not the final Presentation Corpus Planner decision.

Next action: External Presentation Corpus Planner reads the current tracked `VISUAL_REVIEW.json`, corresponding `visual_inputs.json`, mechanical evidence, and current program contract, then makes the final Planner judgment for this round's academic visual gate. Do not expand source count, bump release, claim Planner PASS, claim program maturity, or ask Planner to reopen the old Pages PDF screenshot route as the primary path.
