---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 041_research_presentation_frozen_four_paper_generalization_batch
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

完成 Stage 5 的完整 frozen-batch 真实论文泛化验收。041 不再采用“失败一篇、修复、再换一篇”的 replacement protocol，而是在任何一篇进入 source bundle、render 或 evaluation 之前，一次性冻结四篇真实公开 unseen paper，并让已经在 Stage 4/039 冻结成熟的正常 `research-presentations` production system 在整个 batch 内保持不变。

本 task 的目的不是继续调系统，而是回答一个更严格的问题：当前 shipped production path 是否能够在**同一冻结系统、同一冻结 quality-loop contract、没有 adaptive holdout chasing** 的条件下，对两个统计/生物统计/方法学论文和两个医学影像论文都直接生成完整、source-faithful、exact-CUHK、成熟博士组会级的 paper-talk deck。

本次完整 batch 冻结为以下四篇：

1. **Statistics / computational methodology — TMB**  
   Kristensen, K., Nielsen, A., Berg, C. W., Skaug, H., & Bell, B. M. (2016). **TMB: Automatic Differentiation and Laplace Approximation**. *Journal of Statistical Software*, 70(5). DOI `10.18637/jss.v070.i05`.
2. **Biostatistics / methodology — DESeq2**  
   Love, M. I., Huber, W., & Anders, S. (2014). **Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2**. *Genome Biology*, 15, 550. DOI `10.1186/s13059-014-0550-8`.
3. **Medical imaging — cardiac ultrasound segmentation**  
   Ferreira, D. L., Lau, C., Salaymang, Z., & Arnaout, R. (2025). **Self-supervised learning for label-free segmentation in cardiac ultrasound**. *Nature Communications*, 16, 4070. DOI `10.1038/s41467-025-59451-5`.
4. **Medical imaging — retinal foundation model**  
   Zhou, Y. et al. (2023). **A foundation model for generalizable disease detection from retinal images**. *Nature*, 622, 156–163. DOI `10.1038/s41586-023-06555-x`.

Planner freeze 前的 tracked-repository contamination audit 结论：

- TMB exact title 与 DOI 的 repo-wide search 只命中 superseded 040 的 Planner `REQUEST.md` / `PLAN.md`；040 `implementation_commit=null`，且其 `FINAL_REPORT.md` 明确记录未 acquisition、未 source-bundle freeze、未 render、未 Terra、未 production invocation，因此 040 没有消费 TMB。
- cardiac-ultrasound exact title 与 DOI 同样只命中 040 的 Planner `REQUEST.md` / `PLAN.md`；040 未执行，因此未消费该论文。
- DESeq2 exact title、DOI 及 `DESeq2` repo-wide search 均无命中。
- RETFound exact title、DOI 及 `RETFound` repo-wide search 均无命中。
- 038 的 brms 与 MedSAM 已消费且永久排除，本 batch 不复用。

公开来源/许可预检：JSS 对文章采用 Creative Commons Attribution；DESeq2 为 CC BY 4.0；Ferreira cardiac-ultrasound 为 CC BY 4.0；RETFound 为 CC BY 4.0。医学影像 paper 的 article figures / third-party material 仍必须在实际 acquisition 时逐图核对 credit line；若某具体图明确不在文章 CC 许可覆盖内，不得使用该图像素。

## Frozen decisions

