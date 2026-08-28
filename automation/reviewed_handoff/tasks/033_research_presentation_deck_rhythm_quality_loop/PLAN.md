---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 033_research_presentation_deck_rhythm_quality_loop
decision: PLAN_FROZEN
---

# 033 Research Presentation Deck Rhythm + Bounded Quality Loop — Plan

## Objective and value

只关闭 Stage 4 当前剩余的工程合同：normal one-call `research-presentations` production path 在完成 source ingestion、storyline、gold/layout selection、exact CUHK render 后，必须继续做完整 deck 的节奏审查，并在出现明确质量 blocker 时进入有限、source-faithful 的 repair -> rerender -> rereview，而不是把第一次渲染无条件当成最终结果。

033 PASS 后，Planner 才可独立判断 Stage 4 是否整体完成；本任务本身不运行 Stage 5 最终真实 paper holdout。

## Frozen decisions

- 保留 031/032 已通过的 normal file/path entry、source-fidelity map、通用 workstream grouping、normal gold selector/recipe、Stage 3 executable layouts、canonical exact CUHK compile/render、CUHK identity、medical TP/FP/FN semantics 与 anti-meta leakage。
- 不修改 Stage 2 production-gold mature bar，不重做 Stage 3 layout system。
- deck-level review 必须看完整页面序列/缩略图上下文，不能把六个 page-level PASS 简单聚合成 deck PASS。
- repair 必须基于真实 reviewer finding，并受 source fidelity、scientific dependency、capacity 与 compatible-layout contract 限制；不得为了节奏改写科学结论或虚构关系。
- automatic repair cycle 上限固定为 1。初始 review 有 blocker时最多修一次；repair 后仍有 blocker则明确 `QUALITY_LOOP_FAIL / NO_WINNER`，不得继续无限 retry。
- reviewer 没有 blocker时直接 `READY_TO_DELIVER`，不得为了“再漂亮一点”强制修改。
- 不认识或无法安全映射的 deck-level finding 必须 fail closed，不能自由发挥生成新科学内容。

## Implementation scope

### 1. Add deck-level rhythm evidence to the normal production output

normal production runner 在真实 PNG render 后生成一个 deterministic contact sheet / sequence board，保留实际页面顺序，并将其作为 deck-level visual object；不得只生成文件名列表或文字 summary。

至少保存：

- `deck_contact_sheet` image；
- page order 与 page-job/workstream mapping；
- per-page rendered SHA；
- deck-level identity SHA；
- title/section/workstream sequence；
- 页面主科学对象类型与视觉密度的 machine-readable summary。

contact sheet 只服务于审查，不作为 audience-facing slide。

### 2. Extend the task-local Visual Review contract to deck rhythm

033 使用现有 task-local Visual Review contract：

- manifest: `results/033_research_presentation_deck_rhythm_quality_loop/visual_review/visual_inputs.json`
- evidence: `results/033_research_presentation_deck_rhythm_quality_loop/visual_review/VISUAL_REVIEW.json`

manifest 必须包含：

- 完整主要内容页；
- `deck_contact_sheet` 或等价完整序列视图；
- 当前 production/build/storyline identity binding。

rubric 除逐页成熟度外，必须单独检查完整 deck：

- 信息密度是否在相邻页面间出现不合理跳变；
- 是否连续多页重复同一种模板/构图脸；
- 是否存在过密、过空、重复内容或“总结式填页”；
- 结果 -> 失败 -> 下一实验的节奏是否自然；
- workstream transition 是否既明显又不过度占据视觉注意；
- 标题、主对象、图/公式/医学影像的视觉节奏是否像成熟博士组会；
- 是否存在局部 page PASS 但整套 deck 仍像 benchmark 拼接的情况。

必须读取 deck/contact-sheet item-level judgement 与 observations；top-level package `PASS` 不能替代 deck-level mature judgement。

缺 fresh evidence 时按现有 contract 等待，不消耗 review round。

### 3. Add a bounded quality-loop state and evidence consumer

normal production path 增加 machine-readable `quality_loop_state.json`（或等价现有 representation 扩展），至少记录：

- initial render identity；
- review evidence identity；
- deck-level decision；
- blocking findings；
- selected repair directives；
- repair cycle count；
- repaired render identity（若发生）；
- final decision：`READY_TO_DELIVER` / `QUALITY_LOOP_FAIL_NO_WINNER`。

增加共享、非 033-specific 的 reviewer-evidence consumer。它只能把 finding 映射到有限 repair intent，允许的类别最多包括：

- `REORDER_WITHIN_SOURCE_DEPENDENCY`：仅在 source/workstream dependency contract 允许时调整顺序；
- `ADJUST_TRANSITION_CUE`：只调整 transition 的可见性/篇幅，不发明科学关系；
- `SPLIT_OVERDENSE_PAGE`：使用现有 capacity/SPLIT_REQUIRED 语义拆页；
- `REMOVE_OR_MERGE_REDUNDANT_PAGE`：仅当 source evidence 与 storyline dependency 允许且不丢关键 claim；
- `SWAP_COMPATIBLE_GOLD_LAYOUT`：只能从 normal selector 返回的兼容成熟 gold/layout 中选择；
- `RESCALE_PRIMARY_OBJECT` / `REPAIR_ANNOTATION_LEGEND`：只修投影可读性与已有科学对象的表达。

