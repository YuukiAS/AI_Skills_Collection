---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 037_research_presentation_audience_transition_copy_recovery
decision: PLAN_FROZEN
---

# 037 Research Presentation Audience Transition Copy Recovery — Plan

## Objective and value

只关闭 Stage 4 当前已被真实 production output 明确定位的 audience-facing transition-language gap。当前医学影像页的科学内容、same-case comparison 与 workstream separation 都成立，但页面顶部直接向听众显示 `Workstream transition` 和 `independent workstream; no causal bridge asserted.`，这属于制作/控制层措辞，不符合 Program Goal 对成熟博士组会“只呈现科研叙述、不泄漏 workflow/meta language”的要求。

完成后，多研究方向 deck 仍应让听众一眼看出“这里开始一个独立的新科研方向”，但应通过科学主题标题、section cue、来源支持的上下文和版式结构自然完成，而不是解释内部 storyline/control decision。不得为了去掉元语言而把两个 workstream 强行讲成有因果关系，也不得弱化当前医学影像页的科研内容。

这是新的有限实现机制：共享 normal-production workstream-transition audience-copy / structural-cue emission，而不是继续修改 036 的 process-page layout。

## Frozen decisions

以下能力、语义与 evidence 全部冻结保护：

- 036 已 PASS 的 `EXPERIMENT_DESIGN` / `NEXT_EXPERIMENT` projection scale、source-backed emission 与 generic regression；
- 035 已关闭的 generic-model source-grounding 与成熟模型页；
- 034 dual render-input / rendered-pixel identity 与标题页 audience anti-meta gate；
- 032 已通过的 multi-workstream grouping：统计主线内部连续，医学影像属于独立第二 workstream；不得虚构 causal bridge；
- 当前医学影像页的 same-case Input / GT / Prediction / Error、ROI zoom、TP/FP/FN overlay semantics；
- Stage 2 gold retrieval、Stage 3 executable CUHK layouts、canonical exact CUHK `.tex + PDF + PNG` route；
- quantitative result、negative result、model、process pages 的已通过内容和视觉行为；
- deck contact sheet / deck-level rhythm review、一次 automatic repair 上限、unknown/unsafe finding fail-closed / no-winner；
- Stage 5 双真实 paper holdout 尚未启动，本 task 不得使用其论文做调优。

不得通过隐藏 workstream separation、降低视觉门槛、删除医学科学内容、使用旧 Terra 覆盖新像素或把两个研究方向编造成连续因果故事来完成 037。

## Implementation scope

### 1. 把 transition 从制作语言改成 audience-facing scientific cue

限定检查并最小修改 shared normal production 中负责 multi-workstream transition cue 的已有路径，优先包括：

- `skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py` 中 workstream/page-job/storyline metadata 到 audience-facing page spec 的传播与 transition copy；
- 若最终 cue 在 shared Stage 3 layout emitter 中生成，则只做与该 transition field 直接相关的最小 emission 调整；
- 对应 `plugins/codex/plugins/presentations/...` mirror；
- `tests/test_presentations.py` 或现有 multi-workstream presentation regressions。

生产页面不得再默认显示以下控制/制作措辞：`Workstream transition`、`independent workstream`、`no causal bridge asserted`，以及等价的 workflow / implementation / QA / provenance 解释。允许的 audience-facing表达应来自当前 source/workstream metadata，例如新的 section/scientific topic 名称、当前研究问题/对象或中性的科研主题副标题；若 source 没有额外可安全显示的上下文，宁可只使用清楚的 scientific section/topic cue，也不要生成内部免责声明。

“不虚构因果关系”继续作为内部 storyline constraint 和测试条件存在，但不需要作为面向听众的控制语句逐字显示。

### 2. 保持 workstream separation 可见且通用

transition repair 必须仍让 multi-workstream deck 的第二方向在视觉和阅读结构上明确开始。实现只能依据已有 `workstream` / page-job / source metadata 与通用 section semantics，不得：

- 检查当前 `Segmentation robustness`、clustered calibration、医学标题、页号或 test ID 后写特殊分支；
- 将任何两个相邻 workstream 自动描述为“因此”“导致”“应用于”等因果/承接关系；
- 用 generic card、流程箭头或新的 filler block 替代现有成熟页面。

单 workstream 输入继续不得被强制插入 transition cue。

### 3. 增加与当前 fixture 解耦的 bounded regression

增加或强化有限 regression，使用与当前 clustered-calibration / segmentation 文案无关的两个 workstream，例如一个 estimation/method workstream 与一个 acquisition/measurement workstream，通过正常 shared storyline/production path 验证：

