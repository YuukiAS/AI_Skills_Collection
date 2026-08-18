---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 005_research_presentation_corpus_integrity
decision: PLAN_FROZEN
---

# 005 Research Presentation Corpus Integrity — Plan

## 目标

本 round 只修复长期 corpus 与 academic visual QA 的可信度基础，不扩张来源数量，不追求新 release，不重做已经稳定的 Presentation 格式路由。

## Blocker A — 伪 page-level metadata 必须删除

当前 `build_reference_metadata.py::page_rows()` 从 source metadata 出发，对前 36 个 source 每个自动生成两条页面记录，并通过 `PAGE_FUNCTIONS[(source_index + page_offset) % ...]` 猜 `page_function`；`page_number` 不是实际页码，而是 `metadata page-function record N`。这些记录不能继续作为 Inspected Page Library 或生成参考。

最小修复：

1. 把数据明确拆成三层：
   - Source Registry：候选来源；
   - Inspected Page Library：真实打开过的页面；
   - Synthesized Knowledge：从 inspected pages 归纳的 archetype/QA 知识。
2. Source Registry 增加明确 tier：`PRIMARY_RESEARCH_PRESENTATION | SECONDARY_TEACHING_REFERENCE | PRESENTATION_GUIDANCE | CANDIDATE_BACKLOG`。
3. 删除任何从 source metadata 自动派生 `page_number/page_function/scientific_object/visual_lesson` 的逻辑。`build_reference_metadata.py` 可以生成 source registry/search matrix，但不得制造 inspected page rows。
4. 当前 72 条自动记录必须删除或降级回 candidate/source-level metadata。只有 Executor 真正打开实际 PDF/PPTX/page 并记录真实 page/slide number 后，才可进入 Inspected Page Library。
5. 每条 inspected page 至少包含：source id、真实 page/slide number、实际 scientific object、页面特异观察、page function、rights/provenance、inspection evidence（例如本地 cache checksum + inspected page/slide + inspection date/means）。指导页面若只有原则而没有真实科研页面，不得伪装成 `PRIMARY_RESEARCH_PRESENTATION` page record。

复验：Reviewer 随机抽查 inspected records；任何 `metadata page-function record`、轮转 page function、模板化相同 observation，或无法解释实际页内容的记录都直接 REVISE。

## Blocker B — “独立视觉 reviewer”目前没有看图

当前 `review_research_group_meeting_regression.py` 只检查 render status、PNG 数量以及 manifest 中 `expected_scientific_objects` 是否非空，然后把十项 criteria 全写 `PASS`。这不是 academic visual review。

最小修复：

1. 机械脚本只能做 prerequisite/lint：确认 PPTX slide count、真实 renderer 链、PDF/PNG 存在和 review packet 完整；不得输出 academic `PASS`。
2. 为真实视觉 reviewer 生成可审阅 packet，至少绑定：PPTX commit/fixture、render engine、PDF/PNG 文件、deck plan、Evidence Board、retrieved inspected reference ids、每页 scientific objects。
3. 最终 academic visual decision 必须由实际读取 rendered PNG 的 GPT/人工 reviewer 产生，并逐页写出至少一条页面特异观察；不能由 generator/reviewer script 根据 manifest 自动填十项 PASS。
4. 若当前执行环境无法把 rendered PNG 提供给独立视觉 reviewer，状态应为 `BLOCKED`/等待外部视觉审阅，而不是 PASS。
5. synthetic regression PNG 可以作为 review evidence；不得把公开 source deck 页面、临床图像或版权资料为此提交进仓库。

复验：Reviewer 必须能看到实际 rendered PNG，并核对至少：科研对象是否可读、对象关系是否正确、是否退化成 card/table/dashboard、主图/公式/标签可读性、证据边界是否清楚。没有实际图像观察记录则 REVISE。

## Blocker C — 参考库必须真正进入生成链

当前 regression deck 中的 `RRL-*` reference pull 不能继续引用自动制造的 page records。

最小修复：

- 每个 benchmark/deck plan 在需要参考时检索 2–5 个真实 Inspected Page Library records；
- 检索按 `page_function + scientific_domain/statistical_subdomain + evidence_type` 等任务语义进行，PRIMARY 默认优先；
- 产物留下 retrieval trace：候选、最终选中的 inspected page ids、为什么相关、学习的是哪类组织/证据关系；
- 不复制整页或视觉身份。

本 round 不要求扩大 inspected corpus 到某个数量。宁可只有少量真实页，也不能用自动生成记录凑数。

## 验证与边界

- 更新相关 tests，使自动 page-row synthesis 和机械 visual PASS 成为明确回归失败。
- 现有 `PPTX -> real presentation engine -> PDF -> PNG` 链不能回退。
- 完整 Presentation/Marketplace 测试与 GitHub Actions 通过后再进入 Reviewer。
- 不把 release version bump 当作本 round 成功条件；是否发补丁版本由实现影响和仓库现有版本规范决定。
- 本 round PASS 后，下一轮最高价值 coverage gap 默认是 **statistical-method group meeting**（3–6 张关键页），随后再评估 theorem-heavy / biostatistics / proposal 等缺口。

## Round-level 完成条件

只有 A/B/C 三个 blocker 都有真实证据关闭，且 Reviewer 实际检查过 regression rendered PNG 后，当前 round 才可 `PASS`。`PASS` 不代表整个 Research Presentation Corpus & Quality Program 完成。