禁止 repair intent：

- 改写统计/医学结论；
- 新造 source 不支持的变量、结果、图像或因果关系；
- force gold ID、score override、fixture title/page-number hardcode；
- generic rounded-card / box-arrow fallback；
- 修改 canonical CUHK identity。

找不到安全 mapping 时立即 `QUALITY_LOOP_FAIL_NO_WINNER`。

### 4. Prove the repair path without task-specific production hardcode

当前 032 已通过的工程 deck 不应为了测试 repair 而人为降低 audience-facing 正式产物质量。033 必须同时证明两条路径：

1. **真实 clean path**：normal production entry 生成当前 engineering deck -> real render -> fresh deck-level visual review。若 reviewer 无 blocker，quality loop 明确结束为 `READY_TO_DELIVER`，cycle count 为 0。
2. **deterministic repair regression**：使用一个与 production schema 相同的结构化 reviewer-evidence test fixture 注入至少一个允许的 deck-level finding，证明共享 consumer 产生受限 repair directives、cycle count 不超过 1，并且 rerun/representation 的受影响字段确实变化；不得新增 033-only generator 或按当前 page title/GSC ID 写死。

若测试 fixture 注入未知/不安全 finding，必须证明 fail closed/no-winner。

### 5. Preserve the normal one-call surface

用户视角仍是一次普通 `research-presentations` 请求。skill/runner orchestration 可以在内部经历 generate -> review -> optional one repair -> rerender/rereview，但不得要求用户逐页选择或手工调用 benchmark helper。

不得让 Stage 4 engineering proof 直接调用 027/030/031/032 task-specific generator；共享 normal production components 可以复用。

### 6. Fresh render / CI / visual evidence

Executor 完成后重新生成：

- normal production artifacts；
- contact sheet / deck sequence evidence；
- quality-loop state / trace；
- exact CUHK `.tex + PDF + PNG`；
- mechanical QA；
- 033 task-local visual manifest。

真实 CI 必须通过。视觉 evidence 必须绑定当前 implementation、PDF、page PNG 与 contact-sheet identity。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 033：

1. normal `research-presentations` production entry 仍是唯一 user-facing orchestration surface；
2. 完整 deck 有真实 sequence/contact-sheet 级视觉审查，不是 page PASS 聚合；
3. deck-level reviewer evidence 有独立 item-level judgement/observations，并绑定当前像素；
4. clean engineering deck 在真实 review 无 blocker时正常 `READY_TO_DELIVER`，不发生无意义 repair；
5. 共享 evidence consumer 能将允许 finding 映射为有限、source-faithful repair directives；
6. automatic repair cycle 上限真实 enforced 为 1；repair 后仍失败或 finding 无安全 mapping 时明确 no-winner/fail closed；
7. deterministic repair regression 证明 repair directive 会改变相应 production representation/render input，而不是只写一份报告；
8. 无 force-id、score override、fixture-specific title/page-number/GSC hardcode；
9. source fidelity、workstream storyline、gold/recipe/layout consumption、exact CUHK identity、medical semantics 与 anti-meta leakage 无 regression；
10. exact CUHK compile/render、mechanical QA、targeted/full tests、skills/marketplace/Reviewed Handoff validation 与真实 GitHub CI 全部通过；
11. fresh task-local Terra 对主要页面与 deck/contact-sheet 均达到 mature research-group-meeting / strong conference-talk bar，无 blocking finding；
12. RESULT 明确记录 quality-loop state transition、是否触发 repair、repair budget、no-winner 行为与 remaining limitations。

### Stop condition

达到上述 gate 后立即停止。033 不开始 Stage 5 holdout。

如果真实 deck-level review 暴露新的具体 blocker：

- 在本 task 两轮 review 内仅按冻结 repair-loop scope 做最小修复；
- 若达到 review limit 且 blocker 已明确、存在唯一质量保持 bounded recovery，则按 Program Goal 自动创建新 recovery；
- 不降低 deck-level mature bar，也不通过无限 retry 掩盖失败。

## Natural-language usage / routing expectations

用户只说“根据这篇论文做一份组会汇报”时，系统内部应在第一次完整渲染后检查整套 deck 的节奏。如果整套已经成熟，直接结束；如果某一页过密、连续几页模板重复或 transition 失衡，系统只做一次受限修复并重新检查。若修复后仍不达标，应明确失败，而不是把低质量 deck 当作成功交付。

## Out of scope

033 不得：

- 运行或选择 Stage 5 的 statistics / medical-imaging holdout papers；
- 宣告 `ONE_SHOT_QUALITY_PASS` / `PROGRAM_MATURE`；
- 修改 Stage 2 gold mature bar；
- 重写 Stage 3 scientific layout system；
- 修改 031/032 历史 review；
- 新建无限重试、多代理自博弈或无界 candidate search；
- 要求用户介入选择单页布局。
