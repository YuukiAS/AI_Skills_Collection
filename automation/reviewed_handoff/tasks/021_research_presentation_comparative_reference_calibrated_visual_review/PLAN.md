---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 021_research_presentation_comparative_reference_calibrated_visual_review
decision: PLAN_FROZEN
---

# 021 Research Presentation Comparative Reference-Calibrated Visual Review — Plan

## Frozen decisions

### Objective

把 020 已生成的内部候选真正放到成熟科研 slide 的相对质量坐标中：

```text
3 generated candidates
+
2–4 matched inspected reference renders
-> blinded comparative visual review
-> decoded candidate-vs-reference quality evidence
```

本任务只建立 **comparative reference-calibrated visual review**。它不修改 candidate geometry，不选定完整 deck design system，不生成最终 PPTX/Beamer，也不开始真实 holdout。

### Why this is the minimum next step

020 已证明“reference geometry 能产生多个不同 candidate”，但它没有证明任何 candidate 足够好。上一轮 10 页 synthetic pack 的主要失败就是：绝对 QA 很容易把“可读、正确、没有机械错误”误判成“成熟科研汇报”。

因此 021 必须改变评价问题：

> 不再只问这页有没有问题，而要问它与真正 inspected mature research slides 放在一起时，构图、排版和 scientific-object treatment 是否仍明显像程序化 fixture。

只有这一步成立，后续才有资格根据真实差距修 candidate layer 或锁定 deck-wide design system。

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
- `docs/AI_BRIDGE_VISUAL_REVIEW.md`
- `.github/workflows/ai-bridge-visual-review.yml`
- `skills/tools/documents-media/presentations/shared/references/research_slide_reference_index.csv`
- `skills/tools/documents-media/presentations/shared/references/research_slide_composition_index.json`
- 两个 020 candidate manifests / previews；
- 当前 Bridge Kit visual input adapter / prior 016–017 visual review manifests，理解现有 evidence contract，但不要照搬 absolute rubric。

## Implementation scope

### 1. Build two comparative review cases

继续使用 020 的两个受控 regression requests：

1. statistical estimator / equation page；
2. medical-image aligned comparison page。

每个 case 必须包含：

- 020 的 3 个 generated candidate previews；
- 2–4 个与该 page job 真正匹配的 inspected reference renders。

优先使用 020 candidate manifest 中实际作为 geometry source 的 reference pages，因为这样可以同时检查“从该 exemplar 学了 geometry 后，candidate 的视觉完成度到底保留了多少”。如需增加第三/第四个 reference，只能从 019/现有 inspected corpus 中按同 page function / scientific-object mode 检索，不扩 source corpus。

本轮预计最小集合可直接覆盖：

- estimator：RRL-028、RRL-014；
- medical image：RRL-022、RRL-013。

但 production builder 不得把这些 ID 写死成通用逻辑；task fixture / case spec 可以明确绑定本次受控 regression 的 reference identities。

### 2. Actual reference pixels are mandatory

不能把 composition record、RRL lesson、page title 或 bbox metadata 当作 reference visual evidence。

每个 reference item 必须真正取得 inspected page 的 pixels，并记录：

- `reference_id`（只存在内部 mapping）；
- `source_file_sha256` / inspected source identity；
- 019 `canonical_rendered_page_sha256`；
- **本次实际送给 Terra 的 `review_input_sha256`**；
- actual page number；
- materialization method / renderer；
- rights/public-safe note。

若本次 renderer 产生的 PNG bytes 与 019 canonical render 不同，不要求伪造 byte equality；必须同时保留 canonical SHA 与 actual reviewer-input SHA。真正参与本次视觉判断的 identity 以 `review_input_sha256` 为准。

如果无法恢复 inspected source 的真实 pixels，不能用 metadata 代替，也不能用相似页面顶替；该 case 应 BLOCKED 或选择另一个已 inspected 且真正兼容、可恢复 pixels 的 reference，并在内部 mapping 说明原因。

### 3. Do not commit reference pixels

继续遵守 reference library 的资产边界：下载/渲染的外部 reference page pixels 只用于本次 runtime visual review，不作为新的 repository visual corpus 提交。

允许：

- GitHub Actions runtime temporary files；
- `.cache` / ignored runtime directory；
- workflow artifact（若现有工具链需要，且不作为长期 source corpus）；
- 提交 SHA、page identity、materialization metadata、review output。

禁止：

- 把真实 reference screenshots / PDF pages 复制进 `docs/`、`skills/`、`plugins/`、`results/` 作为持久 binary baseline；
- 把 reference pixels 嵌入 candidate preview；
- 因为 transport 方便而改变 reference library 的版权/缓存边界。

