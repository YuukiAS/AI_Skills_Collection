---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 026_research_presentation_discussion_next_experiment_gold_recovery
review_round: 1
decision: REVISE
implementation_commit: 45ac2a0647fb9a486ba47f64bed300c3e09f4c73
---

# 026 Discussion / Next-Experiment Gold Recovery — Review 1

## Decision

`REVISE`

026 的业务能力已经满足冻结 Plan 的核心要求：真实 CI 已通过；第二批 Terra 对真实 rendered pixels 的 `item_C` 给出 item-level `PASS`，identity map 将其绑定到 `RRL-059 / SRC-077 / page 51`；`GSC-018` 以 `COMPOSITION_ONLY` 权限边界进入现有 gold schema；正常 selector 能选择它，recipe builder 实际消费 source-derived geometry / hierarchy / reading-flow 等字段，移除该 record 后得到 `no compatible gold composition record`，因此 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` 成立。025 的既有 9 条 gold 也未被重审或替换。

当前只剩一个很小但属于冻结 Acceptance Gate 11 的报告一致性 blocker，不需要重新做 Terra、scouting、gold admission 或 runtime implementation。

## Blocking finding — RESULT 的搜索范围计数自相矛盾

### Plan basis

冻结 Plan 的 Acceptance Gate 11 要求 `RESULT` 明确列出实际搜索范围、admitted/rejected candidates、Terra item decisions、rights notes 与 runtime evidence；Frozen recovery boundaries 同时限制最多 8 个 source URLs、4 个 decks、12 个 Terra pages、2 个 admission packets。

### Observed evidence

当前 `RESULT.md` 同时写道：

- 共检查 4 个 source URLs，其中 1 个 Google Drive PDF fetch 失败且“was not intaken”；
- 共 intake/render 4 个 public decks。

这两个数字不能同时成立。实际 tracked source registry 本轮只新增并标记为 `downloaded_inspected` 的三个 source：`SRC-075`、`SRC-076`、`SRC-077`；两个 identity map 也分别来自前两套 deck 与 Zi Wang deck，合计 12 个 Terra pages。由现有 evidence 看，最一致的搜索账本应是“4 个 URL 被检查，其中 1 个失败未 intake；3 个 deck 实际 intake/render；12 页 Terra；2 个 packets”。

### Why blocking

这不影响已建立的 gold 能力，但 026 本身就是一个严格有界的外部 source recovery；如果最终报告对实际资源消耗计数不准确，就无法可靠证明没有越过冻结搜索边界，也不满足 Plan 对搜索范围报告的明确要求。

### Minimal repair

只修正 `results/026_research_presentation_discussion_next_experiment_gold_recovery/RESULT.md` 的搜索范围计数，使其与真实 source registry / identity maps 一致；如果 Executor 能证明实际确有第四个成功 intake/render 的 deck，则必须在 RESULT 中明确列出该 source 及其 provenance，而不能只保留冲突数字。

不得修改：

- `GSC-018` 及现有 10 条 gold；
- Terra evidence / identity map；
- selector / recipe builder / runtime probe 语义；
- 025 历史；
- Stage 3 实现；
- source corpus 的进一步扩张。

修正后重新交 handoff，并保持 required CI / validation 为 PASS 即可。无需重新 scouting 或重新跑 Terra，除非真实文件发生了会改变视觉 identity 的修改。

## Non-blocking evidence already accepted

- `item_C` 的 026 Terra item-level `PASS` 与 `RRL-059` identity binding 一致；
- `GSC-018` 的 reviewer-input SHA、canonical rendered-page SHA、rights boundary 与 source identity 齐全；
- discussion / next-experiment runtime probe 使用正常 selector，无 force-id / score override，并实际消费 gold composition fields；
- handoff tip `6dd72a7e50726e2f9222bf8aac50f12f6b27ef04` 的 `reviewed-handoff/ci-summary` 为 `success`。
