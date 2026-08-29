---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 039_research_presentation_quality_loop_execution_recovery
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

把 Stage 4 已有的“视觉审查 → 最多一次自动修复 → 重新渲染 → 再审查”从部分工程示例机制补成真实可执行的通用闭环。038 已经证明正常 production entry 能生成真实论文 deck，也证明当前 quality-loop consumer 在真实 Terra finding 缺少 `repair_intent` 时会安全停止；但它同时暴露两处工程缺口：一是没有从现有结构化 finding 安全归一到有限 repair family 的适配层，二是部分已声明 repair intent 并没有真正的 layout/render consumer。

039 只修这两个相互依赖的通用缺口。它不修 038 的具体 deck，不读取 038 paper assets 作为测试样例，不重做 Stage 5，也不降低成熟组会视觉门槛。完成后，下一次新的 unseen paper 若出现同类可机械修复问题，系统应能在同一次 one-call 的唯一 repair cycle 内真实改变像素；遇到未知/歧义问题仍然 no-winner。

## Frozen decisions

- 继续沿用当前 `RESEARCH_PRESENTATION_DECK_QUALITY_LOOP_STATE_V1`、task-local Visual Review evidence contract、`MAX_REPAIR_CYCLES=1` 与 `QUALITY_LOOP_FAIL_NO_WINNER`。不得新增第二套 review/repair 状态机。
- 038 的 brms/MedSAM 论文、figure/table/image、DOI、标题、具体页面文案和最终像素不得进入 039 fixture/gold/rule/tuning。可以读取 038 REVIEW/FINAL_REPORT 中抽象 blocker class，但不能复制 holdout 内容做回归。
- finding 没有显式 `repair_intent` 时，只能依据结构化字段做有限归一：至少使用 `requirement_id`、target `item_id`/page logical id、对应 page job/spec 的 content kind/dominant object，以及 finding 自身已有 summary/evidence/recommendation。只有这些信息能唯一指向安全修复时才生成 directive；否则继续 fail closed。
- 优先复用现有 intents：`RESCALE_PRIMARY_OBJECT`、`REPAIR_ANNOTATION_LEGEND`、`SWAP_COMPATIBLE_GOLD_LAYOUT`、`SPLIT_OVERDENSE_PAGE`、`ADJUST_TRANSITION_CUE` 等。只允许新增一个窄范围 audience-copy intent（若现有 intent 无法准确表达），其唯一作用是去除 audience-facing internal/meta 制作语言并回落到同页已有 source-grounded copy；不得生成新科学 claim。
- `RESCALE_PRIMARY_OBJECT`、`REPAIR_ANNOTATION_LEGEND`、`SWAP_COMPATIBLE_GOLD_LAYOUT`、`SPLIT_OVERDENSE_PAGE` 等只要被选中，就必须有真实 production consumer，最终对 render-input identity / pixels 产生可观察变化；禁止仅在 JSON spec/state 写 hint 后就声称 repair 已执行。
- 对 figure/table/medical-image 等科学对象，repair 只能调整 scale、reserved support band、legend/callout 位置、compatible composition 或必要时 split；不得改变 source evidence 的科学含义。
- medical-image repair 禁止生成、重绘、涂改 source pixels、mask 或 segmentation。若安全布局放不下，必须换 compatible layout / split / no-winner，而不是遮挡图像或缩到不可读。
- audience-copy repair 只能使用当前 page job 已有的 `key_message`、annotation、caption、scientific objects 或明确 source anchors 作为 replacement source；如果清除 internal phrase 后没有无歧义、source-grounded replacement，必须 fail closed。
- shared skill source 与 `plugins/codex` mirror 必须保持 parity。
- 039 的视觉验证只能用 non-holdout regression/stress bundle；禁止把 038 失败输出“修到通过”作为 acceptance evidence。
- 039 PASS 不等于 Stage 5 PASS。通过后 Planner 仍需挑选新的 unseen statistics/methodology 与 medical-imaging paper 再做完整 one-shot。

## Implementation scope

