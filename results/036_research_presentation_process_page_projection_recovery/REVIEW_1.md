---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 036_research_presentation_process_page_projection_recovery
review_round: 1
decision: REVISE
implementation_commit: b061ecc99c549bf90f2de0ad80e4379a3bd59451
---

# GPT Review

## Decision

REVISE。

036 的原始投影尺度目标已经取得真实进展，而且不是只依赖 Executor 自报。真实 GitHub `Codex Marketplace` CI 已通过；fresh task-local Terra 与 implementation `b061ecc9...`、当前 render-input identity、rendered-pixel identity 和 contact sheet 一致。最关键的是，Terra 已将 `slide_4_experiment_design` 与 `slide_6_next_experiment` 都判为 item-level `PASS`：实验设计页的 DGP / hierarchy / procedures / endpoints 现在使用了更充分的页面空间，下一实验页的 failure evidence → sampling → comparator → decision 也达到可读且连续的投影尺度。因此 035 留下的两个 process-page scale blocker 本身已经被当前像素关闭。

但 036 仍不能 PASS。独立检查共享生产代码发现，当前通用 process-page emitter 在放大布局的同时仍保留了当前 clustered-calibration engineering fixture 的科学文案。`EXPERIMENT_DESIGN` 会无条件写入 `DGP stress grid`、`Center hierarchy`、`Interval procedures`，并且更严重地无条件写入 `Subject records nested inside each center; 400 reps per cell`；`NEXT_EXPERIMENT` 会无条件写入 `coverage shortfall at high ICC`。新增的 unrelated regression 虽然换成 acquisition / measurement-noise 等不同输入，但只检查几何尺度、字号和 source values 是否存在，没有检查这些 fixture-specific 文案是否被错误带入，所以该测试目前会让 source-unfaithful normal production behavior 通过。

这直接违反冻结 Plan 对“只消费当前 page-job/spec 已有的 source-backed objects”“不得按当前 clustered fixture 术语写死”以及 generic regression 必须约束该行为的要求。当前工程样例恰好与这些固定文本语义一致，因此当前 Terra 的 process-page PASS 不能证明未见真实论文也会 source-faithful。

此外，fresh Terra 新暴露了一个独立的 Stage 4 质量问题：`slide_7_medical_image_comparison` 上仍直接显示 `Workstream transition` 与 `independent workstream; no causal bridge asserted`，并因此把该页以及 `deck_contact_sheet` 判为需要修改。该页 PNG SHA 与 035 完全相同，说明它不是 036 引入的 regression；而 036 Plan 又明确冻结 medical page 与 032 storyline/transition，所以本轮 Executor 不得借 036 越界修改它。这个证据必须保留；若完成下面的 in-scope process-page 修复后 fresh review 仍重复该 finding，Planner 应按质量保持策略单独路由后续 bounded recovery，而不是在 036 内偷偷扩大范围或用旧 PASS 覆盖当前 evidence。

## Blocking findings

### 1. 共享 process-page emitter 仍会向未见 source 注入当前 clustered fixture 的科学语义

**Plan / regression boundary**

- 036 Plan Implementation scope 1–3：`EXPERIMENT_DESIGN` / `NEXT_EXPERIMENT` 只能消费当前 source/spec 的已有 scientific objects；生产实现不得按当前 clustered fixture 的标题、术语、页号或 test ID 写死。
- Acceptance gates 1–5：放大/reflow 必须保持 source-backed content，generic regression 必须能阻止 fixture-specific hardcode 与 underscaled geometry 同时回归。
- Program Goal：真实 audience-facing slide 必须由目标 source 的真实科研对象主导，不得用 engineering fixture 的科学结论替代未见 paper 内容。

**Observed evidence**

- 当前 shared `emit_experiment_design()` 无条件输出 `DGP stress grid`、`Center hierarchy`、`Interval procedures`，以及 `Subject records nested inside each center; 400 reps per cell`。后一句包含明确的当前模拟设计科学事实，不是中性布局标签。
- 当前 shared `emit_next_experiment()` 无条件输出 `coverage shortfall at high ICC`，即使输入 spec 描述的是 unrelated acquisition design。
- 新增 `test_process_page_projection_scale_is_page_job_generic` 的 unrelated spec 使用 acquisition / measurement noise / held-out calibration / unstable endpoint 等内容，但测试只检查 geometry floor、字号与若干 source values 存在，没有断言 clustered-specific固定文本不存在。因此同一共享路径仍可把 ICC / center / interval-specific copy 泄漏到该 unrelated page-job 而测试保持绿色。
- shared/plugin 两份 generator 当前保持 parity，所以这是共享 production behavior，而不是 mirror 偶发差异。

**Minimal repair**