- **完整四篇 batch identity 已冻结。** 任何一篇都不能因为“难做、输出不好看、Terra 失败、某页不好修”而在 batch 内替换。不得先跑一篇再挑下一篇，也不得保留赢家、替换输家。
- **production system 全 batch 冻结。** 以 Planner freeze 时 `main` 的 production behavior 为基线，production-freeze locator 为 commit `d3379b5168bc27b114b362f186f8c239a88a669c`。041 后续允许新增 task-local source/evidence/render/control artifacts，但不得修改 normal production generator、shared/plugin rules、gold library、layout emitters、storyline logic、prompt/routing、validator、quality-loop mapping、tests 或 canonical CUHK template 来适配任何 holdout。
- 在任何 holdout acquisition 前，Executor 必须先对**四篇一起**完成一次机械 contamination/exclusion preflight：tracked repo、presentation reference/gold/corpus/tuning metadata、已有 task fixtures/results，以及本机实际参与 production/reference retrieval 的可见索引。若发现任一候选在 041 freeze 前已真实用于 source/gold/tuning/render（040 的 planner-only mention 除外），必须在**尚未 acquisition 任何四篇正文/补充材料**时返回 `NEEDS_GPT_PLANNER`；不得先消费其他三篇再替换。
- 四篇 contamination preflight 全部通过后，才允许 acquisition。之后 batch identity 不再改动。
- **四个 source bundle 必须在任何一个 deck 首次 production render 前全部完成并冻结。** Executor 可读取每篇完整论文、必要 supplement/extended data/source data 和 rights metadata，构建正常 production entry 所需 bundle；但必须先完成四个 bundle 的 SHA256、source inventory、figure/table/image inventory、license/credit record 和 source-fidelity anchor freeze，之后才允许第一次 generator invocation。
- 一旦四个 bundle freeze 完成，看到任何 slide/render/Terra 后都不得修改 bundle、source selection、claims、figure crop source、page-job hint 或 metadata 再继续称为 unseen one-shot。若 source bundle 本身存在真实错误，只能记为该 batch failure evidence；不能追着输出改 source preparation。
- 四套 deck 必须分别由 normal `research-presentations` production entrypoint 生成。不得调用 benchmark helper、Stage 3/4 task-specific generator、fixture generator 或手工复制 synthetic bundle。
- 每个 deck 只允许使用在 batch freeze 前已经 shipped 的 **最多一次** bounded automatic repair。repair mechanism 本身在四篇之间完全冻结；不得为了前一篇 Terra finding 改 mapping/consumer，然后用于后一篇。
- 自动 repair 只能消费现有结构化 visual-review finding，并受 039 已验证的 fail-closed / source-faithful 约束；unknown/unsafe finding、需要人工重写科学内容、需要第二次 repair 或需要 holdout-specific layout branch 时直接视为该 deck 未通过。
- 不允许手工 patch 生成后的 `.tex`、PNG、PDF、figure、annotation 或 source bundle；不允许按 paper title/DOI/author/dataset 写特殊分支。
- 四套 deck 都必须是完整 paper talk / journal-club / doctoral group-meeting presentation，而不是少数 benchmark pages。完整性按论文自身 scientific arc 判断，不固定页数，但至少覆盖研究问题、核心方法/机制、主要证据、关键限制/失败边界与结论/解释。
- TMB deck 必须由论文自己的 Laplace approximation、automatic differentiation、random effects / latent variables、R/C++ workflow 与 paper 自身性能比较主导；不得套回 Stage 4 clustered-calibration 或 brms 语义。
- DESeq2 deck 必须由论文自己的 negative-binomial GLM、dispersion/fold-change shrinkage、empirical-Bayes / regularization logic、真实 RNA-seq evaluation/figures 与 limitation 主导；不得泛化成 generic bioinformatics workflow。
- cardiac-ultrasound deck 必须真实使用论文许可覆盖的 echocardiography / chamber segmentation evidence，保持 A2C/A4C/SAX、chamber anatomy、weak-label/self-learning pipeline、临床测量与 MRI/clinical comparison 的原文语义；不得生成替代医疗像素。
- RETFound deck 必须真实使用论文许可覆盖的 CFP/OCT retinal image evidence，并保持 pretraining/fine-tuning、ocular diagnosis/prognosis/systemic-disease prediction、saliency/interpretability 等原文语义；不得生成替代 retinal pixels，也不得把 fundus/OCT 图混写成 generic segmentation。
- 所有 audience-facing source attribution 使用正常学术引用。repo path、QA、run id、holdout、tuning、provenance/debug/workflow 等内部语言不得泄漏到 slide body。
- 任一 paper 在正常 production + 允许的一次 shipped repair 后未满足 final bar，则**整个 4-paper batch FAIL**；四篇从此全部计为 consumed holdouts。不得用 3/4、2/4 或跨 batch 拼接成功案例宣称 generalization PASS。
- failed batch 后可以另建 non-holdout generic recovery，但不能使用这四篇的正文、图像、标题、DOI、page-specific content 或 rendered pixels 作为 tuning fixture。generic recovery 完成后，下一 fresh batch 前必须进入 user human gate；041 不自动创建下一批。
- 只有四套全部 Terra + Planner PASS 时，041 才进入最终 `AWAIT_HUMAN_DECISION`，把四套真实 rendered deck 交给用户人工验收。只有用户明确接受，才允许 `ONE_SHOT_QUALITY_PASS` / `PROGRAM_MATURE=true`。