- 第二 workstream 有可见、自然、由 source/workstream metadata 派生的 scientific cue；
- audience-facing output 不含 `Workstream transition`、`independent workstream`、`no causal bridge asserted` 或等价内部控制语言；
- 不含当前 `Segmentation robustness` 等 fixture-specific固定 copy；
- 不生成未经 source 支持的 causal connector/copy；
- 单 workstream regression 仍不出现多余 transition；
- shared/plugin parity 保持成立。

测试约束的是通用 transition-language mechanism，不对当前 slide 7 像素位置做 brittle snapshot。

### 4. 重新生成 Stage 4 engineering deck 并取得 fresh visual evidence

通过正式 normal production entry 重新生成当前 Stage 4 engineering bundle。医学页 audience pixels 发生变化后，更新 task-local visual manifest 并等待 fresh Terra；缺 fresh evidence 时不得消耗 review round或宣告 PASS。

至少必须读取：

- `slide_7_medical_image_comparison` item-level judgement：页面仍明确进入新的医学影像科研主题，same-case image/ROI/TP-FP-FN 语义保持正确，且不再出现制作/控制元语言；
- `deck_contact_sheet` item-level judgement：第二 workstream 的切换仍清楚，整套视觉节奏成熟，没有因去掉 disclaimer 而显得断裂或误导；
- slides 2–6 的 item-level / regression evidence：不得出现新的 scientific、layout 或 audience-meta blocker。

Terra top-level PASS 不能替代上述 item/page-level判断。

### 5. CI / parity

Executor 重新运行 targeted multi-workstream regression、full presentation regressions、skills/marketplace validation、Reviewed Handoff validation与真实 GitHub CI。shared 与 plugin mirror 必须保持 parity。

不得通过修改 review rubric、忽略当前 Program Goal 的 audience-meta禁令、跳过 contact-sheet review或删除失败 assertion来取得 PASS。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 037：

1. 正常 production 的 multi-workstream transition 不再向听众显示 `Workstream transition`、`independent workstream`、`no causal bridge asserted` 或等价制作/控制语言；
2. 第二 workstream 的开始仍通过科学主题/section/source-backed cue 清楚可见，不依赖隐藏 transition 或编造因果关系；
3. 实现由通用 workstream/page-job/source metadata 驱动，不存在当前 segmentation/clustered fixture、页号或 test-ID special case；
4. unrelated dual-workstream regression 证明 source-derived transition、无 fixture copy、无内部 meta language、无 invented causal bridge；单-workstream行为无回归；
5. 医学影像的 Input/GT/Prediction/Error、ROI、TP/FP/FN 与当前视觉可读性无回归；
6. 036 process pages、035 model、result/failure pages、032 storyline grouping、exact CUHK identity、dual identity 与一次 repair budget 无回归；
7. shared/plugin parity、targeted/full tests、skills/marketplace/Reviewed Handoff validation 全部通过；
8. 真实 GitHub `Codex Marketplace` CI 通过；
9. fresh task-local Terra 与当前 implementation/render/pixel/contact-sheet identity 一致，`slide_7_medical_image_comparison` 与 `deck_contact_sheet` 均达到 item-level mature research-group-meeting / strong conference-talk PASS，且其他主要页无新的 blocking regression。

若这些条件全部满足，Planner 再独立判断 Stage 4 是否首次整体 PASS；037 单 task PASS 本身不得自动等同 Stage 4 PASS。

## Natural-language usage / routing expectations

当一个科研汇报包含两个彼此独立的研究方向时，听众应看到类似“Segmentation robustness”这样的科研主题切换，而不是看到“现在发生了一个 workstream transition、这里没有 causal bridge”这样的制作说明。系统内部可以继续严格保证两个方向不会被错误连成因果链，但最终 slide 只需要把科研主题与边界讲清楚。

同样的机制应适用于任意新的第二 research thread，而不依赖医学影像或当前工程样例。

## Out of scope

037 不得：

- 重做 036 process-page geometry/source-grounding；
- 修改 model/result/negative-result/next-experiment 的科学内容或 layout；
- 重做医学影像 panel、ROI 或 TP/FP/FN 语义；
- 改变 032 已冻结的 workstream grouping 或将独立方向强行合并；
- 重写 Stage 2 gold library、Stage 3 layout system、dual identity 或 deck-quality-loop 状态机；
- 增加自动 repair 次数、降低 Terra bar 或更改 visual rubric 来规避 finding；
- 扩 corpus、加入新外部素材、运行或调优 Stage 5 双真实 paper holdout；
- 为当前标题、页号、fixture 或 test ID 新增 production special case。

### Stop condition

一旦通用 audience-facing transition mechanism 经 unrelated regressions 成立、真实 CI 通过、当前医学页与整套 contact sheet 获得 identity-matched fresh item-level PASS 且冻结能力无回归，本 task 立即停止。最多两轮独立 review；不得在 037 内形成无限 copy/layout 微调链。若出现新的、不同的真实 blocker，再按 Program Goal 判断新的 bounded recovery 或真正 human gate。