只在 036 已授权的共享 `EXPERIMENT_DESIGN` / `NEXT_EXPERIMENT` emission 与直接 regression 范围内修复：

- 删除或改造上述 fixture-specific科学句子；scientific supporting copy 必须来自当前 spec/source fields；
- 若确实需要分栏标题，只允许使用不会携带当前研究结论的通用结构标签，或直接从当前 page-job/spec 提供的 nodes / semantic roles 派生；不得把 `center`、`interval`、`ICC`、`400 reps` 等当前 fixture 语义作为所有同类页面默认文案；
- 保留刚刚取得 PASS 的 projection geometry、reading order、capacity/no-winner 行为，不退回小字，也不新增 generic filler；
- 扩展现有 unrelated regression：除继续验证 geometry/source values 外，显式证明 unrelated spec 的输出不含当前 clustered fixture 专用科学文案，同时保持 shared/plugin parity。

不得借此次修复修改 model/result/failure/medical 页面、storyline、CUHK identity、gold retrieval、quality-loop 状态机或 Stage 5 范围。

**Required closure evidence**

- unrelated `EXPERIMENT_DESIGN` 与 `NEXT_EXPERIMENT` 通过同一共享生产路径，输出包含其自身 source-backed objects，并明确不再携带当前 clustered fixture 的 ICC / center / interval / 400-replicate 等固定科学文案；
- 036 的 projection-scale regression、full presentation tests、skills/marketplace/Reviewed Handoff validation 与 shared/plugin parity 全部通过；
- 真实 GitHub CI PASS；
- 因 production TeX / pixels 可能变化，重新生成当前 task-local identity 并取得 fresh Terra；`slide_4_experiment_design` 与 `slide_6_next_experiment` 必须继续 item-level `PASS`，不得为了 source-grounding 修复牺牲已经取得的投影尺度质量。

### 2. Fresh Terra 已确认最终 medical transition 仍有 audience-facing workflow language，但它不属于 036 当前 Executor repair scope

**Plan / regression boundary**

- 036 Plan 冻结 032 storyline、多 workstream continuity、medical comparison 页面与相关语义，禁止为本 task 重做这些已通过能力。
- 036 acceptance 同时要求 fresh item/contact-sheet review，不允许只看 top-level workflow success。
- Program Goal 的最终页面标准禁止内部 workflow / implementation 制作语言出现在 audience-facing slide。

**Observed evidence**

- 当前 fresh Terra 的唯一 visual blocking finding 是 `slide_7_medical_image_comparison` 上的 `Workstream transition` 和 `Segmentation robustness: independent workstream; no causal bridge asserted.`；Terra 因此将该页视为 workflow-style wording blocker，并将 `deck_contact_sheet` 判为 `REVISE`。
- 同一 fresh evidence 明确认为整套 deck 的 result → failure → next-experiment 节奏、composition alternation 与前一 research workstream 都已经成熟，整体修改需求“solely”来自最终 transition wording。
- slide 7 当前 SHA-256 为 `af5b29da...`，与 035 fresh evidence 完全一致；035 对同一像素曾给 PASS。因此这是最新审查新显式化的既存 Stage 4 质量缺口，不是 036 process-page implementation 引入的回归。

**Minimal repair**

本轮 036 Executor **不得修改 slide 7 或扩大 storyline/medical scope**。先关闭 Finding 1 的 in-scope source-grounding缺口，并保留这条 fresh visual evidence。若下一份 identity-matched Terra 仍重复该 finding，Planner 应在 036 的合法 review 路由后把它作为独立、范围清楚的 audience-facing transition-copy recovery 处理；不得选择旧 035 PASS 覆盖当前 finding，也不得在 036 偷偷改被冻结页面。

**Required closure evidence**

- 036 repair 不修改或破坏被冻结的 medical image science、same-case TP/FP/FN、workstream separation 与 storyline semantics；
- 下一次 fresh Terra 必须被真实读取。若该 transition wording 仍被判 blocking，则 036 不得据此宣告 Stage 4 overall PASS，Planner 必须继续质量保持路由。

## Non-blocking notes

- 当前 fresh Terra 已确认 `slide_4_experiment_design` 和 `slide_6_next_experiment` 的原始 projection-scale 问题关闭；后续不得因为修 source-grounding 又把字号、diagram scale 或空间利用退回 035 水平。
- `slide_7_medical_image_comparison` 的图像本体、same-case ROI 与 TP/FP/FN 语义没有被 Terra 否定；当前问题只在 audience-facing transition copy，不需要重做医学影像布局。
- 本轮真实 CI 已通过，review round 1 只由上述 frozen-Plan/source-fidelity finding 和 fresh visual evidence触发，不是 CI failure。
