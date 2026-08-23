---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 023_research_presentation_deck_design_system_integration
decision: PLAN_FROZEN
---

# 023 Research Presentation Deck-Wide Design-System Integration — Plan

## Frozen decisions

This plan is frozen for 023. The frozen objective, implementation scope,
acceptance gates, validation, and out-of-scope boundaries below are binding for
the Executor. This section is a schema-compatible heading; it does not add work
beyond the already frozen task.

## Frozen objective

把 019–022 已验证的单页能力接入完整多页生成链，建立 renderer-neutral 的 **deck design profile**：统一 typography、palette、spacing、caption/annotation、chart/diagram/image/equation treatment，但不统一每页 composition。目标是证明“同一 deck 有一个稳定设计系统，同时不同 scientific page function 仍由 matched exemplar / composition family 决定布局”。

023 仍是工程与生成集成任务，不是最终 design-quality holdout，也不是 contact-sheet rhythm closure。

## Required reading

Executor 至少读取：

- `AGENTS.md`
- Reviewed Handoff schema / README / Executor prompt
- `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- 019–022 的 FINAL_REPORT / REVIEW 与相关 audit reports
- 019 composition schema / selector / validator
- 020 candidate generator / manifests
- 021 comparative preparation / identity map / review decoder
- 022 visual-finish renderer / candidate manifests
- current research-presentation skill / shared visual QA / deck-plan schema

## Implementation scope

023 implementation is limited to deck-wide design-system locking and
multi-page generation integration as detailed below. It must not expand the
reference corpus, redefine the reviewer, start real holdouts, or declare
program maturity.

## 1. Add a renderer-neutral deck design profile

新增一个最小、可验证的 design-profile representation。建议位置在 Presentation shared layer；source 与 Codex plugin mirror 必须保持一致。

profile 至少区分：

### Deck-wide locked properties

- primary / secondary font family；
- title / subtitle / body / caption / annotation / equation type scale；
- background / ink / muted / accent / warning / uncertainty 等 color roles；
- spacing scale / outer margins；
- line / connector / annotation-leader semantics；
- chart typography / axis / legend / uncertainty style；
- image-panel label / shared legend treatment；
- equation highlight / brace / leader treatment；
- caption / qualifier treatment；
- page number / section chrome（若启用）。

### Page-local properties

不得锁死：

- scientific-object bbox；
- exact layout family；
- panel count；
- equation / image / plot / diagram 的相对位置；
- annotation target；
- page-specific accent placement。

这些仍由 page function + matched composition record / candidate geometry 决定。

profile 必须可序列化、可校验，并记录 provenance：来自当前 deck 的 audience / medium / content density、共享 visual tokens，以及哪些值来自 reference-informed candidate layer。不要把某个 022 benchmark 的绝对坐标写入 profile。

## 2. Integrate design profile with reference-calibrated multi-page generation

建立 shared multi-page generation adapter / renderer，使每页流程为：

```text
deck plan slide
-> scientific page job
-> retrieve compatible inspected composition records
-> derive candidate / chosen composition geometry
-> apply locked deck design profile
-> render native slide objects
```

关键要求：

- design profile 控制视觉语言，不控制 scientific composition；
- 019 source geometry 仍真实进入 page geometry；
- 020 semantic compatibility gate 继续有效；
- 022 的 presentation-native equation / image primitives 被复用，而不是重新复制一套 task-specific drawing code；
- audience-facing 页面不出现 RRL/SRC、candidate strategy、QA/provenance/meta language；
- 不允许所有页面自动回落成统一 `title + subtitle + central object + footer` grammar；
- 不允许 default rounded-card scientific containers、无信息装饰条/阴影。

## 3. Controlled multi-page integration fixtures

为了验证 deck-wide lock，而不是再次用 synthetic toy 证明最终质量，本任务使用**工程 fixture**，并明确标记不构成 holdout。

生成两个小型 coherent mini-decks，每套建议 4–5 页：

### Statistical mini-deck

至少覆盖：

- estimator / equation；
- experiment / simulation design；
- quantitative result figure；
- negative result / next experiment。

### Medical-imaging mini-deck

至少覆盖：

- image-grounded task / target；
- experiment / method path；
- quantitative result；
- same-case image / GT / prediction / error comparison。

可以复用既有 deterministic public-safe synthetic inputs作为工程 fixture，但：

- 不得把上一轮 10 页 baseline 当 gold visual template；
- 不得以 synthetic mini-deck 的视觉通过宣称最终科研质量；
- 每页必须重新走当前 reference-composition / design-profile pipeline，而不是复制旧 PPT 页面。

至少一个输出必须是真正 editable PPTX；本 task 两套都优先使用 PPTX，以集中验证 native multi-page integration。Beamer 留给后续独立任务/holdout。

## 4. Composition diversity must survive design-system locking

新增 deterministic regression，证明 design-profile lock 不会把页面压成同一模板：

- 一个 mini-deck 内至少出现 3 种不同 major composition families；
- consecutive slides 不得全部使用同一 major family；
- equation page、result figure page、medical image page 的 primary scientific-object role 必须不同；
- source-derived normalized primary bboxes 在不同 page jobs 上保持差异；
- 同一 profile 下，颜色/字体/spacing 保持一致。

不要使用任意“美观分数”。这些检查只验证结构一致性与多样性，不替代视觉 reviewer。

## 5. Native PPTX and real render

生成真实 editable PPTX，并通过 real presentation engine 得到 PDF / PNG。

必须保存：

- deck plan；
- locked design profile；
- per-slide reference/composition provenance；
- PPTX；
- PDF；
- rendered PNG；
- mechanical QA；
- source/generated identity manifest。

如果环境无法真实 render PPTX，则按现有协议 BLOCK，不得手工重建 parallel PDF 冒充。

## 6. Minimal visual review for integration correctness

023 不负责正式 contact-sheet rhythm gate，但 Planner 必须能看到真实 rendered pages。

Executor 可以生成调试 montage/contact sheet，但不得把“有 montage”写成下一阶段 rhythm QA 已完成。

本 task 的视觉检查只回答：

- deck-wide type / color / spacing 是否明显漂移；
- page-specific composition 是否仍有差异；
- 022 已验证的 equation / image treatment 是否在 multi-page PPTX 中保持；
- 是否重新出现 card/dashboard / internal-meta leakage / generic footer 等明显回归。

不要求新建一套 Terra 机制；如调用 Terra，只能作为当前 integration evidence，不能替代下一 bounded task 的正式 deck-rhythm comparative QA。

## 7. Do not hardcode reviewer winners

不得读取 021/022 的 anonymous item ordering 后把某个 `candidate_strategy` 永久写死成全局 winner。

本 task 可以为 controlled fixture 明确指定 page composition 用于集成回归，但必须写在 fixture/deck plan 层，并明确：这只是 integration fixture，不是未来 one-shot 自动 winner-selection policy。

设计系统必须对不同 composition strategy 都可用。

## 8. Tests and validation

至少增加/更新测试验证：

- design profile schema / validator；
- deck-wide locked tokens 在多页保持一致；
- page-local geometry 没被 profile 覆盖；
- 019 geometry / 020 semantic compatibility regressions继续通过；
- 022 visual-finish manifest semantics继续通过；
- audience-facing anti-meta leakage；
- 至少 3 个 major composition families / mini-deck；
- source/plugin mirror；
- PPTX 打开/结构有效；
- real render status / mechanical QA。

标准全库验证继续执行：Presentation targeted tests、全库 tests、skills validate、marketplace validate/check/path-report、Reviewed Handoff validate、`git diff --check`。

## Out of scope

023 不得：

- 扩 reference corpus；
- 修改 Bridge Kit core；
- 修改 019 composition records；
- 重新定义 comparative reviewer；
- 把 022 某个 candidate strategy 写成全局 winner；
- 宣告 contact-sheet / deck-rhythm QA 已完成；
- 开始 real statistical / medical-imaging holdout；
- 开始 Beamer holdout；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

## Acceptance and regression gates

Planner 只有在以下全部满足时才可 PASS 023：

1. renderer-neutral deck design profile 存在且区分 locked vs page-local properties；
2. 至少两个 coherent multi-page engineering mini-decks 使用同一 shared integration path生成；
3. design profile 的 type / color / spacing / annotation / equation / image treatment 在 deck 内稳定；
4. 页面仍按 scientific page job 使用不同 composition，至少 3 个 major families / mini-deck；
5. source-derived page geometry 仍进入 per-slide layout，未被统一模板覆盖；
6. 022 equation / medical-image visual-finish semantics 在 multi-page PPTX 中保持；
7. audience-facing 无 RRL/SRC/candidate/QA/provenance/meta leakage；
8. 没有明显重新出现 rounded-card dashboard、机械 footer、统一四段式模板脸；
9. 真实 editable PPTX -> PDF/PNG render 成功，mechanical QA PASS；
10. required CI / repository validation PASS；
11. 不把工程 fixture 当最终 design-quality holdout，不提前宣告 rhythm QA 或长期完成。

023 PASS 后，下一 bounded task 才能进入正式 **contact-sheet / deck-rhythm QA**。