1. **Visual finding normalizer in the existing quality-loop consumer**
   - 修改 shared `skills/tools/documents-media/presentations/shared/scripts/deck_quality_loop.py` 及 marketplace mirror。
   - 在 `map_finding_to_directive()` 之前加入一个最小、确定性的 normalization step：显式 intent 仍优先；缺 intent 时仅对已冻结的安全 blocker classes 推导 intent。
   - 至少覆盖：
     - audience-facing internal/meta copy → narrow audience-copy sanitization；
     - figure/caption/supporting-copy collision → compatible annotation/support-band repair；
     - undersized primary figure/table → `RESCALE_PRIMARY_OBJECT`，若已有 capacity signal 明确 `SPLIT_REQUIRED` 才可 `SPLIT_OVERDENSE_PAGE`；
     - process/next-step diagram collision → `SWAP_COMPATIBLE_GOLD_LAYOUT` 或已有可证明 source-faithful 的 compatible reflow；
     - medical legend/callout obstruction → `REPAIR_ANNOTATION_LEGEND`。
   - 任何 requirement/page combination 不能唯一映射时继续返回 unsafe mapping；不得靠模糊关键词把所有 Terra recommendation 自动变成 repair。

2. **Make selected directives executable**
   - 在 normal production path 中补齐 selected directive 的实际消费者。优先在现有 stage3 layout/spec emitter 与 production entry 的已有 hook 内完成，不新建平行 renderer。
   - `RESCALE_PRIMARY_OBJECT`：必须真正改变 scientific object geometry，并同时保留 caption/annotation 可读空间；不能只把 object 放大到覆盖其他内容。
   - `REPAIR_ANNOTATION_LEGEND`：必须为 annotation/legend/citation 提供不遮挡主科学对象的 reserved region 或 compatible placement；medical panels 的 legend 不得进入任何 image crop。
   - `SWAP_COMPATIBLE_GOLD_LAYOUT`：如果采用，必须通过正常 gold compatibility/score contract 选择另一个 compatible composition；不得直接按 page title/test id 指定 gold。
   - `SPLIT_OVERDENSE_PAGE`：只有现有 capacity check 已给 `SPLIT_REQUIRED` 时才可执行；split 后 source dependency、page order、citation 与 evidence trace 必须保持。
   - narrow audience-copy sanitization：只修改 audience-facing rendered copy，不改 source bundle；replacement 必须来自同页已有 source-grounded字段，并把 original/internal string 保留在 internal trace（若现有 trace 已支持）而不是 slide body。
   - repair 后必须重新执行正常 gold/layout/render/contact-sheet/identity 链；`repair_cycle_count` 只能从 0 到 1。

3. **Non-holdout stress regression**
   - 新增或扩展一个与 038 完全无关的 task-local/non-holdout regression bundle，至少产生五类真实 render stress：
     1. annotation 中包含 internal/meta 制作短语，但同页有安全 source-grounded replacement；
     2. paper-style figure + caption + takeaway 在底部会碰撞；
     3. 高密度 table/primary object 在普通布局中过小；
     4. process/next-step diagram 在默认 compatible layout 中发生 label/text collision；
     5. medical-image comparison 的 legend/callout 会遮挡 panel。
   - stress fixture 可以使用 synthetic/public-safe内容，但不得出现 038 论文 title/DOI/figure/table/image/专有对象。
   - 同时保留一个 unknown/ambiguous blocker fixture，证明缺少唯一安全映射时仍 `QUALITY_LOOP_FAIL_NO_WINNER`。

4. **Pixel-effect and identity evidence**
   - 对每个可修类别保存 repair 前后 `quality_loop_state`、render-input identity、rendered-pixel identity、关键 page SHA/contact-sheet SHA。
   - acceptance 不能只断言 directive 被 selected；必须证明 target page 的实际 render-input 或 pixel identity 因 repair 改变，且 source bundle SHA 不变。
   - 若某 intent 被选择但前后 render identity/pixel 无变化，该 intent 视为未实现，039 不得 PASS。

