---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 020_research_presentation_reference_calibrated_candidate_search
decision: PLAN_FROZEN
---

# 020 Research Presentation Reference-Calibrated Candidate Search — Plan

## Frozen decisions

### Objective

把 019 已完成的 reference composition layer 真正推进到下一节点：

```text
inspected composition exemplars
-> same scientific content
-> three compositionally distinct candidate previews
```

本任务只建立 **internal candidate design search**。它不做最终 comparative Terra，不让用户选 style，不锁定完整 deck design system，也不开始真实 holdout。

### Why this is the minimum next step

019 已经可以回答“真实优秀页面的主 scientific object 在哪里、多大、如何对齐、属于什么 composition family”，但系统仍然只有 reference-side 数据，没有 candidate-side 行为。

020 必须证明两件事：

1. generator-side planning 会实际消费 019 composition records，而不是只把 `layout_family` / RRL IDs 写进日志；
2. 对完全相同的 scientific content，系统能内部形成三种真正不同的 composition logic，而不是默认布局换三个颜色。

只有这一步真实成立，下一 task 才值得做 reference-calibrated comparative visual review。

## Required repository reading

Executor 必须先读取：

- `AGENTS.md`
- `automation/reviewed_handoff/README.md`
- `automation/reviewed_handoff/schema.json`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- `results/018_presentation_external_method_audit/FINAL_REPORT.md`
- `results/019_research_presentation_exemplar_composition_representation/FINAL_REPORT.md`
- `docs/audits/RESEARCH_PRESENTATION_EXTERNAL_METHOD_AUDIT.md`
- `docs/audits/RESEARCH_PRESENTATION_COMPOSITION_REPRESENTATION_REPORT.md`
- `skills/tools/documents-media/presentations/shared/references/research_slide_composition.schema.json`
- `skills/tools/documents-media/presentations/shared/references/research_slide_composition_index.json`
- `skills/tools/documents-media/presentations/shared/references/RESEARCH_COMPOSITION_FAMILIES.md`
- `skills/tools/documents-media/presentations/shared/scripts/select_reference_compositions.py`
- 现有 statistical / medical-imaging Presentation regression fixtures 与安全可复用的本地 scientific assets。

## Implementation scope

### 1. Add a renderer-neutral candidate request / candidate manifest contract

新增一个 shared candidate request / result schema，路径可由 Executor 根据现有 shared structure 选择，建议类似：

- `.../shared/references/research_slide_candidate_request.schema.json`
- `.../shared/references/research_slide_candidate_manifest.schema.json`

request 至少表达：

- stable `request_id`
- `page_function`
- `scientific_object`
- 可选 `evidence_type`
- `content_slots`
- `required_roles`
- `primary_scientific_object_role`
- `audience_mode`
- `density_mode`
- `candidate_count`，本轮固定为 3

`content_slots` 必须绑定真实用于 preview 的内容/本地 asset，而不是只写“这里放图”。允许字段包括：

- title text；
- concise body / annotation text；
- equation/vector asset；
- plot/image asset；
- caption / legend；
- data/evidence label。

不得把用户可见 slide 文案硬编码在 candidate engine 本身。

candidate manifest 每个 candidate 至少表达：

- `candidate_id`
- internal `strategy`
- `source_reference_ids`
- `source_composition_families`
- candidate `layout_family`
- normalized candidate `regions`
- `primary_object_area_ratio`
- `reading_flow`
- `content_bindings`
- `geometry_transfer`
- `distinctness_signature`
- `preview_artifact`
- `preview_sha256`

所有 candidate geometry 继续使用 `[0,1]` normalized coordinates。

### 2. Candidate strategies

同一 request 必须内部产生恰好三个候选：

#### A. `reference_faithful`

- 以 selector 排名最高、scientific job 最匹配的 inspected composition exemplar 为主要几何先验；
- 可以根据真实内容长度/比例做适配；
- 不复制 source theme、font、颜色、figure pixels 或 artwork。

#### B. `alternative_composition`

- 必须选择与 A 不同的 composition family，或在确实没有兼容 family 时使用明显不同的 region topology / reading flow；
- scientific-object semantics 必须保持正确；
- 不能为了“不同”牺牲 evidence prominence。

#### C. `controlled_wildcard`

