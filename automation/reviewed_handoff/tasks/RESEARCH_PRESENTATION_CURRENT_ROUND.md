# Research Presentation Current Round

当前 improvement cycle 仍处于 **Phase C：跨领域 Presentation benchmark**。统计/生统 benchmark `016_statistical_method_group_meeting_benchmark` 已在用户质量纠偏、Plan revision、成熟度重构、两轮独立审核以及一次人工授权的机械 CI 依赖恢复后正式关闭。

016 的两轮审核历史保持不变：第二轮 `REVISE` 的唯一 blocker 是干净 GitHub runner 缺少 `matplotlib`，而不是当前五页内容重新被判差。用户随后授权一次严格限定的 CI/test dependency recovery；恢复只补齐测试依赖，没有修改 DGP、simulation 数值、五页 Presentation、Terra rubric、reference corpus 或 visual evidence。新的 GitHub Actions run `32577691334` 中 required jobs 全部成功，因此该人工恢复关闭了第二轮剩余 blocker，没有伪造第三轮自动 Reviewer。

016 最终保留的质量基线包括：真正数学排版、禁止 audience-facing RRL/QA/provenance 泄漏、scientific object 作为视觉中心、reference-design audit、deterministic anti-leak / math-source QA，以及成熟度增强后的 `gpt-5.6-terra` rubric。最终 Terra identity 五页均 PASS、无 blocking finding。

## 当前 bounded task

```text
017_medical_imaging_group_meeting_benchmark
```

这是 Phase C 第二类 benchmark：medical-imaging research group meeting。

### 017 冻结目标

建立一个 5 页、public-safe、真实可编辑/渲染的医学影像研究组会 benchmark，使用 deterministic synthetic cardiac-MR-like lesion-segmentation story，真正检验：

1. imaging task / anatomy / endpoint；
2. multi-center appearance-shift experiment design；
3. quantitative result + uncertainty + endpoint disagreement；
4. same-case image / GT / prediction / error overlay failure analysis；
5. negative result / validation decision + planned next experiment。

具体冻结语义以：

```text
automation/reviewed_handoff/tasks/017_medical_imaging_group_meeting_benchmark/PLAN.md
```

为准。

本任务不使用真实或私有 patient image，不扩 source corpus。现有 inspected medical-imaging library 已覆盖 representative samples、metric+mask、uncertainty、subgroup result、negative comparator、task overview、objective、result table 与 same-case image/GT/prediction panels，足够完成首轮 benchmark。每页仍需语义检索 2–5 个 inspected references，并用内部 `reference_design_audit` 记录真正吸收的设计经验；RRL ID 和 retrieval trace 不得进入 audience-facing slide。

## 医学影像成熟度门槛

017 不接受“图都放进去了”作为 PASS。必须满足：

- image / GT / prediction / overlay 是主要 scientific object，而不是被 UI/card/装饰框吞掉；
- modality、slice/anatomy、lesion/target 与 endpoint 在同页自然 grounding；
- overlay / annotation / legend 足够大，听众无需猜颜色和 panel 语义；
- same-case qualitative evidence 与 case metric 一致；
- quantitative result 直接编码 uncertainty / variation，不以 pastel metric cards 代替结果图；
- average Dice 与 lesion-level / burden endpoint 的差异必须由真实 synthetic evidence 支持；
- planned validation 与 completed evidence 严格区分；
- audience-facing slide 不出现 `RRL-*`、`Reference retrieval`、`Diagram contract`、`Reading target`、repo/run/provenance 等内部元语言；
- 页面整体应达到强 medical-imaging PI 组会或 MICCAI/RSNA 风格 research talk 可直接投影的完成度。

## Visual Review 与 CI 链路

017 必须建立独立 evidence identity：

```text
editable PPTX
-> real presentation engine
-> PDF / PNG
-> mechanical QA
-> results/017_medical_imaging_group_meeting_benchmark/visual_review/visual_inputs.json
-> Bridge Kit gpt-5.6-terra Visual Review
-> tracked VISUAL_REVIEW.json
-> Scheduled Planner independent review
```

Terra rubric 必须检查真实 image pixels、panel alignment、legend/annotation、endpoint semantics、failure mechanism、visual maturity、anti-AI/meta-language 与 reference-informed quality；Terra PASS 仍不能替代 Planner 独立判断。

为了避免再次出现干净 CI runner 缺依赖，017 首轮 generator 优先只使用当前 CI 已声明的 stdlib、Pillow、python-pptx、matplotlib；如必须新增第三方包，Executor 先请求 Planner，不得直接留下新的 undeclared import。

## 后续顺序

017 独立 PASS 后，Planner 才能判断本次 Presentation improvement cycle 是否已经满足当前轮次的收口条件。收口前仍需核对 source/generated/tests/visual evidence consistency 与是否存在未关闭 blocker。

即使本 cycle PASS，也不等于长期 `PROGRAM_MATURE`；长期成熟度仍需要更多领域、page function 和多轮真实 regression 证据。
