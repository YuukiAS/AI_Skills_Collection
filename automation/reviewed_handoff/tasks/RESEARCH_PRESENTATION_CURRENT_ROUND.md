# Research Presentation Current Round

当前仍属于 `REFERENCE_CALIBRATED_ONE_SHOT_QUALITY`，长期 `PROGRAM_MATURE=false`。

**Source of truth：** `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Five-Stage Closure Roadmap、Quality-Preserving Continuation Policy 与 Final Quality Gates。

## Historical decision on 023

`023_research_presentation_deck_design_system_integration` 保持历史 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`，不伪造第三轮。其 low-level editable-PPTX design-profile renderer 不再是第一成熟 production route；当前 production contract 以 canonical exact CUHK Beamer `.tex + PDF` 为主。

## Completed stages

### Stage 1 — Product Contract Reset

`024_research_presentation_product_contract_reset` 已独立 PASS。普通科研组会 / paper talk / research update 未指定格式时，默认走 exact CUHK Beamer/source-editable TeX；显式 PowerPoint/PPTX/Slides 仍可覆盖。Exact CUHK identity 绑定 `skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/`，derived PPTX/scaffold 不得冒充 exact production source。

### Stage 2 — Gold Scientific Composition Library

`025_research_presentation_gold_scientific_composition_library` 保留历史 review-limit 终态；其唯一 coverage gap 由 `026_research_presentation_discussion_next_experiment_gold_recovery` 质量保持 recovery 关闭。026 第二轮独立 PASS，真实 CI 通过。

当前 production gold 已覆盖 roadmap 所需主要 scientific jobs。026 新增 `GSC-018`，来自真实 rendered-pixel item-level Terra `PASS` 的 discussion / next-experiment 页面；正常 selector 可选择它，recipe builder 实际消费 source-derived composition fields，移除后得到 no-compatible-result，因此 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` 已成立。Stage 2 整体关闭。

### Stage 3 — Executable CUHK Scientific Layout System

Stage 3 已首次整体 PASS。

`027_research_presentation_executable_cuhk_scientific_layout_system` 建立核心工程链；027 第二轮达到 review limit 后保留历史终态。028 独立关闭旧 visual dispatch gap；029 完成 task-local Visual Review consumer adaptation；质量保持 recovery `030_stage3_visual_recovery` 在第二轮独立审核中 PASS。六个主要内容页均达到 item/page-level mature research-group-meeting / strong conference-talk bar，证明成熟 gold composition 可以在 exact CUHK content area 中执行为 statistical model、quantitative result、experiment design、negative result、medical comparison 和 next experiment 布局。

Stage 3 PASS 不等于普通用户一次调用已经完成全部生产质量循环，也不等于最终真实 paper holdout 通过。

## Stage 4 — active

### 031 One-Call Production Entry — review limit history

`031_research_presentation_one_call_production_entry` 已完成两轮独立审核并合法停在 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`；不得创建 `REVIEW_3` 或改写成 PASS。

031 已真实建立 normal file/path entry -> source-fidelity map -> storyline/page jobs -> normal gold retrieval -> Stage 3 executable layouts -> canonical CUHK `.tex + PDF` -> real render -> task-local visual-review handoff。repair 后 canonical CUHK identity 与 same-case medical TP/FP/FN semantics 均通过真实像素审查。031 最终唯一 blocker 是 multi-workstream deck-level storyline coherence。

### 032 Storyline Coherence Recovery — PASS

`032_research_presentation_storyline_coherence_recovery` 已在第二轮独立审核中 PASS，真实 CI 与 fresh task-local Terra 均通过。

032 关闭了 031 的 storyline blocker，并把实现从 fixture-specific domain token profile 修成通用 source/page-job workstream contract：

- shared production generator 不再维护 clustered-calibration / segmentation 两套领域专用分类词表；
- normal path 优先消费显式 `workstream` metadata，缺失时使用 evidence-board fallback；
- 当前统计主线连续保持 `STATISTICAL_MODEL -> REAL_DATA_APPLICATION -> EXPERIMENT_DESIGN -> NEGATIVE_RESULT -> NEXT_EXPERIMENT`；
- medical comparison 作为第二个独立 workstream，并明确不虚构 causal bridge；
- 新增与当前两个领域无关的双-workstream regression，证明机制不是当前 fixture hardcode；
- 单-workstream 输入不会被强制插入多余 transition。

fresh Terra 对六个主要内容页全部 item-level `PASS`，并确认 coverage 主线连续、medical transition 可见且 031 已通过的 CUHK identity / medical semantics 无回归。

