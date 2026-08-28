---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 034_research_presentation_render_identity_ci_recovery
---

# 034 Research Presentation Render Identity CI Recovery — Request

## Why this task exists

033 已合法用满两轮 review，并保留 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE` 历史。033 的 deck contact sheet、deck-level evidence consumer、一次 repair budget 和 fail-closed/no-winner 机制本身不需要重做；第二轮真实 GitHub CI 把剩余 blocker 收敛到同一个 evidence-identity 缺口：CI 环境没有真实 PNG render 时，系统既需要明确表示 pixel evidence 尚不存在，又需要证明 bounded repair 已改变实际 production render input。

Program Goal 的 Quality-Preserving Continuation Policy 允许在这种 blocker 已明确且存在唯一 bounded、质量保持恢复路线时自动继续，不要求用户在“保留质量”和“降低质量”之间做无意义选择。

## Product outcome

完成后，normal `research-presentations` production path 的 deck evidence identity 必须在两种环境下都自洽：

- 真实 render 可用时，继续严格绑定 per-page PNG SHA、contact-sheet SHA 和最终像素；
- render unavailable 的 clean CI 路径中，不伪造 pixel SHA，但仍有稳定的 render-input / production-representation identity；
- bounded repair 改变实际 `main.tex` / scientific render input 时，initial 与 repaired identity 必须可验证地不同；
- 033 已通过/保留的 quality-loop scope、repair budget、source fidelity、storyline、gold/layout 和 CUHK/medical 语义不得被放宽。

## Scope

本 recovery 只关闭 033 Review 2 的两个 CI blocker及其直接 evidence contract：

1. no-render sequence summary 对 `rendered_page_sha256=None` 的合法表达；
2. repair 前后 actual render-input identity 的稳定绑定。

不得借机重做 deck-level rubric、增加 repair 次数、修改页面故事线/内容/布局成熟度、运行 Stage 5 holdout，或把缺失像素当作视觉 PASS。
