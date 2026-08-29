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

## Stage 5 — frozen 4-paper batch acceptance

### 038 — first two real-paper holdouts — terminal REVIEW_LIMIT / REVISE

`038_research_presentation_two_real_paper_holdouts` 是第一次真正的双论文 unseen evaluation：

1. statistics/methodology：Bürkner (2017), **brms: An R Package for Bayesian Multilevel Models Using Stan**；
2. medical imaging：Ma et al. (2024), **Segment anything in medical images**。

两篇都在首次 render 前完成 tracked-corpus/tuning exclusion audit、source/license audit 与 source-bundle freeze，并通过正常 production entry 生成真实 exact-CUHK deck。真实 Terra 暴露 7 个阻断视觉问题；允许的单次 quality loop 随后因为真实 review finding 不含 consumer 期望的 `repair_intent` 而没有选择任何 repair，也没有改变 pixels。Round 2 仍失败。

038 保持两轮 review limit 的真实失败历史；没有第三轮，也没有降低质量门。**brms 与 MedSAM 永久失去 unseen holdout 资格**，不得修漂亮后重新宣称 one-shot PASS。

### 039 — generic quality-loop execution recovery — PASS

`039_research_presentation_quality_loop_execution_recovery` 已在第二轮 Planner 独立审核 PASS。该 task 使用与 038 无关的 non-holdout stress bundle，关闭了 038 暴露的通用 consumer/execution gap：

- structured visual finding 即使没有内部 `repair_intent`，也能在 requirement/target/page-job 语义唯一且安全时映射到现有 bounded repair vocabulary；未知/歧义 finding 继续 fail closed；
- audience meta copy、caption/support collision、undersized primary object、process-diagram collision 与 medical legend/callout obstruction 的安全 repair 都有真实下游 layout consumer；
- stress run 实际使用且只使用一次 repair cycle，前后 render-input 与 rendered-pixel identity 均真实变化；source fidelity、CUHK identity 和 medical source pixels 受保护；
- Review 1 唯一剩余的 stress-title 工程语言泄漏由窄范围 revision 关闭；没有借机修改 normal production rules 或使用 brms/MedSAM 调参；
- 真实 GitHub CI PASS；fresh task-local Terra 与最终 implementation/render identities 绑定，六个主要内容页与整套 contact sheet 全部 item-level PASS，无 blocking finding。

039 PASS 只证明 generic recovery，**不构成 Stage 5 holdout PASS**。

### 040 — superseded before execution

`040_research_presentation_replacement_two_real_paper_holdouts` was frozen under the old two-paper replacement protocol, but it was stopped before Executor acquisition/render and superseded by the user-authorized frozen-batch generalization protocol.

The old 040 two-paper replacement protocol is now rejected as insufficient generalization evidence because it could permit adaptive holdout replacement: fail a real paper, repair the system, choose another paper, and repeat until a pair happens to pass. 040 must not execute and must not close the Program.

Because 040 did not execute, its proposed TMB and cardiac-ultrasound papers were not consumed by 040. Their exact titles/DOIs only occur in 040 Planner artifacts in the current tracked-repository contamination audit; `implementation_commit=null` and the 040 terminal report records no acquisition, source-bundle freeze, render, Terra or production invocation.

### 041 — active frozen four-paper generalization batch — PLAN_FROZEN

Current active task:

`041_research_presentation_frozen_four_paper_generalization_batch`

Planner has frozen the complete Stage 5 batch before any 041 source acquisition/render/evaluation:

1. statistics / computational methodology: Kristensen et al. (2016), **TMB: Automatic Differentiation and Laplace Approximation**, DOI `10.18637/jss.v070.i05`;
2. biostatistics / methodology: Love, Huber & Anders (2014), **Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2**, DOI `10.1186/s13059-014-0550-8`;
3. medical imaging: Ferreira et al. (2025), **Self-supervised learning for label-free segmentation in cardiac ultrasound**, DOI `10.1038/s41467-025-59451-5`;
4. medical imaging: Zhou et al. (2023), **A foundation model for generalizable disease detection from retinal images**, DOI `10.1038/s41586-023-06555-x`.

Fresh tracked-repository audit before freeze found DESeq2/RETFound title/DOI/common identifiers absent; TMB/cardiac-ultrasound only appear in superseded 040 Planner artifacts and were never executed. Public-source license preflight is compatible with rights-safe evaluation: JSS articles are Creative Commons Attribution; DESeq2, cardiac-ultrasound and RETFound are CC BY 4.0, with per-figure third-party credit checks still required during acquisition.

041 freezes presentation production behavior at commit `d3379b5168bc27b114b362f186f8c239a88a669c`; later task-local control/source/evidence artifacts may be added, but normal production code, gold, layouts, prompts/routing, validators, quality-loop mapping and canonical CUHK template may not change during the batch. Executor must mechanically recheck four-paper contamination and production freeze **before acquiring any of the four papers**, then acquire/read all four and freeze all four source bundles/hashes before the first render of any deck.

Four decks must run through the normal production entry under one frozen system. Each deck may use at most the already-shipped single bounded automatic repair. Any one paper failing makes the entire 4-paper batch FAIL and consumes all four; there is no within-batch replacement/chasing. If the batch fails, generic recovery may only use independent non-holdout material, and any next fresh batch requires a user human gate first.

041 is now `PLAN_FROZEN` for Codex Executor. Stage 5 remains open and `PROGRAM_MATURE=false`.

## Standing workflow decisions

- 始终保持最高冻结质量标准；review/plan limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不让用户在“保持质量”与“降低质量”之间重复选择。
- 每个 bounded task 最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- 单 task PASS 不等于 Program PASS。
- Stage 1–4 首次整体 PASS 的旁路 notifier 不是 approval gate，不暂停下一 stage。
- 对高成本 final holdout acceptance，failed batch + generic recovery 后，消耗下一批 fresh holdout 前必须打断用户。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终 4-deck batch 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须由完整 frozen batch 中的四篇 unseen paper 各自产生一套完整真实 CUHK 组会 deck；paper notation/data/figures/images 必须主导内容，不能用 synthetic/fixture/CI/mechanical PASS 替代。Terra 必须读 item/page-level evidence，Planner 必须独立审核真实 source/trace/render。

只有一个完整 frozen 4-paper batch 的四套 deck 全部通过 Terra + Planner，Stage 5 才能进入最终用户人工门，并把四套真实 rendered deck/artifact 提供给用户检查。只有用户明确接受四套结果，才允许 `ONE_SHOT_QUALITY_PASS`、`PROGRAM_MATURE=true` 与停止 Planner automation。
