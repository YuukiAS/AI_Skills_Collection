---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 025_research_presentation_gold_scientific_composition_library
decision: PLAN_FROZEN
---

# 025 Research Presentation Gold Scientific Composition Library — Plan

## Frozen decisions

本 Plan 只实现 Stage 2：从现有 inspected/downloaded 科研演示资源中筛出真正可用于 production runtime 的 Gold Scientific Composition Library，并证明选择结果会被运行时代码实际消费、改变 composition recipe。不得扩成 Stage 3 renderer/layout 实现或最终 holdout。

## Frozen objective

建立一条可验证链路：

```text
real scientific page job
-> retrieve only gold-compatible inspected compositions
-> select one or a small compatible set
-> consume normalized composition / hierarchy / annotation relations
-> emit downstream composition recipe / constraints
```

Gold 不是“下载过”“在 RRL 里”“019 有 composition record”就自动成立。每条 gold record 必须有真实 rendered-page identity、实际视觉成熟度证据、科学任务兼容性和明确复用边界。

## Required reading

Executor 至少读取：

- `automation/reviewed_handoff/schema.json`
- `automation/reviewed_handoff/README.md`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- 本任务 `REQUEST.md` / `PLAN.md` / `CURRENT.json`
- 019 的 PLAN / RESULT / REVIEW / FINAL_REPORT 与 composition schema、family vocabulary、records、validator、selector
- 020 的 PLAN / RESULT / REVIEW / FINAL_REPORT 与 source-geometry transfer / semantic compatibility 实现
- 021/022 的 comparative review artifacts，尤其真实 reference item 的 mature-bar judgement 与 reference-render identity 绑定方式
- `shared/references/research_slide_reference_index.csv`
- `shared/references/reference_sources_manifest.json`
- 当前 `research-presentations/SKILL.md`、`visual-qa.md` 与 source/generated presentations plugin mirror

## Implementation scope

### 1. Define a first-class gold admission contract

在 Presentation shared layer 增加小型、可序列化、可校验的 gold-composition record/index。可以复用 019 composition representation，但必须新增 gold admission 语义，而不是给全部 019 records 加一个 `gold=true`。

每条 gold record 至少记录：

- stable gold id；
- 对应真实 `reference_id` / source / actual page number；
- canonical rendered-page SHA 与本次 gold-admission reviewer input SHA（若运行时重新 materialize）；
- scientific job / page function；
- composition family；
- primary scientific object role、normalized bbox/area；
- supporting region roles；
- visual hierarchy、alignment、reading flow；
- annotation / legend / caption / panel relation；
- content-capacity / density envelope；
- portable composition lesson；
- rights/reuse boundary：至少区分 `COMPOSITION_ONLY`、`COMPARATIVE_GOLD`，若已有明确开放许可且 native reuse 合法可记录更宽权限，但不得凭猜测提升；
- gold-admission evidence：真实 rendered-page inspection 与 mature research-group-meeting / strong conference-talk 级别的视觉依据。

不得把 source-specific figure pixels、logo、版权素材或 donor branding 写入可复用 composition payload。

### 2. Re-screen existing inspected references; do not expand corpus

只在当前 repository 已有 inspected/downloaded reference universe 中筛选。不得因为某类覆盖不足就自动做外部 Source Scout；若现有 corpus 真有缺口，应在报告中明确为 Stage 2 coverage limitation，而不是无界下载。

Gold set 必须覆盖后续真实 paper deck 最常见的 scientific jobs，至少包括：

- motivation / research question；
- statistical model / estimator / theorem / proof intuition 中的数学主导页；
- method / experiment design；
- single quantitative result / uncertainty / comparison；
- negative result / failure / model check；
- medical-image aligned panels / overlay / error / zoom；
- discussion / next experiment。

允许一个 gold record 支持多个相邻 job，但不能用一个泛化 layout 伪装全覆盖。最终 gold set 应来自多个真实 source decks，避免单一作者/模板垄断整个库。

### 3. Gold admission must use actual pixels

每个拟进入 gold set 的页面必须基于真实 rendered pixels 做成熟度判断，不能只依据 RRL prose lesson、page title 或 metadata。

优先复用 021/022 中已经绑定实际 reference pixels 且有明确 mature-bar judgement 的 evidence；对没有足够已有视觉证据的拟入选页，使用现有 Bridge Kit / `gpt-5.6-terra` 机制做一次 bounded gold-admission visual packet。Terra 输入必须是真实 reference render，item-level 决策与观察写入 admission evidence。

Gold admission 不能只看 Terra top-level package PASS。页面若被 item-level 判为明显低于 mature group-meeting bar，应排除或降为普通 inspected reference，不得因为 coverage 需要强行纳入。

### 4. Build production-adjacent retrieval and selection

