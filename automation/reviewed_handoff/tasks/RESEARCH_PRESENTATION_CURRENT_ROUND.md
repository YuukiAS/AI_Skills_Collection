# Research Presentation Current Round

当前仍属于 `REFERENCE_CALIBRATED_ONE_SHOT_QUALITY`，长期 `PROGRAM_MATURE=false`。

**Source of truth：** `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Five-Stage Closure Roadmap、Quality-Preserving Continuation Policy 与 Final Quality Gates。

## Historical human decision on 023

`023_research_presentation_deck_design_system_integration` 保持历史 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`，不伪造第三轮，也不做 recovery。

用户决定：023 所修复的 low-level editable-PPTX design-profile renderer **不再是当前第一成熟 production route**。因此 023 作为 engineering history / reusable evidence 保留，但其剩余 spacing/caption/image-panel blocker 不再阻止新的 production program。

不要修改 023 的历史 REVIEW/CURRENT 为 PASS。

## Corrected product direction

第一成熟目标是：用户只给一篇真实科研 paper，普通 `research-presentations` 调用一次，即得到可直接用于博士组会的、exact CUHK 风格、内容具体、审美成熟、无明显 AI 模板感的完整 `.tex + PDF`。

未显式要求 editable PowerPoint 时，不再把 PPTX/scaffold 作为当前主路线。Exact CUHK 必须直接使用：

`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/`

现有 `design-tokens.json`、`pptx/build_reference_deck.py`、`cuhk-reference-deck.pptx` 只属于 derived/non-exact scaffold，不得作为 exact production visual source。

## Five stages

1. **Product Contract Reset**：修正式 skill/routing/tests，使普通科研组会默认 exact CUHK Beamer/PDF，并明确 023/PPTX scaffold 非当前 production default。
2. **Gold Scientific Composition Library**：从成熟科研 slides 中筛 production gold compositions，按真实 scientific job 进入 runtime。
3. **Executable CUHK Scientific Layout System**：把 gold composition 变成 CUHK content area 的 native LaTeX/TikZ/figure/image layouts；禁止退回 generic cards/box-arrow/default plot。
4. **One-Call Production Entry + Quality Loop**：普通 `research-presentations` 入口真实自动走 source fidelity、reference retrieval、generation、render、Terra item-level/page review、deck-rhythm review与 bounded repair。
5. **Two Real Paper Holdouts + Human Closure**：一篇真实 statistics/biostatistics/methodology paper + 一篇真实 medical-imaging paper，完整 one-shot CUHK group-meeting decks；Terra、Planner 均 PASS 后进入用户人工门，只有用户明确接受两套结果才可 `ONE_SHOT_QUALITY_PASS`。

## Completed: Stage 1 — Product Contract Reset

`024_research_presentation_product_contract_reset` 已在第一轮独立审核中 PASS，真实 CI 通过。

Stage 1 已真实改变 production contract：

- 未指定格式的科研组会 / paper talk / research update 默认 route 已改为 exact CUHK Beamer；
- 普通 research 默认 output 已从 `pptx/editable` 改为 `tex/source-editable`；
- 显式 PowerPoint / `.pptx` / editable / Slides 请求仍可覆盖默认；
- exact CUHK canonical source 明确绑定 `shared/templates/cuhk/beamer/source/`；derived PPTX/scaffold 不再冒充 exact production source。

## Completed: Stage 2 — Gold Scientific Composition Library

历史主体任务：

`025_research_presentation_gold_scientific_composition_library`

025 保持历史 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`，不改写为 PASS。它已经建立并验证 9 条 production gold、gold schema / validator / selector / renderer-neutral recipe builder，以及 statistics/biostatistics 与 medical-imaging 的正常 runtime consumption proof；唯一遗留缺口是 `discussion / next experiment` coverage。

质量保持 recovery：

`026_research_presentation_discussion_next_experiment_gold_recovery`

026 在第二轮独立审核中 PASS，真实 CI 通过。它没有降低 mature bar，而是在冻结的有限公开搜索空间中补入 `GSC-018`：

- 4 个公开 URL 被检查，其中 1 个 fetch 失败未 intake；
- 实际 intake/render 3 个 public decks；
- 12 个真实 rendered pages 经两批 Terra admission；
- 只有 `RRL-059 / SRC-077 / page 51` 达到 026 item-level pixel `PASS`，以 `GSC-018` / `COMPOSITION_ONLY` 进入现有 gold library；
- 正常 discussion/next-experiment selector 可以选中该 record，recipe builder 实际消费 source-derived composition fields；移除该 record 后得到 no-compatible-result，因此 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` 成立；
- 025 的既有 9 条 gold 与全部历史 evidence 保持不变。

因此 Stage 2 现在整体关闭。当前 production gold 已覆盖冻结 roadmap 要求的主要 scientific-job family，包括 motivation/research question、数学/统计模型与结果、method/experiment、negative/failure、medical-image comparison，以及 discussion/next experiment。

## Active: Stage 3 — Executable CUHK Scientific Layout System

当前 bounded task：

`027_research_presentation_executable_cuhk_scientific_layout_system`

Stage 3 的唯一目标是把 Stage 2 已验证的 renderer-neutral gold composition recipes 真正落成 **exact CUHK Beamer content area 内可执行、可编译、可复用的 native scientific layouts**。

本阶段必须保持三个边界：

- CUHK identity 来自 canonical `beamer/source/`，不得用 derived PPTX/design tokens 仿制；
- 页面几何必须能追溯到正常 selector -> gold recipe -> CUHK content-space mapping，不能退回 task-specific 手写坐标或 generic cards；
- Stage 3 只建立 layout system 和真实 render/visual evidence，不接普通 one-call production entry，不运行最终真实 paper holdout；这些属于 Stage 4/5。

027 独立 PASS 后，Stage 3 才整体关闭并进入 Stage 4。

## Standing workflow decision — preserve quality before asking human

用户已明确：本 Presentation program 始终按最高冻结质量标准推进，不允许为了少一轮 review、少搜资源或更快进入下一 Stage 而偷工减料。

后续若 review limit 到达，而唯一实质选择是“创建一个范围清楚、质量保持的 bounded recovery”或“放宽已有质量合同”，Planner 自动选择前者，不再要求用户重复授权。保持每个 bounded task 的少量 review 上限，用新的 recovery task 隔离新增 scope；只有真正涉及产品/科学语义冲突、明显新的成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终两套 deck 验收时才进入真正需要用户决定的 human gate。

## Non-negotiable final acceptance

最终两个真实 paper deck 必须满足：

- 真实 paper notation / model / dataset / endpoint / figures / medical images 主导页面；不得用泛化占位符替代具体科研对象；
- 不允许 rounded-card dashboard、空表格、generic box-arrow、默认流程图、默认 Matplotlib 脸、AI 元语言填页；
- 不是论文摘要分页，而是像优秀博士生真正读懂 paper 后给导师组会做的汇报；
- exact CUHK template 真实加载；
- 已下载/检查资源只有在 runtime selected/consumed 并改变输出时才算利用；
- Terra 必须读 item-level/page-level 质量，不能拿 top-level package PASS 冒充成熟质量；
- 正常 production entrypoint 真实工作；
- statistics 和 medical-imaging 两套完整 deck 都经过 Planner 独立验收；
- 最后由用户本人查看并明确接受。

任何 synthetic fixture、engineering mini-deck、单页 candidate、CI PASS、mechanical QA 或 Terra top-level `PASS` 都不能代替上述最终验收。
