---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 041_research_presentation_frozen_four_paper_generalization_batch
review_round: 1
decision: REVISE
implementation_commit: a01865e5380f3c23a3d0eea6bbc6e4f3fdf8591d
---

# GPT Review

## Decision

REVISE.

本轮独立审核确认 041 已经是一个真实的 frozen-batch failure，而不是 Executor 自报或 CI 假失败。四篇在首次 render 前整体冻结，production behavior 没有在 batch 中修改；真实 GitHub CI 已通过。随后 task-local Terra 也已与 041 manifest、`implementation_commit=a01865e...`、source-bundle freeze 与实际 render identities 绑定并完成。

当前不能 PASS，且 041 最终也不能通过“修两页再把 2/4 包装成成功”。TMB 与 RETFound 都在正常 production entry 的 gold composition selector 阶段于 render 前失败，因此 strict 4/4 batch 已经失败。与此同时，DESeq2 与 cardiac-ultrasound 虽然成功生成 exact-CUHK deck，但 fresh Terra 对两套 contact sheet 和除 DESeq2 模型页外的大多数实质页面均给出 `REVISE`：主要问题是论文 figure/page evidence 过小、底部文字/引用碰撞或裁切，未达到成熟博士组会投影质量。

本轮仍保留一次最小、合同内的 Executor action：只允许对已经渲染的 DESeq2 与 cardiac-ultrasound 使用 041 冻结前就已 shipped 的单次 bounded automatic repair。两套 deck 的 `quality_loop_state.json` 当前均仍是 `repair_cycle_count=0 / WAITING_FOR_DECK_VISUAL_REVIEW`，所以 fresh Terra 还没有被实际消费。完成这一条 production behavior 后，041 的真实证据链才完整。TMB/RETFound 不得在 041 内修 selector、换 gold、改 source bundle 或重跑成“成功”。

## Blocking findings

### 1. Strict 4/4 batch 已因两个 pre-render selector failures 失败

**Plan / regression basis**

Frozen Plan 明确要求四篇全部通过 normal production entry + render + item/page-level Terra + Planner，任何一篇失败即整个 batch FAIL；batch 内禁止修改 production code、gold、layout、prompt、validator、quality-loop mapping，禁止替换论文，也禁止 post-output source rewrite。

**Observed evidence**

- TMB 正常 production invocation 在 `build_gold_composition_recipe.build_recipe()` 处抛出 `ValueError: no compatible gold composition record`，没有 PDF、rendered page 或 contact sheet。
- RETFound 出现相同的正常 selector failure，也没有 rendered pixels。
- task-local Terra 明确保留该事实为 batch-level blocking finding：只有两套 deck 有可审查像素，因此 package 不能成为 4/4 acceptance。

**Minimal repair in this task**

无。041 内不得修 selector/gold/layout 或改这两个 source bundle；这些失败必须原样保留为 frozen-batch generalization evidence。Executor 只需确保后续 RESULT / CURRENT 不把两篇失败重新解释为可在本 batch 内恢复。

**Required closure evidence**

041 最终关闭时必须明确记录：TMB、DESeq2、cardiac-ultrasound、RETFound 四篇全部已 consumed；041 batch FAIL；不存在 replacement、holdout-specific repair 或跨 paper production drift。

### 2. 两套已渲染 deck 尚未执行冻结合同允许的唯一一次 shipped runtime repair

**Plan / regression basis**

041 允许每个 deck 最多一次、且只能使用 batch freeze 前已经 shipped 的 bounded automatic repair；repair mechanism 本身不得修改。缺 visual evidence 时等待，不消耗 review round；拿到 fresh task-local evidence 后，真实 production behavior 应完成该有限质量循环。

**Observed evidence**

- fresh Terra 已存在并与最终 manifest / implementation / pixel identities 绑定。
- DESeq2 `quality_loop_state.json`：`repair_cycle_count=0`、`deck_level_decision=WAITING_FOR_DECK_VISUAL_REVIEW`、`selected_repair_directives=[]`。
- cardiac-ultrasound 同样尚未消费本次 Terra。
- Terra 对 DESeq2 的 real-data / experiment / negative-result / next-experiment / comparison 页面和 contact sheet 均给出 `REVISE`；主要为 source figure 太小以及 footer/citation/text collision。
- Terra 对 cardiac-ultrasound 六个实质页面和 contact sheet 均给出 `REVISE`；主要为真实超声/流程/测量证据过小，以及部分底部文字碰撞或裁切。

**Minimal repair**

Executor 只对 DESeq2 与 cardiac-ultrasound 执行已有 quality-loop consumer：

- 消费当前 `VISUAL_REVIEW.json` 中与各 deck 对应的结构化 findings；
- 每套最多一次 repair，`repair_cycle_count <= 1`；
- 不修改 production code、gold library、layout implementation、prompt/routing、validator、repair mapping、canonical CUHK template 或任何 frozen source bundle；
- 不手工 patch `.tex`、PNG、PDF、caption、figure crop source 或 audience copy；
- 若现有 mapping 对某 finding 无安全、无歧义映射，必须 fail closed，并把它记录为真实 failure；
- repair 若被执行，必须产生新的 render-input identity 与 rendered-pixel identity；无真实像素变化不得声称已修复；
- 不对 TMB 或 RETFound 做任何 selector recovery，也不尝试补出缺失 deck。

**Required closure evidence**

- 两个已渲染 deck 的更新 `quality_loop_state.json`，明确记录是否选择 repair、repair cycle 数、前后 identities 和 fail-closed 原因（如有）；
- 若任一 deck 像素发生变化，更新 041 task-local visual manifest 并取得与新 pixels/manifest 绑定的 fresh Terra item-level + contact-sheet evidence；
- 若没有安全 repair 或 repair 后仍失败，直接保留失败，不允许 second repair；
- 更新 RESULT，给出最终四篇逐项 outcome 与 batch-level FAIL，不把局部视觉改善冒充 041 PASS。

## Non-blocking notes

- 这次 real-paper batch 已暴露至少两个值得在 041 终止后做 generic recovery 的独立机制缺口：gold selector 对真实 scientific-object/page-job 的覆盖不足，以及 paper figure/page 在通用布局中反复缩得过小、footer/citation 容量控制不足。这些只能在独立 non-holdout / public-safe regression 上恢复，不能把本批四篇正文、图像、标题、DOI 或 page-specific output 变成 tuning fixture。
- DESeq2 的模型页已经被 Terra 判为清晰、来源特异且投影可读；cardiac-ultrasound 也确实使用真实论文超声像素。后续 generic recovery 应保护这些已经成立的能力，而不是整体重写 production system。
- 根据 Program Goal，041 失败后的 generic recovery 可以自动开展；但 generic recovery PASS 后，在冻结下一批 fresh four-paper holdout 之前必须进入用户 human gate。
