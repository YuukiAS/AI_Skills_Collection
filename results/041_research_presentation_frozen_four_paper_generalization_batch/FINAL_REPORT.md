# Final Report

## What this task solved

041 完成了第一次严格意义上的四论文冻结批次泛化验收。它解决的不是“把四套 deck 调到通过”，而是用同一套冻结 production system、同一套冻结 source-bundle 规则和同一套 shipped quality-loop contract，真实测量当前 `research-presentations` 对四篇未见论文能否一次生成成熟博士组会级 presentation。

结论是：当前系统尚未达到 Stage 5 泛化标准。本批 4/4 要求失败，四篇全部按规则计为 consumed holdouts。这个失败是有效产品证据，而不是流程中断：它把当前剩余缺口从抽象的“可能泛化不好”收敛成可验证的通用机制问题，同时保持了 holdout 的统计意义，没有通过换论文、追结果或手工修页制造成功案例。

## What changed

本 task 只新增并更新了 041 自己的 source、execution、render、visual-review 和 Reviewed Handoff evidence；batch 期间没有修改 presentation production generator、gold library、selector/layout rules、prompt/routing、validator、quality-loop mapping 或 canonical CUHK template。

四篇论文先整体通过 eligibility / contamination preflight，再全部完成 source acquisition 与 source-bundle freeze，之后才开始任何 production render。最终真实结果为：

- TMB：正常 production entry 在成熟构图选择阶段失败，未进入 render；
- DESeq2：生成 exact-CUHK deck，但真实视觉审核未达到冻结质量门，并且 shipped quality-loop consumer 无法安全映射 finding，未产生 repair pixels；
- cardiac-ultrasound：生成 exact-CUHK deck并使用真实论文超声像素，但同样未达到冻结视觉门，quality loop fail closed；
- RETFound：正常 production entry 在成熟构图选择阶段失败，未进入 render。

Review 1 后允许的唯一动作也已经执行：DESeq2 与 cardiac-ultrasound 都真实调用了冻结前已有的 bounded quality-loop consumer。两者都没有得到安全 repair directive，render identities 与 pixels 保持不变，因此没有伪造“自动修复已生效”。

## New capabilities / behavior

041 新增的主要价值是可靠的真实泛化证据链，而不是新的 production feature。现在可以明确区分三件以前容易混在一起的事情：正常入口是否能为真实论文找到成熟构图、真实 deck 是否达到投影/整套节奏质量、以及视觉 finding 是否能通过已经发布的 bounded repair mechanism 安全落到新像素。

本批证明当前系统在这三层仍存在实际缺口：成熟构图检索对更广真实 scientific-object 语义覆盖不足；部分真实论文页面/图像在通用布局中仍会出现尺度或底部容量问题；而现有 repair mapper 对某些 paper-specific object label 无法安全归一到通用 repair family。与此同时，已有能力也得到保护性证据：DESeq2 的统计模型页可以清晰呈现论文特异数学内容，cardiac-ultrasound 可以真实使用论文超声像素，exact CUHK route 与 source freeze 均工作正常。

## Deliberately not adopted / unchanged

没有采用任何会污染 holdout 的捷径：没有把 TMB 或 RETFound 换成更容易的论文，没有为两篇 selector failure 增加 paper-specific gold/keyword，没有修改 DESeq2 或 cardiac-ultrasound 的 frozen source bundle，没有手工 patch 生成后的 TeX/PDF/PNG，也没有在第一次 quality-loop fail closed 后修改 mapping 再重跑。

没有降低 mature doctoral-group-meeting / strong paper-talk bar，也没有把 CI PASS、机械 render 成功、顶层视觉包可审查或 2/4 可生成解释成 Program PASS。038 已消费的 brms/MedSAM 也继续保持排除；本批四篇从此同样不能重新作为 unseen acceptance paper 使用。

## Example usage

从普通用户视角，041 模拟的就是最终产品场景：给系统一篇新的统计方法论文或医学影像论文，要求生成 CUHK 组会汇报，不额外逐页指定布局，也不允许开发者看完输出后再针对该论文改规则。

当前实测意味着：如果新论文的科学对象与现有成熟构图索引的语义标签不能稳定匹配，系统可能在生成前安全停止；如果能够生成，真实论文图像/图表与引用区域仍可能在部分页面出现投影尺度或容量问题；若视觉 finding 无法安全映射到已有 repair family，系统会选择 fail closed，而不是盲目修改科学内容。这种保守失败优于伪造成功，但还不满足最终“一次调用即可用于组会”的产品目标。

## Regression and remaining limitations

真实 GitHub CI 已通过，task-local visual-review workflow 也成功运行；production freeze 审计未发现 batch 期间 presentation production behavior 漂移。最新 Terra 与最终 implementation、manifest、source-bundle identities 和 rendered pixels 绑定，仍保留两个 pre-render selector blockers、quality-loop fail-closed blocker，以及 DESeq2 / cardiac-ultrasound 的可见底部文字与引用碰撞；两个 contact sheet 都没有达到冻结质量门。

041 已达到两轮独立审核上限，不会产生第三轮，也不会在同一批论文上继续追修。按照 Program Goal，下一步只允许在完全独立的 non-holdout / synthetic / public-safe regression 上做 bounded generic recovery。恢复过程中不得使用本批四篇的正文、图片、标题、DOI、page-specific content 或 rendered pixels 作为 tuning fixture。

generic recovery 如果通过，也不能自动消耗下一批 fresh holdout；在冻结下一组四篇真实论文前，必须向用户报告本批失败原因、通用机制修复内容和新增证据，并取得是否继续投入下一批的明确决定。

## Technical appendix

- Task: `041_research_presentation_frozen_four_paper_generalization_batch`
- Final reviewed implementation commit: `9bd69e5b54e7968ec731e00a3c9794c6fad21672`
- Production-freeze locator: `d3379b5168bc27b114b362f186f8c239a88a669c`
- Review decision: Round 2 `REVISE`; task reaches the two-round review limit and remains a failed frozen batch.
- GitHub CI: PASS on the published 041 handoff/control head; Codex Marketplace and AI Bridge Visual Review workflows completed successfully.
- TMB / RETFound failure: `ValueError: no compatible gold composition record` before render.
- DESeq2 final quality-loop state: `UNSAFE_REPAIR_MAPPING / QUALITY_LOOP_FAIL_NO_WINNER`, `repair_cycle_count=0`, no selected directive, unchanged rendered-pixel identity.
- Cardiac-ultrasound final quality-loop state: same fail-closed outcome, no selected directive, unchanged rendered-pixel identity.
- Latest visual evidence: `results/041_research_presentation_frozen_four_paper_generalization_batch/visual_review/VISUAL_REVIEW.json`
- Batch result: `results/041_research_presentation_frozen_four_paper_generalization_batch/RESULT.md`
- Round reviews: `REVIEW_1.md`, `REVIEW_2.md`
- Frozen source manifest: `results/041_research_presentation_frozen_four_paper_generalization_batch/batch_source_bundle_freeze_manifest.json`
- Production invocation trace: `results/041_research_presentation_frozen_four_paper_generalization_batch/production_invocations.json`
