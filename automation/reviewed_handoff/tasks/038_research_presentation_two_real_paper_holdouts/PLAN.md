---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 038_research_presentation_two_real_paper_holdouts
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

完成 Stage 5 的双真实论文 one-shot 验收，并且把“泛化到真实科研材料”与此前 Stage 1–4 的 engineering/synthetic regression 明确分开。038 的价值不是再优化系统，而是验证已经冻结的正常 `research-presentations` production path 是否能在两个未见过的真实领域输入上，直接产生完整、source-faithful、exact-CUHK、成熟组会级 deck。

本任务固定使用：

1. statistics/methodology：Bürkner (2017), **brms: An R Package for Bayesian Multilevel Models Using Stan**, DOI `10.18637/jss.v080.i01`；
2. medical imaging：Ma et al. (2024), **Segment anything in medical images**, DOI `10.1038/s41467-024-44824-z`。

两篇均为公开可获取文章；JSS 文章采用 CC BY，MedSAM 文章采用 CC BY 4.0。Planner 在冻结任务前对仓库 tracked content 做 title/DOI/author/product-name 搜索未发现命中；Executor 仍必须在首次 acquisition 前对 presentation reference/gold/corpus manifest 做一次机械 exclusion audit。只有“预生成前证明曾参与调优/无法合法取得所需 source”才允许把 paper eligibility 交回 Planner；不能因为输出难做而换题。

## Frozen decisions

- Stage 4 已整体 PASS；038 不重开 Stage 4，也不允许以真实 holdout 为新训练样例继续修改 production system。
- 038 是 evaluation-only：正常 production code、gold library、layout emitters、storyline grouping、validator、quality-loop mapping、tests 和 shared/plugin behavior 全部冻结。
- 两篇 holdout identity 已冻结。首次生成前必须证明其没有出现在 reference/gold/corpus/tuning metadata；通过后立即记录 `holdout_eligibility.json`，后续不重新选择更容易的 paper。
- 每篇 paper 的 source preparation 发生在第一次 production render **之前**。Executor 可以读取完整论文、补充材料和公开 source data，构建正常 entrypoint 所需 file/path-oriented bundle；但 bundle 一旦完成必须先写 SHA256 与 source-fidelity inventory，然后才允许调用 generator。看到 slide/render/Terra 后不得改 bundle 再重跑并继续称为 one-shot。
- 正常调用必须使用 `generate_research_presentation_production_entry.py --input-bundle ... --out-dir ...`。不得调用 benchmark helper、fixture generator、Stage 3/4 task-local generator 或手工复制 engineering fixture。
- 一次用户调用中已经冻结的 bounded quality loop 可以工作：每个 deck 最多一次由结构化 visual-review finding 触发的既有 source-faithful repair。除此之外不允许手工修 slide、直接 patch `.tex`、paper-specific branch、第二次 repair 或新规则。
- 统计 deck 与医学 deck 必须分别生成、分别有 source-fidelity map、render-input identity、rendered-pixel identity、PDF、逐页 PNG、contact sheet、sequence/quality-loop evidence；不能把两个 paper 合成一套 deck 来降低标准。
- 两套 deck 都必须是完整 paper talk / journal-club 级组会 presentation。完整性的判断是 source coverage，而不是固定页数：至少应让听众看懂研究动机/问题、核心方法或机制、主要证据、关键限制/失败边界与最终解释；不能只生成少数 benchmark archetype pages。
- brms deck 必须让真实 Bayesian multilevel modeling 内容主导：paper 自身的 formula/model families、prior/Stan/MCMC or inference objects、实例/比较和 paper 中真实图表/结果按来源需要进入 deck。不得复用 clustered-calibration fixture 的科学内容。
- MedSAM deck 必须让真实 medical-image evidence 主导，至少包含一页直接使用文章 CC BY 4.0 覆盖的真实定性医学图像/segmentation figure，并保持 modality、prompt、expert annotation / prediction 等语义与原文一致。不得生成或“修复”不存在的医疗像素。
- article/source attribution 必须随 evidence trace 保留；面向听众的 figure/source note 使用正常学术引用，不把 repository path、QA、run id 或 internal provenance 暴露到 slide body。
- 若任一 holdout在第一次真实生成/允许的一次内建 repair 后仍出现 product blocker，该 one-shot 结果必须保留并永久失去“未见 holdout”资格。后续 generic 修复只能使用非 holdout regression，然后为该 domain 选择新的 unseen paper；禁止在同一论文上调完再宣布最终通过。
- 如果两篇都通过 Terra 与 Planner，038 最终必须进入用户人工验收；不得由 Executor、Terra 或 Planner 自动设置最终 `ONE_SHOT_QUALITY_PASS`。

