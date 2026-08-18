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
| Inspected page library | 48 inspected page rows, 11 inspected decks, source/render hashes present | REVISE：随机核查发现至少 `RRL-020` 与公开原页语义不一致，且缺少明确 inspection date/means |
| Source tiers | `PRIMARY_RESEARCH_PRESENTATION`, `SECONDARY_TEACHING_REFERENCE`, `PRESENTATION_GUIDANCE`, `CANDIDATE_BACKLOG` | accepted for this round |
| Statistics/biostatistics sources | 30+ stats/biostats sources in manifest, 10 candidate backlog rows | sufficient for current round; no new scout needed |
| Visual reviewer | emits `MECHANICAL_VISUAL_REVIEW.json`, not scientific PASS | split accepted; academic visual decision remains NOT_ASSESSED |
| Four-slide regression | PPTX generated; LibreOffice PDF render produced 4 PNGs; reviewer says `MECHANICAL_PASS` | REVISE：reference ids are still hard-coded rather than retrieved with trace; external visual review still pending |
| Remote review | implementation commit `846e3d96c2037e3efc1bb9e325f61ea8097ae32d` reviewed on remote main | Planner review written in `results/011_round_handoff/PLANNER_REVIEW.md` |

## Round History

- `2026-08-18`: Installed Lite Handoff templates without `.agents` writes; Reviewed Handoff validates after schema migration.
- `2026-08-18`: Rebuilt research presentation reference metadata from explicit inspected page specs instead of metadata-derived page rows.
- `2026-08-18`: Generated four regression PNGs through the real PPTX → LibreOffice → PDF → PNG chain; mechanical reviewer correctly stopped at `NOT_ASSESSED` for academic visual judgment.
- `2026-08-18`: External Planner independently reviewed the round and returned `REVISE` because inspected-page fidelity is not yet clean and the regression generator still uses hard-coded `RRL-*` lists instead of semantic retrieval with a trace.

## Current State

`REVISE`

Canonical review: `results/011_round_handoff/PLANNER_REVIEW.md`.

Next action: Codex Executor performs only the two bounded repairs in that review, then regenerates the regression evidence for another independent Planner pass. Do not expand source count or claim program maturity.
