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

Stage 4 已由 Planner 整体判定 PASS；该结论证明普通一次调用会真实串起 source fidelity、storyline、gold retrieval、canonical CUHK、compile/render、task-local visual handoff、deck contact sheet、双层 render identity 与单次 bounded quality-loop contract，但不替代真实 unseen paper 泛化验收。

Stage 4 历史链保持：031 建立 one-call production；032 关闭 multi-workstream coherence；033 建立 deck-level rhythm/quality loop；034 关闭 render identity 与 CI 证据语义；035 关闭 generic model support hardcode；036 关闭 process-page projection/source-grounding；037 关闭最后一个 audience-facing workstream transition 元语言 gap。此前达到 review limit 的 task 历史均保留，后续 recovery 只关闭未解决 blocker，没有事后改写旧 task 为 PASS。

## Stage 5 — active recovery after first real holdout failure

### 038 — first two real-paper holdouts — terminal REVIEW_LIMIT / REVISE

`038_research_presentation_two_real_paper_holdouts` 已完成第一次真正的双论文 unseen evaluation：

1. statistics/methodology：Bürkner (2017), **brms: An R Package for Bayesian Multilevel Models Using Stan**；
2. medical imaging：Ma et al. (2024), **Segment anything in medical images**。

两篇均在生成前完成 tracked-corpus/tuning exclusion audit 与许可/source audit；source bundle 在首次 render 前冻结；两个 deck 都从正常 production entry 独立生成 exact-CUHK PDF/PNG/contact sheet，并取得真实 task-local item-level Terra。

这次真实 Stage-5 测试没有通过质量门。Round-1 Terra 给出 7 个 blocking findings：statistics deck 包含 audience-facing internal fixture copy、workflow footer overlap、不可读 package table 与 closing diagram collision；medical deck 包含 architecture footer overlap、limitations/decision collision 与遮挡真实 CT crop 的 legend/connector。两个 contact sheet 均明确未达到 mature doctoral group-meeting / strong paper-talk bar。

Round-1 只授权冻结的单次 bounded quality loop。Executor 随后没有改 source bundle、production code 或 generated TeX，而是把 Terra finding 交给现有 consumer。两套 `quality_loop_state.json` 都真实记录：`repair_cycle_count=0`、`selected_repair_directives=[]`、`repair_allowed=false`、`QUALITY_LOOP_FAIL_NO_WINNER`，原因是 `unsupported repair intent: <missing>`。由于没有 repair，最终 pixels 与 Round-1 Terra identity 完全未变；Round-2 Planner 因而仍为 `REVISE`。真实 GitHub CI 已 PASS。

038 已依法用满两轮 review 并保留 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE` terminal history；没有第三轮。这里的 review-limit 不是需要用户选择降低质量的真实人工门，因为 Program Goal 的 Quality-Preserving Continuation Policy 已给出唯一 bounded recovery 路线。

**038 的两篇论文从现在起永久失去 Stage-5 unseen holdout 资格。** 后续不得在 brms/MedSAM 上修完再宣称 unseen PASS。

### 039 — active: Quality-loop execution recovery

当前 active task：

`039_research_presentation_quality_loop_execution_recovery`

039 只修 038 暴露的通用 quality-loop consumer/execution gap，不修 brms/MedSAM，不重新执行 Stage 5。当前已冻结的核心范围：

- 继续使用现有 task-local Visual Review contract、现有 `RESEARCH_PRESENTATION_DECK_QUALITY_LOOP_STATE_V1` 与单次 repair budget，不新建状态机；
- Terra finding 缺 `repair_intent` 时，仅利用结构化 requirement/target/page-job/content fields 对可唯一安全判断的 blocker 做有限 normalization；未知/歧义 finding继续 fail closed；
- 已有/新增 repair intent 只有在真正被 production layout/render consumer执行、前后 render-input/pixel identity发生预期变化时才算实现；
- 至少覆盖 audience-facing internal/meta copy、figure/caption/supporting-copy overlap、undersized table/primary object、process/next-step diagram collision、medical legend/callout obstruction；
- medical repair 只改 layout/legend/callout/crop framing，禁止生成或修改医学像素；source bundle SHA必须保持；
- regression/visual tuning 只能使用与 038 无关的 non-holdout stress bundle，不得把 brms/MedSAM title/DOI/figure/table/image/具体 wording 变成 fixture/gold/rule；
- fresh task-local Terra 必须对 repair 后 stress pages 与 contact sheet item-level PASS，并达到既有 mature bar；真实 CI、shared/plugin parity 与 unknown/no-winner regression 也必须 PASS。

039 已完成 PLAN preflight并冻结给 Codex Executor，review budget 从 0/2 开始。若 039 PASS，Planner 才选择新的 statistics/methodology 与 medical-imaging unseen public papers，另开下一次 Stage-5 evaluation；不会复用 038 两篇。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review/plan limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不让用户在“保持质量”与“降低质量”之间重复选择。
- 每个 bounded task 最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- 单 task PASS 不等于 Program PASS。
- Stage 1–4 首次整体 PASS 的旁路 notifier 不是 approval gate，不暂停下一 stage。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终双 deck 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须在 039 generic recovery 完成后，重新选择两个未参与 exemplar extraction / rule distillation / tuning 的真实公开 paper，从正常 `research-presentations` production entrypoint one-shot 生成完整 CUHK 组会 deck：statistics/biostatistics/methodology 一套、medical imaging 一套。真实 paper notation/data/figures/images 必须主导内容；不得 generic cards/box-arrow/default plot/AI 元语言；Terra 必须读 item/page-level judgement，Planner 必须独立审真实 source/trace/render。

新的两套 unseen deck 都通过 Terra + Planner 后，Stage 5 仍必须进入最终用户人工门。只有用户明确接受两套真实 rendered deck，才允许 `ONE_SHOT_QUALITY_PASS` 与 `PROGRAM_MATURE=true`。
