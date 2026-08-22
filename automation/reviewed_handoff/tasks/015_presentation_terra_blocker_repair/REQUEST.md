# 015 Presentation Terra Blocker Repair — Request

Phase A 已通过 `014_presentation_phase_a_recovery` 完成用户授权后的 CI 与 TODO consolidation closure。当前进入 Phase B，只处理现有 canonical `gpt-5.6-terra` 四页 research-group-meeting regression 中已经有真实 visual evidence 支持的 blocker。

当前 canonical evidence 为 `results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json`：slide 1、2、3 为 `REVISE`，slide 4 为 `PASS`。本任务的目标是对这三个已确认问题做最小、可回归的 generator/fixture 修复，保持已接受页面和科学语义稳定；重新通过真实 PPTX render、mechanical QA 与一次新的 Terra Visual Review 后，再交独立 Planner 复核。

不得扩 source corpus、做 Source Scout、启动统计/医学影像新 benchmark、重做 Presentation 插件架构或重复提升 Phase A 已存在的通用规则。Phase C 必须等本任务独立 PASS 后再开始。
