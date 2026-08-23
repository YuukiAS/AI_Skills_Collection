---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 022_research_presentation_candidate_visual_finish_repair
---

# 022 Research Presentation Candidate Visual Finish Repair — Request

## Why this task exists

021 已经建立可信的匿名相对视觉审查，并给出了第一批真正有用的质量差距：当前 candidate engine 虽然能消费真实 reference geometry，但“构图来源正确”仍不等于“页面视觉完成度达到成熟科研汇报水平”。

统计 estimator/equation case 中，真实 inspected reference RRL-028 明显优于三个 generated candidates。generated 中最好的 reference-faithful 版本仍存在公式对比度/可读性不足、annotation 没有直接整合数学对象的问题。

医学影像 case 中没有任何 item 达到 mature research-group-meeting / strong conference-talk bar。generated candidate 的主要可修问题包括 image prominence、panel integration、页面过稀或证据区域过小；同时，当前 synthetic fixture-like imagery 本身也限制了成熟度判断，不能靠继续“美化 toy phantom”把它包装成真实科研证据。

因此下一步不应该继续扩 reference metadata，也不应该直接锁完整 deck design system。必须先修 **candidate visual finish / scientific-object treatment**，让 reference-derived geometry 真正落成更成熟的 equation / medical-image 页面。

## User-facing product goal

长期目标仍是一次调用稳定产生接近成熟教授组会 / 顶会 oral 水平的 PPTX 或 Beamer。用户不应该负责逐页指出公式太淡、主图太小、annotation 与 scientific object 脱节、页面像 neutral fixture 或 synthetic demo。

022 要关闭的是这种“geometry 对了但 visual finish 仍像程序化 regression preview”的差距。

## Scope constraint

022 只允许：

- 保留 019/020 已验证的 composition selection、source geometry transfer 与 compatibility gate；
- 改进 candidate renderer 的 page-level visual treatment / scientific-object treatment；
- 重点修统计 equation page 的公式对比度、投影可读性与直接数学 annotation；
- 重点修医学影像 page 的 image prominence、panel integration、legend/annotation 与无效留白；
- 删除/避免 primary scientific object 周围的默认 rounded-card / generic neutral-fixture 表达；
- 为这些修复增加 deterministic manifest/tests；
- 重新生成两个 controlled requests 的三个 candidates；
- 使用 021 已建立的 comparative pipeline，在新的 immutable identities 下各执行一次 live Terra review，确认 repair 是否真实缩小与 reference bar 的差距。

022 不允许：

- 扩 reference corpus；
- 修改 Bridge Kit core / role / state machine；
- 为某一张 021 reference 写死坐标或视觉样式；
- 修改 019 composition records 来迎合结果；
- 破坏 020 的 scientific-job compatibility gate；
- 把 synthetic medical fixture 声称为成熟真实医学影像证据；
- 锁定完整 deck-wide design system；
- 开始真实 statistical / medical-imaging holdout；
- 开始 Beamer holdout；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

022 完成后，Planner 根据新的 comparative evidence 决定是否已经可以进入 deck-wide design-system locking / generation integration，或仍需一次 bounded candidate-layer repair。
