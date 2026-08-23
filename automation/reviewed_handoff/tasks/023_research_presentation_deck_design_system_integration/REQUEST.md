---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 023_research_presentation_deck_design_system_integration
---

# 023 Research Presentation Deck-Wide Design-System Integration — Request

## Why this task exists

022 已经证明 candidate layer 不再只能生成“可读但明显低于成熟 reference bar”的单页：统计公式页已有 generated candidate 达到 mature research-group-meeting / strong conference-talk 水平，医学影像页也有两个 generated candidates 达到成熟组会水平。

但这仍然只是单页证据。长期目标要求一次调用生成完整 PPTX / Beamer；如果每一页都独立检索 reference、独立生成 candidate、独立选择视觉处理，却没有 deck-wide design system，完整 deck 仍可能出现字体、颜色、间距、caption、annotation、chart/diagram/image/equation treatment 漂移，或者相反地为了“统一”退化成每页同一模板。

因此 023 要建立 **candidate / exemplar -> locked deck design system -> multi-page generation integration**：把前序已经验证的 reference retrieval、composition transfer、candidate search 和 visual-finish primitives 接入一个完整多页 deck 的生成流程，使 deck 在统一视觉语言下仍按 page function 使用不同 composition。

## User-facing product goal

用户未来给出新的科研材料时，不应逐页指定字体、颜色、layout 或视觉风格。系统应在内部完成 anchor-page 设计探索，锁定一套适合当前研究内容的 design system，然后把它稳定应用到整套 deck，同时保持公式页、结果页、医学影像页、实验设计页等各自的科学表达方式。

## Scope constraint

023 只实现和验证 deck-wide design-system locking / generation integration：

- 复用 019 composition representation、020 candidate search、021 comparative review semantics 与 022 visual-finish primitives；
- 建立 renderer-neutral deck design profile / tokens，并明确哪些属性 deck-wide 锁定、哪些属性由 page function / composition 决定；
- 用受控的多页科研 fixture 验证同一 design system 可跨不同 page functions 生成完整 editable PPTX；
- 页面 composition 必须继续来自 matched inspected exemplars / composition records，而不是统一模板；
- 不把旧 10 页 synthetic review pack 当 gold reference；
- 不开始最终 real statistical / medical holdout；
- 不把 contact-sheet / deck-rhythm 独立质量 gate 在本任务中提前宣告完成；可以生成 montage 供调试，但正式节奏审查留给下一 bounded task；
- 不宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

本任务完成后，Planner 再单独创建 contact-sheet / deck-rhythm QA task。只有 full-deck integration 与 rhythm QA 都成立后，才进入真实 holdout。