## Implementation scope

1. **Eligibility + license/source audit**
   - 检查 `reference_sources_manifest.json`、reference index/search matrix、gold metadata/lessons、tracked task fixtures/results 与其他 tuning metadata 是否出现两篇 paper 的 title、DOI、author/product identifiers。
   - 为每篇生成 task-local eligibility record，记录 search scopes/results、published URL、DOI、license、source version 和 acquisition date。
   - 若预生成审计发现任何真实 prior tuning use，停止该 paper acquisition/generation并 `NEEDS_GPT_PLANNER`；不要私自替换。

2. **Source acquisition and freeze-before-render staging**
   - 获取完整 published PDF/HTML 与必要 supplement/source-data；读取完整 paper，而不是只抓 abstract。
   - 记录 PDF/source SHA256、页数、section inventory、figure/table inventory、可复用 figure/image 的 license/credit line。
   - 从论文构建正常 production bundle。每个 substantive claim、equation/model object、figure/table/image、result、limitation 都必须带真实 source anchor。
   - 写出 `source_bundle.json` 与 `source_bundle.sha256`；写 bundle 后再运行一次 freeze check，确认后续 pipeline 不会自动修改 bundle。

3. **Two independent normal production invocations**
   - statistics output: `results/038_research_presentation_two_real_paper_holdouts/statistics/`；
   - medical output: `results/038_research_presentation_two_real_paper_holdouts/medical/`；
   - 分别调用 normal production entrypoint；保存实际命令、exit code、source-fidelity map、deck plan、gold selections、canonical CUHK `.tex + PDF`、rendered pages、identities、contact sheet、sequence summary 与 quality-loop state。
   - 不允许调用 task-specific benchmark/generator；不允许手改生成后的 `.tex`/PNG/PDF。

4. **Built-in bounded quality loop only**
   - 如果 normal shipped quality-loop 需要 reviewer evidence，使用 task-local Visual Review contract 提交第一轮真实像素；只允许现有 mapping 支持的最多一次自动 source-faithful repair。
   - 任何 unknown/unsafe finding、repair budget exhausted、paper-specific manual intervention need 都 fail closed / no-winner，并保留 holdout failure evidence。

5. **Combined task-local final visual evidence**
   - 最终候选像素确定后，生成一个 038 task-local `visual_review/visual_inputs.json`，同时包含 statistics deck 的所有 substantive pages + statistics contact sheet，以及 medical deck 的所有 substantive pages + medical contact sheet。
   - manifest 必须绑定两套各自的 source-bundle SHA、implementation/base identity、render-input identity、rendered-pixel identity、PDF/contact-sheet/page SHA 和 source-fidelity map。
   - Terra rubric 必须明确这是两个独立 real-paper holdout，逐项判断 source specificity、exact CUHK、scientific object prominence、math/plot/image semantic fidelity、projection readability、无内部元语言，并分别对两个 contact sheet 给出成熟组会 deck judgement。

6. **Result handoff**
   - `RESULT.md` 必须把两篇 paper 分开汇报：eligibility/source evidence、frozen source bundle hash、normal invocation evidence、quality-loop behavior、render identities、page/contact-sheet paths、任何 failure。
   - 不得把 CI green、PDF compile、top-level Terra package PASS 当 final quality PASS。

## Acceptance and regression gates

038 只有在以下全部成立时才可以被 Planner 判定 task PASS：

