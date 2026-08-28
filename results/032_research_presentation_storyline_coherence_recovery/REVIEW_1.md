---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 032_research_presentation_storyline_coherence_recovery
review_round: 1
decision: REVISE
implementation_commit: bbc71ae442940d2f43af954eee8f13b9e8648393
---

# 032 Storyline Coherence Recovery — Review 1

## Decision

`REVISE`

当前实现已经把这份 engineering bundle 的页面顺序和视觉过渡修到了可接受水平，但还没有满足冻结 Plan 对“通用、source-derived workstream grouping”的实现要求。真实 CI 已通过；fresh task-local Terra 也绑定当前 implementation/render identity，六个主要内容页全部 item-level `PASS`，其中 medical page 明确不再像插入主线的无关 benchmark 页。因此这轮不返修页面视觉，也不重做 031 已关闭的 CUHK identity、medical semantics、gold/layout 或 source-fidelity 能力。

唯一 blocker 是 production classifier 仍把当前 fixture 的两个 workstream 语义硬编码在共享生成器里。

## Blocking finding — workstream grouping 仍是当前 fixture 的 token profile，而不是通用 source-derived contract

### Plan basis

冻结 Plan 明确要求：

- workstream identity 来自 source/page-job information 或通用 workstream metadata；
- 不得把当前 fixture 的具体内容写成专用排序规则；
- deterministic regression 必须证明 grouping 基于通用 workstream metadata/evidence，而不是字符串 hardcode；
- 032 的产品价值是 normal production route 能处理“包含多个彼此独立 research workstream”的输入，而不仅是当前 clustered-calibration + segmentation bundle。

### Observed evidence

真实实现 diff 在共享 `generate_research_presentation_production_entry.py` 中新增了固定的 `WORKSTREAM_PROFILES`。当前仅有两个 profile：

- `clustered_interval_calibration`，依赖 `clustered / coverage / icc / cr2 / bootstrap / small-g ...` 等固定 token；
- `segmentation_robustness`，依赖 `medical / segmentation / lesion / gt / prediction / error / roi ...` 等固定 token。

`classify_workstream()` 先从 source/evidence 文本取 token，再与这两个固定 token 集求交并据此分组。当前 `storyline_trace.json` 也显示六页正是由这些固定 token 命中后被分成上述两个 workstream。

现有“source-derived”回归只把页面 `title` 和 `section` 改成 `Retitled page N`，但 source/evidence 中的 clustered/coverage/segmentation 等 token 完全没有变化，所以它只能证明“没有按标题硬编码”，不能证明“没有按当前 fixture 的内容字符串硬编码”。

这与冻结 Plan 要求的通用 workstream contract 不一致。如果下一份正常输入是例如“survival-model inference + genomics QC”或“two unrelated imaging subprojects”，当前 shared production classifier 没有对应 profile，就会退回 evidence-board/page-job fallback；它没有证据证明能够正确把一个 workstream 的 model/result/failure/next-step 连在一起。因此 032 目前只解决了当前 bundle，而没有证明 normal production behavior 已获得通用多-workstream grouping 能力。

### Minimal repair

只修这一层，不改变已经通过的页面设计和当前 storyline outcome：

1. 移除 shared production code 中针对 `clustered_interval_calibration` / `segmentation_robustness` 的 fixture-specific token profiles，或将它们移出通用分类逻辑，不允许作为 production classifier 的已知领域表。
2. 使用冻结 Plan 已允许的通用机制之一：
   - 优先消费 page-job/source ingestion 产生的通用 `workstream` metadata（id/label/scope/relationship），并让当前 engineering bundle 通过同一 schema 提供其 source-supported workstream；或
   - 使用不依赖当前两个领域词表的通用 evidence/source-anchor grouping 机制。
3. 保持单 workstream 输入向后兼容；没有 source-supported cross-workstream relation 时继续明确标为 independent，不虚构桥接。
4. 加一个真正能击穿当前 hardcode 的 deterministic regression：至少构造第二个与 clustered/segmentation 无关的双-workstream输入，或替换所有领域 token，仅保留通用 workstream metadata，然后证明两个 workstream 各自内部保持连续、第二 workstream 有 transition、单-workstream不插 divider。
5. 当前 engineering bundle 的最终顺序仍应保持：`STATISTICAL_MODEL -> REAL_DATA_APPLICATION -> EXPERIMENT_DESIGN -> NEGATIVE_RESULT -> NEXT_EXPERIMENT -> MEDICAL_IMAGE_COMPARISON`；现有六页科学内容、gold选择、Stage 3 layouts、CUHK identity、medical overlays 不得无关修改。
6. 重新生成 032 artifacts，运行 required tests/validation/真实 CI。若 audience-facing transition pixels 或页面 identity 变化，必须重新获得 fresh task-local Terra evidence；不得复用旧 identity 的视觉结论。

## Evidence already accepted and frozen

- 真实 `Codex Marketplace` CI run 对 032 handoff 成功。
- fresh `VISUAL_REVIEW.json` 与 implementation `bbc71ae...`、当前 PDF 和六张 PNG identity 一致。
- 六个主要内容页均 item-level `PASS`；coverage workstream 已连续，medical page 已作为明确独立 workstream 出现在末尾。
- Terra 明确确认 medical transition 可见且没有因 deck coherence 被判 `REVISE`。
- normal production entry、source-fidelity map、normal gold selector/recipe、Stage 3 layout consumption、exact CUHK identity、medical TP/FP/FN semantics 与 anti-meta leakage 未发现新的 blocker。

因此本轮只允许修 workstream grouping 的通用性证据，不应重新设计页面或扩大到 deck-rhythm / bounded repair loop。
