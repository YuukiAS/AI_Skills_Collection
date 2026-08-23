---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 019_research_presentation_exemplar_composition_representation
decision: PLAN_FROZEN
---

# 019 Research Presentation Exemplar Composition Representation — Plan

## Frozen decisions

### Objective

把当前已经 `verification_status=inspected` 的真实科研 slide 从“RRL + prose lesson”提升为**机器可用、renderer-neutral、绑定真实页面 identity 的 composition representation**。

本任务只建立 reference -> composition 这一层。它不生成新 deck，不做 multi-candidate search，不改 Terra，不跑真实 holdout，也不重构 PPTX / Beamer renderer。

018 已确认下一代链路应按以下顺序推进：

```text
inspected reference page
-> composition representation
-> candidate design search
-> comparative visual review
-> locked design system
-> real holdout one-shot generation
```

019 只负责第二个节点。

### Why this is the minimum next step

当前 `research_slide_reference_index.csv` 已记录 page function、scientific object、evidence type、figure/text ratio、为什么该页有效等信息，但这些仍不足以约束生成器回答以下问题：

- 主 scientific object 在页面哪个区域、占多大面积；
- 标题、公式、图、annotation、caption 如何形成视觉层级；
- 页面是单主图、左右分栏、对齐多 panel、横向流程还是 equation-first；
- 哪些对象共享对齐边、哪些区域承担解释、哪些是辅助信息；
- 阅读方向和留白如何组织。

因此 019 的核心产物必须是**结构化几何与语义构图对象**，不能再只是增加一列 prose lesson。

## Required repository reading

Executor 必须先读取：

