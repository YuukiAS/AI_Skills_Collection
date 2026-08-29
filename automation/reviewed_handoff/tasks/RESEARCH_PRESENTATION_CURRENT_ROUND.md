# Research Presentation Current Round

当前仍属于 `REFERENCE_CALIBRATED_ONE_SHOT_QUALITY`，长期 `PROGRAM_MATURE=false`。

**Source of truth：** `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Five-Stage Closure Roadmap、Quality-Preserving Continuation Policy 与 Final Quality Gates。本文只记录当前阶段状态与已经冻结的历史结论，不维护第二套 roadmap。

## Historical decision on 023

`023_research_presentation_deck_design_system_integration` 保持历史 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`，不伪造第三轮。其 low-level editable-PPTX design-profile renderer 不再是第一成熟 production route；当前 production contract 以 canonical exact CUHK Beamer `.tex + PDF` 为主。

## Completed stages

### Stage 1 — Product Contract Reset — PASS

`024_research_presentation_product_contract_reset` 已独立 PASS。普通科研组会 / paper talk / research update 未指定格式时，默认走 exact CUHK Beamer/source-editable TeX；显式 PowerPoint/PPTX/Slides 仍可覆盖。Exact CUHK identity 绑定 canonical CUHK Beamer source，derived PPTX/scaffold 不得冒充 exact production source。

### Stage 2 — Gold Scientific Composition Library — PASS

