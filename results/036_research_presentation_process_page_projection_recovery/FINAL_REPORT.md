# Final Report

## What this task solved

036 关闭了 Stage 4 工程样例中两个流程型页面的投影尺度问题。实验设计页与下一实验页现在能把已有的、来源支持的科研对象放到足够大的可用区域中，保持清楚的阅读顺序和成熟字号，而不是在大面积空白中央放一个偏小的流程图。

同时，Review 1 发现的来源忠实性缺口也已关闭：共享流程页不再默认注入 clustered-calibration 工程样例专用的 ICC、center、interval 或固定重复次数等科学文案。

## What changed

共享 `EXPERIMENT_DESIGN` 与 `NEXT_EXPERIMENT` scientific-layout emission 现在从当前 page-job/spec 自身读取节点和证据标签，用这些 source-backed 对象形成页面标题层、层级说明和 failure-evidence copy。第一轮已经通过的放大几何、节点尺度、连接顺序与容量处理保持不变。

对应 generic regression 被强化：使用与当前 clustered-calibration 文案解耦的 acquisition / measurement-noise 输入，验证同一共享路径既保留其自身 source values，又不会泄漏当前 fixture-only 科学术语。shared skill source 与 Codex marketplace mirror 保持一致。

## New capabilities / behavior

一般性的实验设计页和下一实验页现在可以在 exact CUHK Beamer 页面中获得投影可读的流程尺度，同时继续由当前 source/page-job 驱动科学内容。换言之，系统不再需要依赖当前 clustered-calibration 示例的标题或术语才能产生较大的流程页，也不会为了放大页面而把示例专用科学结论带到无关研究中。

当前 Stage 4 工程 deck 的实验设计页、下一实验页与整套 contact sheet 已取得与最新实现和最新像素身份绑定的 item-level Terra PASS。

## Deliberately not adopted / unchanged

本任务没有重做模型页、结果页、负结果页、医学影像页、CUHK 模板、gold composition library、storyline/workstream grouping、render identity 或 deck-quality-loop 状态机；也没有扩 corpus、运行 Stage 5 holdout、增加自动 repair 次数或降低视觉标准。

没有通过添加 generic filler、装饰性卡片或缩小字体来伪造信息密度。医学影像页中的既有 workstream transition 文案也没有在 036 内修改，因为它被本任务冻结为 out of scope。

## Example usage

当用户提供一篇包含实验设计的研究材料时，系统可以把真实实验因素、研究层级、方法和 endpoint 组织成投影可读的流程，而不是依赖 clustered-calibration 示例词汇。若材料描述一次失败结果后的下一步实验，系统可以把已有 failure evidence、采样/操纵方案、比较器和决策规则排成连续的 evidence-to-decision 路径，并保持这些内容来自当前材料本身。

## Regression and remaining limitations

真实 GitHub CI 已通过，fresh task-local Terra 对六个主要内容页和 deck contact sheet 均给出 item-level PASS；实验设计页与下一实验页的投影尺度没有因第二轮 source-grounding repair 回退。

036 本身没有剩余 blocker。不过 Planner 独立检查当前实际生成的医学影像页，确认其顶部仍显示 `Workstream transition` 与 `independent workstream; no causal bridge asserted.`。这不是 036 引入的 regression，也被 036 Plan 明确冻结，因此不影响 036 task PASS；但它仍可能违反 Program Goal 对 audience-facing workflow/meta language 的长期质量政策。Stage 4 整体因此仍需一个独立、窄范围的 transition-copy recovery 后再判断是否首次整体 PASS。

## Technical appendix

Implementation commit: `6045675e94d829dd4aa1cf47c0a7cd368002e4cc`.

GitHub CI: `Codex Marketplace` run `33219779376` on the published repair handoff completed successfully, including marketplace validation, presentation regression coverage and Linux/Windows smoke jobs.

Fresh visual review: `results/036_research_presentation_process_page_projection_recovery/visual_review/VISUAL_REVIEW_6045675.json`.

Fresh Terra identity bindings include render-input identity `eef1037690a953c78fdcb290907ee795bef9e6b7bbb5b0a6f564b9d2fc8f1e7b`, rendered-pixel identity `0b2a489ca3c7f0cdb3a14d0de7d76adcc582b7e6027d3e491ea024d585a66443`, and deck-contact-sheet SHA `75bf60339ba39b5b61ced0ad358401e9e3b2bea9d93bbbba4113b8033c10b434`.

Key task artifacts remain under `results/036_research_presentation_process_page_projection_recovery/`.
