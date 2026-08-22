# Research Presentation Current Round

当前 improvement cycle 已进入 **Phase C：跨领域 Presentation benchmark**，但统计/生统 benchmark 正在执行一次由用户质量纠偏触发的合法 Plan revision。

Phase A 已通过人工授权后的 `014_presentation_phase_a_recovery` 合法关闭；013 的两轮 `REVISE`、review-limit 与人工决策历史保持可追溯。Phase B 的 `015_presentation_terra_blocker_repair` 已完成第二轮独立审核并 PASS。

015 留下的 diagram-clarity 观察已经在 016 的初版 slide 3 中得到部分验证，但 016 第一轮真实 rendered slides 暴露出更重要的问题：旧审查过度强调“对象存在、语义基本正确、机械 QA 和 Terra PASS”，没有把**成熟科研组会成品的专业完成度**作为硬门槛。用户明确否定当前 016 的整体视觉质量，因此旧 Terra 对 slide 2–5 的 PASS 不再作为视觉 accepted-element lock。

## 当前 bounded task

```text
016_statistical_method_group_meeting_benchmark
```

这是 Phase C 第一类 benchmark：statistical / biostatistical method group meeting。

### 016 当前 revision 目标

科学故事、DGP、simulation 和真实数值保持不变，但全部 5 页重新按成熟统计/生统组会标准实现。新版冻结语义以：

```text
automation/reviewed_handoff/tasks/016_statistical_method_group_meeting_benchmark/PLAN.md
```

为准。

这次 revision 新增以下硬门槛：

- 核心统计公式必须真正 typeset/render，不能把 `beta_1`、`rho`、`sum_g`、`(X'X)^(-1)` 等源码式文本直接给 audience；
- `RRL-*`、`Reference retrieval`、`EVIDENCE_MANIFEST`、`Diagram contract`、`Reading target`、`style not copied` 等内部 QA/provenance 文案不得进入 audience-facing slide；
- 旧 pastel cards / boxy wireframe 不是 accepted element，可以在保持科学证据不变的前提下重构；
- formula / result figure / simulation evidence / negative evidence 必须成为真正的视觉中心；
- English slide text 必须去掉明显 AI/制作元话语，使用自然学术标题、annotation 和 caption；
- 参考页必须真正影响信息密度、公式/图层级与 annotation，而不是只留下 retrieval IDs。

## Reference-informed quality

016 不扩 source corpus；现有 inspected library 已有足够的统计页面用于本次重构。重点 lesson 包括：

- `RRL-028`：公式可以独立成为页面主对象；
- `RRL-030` / `RRL-033`：不确定性应直接编码在占主导面积的结果图中；
- `RRL-023`：区间图直接承载比较与不确定性；
- `RRL-025`：负结果/修正应由真实 evidence 主导，而不是卡片式总结；
- `RRL-026`：simulation 页面应同时暴露生成机制与实际输出；
- `RRL-009`：只有真实 estimator mechanism 才值得画 diagram；
- `RRL-044`：推断目标、模型成分与检查对象需要视觉层级清楚，不能用错误方向箭头制造因果含义。

同时以 MIT EECS/NSE Communication Lab 的 one-message-per-slide、message title、visuals-over-text、signal-to-noise、direct annotation 等公开规范作为最低沟通质量基线；NeurIPS/CVPR 的大字体、少文字、主视觉足够大等要求只用于视觉完成度下限，不削弱统计组会的技术深度。

## Visual Review 与 QA 修订

新的 016 visual identity 必须升级 consumer-specific Terra rubric，明确检查：数学排版、内部元语言泄漏、AI-template/wireframe 痕迹、scientific hierarchy、自然学术文案、reference-informed quality 和真实会场可读性。

可机械识别的低级问题必须在 Terra 之前由 deterministic QA 拦截：内部 ID/QA 文案泄漏、核心公式仍是 source-like ASCII、slide 1 错误串行 connector 等都应直接失败。Mechanical QA 仍不得冒充最终学术 PASS。

Terra 只是视觉证据生产器，不是最终 Reviewer。即使 Terra PASS，只要 Planner 独立查看真实 rendered pixels 后认为页面仍明显不像成熟统计/生统组会成品，仍必须判 `REVISE`。

## 后续顺序

016 第二轮独立 PASS 后，Phase C 仍必须再完成一轮：

```text
medical-imaging research group meeting benchmark
```

医学影像 benchmark 使用同等级别的成熟度门槛，并进一步按 MICCAI/RSNA 风格检查 image / GT / prediction / overlay、failure case、quantitative result、method/experiment diagram、validation/endpoint semantics、直接 annotation/legend 与真实会场可读性。

只有统计/生统和医学影像两类 benchmark 都通过，且 source/generated/tests/visual evidence 没有未关闭 blocker，才能判断本次 Presentation improvement cycle 是否可以收口。cycle PASS 不等于长期 `PROGRAM_MATURE`。
