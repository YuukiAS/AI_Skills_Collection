---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 013_presentation_todo_consolidation
decision: PLAN_FROZEN
---

# 013 Presentation TODO Consolidation — Plan

## Objective and value

先把 `research-presentations/TODO.md` 从历史经验清单整理成可持续维护的研究演示知识入口：明确哪些规则已经进入 active layer，哪些经过真实返修证据后现在应提升，哪些应继续等待跨领域 benchmark，哪些只是被更强规则覆盖。目标不是减少规则数量，而是消除“TODO 状态与真实实现脱节”以及“每轮返修继续叠规则”的风险，为后续 Terra blocker repair、统计/生统 benchmark 和医学影像 benchmark 建立稳定基线。

## Frozen decisions

1. 本轮只做 TODO consolidation，不扩 source corpus，不做 Source Scout，不创建新的 benchmark，也不返修当前四页 Terra regression 的具体 slide/generator 问题。Phase B 必须等本任务独立 PASS 后另开 bounded Reviewed Handoff task。
2. `TODO.md` 中每一个 checklist item，或其中语义上可独立执行的规则，都必须拥有且只拥有一个明确分类：
   - `ALREADY_IMPLEMENTED`：当前 active layer 已有语义等价或更强规则，并且有可定位的实现/回归依据；只更新 TODO 状态与说明，不重复造实现。
   - `PROMOTE_NOW`：已有真实项目反复返修、当前 visual evidence 或 regression failure 支持，且对不同科研演示具有稳定通用价值；必须进入正确 active layer 并补 regression evidence。
   - `KEEP_BACKLOG`：规则合理，但目前缺少足够真实失败证据、跨领域验证或不是当前阻断项；保留原经验，不强行实现。
   - `DUPLICATE_OR_SUPERSEDED`：已被更强的 active rule 覆盖或与另一条 TODO 重复；可合并/标注，但必须保留可追溯说明。
3. `TODO.md` 是历史经验与 backlog 的可读入口。不得大规模删除原有有用内容。建议采用清楚、可机器检查的分类标记和简短依据；`KEEP_BACKLOG` 继续保持未完成语义，其余类别只有在事实成立后才可标记为已处理。
4. 以下经验族必须逐项保留并找到真实去向，不得因清理而丢失：audience-first / notation grounding、one-slide-one-job、scientific-object-first、已有方法比较、derivation/prior/scaling 的来源与符号 grounding、diagram gate/geometry/arrow/box/color/text、scientific hierarchy 而非机械对称、主图获得足够面积、真实数据/概念 grounding、revision-scope、source fidelity、evidence boundary，以及 medical image / statistical model / theorem / simulation 等 page archetype。
5. 当前 active layer 已经明确覆盖的规则不得重复提升。特别是：
   - `research-presentations/SKILL.md` 已要求 2–5 个 inspected reference pages、PRIMARY 优先、retrieval trace、audience/notation grounding、one-slide-one-job、scientific-object-first、source/evidence fidelity、真实 render+inspection、医学图像与统计对象的基本页面语义；
   - `RESEARCH_SLIDE_ARCHETYPES.md` 已要求 RESULT_FIGURE 明确 metric semantics/favorable direction 且图形编码支持结论、医学证据获得足够面积，并要求 EXPERIMENT_DESIGN 在冻结合同要求 comparator/estimator/endpoint 时把比较路径真实闭合；
   - 因此当前 Terra slide 1–3 暴露的是 generator/fixture 没有遵守已有规则，不是这三条规则尚未存在。它们在 TODO consolidation 中应按已有覆盖处理，而不是再造第二套规则。
6. 本轮冻结三个 `PROMOTE_NOW` 通用规则族，且只允许围绕它们做必要的 active-layer promotion：
   - **Revision scope / correction regression**：用户、导师或 reviewer 明确指出某个局部问题后，该纠正成为后续返修的回归约束；只改要求修的组件及其直接依赖，不能借返修重排已经正确的页面或恢复已被明确否定的设计。
   - **Diagram semantic gate + structural connectors**：只有当过程、关系、计算流或实验路径本身是科学内容时才使用 diagram；diagram 必须编码真实组件和真实关系，不能用卡片/气泡/文字框冒充科学示意图。箭头/连接线必须是结构连接而不是文本字符，方向与 lane/sequence 必须对应真实流向。不要把 TODO 中每个像素级 geometry/color 数字都提升成硬规则。
   - **Real evidence vs conceptual grounding**：冻结合同要求真实 plot/image/table/data/evidence 时，不能用 fabricated proxy、装饰图或概念插图替代；概念 illustration 可以帮助 grounding，但必须明确其概念性质，且不能满足真实 evidence requirement。