如现有 generic visual-review workflow 无法在 GitHub runner 临时 materialize public-safe reference pages，允许增加一个**最小 consumer-side task workflow / preparation script**：在 runtime 下载并校验既有 public source、渲染指定页、建立匿名 input manifest，再调用现有 `ai-bridge visual-review run`。不得修改 Bridge Kit core / role / state machine。

### 4. Blind the reviewer to provenance and generated/reference identity

Terra-visible items 使用稳定但无语义的匿名 ID，例如 `item_A` … `item_F`。

Terra-visible manifest / filenames / descriptions / pixels 中不得出现：

- RRL / SRC ID；
- talk / author / institution name；
- repo path 中可识别 `candidate`, `reference_faithful`, `wildcard` 等身份的文件名；
- `generated` / `reference` / `gold` / `baseline` 标签；
- candidate strategy；
- “这是大牛 slide”之类先验提示。

为此，runtime 必须把所有图像复制/渲染成统一匿名文件名后再送审。

单独保存内部 `review_identity_map.json` 或等价 artifact，将 anonymous item ID 映射回：

- candidate ID / source reference ID；
- item class（candidate/reference）；
- source/preview SHA；
- actual reviewer-input SHA；
- page job；
- materialization provenance。

这个 mapping 不得作为 Terra prompt/context 的一部分。

### 5. Comparative rubric

为两个 case 分别建立 comparative visual input manifest，仍使用 Bridge Kit `gpt-5.6-terra`，但 rubric 必须是**相对质量审查**，不是旧 absolute checklist。

共同 rubric 至少要求 reviewer：

1. 逐个匿名 item 看真实 pixels；
2. 按共同 page job 判断 composition maturity，而不是比较不同研究结论谁“更科学”；
3. 明确评价：
   - composition / balance / whitespace；
   - typography hierarchy；
   - primary scientific object prominence；
   - equation / figure / medical-image treatment；
   - annotation / caption / legend integration；
   - visual specificity vs generic template；
   - natural academic language / audience-facing density；
   - AI-template / fixture / wireframe fingerprints；
   - projection readability；
4. 给出匿名 item 的相对 tiers / ordering，并说明关键差距；
5. 明确指出哪些 item 看起来达到 mature research-group-meeting / strong conference-talk level，哪些只是 technically readable；
6. 不因为某个 item 在当前集合里相对最好，就默认它“足够好”。

对于 estimator case，额外检查公式是否真正承担构图与叙事，而不是“把公式放大后放进框”。

对于 medical-image case，额外检查影像是否真正是视觉中心、panel correspondence / legend / annotation 是否自然，装饰容器是否压过 scientific image。

不要让 reviewer 根据 source prestige、作者、机构或 reference identity 判断。

### 6. Exactly one live Terra review per immutable case identity

每个 case 的匿名 items、实际 input SHA、rubric 与 page-job contract 组成 immutable review identity。

对同一 identity 只运行一次 live `gpt-5.6-terra`。如果图片、rubric、item mapping 的 Terra-visible部分或 input SHA 发生变化，才构成新 identity。

不要重复刷新同一输入“刷一个更喜欢的答案”。

本任务预计需要：

- 1 次 statistical comparative review；
- 1 次 medical-image comparative review。

Visual evidence 必须落在：

`results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/**`

可按 `statistical/`、`medical/` 分目录保存各自 `visual_inputs.json`、`VISUAL_REVIEW.json` 与 identity metadata。

### 7. Decode only after review

Terra evidence 写回后，再使用内部 identity map 生成 planner-readable comparative summary，例如：

`docs/audits/RESEARCH_PRESENTATION_COMPARATIVE_VISUAL_REVIEW_REPORT.md`

必须区分：

- blind reviewer 对匿名 items 的实际判断；
- 解码后哪个 item 是 candidate、哪个是真实 inspected reference；
- 每个 candidate 相对于 reference items 的主要质量差距；
- 是否存在“相对最好 candidate 仍明显低于 reference bar”的情况；
- 哪些差距属于下一 task 应修的 design/candidate 层，而不是继续加 reference metadata。

禁止 Executor 自行把 comparative evidence 转成整个 Program 的 PASS。

### 8. No forced winner

内部 summary / schema 必须允许至少这些语义：

- `CANDIDATE_NEAR_REFERENCE_BAR`
- `CANDIDATE_BELOW_REFERENCE_BAR`
- `NO_CANDIDATE_MEETS_REFERENCE_BAR`
- `BLOCKED_REFERENCE_PIXELS`

不要求把它们写成 Bridge Kit 的通用 decision token；可以只作为 021 consumer-side decoded summary vocabulary。

