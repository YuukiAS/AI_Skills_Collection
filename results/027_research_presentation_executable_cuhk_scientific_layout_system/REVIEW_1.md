---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 027_research_presentation_executable_cuhk_scientific_layout_system
review_round: 1
decision: REVISE
implementation_commit: 2b0942ed34896eeb28788f113319858ea1e78ad7
---

# 027 Executable CUHK Scientific Layout System — Review 1

## Decision

`REVISE`

Stage 3 的底层执行链已经成立，但视觉成熟度门槛尚未满足，因此不能 PASS。

本轮独立核对确认以下能力可以保留，不要求重做：canonical CUHK Beamer source 被真实用于构建；六类 page job 都通过正常 Stage 2 selector / gold recipe 进入 resolved CUHK layout；source-derived geometry mutation 会改变 emitted geometry；capacity overflow 会返回 `SPLIT_REQUIRED` 而不是 generic fallback；数学页使用 native LaTeX；integration deck 已真实 xelatex 编译、PDF->PNG 渲染并通过 mechanical QA；当前 handoff tip 的 Codex Marketplace CI run `32814547749` 全部 job 成功。

真正阻断 027 的是冻结 Plan Acceptance Gate 5 / 9：六个主要内容页中只有统计模型页达到成熟博士组会 / strong conference-talk bar，其余五页均有真实像素级 blocking finding。`VISUAL_REVIEW.json` 的 top-level 结论为 `REVISE`，且五条 blocker 都能从当前 emitted TeX / page structure 独立确认，不是仅凭 Executor 自报。

## Blocking finding 1 — quantitative result 的主证据仍不可投影阅读

### Plan basis

冻结 Plan 要求 quantitative result / uncertainty 页面以主结果 figure/plot 为视觉中心，legend、tick、annotation、caption 必须达到投影尺度可读；不得以小图配大块空白通过。

### Observed evidence

Terra 对 `slide_3_real_data_application` 判 `REVISE`：三面板 coverage plot 虽存在，但轴、legend、facet label 与 annotation 在实际 rendered page 上过小，主证据相对页面空白显得不足。

当前 emitted TeX 将 plot 放在约 `0.66\paperwidth x 0.36\paperheight` 的区域，并直接嵌入既有 raster asset。实际像素审查说明，仅扩大容器并没有保证 asset 内部标签达到投影字号。

### Minimal repair

修复共享 result/figure layout，而不是只给本页写死坐标：让 dominant plot 在 CUHK safe region 内获得更高的有效面积，并确保 fixture plot 的 axes / legend / facet labels / callouts 以 presentation-scale 生成或重排。保留正常 selector -> `GSC-014` recipe -> resolver 链；如现有 compatible layout 无法容纳，应走现有 compatibility/capacity contract，而不是回落 generic template。

修后必须看到新的真实 rendered page，主结果和所有关键标注在正常投影尺度可辨认。

## Blocking finding 2 — experiment-design primitive 退化成 generic box-arrow

### Plan basis

冻结 Plan 明确禁止用 generic box-arrow 流程图代替真实研究机制；method / experiment 页面必须由真实 scientific objects、relations 和科学正确的连接方向驱动。

### Observed evidence

Terra 对 `slide_4_experiment_design` 判 `REVISE`。当前页面实际上只是四个圆角框：`DGP knobs -> Clustered samples -> Interval procedures -> Coverage diagnostics`。

当前 generated `main.tex` 也直接确认这一点：页面由四个 `StageThreeBox` 加三条水平 `StageThreeArrow` 构成，除了四个泛化标签外没有中心数、ICC、样本规模、比较方法、评价端点等具体实验对象。因此当前实现虽然消费了 `GSC-004` 的几何，但没有把其 scientific relation lesson 转成成熟的实验设计图。

### Minimal repair

修复共享 method/experiment diagram primitive，使它能够消费 page spec 中的具体 design factors / units / procedures / endpoints，并用 native TikZ 画出科学关系，而不是固定的四框流水线。027 fixture 至少要明确展示本例的 cluster count / ICC / sample-size 或等价 DGP 因素、采样单位、interval procedures 与 coverage/width/bias 等评价端点。连接方向必须语义正确、5 秒内可读。

不得绕开正常 gold recipe，也不得只把当前四个框换颜色或加装饰。

## Blocking finding 3 — negative-result 页面存在真实文本重叠

### Plan basis

冻结 Plan 要求 negative/failure 页面把失败证据与解释邻近呈现，同时必须无裁切、无重叠、可直接阅读。

### Observed evidence

