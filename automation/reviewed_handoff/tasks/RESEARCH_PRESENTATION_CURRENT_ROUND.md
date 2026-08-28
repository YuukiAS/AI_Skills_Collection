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

033 没有取得与当前实现绑定的完整 deck/contact-sheet item-level visual quality PASS，因此保留 review-limit 历史，由 034 质量保持 recovery 接续。

### 034 Render Identity CI Recovery — review limit history

`034_research_presentation_render_identity_ci_recovery` 已完成两轮独立审核并合法停在 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`；不得创建 `REVIEW_3` 或改写成 PASS。

034 已真实关闭 033 的 evidence-identity 根问题：

- 始终存在的 render-input identity 直接绑定实际 `main.tex`、`scientific_layouts.tex`、canonical CUHK support 与必要 scientific assets；
- no-render CI path 明确允许 pixel evidence unavailable，不伪造 page/contact-sheet SHA；
- real-render path 继续严格绑定 per-page PNG、contact sheet 与 PDF；
- deterministic repair 改变真实生产表示时，render-input identity 随之改变；
- 真实 GitHub `Codex Marketplace` CI 已通过。

034 第一轮 visual review 又发现并修复了两个 presentation blocker：标题页工程元语言泄漏被移除并加入通用 metadata anti-leak gate；统计模型页从公式+单句的明显欠填充状态补足为公式主对象、模型角色与解释层。修复后 fresh Terra 对六个内容页及整套 `deck_contact_sheet` 均给出 item-level `PASS`，确认当前工程样例的 CUHK 身份、跨页节奏、workstream transition 与医学影像语义均成熟可评估。

034 第二轮独立代码审核仍发现唯一 blocker：共享 `STATISTICAL_MODEL` equation renderer 的 supporting copy 里残留当前 clustered-calibration fixture 专用文本，包括 `Calibration link`、固定 ICC/center-variation/interval-comparison caption，以及缺少 scientific objects 时的 `Source-grounded terms...` 制作型 fallback。当前 engineering fixture 恰好语义匹配，所以 Terra 像素 PASS 不能证明这一 normal production path 对未见模型 source-faithful。这个 finding 直接违反 034 Review 1 已冻结的“supporting content 必须由通用 source/page-job fields 驱动、不得按当前 clustered fixture 术语写死”的修复边界。

该 blocker 不需要用户改变产品/科学语义，且存在唯一、范围清楚、质量保持的新机制，因此按 Quality-Preserving Continuation Policy 自动进入 035；034 的 dual identity、title anti-leak 与已通过视觉证据全部保留，不重做。

### 035 Generic Model Support Recovery — review limit history

`035_research_presentation_generic_model_support_recovery` 已完成两轮独立审核并合法停在 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`；不得创建 `REVIEW_3` 或改写成 PASS。

035 的原始 generic-model source-grounding blocker 已被真实关闭：

- shared `STATISTICAL_MODEL` renderer 不再无条件输出 `Calibration link`、固定 ICC / center-variation / interval-comparison supporting caption 或 `Source-grounded terms` 制作型 fallback；
- supporting model body 只消费当前 spec/source 的 scientific objects、key message、annotation 等 source-backed fields，允许中性布局标签但不携带当前 fixture 科学结论；
- unrelated Cox regression 真实经过同一共享 model path，并证明不会泄露 clustered-calibration 专用术语；
- 当前 engineering model page 继续保持公式主导、信息完整，fresh Terra 对 `slide_2_statistical_model` 给出 item-level `PASS`；
- shared/plugin parity 与真实 GitHub `Codex Marketplace` CI 已通过。

035 第一轮只允许对模型页做 in-scope 视觉重平衡，并明确冻结 slides 3–7。第二轮 fresh Terra 与 implementation/render/pixel/contact-sheet identity 一致后，模型页继续 PASS，但最新完整审查把两个此前未变化的 process pages 判为 `REVISE`：

- `slide_4_experiment_design` 的中央 DGP → hierarchy → procedures → endpoints pipeline 相对可用画布明显过小，上下留白过多，endpoint 与 connector annotations 投影字号偏小；
- `slide_6_next_experiment` 的 failure evidence、sampling/manipulation、comparators 与 decision-rule copy 仍偏小；
- `deck_contact_sheet` 因 slides 4 / 6 的 density / scale dips 未稳定达到 strong projection-ready doctoral group-meeting bar。

