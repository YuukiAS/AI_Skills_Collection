# statistical-modeling — Long-Term TODO

Canonical maintenance inbox for the `statistical-modeling` plugin.

## Open candidates

### Delegate reader-facing wording without giving away statistical semantics

status: READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER
source: cross-plugin communication boundary audit, 2026-09-05
proposal: Keep `statistical-modeling` as the owner of model choice, assumptions, inferential target/estimand semantics, uncertainty, diagnostics, comparison and statistical conclusion. After those semantics are frozen, use the canonical generic language layer for reader-facing result interpretation, assumption/diagnostic explanations, table/figure captions, bounded conclusions and limitation wording. See `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`.
required boundary: the language layer may translate ordinary English scaffolding and improve explanation, but must not change the estimand/parameter meaning, conditioning set, comparator, uncertainty, calibration statement or conclusion strength. Statistical tables/plots remain statistically owned here even when their captions are rewritten elsewhere.
promotion gate: after task 050 closes and the generic language layer identity is settled, replay one real statistical analysis handoff with a caption/result/conclusion package and verify zero statistical-semantic drift.

### Curriculum-driven capability refinement pilot

status: BLOCKED_NEEDS_EVIDENCE
source: user-approved design direction, 2026-09-01
proposal: Use bounded competency modules backed by authoritative textbooks, methodological papers, and official software guidance. Study/extraction must be reviewed before any active plugin change. See `docs/workflows/CURRICULUM_DRIVEN_DOMAIN_PLUGIN_REFINEMENT.md`.
first pilot: prior specification + prior predictive checking
candidate sources: *Doing Bayesian Data Analysis*, *Bayesian Data Analysis*, *Statistical Rethinking*, and relevant official PyMC / Stan guidance, subject to lawful source access and Planner confirmation.
promotion gate: demonstrate improved reasoning on should-trigger, should-not-trigger, and grey cases; then replay the production path and unrelated regression before release.

No production change is currently frozen from this candidate.

Future TODOs should come from real modeling tasks (Bayesian, causal, inference, simulation, diagnostics, data analysis) and must distinguish scientific/statistical correctness from Presentation/report communication issues.

## Promotion notes

- A wrong assumption, estimand, uncertainty interpretation or calibration claim can qualify as a severe single-project failure.
- A project-specific model choice remains project-local unless it reflects a reusable workflow or diagnostic rule.
- Do not use this plugin to own Presentation layout or manuscript prose.
- Do not fork a second generic say-it-plain/caption-writing rule set; hand off reader-facing wording only after statistical semantics are stable.

## 2026-09-15：统计实现设计的用户审阅反馈

### 统计方案不能只给方法名称而把算法选择留给执行者

status: NEW
source: 用户对研究实施前置方案的审阅，2026-09-15。
evidence: 私有研究项目的设计审阅；本公开记录只保留通用问题，不包含该项目源码、数据、数值结果或日志。本次未运行本插件的生产回放，不能据此声称插件已经造成实装失败。
problem: 高层方法说明没有覆盖输入输出、变量角色、参数变换、目标密度、更新顺序、测试参照及计算成本时，执行者仍需补做实质统计设计。用户要求由规划者先明确这些内容，经独立审查后才执行。需要后续检查插件能否帮助识别这种“看似详细、实则不可直接实现”的方案空白。
project-specific context: 当前项目明确禁止Codex规划。该权限限制来自用户和任务合同，不应通过调用具有规划能力的统计插件绕过；不将此限制未经审查推广为所有项目的永久工作流规则。

### 独立参照、近似误差和数值实现误差应分别说明

status: NEW
source: 同次前置设计审阅，2026-09-15。
evidence: 用户提出需要明确哪些对象有解析真值、哪些仅有软件或采样参照；相关私有证据未公开。本条为待评估能力需求，不是已完成的插件回归结果。
problem: 两个程序调用同一底层数值库，或共享同一种近似时，其一致性并不能证明近似准确。需要分别说明解析恒等式、独立积分、可靠多链采样、已知生成机制、真实留出评价和历史快照各自验证什么。重复项的误差可能被重数放大；参考采样必须带混合诊断与Monte Carlo误差，不能默认视为真值。
project-specific context: 不把某一研究模型的具体积分方法、误差阈值或采样设置写成通用默认；后续中央规划者应选合法公开案例验证这一能力。

### 随机数与数据处理应绑定到统计目标，而不是只记录一个seed

status: NEW
source: 同次前置设计审阅，2026-09-15。
evidence: 用户明确追问数据生成、拟合、后验预测、多链、重采样、确定性变换及多seed敏感性的区别。本轮只记录需求，未宣称这些场景已经完成插件回放。
problem: 需要区分同一数据的算法随机性、不同生成数据的统计重复、先验/截断的模型敏感性；同时说明训练集变换、身份对齐、后验期望区间与预测区间、重采样单位和恢复目标。不能把几个算法seed当成独立数据重复，或将真实数据中不可观测参数标成ground truth。
project-specific context: 具体随机流机制、seed、变换池和检验门槛仍属于项目设计，不能自动复制成中央插件规则。

以上条目不授权修改SKILL、runtime、路由、版本、Marketplace或生产测试。后续真实实现若产生新证据，应在对应条目补充或去重；未发现新问题时无需制造TODO。