---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 036_research_presentation_process_page_projection_recovery
decision: PLAN_FROZEN
---

# 036 Research Presentation Process Page Projection Recovery — Plan

## Objective and value

只关闭 035 Review 2 已由 fresh item-level Terra 明确定位的 process-page projection-scale blocker：当前共享 `EXPERIMENT_DESIGN` 与 `NEXT_EXPERIMENT` 页面虽然科学语义、故事线和来源映射正确，但中央 diagram / labels / decision copy 相对 available CUHK content area 偏小，并留下明显无效留白，导致这两个页面与整套 `deck_contact_sheet` 未稳定达到成熟博士组会的投影可读性标准。

完成后，同一 normal production path 应在不增加无来源科研内容、不降低视觉门槛的前提下，把现有 source-backed process objects 放大、重排到真正适合投影的尺度，并保持 result → failure → next-experiment 逻辑以及所有已经通过的 Stage 4 能力。

这是 035 review-limit 后的质量保持 recovery，使用新的有限实现机制：共享 process-page geometry / emission / capacity reflow，而不是继续修改已经通过的 model-support mechanism。

## Frozen decisions

以下能力与语义全部冻结保护：

- 035 已关闭的 generic-model source-grounding：`STATISTICAL_MODEL` supporting science 只能来自当前 source/spec fields，不得恢复 clustered/ICC fixture hardcode 或内部制作 fallback；
- 当前 model page 的公式主导、source-backed supporting layer 与 fresh item-level PASS；
- 034 dual render-input / rendered-pixel identity contract 与 title/subtitle audience anti-meta gate；
- 032 storyline、多 workstream continuity 与明确的 non-causal medical transition；
- Stage 2 gold retrieval 和 Stage 3 已通过的其他 executable CUHK layouts；
- canonical exact CUHK `.tex + PDF + PNG` production route；
- quantitative result、negative result、medical comparison 的已通过科学语义与页面行为；
- medical same-case TP/FP/FN semantics；
- deck contact sheet / deck-level rhythm consumer、一次 automatic repair 上限、unknown/unsafe finding fail-closed/no-winner；
- Stage 5 双真实 paper holdout 仍未启动，不得在本 task 调优或消费。

不得通过降低字号要求、忽略 fresh Terra、恢复 generic filler、增加无来源科学说明或把旧 034 PASS 当成当前 closure evidence 来完成 036。

## Implementation scope

### 1. 通用放大 `EXPERIMENT_DESIGN` process layout

限定修改共享 scientific-layout geometry/emission 及其直接测试/mirror 支撑，优先处理：

- `skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py` 中 `EXPERIMENT_DESIGN` 的 primary geometry、typed hierarchy/process emission 与必要 label/connector sizing；
- 若 normal production spec propagation 确有必要，可最小修改对应 production-entry propagation；
- 对应 `plugins/codex/plugins/presentations/...` mirror；
- `tests/test_presentations.py` 或现有 presentation regression。

修复必须只消费当前 page-job/spec 已有的 source-backed DGP factors、hierarchy、procedures、endpoints、annotation/caption 等对象。允许：

- 让中央 pipeline 使用更多 CUHK safe content area，尤其利用当前上下空白；
- 提高 node、endpoint、connector annotation 的投影字号/视觉尺度；
- 根据已有对象数量做通用的两行、分层或更紧凑的 hierarchy reflow，只要 reading order 仍清楚；
- 减少 purely-layout whitespace 或装饰性间距。

不得删除关键实验因素来“变大”，也不得新增当前 source 不存在的科学结论。若内容容量超过单页成熟字号，应由既有 capacity/no-winner/split contract 明确处理，而不是把字体缩小到能塞进去。

### 2. 通用放大 `NEXT_EXPERIMENT` evidence-to-decision layout

对共享 `NEXT_EXPERIMENT` path 做同样受限的 projection-scale 修复：

- prior failure evidence、sampling/manipulation options、comparator arms、decision rule 都必须继续来自当前 source/spec；
- 允许重新分配这些对象的宽高、纵向位置和节点间距，使 failure evidence、CR2 / wild-cluster comparator labels、go/no-go criterion 等在投影尺度下可读；
- 保留 prior failure → manipulation → comparator → decision 的 reading order 与语义；
- 对 copy 可以做纯版面级 wrap/reflow，但不得改变科学含义，也不得添加总结性 filler；
- 若现有文字量在成熟字号下一页不可容纳，优先走现有 no-winner/split 机制，而不是缩小成小字。

不得按 `G=8`、ICC、DPP、Mondrian、CR2 等当前 fixture 术语写生产分支；这些词只可以作为当前 source-backed 内容自然出现。

### 3. 用与当前 fixture 文案解耦的 bounded regression 锁定 projection behavior

增加或强化有限 regression，直接验证共享 page-job path 而不是当前标题/页号：

- 一个 `EXPERIMENT_DESIGN` spec 和一个 `NEXT_EXPERIMENT` spec 通过共享 geometry/emission path；
- 关键 diagram/object 区域达到明确的 projection-scale geometry floor，并充分使用 safe content region；
- 关键 labels / nodes 不退回过小的 hardcoded font/box；
- production code 不按当前 engineering fixture 的完整标题、术语、页号或 test ID 分支；
- source-backed content 与 reading order 保留；
- no-support/no-capacity 情况仍 fail closed / no-winner，不引入 generic filler。

