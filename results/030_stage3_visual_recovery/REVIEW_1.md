---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 030_stage3_visual_recovery
review_round: 1
decision: REVISE
implementation_commit: f0a23caa17bdc4cc1f2756e6dd8f587e6a32acf8
---

# 030 Stage 3 Visual-Maturity Recovery — Review 1

## Decision

`REVISE`

030 已经实质关闭了 027 留下的大部分 Stage 3 视觉结构问题，而且真实 CI 已通过，task-local Visual Review 也第一次按正常 push resolver 自动产生了与当前实现 identity 一致的 fresh evidence。六个主要内容页中，统计模型页、实验设计页和医学影像页达到当前 mature research-group-meeting / strong conference-talk 门槛；结果页、负结果页和下一实验页仍各有一个明确、范围很小的 blocker。

本轮不重做已经通过的 primitive，也不扩大 Stage 2 corpus、CUHK identity、Terra contract 或 Stage 4 scope。只修下面三个当前像素中可直接观察、且与冻结 Plan 明确相关的问题。

## Blocking finding 1 — 结果页仍暴露制作/QA 元语言

### Plan basis

030 Acceptance Gate 2 要求 quantitative result 成为成熟、可投影的科研结果图；Acceptance Gate 1 同时要求 audience-meta leak gate 保持。Program Goal 明确禁止把内部 workflow、QA、provenance 或制作语言放到观众页面。

### Observed evidence

fresh Terra 对 `slide_3_real_data_application` 的真实像素判为 `REVISE`。图本身已经明显改善：三分面 coverage plot、坐标轴、刻度、method key、0.95 nominal line 与 small-G callout 都可见；真正剩下的问题是图下方出现：

> Native axes, facets, method key, nominal line, and interval callout are bound inside the result figure.

这句话描述的是实现/验收机制，而不是科研结论。生成后的 `main.tex` 中也实际包含这段 audience-facing 文本，因此不是 Terra 的主观误读。

### Minimal repair

只把该句替换为与当前模拟结果一致的科学解释，例如直接概括 cluster count / ICC 下 coverage pattern 或 small-G failure 的含义。不要改变现有数值、图形几何、method mapping、nominal line 或 callout identity。

修复后需要看到：真实 rendered page 不再包含实现/QA/provenance 语言，同时现有结果图保持可读。

## Blocking finding 2 — 负结果页缺少可读的纵轴刻度

### Plan basis

030 明确冻结了 027 已通过的 negative-result 语义，同时 Acceptance Gate 1 要求该能力不回归。对于以 coverage 为主证据的定量图，当前 Stage 3 visual contract 要求图本身具有可读的 native axis / ticks / nominal reference，不能只依靠条顶数值或旁边文字解释。

### Observed evidence

fresh Terra 对 `slide_5_negative_result` 判为 `REVISE`。页面已经没有上一阶段的文字重叠问题，paired bars、uncertainty bars、method key、条顶数值、0.95 target line 和 “still below nominal” 提示都存在；但主图没有可见的纵轴刻度与标度。观众因此能看出“低于 0.95”，却不能自然地从坐标轴读取 coverage 的量级。

这不是要求重做 negative-result layout，而是当前原生结果图表达少了一个基本定量坐标组件。

### Minimal repair

在共享 negative-evidence/result-figure primitive 中补一个投影可读的 coverage y-axis/ticks，并保留现有 0.95 nominal line、bars、uncertainty、method key 和右侧解释。不要改变 underlying simulation values，也不要对 slide 5 做无关重设计。

修复后需要看到：真实 rendered page 上纵轴标度清楚可读，原来的 negative-evidence 结构与语义保持。

## Blocking finding 3 — 下一实验最后一条关系箭头方向反了

### Plan basis

030 Acceptance Gate 5 要求 next-experiment 页形成明确的 evidence -> manipulation/comparator -> endpoint -> decision criterion 科研推理结构；Plan 还要求每条 connector 都表达真实、有方向的 scientific relation。

### Observed evidence

fresh Terra 对 `slide_7_next_experiment` 判为 `REVISE`。内容层已经明显达到预期：页面包含具体 failure evidence、sampling manipulation、comparator arms、quantitative endpoint 与 go/no-go criterion，不再是 generic card workflow。当前只剩最后一条连接线的箭头落在 comparator 一侧，视觉上形成从 go/no-go decision 反向指回 comparator 的关系，与其余从左到右的 evidence-to-decision 推理方向冲突。

### Minimal repair

只修正这一条 connector 的端点/箭头方向，使 comparator / endpoint 继续流向最终 decision rule。若底层 typed-relation primitive 的 from/to 语义存在统一方向错误，应修共享 primitive 并加确定性回归；不要通过对 030 单页写死坐标来遮盖问题。

修复后需要看到：真实 rendered page 的最终关系方向与科研推理顺序一致，现有具体内容与 `GSC-018` 正常选择/消费路径保持。

## Evidence already accepted and frozen

本轮以下能力已得到当前实现与 fresh visual evidence 支持，返修不得无关改动：

- `slide_2_statistical_model`：PASS，native LaTeX 数学为主视觉；
- `slide_4_experiment_design`：PASS，center/subject hierarchy、DGP factors、procedures、endpoints 与方向关系可读；
- `slide_6_medical_image_comparison`：PASS，同病例 input/GT/prediction/error、真实 ROI crop/zoom 与邻近 TP/FP/FN legend 成立；
- quantitative result 已从旧 raster-only 路线升级为 presentation-native figure；
- next-experiment 的具体 evidence/manipulation/comparator/decision 内容已经成立，只修最后 connector；
- exact CUHK、normal Stage 2 selector/recipe、geometry transfer、`SPLIT_REQUIRED`、anti-meta gate 的底层机制不得回归；
- 当前真实 CI 已通过，030 task-local push discovery -> Terra -> evidence writeback 已真实运行。

## Required second-round evidence

Codex 完成上述三个最小修复后，应重新生成当前 Stage 3 TeX/PDF/PNG/机械证据与 030 task-local manifest，并重新走真实 CI 与自动 task-local Terra。第二轮 Planner 只审核新的 implementation identity；旧 `VISUAL_REVIEW.json` 只能作为 blocker closure context。

不得为了通过第二轮降低 mature bar，也不得启动 Stage 4。只有六个主要内容页在新的同一 identity 下全部 item/page-level PASS，且 CI/validation 无回归时，030 才可 PASS 并关闭 Stage 3。