7. derivation/prior/scaling 的通用“来源、符号、假设必须 grounding”若已由 source fidelity / notation grounding 覆盖，应标为 `ALREADY_IMPLEMENTED` 或 `DUPLICATE_OR_SUPERSEDED`；更细的推导页、prior/posterior/scaling 版式启发在 theorem/statistical benchmark 前默认 `KEEP_BACKLOG`，除非当前代码/tests 已真实覆盖。
8. theorem-heavy、simulation、negative-result 等尚未经过本 cycle 对应 benchmark 的细粒度版式规则，不因本任务而强行进入 schema/generator；保留为 `KEEP_BACKLOG` 或按已有 archetype 覆盖标注。
9. 只有机器可验证、且确实需要成为跨实现 contract 的新规则才允许修改 `deck-plan.schema.json` / validator。本轮不以“更严格”为理由扩大 schema；优先把语义规则放在 SKILL / visual QA / archetype 中，并用 deterministic regression 检查其存在和镜像一致性。
10. 当前 canonical gpt-5.6-terra evidence 仍为后续 Phase B 的输入。本任务不得修改/伪造 `VISUAL_REVIEW.json`，不得为了本轮 TODO 整理重复调用 Visual Review API，也不得宣称当前 Terra blocker 已关闭。

## Implementation scope

允许按需要修改：

- `skills/tools/documents-media/presentations/research-presentations/TODO.md`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/visual-qa.md`
- `skills/tools/documents-media/presentations/shared/references/RESEARCH_SLIDE_ARCHETYPES.md`
- `skills/tools/documents-media/presentations/shared/deck-plan.schema.json` 与 validator，仅当上述 machine-enforceable contract 确有必要
- `tests/test_presentations.py`
- 与上述 source changes 对应、必须通过现有生成流程同步的 Marketplace/plugin/generated mirror
- 本 task 的 `results/013_presentation_todo_consolidation/RESULT.md`

Executor 必须先做逐条 inventory：对 TODO item 建立“分类 → 当前依据/目标 active layer → 是否需要代码改动 → regression evidence”的可审计映射，再执行最小修改。若某一条分类需要新的产品/科研语义选择而无法由本 Plan 推导，进入 `NEEDS_GPT_PLANNER`，不要自行发明第五类或扩大 promotion scope。

## Acceptance and regression gates

1. TODO 中全部 checklist item / 独立规则都有四分类之一，不存在未解释的裸 `[ ]` 或含糊“以后再说”；分类定义和标记可由测试机械检查。
2. `ALREADY_IMPLEMENTED` 必须能定位到当前 active rule 和/或 regression，不得只因“听起来合理”打勾。
3. 三个冻结 `PROMOTE_NOW` 规则族已进入最合适的 active layer，并有针对语义边界的 regression tests；不是只改 TODO checkbox。
4. `KEEP_BACKLOG` 仍保留原始经验和以后何种 evidence/benchmark 会触发提升的上下文，不删除。
5. `DUPLICATE_OR_SUPERSEDED` 能指出被哪个更强规则覆盖，历史经验仍可追溯。
6. current Terra 已知的 metric direction、medical-image evidence area、experiment comparator-path 三条规则若已存在，应被识别为已有 active contract；本 task 不修改生成器来“顺便修图”。
7. source skill、shared QA/archetypes、tests 与 generated/plugin mirror 没有明显漂移；必须通过现有生成/一致性检查。
8. 至少运行 `python -m unittest tests.test_presentations` 以及仓库当前 Presentation/Marketplace/全库相关验证；`ci_required=true`，最终进入 GPT review 前必须使用真实 GitHub CI/check 结果。
9. 不新增顶级 Presentation plugin/skill，不改现有长期 Program 架构，不扩 reference corpus，不新增 external source，不调用 Terra 产生新 visual identity。
10. RESULT 必须给出分类统计、三项 promotion 的具体落点、保留的高价值 backlog 示例、未提升的理由、测试/生成检查结果，以及确认 Phase B 尚未开始。

Reviewer 复核时必须读取真实 diff、TODO 分类、active rules、tests 和 generated mirror，不接受 Executor 自报“全部分类完成”作为证据。发现分类遗漏、用 checkbox 冒充 promotion、或删除有价值历史经验均为 blocker。

## Natural-language usage / routing expectations

本任务不新增用户调用入口。完成后的实际价值是：后续用户要求“做统计方法组会”“做医学影像 failure case”“返修某一页图”时，Presentation skill 读取的是已经分层的 active rules 与明确 backlog，而不是一份状态未知、互相重复的历史 TODO；与此同时，尚未经过 benchmark 的 theorem/simulation 细节不会被提前硬编码成普遍默认。

## Out of scope

- 不修当前 Terra slide 1/2/3 的具体 layout、plot 或 experiment-design generator。
- 不重新渲染当前四页 regression，不调用新的 Terra review。
- 不新建 statistical/biostatistical 或 medical-imaging benchmark；这些属于 Phase C。
- 不扩 Source Registry、Inspected Page Library、Synthesized Knowledge，不做 Source Scout。
- 不下载或检查新的外部 decks。
- 不重做 `presentations` Marketplace 插件架构、profile 拓扑或其他 writing/research plugins。
- 不把每个历史颜色、坐标、间距经验都机械升级成 schema hard gate。