## Implementation scope

1. **Four-paper eligibility / contamination preflight before acquisition**
   - 对四篇一次性检查 exact title、DOI、主要 author / product identifier / common shorthand。
   - 检查 presentation reference source manifest/index/search matrix、gold composition metadata/lessons、tracked fixtures/results、quality-loop stress inputs 与其他 tuning metadata。
   - TMB 与 cardiac-ultrasound 在 040 planner-only artifacts 中的命中必须显式记录为 non-consuming historical mention，并交叉核对 040 `implementation_commit=null` 与无生成/视觉 evidence 的 terminal report。
   - 写 task-local `batch_eligibility.json`，列出四篇 identity、search scopes、命中/排除理由、公开 source locator、license 与 pre-acquisition decision。
   - 只有四篇全部 eligibility PASS 才进入 acquisition；任一不通过则在未读取任何四篇正文/补充材料前返回 Planner。

2. **Production freeze verification**
   - 记录 `d3379b5168bc27b114b362f186f8c239a88a669c` 为 041 的 production-freeze locator。
   - acquisition 前验证自该 locator 以来没有 presentation production/gold/layout/prompt/validator/quality-loop/template 行为变化；041 自身 PLAN/CURRENT/results/source artifacts 等 control/evidence 文件不算 production drift。
   - 在四篇执行期间再次检查该 freeze；若 production drift 出现，停止 batch，不把不同系统版本混进同一 acceptance batch。

3. **Acquire all four sources, then freeze all four bundles before any render**
   - 获取每篇完整 published article（PDF/HTML），以及解释核心方法、实验、限制或真实医学图像所必需的 supplement / extended data / source-data metadata。
   - 实际读取完整 paper；不能只用 abstract、publisher summary 或 metadata。
   - 为每篇记录 article/source SHA256、页数/section inventory、figure/table inventory、可复用图像的 license/credit line 与 source anchors。
   - 医学影像逐图检查第三方 credit；只使用 CC 许可或明确可复用的 article-owned image pixels。
   - 构建四个正常 production input bundle；每个 substantive claim、equation/model object、figure/table/image、result、limitation 都要有真实 source anchor。
   - 在第一次 render 前写出四份 `source_bundle.json` + SHA256，并生成 batch-level freeze manifest，绑定四个 bundle hash；freeze 后禁止修改。

4. **Four normal production invocations under one frozen system**
   - 建议 task-local 输出结构：
     - `results/041_research_presentation_frozen_four_paper_generalization_batch/statistics_tmb/`
     - `.../biostatistics_deseq2/`
     - `.../medical_cardiac_ultrasound/`
     - `.../medical_retfound/`
   - 四篇分别调用 normal production entrypoint，并保存实际 command、exit code、source-fidelity map、deck plan、gold selections、canonical CUHK `.tex + PDF`、rendered pages、render identities、contact sheet、sequence summary 与 quality-loop state。
   - 允许执行顺序不同，但 production behavior 与四个 frozen bundles 在第一篇 render 之后都不可改变。

