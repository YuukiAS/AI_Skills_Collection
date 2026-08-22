---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 015_presentation_terra_blocker_repair
review_round: 1
decision: REVISE
implementation_commit: 7dc892715ce91fb2d59f97036d25ec0bbec0548d
---

# GPT Review

## Decision

`REVISE`。

本轮三个原始 Terra blocker 已经实质关闭：slide 1 已明确 burden error 为 lower-is-better，slide 2 的同一 synthetic case 已显著放大，slide 3 已形成显式 local-only comparator 与 shared endpoint gate 的完整比较路径；slide 4 仍由新 Terra evidence 判为 PASS。真实 conventional CI/transport 也已通过。

但新的 `gpt-5.6-terra` evidence 暴露出两个仍属于冻结合同范围内、且会影响科研解释正确性的最小 blocker：slide 1 缺少可见的 synthetic/illustrative evidence boundary；slide 2 的 FP/FN overlay 缺少颜色语义 legend。两项都可以局部修复，不需要改变 synthetic 数据、病例、主要布局、slide 3/4 或 Phase B 范围。

## Evidence reviewed

### 1. CI 与新视觉 identity 合法

当前 CI locator 上 `reviewed-handoff/ci-summary` 为 `success`，指向 GitHub Actions run `32564131325`。当前 tracked `VISUAL_REVIEW.json` 使用 `gpt-5.6-terra`，其四张 PNG SHA 与新的 `visual_inputs.json` identity 一致；mechanical evidence 仍为 `MECHANICAL_PASS`，render status 为 `ok`。

### 2. 三个旧 blocker 已关闭

- slide 1：generator 已直接显示 `Burden error / lower is better`，并使用 raw error value；interpretation 不再把错误方向写反。新 Terra review 明确认为 error intervals、value labels、legend 和 endpoint-specific ranking 均可读。
- slide 2：同一 120x120 synthetic source grid 被放大到 188 pixels 的 visual crop，仍保留原 GT/prediction/overlay 和相同 metrics/counts。新 Terra review明确认为四个 aligned panels 与 case metrics 已经 large and readable。
- slide 3：generator 中存在显式 `Local-only comparator` branch；global estimator 与 local-only comparator 均通过 structural connectors 进入同一 endpoint evaluation gate。新 Terra review 对 slide 3 给出 PASS。
- slide 4：本轮 generator 的 slide 4 逻辑未修改，新 Terra review继续 PASS；没有证据支持重新设计它。

## Blocking findings

### F-015-01 — slide 1 缺少可见 evidence boundary

**冻结依据**：PLAN acceptance gate 7 要求 synthetic evidence boundary 保持正确；Visual Review rubric 也明确要求 synthetic / preliminary / generated evidence 不得看起来像 completed proof。

**真实证据**：当前 slide 1 是完整定量结果图，并有明确 interpretation 与 meeting decision，但 generator 的 `draw_result_page` 没有任何 visible `synthetic` / `illustrative` / `not validation` 标签。新 Terra evidence 因此判断该页可能被理解为已经完成的验证结果。

**最小修复**：只在主图附近增加一个紧凑、投影可见的 evidence-boundary 标签，例如 `Illustrative synthetic results — not completed validation`，并让 interpretation 保持与该边界一致。不得修改 endpoint 数值、method ranking、主图结构、标题或其它已接受元素。

**复验条件**：新 render 中该标签必须与主结果图处于直接视觉邻域且可读；新 Terra review 不再因 evidence-boundary 缺失判 slide 1 `REVISE`。

### F-015-02 — slide 2 overlay 缺少 TP/FP/FN 颜色语义

**冻结依据**：PLAN acceptance gate 4 要求 case metrics 与错误区域可读；该页 frozen archetype 明确要求 FP/FN overlay，而 active visual contract 要求 scientific object 的 label/legend 能让观众直接解释图像。

**真实证据**：当前 overlay 使用绿色、红色、蓝色表达 overlap / false positive / false negative，但 `draw_phantom` 只绘制颜色，没有可见 legend。新 Terra evidence 因此指出观众无法仅从页面像素判断哪种颜色对应 TP、FP、FN。

**最小修复**：在 overlay panel 内或紧邻位置增加小型直接 legend，例如 `green = TP/overlap, red = FP, blue = FN`。保留同一 synthetic case、同一 mask/prediction、同一 metrics/counts、当前放大后的 crop 尺寸和整体页面层级。

**复验条件**：新 render 中 legend 投影可读且不挤压现有 case visual；新 Terra review 不再因 overlay color semantics 判 slide 2 `REVISE`。

## Accepted elements locked for repair

本轮返修不得修改以下已通过内容：

- slide 1 的 synthetic endpoint 数值、lower-is-better 编码与当前 method ranking；
- slide 2 的 synthetic case、GT、prediction、metrics/counts 和当前放大的 case visual geometry；
- slide 3 全页，当前 comparator path 已 PASS；
- slide 4 全页，当前 statistical model 与 evidence boundary 已 PASS；
- reference retrieval / source tiers / inspected-reference trace；
- Source Registry、Inspected Page Library、Synthesized Knowledge；
- Phase C benchmark 与长期 Presentation plugin 架构。

## Required repair and handoff

Executor 只做上述两个局部修复，并补最小 deterministic regression：至少保证 slide 1 存在 visible synthetic/illustrative evidence-boundary text，slide 2 存在明确 TP/FP/FN overlay legend。随后重新生成真实 editable PPTX -> PDF/PNG -> mechanical evidence -> visual-input identity；对新的 identity 只运行一次 `gpt-5.6-terra` live review，再进入真实 CI 与第二轮独立审核。

不要为了追求 Terra PASS 对同一 identity 重跑，也不要借本次返修调整 slide 3/4、扩 corpus 或提前开始 Phase C。
