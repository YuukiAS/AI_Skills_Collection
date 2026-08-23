# Research Presentation Design Quality Program Goal

长期目标：让 Research Presentation 系统在**新的真实科研材料**上，一次调用即可稳定生成接近成熟教授组会、seminar 或顶会 oral 水平的 PPTX / Beamer，而不需要用户逐页纠正基础视觉问题。

上一轮 synthetic statistical / medical-imaging cycle 已证明工程链路、科学正确性、真实渲染、机械 QA、Terra 和独立 Planner review 可以工作，但它**不构成高质量视觉金标准**。上一轮 10 页 review pack 保留为 medium / negative baseline；长期 `PROGRAM_MATURE=false`。

## Current Program Goal

新的主线为：

```text
real research material
-> evidence / narrative structure
-> matched inspected research-slide exemplars
-> composition representation / design recipe
-> internal candidate design search
-> comparative visual review
-> locked design system
-> editable PPTX or native Beamer
-> real render + contact-sheet rhythm QA
-> independent Planner review
```

核心要求：

- reference library 不能只留下 prose lesson / RRL ID，必须真实影响构图决策；
- 对高价值或不确定页面，需要内部多候选视觉探索或等价机制，而不是单次默认布局；
- Terra / Planner 的 design-quality review 必须能与真实 inspected exemplars 做相对比较，绝对 PASS 不足以证明高质量；
- full-deck contact sheet / montage 必须参与节奏与重复布局检查；
- PPTX 与 Beamer 共享科研叙事、证据和 exemplar retrieval，但使用各自适合的 renderer / composition grammar；
- 能机械阻断的 AI-slop、内部元语言、默认模板重复等问题进入 deterministic QA；需要审美和学术判断的质量问题留给视觉 reviewer；
- 不再用 synthetic toy 作为最终 design-quality 证明。

## Required Real Holdout Evidence

`ONE_SHOT_QUALITY_PASS` 至少需要两个未用于 exemplar extraction / rule distillation 的公开真实科研 holdout：

- 一个 statistics / biostatistics / methodology holdout；
- 一个 medical-imaging holdout。

从真实论文 / notes / figures 出发，在无用户逐页返修的情况下完成 narrative、reference-calibrated design、candidate selection、PPTX / Beamer、real render、comparative visual review 与 Planner review。至少一个必须输出 editable PPTX；若验证 Beamer，应选天然适合 mathematics / theory 的独立 holdout。

## Maturity Criteria

只有同时满足以下条件，Planner 才可宣告 `ONE_SHOT_QUALITY_PASS`：

- inspected references 真正进入 composition / design recipe；
- 内部 multi-candidate visual search 或等价设计探索机制成立；
- comparative reference-calibrated Terra / Planner review 成立；
- contact-sheet deck-rhythm QA 生效；
- PPTX / Beamer 路由尊重不同媒介优势；
- 两个真实 holdout 在无用户逐页纠正条件下通过；
- 生成 deck 不再出现上一轮 medium baseline 的统一模板脸、默认图表脸、box-arrow wireframe、AI 元语言与弱 composition；
- Planner 能基于真实 reference comparison 说明为什么生成结果接近成熟 research-talk level，而不只是列出机械检查全部通过。

`ONE_SHOT_QUALITY_PASS` 仍不自动等于永久 `PROGRAM_MATURE`。长期成熟度需要后续真实项目回归和多轮稳定证据。
