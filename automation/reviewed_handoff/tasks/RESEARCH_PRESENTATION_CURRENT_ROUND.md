# Research Presentation Current Round

用户已提出新的明确产品目标，因此上一轮“cycle PASS 后不自动继续”的停止条件已经被新的用户要求解除。当前进入新的 **REFERENCE_CALIBRATED_ONE_SHOT_QUALITY** round。

上一轮 statistical / medical-imaging synthetic benchmark 的结论不被删除，也不被伪造成失败；但其意义重新限定为：工程链路、科学正确性、真实 render、机械 QA、Terra 与 Planner 协作已经建立。它**不是**成熟科研汇报的 gold visual baseline，也不能证明一次调用即可稳定生成高质量 PPTX / Beamer。

长期 `PROGRAM_MATURE=false`。

## 本轮核心问题

当前最大风险不是缺少更多规则，而是：

```text
inspected reference slide
-> RRL / prose lesson
-> generator重新凭空设计
```

参考资料没有足够进入真实 composition decision。新 round 要逐步建立：

```text
reference
-> composition representation
-> candidate design search
-> comparative review
-> locked design system
-> real holdout one-shot generation
```

同时保留 Reviewed Handoff：每个阶段都必须拆成独立 bounded task，最多两轮 review；Codex Executor 不得根据长期 roadmap 自主连续实现多个阶段。

## 当前 bounded task

当前任务：

`018_presentation_external_method_audit`

目标：先对当前公开 Presentation skill / workflow 与本仓库已有机制进行源码级方法审计，确认哪些机制真正值得进入下一阶段，以及许可证/复用边界。至少覆盖 `frontend-slides`、`high-quality-slides`、`many-ppt-skills`、`slideweaver`、`manuscript-to-editable-slides`、`academic-paper-image-ppt`、可访问时的 `ppt-master`，以及 Assertion-Evidence、MIT Communication Lab、PLOS 科研演示指导。

018 只做 comparative audit，不修改 active Presentation skill、generator、Terra rubric、reference corpus，也不提前实现 composition layer / multi-candidate search / holdout benchmark。

## 后续 roadmap（非 Executor 授权）

018 PASS 后，Planner 根据真实审计证据只冻结一个下一任务。候选方向包括：

- exemplar composition representation；
- internal multi-candidate design search；
- comparative reference-calibrated visual review；
- contact-sheet / deck-rhythm QA；
- real statistical holdout；
- real medical-imaging holdout；
- 必要时独立 Beamer holdout。

这些只是长期顺序候选。没有对应 `PLAN_FROZEN` 时，Executor 不得自行开始。

## 当前完成条件

本 round 只有在真实 reference-to-composition transfer、内部设计探索、comparative review、deck-rhythm QA 与两个真实 holdout one-shot benchmark 全部成立后，才有资格写 `ONE_SHOT_QUALITY_PASS`。

当前绝不能宣告本轮 PASS，也不能再次用“Terra 5/5 PASS”单独关闭 design-quality 目标。
