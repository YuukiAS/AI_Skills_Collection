# Research Presentation Current Round

上一轮 synthetic statistical / medical-imaging benchmark 继续只作为工程链路、科学正确性和基础视觉 QA baseline，不是高质量科研汇报的 gold visual baseline。长期 `PROGRAM_MATURE=false`。

当前仍处于 **REFERENCE_CALIBRATED_ONE_SHOT_QUALITY** round。Reviewed Handoff 继续作为主流程：每个阶段拆成独立 bounded task，最多两轮 review；Codex Executor 不得根据长期 roadmap 自主连续实现多个阶段。

## 已完成：018 外部 Presentation 方法审计

`018_presentation_external_method_audit` 已在第二轮独立审核中 `PASS`。

第一轮唯一 blocker 是 `brycewang-stanford/many-ppt-skills` 八条原则没有全部按原文文件审计；返修后已补读并记录 `principles/01` 至 `principles/08` 全部原文，structured matrix 与主报告同步更新。最终真实 CI 通过，且任务没有 vendor 外部 skill、复制模板/截图，也没有提前修改 active Presentation skill、Terra、renderer 或 reference corpus。

018 的核心结论保持不变：当前最大架构缺口不是更多抽象设计规则，而是 reference library 缺少机器可用的 composition representation。现有链路仍容易退化为：

```text
inspected reference page
-> prose lesson / RRL trace
-> generator重新凭经验设计
```

因此下一步不是直接做 multi-candidate generator 或 comparative Terra，而是先建立：

```text
inspected reference page
-> structured composition representation
```

## 当前 bounded task

当前任务：

`019_research_presentation_exemplar_composition_representation`

目标：只使用现有 `verification_status=inspected` 的真实科研 reference pages，建立一个小而真实、renderer-neutral、机器可用的构图中间层。

019 至少要把真实页面转成：

- normalized 主 scientific object bbox / area；
- title / figure / equation / image / annotation / caption 等 region roles；
- visual hierarchy；
- alignment groups；
- reading flow；
- layout family；
- abstract color roles；
- 与真实 RRL identity / rendered-page SHA 的绑定。

它必须包含 deterministic validator、只读 composition selector 和不含 source pixels 的 abstract debug montage，从而证明这些记录不只是 prose metadata。

019 明确禁止：

- 扩 reference corpus；
- multi-candidate visual generation；
- comparative Terra；
- contact-sheet quality gate；
- real statistical / medical-imaging holdout；
- PPTX / Beamer renderer 重构；
- 修改 active `research-presentations/SKILL.md`；
- 宣告 `ONE_SHOT_QUALITY_PASS`。

## 后续 roadmap（非 Executor 授权）

019 PASS 后，Planner 再基于真实 composition layer 只冻结一个下一任务。候选方向仍包括：

- internal multi-candidate design search；
- comparative reference-calibrated visual review；
- contact-sheet / deck-rhythm QA；
- real statistical holdout；
- real medical-imaging holdout；
- 必要时独立 Beamer holdout。

这些仍只是长期顺序候选。没有对应 `PLAN_FROZEN` 时，Executor 不得自行开始。

## 当前完成条件

本 round 只有在 reference-to-composition transfer、内部设计探索、comparative review、deck-rhythm QA 与两个真实 holdout one-shot benchmark 全部成立后，才有资格写 `ONE_SHOT_QUALITY_PASS`。

当前绝不能宣告本轮 PASS，也不能再次用单一 Terra absolute PASS 关闭 design-quality 目标。
