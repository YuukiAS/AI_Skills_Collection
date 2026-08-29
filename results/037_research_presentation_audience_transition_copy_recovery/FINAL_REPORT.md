# Final Report

## What this task solved

037 关闭了 Stage 4 最后一个已定位的 audience-facing presentation gap：多研究方向 deck 在切换到独立的医学影像方向时，不再把内部 storyline/control 说明直接展示给听众。

此前页面顶部会出现 `Workstream transition` 与 `independent workstream; no causal bridge asserted.`。现在最终页面只显示自然的科研结构提示和当前材料自身提供的研究主题/范围；两个研究方向“不虚构因果关系”的约束仍保留在内部 storyline 逻辑中，而不再变成听众需要阅读的免责声明。

## What changed

共享 normal-production storyline / page-spec 路径现在把当前 workstream 的 label 与安全、来源支持的 scope 传给 audience-facing transition。若 scope 含 workflow、implementation、provenance、workstream、causal-bridge 等内部控制词，则不会把该说明直接输出到页面。

最终 scientific-layout emission 将原先的内部标签替换为中性的 `Research direction`，并使用 source-derived scientific topic/scope 形成可见切换。生产 validator 增加了针对旧内部 transition 文案的 audience-facing 防泄漏检查。

对应回归覆盖了当前 Stage 4 deck、deck-quality repair path、与当前领域无关的双-workstream 输入，以及单-workstream 输入。shared skill source 与 Codex marketplace mirror 保持一致。

## New capabilities / behavior

普通 multi-workstream research deck 现在可以清楚告诉听众“这里开始另一个研究方向”，同时不暴露内部编排语言，也不会自动把两个独立方向编造成因果或方法继承关系。

这种行为由当前 source/workstream metadata 驱动，而不是依赖 `Segmentation robustness`、医学影像页号或工程 fixture。当前真实 Stage 4 页面显示 `Segmentation robustness: independent visual failure analysis.`，其 label 与 scope 均直接存在于输入 bundle 的 workstream metadata 中。

Fresh task-local Terra 对当前医学影像页和完整 deck contact sheet 均给出 item-level PASS，并确认 same-case Input/GT/Prediction/Error、ROI、TP/FP/FN 语义与跨方向切换均保持清楚。

## Deliberately not adopted / unchanged

本任务没有重做 036 已通过的实验设计页/下一实验页，没有修改 035 已关闭的模型页来源驱动机制，也没有重写结果页、负结果页、医学 panel/ROI/overlay、CUHK 模板、gold composition library、render identity 或 deck-quality-loop 状态机。

没有通过隐藏第二 workstream、删除医学内容、增加 generic card/流程箭头、引入新的 filler copy，或把独立研究方向强行描述为“因此”“应用于”“导致”等因果关系来解决问题。

本任务也没有使用 Stage 5 的真实 paper holdout，因此当前 PASS 不构成长周期产品最终验收。

## Example usage

如果一份科研汇报先讲一种统计方法，随后还包含一个彼此独立的成像误差分析方向，系统可以在第二方向开始时显示该方向自身的科学主题和来源支持的范围描述，而不是显示“workstream transition”或“这里不存在 causal bridge”这样的制作说明。

如果输入只有一个研究方向，系统不会为了统一模板而额外插入 transition cue。若第二方向的 scope 本身含内部 workflow/control 语言，系统会保留清楚的科学主题边界，同时不把不适合听众的控制词直接输出到页面。

## Regression and remaining limitations

真实 GitHub `Codex Marketplace` CI 已通过。与当前领域无关的双-workstream regression 证明 transition 由通用 metadata 驱动，不泄漏 segmentation fixture 文案，也不自动生成未经来源支持的 causal connector；single-workstream regression 继续通过。

Fresh task-local Terra 与当前 implementation、render-input、rendered-pixel 和 contact-sheet identity 一致，六个主要内容页及 `deck_contact_sheet` 均为 item-level PASS，且没有 blocking findings。Terra 对模型页留白和 coverage plot 远距离字号给出了轻微非阻断建议，但当前完整 deck 已达到冻结的成熟组会标准，这些页面又属于 037 冻结范围，因此没有在本 task 内扩大返修。

037 本身没有剩余 blocker。Stage 4 的工程闭环现在可以整体关闭；长期 Program 仍未成熟，下一阶段必须用两个未参与 exemplar extraction、rule distillation 或 tuning 的真实公开 paper 走正常 production entrypoint one-shot 生成完整 deck，并最终交由用户人工验收。

## Technical appendix

Implementation commit: `dc1ab6f98d4742fa24cbb70373b11fa35b9e8dfd`.

Real GitHub CI: `Codex Marketplace` run `33222475797` completed successfully on the published 037 handoff, including presentation regressions, marketplace validation and Linux/Windows smoke jobs.

Fresh task-local visual review: `results/037_research_presentation_audience_transition_copy_recovery/visual_review/VISUAL_REVIEW.json`.

Fresh evidence bindings include render-input identity `8ad96cd9810892d08a6a1f0f1880b9b1d86083368c7c3695376a8eaeb95f14c6`, rendered-pixel identity `e763bd215cede7dbfb0733cfda768bc3591e8041e7614cb5f7a75ad799cb3654`, deck-contact-sheet SHA `7f3159a2fc286302677be0bca4434bb468a2ac6439f62e16f5a57dd753136618`, PDF SHA `d922dfcc20cca9c57c2ceb5752a64b657912e93f91346d9aae284b0ab9301893`, and medical-page SHA `981587c717b8398c05658b31c7b043c3b56b2935a68f053e3328430247ac7c8c`.

Key artifacts remain under `results/037_research_presentation_audience_transition_copy_recovery/`.