- 从兼容 exemplars 中选择在 composition signature 上与 A/B 距离最大的可行方向，或基于两个真实 composition records 做有约束的几何重组；
- 仍必须能逐字段说明来源和 adaptation reason；
- 不允许自由随机生成一个与 reference 无关的 layout。

三个策略名称只存在内部 manifest，不得出现在 slide preview 的 audience-facing pixels 中。

### 3. Reference retrieval must be real and dynamic

candidate engine 必须实际调用/复用 019 的 composition selector / index。

禁止在业务逻辑中硬编码：

- `RRL-xxx` 候选列表；
- 某个 fixture 永远绑定某个 family；
- 某个 page function 永远返回一套固定坐标。

允许 tests 对预期查询结果做断言，但 production/shared candidate search 逻辑必须由 query + composition records 驱动。

每个 candidate manifest 必须保留：

- 实际检索到的 candidate exemplar IDs；
- 选择当前 exemplar/family 的理由；
- source bbox -> candidate bbox 的 transfer/adaptation trace。

### 4. Geometry transfer must be inspectable

`geometry_transfer` 至少记录：

- source `reference_id`
- source `region_id` / role
- source normalized bbox
- candidate region / content slot
- candidate normalized bbox
- adaptation type
- concise adaptation reason

允许的 adaptation type 保持小而明确，例如：

- `preserve`
- `scale`
- `translate`
- `merge`
- `split`
- `reorder`

不要建立庞大 ontology。

关键要求：未来 Reviewer 必须能回答“这个 candidate 到底从真实 reference 学了什么”，而不是只看到一句 `inspired by RRL-xxx`。

### 5. Use a fixed neutral preview skin for 020

020 只验证 composition search，不同时验证完整 style discovery。

因此三个 candidate preview 默认使用同一套 restrained neutral research preview skin：

- 同一字体系统；
- 同一基础 palette；
- 同一 spacing scale；
- 同一 title/caption visual language。

这样候选差异必须主要来自 composition / object hierarchy，而不是换颜色制造“不同”。

preview skin 是内部 regression skin，不得因此写入 active `research-presentations/SKILL.md` 作为用户默认主题。

### 6. Candidate previews must contain real scientific content

不能只生成 wireframe / labeled rectangles。

至少建立两个受控 regression requests，每个 request 都生成 3 个真实内容 preview：

#### Request 1 — statistics / equation or estimator page

使用仓库中已有、可安全复用的 deterministic statistical Presentation fixture 内容，例如真实排版公式、估计量、解释文本或结果资产。

要求至少一个 equation/estimator scientific object 真正进入 preview，且公式/科学对象不是 ASCII source-like placeholder。

#### Request 2 — medical-image / aligned evidence page

使用仓库已有、可安全复用的 deterministic medical-imaging fixture content / synthetic image assets。

要求真实 image / GT / prediction / overlay 或等价 scientific image object 真正进入 preview，不得用空图框代替。

这些旧 synthetic fixtures **只作为 candidate-engine regression content**，不是 gold exemplar、不是 design-quality pass 证据，也不改变上一轮 10 页 medium/negative baseline 的定位。

### 7. Preview format

每个 candidate 必须产生固定 16:9 的真实视觉 preview，并能转换为 PNG 供下一阶段视觉 reviewer 使用。

允许实现：

- self-contained SVG / HTML preview + deterministic PNG render；
- 或其他现有仓库可稳定渲染的 preview format。

本轮不要求最终 editable PPTX，因为当前任务是在正式 PPTX/Beamer generation 之前做内部设计搜索。

但 preview 必须满足：

- 真实标题/公式/图/影像/annotation；
- 无 lorem ipsum / `TBD` / generic placeholder；
- audience-facing pixels 不出现 `Candidate A/B/C`、`reference_faithful`、RRL IDs、repo path、QA/provenance；
- 不嵌入 reference screenshot / source figure pixels；
- 输出 SHA 可追踪。

建议同时生成一个**内部 candidate comparison sheet**，只用于 Reviewer 查看三个候选是否真的不同；这个 sheet 不是 full-deck contact-sheet rhythm gate，也不代表下一阶段 comparative Terra 已实现。

### 8. Deterministic candidate-distinctness checks

新增机械 validator，至少检查：

