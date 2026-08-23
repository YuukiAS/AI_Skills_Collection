---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 021_research_presentation_comparative_reference_calibrated_visual_review
---

# 021 Research Presentation Comparative Reference-Calibrated Visual Review — Request

## Why this task exists

020 已经证明同一份科研内容可以基于真实 inspected composition records 生成三个构图上真正不同、且 geometry transfer 可追溯的内部候选。但“候选确实不同”不等于“候选已经达到成熟科研汇报水平”。

如果下一步仍然只让 Terra 对 generated candidate 做绝对 `PASS/REVISE`，系统依旧会重演上一轮失败：只要页面可读、对象存在、没有明显机械错误，就可能把中等质量的程序化页面误判成高质量科研 slide。

本任务要建立真正的 **candidate -> comparative reference-calibrated review** 层：把 020 的 generated candidates 与匹配的真实 inspected reference renders 放入同一视觉审查上下文，让独立视觉 reviewer 判断它们在构图、排版、科学对象层级、图/公式/影像处理、标注、自然学术语言与 AI 模板痕迹上的相对差距。

## User-facing product goal

长期目标仍是：用户给出新的科研材料后，系统内部完成设计探索与选择，最终一次调用得到接近成熟教授组会 / 顶会 oral 的 PPTX 或 Beamer，而不是要求用户逐页纠正。

因此 021 的 comparative review 是内部质量裁判，不是用户 style picker。它必须允许：

> 三个 candidate 都明显低于真实 reference bar，因此没有任何 candidate 应被选为最终方向。

不能把 “best of three” 自动等价成 “good enough”。

## Scope constraint

021 只实现和验证 comparative reference-calibrated visual review：

- 使用 020 的两个 regression requests 和三个 candidate previews；
- 为每个 request 加载 2–4 个真正匹配 page job 的 inspected reference renders；
- 实际送审 reference pixels 必须绑定 SHA，不得只用 metadata / RRL prose；
- Terra-visible item 使用匿名 ID，不暴露作者、机构、RRL/source ID 或“这是 reference / 这是 generated”的身份提示；
- reviewer 先独立评价所有匿名 items，再形成相对排序与差距说明；
- review evidence 必须能在审查后由内部 mapping 解码回 candidate / reference identity；
- 允许输出 `NO_CANDIDATE_MEETS_REFERENCE_BAR` 或等价结论；
- 不修改 Bridge Kit 通用 core；
- 不修改 candidate geometry 以追求本轮 PASS；
- 不锁定完整 deck design system；
- 不开始真实 statistical / medical-imaging holdout；
- 不宣告 `ONE_SHOT_QUALITY_PASS`。

本任务完成后，Planner 再根据 comparative evidence 决定下一 bounded task 是修 candidate/design layer、建立 deck-wide design-system lock，还是先补其他审查机制。