5. **Fresh task-local Visual Review**
   - 039 使用现有 Bridge Kit task-local manifest/evidence contract；缺 fresh evidence 时等待，不消耗 review round。
   - manifest 至少包含 repair 后五类 stress pages 与整套 contact sheet，并绑定 implementation/render identities。
   - Terra 必须逐项判断：内部制作语言已从 audience body 消失；figure/table/diagram/legend 无 overlap/clipping/obstruction；主科学对象可投影阅读；medical pixels未被修改；contact sheet 达到 mature doctoral group-meeting / strong paper-talk bar。

6. **Regression and parity**
   - 跑现有 research-presentation production/quality-loop/unit tests，并新增针对 normalization、actual pixel-effect、unknown fail-closed、一轮 repair budget 的回归。
   - shared 与 plugin mirror 保持一致；normal no-review path、already-PASS visual path、unknown/unsafe path不得回归。

## Acceptance and regression gates

039 只有在以下全部成立时才可以 PASS：

- 真正的 038 holdout内容没有被作为 fixture/gold/rule/tuning输入；代码/测试中不得出现 brms/MedSAM title、DOI、figure/table filename 或其特定 scientific wording 作为分支键；
- 真实 Terra-style finding 缺 `repair_intent` 时，五类冻结 blocker中可唯一安全映射的类别能得到确定 repair directive；unknown/ambiguous类别仍 fail closed；
- selected repair directive 对 target production render 有实际 effect：至少 render-input identity 变化，且有 render 时 target pixel SHA/rendered-pixel identity随之变化；
- audience internal/meta copy 被替换为同页已有 source-grounded audience copy，没有新增科学 claim；
- figure/caption/supporting copy 不重叠，table/primary object 达到投影可读尺度，process/next-step diagram 不碰撞，medical legend/callout 不遮挡 image panel；
- medical source pixels与 source asset SHA保持不变；exact CUHK identity、source-fidelity map、gold/reference trace、one-repair budget全部保留；
- source bundle SHA 在 repair 前后不变；不得通过改 input 来实现 repair；
- non-holdout stress fixture 的 fresh task-local Terra 对所有目标 pages 与 contact sheet item-level `PASS`，并明确达到 mature research-group-meeting / strong paper-talk bar；
- 真实 GitHub CI PASS；shared/plugin parity PASS；现有 production/quality-loop regression PASS；
- 任何无法安全修的 finding 仍 no-winner，不得为追求视觉 PASS 放宽 fail-closed contract。

停止条件：039 最多两轮 Reviewer review。若在该范围内不能取得“安全 mapping + actual pixel effect + fresh Terra PASS”的新增证据，保留失败历史，不继续重复同一 mapping/repair动作；Planner 再判断是否出现新的架构级或真正需要用户决定的问题。

## Natural-language usage / routing expectations

完成后，用户仍只需要普通地说“把这篇论文做成组会汇报”。如果第一次渲染出现一个系统能无歧义识别的可修视觉问题，例如原始图太小、caption 与 takeaway 挤在一起、医学图例挡住图像或 audience body 泄漏制作型说明，系统可以在同一次 one-call 中用唯一一次 repair 自动换尺度/布局/annotation placement，并重新生成真正不同的像素再审查。

如果审查意见过于笼统，或修复可能改变科学 claim、医学像素、来源关系，系统仍会停止并 no-winner，而不是自动猜测。

## Out of scope

- 不重跑或修复 038 的 brms/MedSAM deck，不把它们重新判为 unseen。
- 不选择下一组 Stage-5 holdout paper；039 PASS 后由 Planner另开 evaluation task。
- 不扩 reference/gold corpus，不新增外部付费/许可不明素材。
- 不重做 Stage 1–4 storyline、CUHK template、render identity、source-fidelity、gold retrieval 等已通过机制。
- 不增加第二个 repair cycle，不做无限 auto-layout search。
- 不新建新的 Visual Review schema/state machine，不改变 Reviewed Handoff review limit。
- 不通过缩小字号、删除必要科学证据、生成医学像素或降低 Terra mature bar 来换取 PASS。
