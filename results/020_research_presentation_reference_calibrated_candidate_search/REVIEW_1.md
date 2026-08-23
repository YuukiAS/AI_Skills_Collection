---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 020_research_presentation_reference_calibrated_candidate_search
review_round: 1
decision: REVISE
implementation_commit: e37d7bd228853f5c385f81e9915baeebf8f91dc1
---

# GPT Review

## Decision

`REVISE`。

020 已经把 candidate request / manifest、三候选输出、真实公式/影像内容、预览哈希、distinctness signature 与 source-to-candidate trace 这些基础设施搭起来，真实 CI 也已经通过；但当前实现还没有满足冻结 Plan 最关键的两条语义要求：**候选几何必须真正由 019 composition records 驱动，而不能只是先选一个 family 再套固定坐标；用于 alternative / wildcard 的 source exemplar 也必须是真正兼容当前 scientific job 的页面，而不能被通用停用词匹配污染。**

当前 handoff tip `b4240811518cca2c6b314eeafa699be50648de56` 的 `reviewed-handoff/ci-summary=success`，指向 GitHub Actions run `32628234338`；`codex-marketplace`、Windows sparse checkout 与 Linux/Windows editable-install smoke 均成功。因此本轮 blocker 不是 CI，而是 candidate-search 本身的 reference calibration 语义。

## Independent review

### 已满足的部分

- 两个 regression request 都产生恰好 3 个候选，并使用相同 scientific content payload；统计页包含真实 rendered equation，医学影像页包含真实本地 synthetic image/overlay evidence。
- 三个候选的 preview SHA 和 geometry signature 不同；没有把 strategy、RRL、repo path、QA/provenance 打到 audience-facing text。
- shared generator 实际调用 019 selector/index，没有在 production 逻辑里直接硬编码固定 `RRL-xxx` 列表。
- 020 没有越权修改 active research-presentations workflow、Terra、Bridge Kit、PPTX/Beamer renderer，也没有提前做 holdout 或宣告 one-shot quality。

这些都说明 020 的“候选搜索外壳”成立，但还不足以证明真正的 `reference -> composition -> candidate` 迁移。

## Blocking findings

### F-020-01 — 候选 bbox 由 family-specific 固定坐标生成，019 的真实 source geometry 没有进入布局计算

**冻结依据**：PLAN 要求 generator-side planning 实际消费 019 composition records，而不是只把 `layout_family` / RRL IDs 写进日志；`reference_faithful` 应把最高匹配 exemplar 作为主要几何先验，并留下真实的 source bbox -> candidate bbox transfer/adaptation trace。

**观察到的实现**：`candidate_regions(request, strategy, source)` 虽然读取了 `source["layout_family"]`，但每个 family 的 candidate bbox 都是在 Python 中写死的一组固定坐标。例如医学影像 `aligned-multi-panel` 永远生成 `0.07/0.22/0.20/0.36`、`0.30/0.22/0.20/0.36` 等 box；统计 `equation-dominant`、`split-visual-explanation`、`result-with-callout` 也各自使用固定 bbox。source record 的真实 `regions[].bbox` 没有参与这些 candidate bbox 的计算。

随后 `transfer_trace()` 才把真实 source bbox 与已经生成好的固定 candidate bbox 并列记录，并统一给出“fit ... while preserving the source role hierarchy”的 adaptation reason。也就是说，当前 trace 是**事后说明差异**，不是**由 source geometry 推导 candidate geometry**。例如医学 reference-faithful 候选把 RRL-022 的整块 `image_grid` bbox `x=.10,y=.08,w=.78,h=.76` 事后映射到四个预先写死的小 panel；manifest 能记录这个映射，但 generator 并没有从该 bbox 计算这些 panel 的位置和尺度。

**为什么阻断**：如果把 RRL-022 换成同一 family、但 bbox/对齐关系明显不同的另一个真实 exemplar，当前 candidate geometry 基本不会因此变化。这仍然是“family template selection”，不是 019 计划建立的“真实 exemplar composition transfer”。若现在进入 comparative Terra，视觉 reviewer 实际比较的仍是手写 family templates，会把 reference calibration 的核心缺口隐藏到后续阶段。

