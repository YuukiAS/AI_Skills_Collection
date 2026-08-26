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

## Stage 3 status — active recovery, not yet passed

### 027 historical result

`027_research_presentation_executable_cuhk_scientific_layout_system` 已建立 Stage 3 核心工程链：normal Stage 2 selector -> gold recipe -> CUHK content-space resolver -> native LaTeX/TikZ/figure/image objects -> canonical exact CUHK compile/render。geometry mutation、`SPLIT_REQUIRED` capacity contract、native LaTeX model page、negative-result layout、audience-meta leak gate、真实 xelatex/PDF/PNG/mechanical QA 与真实 CI 均已成立。

第一轮 Review 为 `REVISE`。返修后通过 028 恢复的 fresh `gpt-5.6-terra` evidence 显示：

- slide 2 statistical model：PASS；
- slide 5 negative result：PASS；
- slide 3 quantitative result：REVISE，图内字号/legend 仍不具备投影尺度可读性；
- slide 4 experiment design：REVISE，仍以 generic card/arrow primitive 承载具体实验语义；
- slide 6 medical comparison：REVISE，没有真实可检查的 error image crop/zoom；
- slide 7 next experiment：REVISE，仍是卡片化 workflow，而不是 evidence-to-decision 研究推理视觉。

027 第二轮已正式 `REVISE` 并达到 review limit。027 保留 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE` 历史，不得伪造 REVIEW_3，也不得把真实 CI/机械 PASS 当 Stage 3 PASS。

### 028 control-plane recovery

`028_research_presentation_stage3_visual_review_dispatch_recovery` 已独立 PASS。真实 workflow_dispatch run `32923111244` 成功生成并写回与返修后六张 PNG identity 一致的新 Terra evidence。028 只关闭 visual-review dispatch gap，不替代 027 REVIEW_2，也不代表 Stage 3 PASS。

### 029 visual contract consumer adaptation — completed

`029_reviewed_handoff_visual_contract_adaptation` 已在第一轮独立审核中 PASS。真实 `Codex Marketplace` CI 与 `AI Bridge Visual Review` push run 均成功；push-mode resolver 已真实执行 0-task no-op，确定性回归覆盖 1-task、fresh evidence、invalid identity 与 multiple eligible fail-closed 行为。普通 push 不再依赖 repository-level 固定 manifest/output vars，显式 `workflow_dispatch` 仍保留。

029 只关闭 consumer control-plane seam，不构成 Stage 3 PASS，也不发送 stage notifier。

### Active bounded task — 030 Stage 3 visual-maturity recovery

当前 active task：

`030_stage3_visual_recovery`

030 是 027 review limit 后的质量保持业务 recovery，只处理四类已被 fresh Terra 明确定位的 layout blocker：

- quantitative result：建立 presentation-native result-figure path，直接控制 axes/tick/facet/legend/reference line/callout 的投影可读性，不再只扩大不可读 raster；
- experiment design：建立 typed scientific hierarchy / relation primitive，让 center-subject 层级、DGP 因素、procedure branches 与 endpoints 由结构本身表达，不再使用 generic card/arrow；
- medical comparison：建立真实 same-case ROI crop/zoom image primitive、callout 与邻近 TP/FP/FN legend；
- next experiment：建立 evidence -> manipulation/comparator -> endpoint -> decision criterion 的科研推理布局，并继续通过正常 discussion-compatible gold path。

027 已通过的 exact CUHK、Stage 2 selector/recipe、geometry transfer、`SPLIT_REQUIRED`、statistical-model page、negative-result page 与 anti-meta gate 必须保持。

030 已真实启用 task-local Visual Review contract：

- `visual_review_required=true`；
- manifest: `results/030_stage3_visual_recovery/visual_review/visual_inputs.json`；
- evidence: `results/030_stage3_visual_recovery/visual_review/VISUAL_REVIEW.json`。

真实 CI 通过并进入视觉证据阶段后，029 已验证的 push resolver 应自动发现唯一 030 target，由 GitHub Actions secret 路径运行 Terra 并写回 evidence；缺 evidence 只等待，不消耗 review round，不再创建手工 dispatch recovery。

Stage 3 只有在 030 对六个主要内容页取得与当前 identity 一致的 fresh item/page-level mature-bar PASS、Planner 独立审核通过后才整体关闭。届时发送一次 Stage 3 PASS notifier，并自动创建 Stage 4；此前不得开始 Stage 4。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不要求用户在“继续保持质量”和“降低质量”之间重复选择。
- 每个 bounded task 仍最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终双 deck 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须从正常 `research-presentations` production entrypoint 对两个未参与调优的真实公开 paper one-shot 生成完整 CUHK 组会 deck：statistics/biostatistics/methodology 一套、medical imaging 一套。真实 paper notation/data/figures/images 必须主导内容；不得 generic cards/box-arrow/default plot/AI 元语言；Terra 必须读 item/page-level judgement，Planner 必须独立审真实 source/trace/render；两套 deck 都通过后仍必须进入用户最终人工门。只有用户明确接受两套结果才允许 `ONE_SHOT_QUALITY_PASS`。
