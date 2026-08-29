---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 042_research_presentation_semantic_compatibility_recovery
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

041 已经用一个完整 frozen four-paper batch 证明，当前 `research-presentations` 的剩余泛化缺口至少有一个共同的结构性来源：**相同的科学页面/对象语义在不同真实论文里会带有不同的自由文本 label，而成熟构图检索与 bounded quality-loop repair mapper 目前分别依赖各自较窄的词面匹配。** 结果是两种保守失败：正常 production 在已有成熟 gold 实际可表达相应 page job 时仍可能 `no compatible gold composition record`；或者真实视觉 finding 已经明确指出“主科学对象过小/说明与引用碰撞”，消费者仍因对象 label 不在预设 vocabulary 内而 `UNSAFE_REPAIR_MAPPING`。

042 的目标是在**不使用 041 四篇失败 holdout 的具体内容、不新增/调优 gold、不降低 mature quality bar**的前提下，建立一个最小共享的 scientific-object semantic compatibility layer，让 gold retrieval 与现有 quality-loop mapping 对“结构上等价、名字不同”的科研对象保持稳定。它必须继续保留真正未知/不兼容输入的 no-winner / fail-closed 行为，并通过独立 non-holdout stress render + fresh Terra 证明这一变化最终能落到真实像素，而不是只让内部状态更容易 PASS。

本 task 只恢复通用机制，不重新执行 041，也不开始新的 Stage 5 holdout batch。042 若 PASS，下一 fresh 4-paper batch 仍必须先经过用户 human gate。

## Frozen decisions

- **041 是不可改写的 failed batch。** TMB、DESeq2、cardiac-ultrasound、RETFound 四篇全部已 consumed；042 不读取其正文/图像/标题/DOI/page-specific rendered content 来设计 fixture、关键词或分支，也不修改 041 source bundle、render 或 visual evidence。
- **不新增 holdout-specific keyword。** production code、tests 和 stress fixture 中不得加入任何旨在匹配上述四篇的标题、DOI、作者、产品名、数据集名或 paper-specific scientific-object 名称。允许测试“任意前后缀/别名不会改变结构语义”，但别名必须是与 041 无关的中性字符串。
- **现有 mature gold composition library 冻结。** 042 不做 source scouting，不新增/删除 gold record，不降低 rights/visual/maturity bar，也不通过“任意 page job 都回退到 general card/box-arrow”消灭 no-match。若现有 gold 对某个规范化语义确实没有成熟兼容项，本 task 必须保留 no-winner 并停止在新的明确 evidence 上；后续是否补 gold 另开 bounded recovery。
- **只建立一层共享的结构语义归一机制。** 不维护第二套 roadmap，也不新造大而全 ontology。允许新增一个小型共享 helper 或在已有 shared script 中实现等价逻辑，但 selector 与 quality-loop 必须消费同一套规范化语义，而不是各写一套 alias 表。
- 规范化只描述 presentation-relevant 的**结构角色**，不编码论文科学结论。至少要能稳定区分现有成熟生产所需的几类角色：数学/模型对象、定量 source figure/plot/table、实验/流程图、医学图像 panel/comparison、讨论/决策对象。实际内部命名由 Executor 决定，但数量必须有限，且能从已有 structured page/spec fields 与通用结构词得到；不得从论文 identity 推导。
- **page function、domain、panel/capacity 等硬约束继续有效。** 规范化对象角色只能消除词面 alias 的假不兼容，不能绕过 page-function mismatch、明显 domain mismatch、panel-count incompatibility、rights boundary 或 content-capacity no-winner。
- **已有 quality-loop vocabulary 不扩张。** 继续使用已经 shipped 的 `RESCALE_PRIMARY_OBJECT`、`REPAIR_ANNOTATION_LEGEND`、`SWAP_COMPATIBLE_GOLD_LAYOUT` 等有限 repair intent；042 只修“同一结构对象因 label 不同而无法安全识别”的 compatibility gap。unknown / ambiguous finding 继续 fail closed；每个 deck 最多一次 repair。
- **真实像素仍是最终证据。** 不能因为 selector 返回 match、mapper 产生 directive 或 unit test 通过就宣称恢复完成。至少一个独立 stress deck 必须真实触发一次安全 repair，前后 render-input 与 rendered-pixel identities 都改变，并通过 fresh item/page-level + contact-sheet Terra。
- Bridge Kit task-local Visual Review contract 继续作为视觉 evidence contract；缺 fresh evidence 时等待，不消耗 Reviewer round，不新造状态机。
- exact CUHK、source fidelity、数学原生 LaTeX、真实/允许的 scientific assets、medical image semantics、single-cycle quality loop 和 Stage 1–4 已通过行为均为 regression boundary。

## Implementation scope

