# 011 Round Handoff — Planner Review

reviewed_commit: `846e3d96c2037e3efc1bb9e325f61ea8097ae32d`
review_round: 1
decision: REVISE

## 结论

本轮已经修掉上一版最严重的两类伪证据：`build_reference_metadata.py` 不再从 source metadata 自动轮转生成 page-level 记录；机械视觉 reviewer 也不再替外部 Planner 写 academic PASS。现有四页 regression 仍走真实 `PPTX -> LibreOffice -> PDF -> PNG` 链，方向正确。

但当前 round 还不能 PASS，原因不是数量不足，而是还有两个实质性 integrity blocker，外加一个尚未完成的外部视觉验收门槛。

## Blocker 1 — Inspected Page Library 仍有页面特异记录与真实页内容不一致，且 inspection evidence 字段不完整

### 冻结依据

长期合同和原 corpus integrity PLAN 要求 inspected page 只能来自真正打开/渲染过的实际页面，每条至少绑定真实页码、实际 scientific object、页面特异观察、rights/provenance，以及可复核的 inspection evidence（包括 cache/source checksum、page/slide、inspection date/means）。随机抽查发现任何无法解释实际页内容的记录都必须 REVISE。

### 当前证据

自动 page-row synthesis 已经移除，这一点通过：当前 `page_rows()` 只消费显式 inspected-page specs，并校验 source/rendered-page checksum。

但随机核查 committed index 与公开原 deck 时发现至少一条实质不一致：

- `RRL-020 / SRC-006 / ISBI2025_Presentation.pdf / actual_page_number=8` 被记录为 `STATISTICAL_MODEL`，scientific object 写成 “PET-Disentangler loss with segmentation and reconstruction”，并写明 “loss components visible”。
- 对公开原 PDF 的第 8 页（1-based）核查时，实际页面是 PET-Disentangler method overview：Encoder、Mask prediction、Seg. Decoder、Image Decoder、Skip connections、GT/Ground truth 等对象；总体 objective/loss 页面出现在更后面的页，而不是这里。

同一抽样中，`RRL-026` 对 Bayesian Workflow 的 fake-data simulation、`RRL-028` 对 CDC MRP talk 的 poststratification identity 与公开 PDF 内容基本对应，说明问题不是整个索引都无效，而是当前仍存在具体的错页/错观察记录，不能因为 hash 存在就整体接受 48 rows。

此外，当前 `research_slide_reference_index.csv` 虽然包含 source checksum、rendered-page checksum、page number 和 `verification_status=inspected`，但没有显式的 `inspection_date` / `inspection_means`（或等价 inspection-evidence 字段）。仅有 hash 不能说明何时、以什么方式真正检查过该页。

### 最小修复

1. 重新检查 `SRC-006` 的所有 inspected rows，至少纠正或删除 `RRL-020`；若发现同一 source 有页码偏移或 observation 迁移，整体修正该 source 的 records。
2. 对其余 inspected rows 做一次有限 integrity sweep，重点找 page number 与 visible title / scientific object / page-specific observation 不一致的情况；不要新增 corpus 数量。
3. 为 inspected records 增加可复核的 inspection evidence 字段，至少包含 inspection date 和 inspection means；保留现有 source/rendered-page checksum。
4. 更新 regression test：hash 存在不能单独成为 inspected 的充分条件；字段完整性和 source/page identity 必须可验证。

### 复验

Planner 下一轮随机抽查跨 source 的 inspected records，并再次核公开 deck。任何错页、模板化 observation、无法解释实际页面的记录继续 REVISE。

## Blocker 2 — Regression 目前只是硬编码 reference ids，不是“检索 2–5 个 inspected pages”

### 冻结依据

原 corpus integrity PLAN 明确要求生成链在需要参考时，按 `page_function + scientific_domain/statistical_subdomain + evidence_type` 等任务语义检索 2–5 个真实 inspected records，PRIMARY 默认优先，并留下 retrieval trace：候选、最终选择、为什么相关、学到的组织/证据关系。Reference index 不能只是存在而不真正进入生成链。

