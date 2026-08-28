---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 032_research_presentation_storyline_coherence_recovery
decision: PLAN_FROZEN
---

# 032 Research Presentation Storyline Coherence Recovery — Plan

## Objective and value

只关闭 031 第二轮暴露的一个 deck-level production blocker：normal one-call route 在输入含多个独立 research workstream 时，必须形成 source-faithful、可读的 workstream grouping 与 transition，而不是把局部都合格的页面机械拼成不连贯的 deck。

这项修复的价值是把 Stage 4 从“每页可以正常生产”推进到“同一份输入能被正常组织成科研故事”。本任务不是完整 deck-rhythm / bounded repair loop，也不是 Stage 4 PASS。

## Frozen decisions

- 031 的 `REVIEW_1 / REVIEW_2 / FINAL_REPORT / CURRENT` 历史必须保留；不得伪造第三轮。
- 031 已通过并冻结保护的能力不得重做：normal file/path entry、source-fidelity map、compatibility-driven gold selector / recipe、Stage 3 executable layouts、canonical exact-CUHK compile/render、visible CUHK identity、medical semantic overlays、anti-meta leakage。
- 当前 source bundle 真实包含两个 workstream，但 source 不支持把 segmentation error 解释成 clustered interval coverage 的因果组成部分；禁止编造科学桥接。
- 修复机制必须是 source-derived workstream grouping / ordering / transition，不得硬编码本 fixture 的页号、具体标题、section 文本或 `GSC-*` ID。
- 对当前 regression，clustered interval-calibration 的 `Model -> quantitative result -> experiment design -> negative result -> next experiment` 必须保持连续；medical segmentation comparison 作为明确标识的第二 workstream，而不是插在 failure 与 next experiment 中间。
- workstream 切换必须有明显 audience-facing cue。单纯依赖现有顶部 miniframe section navigation 不足，因为当前 fresh pixel review 已证明这种信号没有解决 deck coherence blocker。
- 优先使用 canonical CUHK 能自然承载的 section / transition frame 或等价轻量机制；不得为了 transition 重新设计 CUHK visual identity。

## Implementation scope

### 1. Add a minimal production-level storyline grouping contract

检查 normal production runner 当前如何从 bundle/page jobs 决定顺序。增加一个共享、可追踪的 workstream grouping 层，使 page jobs 可以被归入 source-supported workstream，并在同一 workstream 内按科研依赖顺序排列。

workstream identity 必须来自 source/page-job information，而不是 032 fixture 专用规则。可以使用现有 page-job/query/evidence/domain/source-anchor 信息，或在正常 deck-plan representation 中加入最小的通用 workstream metadata；如果加入字段，必须保持旧单-workstream输入向后兼容。

至少保存 machine-readable storyline trace，包含：

- 每个 page job 的 workstream assignment 与依据；
- workstream 内排序；
- workstream 之间的顺序；
- transition cue 的 audience-facing label；
- 是否存在 source-supported cross-workstream relation；若不存在必须明确为 independent workstream，而不是自动发明桥接。

### 2. Preserve source fidelity while repairing order

对当前 regression：

- coverage workstream 的 model/result/design/failure/next-experiment 逻辑链必须连续；
- segmentation page 必须被移动到独立 workstream 位置，并有明显 transition/section cue；
- 原 source anchors、evidence IDs、gold selection 与 layout family 保持不变，除非纯粹因页面顺序改变导致 locator 更新；
- 不得改写 source bundle 来制造不存在的科学关系。

如果实现采用 transition frame，它只能表达 source-supported 的 workstream label / scope，例如“Segmentation robustness — independent visual failure analysis”，不能声称它解释 clustered coverage failure。

### 3. Reuse the same normal production entry

必须仍从正常 `research-presentations` production runner 的 file/path interface 读取当前 engineering bundle；不得新增 032-only generator 或 test-only orchestration route。

同一个 invocation 应重新产生：

- deck plan；
- source-fidelity map；
- storyline/runtime trace；
- normal gold/layout trace；
- canonical exact-CUHK `.tex + PDF`；
- rendered PNGs；
- mechanical QA；
- 032 task-local visual-review manifest。

