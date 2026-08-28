---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 034_research_presentation_render_identity_ci_recovery
review_round: 1
decision: REVISE
implementation_commit: 68cc193ec09d29617a8f2642dac49615a0c5df76
---

# GPT Review

## Decision

REVISE。

034 原本要关闭的 render-input identity / rendered-pixel identity CI 缝隙已经实质关闭：真实 GitHub CI 已通过，当前 production representation 在有真实 render 时同时绑定 render-input 与 pixel identity，在无 render 时允许 pixel evidence 明确不可用；implementation diff 也确实把 `main.tex`、`scientific_layouts.tex`、直接科学资产和 canonical CUHK source 纳入稳定 render-input identity，而不是继续用缺失 PNG 冒充稳定像素身份。

但 034 的冻结 Plan 同时要求 fresh task-local deck/contact-sheet 视觉证据达到既有 Stage 4 mature bar，且不得回归 anti-meta leakage。当前 fresh Visual Review 与当前 implementation、PDF、六张内容页和 contact sheet 身份一致，逐页结果显示 slide 3–7 继续 PASS，但 `slide_2_statistical_model` 为 REVISE，`deck_contact_sheet` 为 BLOCKED，并给出两个 blocking findings。两个 finding 都能由当前真实 audience-facing `main.tex` / production source 独立复核，因此不能把 Terra top-level package 或 CI success 当作质量 PASS。

本轮不需要 human decision，也不需要 Plan revision。只允许关闭下面两个已观察到的视觉 blocker；不得借机改写 deck-quality loop、Stage 2 gold bar、Stage 3 layout system、storyline、医学影像语义或增加第二个 automatic repair cycle。

## Blocking findings

### 1. Audience-facing title slide 泄露工程/工作流语言

**Frozen boundary**

033/034 延续的 Stage 4 质量合同要求 audience-facing deck 不出现 provenance / workflow / implementation 元语言；034 只有在 fresh deck/contact-sheet evidence 无 blocking finding 且既有 anti-meta leakage 能力无回归时才可 PASS。

**Observed evidence**

Fresh Terra 在 `deck_contact_sheet` 给出 `BF-01`：标题页副标题直接显示 `One-call production regression from source bundle to exact CUHK deck.`。当前真实 `main.tex` 也逐字包含该 subtitle；其来源是 normal production bundle 的 `metadata.subtitle`，不是 Terra 猜测或截图误读。现有 mechanical validator 会检查 audience-facing TeX 的一组 forbidden terms，但当前这类 `production regression` / `source bundle` 工程措辞没有被挡住。

**Minimal repair**

只修 audience-facing metadata 这一条链：

- 让 Stage 4 engineering bundle 的标题页 metadata 变成研究听众可见的 study/research description，而不是工程回归描述；内容必须与现有 source title/model/results 语义一致。
- 同时补一个小而通用的 anti-meta regression，使正常 production 的 title/subtitle 也受 audience-facing meta-leak policy 约束；不要按当前完整 subtitle、当前 fixture title、页号或 task key 写死。
- 不要通过删除全部 subtitle、统一替换成空泛 `Research update`、或对任意用户研究文本做大范围重写来“过测试”。目标只是阻止明显 production/source-bundle/workflow 元语言进入观众页。
- shared / plugin mirror 若受影响必须保持一致。

**Required closure evidence**

- 新 `main.tex` 与真实标题页像素不再出现上述工程/工作流措辞，并保留 source-specific research title/description。
- 有 regression 证明 title/subtitle 中注入明显 internal production/provenance language 会被 normal validation 拒绝或在进入 audience-facing TeX 前安全处理。
- 重新真实 render，并取得绑定新 implementation / PDF / contact-sheet identity 的 fresh task-local Visual Review；`deck_contact_sheet` 不再因 title leakage 阻塞。

### 2. Statistical-model page 明显欠填充，破坏整套 deck 的成熟节奏

