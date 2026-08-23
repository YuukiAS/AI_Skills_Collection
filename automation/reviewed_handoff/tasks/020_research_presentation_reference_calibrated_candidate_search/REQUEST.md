---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 020_research_presentation_reference_calibrated_candidate_search
---

# 020 Research Presentation Reference-Calibrated Candidate Search — Request

## Why this task exists

019 已经把真实 inspected research-slide references 转成可查询的 renderer-neutral composition representation，但当前系统仍没有证明这些构图记录会真正进入生成决策。

如果下一步只是把 `layout_family` 或 primary bbox 写进日志，系统仍可能退回旧路径：

```text
reference composition
-> prose / family name
-> generator凭默认习惯只生成一版
```

本任务要建立真正的 **composition -> candidate** 层：对同一份真实 scientific slide content，内部产生三个构图逻辑确实不同、可渲染检查、可追溯到 inspected composition exemplars 的候选方向。

## User-facing product goal

长期目标仍是一次调用生成成熟科研 PPTX / Beamer，而不是要求用户逐页选择 layout。

因此 020 的三个候选默认只用于**内部设计搜索**。本任务不要求用户挑选，也不实现最终 comparative Terra adjudication；它只证明系统已经有多个真实视觉候选可供下一阶段独立比较，而不是单次默认布局。

## Scope constraint

020 只实现 reference-calibrated candidate search / preview 层：

- 必须消费 019 的 composition index / selector；
- 必须使用同一 scientific content 生成真实不同的候选构图，而不是三个配色变体；
- 必须保留 reference-to-candidate geometry transfer 证据；
- 候选 preview 必须使用真实科研内容，不得是 lorem ipsum、空占位卡或纯 wireframe；
- 不得复制 source screenshot、论文 figure pixels、品牌主题或整页 artwork；
- 不得扩 reference corpus；
- 不得修改 Terra / comparative review；
- 不得开始真实 holdout one-shot benchmark；
- 不得宣告 `ONE_SHOT_QUALITY_PASS`。

本任务完成后，下一阶段才有资格把 candidate previews 与 matched real exemplars 一起送入 comparative visual review。