5. **Existing bounded quality loop only**
   - 若某 deck 的 shipped quality loop 需要 visual-review evidence，继续使用 Bridge Kit task-local Visual Review contract，不新造状态机。
   - 缺 visual evidence 时进入等待/发布/拉取 evidence 的既有路径，不消耗 GPT review round。
   - 每个 deck `repair_cycle_count <= 1`。repair 前后必须有真实 render-input / rendered-pixel identity；若没有真实像素变化，不得声称 repair 生效。
   - repair 后仍有 blocking finding、需要 second repair、需要手工 TeX/source edit 或 finding 无安全映射时，该 deck FAIL，进而整个 batch FAIL。

6. **Combined final task-local Terra evidence**
   - 最终候选像素确定后，使用 041 已声明的 task-local `visual_review/visual_inputs.json` 作为统一 final manifest；它必须包含四套 deck 的所有 substantive pages 和各自 contact sheet。
   - manifest 必须按 deck 绑定：paper identity/DOI、frozen source-bundle SHA、production-freeze locator、render-input identity、rendered-pixel identity、PDF/contact-sheet/page SHA、source-fidelity map、quality-loop state。
   - Terra rubric 必须按四个独立 real-paper holdout 逐项检查 source specificity、exact CUHK、scientific object prominence、math/plot/image semantic fidelity、projection readability、audience-facing language，以及 medical image modality/anatomy semantics。
   - 四个 contact sheet 必须分别给 mature doctoral-group-meeting / strong paper-talk judgement；top-level package `PASS` 不能替代 item/page-level decisions。

7. **CI / result / Reviewer handoff**
   - 真实 GitHub CI 必须对 published 041 handoff 通过；本地 test/mechanical pass 不替代 GitHub evidence。
   - `RESULT.md` 必须先给 batch-level verdict，再分别记录四篇的 eligibility、source freeze hash、normal invocation、quality-loop behavior、render identities、page/contact-sheet paths 与 failures。
   - Reviewer 必须独立读取四篇真实 source、四个 frozen bundle/source-fidelity maps、normal invocation traces、实际 TeX/render、final item-level Terra 与四个 contact sheet；不得只相信 Executor 自报或 top-level Terra。

## Acceptance and regression gates

041 只有在以下**全部**成立时才允许 Planner 判定 task PASS：

- 四篇 identity 与类别与本 PLAN 完全一致；没有 batch 内 replacement/chasing。
- acquisition 前完成四篇联合 contamination audit；TMB / cardiac-ultrasound 仅有 040 planner-only historical mentions，DESeq2 / RETFound 无 prior tuning/source/gold use；不存在真实 prior consumption。
- production system 与 `d3379b5168bc27b114b362f186f8c239a88a669c` 冻结基线相比没有影响 presentation behavior 的 drift。
- 四篇完整论文及必要 supplement/extended data 已实际读取；四个 source bundle 在**任何一个** production render 前全部冻结且有 SHA/batch freeze manifest。
- 四个 deck 均由 normal production entrypoint 独立生成，无 benchmark/fixture/task-specific bypass、无输出后 source rewrite、无手工 TeX/image patch、无 paper-specific code/hardcode。
- 任一 automatic repair 都是 batch freeze 前已经 shipped 的 bounded quality loop，且每个 deck最多一次；repair mechanism 四篇之间不变。
- 四个 deck 均是完整 paper talk，真实 paper notation/data/figures/images/claims 主导，关键 claim/method/result/limitation 可追溯。
- TMB 的 Laplace/AD/random-effects/R-C++/performance comparison 语义正确；DESeq2 的 NB-GLM/shrinkage/dispersion/LFC/empirical evidence 语义正确。
- cardiac-ultrasound 使用真实 rights-safe echocardiography / segmentation pixels且 anatomy/view/clinical-comparison 语义正确；RETFound 使用真实 rights-safe CFP/OCT pixels且 modality/disease/interpretability 语义正确；无 fabricated medical pixels。
- exact CUHK source identity、runtime gold retrieval/consumption trace、source-fidelity maps、render-input/pixel identity、deck sequence 与 quality-loop trace 对四篇都完整。
- 真实 GitHub CI PASS。
- fresh 041 final Terra evidence 与最终四套 candidate pixels identity 匹配；每个 substantive page 都有 item-level decision/observation；四个 contact sheet 都有独立 item-level `PASS` 且达到 mature doctoral-group-meeting / strong paper-talk bar；无 blocking finding。
- Planner 独立审核四篇 source/trace/render/Terra 后四套全部 PASS；不能把 synthetic/fixture/CI/mechanical PASS 当作 real-paper acceptance。
- 没有 holdout-specific hardcode，也没有在第一篇输出后改变后续三篇会使用的 production behavior。

