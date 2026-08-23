---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 022_research_presentation_candidate_visual_finish_repair
decision: PLAN_FROZEN
---

# 022 Research Presentation Candidate Visual Finish Repair — Plan

## Frozen decisions

### Objective

在不破坏 019/020 已验证的 reference-to-geometry 链路前提下，修复 021 comparative evidence 暴露出的 candidate visual-finish 缺口：

```text
reference-derived geometry
+
page-level scientific-object treatment repair
-> 3 repaired candidates per case
-> new blind comparative review identity
-> verify whether gap to real reference bar materially shrinks
```

本任务仍是 candidate layer repair，不是 deck-wide design-system locking，也不是最终 one-shot holdout。

### Evidence that freezes this scope

021 的 blind comparative evidence 已经足够明确：

- statistical estimator/equation：RRL-028 是唯一 mature / projection-ready item；三个 generated candidates 全部低于 bar；generated 中最好的一版主要缺 equation contrast / legibility 与 direct mathematical annotation；
- medical-image comparison：五个 items 全部低于 mature bar；generated candidates 的可修问题包括 image comparison 偏小、panel/legend integration 不够成熟、页面偏 sparse；同时 synthetic fixture-like imagery 本身不是可通过视觉修饰消除的问题。

所以 022 不继续加 reference metadata，也不重新设计 composition selector；只修“相同 reference-derived composition 怎么被真正画成成熟科研页”。

## Required repository reading

Executor 至少读取：

- `AGENTS.md`
- `automation/reviewed_handoff/README.md`
- `automation/reviewed_handoff/schema.json`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- `results/019_research_presentation_exemplar_composition_representation/FINAL_REPORT.md`
- `results/020_research_presentation_reference_calibrated_candidate_search/FINAL_REPORT.md`
- `results/020_research_presentation_reference_calibrated_candidate_search/REVIEW_1.md`
- `results/020_research_presentation_reference_calibrated_candidate_search/REVIEW_2.md`
- `results/021_research_presentation_comparative_reference_calibrated_visual_review/FINAL_REPORT.md`
- `results/021_research_presentation_comparative_reference_calibrated_visual_review/REVIEW_1.md`
- `docs/audits/RESEARCH_PRESENTATION_COMPARATIVE_VISUAL_REVIEW_REPORT.md`
- 020 candidate generator / schema / manifests / preview renderer；
- 021 comparative preparation / validator / visual manifests / identity maps / Terra evidence。

## Implementation scope

### 1. Preserve composition semantics before changing visual finish

022 必须保持 020 已验证的这些事实：

- selected 019 source normalized geometry 真实进入 candidate bbox 推导；
- `geometry_transfer` 仍来自实际 split / scale / translate / reorder；
- medical-image request 只在 medical-image-compatible source pool 中选 reference；
- estimator/equation request 只在 equation-compatible source pool 中选 reference；
- 三个 candidate 仍是同 scientific content、不同 composition logic，而不是三套颜色主题。

不得把 visual repair 写成新的 task-specific hardcoded coordinates。

需要增加 regression test，确认修改 visual renderer 后：

- 同 family 不同 source geometry 仍会产生不同 primary candidate bboxes；
- 020 的 compatibility-gate regression 继续通过；
- candidate strategy / RRL / QA / provenance 仍不会泄漏到 audience-facing pixels/text。

### 2. Replace the neutral regression skin with presentation-native page treatment

020 的 neutral preview skin 只适合验证 geometry，不适合作为成熟科研视觉层。022 可以新增/重构 **page-level rendering primitives**，但不能提前建立完整 deck theme engine。

这些 primitives 应服务 scientific object，而不是服务装饰：

- restrained academic type hierarchy；
- high-contrast text / equation treatment；
- scientific-object-first spacing；
- direct annotation / legend；
- minimal informational color roles；
- no default rounded-card container around the main scientific object；
- no decorative title rule / color bar / shadow that carries no information；
- no mechanical footer sentence just to fill space。

可以让三个候选共享同一套 page-level visual tokens，以确保 comparative difference 仍主要来自 composition。不要通过给三个候选不同 theme 来制造“设计探索”。

### 3. Statistical estimator/equation repair

021 已明确指出：当前 generated equation candidates 的主要 blocker 是 equation contrast / legibility 与 direct mathematical annotation。

修复要求：