032 PASS 只表示 production storyline 已关闭；Stage 4 仍需完整 deck-level rhythm review 与 bounded quality-repair loop。

### 033 Deck Rhythm + Bounded Quality Loop — review limit history

`033_research_presentation_deck_rhythm_quality_loop` 已完成两轮独立审核并合法停在 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`；不得创建 `REVIEW_3` 或改写成 PASS。

033 已真实建立并保留以下共享生产能力：完整 deck contact sheet / sequence summary、deck-level reviewer-evidence consumer、受限 repair intent、automatic repair cycle 上限 1、unknown/unsafe finding fail-closed / no-winner，以及 task-local Visual Review 对 page/contact-sheet/build/quality-loop evidence 的绑定。它没有使用 Stage 5 holdout，也没有引入 033-only production generator。

Review 1 的 clean-run contact-sheet manifest blocker 已局部修复，但第二轮真实 `Codex Marketplace` CI 再次失败并把剩余问题收敛为一个 evidence-identity 语义缺口：

- GitHub runner 无真实 PNG render 时，`rendered_page_sha256` 合法为空，但 clean regression 仍无条件把它当成 64-char pixel SHA；
- deterministic `ADJUST_TRANSITION_CUE` repair 已真实改变 production `deck_plan` 与 `main.tex`，但当前 `deck_identity_sha256` 主要绑定 page-order / pixel SHA / contact-sheet SHA 等字段；在 no-render runner 中 pixel SHA 都不存在，导致 initial 与 repaired identity 相同，无法证明 actual render input 已改变。

当前 033 visual-review 目录没有 fresh `VISUAL_REVIEW.json`。对应 Visual Review workflow 的 top-level success 不能替代 deck/contact-sheet item-level judgement，因此 033 没有进入视觉质量 PASS。

### Active bounded recovery — 034 Render Identity CI Recovery

当前 active task：

`034_research_presentation_render_identity_ci_recovery`

034 是 033 review-limit 后按 Quality-Preserving Continuation Policy 自动创建的最小 recovery；不需要用户决定，也不降低任何质量门槛。它使用与 blocker 对应的新有限机制，而不是继续逐项放宽 validator/test：

- 明确区分始终存在的 **render-input / production-representation identity** 与只有真实渲染成功后才存在的 **rendered-pixel identity**；
- render-input identity 必须直接绑定本次实际生成的 `main.tex`、`scientific_layouts.tex` 和必要 scientific asset SHA，因此即使 CI 没有完整 TeX/PNG 栈也能审计“送去渲染的东西是否发生变化”；
- no-render path 不得伪造 page/contact-sheet pixel SHA，而要 machine-readable 地标记 pixel evidence unavailable；
- real-render path 继续严格核对真实 per-page PNG SHA、contact-sheet SHA 和 task-local visual manifest binding；
- deterministic transition repair 前后 render-input identity 必须不同，并保留 regression 对实际 `deck_plan` / `main.tex` 变化的直接检查；
- 033 已有 contact sheet、deck-level rubric、一次 repair budget、fail-closed/no-winner、source fidelity、032 storyline、gold/layout、CUHK identity 与 medical semantics 全部冻结保护。

034 必须先通过修复后的 targeted/full regression 与真实 GitHub CI；之后再按现有 task-local Visual Review contract等待 fresh deck/contact-sheet item-level evidence。缺 visual evidence 时只等待，不消耗 review round。

034 独立 PASS 后，Planner 才可重新判断 Stage 4 是否整体首次 PASS。若 Stage 4 整体 PASS，应发送一次 Stage 4 旁路 notifier，并随后创建 Stage 5 的真实双-paper holdout bounded task；不得跳过 Stage 5 最终用户人工门。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不要求用户在“继续保持质量”和“降低质量”之间重复选择。
- 每个 bounded task 最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- Stage 1–4 某 stage 首次独立 PASS 时发送一次旁路 notifier，但 notifier 不是 approval gate，不暂停后续 stage。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终双 deck 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须从正常 `research-presentations` production entrypoint 对两个未参与调优的真实公开 paper one-shot 生成完整 CUHK 组会 deck：statistics/biostatistics/methodology 一套、medical imaging 一套。真实 paper notation/data/figures/images 必须主导内容；不得 generic cards/box-arrow/default plot/AI 元语言；Terra 必须读 item/page-level judgement，Planner 必须独立审真实 source/trace/render；两套 deck 都通过后仍必须进入用户最终人工门。只有用户明确接受两套结果才允许 `ONE_SHOT_QUALITY_PASS`。
