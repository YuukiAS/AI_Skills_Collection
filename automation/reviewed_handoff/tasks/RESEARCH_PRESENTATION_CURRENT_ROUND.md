# Research Presentation Current Round

当前仍属于 `REFERENCE_CALIBRATED_ONE_SHOT_QUALITY`，但产品路线已根据用户最终要求重新冻结。长期 `PROGRAM_MATURE=false`。

**Source of truth：** `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Five-Stage Closure Roadmap 与 Final Quality Gates。

## Human decision on 023

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
2. **Gold Scientific Composition Library**：从已经 inspected/downloaded 的成熟科研 slides 中筛 gold compositions，按真实 scientific job 进入 runtime；不无界扩 corpus。
3. **Executable CUHK Scientific Layout System**：把 gold composition 变成 CUHK content area 的 native LaTeX/TikZ/figure/image layouts；禁止退回 generic cards/box-arrow/default plot。
4. **One-Call Production Entry + Quality Loop**：普通 `research-presentations` 入口真实自动走 source fidelity、reference retrieval、generation、render、Terra item-level/page review、deck-rhythm review与 bounded repair。
5. **Two Real Paper Holdouts + Human Closure**：一篇真实 statistics/biostatistics/methodology paper + 一篇真实 medical-imaging paper，完整 one-shot CUHK group-meeting decks；Terra、Planner 均 PASS 后进入用户人工门，只有用户明确接受两套结果才可 `ONE_SHOT_QUALITY_PASS`。

## Completed: Stage 1 — Product Contract Reset

`024_research_presentation_product_contract_reset` 已在第一轮独立审核中 PASS，真实 CI 通过。

Stage 1 已真实改变 production contract：

- 未指定格式的科研组会 / paper talk / research update 默认 route 已改为 exact CUHK Beamer；
- `markdown_to_deck_plan.py` 普通 research 默认 output 已从 `pptx/editable` 改为 `tex/source-editable`；
- 显式 PowerPoint / `.pptx` / editable / Slides 请求仍可覆盖默认；
- exact CUHK canonical source 明确绑定 `shared/templates/cuhk/beamer/source/`；derived PPTX/scaffold 不再冒充 exact production source；
- required tests / validation / CI 已通过。

024 的 task-local PASS gate 不构成 program-level approval gate。

## Stage 2 — Current human decision point

当前任务：

`025_research_presentation_gold_scientific_composition_library`

025 已完成 Revision 1 的有界现有库 recovery，并在第二轮独立审核后达到 review limit。真实 CI 通过，REVIEW_1 的两个实现 blocker 已关闭：

- 最终 9 条 gold records 均有 025 item-level pixel `PASS` 与 identity binding；
- statistics / medical runtime probes 均通过正常 semantic compatibility 路径证明 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED`。

但冻结的 Stage 2 coverage 仍缺 `discussion / next experiment`：Revision 1 已额外送审 20 个现有 inspected candidates，达到有界筛选上限，仍无该类页面达到 production-gold item-level `PASS`。

因此 025 当前合法停在人工决策点，不创建第三轮 review，也不提前创建 Stage 3。

推荐的人工作品决策：保持 mature-bar 不变，授权一个新的、严格限定的 Stage 2 coverage recovery task，只针对 `discussion / next experiment` 缺口做小规模外部 source scouting / intake / real-pixel admission；保留现有 9 条 gold 和 025 历史 evidence。该 recovery PASS 后再进入 Stage 3。

备选方案是用户明确接受这一 coverage gap 并放宽 Stage 2 contract；Planner 不自行做该质量标准变更。

## Non-negotiable final acceptance

最终两个真实 paper deck 必须满足：

- 真实 paper notation / model / dataset / endpoint / figures / medical images 主导页面；不得用泛化 `alpha/beta/x/y` 占位符替代具体科研对象（除非它们本来就是 paper 的正式定义记号）；
- 不允许 rounded-card dashboard、空表格、generic box-arrow、默认流程图、默认 Matplotlib 脸、AI 元语言填页；
- 不是论文摘要分页，而是像优秀博士生真正读懂 paper 后给导师组会做的汇报；
- exact CUHK template 真实加载；
- 已下载/检查资源只有在 runtime selected/consumed 并改变输出时才算利用；
- Terra 必须读 item-level/page-level 质量，不能拿 top-level package PASS 冒充成熟质量；
- 正常 production entrypoint 真实工作；
- statistics 和 medical-imaging 两套完整 deck 都经过 Planner 独立验收；
- 最后由用户本人查看并明确接受。

任何 synthetic fixture、engineering mini-deck、单页 candidate、CI PASS、mechanical QA 或 Terra top-level `PASS` 都不能代替上述最终验收。