### 当前证据

当前 `generate_research_group_meeting_regression.py` 在 `SLIDES` 常量中直接写死：

- RESULT_FIGURE → `RRL-003/RRL-020/RRL-022/RRL-029`
- FAILURE_CASE → `RRL-013/RRL-017/RRL-021/RRL-022`
- EXPERIMENT_DESIGN → `RRL-002/RRL-006/RRL-008/RRL-019`
- STATISTICAL_MODEL → `RRL-024/RRL-025/RRL-035/RRL-038/RRL-044`

manifest 中只有通用的 `learned_organization` 与 `reference_rationale`，没有查询条件、候选集合、排序/筛选依据，也没有说明为什么某个具体 inspected page 对当前 slide 的对象拓扑或证据关系相关。

因此当前只能证明“生成器引用了 index 中存在的 ID”，不能证明 reference corpus 被真正检索和使用。

### 最小修复

1. 增加一个简单、可审计的 reference retrieval 层；不需要复杂模型。按 slide intent/archetype、page function、domain/subdomain、evidence type 和 source tier 从 inspected index 筛选/排序即可。
2. generator 不再以 literal RRL list 作为唯一来源；每页运行 retrieval 后选择 2–5 条 inspected references。
3. EVIDENCE_MANIFEST / deck-plan evidence 中为每页留下 retrieval trace，至少记录 query intent、候选 ids、最终 ids、选择理由，以及实际学习的组织/证据关系。
4. PRIMARY 默认优先，但允许为了某个统计/教学对象使用 SECONDARY；必须在 trace 中说明原因。
5. 不复制 source 页面的视觉身份或整页内容。

### 复验

Planner 下一轮应能从同一 regression packet 反向看到：为什么每页得到这 2–5 个 references，而不是只看到预先写好的 RRL 编号。测试应明确禁止退化回纯 hard-coded reference list。

## Pending Gate — Academic visual review 尚未完成

机械 reviewer 的职责拆分已经正确：当前输出只到 `MECHANICAL_PASS`，`academic_visual_decision=NOT_ASSESSED`，没有再伪造科学视觉 PASS；这部分实现方向通过。

仓库也已经提交四张真实 LibreOffice regression PNG，因此后续 Planner 必须实际查看四张 rendered PNG，并逐页记录页面特异观察后，才能关闭 academic visual gate。本轮检查尝试通过 GitHub connector 读取 PNG；connector 能返回 base64 binary，但当前自动化运行环境没有建立可把该 connector binary 安全解码并交给图像查看器的通道，因此本次没有、也不会写 academic visual PASS。

由于当前已经存在上述两个可由 Executor 修复的 implementation blocker，本轮总体决定为 `REVISE` 而不是用工具可见性问题替代实现返修。下一轮在 Blocker 1/2 修复后必须再次尝试实际图像审阅；若届时仍无法真正看到 rendered PNG，则应 `BLOCKED`，不能 PASS。

## Source Scout

本轮不新增 Source Scout 搜索。当前 commit 已新增 10 条 statistics/biostatistics candidate backlog，并且本轮首先需要修复 corpus integrity 和 retrieval 使用链；继续堆来源不会关闭当前 blocker。

下一轮 acquisition priority 仍保持：完成本轮 integrity 后，优先做 3–6 张 `statistical-method group meeting` 关键页 benchmark，再根据实际失败模式决定 theorem-heavy / biostatistics validation-study / PhD proposal 的次序。

## CI / release

本轮不以版本发布为成功条件。当前 connector 没有返回 `846e3d96...` 的 commit status 条目，因此本次不把 CI 记为 PASS。由于已有 implementation blocker，先修复上述两项并重新运行 Presentation/Marketplace tests 与远端 Actions；下一轮再核 CI。

## 下一动作

Executor 只修上述 Blocker 1 和 Blocker 2，并准备下一轮可实际视觉审阅的 regression evidence。不要扩充 corpus 数量，不要 bump release，不要重做已经稳定的 editable PPTX/Beamer 路由。