**Frozen boundary**

033 的 deck-level mature bar 明确拒绝过空页面和相邻页不合理的信息密度跳变；034 保留该 bar，并要求 fresh item/page-level + contact-sheet evidence 无 blocker。

**Observed evidence**

Fresh Terra 的 `BF-02` 与 `slide_2_statistical_model` item review 都指出：当前模型页只有一个居中的混合模型公式和一条解释句，页面大面积留白，作为完整博士组会页面明显未完成。这个判断可以从真实 `main.tex` 独立复核：该 frame 只有两个 `StageThreeNode`，即公式与 ICC/cluster-count annotation；没有其他 supporting scientific object。与此同时，production bundle 已经提供 source-grounded `key_message` 和 `scientific_objects`（clustered outcome equation / center random effect / individual error），但 normal production `build_specs` 当前没有把这些 supporting fields 带入最终 spec，`deck_sequence_summary` 中该页的 `scientific_objects` 也因此为空。这说明 blocker 不是要求凭空增加内容，而是已有 source-supported explanation 没有进入最终页面。

**Minimal repair**

在不改 Stage 2 gold mature bar、不 force gold ID、不重写 Stage 3 layout system的前提下，让 normal `STATISTICAL_MODEL` production path 能利用已经存在的 source-grounded supporting information，形成一个完整但仍以公式为主对象的模型页。允许的最小形态包括：紧凑的变量/方差成分解释、模型结构小示意、或等价的 source-specific supporting block；必须满足：

- 只消费现有 page-job/source evidence 支持的内容，例如 center variation、individual variation、ICC 与 interval calibration 关系；不得新造 source 不支持的统计结论、变量或比较结果。
- 解决方案应由通用 production fields 驱动（如 `key_message` / `scientific_objects` /已有 annotation 等），不能按当前 clustered fixture 的标题、术语、页号或 GSC ID 写死。
- 方程继续是主科学对象且投影可读；修复目标是补足解释层次与版面平衡，不是把页面塞满文本。
- 当前 selector/recipe/layout trace、CUHK identity、后续 result/design/failure/next-experiment/medical 页面已通过的形态全部保护。

**Required closure evidence**

- source-fidelity / runtime trace 能证明新增 supporting content 来自现有模型 source/page-job fields，而非手写 fixture-specific bypass。
- 新 `main.tex` / render-input identity 和模型页 pixel identity 随修复真实变化；模型页不再只有公式+单句两对象的欠填充构图。
- 重新运行 targeted/full tests、production validator、skills/marketplace/Reviewed Handoff validation 与真实 GitHub CI。
- 取得 fresh item-level Terra：`slide_2_statistical_model` 达到 mature bar，`deck_contact_sheet` 无 density/rhythm blocker；同时 slide 3–7、workstream continuity、CUHK identity 与 medical TP/FP/FN semantics 不回归。

## Non-blocking notes

- 034 的核心 identity recovery 本身当前没有发现新的 blocker：render-input identity 与 rendered-pixel identity 已分层，真实 render 时 pixel evidence 为 AVAILABLE，当前 manifest 也绑定了实际 `main.tex`、scientific layout、资产、PDF、六张页面与 contact sheet。
- Fresh Terra 对 `slide_3_real_data_application`、`slide_4_experiment_design`、`slide_5_negative_result`、`slide_6_next_experiment`、`slide_7_medical_image_comparison` 均为 PASS；CUHK identity、结果→失败→下一实验节奏、独立 medical workstream transition 和 TP/FP/FN 语义均得到正向观察。返修不得无关重做这些页面。
- 当前 Terra finding 没有提供既有 bounded quality-loop 所要求的受支持 `repair_intent`。不要为了自动吞掉这两个 finding 而放宽 unknown-finding fail-closed 规则；本轮是 Reviewed Handoff 的一次明确、有限 implementation repair，automatic repair cap 仍保持 1。
