---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 027_research_presentation_executable_cuhk_scientific_layout_system
final_decision: REVISE
---

# 027 Final Report — Executable CUHK Scientific Layout System

## What 027 achieved

027 已经建立了 Stage 3 的核心执行链：真实科研 page job 会通过正常 Stage 2 gold selector 与 recipe，进入 CUHK content-space resolver，再生成 native LaTeX/TikZ/figure/image-panel 对象，最终使用 canonical exact CUHK Beamer source 编译成真实 PDF/PNG。source-derived geometry 会影响实际 emitted geometry，容量不匹配时会返回 `SPLIT_REQUIRED`，而不是退回 generic fallback。

这意味着 Stage 3 已经不再是“选完参考页后重新手写一套布局”的假集成。exact CUHK 身份、gold-to-layout trace、native LaTeX 数学、真实 xelatex 编译、PDF-to-PNG 渲染、机械检查、audience-meta leak gate 与真实 CI 都已经成立。

## What improved after Review 1

第一轮返修后，统计模型页继续保持成熟；negative-result 页已经从真实文本重叠的失败状态修到 item-level `PASS`。实验设计、医学影像和下一实验页也加入了更具体的科研对象，说明上一轮 blocker 并非完全没有改善。

## Why 027 still cannot pass

返修后的 fresh Terra evidence 来自真实 `workflow_dispatch`，并与当前六张 PNG identity 一致。六个主要内容页里，slide 2 与 slide 5 为 `PASS`，但 slide 3、4、6、7 仍为 `REVISE`：

- 结果图内部字号与 legend 仍不够投影可读；
- 实验设计仍以通用卡片/箭头组织具体内容，而不是科学关系图；
- 医学影像页虽然放大 panel，但真正 error ROI 没有形成真实 image zoom；
- next-experiment 虽有具体术语和判定指标，仍然是卡片化 workflow，而不是 evidence-to-decision 研究推理视觉。

这些都是冻结 Stage 3 质量合同的核心要求，因此不能用 CI PASS、机械 QA 或 top-level Terra 状态替代。

## Review-limit handling

027 已经使用两轮独立审核，因此按 Reviewed Handoff 不允许第三轮。当前不需要用户决定是否降低标准：Program Goal 已明确要求优先保持最高冻结质量门槛。剩余四个 blocker 已被真实像素证据明确定位，并且存在新的、范围清楚的实现机制，所以应保留 027 的 `REVIEW_LIMIT / REVISE` 历史，并创建新的 bounded Stage 3 recovery task，只处理这四类未成熟 layout primitive。

## Preserved capabilities

后续 recovery 不应重做或回归：canonical CUHK identity、normal gold selector/recipe 路径、geometry-transfer regression、`SPLIT_REQUIRED` capacity contract、native LaTeX model page、已通过的 negative-result layout、audience-meta leak gate、现有 Stage 2 gold library与 027 的真实 CI/build evidence。

## User-checkable artifacts

- `results/027_research_presentation_executable_cuhk_scientific_layout_system/REVIEW_1.md`
- `results/027_research_presentation_executable_cuhk_scientific_layout_system/REVIEW_2.md`
- `results/027_research_presentation_executable_cuhk_scientific_layout_system/RESULT.md`
- `results/027_research_presentation_executable_cuhk_scientific_layout_system/visual_review/VISUAL_REVIEW.json`
- `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/`

Stage 3 目前仍未整体 PASS，Stage 4 不能启动。
