# Research Presentation Corpus & Quality Program

本文件定义 `presentations` / `research-presentations` 的长期参考库与质量计划。它不是一次版本发布任务；任何 `v4.x` 发布、测试全绿或素材数量增长都不能自动代表 program 完成。

## 长期目标

逐步建立一个可验证、可检索、可用于科研演示生成与独立视觉验收的 Research Presentation Corpus，使医学影像、统计方法、理论型报告、模拟实验、博士 proposal/committee/defense、负结果、因果推断、生物统计验证研究等真实任务经过多轮 benchmark 后，关键页面结构稳定、科研对象与证据关系正确，并且 editable PPTX 的真实渲染质量可持续通过独立检查。

## 三层数据边界

必须严格区分：

1. **Source Registry**：候选 deck、课程、公开演讲、指导页面和来源 URL。只表示“这个来源值得考虑”，不得暗示具体页面已经检查。
2. **Inspected Page Library**：只有真正打开并检查过实际页/slide 的记录才能进入。每条必须包含真实 source、真实页码/slide number、实际 scientific object、页面特异观察、rights/provenance 和 inspection evidence。
3. **Synthesized Knowledge**：从已检查页面归纳出的页面原型、对象拓扑、证据邻接、失败模式与 QA 经验。必须能追溯到 Inspected Page Library，但不能反向伪造 page-level evidence。

严禁从 source metadata、speaker、domain、轮转枚举或模板函数自动猜 `page_function`、`page_number`、scientific object 或 visual lesson。候选 source 数量不受此限制，但 page-level record 必须来自真实页面检查。

## Reference Tier

来源必须区分：

- `PRIMARY_RESEARCH_PRESENTATION`：真实科研报告、组会、committee/proposal/defense、conference/research talk 等，可作为生成参考的默认优先层。
- `SECONDARY_TEACHING_REFERENCE`：课程/教学 slides，可学习公式、定理、例题或对象组织，但不能冒充真实科研汇报经验。
- `PRESENTATION_GUIDANCE`：Communication Lab、写作/演讲指导等，只提供原则，不产生真实科研页面记录，除非明确检查其示例页且单独标注。
- `CANDIDATE_BACKLOG`：尚未检查或无法确认质量的候选来源。

生成参考默认优先 `PRIMARY_RESEARCH_PRESENTATION`。覆盖按 gap 驱动，不按凑数驱动。

## 生成与检索要求

真实研究 deck 生成时，应检索 2–5 个与当前页面工作最相关的 **Inspected Page Library** 记录，并留下 retrieval trace。只能学习信息层级、科学对象组织、证据邻接、不确定性表达和失败模式；不得复制整页、机构视觉身份、版权图片或源 deck 的具体样式。

## Benchmark 与 QA

Benchmark 逐步覆盖至少：medical-imaging group meeting、statistical-method group meeting、theorem-heavy seminar、simulation update、PhD proposal、negative-result update、causal inference、biostatistics validation-study。每类先做 3–6 张关键页，不追求完整 deck。

回归输入必须是真实科研对象或明确标记的 synthetic scientific evidence。生成器不能给自己最终 PASS；机械 lint 不能冒充 academic visual QA。

Editable PPTX 的视觉验收必须来自真实 `PPTX -> presentation engine -> PDF -> PNG` 链路。最终 academic visual reviewer 必须实际读取并分析 rendered PNG，对具体页面写出观察和判定；只检查 PNG 数量、manifest、expected objects 或由脚本把所有 criteria 机械填成 PASS 都不合法。

## 成熟度

Round-level 只允许 `PASS / REVISE / WAIT_CI / BLOCKED`（若当前仓库合同另有合法 round 状态则遵循当前合同）。`PASS` 只关闭当前 round，并指出下一轮最高价值 coverage/implementation gap。

只有至少 5–8 类真实科研任务经过多轮独立 benchmark，关键页面连续不需要推翻结构、不退化成 card/table/dashboard、统计/医学语义与证据关系正确、真实渲染 QA 稳定，且当前仓库存在正式成熟证据时，才允许 `PROGRAM_MATURE`。