- 每个 request 恰好 3 个 candidates；
- candidates 使用完全相同的 content payload；
- candidate preview SHA 不相同；
- 至少两个不同 composition families；
- A 与 B 不得是同一 geometry 只换色；
- C 必须有明确的 composition-distance / alternate-topology 依据；
- primary scientific object 在三个 candidate 中都存在且满足 page-job semantics；
- source -> candidate transfer trace 完整；
- audience-facing preview 无内部 IDs / candidate strategy / QA/provenance；
- source reference pixels 没有进入 candidate preview。

不要用任意“美观分数”做 deterministic gate。

### 9. Composition distance

实现一个简单、可解释的 renderer-neutral composition distance / distinctness signature，用于 C 的选择和机械去重。

可以组合：

- layout family mismatch；
- primary bbox center / area difference；
- region-role topology；
- reading-flow category；
- region count / alignment-group structure。

不要训练模型，不要引入复杂 embedding，也不要把此距离冒充视觉质量分数。

### 10. Add an implementation report

新增：

`docs/audits/RESEARCH_PRESENTATION_CANDIDATE_SEARCH_REPORT.md`

至少说明：

- candidate search 如何消费 019 records；
- 三个策略如何区分；
- source geometry 如何迁移并适配真实 content；
- 两个 regression requests 的实际 candidate families / source IDs；
- preview 如何渲染；
- distinctness 如何机械验证；
- 当前仍不能判断哪一个 candidate “更好”的原因；
- 为什么下一阶段必须是 comparative reference-calibrated visual review，而不是直接把 A 或任意 candidate 当最终 layout。

## Acceptance and regression gates

至少更新 Presentation tests，验证：

1. candidate request / manifest schema 可读取；
2. candidate search 真实读取 019 composition records；
3. production/shared search 没有硬编码固定 RRL IDs；
4. 两个 regression requests 都恰好得到 3 个 candidates；
5. 同 request 三个 candidates content payload 一致；
6. 至少两个不同 composition families，且 preview SHA 均不同；
7. geometry transfer trace 可验证 source bbox 与 candidate bbox；
8. statistical request 含真实 equation/estimator scientific object；
9. medical-image request 含真实 image / overlay scientific object；
10. candidate preview audience-facing text 无内部 candidate / RRL / QA/provenance 泄漏；
11. candidate comparison sheet / previews 可审查，但不包含 reference screenshot pixels；
12. source / generated plugin mirror 按当前 packaging contract 保持一致；
13. required CI 全部通过。

## Out of scope

020 禁止：

- 扩 reference corpus / Source Scout；
- 修改 019 composition records 以迎合测试，除非发现真正数据错误并由 Planner re-plan；
- 修改 active `research-presentations/SKILL.md` 用户工作流；
- 修改 Terra rubric / Bridge Kit；
- comparative reference-vs-candidate visual review；
- candidate 自动 winner selection；
- 用户 style picker / 让用户人工挑 A/B/C；
- deck-wide design-system lock；
- full-deck contact-sheet rhythm QA；
- real statistical holdout；
- real medical-imaging holdout；
- Beamer / PPTX renderer 重构；
- 宣告 `ONE_SHOT_QUALITY_PASS` / `PROGRAM_MATURE`。

## Acceptance gates

Planner/Reviewer 只有在以下全部满足时才可 PASS：

1. candidate search 真实消费 019 composition records，而非重新凭空设计；
2. 同一 scientific content 能产生恰好 3 个真实视觉 candidate previews；
3. 三个 candidate 的差异主要来自 composition，不是配色变化；
4. reference-to-candidate geometry transfer 可审计；
5. candidate previews 含真实 scientific objects，不是 wireframe；
6. 统计与医学影像两类受控 regression content 都能经过同一 shared candidate engine；
7. 没有硬编码 task-specific RRL/layout；
8. 没有 reference screenshot / source pixels / source visual identity 复制；
9. 没有内部 candidate/RRL/QA/provenance 泄漏到 preview pixels；
10. deterministic distinctness / integrity validation 成立；
11. 没有提前实现 comparative review / holdout / renderer integration；
12. repository validation / required CI 全部通过。

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

如果 candidate preview 有独立 validator / renderer，必须把其真实命令与结果写入 `RESULT.md`。

本任务 `ci_required=true`。Executor 完成后写 `RESULT.md`，提交实现并进入真实 CI；Scheduled Planner 在 CI 成功后独立检查 candidate manifests、geometry transfer、preview pixels、tests 与 scope boundary。