在 shared Presentation layer建立只读 gold selector / retriever，输入至少包含：

- scientific job / page function；
- dominant scientific object type；
- domain family（statistics/biostatistics/medical imaging 等）；
- content density / panel count / equation-vs-image-vs-plot emphasis；
- 必要的 evidence type。

选择前必须有 semantic compatibility gate，不能再次出现 020 第一轮那种因为通用词重叠而把无关 Bayesian model page 选给 medical-image overlay 的情况。

selector 输出必须保留为什么兼容、为什么被选择、哪些 gold candidates 被排除的 trace，但这些都只能用于内部 provenance，不得出现在 audience-facing slide。

### 5. Prove selected -> consumed -> output-affected

这是 025 的核心回归，不允许只证明“selector 返回了一个 ID”。

至少为两个不同 scientific jobs 做 deterministic runtime probes：

- 一个 statistics/biostatistics 数学或 quantitative-result job；
- 一个 medical-imaging image-comparison / failure-analysis job。

每个 probe 必须证明：

1. gold selector 真实选出 compatible record；
2. 下游 composition-recipe builder 实际读取该 record 的 normalized geometry / hierarchy / annotation relations；
3. recipe 输出包含 source-derived constraints，而不是 family 名称后再写死坐标；
4. 在保持 scientific content 不变时，替换为另一 compatible gold record 或屏蔽当前 record，会产生可解释的 recipe 差异；
5. 不允许为这两个 probe 写 test-specific hardcode。

这里的“output”是 Stage 3 将消费的 renderer-neutral composition recipe / constraints，不要求本任务生成最终 CUHK slide pixels。

### 6. Keep gold and general inspected library separate

保留现有 inspected reference library，不删除普通 records。Gold library 是其高质量 production subset，不应覆盖或篡改 019–022 历史记录。

至少提供：

- gold index/records；
- validator；
- selector；
- composition-recipe builder / adapter；
- gold-admission report；
- deterministic runtime trace/probe artifacts；
- source/generated mirror（若 shared/plugin 结构要求）。

### 7. Tests and validation

增加/更新测试至少验证：

- gold record 必须对应真实 inspected reference；
- page/source/render identity 绑定正确；
- rights/reuse boundary 非空且只使用允许枚举；
- gold admission evidence 存在且不是 metadata-only；
- semantic compatibility gate；
- selector 不返回明显不兼容 job；
- selected record 被 recipe builder 实际消费；
- record 替换会改变 source-derived recipe；
- audience-facing anti-meta leakage；
- source/generated mirror；
- 不修改 canonical CUHK template 本体。

继续运行 Presentation targeted tests、全库 tests、skills validation、marketplace validate/check/path-report、Reviewed Handoff validation 与 `git diff --check`。

## Out of scope

025 不得：

- 外部无界扩 reference corpus；
- 新建 Stage 3 的 LaTeX/TikZ/figure/image renderer 或 scientific layout macros；
- 修改 canonical CUHK template 视觉 identity；
- 恢复或修 023 PPTX renderer；
- 把 synthetic benchmark 当 gold source；
- 运行最终真实 statistical / medical-imaging paper holdout；
- 修改 Terra core / Bridge Kit reviewer semantics；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

## Validation

Executor 至少运行：

- gold-library / selector / recipe targeted tests；
- Presentation targeted tests；
- `python -m unittest discover -s tests`；
- `python scripts/skills.py validate`；
- marketplace build `--write --validate --check --path-report`；
- Reviewed Handoff validation；
- `git diff --check`；
- 若产生新的 gold-admission Terra packet，保存真实 item-level evidence 与 identity binding。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 025：