slides 4 / 6 的当前 PNG SHA 与 034 当时 item-level PASS 的像素完全一致，因此这不是 035 引入的 regression；但 Program Goal 要求使用当前 fresh evidence，而不能挑选旧 PASS 覆盖新的真实质量发现。由于 035 已用满两轮且 Review 1 禁止越界修改 slides 3–7，本任务保留 terminal history，不在 035 内继续修复。

这个新 blocker 不需要用户改变产品/科学选择，也不需要降低质量门槛；共享 `EXPERIMENT_DESIGN` / `NEXT_EXPERIMENT` geometry/emission 已提供一个新的、范围清楚的 bounded implementation mechanism，因此按 Quality-Preserving Continuation Policy 自动进入 036。

### Active bounded recovery — 036 Process Page Projection Recovery

当前 active task：

`036_research_presentation_process_page_projection_recovery`

036 只处理当前 fresh Terra 已明确指出的两个 process-page projection-scale 问题：

- 通用放大/重排共享 `EXPERIMENT_DESIGN` scientific pipeline，让 source-backed DGP factors、hierarchy、procedures、endpoints 与 connector annotations 更充分使用 CUHK safe region 并达到投影可读尺度；
- 通用放大/重排共享 `NEXT_EXPERIMENT` evidence-to-decision path，让 prior failure、sampling/manipulation、comparators 与 decision rule 在成熟字号下形成连续推理；
- 修复只能依据 page-job/general capacity/layout semantics，不得按当前 clustered fixture 的标题、术语、页号或 test ID 写死；
- 不新增无来源科学内容，不以 generic filler/cards/box-arrow 假装密度；若一页容量无法在成熟字号下容纳现有内容，必须走现有 capacity/no-winner/split/fail-closed 路线，而不是缩小字体强塞；
- 增加与当前 fixture 文案解耦的 bounded regressions，直接约束两类 page-job 的 projection geometry / readability mechanism；
- 035 model source-grounding、034 dual identity/title anti-meta、032 storyline、多 workstream transition、gold retrieval、exact CUHK identity、result/failure/medical 页面、medical TP/FP/FN、一次 repair budget 全部冻结保护；
- shared/plugin parity、targeted/full tests 与真实 GitHub CI 必须通过；pixels 改变后必须等待 task-local fresh Terra，至少 `slide_4_experiment_design`、`slide_6_next_experiment`、`deck_contact_sheet` 全部 item-level `PASS`，且 model/result/failure/medical 等无新的 blocker。

036 不运行 Stage 5 holdout、不扩 corpus、不重写 deck-quality-loop 状态机。其停止条件是：两类 process-page projection mechanism 经 bounded regression 成立，当前 slides 4 / 6 与 contact sheet 获得 fresh item-level PASS，真实 CI 闭合且冻结能力无回归。

036 独立 PASS 后，Planner 才可重新判断 Stage 4 是否整体首次 PASS。若 Stage 4 整体 PASS，应发送一次 Stage 4 旁路 notifier，并随后创建 Stage 5 的真实双-paper holdout bounded task；不得跳过 Stage 5 最终用户人工门。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不要求用户在“继续保持质量”和“降低质量”之间重复选择。
- 每个 bounded task 最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- Stage 1–4 某 stage 首次独立 PASS 时发送一次旁路 notifier，但 notifier 不是 approval gate，不暂停后续 stage。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终双 deck 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须从正常 `research-presentations` production entrypoint 对两个未参与调优的真实公开 paper one-shot 生成完整 CUHK 组会 deck：statistics/biostatistics/methodology 一套、medical imaging 一套。真实 paper notation/data/figures/images 必须主导内容；不得 generic cards/box-arrow/default plot/AI 元语言；Terra 必须读 item/page-level judgement，Planner 必须独立审真实 source/trace/render；两套 deck 都通过后仍必须进入用户最终人工门。只有用户明确接受两套结果才允许 `ONE_SHOT_QUALITY_PASS`。
