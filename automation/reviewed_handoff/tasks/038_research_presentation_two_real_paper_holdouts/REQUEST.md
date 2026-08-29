---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 038_research_presentation_two_real_paper_holdouts
---

# Reviewed Handoff Request — 038_research_presentation_two_real_paper_holdouts

## Objective

执行 Program Goal 的 Stage 5 最终真实 holdout 验证：在不再修改 production 规则、布局、gold、storyline 或质量循环的前提下，用两个此前未参与 exemplar extraction / rule distillation / tuning 的真实公开论文，分别从正常 `research-presentations` production entrypoint 生成完整 exact-CUHK 组会 deck，并取得真实 render、逐页 Terra、deck-contact-sheet Terra 与 Planner 独立审核。

Stage 4 已由 Planner 首次整体判定 PASS。037 已关闭最后一个 audience-facing multi-workstream transition 缺口；因此 038 不再是开发/调参任务，而是最终的 unseen-paper evaluation。任何针对这两篇 holdout 看到结果后再修改 production code、gold、layout rule、selector、validator、prompt、repair mapping 或 source bundle，都将污染 holdout，不能继续把同一篇论文计作最终 one-shot 证据。

## Frozen holdout papers

### Statistics / methodology holdout

- Paul-Christian Bürkner, **“brms: An R Package for Bayesian Multilevel Models Using Stan”**, *Journal of Statistical Software*, 2017, 80(1), 1–28.
- DOI: `10.18637/jss.v080.i01`.
- Published source: `https://www.jstatsoft.org/article/view/v080i01`.
- JSS applies a Creative Commons Attribution license to its articles, so source figures/tables may be reused with attribution under the journal license.
- Planner repository search before freezing 038 found no match for the title / DOI / Bürkner identity in `YuukiAS/AI_Skills_Collection`; Executor must still re-check the presentation reference/gold manifests and any tracked corpus metadata before acquiring the paper. Any prior use in exemplar extraction, gold selection lessons, rule distillation or tuning disqualifies this paper before generation.

### Medical-imaging holdout

- Jun Ma, Yuting He, Feifei Li, Lin Han, Chenyu You, Bo Wang, **“Segment anything in medical images”**, *Nature Communications*, 2024, 15:654.
- DOI: `10.1038/s41467-024-44824-z`.
- Published source: `https://www.nature.com/articles/s41467-024-44824-z`.
- The article is Open Access under Creative Commons Attribution 4.0; article images are included in that license unless a figure-specific credit states otherwise. Reused figures/images must retain appropriate attribution and any figure-specific exception must be respected.
- Planner repository search before freezing 038 found no match for the title / DOI / `MedSAM` identity in `YuukiAS/AI_Skills_Collection`; Executor must still re-check tracked reference/gold/corpus metadata before acquisition. Any prior tuning use disqualifies this paper before generation.

These choices are frozen for the first Stage 5 attempt. Do not substitute a different paper merely because one is harder for the current production system. A paper may be replaced only if pre-generation exclusion/licensing/source-access checks prove it is not an eligible holdout; that is a control/evidence issue and must be returned to Planner before any deck generation.

## User-provided inputs

- `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`, especially Stage 5, Final Quality Gates and Quality-Preserving Continuation Policy.
- Stage 1–4 terminal history, including 030, 032, 036 and 037 PASS evidence and the review-limit histories that were closed by bounded recoveries.
- Current normal production contract in `skills/tools/documents-media/presentations/research-presentations/SKILL.md`.
- Normal entrypoint: `skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle <bundle.json> --out-dir <output-dir>`.
- Existing exact CUHK Beamer template, gold library, source-fidelity map, dual render identity, contact-sheet/deck-rhythm review and one-repair quality-loop behavior.
- Existing Bridge Kit task-local Visual Review contract.

## User constraints

- 038 is evaluation-only. Do not modify production files under `skills/`, `plugins/`, production validators/selectors/layouts, gold/reference rules, tests, CI workflow semantics or shared quality-loop logic in response to either holdout.
- Before the first production generation, acquire/read the complete published paper and relevant supplement/source-data material needed for correct interpretation. Record source URLs, DOI, license, local file hashes, page/figure inventory and citation/attribution information.
- Build each paper’s file/path-oriented input bundle once from real paper anchors. The bundle must contain real paper notation, claims, methods, results, limitations, figures/tables/images and source mappings appropriate to the paper. Freeze and hash the bundle **before** the first generated slide is inspected. Do not hand-tune the bundle after seeing render or Terra output.
- Invoke the normal production entrypoint, not benchmark helpers, fixture generators, task-specific layout scripts or copied Stage 4 engineering bundles. The two decks must be generated independently from their own frozen source bundles.
- A normal built-in quality-loop repair is allowed only if it is the already-shipped Stage 4 production behavior: at most one structured, source-faithful repair cycle from task-local reviewer evidence. No manual slide editing, bespoke TeX patch, paper-specific code branch, extra repair cycle or source-bundle rewrite is allowed.
- Both outputs must be complete research/paper-talk decks, not six benchmark archetype pages. Page count is source-driven, but the deck must cover the paper’s motivation/question, method/mechanism, central evidence/results, uncertainty/limitations and take-home interpretation; omit a section only when the paper itself does not support it.
- The statistics deck must be dominated by the brms paper’s actual model notation, Bayesian/multilevel objects, examples/results/tables/figures and stated limitations. Do not replace its scientific content with the Stage 4 clustered-calibration fixture, generic ICC examples or placeholder equations.
- The medical-imaging deck must use real MedSAM paper figures / medical images from the licensed article (or its licensed source-data assets when directly tied to the paper), including at least one genuine qualitative medical-image segmentation comparison. Do not fabricate CT/MR/ultrasound/endoscopy pixels, masks, ROI or error overlays.
- Reused third-party material must preserve attribution and license/source notes suitable for a scientific talk. Do not commit the full third-party PDF merely for convenience unless the license and repository policy clearly permit redistribution; hashes and source URLs are sufficient for source provenance when raw paper files can remain task-local/untracked.
- Exact CUHK identity, source fidelity, scientific object prominence, projection readability, page variety, deck rhythm, no generic-card substitution, no audience-facing workflow/QA/provenance language and no fabricated claims remain non-negotiable.
- Fresh task-local Terra must review every substantive page of both decks and one contact sheet per deck. Top-level PASS is insufficient; item/page-level decisions, observations and comparative mature-talk judgement are required.
- If either holdout exposes a real product blocker, preserve the failed one-shot evidence. Do not fix production code against that paper and then claim the same paper is still unseen. Planner must route a non-holdout bounded recovery; after the generic fix, final acceptance requires a **new** previously unseen replacement paper for the affected domain.
- Even if both decks receive Terra + Planner PASS, Stage 5 must end at final `AWAIT_HUMAN_DECISION`. Only explicit user acceptance of both real rendered decks may set `ONE_SHOT_QUALITY_PASS` / `PROGRAM_MATURE=true`.