Terra 对 `slide_5_negative_result` 判 `REVISE`，指出图下解释文字重叠形成不可读的暗带。

当前 generated `main.tex` 独立确认：两段不同文本被同时放在完全相同的 `y=0.7478`、相同宽度区域，因此这是确定性的布局缺陷，不是模型审美波动。

### Minimal repair

修复共享 negative/failure figure layout 的 annotation/caption packing：只保留一个清晰主解释，或为 annotation 与 caption 分配互不重叠的可计算区域；同时保持 negative evidence 图为视觉中心。增加 deterministic regression，禁止两个 audience text object 在同一 resolved region 无意重叠。

## Blocking finding 4 — medical-image panel 太小，无法检查真实错误

### Plan basis

冻结 Plan 要求同病例 input / GT / prediction / error / zoom 能在投影尺度下直接检查，panel label、legend、callout 清楚，医学影像本身必须成为页面主体之一。

### Observed evidence

Terra 对 `slide_6_medical_image_comparison` 判 `REVISE`。same-case 结构和标签本身正确，但每个 panel 以及 lesion/error marking 过小，GT 与 error 细节无法可靠检查。

当前 TeX 中四个 panel 各约 `0.1802\paperwidth x 0.2128\paperheight`，并且没有额外 zoom/crop 来补偿小病灶尺度。这与真实像素 judgement 一致。

### Minimal repair

修复共享 medical-image layout，使 panel-count / lesion-scale 能真实影响 resolved geometry：对于四 panel case，优先扩大 image area、减少无效空白，并在需要时增加共享的 zoom/crop/callout 机制。必须继续保持 same-case identity、直接 panel labels 和 error semantics；不得用 task-specific 手写坐标或把影像换成装饰性缩略图。

## Blocking finding 5 — discussion / next-experiment 仍是 generic workflow

### Plan basis

冻结 Plan 要求 discussion/next-experiment 页面通过正常 selector 消费 discussion-compatible gold，把“已有证据/限制 -> 下一验证动作”组织成具体研究推理；禁止 generic future-work cards/box-arrow。

### Observed evidence

正常 runtime 已正确选中 `GSC-018`，但 Terra 对 `slide_7_next_experiment` 判 `REVISE`：页面只是 `Small-G limit -> DPP batch query -> Mondrian partition -> CR2 / wild bootstrap` 四框箭头，没有显示实验因素、比较设置、判定指标或预期诊断结果。

当前 generated TeX 同样确认它仍是四个 `StageThreeBox` 加水平箭头。也就是说，Stage 2 的 `GSC-018` 已被选中，但其 discussion/next-experiment 科研推理还没有被 Stage 3 primitive 充分执行出来。

### Minimal repair

修复共享 discussion/next-experiment primitive，使其至少表达：当前失败证据/限制、待变化的实验因素或选择策略、明确 comparator setup、coverage 或其他 decision criterion，以及结果如何决定下一步。继续由正常 selector / recipe / relation fields 驱动，不允许 force-id、score override 或通用四框模板。

## Accepted evidence that must not be regressed

- `slide_2_statistical_model` 当前 item-level `PASS`；核心公式是 native LaTeX、足够大且层级清楚。若其像素不因共享修复改变，不需要为它重新设计。
- canonical CUHK identity 与 source hashes 已由 build manifest 记录，真实 compile/render 成功；不要修改 canonical theme/style/assets。
- mutation regression 已证明 `primary_bbox` 改变会改变 resolved/emitted geometry；修复不得退回“先写死坐标、后附 provenance”。
- `SPLIT_REQUIRED` capacity failure contract 已成立；修复不得新增 generic fallback。
- Stage 2 gold library、025/026 evidence、Stage 4/5 均不在本轮返修范围。

## Required repair evidence

返修后至少需要：

1. 重新生成受影响的 Stage 3 integration pages 与 build/runtime traces；
2. exact CUHK xelatex compile + real PDF/PNG render + mechanical QA 继续 PASS；
3. 新的 deterministic tests 覆盖 experiment/next-experiment scientific specificity、negative text non-overlap、medical panel readable-area/crop relation，以及 result figure projection-scale contract；
4. 对新像素重新运行 027 task-local Terra item/page-level review；不得复用旧 `REVISE` identity，也不得用 top-level package status 代替逐页 judgement；
5. required repository tests / validation / real CI PASS；
6. 不开始 Stage 4，不运行 Stage 5 holdout，不降低 frozen mature bar。

只有六个主要内容页最终都达到冻结视觉成熟度门槛，027 才有资格在第二轮独立审核中 PASS。