Batch decision 是严格 **4/4**：

- 任一 deck 未通过上述任一门槛，整个 041 batch = FAIL；四篇全部标记 consumed holdouts。
- 失败后不降低 bar，不在同一 task 内替换 paper，不在同一 holdout 上调 production 后重新宣称 unseen PASS。
- 可后续创建独立 non-holdout generic recovery；但 generic recovery PASS 后，在任何下一 fresh batch 前必须进入用户 human gate，说明本 batch 为什么失败、修复了什么通用机制、为什么值得再消耗一批 unseen paper。

如果四套全部通过：

- 041 task 可由 Planner PASS；
- Stage 5 仍不得自动写 `ONE_SHOT_QUALITY_PASS` / `PROGRAM_MATURE=true`；
- 必须把四套真实 rendered deck/artifact 路由到最终 `AWAIT_HUMAN_DECISION`；
- 只有用户明确接受完整四套结果后，才允许关闭 Program 和 Planner automation。

## Natural-language usage / routing expectations

本 task 模拟四个普通科研用户请求，而不是 benchmark 调用。例如：“把这篇 TMB 论文做成统计方法组会汇报”“把这篇 DESeq2 论文整理成 biostat paper talk”“把这篇心脏超声分割论文做成组会 slides”“把这篇 RETFound retinal foundation-model 论文整理成 CUHK paper talk”。

用户不应需要知道 gold ID、layout emitter、quality-loop state、holdout manifest 或 benchmark helper。正常 production route 应从真实 paper source bundle 自动生成完整可讲的 deck。最终标准是：四篇各自都像认真读过原论文的博士生汇报，而不是同一套 AI 模板换标题；数学论文保留真实记号和机制，生物统计保留真实模型和数据证据，医学影像保留真实 modality/anatomy/image semantics，整套页面在投影下可读且叙事成熟。

## Out of scope

- 不在 041 内新增第五篇候选、候补 paper 或 replacement list。
- 不根据前一个 holdout 结果改变后一个 holdout 的输入、source bundle、production code、gold、layout、prompt、validator、quality-loop mapping 或验收 rubric。
- 不扩充 reference/gold corpus，不从四篇 holdout 提炼新的 gold composition、prompt rule、repair mapping 或 fixture。
- 不修改 normal production generator、shared/plugin architecture、canonical CUHK template 或 PPTX route。
- 不把 038 的 brms/MedSAM 失败论文重新作为 unseen，也不使用其 page-specific failure content做 tuning。
- 不把 TMB/Ferreira 在 superseded 040 的 Planner-only mention误判为真实 consumption；但若 acquisition 前出现新的真实 prior-use evidence，必须停止并交回 Planner，不能忽略。
- 不允许 second repair、手工 slide beautification、手工 `.tex` patch、生成式医疗图像替代、许可不明图像复用或降低投影/审美/内容门槛。
- 不由 Executor/Terra/Planner替用户做最终长期成熟决定；4/4 Terra + Planner PASS 后仍必须停在最终人工 artifact 验收门。