不能设置“总有一个 candidate winner”。如果三个 candidate 都明显弱于 reference，应明确保留 no-winner 结果，供 Planner 决定下一轮修 candidate layer。

### 9. Deterministic integrity checks

新增最小 validator / tests，至少检查：

- 每个 case 恰好包含 3 个 020 candidates；
- reference item 数量在 2–4；
- candidate SHA 与 020 manifest 对齐；
- reference item 来自 inspected composition/reference records；
- internal mapping 包含 canonical SHA 与 actual reviewer-input SHA；
- Terra-visible manifest 只使用匿名 IDs / anonymous runtime filenames；
- Terra-visible manifest 不含 RRL/SRC、作者、机构、candidate strategy 或 item class；
- 每个 input 的 declared SHA 与实际 bytes 一致；
- two cases 的 page-job contract 分别为 estimator/equation 与 medical-image comparison；
- visual evidence output 绑定 immutable input identity；
- 不提交 reference screenshots/pages；
- source/generated plugin mirror 只在确实新增 shared consumer code 时同步；
- required CI 通过。

不要建立任意“美观分数阈值”的 deterministic gate。

### 10. Implementation report

新增：

`docs/audits/RESEARCH_PRESENTATION_COMPARATIVE_VISUAL_REVIEW_REPORT.md`

至少说明：

- reference pixels 如何 materialize 与校验；
- 为什么 actual input SHA 与 canonical SHA 分开记录；
- anonymization 如何防止 provenance bias；
- 两个 case 各自有哪些匿名 items；
- Terra comparative rubric 与旧 absolute rubric 的关键差异；
- live Terra 的实际相对结论；
- 解码后的 candidate-vs-reference gap；
- 是否存在 no-winner；
- 下一步最小架构修复应由 evidence 决定什么；
- 当前为什么仍不能做 `ONE_SHOT_QUALITY_PASS`。

## Acceptance and regression gates

Planner/Reviewer 只有在以下全部满足时才可 PASS 021：

1. 两个 case 都真正包含 020 的三个 candidate 与至少两个真实 inspected reference renders；
2. reference pixels 真实参与 Terra，而不是 metadata/prose 替代；
3. actual Terra input SHA 被独立绑定；
4. reviewer 在 Terra-visible阶段不知道作者/机构/RRL/source，也不知道 item 是 generated 还是 reference；
5. 两个 case 各只对一个 immutable identity 执行一次 live Terra；
6. reviewer 输出包含逐 item 的相对成熟度/排序/差距，而不是只给全局 PASS；
7. 解码后能明确看到每个 candidate 与真实 reference bar 的关系；
8. no-winner 是合法结果，没有 best-of-bad 强制晋级；
9. 不提交外部 reference pixels，不修改 Bridge Kit core；
10. 不修改 020 candidate geometry 来追求 review 结果；
11. 没有提前开始 deck-wide lock、PPTX/Beamer final integration 或真实 holdout；
12. repository validation / required CI 全部通过。

注意：**021 的 PASS 表示 comparative review 机制可信，不表示 candidate 视觉质量已经 PASS。** 如果 comparative evidence 显示所有 candidate 都低于 reference bar，021 仍可以在机制正确的前提下 PASS，随后由 Planner 创建新的 design repair task。

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

如果新增 comparative input builder / integrity validator，必须运行真实命令并写入 `RESULT.md`。

如果需要 GitHub Actions runtime materialize reference pixels，必须记录真实 workflow run、source SHA 校验与 Terra evidence writeback；不得只在本地伪造 `VISUAL_REVIEW.json`。

## Out of scope

021 禁止：

- 扩 reference corpus / Source Scout；
- 修改 019 composition records；
- 修改 020 candidate geometry / preview skin 以追求更高评价；
- 修改 active `research-presentations/SKILL.md`；
- 修改 Bridge Kit core / state machine / reviewer role；
- 自动选择并锁定最终 deck design system；
- full-deck contact-sheet rhythm QA；
- real statistical holdout；
- real medical-imaging holdout；
- Beamer / PPTX renderer 重构；
- 宣告 `ONE_SHOT_QUALITY_PASS` / `PROGRAM_MATURE`。

## Handoff

完成后写 `results/021_research_presentation_comparative_reference_calibrated_visual_review/RESULT.md`，更新 `CURRENT.json` 到正确 CI/review handoff 状态并 push `origin/main`。

如果 live Terra 因 reference pixel transport、public-safe policy、secret、workflow 或 source SHA mismatch 无法真实运行，不得伪造 evidence；按实际原因 BLOCKED / handoff 给 Planner。
