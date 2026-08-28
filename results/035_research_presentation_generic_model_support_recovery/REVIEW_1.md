---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 035_research_presentation_generic_model_support_recovery
review_round: 1
decision: REVISE
implementation_commit: 5501edce262254547bbcefbe04a0827172a73861
---

# GPT Review

## Decision

REVISE。

035 的核心 generic-model source-grounding blocker 已经由真实代码与回归证据关闭：共享 `STATISTICAL_MODEL` renderer 不再无条件输出 `Calibration link`、固定 ICC / center-variation / interval-comparison caption 或 `Source-grounded terms` fallback；模型 supporting blocks 只从当前 spec 的 `scientific_objects`、`key_message` 和可选 `caption` 读取科学内容，中性布局标签为 `Model components` / `Interpretation`。新增 Cox regression 真实经过同一 shared model path，并证明非 clustered 模型不会泄露当前 engineering fixture 的科学语义。shared/plugin mirror 对应改动一致，真实 GitHub `Codex Marketplace` CI 已通过。

fresh task-local Terra 也与 implementation `5501edce...`、当前 render-input identity、rendered-pixel identity 和 contact sheet 一致；`slide_2_statistical_model` 本身 item-level PASS，明确确认公式仍为主科学对象、supporting explanation 可读、CUHK identity 正常且没有内部制作语言泄漏。

但 035 的 frozen acceptance gate 还明确要求：当前 pixels 变化时，`slide_2_statistical_model` **与** `deck_contact_sheet` 都必须取得 fresh item-level PASS。当前 `deck_contact_sheet` 是 `REVISE`，因此 Planner 不能把 035 标成 PASS。Terra 指出的主要 deck-level 差距是：新的模型页比相邻结果页明显更疏，而下一实验页仍较密，导致整套 deck 的密度节奏不够均衡。

这里需要严格区分“035 引入的变化”和“既有页面的新审查意见”。`slide_6_next_experiment` 当前也被 Terra 判为 `REVISE`，但它的 PNG SHA-256 与 034 已经 item-level PASS 的上一版完全相同（均为 `0fc4574e...`）。因此这不是 035 implementation 对 slide 6 造成的 regression，也不能据此突破 frozen scope 去重做 slide 3–7。第一轮返修只允许处理 035 范围内、确实发生变化的模型页密度与版面利用；如果在模型页完成最小重平衡后，fresh Terra 仍因为完全未变化的 slide 6 阻止 contact-sheet PASS，Executor 应保留证据并进入 `NEEDS_GPT_PLANNER`，而不是擅自修改冻结的下一实验布局。

## Blocking findings

### 1. Fresh deck-level visual gate 未通过：模型页改为 source-driven 后，整套 deck 的密度节奏出现可见不均衡

**Plan / regression boundary**

035 Plan 的 acceptance gate 5 要求当前 engineering model page 保持完整、公式主导、source-faithful；gate 7 冻结 slide 3–7 的既有行为；gate 10 则要求 pixels 改变后 `slide_2_statistical_model` 与 `deck_contact_sheet` fresh item-level PASS。035 不允许为了视觉填充重新引入无来源 supporting copy。

**Observed evidence**

- 当前 shared renderer 的 model support 已改为 source-driven，`slide_2_statistical_model` fresh Terra 为 PASS。
- 当前 model page 的实际 TeX 只展示来源已有的 mixed-effects 公式、ICC 解释、三个 `scientific_objects` 与 source-backed `key_message`，没有旧的固定 ICC caption 或制作语言。
- fresh Terra 对 `deck_contact_sheet` 给出 `REVISE`：主要观察是 slide 2 相比 slide 3 更开放，而 slide 6 信息更密，形成明显 density jump。
- fresh Terra 对 slide 6 的小字号提出 `REVISE`，但当前 slide 6 PNG 与 034 fresh Terra PASS 时的 PNG SHA 完全一致，证明 035 没有修改该页面。

**Minimal repair**

只在现有 `STATISTICAL_MODEL` source-driven layout/emission 范围内做一次最小视觉重平衡，不新增任何科学文案、不恢复 fixture hardcode，也不修改 slide 3–7：

- 保持公式为第一视觉主对象，但可以利用现有空白适度放大公式、annotation、`Model components` / `Interpretation` 两个 source-backed blocks，或调整它们的纵向分布与区域占比；
- supporting content 仍只能来自当前 `scientific_objects`、`key_message`、`annotation`、显式 `caption` 等 source-backed fields；缺字段时仍宁可留白，不能生成泛化/制作型填充文案；
- 不修改 `NEXT_EXPERIMENT` renderer、slide 6 文案、032 storyline、gold selection、medical semantics、deck-quality-loop 状态机或一次 repair budget；
- unrelated Cox regression 与 minimal-spec no-fallback regression 必须继续通过，防止为填满页面重新引入 domain hardcode。

如果上述 in-scope model-page rebalancing 后，fresh Terra 的 model page 与 contact sheet 均 PASS，则 blocker 关闭。若 model page PASS、但 contact sheet 仍只因 unchanged slide 6 被判 REVISE，则不要越界修改 slide 6；记录 current/previous pixel identity 与 item decisions并交回 Planner 路由。

**Required closure evidence**

- targeted unrelated-model regression、full presentation tests、shared/plugin parity 与真实 GitHub CI 继续 PASS；
- fresh task-local manifest 绑定新的 implementation/render identities；
- `slide_2_statistical_model` item-level PASS，且 supporting copy 仍全部 source-backed / neutral-label；
- `deck_contact_sheet` item-level PASS；
- slide 3–7 的 source/production behavior 无 035 引起的无关变化；若 Terra 对 unchanged slide 6 仍有独立意见，必须通过 SHA/identity 明确证明其不是本轮 regression，而不是在 035 内偷偷扩 scope。

## Non-blocking notes

- 035 的原始科学语义 blocker 已真实关闭。代码级证据和 Cox regression 都支持这一点，不需要再次重写 source-grounding mechanism。
- 当前 slide 6 的审查分歧属于相同像素在 034 与 035 两次 Terra 中的判断差异：034 为 PASS、035 为 REVISE。由于像素 SHA 相同，本轮不把它误报为 Executor regression。
- fresh Terra 仍认可整套 deck 的 CUHK identity、第一 workstream 的 model → result → design → failure → next experiment 连续性、独立 segmentation transition，以及不同 scientific-object 类型之间的构图变化；没有发现 generic-card 模板脸或内部 workflow 元语言回归。