1. **建立最小共享 scientific-object semantic normalizer**
   - 审查当前 production spec/query、resolved layout、sequence summary 与 quality-loop 所使用的结构字段，选择一个最小 source of truth；优先复用已有 `page_job`、`content_kind`、`dominant_object_type`、panel/figure/image/diagram 等结构信息，不从 paper identity 推导。
   - 实现有限 canonical role family 或等价归一函数，使诸如 `foo_method_figure`、`studyA_result_plot`、`custom_equation_object`、`case_image_panels` 这类**与任何真实 holdout 无关**的别名，可以在结构信息足够时归一到同一 presentation role。
   - selector 与 quality-loop 必须共享该归一机制；禁止分别维护两份 alias vocabulary。
   - 无足够结构证据时返回 unknown，而不是猜测。

2. **将 mature gold retrieval 改为“硬约束 + 规范化结构兼容”**
   - 允许修改 `skills/tools/documents-media/presentations/shared/scripts/select_gold_compositions.py`、`build_gold_composition_recipe.py` 及其真正需要的最小 shared helper。
   - 保留 page-function/domain/panel/capacity 等现有硬排除；只把当前脆弱的 scientific-object literal token overlap 替换/补充为规范化结构角色兼容证据。
   - 排名仍只在兼容的 mature gold 中进行；没有兼容项时仍 `no winner`。
   - 不修改 `research_gold_composition_index.json` 的 gold 内容来让测试通过；若发现现有 record 缺少可可靠归一的结构 metadata，只允许从 record 已有字段即时推导，或做不改变 gold membership/质量语义的最小 schema-compatible派生，不得新增 holdout-driven record。

3. **让 bounded quality-loop 消费同一规范化对象语义**
   - 允许修改 `deck_quality_loop.py` 以及 production entry / sequence-summary 中为传递 canonical role 所必需的最小字段。
   - 对已经结构化到具体 target page 且 finding 语义唯一的情况，alias 后的 source figure/plot/table、process diagram、medical panel 等必须仍能映射到**已有**安全 repair family。
   - 例如：一个独立 stress page 的 canonical role 为 quantitative source figure，Terra finding 为 projection readability + primary object too small 时，应能在无需内部 `repair_intent` 的前提下安全映射到现有 scale repair；caption/support overlap 的已有安全路径同理。
   - finding 指向 unknown role、跨多个互斥 repair family、需要改科学 claim、需要第二次 repair 或没有实际 downstream layout consumer 时必须 fail closed。

4. **独立 non-holdout alias/compatibility regression**
   - 新增与 041 四篇无关的 unit/integration fixtures，至少覆盖：
     - 数学/模型对象的多种中性 alias；
     - 定量 source figure / plot / table 的多种中性 alias；
     - experiment/process diagram alias；
     - medical image panel/comparison alias；
     - unknown object 与真实不兼容 page-function/domain 组合。
   - 对结构等价 alias，selector 的兼容集合/首选 mature composition 应保持稳定，或至少保持在同一兼容 mature family 内；不能因为无关前后缀变化突然 no-match。
   - unknown / incompatible case 必须继续 no-winner。
   - 增加显式 guard，证明新增 production/test code 不包含 041 四篇的 title/DOI/holdout-specific identifier 作为匹配条件。

5. **独立 visual stress run，验证 directive 真正改变 pixels**
   - 使用 repository 中已有 non-holdout/public-safe材料或新建中性 synthetic/public-safe task-local stress bundle；不得复制 041 source、figures 或 page-specific rendered content。
   - stress deck 至少包含一个 paper-like aliased quantitative figure page，以及一个容易暴露底部 caption/citation容量或 process-layout问题的页面；若使用 medical stress，则只能用现有 public-safe non-holdout asset。
   - 首次生成必须走 normal `research-presentations` production entry，而不是 benchmark-only renderer。
   - 通过 task-local Visual Review 获取结构化 finding；若 finding 与现有安全 repair family唯一对应，允许且最多执行一次已有 bounded repair。
   - repair 前后必须记录 render-input identity、rendered-pixel identity 和 affected page hashes；声称 repair 生效时两层 identity 必须真实变化。
   - repair 后更新 042 的 task-local visual manifest，并取得 fresh Terra；目标页面与完整 contact sheet 都必须达到 frozen mature research-group-meeting / strong paper-talk bar。若真实 finding 无安全映射，则记录 fail-closed，不得改 finding JSON 手工塞内部 intent。

6. **CI / mirror / regression**
   - 同步 presentation skill 与 Codex plugin mirror 中实际需要保持一致的 shared scripts；不得出现一边修复、一边旧逻辑残留。
   - 运行 targeted selector/quality-loop tests、presentation production-entry tests、full unit tests、skill/marketplace validation、Reviewed Handoff validation、visual-review preflight 与真实 GitHub CI。
   - Reviewer 必须独立检查真实 diff，确认没有 041 holdout hardcode、没有 gold admission变化、没有 quality bar放宽，并读取最终 stress render 与 item/page-level Terra，而不是相信 RESULT 自报。

