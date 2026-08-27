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

031 是 Stage 4 的第一项 bounded integration，只证明正常 `research-presentations` production route 能把用户提供的 public-safe engineering research input 一次性连接到：

source ingestion / source-fidelity evidence map -> storyline/page jobs -> normal gold retrieval -> Stage 3 executable layouts -> canonical exact CUHK `.tex + PDF` -> real render -> task-local visual-review handoff。

关键边界：

- 必须走 normal user-facing production entry，不得把 027/030 benchmark generator 当产品入口；
- engineering regression input 只用于 Stage 4 集成证明，明确排除在 Stage 5 holdout 之外；
- production code 不得硬编码该 fixture 的 title、notation、page sequence、gold IDs 或 layout；
- 不允许 force-id / score override 绕过 Stage 2 compatibility；
- 必须保存 source -> plan -> gold -> layout -> output runtime trace；
- 必须真实使用 canonical exact CUHK source 并 compile/render；
- 必须启用 031 task-local Visual Review contract；
- 031 PASS 本身不自动等于 Stage 4 PASS。若 deck-rhythm review / bounded repair loop 尚未通过 normal production path 真实建立，Planner 将创建下一项有限 Stage 4 task，而不是降低合同。

当前 031 已 `PLAN_FROZEN`，下一步由现有 Reviewed Handoff watcher 交给 Codex Executor。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不要求用户在“继续保持质量”和“降低质量”之间重复选择。
- 每个 bounded task 仍最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- Stage 1–4 某 stage 首次独立 PASS 时发送一次旁路 notifier，但 notifier 不是 approval gate，不暂停后续 stage。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终双 deck 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须从正常 `research-presentations` production entrypoint 对两个未参与调优的真实公开 paper one-shot 生成完整 CUHK 组会 deck：statistics/biostatistics/methodology 一套、medical imaging 一套。真实 paper notation/data/figures/images 必须主导内容；不得 generic cards/box-arrow/default plot/AI 元语言；Terra 必须读 item/page-level judgement，Planner 必须独立审真实 source/trace/render；两套 deck 都通过后仍必须进入用户最终人工门。只有用户明确接受两套结果才允许 `ONE_SHOT_QUALITY_PASS`。
