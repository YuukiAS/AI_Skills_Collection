---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 038_research_presentation_two_real_paper_holdouts
review_round: 1
decision: REVISE
implementation_commit: 1e376b51d703f42324f111b06b6bf4e2d062b8e6
---

# GPT Review

## Decision

REVISE。

038 已经完成了真正的 Stage 5 首次 unseen-paper 生成，而不是 synthetic/fixture 验证：两篇冻结论文均通过预生成 eligibility/source audit，source bundle 在首次 render 前冻结；实现 diff 未修改 `skills/`、`plugins/`、tests 或 production 规则；两个 deck 都从正常 production entrypoint 独立生成并取得 exact-CUHK PDF、逐页像素、render identities 与 contact sheet。当前 GitHub `Codex Marketplace` CI 也真实通过。

但是两套最终像素均未达到 Program Goal 的 Final Quality Gates。Fresh 038 task-local Terra 与 implementation `1e376b51...`、两套 frozen bundle / render-input / rendered-pixel / PDF / contact-sheet identity 匹配，overall decision 为 `BLOCKED`，并给出 7 个 blocking findings。统计 deck 的 contact sheet 被判定未达到 mature doctoral group-meeting paper-talk bar；医学 deck 的 contact sheet同样被判定未达到该 bar。CI green、PDF compile 和 top-level workflow success 因此不能替代真实视觉质量结论。

这轮 `REVISE` 只授权 Plan 已经预先冻结的 bounded quality loop：每个 deck 最多消费这份结构化视觉证据执行一次已 shipped 的 source-faithful automatic repair。不得修改 source bundle、production code、gold/layout rules、selector/validator/prompt，也不得手工 patch `.tex`、PNG 或 PDF。若某 finding 对现有 repair mapping 属于 unknown/unsafe，或一次 repair 后仍未关闭，则必须 fail closed、保留该 holdout 的失败 one-shot evidence并交回 Planner；不得进行第二次 repair，也不得把同一论文继续当作 unseen holdout 调参。

## Blocking findings

### 1. 统计 deck 暴露内部 fixture 语言，并且多个核心证据页不可投影阅读

**Plan / regression boundary**

- Frozen decisions / acceptance gates 要求 audience-facing slide 不得暴露 workflow、QA、provenance 或 engineering fixture 语言。
- statistics deck 必须由 brms 的真实 Bayesian multilevel / Stan 内容、实例、比较和限制主导，并达到 mature paper-talk 可读性。
- 任何 repair 只能来自既有 bounded quality loop，且 source bundle 不得在看到 render/Terra 后改写。

**Observed evidence**

- Terra BF-01：statistics slide 3 真实显示 `rather than importing the Stage 4 clustered-calibration fixture.`。独立读取最终 `main.tex` 也确认该句位于 audience-facing kidney-example 页。
- Terra BF-02：statistics slide 4 底部 source/caption 与解释文字重叠，workflow figure caption 被裁切。
- Terra BF-03：statistics slide 5 的 package comparison table 缩得不可读，source line 与右侧解释相撞。
- Terra BF-04：statistics slide 6 的 worked-example/comparator/decision-rule 文本与图形多处碰撞。
- statistics contact sheet item-level decision 为 `BLOCKED`；Terra 明确判断该 deck 因核心 evidence page 不可读、页面破损及内部 fixture 语言，未达到成熟博士组会 paper-talk 标准。

**Minimal repair**

只把上述 identity-matched Terra blocking findings交给已经 shipped 的 038/Stage-4 bounded quality loop。允许每个 deck至多一次现有 mapping 支持的 source-faithful repair；不得人工改写 kidney 文案、手调 table crop、直接移动 TeX 坐标或新增 paper-specific分支。若现有 mapping 无法安全处理内部语言泄漏、figure/table scale 或碰撞，必须 no-winner / fail closed，而不是越权修 038。

**Required closure evidence**