## Acceptance and regression gates

042 只有在以下全部成立时才允许 PASS：

1. **共享语义机制真实存在且只有一套。** Gold selector 与 quality-loop 对 scientific object 使用同一 canonical semantic role/normalizer；不能靠两份手工 alias 表碰巧让测试绿。
2. **Alias invariance。** 至少四类支持对象（数学模型、定量 source figure/plot/table、process diagram、medical image panel）在独立中性 alias 下保持兼容成熟布局；无关 prefix/suffix 或 paper-like identifier 不再导致假 no-match。
3. **No-winner 保留。** unknown role、page-function mismatch、明显 domain mismatch、panel/capacity incompatibility 仍然拒绝；不得新增 unconditional general fallback。
4. **Gold bar 不变。** `research_gold_composition_index.json` 的 admitted mature set/rights boundary不因本 task扩大；没有新的低质量 card/arrow fallback。
5. **Repair mapping 复用现有 vocabulary。** 对结构化、唯一、安全的 undersized-primary-object / caption-support collision / process-layout finding，canonical role 能让现有 repair family被选择；对歧义 finding继续 fail closed。不得新增第二次 repair或新的宽泛 intent。
6. **真实 downstream pixel effect。** 至少一个 non-holdout stress deck真实执行且只执行一次 safe repair，前后 render-input 与 rendered-pixel identities 均不同；不是只写 hint/state。
7. **Fresh Terra。** 与最终 implementation/render identities绑定的 task-local visual evidence中，所有被修改目标页和完整 contact sheet均无 blocking finding，并达到 mature research-group-meeting / strong paper-talk bar；若使用医学图像，必须确认 modality/panel/annotation语义不被 repair破坏。
8. **Stage 1–4 regression protection。** exact CUHK identity、source fidelity、已有 model/result/process/medical/next-step layouts、single-cycle quality-loop limit、正常 production entry与 existing tests全部保持通过。
9. **真实 GitHub CI PASS。** 本地 tests/mechanical validation不替代 GitHub evidence。
10. **Holdout firewall。** 新增/修改 production code与test fixture不得出现 041 四篇的标题、DOI、作者/产品专用词、page-specific source content或 rendered hashes作为匹配/断言依据；041 artifacts没有被修改以制造 closure。

**Stop condition：** 若共享语义归一后，现有 mature gold 对某一必需结构角色仍确实没有兼容 record，042 不得偷偷 intake 新 gold或降低门槛；以新增的 selection evidence终止本 task，再由 Planner决定是否创建独立 gold-coverage recovery。若安全 repair 已能映射但现有下游 layout无法在一次 cycle内产生合格像素，042 同样不得扩成新 layout architecture；保留真实 Terra blocker，后续另开 bounded layout-capacity recovery。这样避免重复 041/039 的失败动作或形成无界恢复链。

## Natural-language usage / routing expectations

用户侧行为不新增新的命令或选项。修复后，普通调用仍然是“根据这篇科研论文生成一套 CUHK 组会汇报”。差别应体现在内部稳定性：论文把主要结果对象叫作 `effect figure`、`benchmark panel`、`response plot` 或其他结构上等价的名字，不应仅因 label 不同就让 mature gold selector失配；同样，当视觉审核明确指出该主图过小，bounded quality loop应根据结构角色安全选择已有缩放 repair，而不是因为自由文本名称不同直接无法理解。

对真正不支持的对象或不兼容布局，产品仍应明确 no-winner / fail closed，而不是生成低质量通用卡片。因此用户看到的是“支持范围内更稳健，不支持范围内仍保守停止”，而不是质量门槛降低。

## Out of scope

- 不重新运行、修复、美化或重新评估 041 的任何一个 holdout deck。
- 不选择、冻结或 acquisition 下一组 Stage 5 fresh papers；042 PASS 后先进入用户 human gate。
- 不新增 gold composition source、外部 reference intake 或无界 corpus scouting。
- 不重写 canonical CUHK template、整体 storyline、source ingestion、figure extraction 或医学图像 pipeline。
- 不新增第二套 repair state machine、第二次 repair cycle、LLM自由修图/自由改 scientific claims，或宽泛“任何 finding都自动修”的 mapping。
- 不把 strict production-entry validator 中与 031 fixture相关的其他历史问题顺手纳入，除非它直接阻止本 plan 的独立 stress production entry；若需要较大 validator redesign，记录为后续任务而不是扩大 042。
- 不把“减少 no-match 数量”本身当作成功指标；成熟 gold兼容性、真实像素质量和 fail-closed边界必须同时成立。
