# Research Presentation Current Round

当前仍属于 `REFERENCE_CALIBRATED_ONE_SHOT_QUALITY`，长期 `PROGRAM_MATURE=false`。

**Source of truth：** `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Five-Stage Closure Roadmap、Quality-Preserving Continuation Policy 与 Final Quality Gates。

## Historical decision on 023

`023_research_presentation_deck_design_system_integration` 保持历史 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`，不伪造第三轮。其 low-level editable-PPTX design-profile renderer 不再是第一成熟 production route；当前 production contract 以 canonical exact CUHK Beamer `.tex + PDF` 为主。

## Completed stages

### Stage 1 — Product Contract Reset

`024_research_presentation_product_contract_reset` 已独立 PASS。普通科研组会 / paper talk / research update 未指定格式时，默认走 exact CUHK Beamer/source-editable TeX；显式 PowerPoint/PPTX/Slides 仍可覆盖。Exact CUHK identity 绑定 `skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/`，derived PPTX/scaffold 不得冒充 exact production source。

### Stage 2 — Gold Scientific Composition Library

`025_research_presentation_gold_scientific_composition_library` 保留历史 review-limit 终态；其唯一 coverage gap 由 `026_research_presentation_discussion_next_experiment_gold_recovery` 质量保持 recovery 关闭。026 第二轮独立 PASS，真实 CI 通过。

当前 production gold 已覆盖 roadmap 所需主要 scientific jobs。026 新增 `GSC-018`，来自真实 rendered-pixel item-level Terra `PASS` 的 discussion / next-experiment 页面；正常 selector 可选择它，recipe builder 实际消费 source-derived composition fields，移除后得到 no-compatible-result，因此 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` 已成立。Stage 2 整体关闭。

### Stage 3 — Executable CUHK Scientific Layout System

Stage 3 已首次整体 PASS。

`027_research_presentation_executable_cuhk_scientific_layout_system` 建立了核心工程链：normal Stage 2 selector -> gold recipe -> CUHK content-space resolver -> native LaTeX/TikZ/figure/image objects -> canonical exact CUHK compile/render，并证明 geometry mutation、`SPLIT_REQUIRED` capacity contract、native LaTeX model page、真实 xelatex/PDF/PNG/mechanical QA 与真实 CI。

027 第二轮达到 review limit 后保留历史 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`，没有伪造第三轮。028 独立关闭旧 visual dispatch gap；029 独立完成 task-local Visual Review consumer adaptation，使 push-mode resolver 可以按当前 task identity 自动发现唯一待审视觉任务。

质量保持 recovery `030_stage3_visual_recovery` 在第二轮独立审核中 PASS，真实 CI 与 task-local `gpt-5.6-terra` evidence 均绑定当前 implementation identity。六个主要内容页全部达到 item/page-level mature research-group-meeting / strong conference-talk bar：

- statistical model：native LaTeX 数学为主视觉；
- quantitative result：presentation-native axes/ticks/facets/method mapping/nominal line/callout 可投影阅读；
- experiment design：DGP factors、center/subject hierarchy、procedures 与 endpoints 通过 typed scientific relations 表达；
- negative result：coverage scale、target、uncertainty 与 failure conclusion 完整；
- medical comparison：same-case full panels + real ROI crop/zoom + adjacent TP/FP/FN legend；
- next experiment：normal `GSC-018` compatible path 形成 evidence -> manipulation/comparator -> endpoint -> go/no-go decision reasoning。

030 同时真实证明 CI PASS 后，029 的 task-local push resolver 可自动触发 GitHub Actions secret 路径并写回 fresh Visual Review evidence，不再需要人为 `workflow_dispatch` recovery。

Stage 3 PASS 只说明成熟受约束科研布局可以在 exact CUHK content area 中执行；它不等于普通用户的一次调用已经走完整生产链，也不等于最终真实 paper holdout 通过。

## Stage 4 — active

### Active bounded task — 031 One-Call Production Entry

当前 active task：

`031_research_presentation_one_call_production_entry`

031 第一轮独立审核已完成，结论为 `REVISE`。主体 one-call production integration 已得到正向 evidence：普通 `research-presentations` file/path 入口可以完成 source ingestion / source-fidelity map -> storyline/page jobs -> normal gold retrieval -> Stage 3 executable layouts -> canonical CUHK `.tex + PDF` -> real render -> task-local visual-review handoff；runtime trace 也证明没有 benchmark-helper orchestration、force-id 或 score override。

当前只保留两个冻结范围内的视觉 blocker：

1. source-side canonical CUHK provenance 成立，但 fresh rendered-pixel review 无法在六个 content pages 上识别出 canonical CUHK logo/identity；生成 build 的 canonical theme 本身声明每页 headline/logo，因此必须先解决 source contract 与实际 pixels 的不一致，而不是靠额外文字贴片伪造 identity；
2. medical comparison 使用 same-case Input / GT / Prediction / Error + ROI zoom，但当前 Prediction view 没有让 prediction mask 与 Error panel 的 TP/FP/FN 颜色在像素上无歧义对应，属于 image semantic inspectability blocker。

第一轮已接受并冻结保护：source-fidelity evidence map、正常 selector/recipe/layout consumption、canonical source copy/compile、real render/mechanical QA、anti-meta leakage、数学/结果图/实验设计/负结果/下一实验的 current page content，以及 031 明确不声称 Stage 4 PASS。

下一步只允许 Codex 做上述两个最小修复，随后重新生成当前 task 的 `.tex + PDF + PNG`、真实 CI 与 fresh task-local Visual Review evidence。031 PASS 后仍不自动等于 Stage 4 PASS；若 deck-level rhythm review / bounded repair loop 尚未通过 normal production path 建立，Planner 将创建下一项有限 Stage 4 task。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不要求用户在“继续保持质量”和“降低质量”之间重复选择。
- 每个 bounded task 仍最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- Stage 1–4 某 stage 首次独立 PASS 时发送一次旁路 notifier，但 notifier 不是 approval gate，不暂停后续 stage。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终双 deck 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须从正常 `research-presentations` production entrypoint 对两个未参与调优的真实公开 paper one-shot 生成完整 CUHK 组会 deck：statistics/biostatistics/methodology 一套、medical imaging 一套。真实 paper notation/data/figures/images 必须主导内容；不得 generic cards/box-arrow/default plot/AI 元语言；Terra 必须读 item/page-level judgement，Planner 必须独立审真实 source/trace/render；两套 deck 都通过后仍必须进入用户最终人工门。只有用户明确接受两套结果才允许 `ONE_SHOT_QUALITY_PASS`。
