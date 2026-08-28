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

质量保持 recovery `030_stage3_visual_recovery` 在第二轮独立审核中 PASS，真实 CI 与 task-local `gpt-5.6-terra` evidence 均绑定当前 implementation identity。六个主要内容页全部达到 item/page-level mature research-group-meeting / strong conference-talk bar：statistical model、quantitative result、experiment design、negative result、medical comparison、next experiment。

Stage 3 PASS 只说明成熟受约束科研布局可以在 exact CUHK content area 中执行；它不等于普通用户的一次调用已经走完整生产链，也不等于最终真实 paper holdout 通过。

## Stage 4 — active

### 031 One-Call Production Entry — review limit history

`031_research_presentation_one_call_production_entry` 已完成两轮独立审核并合法停在 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`；不得创建 `REVIEW_3` 或改写成 PASS。

031 已真实建立并通过以下 production integration 能力：普通 `research-presentations` file/path entry 可以完成 source ingestion / source-fidelity map -> storyline/page jobs -> normal gold retrieval -> Stage 3 executable layouts -> canonical CUHK `.tex + PDF` -> real render -> task-local visual-review handoff；runtime trace 没有 benchmark-helper orchestration、force-id 或 score override。

第一轮两个视觉 blocker 在 repair implementation `11509b5e2bf7959433f1616c1d4ad77f77f4000e` 中已关闭：

- canonical CUHK crest / purple navigation identity 已在六张真实 content-page pixels 中可见；
- medical comparison 的 GT / Prediction / Error full panels 与 ROI zoom 已使用同病例、同 ROI 的可检查 TP/FP/FN semantic overlays。

真实 repair CI 已通过；fresh task-local Terra 对五页给出 item-level PASS，医学页内部 image semantics 也通过。

031 第二轮唯一剩余 blocker 是 deck-level storyline coherence：当前 engineering bundle 包含 clustered interval-calibration 与 synthetic segmentation-robustness 两个独立 workstream，但 normal production ordering 将 medical page 插在 coverage failure 与其 next experiment 之间，且没有足够强的 workstream transition。source 不支持把两者虚构为同一因果故事，因此必须通过 production storyline grouping 修复，而不是修改页面科学内容。

### Active bounded recovery — 032 Storyline Coherence Recovery

当前 active task：

`032_research_presentation_storyline_coherence_recovery`

032 是 Program Goal Quality-Preserving Continuation Policy 下的自动 bounded recovery，只关闭 031 的 storyline blocker，不降低 deck coherence bar，也不重做 031 已通过部分。

冻结机制：

- normal production path 增加 source-derived workstream grouping / ordering / transition contract；
- 不 hardcode 当前 fixture 的页号、标题或 `GSC-*` ID；
- 同一 workstream 的科研依赖链保持连续；
- 对 source 没有科学关系的 workstream 不虚构因果桥；
- 当前 regression 中 coverage 的 `Model -> Results -> Design -> Negative -> Next Experiment` 连续，segmentation comparison 作为清楚标识的第二 workstream；
- workstream 切换必须有强于现有顶部 miniframe 的 audience-facing transition cue；
- 保留 normal one-call entry、source fidelity、gold/recipe/layout consumption、exact CUHK identity、medical semantics 与 anti-meta leakage；
- 重新生成真实 `.tex + PDF + PNG`、真实 CI 与 032 task-local fresh Visual Review evidence。

032 PASS 只表示 031 的 production-storyline gap 被关闭。完整 Stage 4 仍需后续独立 bounded task 建立 deck-level rhythm review 与 bounded quality-repair loop；不得因为 032 PASS 提前进入 Stage 5。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不要求用户在“继续保持质量”和“降低质量”之间重复选择。
- 每个 bounded task 仍最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- Stage 1–4 某 stage 首次独立 PASS 时发送一次旁路 notifier，但 notifier 不是 approval gate，不暂停后续 stage。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终双 deck 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须从正常 `research-presentations` production entrypoint 对两个未参与调优的真实公开 paper one-shot 生成完整 CUHK 组会 deck：statistics/biostatistics/methodology 一套、medical imaging 一套。真实 paper notation/data/figures/images 必须主导内容；不得 generic cards/box-arrow/default plot/AI 元语言；Terra 必须读 item/page-level judgement，Planner 必须独立审真实 source/trace/render；两套 deck 都通过后仍必须进入用户最终人工门。只有用户明确接受两套结果才允许 `ONE_SHOT_QUALITY_PASS`。