测试的目标是约束通用 process-page 可读性机制，不是把当前像素坐标逐点 snapshot 成新的 brittle golden。

### 4. 重新生成当前 Stage 4 engineering deck 并取得 fresh visual evidence

重新走正常 production route 生成当前 engineering bundle。因为 slides 4 / 6 预期发生真实像素变化，必须更新 task-local `visual_inputs.json` 并等待 fresh `VISUAL_REVIEW.json`。

视觉闭环必须读取 item-level judgement，而不是只看 workflow success。至少要求：

- `slide_4_experiment_design` item-level `PASS`：中央 experiment pipeline 使用页面空间合理，节点、endpoint 与 connector annotations 投影可读；
- `slide_6_next_experiment` item-level `PASS`：failure evidence、sampling/manipulation、comparators 与 decision rule 均投影可读，source-specific reasoning 连续；
- `deck_contact_sheet` item-level `PASS`：不再因这两个 process pages 形成明显 density/scale dips，整套 result → failure → next-experiment 与 workstream transition 保持成熟节奏；
- `slide_2_statistical_model` 继续 source-driven、公式主导且无 clustered hardcode / internal meta regression；
- result / negative-result / medical 页面、CUHK identity、storyline 和 medical semantics 无新的 blocker。

### 5. CI / parity

shared 与 plugin mirror 必须保持 parity。Executor 重新运行 targeted/full presentation regressions、skills/marketplace validation、Reviewed Handoff validation 与真实 GitHub CI。

不得为了让 Terra PASS 删除 source-fidelity assertion、放松 current visual rubric、跳过 contact-sheet review 或复用旧视觉 evidence。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 036：

1. `EXPERIMENT_DESIGN` 的共享 process layout 真正扩大/重排现有 source-backed scientific objects，解决大面积无效留白与小标签问题，而非当前 fixture hardcode；
2. `NEXT_EXPERIMENT` 的共享 evidence-to-decision layout 真正提高 failure/comparator/decision objects 的投影可读性，同时保留来源语义和 reading order；
3. 两类页面都没有通过新增无来源文字、generic cards、装饰性 box-arrow 或更小字体来伪造密度；
4. capacity 超限时保持现有 no-winner/split/fail-closed 行为，不强制从不可读布局中选赢家；
5. bounded generic regression 对两个 page-job path 均通过，并能阻止重新出现明显 underscaled process geometry；
6. 035 model source-grounding、模型页成熟度、034 dual identity 与 title anti-meta 全部无回归；
7. result / failure / medical pages、032 storyline、多 workstream transition、exact CUHK identity、medical TP/FP/FN 与一次 repair budget 无回归；
8. shared/plugin parity、targeted/full tests、skills/marketplace/Reviewed Handoff validation通过；
9. 真实 GitHub `Codex Marketplace` CI 通过；
10. fresh task-local Terra 与当前 implementation/render/pixel/contact-sheet identity 一致，`slide_4_experiment_design`、`slide_6_next_experiment`、`deck_contact_sheet` 均 item-level `PASS`，且没有新的 blocking regression。top-level workflow success 不替代这些 item-level gates。

## Natural-language usage / routing expectations

用户仍只需要正常提供研究材料并请求生成科研组会汇报。若一页是在解释实验设计，系统应把真正的实验因素、层级、方法与 endpoint 组织成投影可读的科学流程，而不是把一个小流程图放在大块空白中央。若一页是在说明失败后下一步实验，系统应让已有 failure evidence、操纵因素、比较器与决策规则在一眼可读的尺度上形成连续推理。

这些行为应适用于一般 research presentation page jobs，而不依赖当前 clustered-calibration 工程样例的具体名词。

## Out of scope

036 不得：

- 重写 035 generic-model source-grounding 或模型页科学内容；
- 重写 Stage 2 gold composition library；
- 全面重设计 Stage 3 scientific layout system；
- 修改 032 storyline/workstream grouping；
- 修改 quantitative result、negative-result 或 medical comparison 的科学语义；
- 修改 deck-quality-loop 状态机、review rubric 或 automatic repair 次数；
- 降低 Terra / mature group-meeting quality bar；
- 扩 corpus、引入新外部素材或运行 Stage 5 双-paper holdout；
- 为当前 fixture 标题、术语、页号或 test ID 新增 production special case；
- 因为发现其他“可以更优雅”的 abstraction 扩大本任务。

### Stop condition

一旦共享 `EXPERIMENT_DESIGN` / `NEXT_EXPERIMENT` projection-scale mechanism 在 bounded regressions 中成立、当前 engineering slides 4 / 6 与整套 contact sheet 获得 fresh item-level PASS、真实 CI 通过且冻结能力无回归，本 task 立即停止。若同一投影尺度 blocker 在本有限机制和最多两轮审核后仍无法关闭，只允许按 Program Goal 基于新增 evidence 判断新的 bounded recovery 或真正 human gate；禁止在 036 内无限迭代。