- 两篇 paper 在首次生成前均通过 tracked-corpus/tuning exclusion audit，且 source/DOI/license 可验证；
- 两篇完整 paper（及方法/图像语义需要的相关 supplement/source data）已实际读取，source bundle 在首次 render 前冻结并有 SHA；
- 两个 deck 均由正常 production entrypoint 独立生成，没有 benchmark/fixture/task-specific bypass，没有输出后 source-bundle rewrite、手工 TeX patch 或 paper-specific production code change；
- 任何自动 repair 都来自既有 Stage 4 bounded quality loop，且每 deck 不超过一次；
- 两个 deck 都是完整 paper talk，真实 source notation/data/figures/images/claims 主导，关键 claim/method/result/limitation 可回溯；
- statistics deck 无 Stage 4 fixture 科学文案或 placeholder model，paper 的 Bayesian/multilevel/Stan 内容保持正确；
- medical deck 使用真实 MedSAM article medical-image/segmentation evidence，qualitative image semantics 与原文一致，无 fabricated medical pixels；
- exact CUHK source identity、gold retrieval、render-input/pixel identity、source-fidelity map 和 deck quality-loop trace 均完整；
- 真实 GitHub CI 对 038 published handoff 通过；
- fresh 038 task-local Terra 与最终两个候选像素 identity 匹配，每个 substantive page 都有 item-level decision/observations；两个 contact sheet 均有独立 item-level `PASS` 和 mature doctoral-group-meeting / strong paper-talk judgement；
- Terra 无 blocking findings，Planner 独立读取两篇真实 source、bundle/trace、实际 `.tex`/render 与 item-level evidence 后也认为两套 deck 满足 Program Goal Final Quality Gates；
- 没有以“synthetic CI/mechanical pass”替代真实 paper visual/source judgement。

如果任一真实 deck 失败上述质量门：

- 不降低质量标准；
- 不在同一 holdout 上修改 production 再宣称 unseen；
- 保留这次 holdout 的 terminal evidence；
- 由 Planner 按 Quality-Preserving Continuation Policy 创建非 holdout generic recovery，修复完成后再选该 domain 的新 unseen replacement paper。

如果两套 deck 均通过：

- 038 task 可以 PASS；
- Stage 5 **仍不得**自动闭合 Program；
- 必须把两个真实 rendered deck/artifact 交给用户，并将 program route 设为最终 `AWAIT_HUMAN_DECISION`；
- 只有用户明确接受两套结果后，才允许 `ONE_SHOT_QUALITY_PASS` 与 `PROGRAM_MATURE=true`。

## Natural-language usage / routing expectations

本任务模拟的最终用户请求就是普通科研场景，例如：“把这篇统计方法论文做成组会汇报”或“把这篇医学影像论文整理成 CUHK 组会 slides”。用户不应需要知道 gold ID、layout emitter、quality-loop state 或 benchmark helper；正常 production route 应从已经整理好的真实 paper source bundle直接生成可讲的完整 deck。

通过标准也不是“文件存在”，而是：统计论文讲得像统计论文，医学影像论文讲得像医学影像论文；关键公式、数据、结果和图像来自原文；页面可投影阅读；整套有真实叙事节奏；系统内部控制语言不泄漏。

## Out of scope

- 不新增第三个 holdout，也不为了更好看而挑选更多 paper 后只展示赢家。
- 不扩充 reference corpus/gold library，不从这两篇 holdout 提炼新 gold/rules。
- 不修改 production generator、layout、selector、validator、quality-loop mapping、CI 或 shared/plugin architecture。
- 不做 PPTX/editable route 验收；当前 Program Goal 的 final route 是 exact CUHK Beamer `.tex + PDF`。
- 不重做 Stage 1–4 regression 已证明的机制，除非真实 holdout暴露 blocker；即使暴露，也必须在新的非-holdout recovery task 中修，而不是 038 内调参。
- 不替用户执行最终审美/科研接受决定。Terra + Planner 均 PASS 后仍必须停在最终人工门。
