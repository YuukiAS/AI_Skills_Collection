---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 041_research_presentation_frozen_four_paper_generalization_batch
review_round: 2
decision: REVISE
implementation_commit: 9bd69e5b54e7968ec731e00a3c9794c6fad21672
---

# GPT Review

## Decision

REVISE，并在本 task 到达两轮审核上限后保留为真实失败历史。

第二轮独立审核确认，041 的最终事实已经稳定，不存在可以在本 frozen holdout batch 内继续合法追修的空间。四篇论文在首次 render 前完成整体冻结，batch 内 production system 没有漂移；真实 GitHub CI 已通过。TMB 与 RETFound 仍然在正常 `research-presentations` production entry 的成熟构图检索阶段于 render 前失败，因此严格 4/4 验收已经失败。DESeq2 与 cardiac-ultrasound 则真实执行了 Review 1 唯一允许的 shipped quality-loop consumer，但现有消费者无法把本次真实视觉 finding 安全、唯一地映射为已有 repair directive：两套均保持 `repair_cycle_count=0`、没有 selected directive、render-input 与 rendered-pixel identities 不变，并以 fail-closed 结束。

最新 task-local Terra 与 `implementation_commit=9bd69e5...`、当前 manifest、冻结 source-bundle identities 和未变化的最终 pixels 绑定，仍明确保留 batch blocker；同时 DESeq2 与 cardiac-ultrasound 的最终像素仍存在底部正文/引用碰撞，两个 contact sheet 均未通过。由此不能把“consumer 被调用过”解释成 repair 成功，更不能进行第二次 repair、修改 holdout source、扩 gold 或改 selector 来挽救 041。

041 因此在 Round 2 结束。四篇全部计为 consumed holdouts，不得在后续修漂亮后重新宣称 unseen PASS。后续若继续，只能按 Program Goal 在独立 non-holdout / synthetic / public-safe regression 上做 generic recovery；generic recovery PASS 后，在消耗下一组 fresh four-paper batch 前必须进入用户人工门。

## Blocking findings

### 1. Strict 4/4 batch 在两个正常 production pre-render selector failure 后不可在 041 内恢复

**Plan / regression basis**

Frozen Plan 明确要求四篇全部通过 normal production entry、render、item/page-level Terra、contact-sheet mature bar 与 Planner review；任何一篇失败即整个 batch FAIL。batch 内禁止修改 production generator、gold library、selector/layout rules、prompt、validator、quality-loop mapping，也禁止替换 paper 或改 frozen source bundle 追结果。

**Observed evidence**

- TMB 的真实 invocation 在 `build_gold_composition_recipe.build_recipe()` 中因无兼容成熟构图记录抛出 `ValueError: no compatible gold composition record`，未产生 PDF、rendered page 或 contact sheet。
- RETFound 发生相同的正常 production selector failure，也未产生 rendered pixels。
- 最新 Terra 的 batch-level finding 继续把两项 pre-render failure 记为 blocking evidence；可视化子集不能替代 4/4 render availability。

**Minimal repair**

041 内无合法 repair。不得为这两篇修改 selector/gold/layout/source bundle，也不得替换 paper。

**Required closure evidence**

041 的终止记录必须明确四篇全部 consumed、batch FAIL、无 replacement、无 holdout-specific hardcode、无第三轮 review。该证据已经成立。

### 2. Review 1 允许的唯一 shipped automatic repair 已真实尝试，但 fail closed；不得再进行第二次尝试

**Plan / regression basis**

每个 deck 最多只能使用 batch freeze 前已经 shipped 的一次 bounded automatic repair。若 finding 无安全、唯一映射，应 fail closed；不能修改 repair mapping 后再对同一 holdout 重试，也不能手工 patch `.tex`、图片、caption 或 source bundle。

**Observed evidence**

- DESeq2 `quality_loop_state.json`：`deck_level_decision=UNSAFE_REPAIR_MAPPING`、`selected_repair_directives=[]`、`repair_cycle_count=0`、`final_decision=QUALITY_LOOP_FAIL_NO_WINNER`；初始与最终 render/pixel identities 未发生变化。
- cardiac-ultrasound 同样以 `UNSAFE_REPAIR_MAPPING / QUALITY_LOOP_FAIL_NO_WINNER` 结束，没有 selected directive，也没有新 pixels。
- DESeq2 的首个真实 scale finding 所对应页面在 sequence summary 中使用 paper-specific scientific-object label；当前 frozen repair mapper只对有限通用 object-kind vocabulary做安全自动映射。这是一个可在后续 generic recovery 中处理的通用语义兼容性缺口，但 041 内不得改 mapper 后重新消费 holdout。

**Minimal repair**

041 内无第二次 repair。保留 fail-closed 结果作为产品真实行为证据。

**Required closure evidence**

RESULT / FINAL_REPORT 必须记录 consumer 已真实运行但未产生 repair directive 或像素变化；不得把 `repair_cycle_count=0` 误写成“尚未尝试，所以还能再来一次”。该证据已经成立。

### 3. Fresh Terra 仍对最终未变化像素给出 blocking visual findings

**Plan / regression basis**

Final bar 要求 item/page-level projection readability 和 contact-sheet mature doctoral-group-meeting quality。顶层 package 可审查不等于质量 PASS。

**Observed evidence**

- 最新 Terra `BF-03`：DESeq2 slide 4 底部解释文字与 source label 可见重叠，slides 6/7 底部文字也仍碰撞或超出内容区；DESeq2 contact sheet 为 `REVISE`。
- 最新 Terra `BF-04`：cardiac-ultrasound slide 4 的 source label 与解释正文可见重叠；cardiac-ultrasound contact sheet 为 `REVISE`。
- 最新 Terra `BF-02` 还明确保留 quality-loop fail-closed 为 batch blocker。
- 因 render identities 未变化，早先 Terra 对多张论文 figure/page evidence 投影尺度过小的观察也不能被“没有像素变化”的后续执行动作视为已修复；最新 evidence 至少已经足够单独阻止两套 rendered deck 达到冻结 bar。

**Minimal repair**

不在 041 内继续修改。下一步只能在独立 non-holdout stress material 上恢复通用语义选择/repair compatibility 与布局容量行为，然后重新做真实视觉审核。

**Required closure evidence**

041 终止为 failed batch；后续 generic recovery 必须使用与四篇失败论文无关的测试输入，并在新的真实 pixels 上证明改进，不能引用本批 page-specific content 作为 tuning fixture。

## Non-blocking notes

- 真实 GitHub CI 已通过；当前失败不是 CI、发布或视觉证据缺失造成的。
- production freeze 得到保持；从冻结 locator 到当前主分支没有发现 presentation production/gold/layout/prompt/validator/quality-loop/template 行为漂移。
- DESeq2 的统计模型页已经证明 paper-specific 数学内容可以在 exact CUHK 中清晰呈现；cardiac-ultrasound 也确实使用了真实论文超声像素。后续 generic recovery 应保护这些已成立能力，而不是整体重写系统。
- 当前证据将后续通用恢复收敛为有限问题：成熟构图选择对通用科学对象语义的兼容性，以及相同语义层如何被 bounded quality loop 安全识别并真正驱动已有像素级 repair。不得通过向 selector/mapper 加 TMB、RETFound、DESeq2 或 cardiac-ultrasound 专用关键词解决。