1. gold composition 是现有 inspected corpus 的明确高质量 subset，不是把全部 019 records 改名；
2. 覆盖后续真实科研汇报需要的主要 scientific jobs，且来自多个真实 source decks；
3. 每条 gold record 有真实 page/render identity、成熟度 evidence 与 rights/reuse boundary；
4. 拟入选页面基于真实 pixels 审核，低于 mature group-meeting bar 的页面不会为凑覆盖被强行纳入；
5. gold selector 有 scientific-job / object / domain / density 等语义兼容门槛；
6. statistics 与 medical-imaging 两个 runtime probe 都证明 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED`；
7. source-derived geometry/hierarchy/annotation relation 真正进入 renderer-neutral composition recipe，而不是只记录 provenance；
8. 替换 compatible gold record 会在相同科学内容下产生可解释 recipe 差异；
9. audience-facing contract 不泄漏 RRL/gold/QA/provenance/meta language；
10. 没有扩 corpus、没有实现 Stage 3 renderer/layout、没有修改 023 或最终 holdout；
11. required tests / validation / CI 全部通过；
12. `RESULT.md` 明确列出 gold coverage、被拒绝的候选及原因、runtime consumption evidence 与仍缺失的 page-job coverage。

025 PASS 只关闭 Stage 2。Planner PASS 后创建 Stage 3 — Executable CUHK Scientific Layout System 的独立 bounded task；Executor 不得自行继续。

## Plan Revision 1 — Targeted In-Corpus Gold Recovery

本次 revision 只解决 REVIEW_1 后出现的一个实质歧义：原 13 页 admission packet 中只有 `RRL-019` 与 `RRL-013` 达到新的 production-gold 像素级门槛，而 frozen Stage 2 又要求更广的 scientific-job 覆盖与 statistics / medical runtime proof。该冲突不得通过降低视觉标准、复用更旧且更宽松的 judgement，或外部扩 corpus 解决。

### Revision decision

采用**有界的现有库内重新筛选**。Executor 可以在当前 repository 已经 inspected/downloaded、已有真实 rendered-page identity 的 reference universe 中继续寻找候选，不限于第一轮的 13 页 packet；仍然禁止任何外部 Source Scout、下载新 deck、把未检查页面临时加入 corpus，或修改 019–022 的历史 evidence。

### Evidence precedence

- `025` 本轮 admission-specific Terra 对已经审过的 13 页具有当前 gold-admission 语义上的优先级。
- 对这些相同像素，不得用较旧的 021/022 comparative judgement 覆盖新的 `025` item-level `REVISE`；特别是 `RRL-028` 继续视为 **not admitted to production gold**。
- `RRL-019` 与 `RRL-013` 可保留为当前已准入 gold，但其用途仍受各自 scientific-job / domain compatibility 约束。
- 对尚未进入 025 admission packet 的页面，旧 evidence 只有在它本身明确对同一真实 rendered pixels 给出 mature-bar item-level judgement 时才可复用；否则必须走新的 admission packet。

### Bounded candidate expansion

为了避免把“重新筛选现有库”变成无界视觉搜索：

1. 只从现有 `research_slide_reference_index.csv` / `research_slide_composition_index.json` 中已有 inspected records 取候选，并排除已经在 13 页 packet 中被判 `REVISE` 的同一页面。
2. 先按当前 Stage 2 缺口做语义预筛，优先寻找：
   - statistics / biostatistics 的 mathematical model / estimator / theorem / quantitative-result；
   - single-result / uncertainty / comparison；
   - negative result / failure / model check；
   - motivation / research question；
   - discussion / next experiment；
   - 若需要支撑 medical alternate，再补同领域 image-comparison / failure-analysis。
3. 每个缺失 job family 最多送审 2–4 个最相关的现有 inspected candidates；新增送审总量最多 20 页，最多拆成 2 个 admission packets。不要为了凑满 20 页而送明显不兼容页面。
4. 所有新增候选仍必须基于真实 rendered pixels、匿名 item-level Terra judgement 与 reviewer-input SHA。`PASS` 才能进入 gold；`REVISE` 继续留在普通 inspected library。
5. 若在上述有界筛选后仍无法满足主要 coverage 或 runtime proof，不降低门槛、不外部扩库；明确写出 coverage limitation，并按 Reviewed Handoff 路由回 Planner / human decision。

### Runtime probe clarification

REVIEW_1 对 `force_gold_id` 的阻断结论保持不变：

- 删除 `score=999` / `forced compatible probe` 这类绕过正常 compatibility gate 的证明路径，或让任何显式 alternate 先通过与 production selector 相同的 compatibility validation。
- statistics 与 medical probes 的 baseline 必须由正常 selector 选择。
- alternate 优先采用“屏蔽 baseline 后由同一个 selector 选择下一条兼容 gold”的方式；若显式指定 alternate，也必须由 selector 的 compatibility check 证明兼容。
- trace 必须保存 baseline / alternate 的真实 compatibility reasons、被排除候选及 source-derived recipe 差异。
- 若某个 probe 在当前 gold set 下找不到第二个兼容候选，不得伪造 alternate；应把它作为 Stage 2 coverage limitation，而不是绕过门槛。

### Revision acceptance

本 revision 不改变原 Acceptance Gates，只明确关闭这次 Planner conflict。第二轮审核时，Planner 仍必须看到：

- 最终 gold index 中**每一条**记录都有一致、可追溯的像素级 admission evidence；
- 新 admission report 完整列出 admitted / rejected candidates，而不是只列 runtime baseline；
- 主要 scientific-job coverage 是由实际 admitted gold 支撑的；
- statistics 与 medical runtime probes 均通过正常语义兼容路径证明 selected -> consumed -> output-affected；
- 没有新 source、没有 Stage 3 实现、没有通过降低 mature-bar 标准来补覆盖。