1. 核心 estimator/equation 必须成为真正 primary scientific object，而不是被放进浅色/半透明容器后降低对比度；
2. 公式前景与背景使用稳定高对比组合，避免低对比灰字/灰底；
3. 公式字号/scale 必须使用 source-derived equation region 的可用面积，而不是固定缩小；
4. annotation 必须**直接绑定数学对象或具体 term**：例如 leader/brace/highlight/adjacent label 应有明确 target relation，不能只在页面另一侧写一段“middle term means ...”；
5. 如果说明的是 sandwich covariance 中的 cluster-level aggregation，应让 annotation 直接指向对应 middle term / factor，而不是重复整句定义；
6. annotation 不得遮挡公式、破坏 reading order 或制造多余卡片；
7. 公式下方/旁边的辅助文字只保留当前 page message 必需内容；不得继续使用 generic explanatory footer。

不要为本次 cluster-robust estimator 写死某个公式 token 的坐标。实现应基于 candidate manifest 中的 equation region / annotation anchors 或等价 generic structure，使其它 estimator/theorem/equation request 可复用。

### 4. Medical-image comparison repair

021 的 generated medical candidates 存在两类可修视觉问题：image comparison 偏小 / underdeveloped，以及 panel / legend / annotation integration 不够成熟。

修复要求：

1. image/overlay evidence 应继续成为页面视觉中心；primary scientific image area 不得因为新的 visual skin 被 padding/card chrome 吞掉；
2. panel row / image grid 的可见面积应尽量继承 source-derived primary region，内部 padding 只保留实际 label/legend 所需；
3. 同一 comparison 中 panel labels / correspondence 应紧邻各 panel，不能漂在远离影像的说明区；
4. overlay legend 应靠近 overlay 或作为共享 legend 与 image row 对齐；
5. focus-callout candidate 必须避免“大量空白 + 小图 + 一段说明”的 sparse fixture 感；如果 scientific evidence 只有小区域，应优先扩大/crop evidence 或重排 annotation，而不是用空白制造所谓高级感；
6. primary image 不使用默认 rounded-card background；容器若不承载语义应删除；
7. 保持 synthetic-only evidence boundary，但不要把 synthetic qualifier 做成抢眼 QA 标签。

重要：本任务不要求通过美化 synthetic phantom 证明真实临床视觉成熟度。comparative review 中若剩余差距主要是“synthetic/demo-like evidence”，应在报告中明确保留，后续由 real holdout 解决。

### 5. Reference-calibrated visual targets, not arbitrary aesthetic thresholds

不要新增随意的“美观分数 >= 8”或固定像素阈值。

可机械检查的 visual-finish contract 应尽量来自：

- selected composition record 的 primary/equation/image region；
- source-derived area ratios；
- candidate manifest 的 semantic role；
- explicit annotation target relation；
- deterministic presence/absence of banned container/meta-language；
- image/legend/caption adjacency relationship。

例如可以检查 repaired candidate 的 primary scientific object 没有比 source-derived target region 因装饰性 padding 明显缩水；但不要为所有 future slides 发明一个统一的任意面积常数。

### 6. Extend candidate manifest only where needed for visual provenance

如当前 schema 不足以表达 visual-finish semantics，允许最小新增，例如：

- `visual_tokens`；
- `primary_object_treatment`；
- `annotation_targets`；
- `legend_binding`；
- `container_role`；
- `equation_rendering`；
- `panel_correspondence`。

这些字段必须描述实际 renderer 行为，不能成为事后解释。

validator/tests 至少检查：

- annotation target 指向真实 candidate region / semantic object；
- primary object 没被 non-semantic card container 包围；
- visual tokens 对三个候选一致；
- candidate content 与 source/geometry provenance 仍可追踪；
- audience-facing text 无 internal/meta leakage。

### 7. Rebuild the same two controlled candidate sets

继续使用 020/021 的两个 controlled requests：

- statistical estimator/equation；
- medical-image comparison。

每个 case 仍生成恰好 3 个候选：

- reference-faithful；
- alternative composition；
- controlled wildcard。

必须生成新的 preview SHA；旧 020 previews 保留为历史 provenance，不覆盖其 identity。

新增 repair report，例如：

`docs/audits/RESEARCH_PRESENTATION_CANDIDATE_VISUAL_FINISH_REPAIR.md`

至少记录：

- 021 哪些 gap 被映射到什么 generic renderer repair；
- 哪些是可修 visual-finish gap；
- 哪些属于 synthetic-content limitation；
- before/after candidate identity；
- source geometry transfer 是否保持；
- 未把哪些东西硬编码成当前 benchmark 特例。

