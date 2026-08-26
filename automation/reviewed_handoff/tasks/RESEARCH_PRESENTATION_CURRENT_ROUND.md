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

## Stage 3 status — not passed

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

## Active bounded task — 029 visual contract consumer adaptation

当前 active task：

`029_reviewed_handoff_visual_contract_adaptation`

027/028 暴露出 AI_Skills_Collection consumer 尚未真正接入 Bridge Kit 已有 task-local Visual Review contract：当前 push workflow 在没有 repository-level manifest/output vars 时会静默 skip live review。为避免下一次 Stage 3 视觉返修再次创建显式 dispatch recovery，029 先做一个严格限定的控制面 consumer adaptation。

029 只允许：

- 让 push-mode GitHub Actions 从 tracked `CURRENT.visual_review_required`、task-local manifest/evidence path 自动发现唯一 pending visual task；
- 0 eligible task 正常 no-op；1 个 task 自动运行；多个或 identity 非法时 fail closed；
- 保留 explicit `workflow_dispatch` 作为人工恢复入口；
- 使用包含 task-local Reviewed Handoff visual contract 的稳定 Bridge Kit pin；
- 增加确定性 regression 和真实 CI。

029 不修改 Presentation 页面、Stage 2 gold、027/028 历史、Terra 核心、Reviewed Handoff state machine 或 review budget。

029 独立 PASS 后，Planner 立即创建新的 bounded Stage 3 visual-maturity recovery，只修 027 剩余四类 layout primitive，并真实启用 `visual_review_required` + task-local manifest/evidence path。该 recovery 必须使用新的 job-specific mechanism，而不是继续给旧 generic card/arrow primitive 填更多文字。

Stage 3 只有在新的 recovery 对所有主要内容页取得 fresh item-level mature-bar PASS 后才整体关闭；此前不得开始 Stage 4。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不要求用户在“继续保持质量”和“降低质量”之间重复选择。
- 每个 bounded task 仍最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。当前 consumer wiring 由 029 负责补齐，不新造状态机。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终双 deck 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须从正常 `research-presentations` production entrypoint 对两个未参与调优的真实公开 paper one-shot 生成完整 CUHK 组会 deck：statistics/biostatistics/methodology 一套、medical imaging 一套。真实 paper notation/data/figures/images 必须主导内容；不得 generic cards/box-arrow/default plot/AI 元语言；Terra 必须读 item/page-level judgement，Planner 必须独立审真实 source/trace/render；两套 deck 都通过后仍必须进入用户最终人工门。只有用户明确接受两套结果才允许 `ONE_SHOT_QUALITY_PASS`。
