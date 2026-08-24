---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 025_research_presentation_gold_scientific_composition_library
review_round: 1
decision: REVISE
implementation_commit: a58104329cb4c05ddef777812c1738c3d4c510ca
---

# 025 Gold Scientific Composition Library — Review 1

## Decision

`REVISE`

本轮实现已经建立了有价值的 Stage 2 骨架：10 条 gold composition records、独立 selector、renderer-neutral recipe builder、source/plugin mirror 与真实 CI 都已成立；recipe builder 也确实读取 `primary_bbox`、visual hierarchy、alignment、reading flow、annotation/panel relations 和 content capacity，而不是只返回一个 reference ID。

但当前还不能判 Stage 2 PASS，因为冻结 Plan 的两个核心证据门槛没有真正满足。

## Blocking finding 1 — 10 条 gold records 并未全部获得真实像素级成熟度准入证据

### Plan basis

PLAN §3 和 Acceptance Gate 3–4 明确要求：每个拟进入 gold set 的页面必须基于真实 rendered pixels 做成熟度判断；只有 021/022 中已有明确 item-level mature-bar judgement 的页面可以直接复用，否则必须用现有 Bridge Kit / `gpt-5.6-terra` 做 bounded gold-admission visual packet。不能用 RRL prose、019 composition record 或 metadata 代替像素级准入。

### Observed evidence

当前 `research_gold_composition_index.json` 有 10 条记录，但多条记录的 `gold_admission_evidence` 只引用 `research_slide_composition_index.json` 或 `research_slide_reference_index.csv`，并用 `REFERENCE_ACCEPTED` / `REFERENCE_ADMITTED_WITH_LIMITATION` 之类本任务自定义标签描述成熟度；这些路径本身不是 item-level pixel reviewer judgement。

例如：

- `GSC-001 / RRL-001` 的 evidence 只指向 `research_slide_reference_index.csv`；
- `GSC-004 / RRL-019` 和 `GSC-005 / RRL-030` 只以 019 composition record 作为成熟度依据；
- `GSC-003 / RRL-014` 虽引用 021/022 materialization identity，但没有给出该 reference item 的明确 mature-bar item-level judgement。

与此同时，`gold_admission_report.json` 的 `admitted_gold_ids` 实际只有 `GSC-002` 与 `GSC-007`，因为该字段是从两个 runtime probe 的 baseline selection 自动生成的，而不是 10 条 gold records 的真实准入清单。这与 RESULT 所称“gold index contains 10 records”以及 admission report 的职责不一致。

### Why blocking

如果没有真实像素级准入，Stage 2 仍然可能把“结构化过的普通 inspected page”误当 production gold。Stage 3 随后会把这些未经成熟度验证的构图固化成 CUHK executable layouts，直接违背本阶段存在的目的。

### Minimal required repair

只在现有 corpus 内修复，不扩 source：

1. 逐条审计 10 条 gold record 的现有 021/022 item-level pixel evidence；只有确实存在明确 mature-bar judgement 的记录可直接保留该 evidence。
2. 对其余拟保留记录，使用现有 Bridge Kit / `gpt-5.6-terra` 做一次 bounded gold-admission packet，输入必须是真实 reference render，并保存 item-level decision/observation 与实际 reviewer-input SHA。
3. item-level 明显低于 mature research-group-meeting bar 的页面从 gold set 移除或降回普通 inspected reference；不得为了覆盖强行保留。
4. 重写 `gold_admission_report.json`，明确列出全部 admitted gold IDs、逐条 evidence source、被拒绝/降级候选及原因；不要再把两个 runtime baseline IDs 冒充整套 admission list。
5. index 中每条保留 gold record 的 `gold_admission_review_input_sha256`、maturity evidence 与 report 必须一致可追溯。

### Closure evidence required

新的 admission report + 真实 item-level Terra/既有 comparative evidence + identity binding；validator/tests 应阻止 metadata-only gold admission。

## Blocking finding 2 — statistics runtime probe 通过 `force_gold_id` 绕过兼容性门槛，不能证明“替换为另一 compatible gold record”

### Plan basis

PLAN §5 与 Acceptance Gate 5、8 明确要求：相同 scientific content 下替换为**另一 compatible gold record**或屏蔽当前 record，产生可解释 recipe 差异；不允许 test-specific hardcode，也不能绕过 selector 的 semantic compatibility gate。

### Observed evidence

`generate_gold_composition_probe_artifacts.py` 的 statistics probe 查询为：

- `page_function = ESTIMATOR`
- `domain_family = statistics`
- dominant object = equation

baseline 由 selector 正常选择 `GSC-002`，但 alternate 被硬编码为 `GSC-003`，并通过 `build_recipe(..., force_gold_id="GSC-003")` 强制进入 recipe。

`build_gold_composition_recipe.py` 的 `force_gold_id` 路径不会调用 `score_record` / semantic compatibility gate，而是直接构造 `score=999`、`compatibility_reasons=["forced compatible probe"]`。但 `GSC-003` 的 `domain_families` 是 `biostatistics` / `medical_imaging`，并不包含 statistics；按正常 selector 逻辑，对该 statistics query 会产生 `domain_family mismatch`。

因此当前 probe 证明的只是“强行换成另一条 record 后 hash/bbox 会变”，没有证明“兼容替换会改变 source-derived recipe”。

### Why blocking

这是 025 最核心的 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` 回归之一。如果 alternate 可以绕过 compatibility gate，测试可以在任何两条不相关 record 之间制造 recipe 差异，不能证明 production retrieval 真正工作。

### Minimal required repair

1. 删除 probe 中绕过语义兼容的 `force_gold_id` 证明方式，或者让 force path 本身先执行与正常 selector 相同的 compatibility validation，只有兼容时才允许。
2. statistics 和 medical 两个 probe 都必须由实际兼容候选产生 alternate；可以屏蔽 baseline 后让 selector 选择下一条兼容记录，或显式选择一条经 selector 验证兼容的 record。
3. trace 中保存 baseline/alternate 的真实 compatibility reasons 和 exclusion evidence。
4. tests 必须证明若指定不兼容 alternate，probe/recipe 会拒绝，而不是生成 `score=999` 的伪兼容结果。

### Closure evidence required

重新生成的 runtime probe traces 应显示两个领域都由正常兼容门槛选择/验证 alternate，且 source-derived bbox/hierarchy/relations 的改变导致 recipe 可解释变化。

## Non-blocking observations

- 真实 CI `reviewed-handoff/ci-summary` 已通过；本轮没有 CI blocker。
- source/plugin mirror、gold schema/validator、selector、recipe builder 和 audience-safe meta boundary 的总体方向符合 Stage 2。
- 当前没有发现扩 corpus、修改 canonical CUHK、恢复 023 或提前实现 Stage 3/holdout 的 scope creep。

返修只应关闭上述两个 blocker，不要借机实现 Stage 3 renderer 或扩展 corpus。