**最小修复**：不需要重写 renderer，也不需要新增大型布局求解器。让 candidate geometry 至少从 selected source record 的 normalized regions / alignment / primary bbox 派生：

1. `reference_faithful` 必须以 source title/primary/annotation/legend 等真实 region bbox 和相对关系为起点，再按当前 content slot 数量做可解释的 split/merge/scale/translate；
2. `alternative_composition` / `controlled_wildcard` 同样从各自 selected source composition 的真实 geometry 派生，而不是只根据 family 名称选固定坐标；
3. `geometry_transfer.adaptation_type/reason` 必须由实际执行的几何操作产生，而不是事后统一猜测；
4. 增加 regression：对同一 family 的两个不同 source composition record，若 primary/region geometry 不同，生成后的 candidate geometry 应发生可解释变化，从而证明 bbox 数据真的进入计算。

允许保留一个很小的 renderer-neutral adaptation helper；不要借本 finding 扩成通用自动排版系统。

### F-020-02 — `controlled_wildcard` 的“兼容 exemplar”筛选被通用词污染，医学影像候选实际使用了不相关的 Bayesian model page

**冻结依据**：PLAN 要求 C 从“兼容 exemplars”中选择 composition-distance 最大的可行方向；candidate source 必须能逐字段说明来源和 adaptation reason，不能为了不同而牺牲 scientific-object semantics。

**观察到的实现**：`tokens()` 只按长度过滤，没有停用词/领域兼容性门槛；`compatible_records()` 只要任何 token overlap 就可进入 pool。当前医学影像 manifest 中，RRL-034（`STATISTICAL_MODEL`，scientific object=`Bayesian toy model construction`）仅靠诸如 `and/with` 一类通用词得到低分后仍进入 pool，最终被 distance 最大化选为 `controlled_wildcard`。结果 manifest 明确显示：医学影像 lesion-overlay request 的 wildcard source 是 RRL-034，沿用了 `split-visual-explanation` family 和 `title-to-model-bullets-to-concrete-example` reading flow，再把其中的 `model_specification` / `concrete_example` region 事后映射到医学 overlay / error / legend。

**为什么阻断**：这不是“受约束 wildcard”，而是在语义不兼容的 reference 上做几何借壳。它会系统性奖励“离得远但不相关”的页面，后续一旦 reference library 扩大，距离最大化很容易挑到越来越离谱的 exemplar。

**最小修复**：在 composition distance 之前加一个小而明确的 compatibility gate：

- 去掉 `and`、`with` 等无判别力 token；
- page function / evidence type / content mode 至少满足一条强兼容关系；医学影像 page 必须优先要求 `medical_image` 或明确 image-comparison compatible composition，统计 equation/estimator page 必须要求 equation/estimator compatible composition；
- distance 只能在通过 compatibility gate 的 pool 内排序；
- 若兼容 family 不足 3 个，可以用同一 compatible family 的 alternate topology/真实几何重组，而不是退化到无关 domain/page job。

增加 regression，确保当前 medical-image wildcard 不再选择 Bayesian toy-model / unrelated statistical-model exemplar，也确保 generic stopwords 不能单独让 record 进入 compatible pool。

## Scope for revision

本轮只修以上两个 blocker：

1. 让 selected composition record 的真实 normalized geometry 真正参与 candidate bbox 派生；
2. 收紧 compatible exemplar pool，再在其中做 alternate/wildcard distance selection；
3. 重新生成两个 request 的 manifests/previews/comparison sheets，并更新报告与 tests；
4. 保持 neutral preview skin、scientific content、019 records、active Presentation skill、Terra、Bridge Kit、PPTX/Beamer renderer 和 holdout 范围不变。

不要提前实现 comparative Terra、winner selection、deck design-system lock 或真实 holdout。

## Re-review gate

第二轮只需证明：

- 同一 family 的不同真实 source geometry 能真实改变 candidate geometry；
- manifest transfer trace 对应 generator 实际执行的 adaptation；
- medical/statistical candidate source 都通过明确 compatibility gate；
- 三候选仍保持相同 content、真实 scientific objects、至少两种 composition logic、无内部信息泄漏；
- required CI 再次通过。

满足后 020 才可以关闭并进入下一阶段的 comparative reference-calibrated visual review。