### 4. Deterministic regression

增加最小回归，至少证明：

- 当前 bundle 的 coverage workstream 页面顺序连续，`NEXT_EXPERIMENT` 不再被 medical page 分隔；
- medical page 被标为独立 workstream，并有显式 transition cue；
- 删除/改变 fixture 的具体标题文本后，grouping 逻辑仍基于通用 workstream metadata/evidence 而非字符串 hardcode；
- 单-workstream输入不被强制插入多余 transition；
- gold selector / recipe / Stage 3 layout / CUHK identity / medical overlay tests 继续通过；
- audience-facing pages 不泄漏 internal workstream IDs、RRL/GSC/SRC、QA/provenance/workflow 语言。

### 5. Fresh visual evidence

032 必须使用 task-local Visual Review contract：

- manifest: `results/032_research_presentation_storyline_coherence_recovery/visual_review/visual_inputs.json`
- evidence: `results/032_research_presentation_storyline_coherence_recovery/visual_review/VISUAL_REVIEW.json`

manifest 应包含完整主要内容页；若新增 transition frame，也必须作为 review item 或被 contact/deck review 明确包含。

rubric 重点检查：

- medical workstream 是否不再像无关 benchmark 插页；
- coverage failure 到 next experiment 的故事链是否连续；
- transition 是否明确但不过度占页；
- 没有虚构 cross-workstream scientific relation；
- 031 已通过的 CUHK identity、医学语义和主要页面可读性没有回归。

缺 fresh visual evidence 时只等待，不消耗 review round。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 032：

1. normal production entry 仍是唯一 orchestration surface；
2. 当前 engineering bundle 被 source-derived workstream grouping 处理，不是 fixture-specific page reorder；
3. clustered interval-calibration workstream 的 model/result/design/failure/next-experiment 保持连续；
4. segmentation page 作为明确的独立第二 workstream，并有强于现有顶部导航的 audience-facing transition cue；
5. 不虚构 source 不支持的科学关系；
6. source-fidelity map、gold selection/recipe、Stage 3 layout consumption 与 medical semantics 保持成立；
7. exact CUHK identity、真实 compile/render、mechanical QA 继续通过；
8. deterministic targeted/full tests、skills/marketplace/Reviewed Handoff validation 与真实 GitHub CI 全部通过；
9. fresh task-local Visual Review 绑定当前 implementation/render identity，并且医学页不再因 deck coherence 被 item-level `REVISE`；
10. 031 已通过的主要内容页没有新的阻断性回归；
11. RESULT 明确记录 storyline grouping mechanism、current regression order、transition evidence 与 remaining Stage 4 gap。

### Stop condition

达到上述 gate 后立即停止。032 不继续实现 deck-rhythm scoring、candidate comparison 或 bounded automatic repair loop。

如果在该最小 grouping/transition机制下 fresh evidence 仍显示相同“无关 benchmark 插页”问题：

- 不重复只改 section label / page order 的同一动作形成无限 recovery；
- 记录实际 evidence 并交回 Planner，判断是否需要新的 deck-level narrative mechanism。

## Natural-language usage / routing expectations

用户给一份只包含单一研究主题的 paper/update 时，系统应像现在一样直接生成连贯 deck，不额外插入无意义的 workstream divider。

用户给一份包含两个相对独立研究方向的组会更新时，系统应把每个方向内部的结果、失败和下一实验组织在一起，并在切换方向时明确告诉听众“现在进入第二个 workstream”，而不是把第二方向的一页夹在第一方向的失败与后续实验之间。

## Out of scope

032 不得：

- 改写 031 历史或创建 `REVIEW_3`；
- 修改 Stage 2 gold corpus / admission evidence；
- 重做 Stage 3 layout system；
- 更换 canonical CUHK template；
- 重新设计已通过的 medical overlay semantics；
- 实现完整 deck-rhythm / deck-level scoring；
- 实现 bounded automatic visual repair loop；
- 使用 Stage 5 statistics / medical-imaging holdout papers；
- 宣告 Stage 4、`PROGRAM_MATURE`、`ONE_SHOT_QUALITY_PASS` 或最终 human acceptance。