- `AGENTS.md`
- `automation/reviewed_handoff/README.md`
- `automation/reviewed_handoff/schema.json`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- `results/018_presentation_external_method_audit/FINAL_REPORT.md`
- `docs/audits/RESEARCH_PRESENTATION_EXTERNAL_METHOD_AUDIT.md`
- `docs/audits/research_presentation_external_method_matrix.json`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/references/research_slide_reference_index.csv`
- `skills/tools/documents-media/presentations/shared/references/reference_sources_manifest.json`
- `skills/tools/documents-media/presentations/shared/references/RESEARCH_SLIDE_ARCHETYPES.md`
- 当前 reference retrieval / Presentation regression 中使用 RRL records 的相关脚本与 tests。

## Implementation scope

### 1. Add a renderer-neutral composition schema

新增一个 shared reference schema，例如：

`skills/tools/documents-media/presentations/shared/references/research_slide_composition.schema.json`

schema 至少需要表达：

- `reference_id`
- `source_id`
- `actual_page_number`
- `page_function`
- `scientific_object`
- `evidence_type`
- `rendered_page_sha256`
- `inspection_basis`
  - 仅允许 `pptx_geometry` 或 `rendered_page_annotation`
- `layout_family`
- `reading_flow`
- `regions`
- `primary_scientific_object_region_id`
- `primary_object_area_ratio`
- `alignment_groups`
- `visual_hierarchy`
- `color_role_summary`
- `composition_inspection_means`
- `portable_composition_lessons`
- `reuse_boundary`

所有几何必须使用 renderer-neutral normalized coordinates：

```text
x, y, w, h in [0, 1]
```

不能把 PowerPoint EMU / inch 或 Beamer pt 作为 canonical representation。

### 2. Region model

每个 `regions[]` 至少包含：

- stable `region_id`
- semantic `role`
- normalized `bbox`
- `hierarchy_rank`
- `alignment_group`（可空）
- `content_mode`

允许的核心 role 至少覆盖：

- `title`
- `primary_scientific_object`
- `secondary_scientific_object`
- `equation`
- `body_text`
- `annotation`
- `caption`
- `legend`
- `decision_or_next_step`

不要为了覆盖未来所有场景建立庞大 taxonomy。只有真实 exemplar 中需要的角色才进入初版枚举。

`content_mode` 用于区分 figure / equation / medical-image / diagram / text / table 等科学对象类型，但不得包含 source-specific visual identity。

### 3. Composition families

新增一个简洁、由真实 exemplar 归纳得到的 family vocabulary，例如放在：

`skills/tools/documents-media/presentations/shared/references/RESEARCH_COMPOSITION_FAMILIES.md`

初版 family 不超过 8 个，并且必须来自实际 inspected pages，不得凭空设计完整模板库。候选可以包括但不限于：

- single-visual-dominant
- equation-dominant
- split-visual-explanation
- aligned-multi-panel
- horizontal-process-flow
- result-with-callout
- comparison-focused
- decision-or-next-step

具体名称可由 Executor 根据实际页面调整，但必须保持 renderer-neutral，并说明每个 family 的适用 scientific job 与不适用情况。

这些是 composition families，不是 PowerPoint 模板，也不是 style presets。

### 4. Build a bounded exemplar composition index

新增：

`skills/tools/documents-media/presentations/shared/references/research_slide_composition_index.json`

本任务只建立一个**小而有代表性的初版**，不要求给全部 RRL 页面标注。

最低要求：

- 至少 12 个 composition records；
- 来自至少 4 个不同 `source_id`；
- 覆盖至少 6 类 scientific page jobs / composition needs；
- 必须同时包含统计/方法类页面和医学影像/科学图像类页面；
- 至少包含：
  - 一个 equation / statistical-model dominant exemplar；
  - 两个 quantitative result exemplars；
  - 两个 method / experiment flow exemplars；
  - 两个 image / aligned-panel exemplars；
  - 一个 negative-result / model-check exemplar；
  - 一个 next-experiment / decision exemplar。

只能从当前 `research_slide_reference_index.csv` 中 `verification_status=inspected` 的页面选择。

不得使用上一轮 016 / 017 synthetic benchmark 页面作为 exemplar source。

### 5. Real-page inspection requirement

每个 composition record 必须来自真实页面检查，不得根据 talk metadata、page title、已有 prose lesson 或 page function 猜 bbox。

如果原始 source 是可解析 PPTX：

- 优先读取真实 shape geometry；
- `inspection_basis=pptx_geometry`。

如果只有 PDF / rendered PNG：

- 必须实际打开/渲染对应页面并基于真实像素做 annotation；
- `inspection_basis=rendered_page_annotation`；
- record 必须绑定现有 `rendered_page_sha256`。

不要求 OCR，也不要为了本任务引入高成本 OCR pipeline。

### 6. Do not copy visual identity

composition representation 只允许保存：

- normalized geometry；
- semantic roles；
- hierarchy；
- alignment；
- reading flow；
- abstract color roles；
- portable composition lesson。

禁止保存或复制：

- source screenshot；
- exact page artwork；
- exact institutional theme；
- exact source font pairing；
- exact source-specific decorative asset；
- whole-slide SVG/PPTX clone；
- copyrighted figure pixels。

`color_role_summary` 只能表示诸如：

- neutral background + one accent；
- categorical multi-color figure；
- monochrome equation with one highlighted term；

不得记录“复制这个 source 的具体品牌色”。

### 7. Add deterministic validation

新增一个共享 validator，例如：

`skills/tools/documents-media/presentations/shared/scripts/validate_reference_compositions.py`

至少检查：

- schema 合法；
- `reference_id` 在现有 index 中真实存在；
- 该 RRL 为 `verification_status=inspected`；
- `source_id` / page / page_function 与 RRL index 一致；
- `rendered_page_sha256` 与现有 RRL record 完全一致；
- bbox 数值全部在 `[0,1]`；
- `w > 0`, `h > 0`；
- primary scientific object region 存在；
- `primary_object_area_ratio` 与 primary bbox 面积一致；
- hierarchy rank 合法；
- layout family 在 family vocabulary 中；
- 不存在 source screenshot / absolute path / RRL provenance 泄漏到 audience-facing artifact 的新路径。

### 8. Add a minimal composition selector

新增一个只读 helper，例如：

`skills/tools/documents-media/presentations/shared/scripts/select_reference_compositions.py`

输入至少支持：

- `page_function`
- 可选 `evidence_type`
- 可选 `scientific_object` 关键词
- `limit`

输出匹配的 composition records / reference IDs，并保留 composition family 与主要几何信息。

它只负责**检索 composition exemplar**，不得：

- 生成 slide；
- 产生 visual candidates；
- 自动决定最终 layout；
- 调用 Terra；
- 修改 deck plan。

### 9. Add an abstract debug view

为了让 Planner/Reviewer 能检查这些 geometry 是否至少形成合理构图，而不提交 source slide 像素，生成一个可审查的**抽象 composition debug montage**：

- 可用 SVG 或其他文本型矢量格式；
- 每个 exemplar 只画 normalized region boxes、role labels、reading flow / primary region；
- 不嵌入原始 source screenshot、figure 或品牌视觉资产；
- 该 montage 只是 annotation QA，不是新的 slide template。

建议路径：

`docs/audits/research_presentation_composition_debug_montage.svg`

### 10. Add a short implementation report

新增：

`docs/audits/RESEARCH_PRESENTATION_COMPOSITION_REPRESENTATION_REPORT.md`

至少说明：

- 选了哪些 page jobs / source IDs；
- geometry 是如何从真实页面获得的；
- 哪些字段是真实测量，哪些是抽象分类；
- composition representation 能解决什么；
- 它现在还不能解决什么；
- 为什么下一阶段可以基于它做 candidate search，而不能直接宣告 design quality 成熟。

## Acceptance and regression gates

至少更新 Presentation tests，验证：

1. composition schema / index 可读取；
2. 至少 12 个 records、至少 4 个 source IDs、至少 6 类 page needs；
3. 所有 records 绑定真实 inspected RRL 与相同 rendered-page SHA；
4. normalized bbox / area ratio / family vocabulary 合法；
5. selector 对 `RESULT_FIGURE`、`STATISTICAL_MODEL` / equation 类、medical-image / aligned-panel 类查询能返回真实 composition records；
6. debug montage 存在且不包含 source screenshot / embedded binary；
7. source / generated plugin mirror 如果当前 packaging contract 要求同步，则保持一致。

## Out of scope

019 禁止：

- 修改 `research-presentations/SKILL.md` 的 active generation rules；
- 修改 `visual-qa.md` / Terra rubric；
- 修改 Bridge Kit；
- 新增或扩充 source corpus；
- Source Scout；
- multi-candidate visual generation；
- design-system selection；
- comparative Terra review；
- contact-sheet quality gate；
- statistical / medical-imaging real holdout；
- Beamer renderer / PPTX renderer 重构；
- 引入外部 skill runtime；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

如果在实现 composition schema 时发现 renderer 需要额外字段，把字段记录为 future requirement；不要在同一 task 顺手重构 renderer。

## Acceptance gates

Planner/Reviewer 只有在以下全部满足时才可 PASS：

1. composition layer 是结构化 geometry + semantic roles，不是新的 prose lesson 表；
2. 至少 12 个 records 全部绑定真实 inspected RRL 与相同 rendered SHA；
3. page-function / source / domain 覆盖达到冻结下限；
4. 每个 bbox 来源于真实页面检查或 PPTX geometry，不从 metadata 猜；
5. representation renderer-neutral，可同时作为未来 PPTX / Beamer 的上游输入；
6. 没有复制 source visual identity / screenshot / copyrighted figure pixels；
7. validator 能机械发现坏 reference、坏 SHA、越界 bbox、缺 primary object 等错误；
8. selector 能按 scientific job 返回 composition records，但没有越权做 layout generation；
9. abstract debug montage 能帮助 Reviewer 检查构图 annotation，而不暴露 source pixels；
10. 没有提前实现 020+ 阶段；
11. repository validation / required CI 全部通过。

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

本任务 `ci_required=true`。Executor 完成后写 `RESULT.md`，提交实现并进入真实 CI；Scheduled Planner 在 CI 成功后独立检查 schema、composition records、debug montage、tests 和 scope boundary。
