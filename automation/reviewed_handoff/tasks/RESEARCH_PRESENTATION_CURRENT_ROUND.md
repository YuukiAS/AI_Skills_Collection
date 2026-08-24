# Research Presentation Current Round

当前仍属于 `REFERENCE_CALIBRATED_ONE_SHOT_QUALITY`，但产品路线已根据用户最终要求重新冻结。长期 `PROGRAM_MATURE=false`。

**Source of truth：** `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Five-Stage Closure Roadmap、Quality-Preserving Continuation Policy 与 Final Quality Gates。

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

## Stage 2 — Active coverage recovery

历史 task：

`025_research_presentation_gold_scientific_composition_library`

025 已完成 Revision 1 的有界现有库 recovery，并在第二轮独立审核后达到 review limit。真实 CI 通过，REVIEW_1 的两个实现 blocker 已关闭：

- 最终 9 条 gold records 均有 025 item-level pixel `PASS` 与 identity binding；
- statistics / medical runtime probes 均通过正常 semantic compatibility 路径证明 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED`。

冻结的 Stage 2 coverage 仍缺 `discussion / next experiment`：Revision 1 已额外送审 20 个现有 inspected candidates，达到有界筛选上限，仍无该类页面达到 production-gold item-level `PASS`。

025 历史继续保持 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`，不得伪造第三轮或改写成 PASS。

用户已授权新的、严格限定的 Stage 2 coverage recovery；Planner 已创建并冻结：

`026_research_presentation_discussion_next_experiment_gold_recovery`

026 只处理 `discussion / next experiment` coverage gap：

- 保留现有 9 条已通过 gold、selector、runtime probes 与全部 025 evidence，不重审、不重做已 PASS 部分；
- 保持 production-gold mature bar，不允许为了推进 Stage 3 而放宽 coverage/视觉质量合同；
- 允许一次新的、有界、rights-safe 的公开 source scouting / intake / real-pixel Terra admission；
- 搜索资源上限固定为最多检查 8 个公开 source URLs、最多 intake 4 个 decks、最多 Terra 审查 12 个真实 rendered pages、最多 2 个 admission packets；
- 新候选只有真实 rendered-pixel item-level mature-bar `PASS` 才能进入 production gold；
- 一旦至少一个成熟 discussion / next-experiment gold 被正常 selector 选择、recipe builder 消费并证明 output affected，即停止 scouting；
- 不得开始 Stage 3 renderer/layout，不得修改 023 或最终 holdout。

当前 026 已 `PLAN_FROZEN`，下一步交给 Codex Executor。026 独立 PASS 后，Stage 2 才可整体视为关闭，并进入 Stage 3。

## Standing workflow decision — preserve quality before asking human

用户已明确：本 Presentation program 始终按最高冻结质量标准推进，不允许为了少一轮 review、少搜资源或更快进入下一 Stage 而偷工减料。

后续若 review limit 到达，而唯一实质选择是“创建一个范围清楚、质量保持的 bounded recovery”或“放宽已有质量合同”，Planner 应自动选择前者；这类显然的质量保持 continuation 不再要求用户重复授权。

保持每个 bounded task 的少量 review 上限，用新的 recovery task 隔离新增 scope；不要简单提高单 task review 次数形成无限返修。只有真正涉及产品/科学语义冲突、明显新的成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终两套 deck 验收时才进入需要用户决定的 human gate。

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