`025_research_presentation_gold_scientific_composition_library` 保留 review-limit 历史，其唯一 coverage gap 由 `026_research_presentation_discussion_next_experiment_gold_recovery` 关闭。026 第二轮独立 PASS。当前 production gold 已覆盖 roadmap 所需主要 scientific jobs，并建立 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` 的真实选择/消费证据。

### Stage 3 — Executable CUHK Scientific Layout System — PASS

`027_research_presentation_executable_cuhk_scientific_layout_system` 建立核心工程链并保留 review-limit 历史；028 关闭旧 visual dispatch gap；029 完成 task-local Visual Review consumer adaptation；`030_stage3_visual_recovery` 第二轮独立 PASS。六个主要内容页已证明成熟 scientific composition 可在 exact CUHK content area 中执行为统计模型、定量结果、实验设计、负结果、医学影像比较与下一实验布局，并达到 item/page-level mature research-group-meeting / strong conference-talk bar。

### Stage 4 — One-Call Production + Bounded Quality Loop — PASS

Stage 4 已由 Planner 首次整体判定 PASS。该结论关闭的是普通一次调用的 production 工程闭环，不等于最终 Program PASS，也不替代 Stage 5 的两个真实未见论文。

Stage 4 的历史链保持如下：

- `031_research_presentation_one_call_production_entry` 建立 normal file/path input -> source-fidelity map -> storyline/page jobs -> normal gold retrieval -> executable layouts -> canonical CUHK `.tex + PDF` -> real render -> task-local visual handoff；因 multi-workstream storyline coherence 在两轮后保留 review-limit 历史。
- `032_research_presentation_storyline_coherence_recovery` PASS：把 storyline/grouping 改成通用 source/workstream metadata 驱动，加入 unrelated dual-workstream 与 single-workstream regression。
- `033_research_presentation_deck_rhythm_quality_loop` 建立完整 deck contact sheet / sequence review、一次 automatic repair 上限、unsafe/unknown fail-closed/no-winner；因 no-render evidence identity 语义缺口保留 review-limit 历史。
- `034_research_presentation_render_identity_ci_recovery` 建立 render-input identity 与真实 rendered-pixel identity 双层证据，关闭标题页工程元语言和模型页欠填充；因 model supporting copy 的 fixture-specific source-grounding 缺口保留 review-limit 历史。
- `035_research_presentation_generic_model_support_recovery` 关闭共享模型页的 clustered-calibration hardcode，并用 unrelated Cox regression 证明通用性；因 fresh Terra 暴露 process-page projection dips 保留 review-limit 历史。
- `036_research_presentation_process_page_projection_recovery` PASS：关闭实验设计页/下一实验页的投影尺度与 source-grounding 问题，unrelated acquisition/measurement-noise regression 通过，fresh Terra 对 slides 2–7 与 deck contact sheet 全部 item-level PASS。
- `037_research_presentation_audience_transition_copy_recovery` 第一轮独立 PASS：关闭 Stage 4 最后一个 audience-facing gap。最终医学影像页不再显示 `Workstream transition`、`independent workstream`、`no causal bridge asserted` 等内部控制说明，而是显示由当前 workstream metadata 提供的自然科研主题/范围；内部仍保留“不虚构跨方向因果关系”的 storyline constraint。unrelated dual-workstream 与 single-workstream regression 均证明实现不是当前 segmentation fixture special case。

037 的真实 GitHub `Codex Marketplace` CI 已通过。fresh task-local Terra 与 implementation `dc1ab6f...`、render-input identity `8ad96cd...`、rendered-pixel identity `e763bd...` 和 contact-sheet SHA `7f3159...` 绑定；六个主要内容页及 `deck_contact_sheet` 全部 item-level `PASS`。医学页明确通过 same-case Input/GT/Prediction/Error、ROI、TP/FP/FN 语义及独立研究方向切换；contact sheet 明确通过完整 sequence、结果→失败→下一实验节奏、页面构图变化与成熟博士组会标准。

Planner 同时独立检查 production diff、当前 `main.tex` 与 source bundle，未发现新的 Stage 4 blocker。因此 Stage 4 在 037 PASS 后正式整体关闭。

## Stage 5 — active: Two Real Paper Holdouts + Human Closure

当前 active task：

`038_research_presentation_two_real_paper_holdouts`

038 已完成 Planner 预检并冻结 Plan。它是 evaluation-only，不允许再用 holdout 调 production code/rules/gold/layout/prompt。首次 Stage 5 固定两篇真实公开论文：

1. statistics / methodology：Paul-Christian Bürkner (2017), **brms: An R Package for Bayesian Multilevel Models Using Stan**, DOI `10.18637/jss.v080.i01`，Journal of Statistical Software；JSS 文章采用 CC BY。
2. medical imaging：Jun Ma et al. (2024), **Segment anything in medical images**, DOI `10.1038/s41467-024-44824-z`，Nature Communications；文章采用 CC BY 4.0，并包含真实多模态医学影像与 segmentation figures。

Planner 在冻结 038 前对仓库 tracked content 做 title/DOI/author/product-name 搜索，未发现两篇论文被使用的记录；Executor 仍必须在首次 acquisition 前检查 reference/gold/corpus/tuning manifests。若任一 paper 在生成前被证明曾参与 exemplar extraction/rule distillation/tuning，则必须停止并交回 Planner，不得私自换成更容易的 paper。

038 的核心冻结规则：

- 完整读取 published paper 与必要 supplement/source data；
- 每篇先构建真实 paper source bundle，并在第一次 render 前冻结 bundle SHA；看到 slides/Terra 后不得改 bundle 再称 one-shot；
- 两篇分别调用正常 `generate_research_presentation_production_entry.py --input-bundle ... --out-dir ...`，禁止 benchmark/fixture/task-specific bypass；
- 只允许已经 shipped 的一次 bounded automatic repair，不允许手工 TeX/slide patch、paper-specific production branch 或第二次 repair；
- 两套都必须是完整 paper-talk/group-meeting deck，不是少数 benchmark pages；真实 paper notation/data/figures/images/claims 必须主导；
- medical deck 必须真实使用 MedSAM 文章许可覆盖的医学图像/segmentation evidence，不得 fabricated medical pixels；
- 最终 task-local Terra 必须逐页审两套 deck，并分别审两个 contact sheet；top-level package PASS 不够；
- 若真实 holdout暴露 product blocker，保留失败 one-shot evidence，同一 paper 永久失去“未见 holdout”资格；generic repair 必须另开非-holdout bounded task，之后换新的 unseen paper；
- 即使两套 deck 均被 Terra + Planner 判定 PASS，也只能进入最终用户人工门。只有用户明确接受两套真实 rendered deck 后才允许 `ONE_SHOT_QUALITY_PASS` / `PROGRAM_MATURE=true`。

038 当前为 `PLAN_FROZEN`，等待 Codex Executor 执行。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review/plan limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不用用户在“保持质量”与“降低质量”之间重复选择。
- 每个 bounded task 最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- 单 task PASS 不等于 Program PASS。
- Stage 1–4 首次整体 PASS 的旁路 notifier 不是 approval gate，不暂停下一 stage。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终双 deck 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须从正常 `research-presentations` production entrypoint 对两个未参与调优的真实公开 paper one-shot 生成完整 CUHK 组会 deck：statistics/biostatistics/methodology 一套、medical imaging 一套。真实 paper notation/data/figures/images 必须主导内容；不得 generic cards/box-arrow/default plot/AI 元语言；Terra 必须读 item/page-level judgement，Planner 必须独立审真实 source/trace/render；两套 deck 都通过后仍必须进入用户最终人工门。只有用户明确接受两套结果才允许 `ONE_SHOT_QUALITY_PASS`。