- statistics frozen source-bundle SHA 保持 `32d1a9d1241ff8b4c77b6a98fe5b20b5b88ed04f3d60b0b10f9897304f15421b` 不变；production/shared/plugin code 无 holdout-driven修改；repair count 不超过 1。
- repair 后产生新的 render-input / rendered-pixel identities 与新 PDF/page/contact-sheet SHA。
- fresh task-local Terra 重新逐页审核最终像素：内部 fixture/workflow language 完全消失；workflow figure/caption、package comparison、closing reasoning page 均可投影阅读且无 overlap/clipping；statistics contact sheet item-level `PASS` 并明确达到 mature doctoral group-meeting / strong paper-talk bar。
- 若任一 blocking finding 在唯一一次 repair 后仍存在，则 statistics holdout 本轮失败并永久失去 unseen 资格，不得第二次修。

### 2. 医学 deck 的 architecture、limitations 与真实 CT comparison 三个核心页仍存在可见遮挡/碰撞

**Plan / regression boundary**

- medical deck 必须真实使用 MedSAM article 的许可图像并保持 prompt / expert annotation / prediction 语义，同时 scientific objects 必须清晰、无遮挡、可投影阅读。
- 两个 contact sheet 均必须 item-level `PASS`；top-level package success 不构成最终质量 PASS。
- 只允许既有 bounded quality loop 的一次自动 repair，不允许 fabricated medical pixels、手工 image edit 或 paper-specific layout patch。

**Observed evidence**

- Terra BF-05：medical slide 4 的 architecture figure 下方 citation 与 explanatory takeaway 明显重叠。
- Terra BF-06：medical slide 5 comparator labels、decision diamond、解释段落和底部结论发生多处碰撞。
- Terra BF-07：medical slide 6 的 `Overlay legend` 和 connector 直接压在 lower MedSAM crop 上，遮挡真实 medical-image evidence。
- medical contact sheet item-level decision 为 `BLOCKED`；Terra 明确认为 slides 4–6 的 overlap/obstruction 使整套 deck 未达到成熟博士组会 paper-talk bar，尽管真实 MedSAM 图像证据本身是有效的。

**Minimal repair**

同样只允许现有 bounded quality loop 消费这份 Terra finding 做至多一次自动 source-faithful repair。不得重绘/生成医学像素，不得人工剪补原图，不得手工改 `.tex`，也不得为 MedSAM 新增 layout special case。对无法由既有 mapping 安全解决的 legend placement / collision 必须 fail closed。

**Required closure evidence**

- medical frozen source-bundle SHA 保持 `fef82966184d4db938d4bfdd12101d289ebdca80bf246a3ed7c9fb72f42fa33b` 不变；真实 article pixels 与 attribution保持；repair count 不超过 1。
- repair 后新的 render identities / pixel SHA 与 task-local manifest严格绑定。
- fresh Terra 对 architecture、limitations、same-case CT comparison 逐项 `PASS`：caption/takeaway不重叠，decision/comparator区域可读，legend/connector不遮挡任何 medical-image crop；medical contact sheet item-level `PASS` 并明确达到成熟组会 paper-talk bar。
- 若唯一一次 repair 后仍有 blocker，则 medical holdout 本轮失败并永久失去 unseen 资格；不得再用同一 paper 调整后宣称最终 Stage 5 unseen PASS。

## Non-blocking notes

- 当前 evidence 证明真实科研内容并非完全失败：Terra确认 statistics deck 有真实 brms/Stan-specific notation 和 kidney-example evidence；medical deck 有真实 MedSAM medical-image segmentation panels，并保留 prompt/annotation/prediction 语义。当前主 blocker 是 production 在真实 paper 内容容量下的视觉适配与 audience-facing leakage，而不是“没有读取真实论文”。
- 两套 deck 当前各 5 个 substantive pages；Terra 本轮明确把 dominant cross-deck issue 判断为 undersized evidence 与 layout collisions，而非 subject coverage。因此本轮不额外扩大 scope 去要求固定页数或重写 storyline。
- 038 是首次真实 holdout 验证，fresh Terra 的失败本身是有效产品证据。后续不得通过修改 holdout source bundle 或手工修输出把这次失败历史抹掉。