### 8. Run a new comparative review after repair

复用 021 已通过的 comparative pipeline，不再新造一套视觉 reviewer。

对 repaired statistical case 和 repaired medical case：

- 使用新的 candidate SHA；
- 继续使用与 page job 匹配的真实 inspected references；
- reference pixels runtime materialize，不提交；
- Terra-visible item 继续匿名；
- 每个**新的 immutable identity**各运行恰好一次 live `gpt-5.6-terra`；
- 不对相同 identity 重刷。

新的 decoded report 必须同时说明：

- repaired candidates 相比 021 old candidates 是否实质进步；
- statistical best candidate 是否已接近/达到 RRL-028 所代表的 mature equation-slide bar；
- medical candidate 的 layout/image-treatment gap 是否已关闭；
- 如果 medical 仍 `REVISE`，剩余差距是否主要来自 synthetic evidence realism，而不是构图/排版/影像层级；
- 是否仍是 `NO_CANDIDATE_MEETS_REFERENCE_BAR`。

### 9. Do not force PASS from relative improvement

“比 021 好”不是充分条件。

Planner review 时允许：

- repaired statistical candidates 仍全部低于 mature bar -> 022 `REVISE`；
- medical visual-treatment blocker 仍明显存在 -> 022 `REVISE`；
- medical 只剩 synthetic evidence realism limitation，而 composition / image prominence / integration 已达到当前 matched reference 水平 -> 可以记录为后续 real-holdout 必须验证的非阻断限制。

Executor 不得自行决定“够好了”。

### 10. Scope boundaries

022 不得：

- 扩 reference corpus；
- 修改 Bridge Kit core；
- 修改 019 composition records；
- 破坏 020 candidate-source compatibility；
- 使用 021 reviewer ordering 直接写死 winner；
- 锁定完整 deck-wide design system；
- 做 full-deck generation；
- 开始 real statistical / medical holdout；
- 把 synthetic image 当作真实临床证据；
- 宣告长期质量目标完成。

## Acceptance and regression gates

Planner/Reviewer 只有在以下全部满足时才可 PASS 022：

1. 019/020 的 source geometry transfer 与 semantic compatibility regressions 继续通过；
2. statistical equation candidate 的公式不再因低对比/容器处理失去投影可读性；
3. statistical annotation 与具体 mathematical object/term 有直接可审计绑定，而不是远距离说明文字；
4. medical primary images 没有被 generic card/padding 压缩，panel correspondence / legend / annotation 更直接；
5. focus-callout medical candidate 不再表现为小图 + 大块无效留白的 fixture composition；
6. 三候选共享同一 page-level visual tokens，差异仍来自 composition 而不是换 theme；
7. candidate manifest / renderer 行为一致，新增字段不是事后解释；
8. old 020/021 identities 保留，repaired candidates 产生新 SHA；
9. 两个 repaired cases 各在新的 immutable identity 下只运行一次 live comparative Terra；
10. comparative evidence 显示统计 candidate 与 mature equation reference 的差距已实质缩小，且没有继续出现 equation contrast / direct annotation blocker；
11. comparative evidence 不再指出明显的 medical image prominence / panel-integration blocker；若剩余主要是 synthetic evidence realism，应明确留给 real holdout；
12. 不提交外部 reference pixels，不修改 Bridge Kit core，不提前开始 deck-wide lock 或真实 holdout；
13. repository validation / required CI 全部通过。

021 已建立的 comparative review mechanism 本身不是本轮返修对象，除非 repaired inputs 暴露了明确的 consumer-side bug；不得借此重构 Bridge Kit。

## Validation

至少运行：

```bash
python -m unittest tests.test_presentations
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
git diff --check
```

如新增/修改 candidate validator、renderer 或 comparative preparation script，必须执行其 targeted validation。

涉及 repaired visual identity 时，必须真实生成 PNG candidates，并按上述规则运行新的 live Terra comparative review。不要用 mock Terra 结果作为 acceptance evidence。

## Executor handoff

完成实现后：

- 写 `results/022_research_presentation_candidate_visual_finish_repair/RESULT.md`；
- visual evidence 放在该 task 的 `visual_review/**` 或计划中明确的 task-owned目录；
- 报告 implementation commit、candidate SHA、new comparative review identity、实际 Terra evidence 与 validation；
- 更新 CURRENT 到 `WAITING_FOR_CI`；
- push `origin/main`；
- 等 required CI；
- 不写 Planner-owned REVIEW / FINAL_REPORT。
