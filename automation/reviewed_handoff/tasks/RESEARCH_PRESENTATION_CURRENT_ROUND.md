# Research Presentation Current Round

上一轮 synthetic statistical / medical-imaging benchmark 继续只作为工程链路、科学正确性和基础视觉 QA baseline，不是高质量科研汇报的 gold visual baseline。长期 `PROGRAM_MATURE=false`。

当前仍处于 **REFERENCE_CALIBRATED_ONE_SHOT_QUALITY** round。Reviewed Handoff 继续作为主流程：每个阶段拆成独立 bounded task，最多两轮 review；Codex Executor 不得根据长期 roadmap 自主连续实现多个阶段。

## 已完成：018 外部 Presentation 方法审计

`018_presentation_external_method_audit` 已 PASS。

018 的核心结论保持不变：当前最大架构缺口不是更多抽象设计规则，而是 reference library 缺少机器可用的 composition representation，因此新链路应按：

```text
inspected reference page
-> structured composition representation
-> internal candidate design search
-> comparative reference-calibrated visual review
-> locked design system
-> real holdout one-shot generation
```

逐步推进。

## 已完成：019 Reference Composition Representation

`019_research_presentation_exemplar_composition_representation` 已在第一轮独立审核中 PASS。

当前新增 composition layer 已包含：

- 13 个绑定真实 inspected RRL / canonical rendered-page SHA 的 composition records；
- 8 个 renderer-neutral composition families；
- normalized regions / primary scientific-object area / hierarchy / alignment / reading flow；
- deterministic validator；
- 只读 composition selector；
- 不含 source pixels 的 abstract debug montage。

019 证明系统现在能够机器读取“优秀科研页面怎么构图”，但还没有证明生成器会真正使用这些 geometry，也没有 multi-candidate visual search、comparative review 或真实 holdout 证据。

## 当前 bounded task

当前任务：

`020_research_presentation_reference_calibrated_candidate_search`

目标：让同一份 scientific slide content 真正基于 019 的 inspected composition exemplars 产生三个内部候选构图，并保留 source-to-candidate geometry transfer，而不是继续单次默认布局。

020 的关键要求：

- 同一 content payload 内部生成恰好 3 个 candidate previews；
- 三个方向分别承担 reference-faithful、alternative composition、controlled wildcard；
- 差异必须主要来自 composition / object hierarchy，不是换三个颜色；
- candidate search 必须动态消费 019 selector/index，不得硬编码 RRL / fixture layout；
- preview 必须含真实 scientific object，而不是纯 wireframe；
- 至少覆盖一个统计公式/估计量 regression request 和一个医学影像/aligned-evidence regression request；
- old synthetic fixtures 只允许作为 candidate-engine regression content，不得提升为 gold visual baseline；
- 020 不做 comparative Terra、不选 winner、不锁定全稿 design system，也不做真实 holdout。

## 后续 roadmap（非 Executor 授权）

020 PASS 后，Planner 再单独冻结下一任务。后续仍需至少完成：

- comparative reference-calibrated visual review；
- deck-wide design-system locking / generation integration；
- contact-sheet / deck-rhythm QA；
- real statistical holdout one-shot；
- real medical-imaging holdout one-shot；
- 必要时独立 Beamer holdout。

这些仍只是长期方向。没有对应 `PLAN_FROZEN` 时，Executor 不得自行开始。

## 当前完成条件

本 round 只有在 reference-to-composition transfer、内部设计探索、comparative review、deck-rhythm QA 与两个真实 holdout one-shot benchmark 全部成立后，才有资格写 `ONE_SHOT_QUALITY_PASS`。

当前绝不能宣告本轮 PASS，也不能再次用单一 Terra absolute PASS 关闭 design-quality 目标。
