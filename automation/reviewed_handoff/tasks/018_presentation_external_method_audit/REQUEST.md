# 018 Research Presentation External Method Audit — Request

用户已明确否定上一轮 10 页 synthetic review pack 作为“高质量科研汇报”的金标准。上一轮结果仅保留为工程链路、科学正确性与基础视觉 QA baseline；长期目标仍不是 `PROGRAM_MATURE`，而是建立能够在新的真实科研材料上一次调用稳定生成成熟 PPTX / Beamer 的 Presentation 系统。

本任务是新一轮 `REFERENCE_CALIBRATED_ONE_SHOT_QUALITY` 的第一个 bounded task。目标不是立即修改 generator，也不是继续增加 synthetic benchmark，而是先对公开 Presentation skill / workflow 与本仓库当前实现做方法审计，找出真正值得进入下一阶段架构设计的机制、许可证边界和当前能力缺口。

必须覆盖至少：

- `zarazhangrui/frontend-slides`
- `andyqiu847-ai/high-quality-slides`
- `brycewang-stanford/many-ppt-skills`
- `RFYoung/slideweaver`
- `wmyung/manuscript-to-editable-slides`
- `sunzhejian/academic-paper-image-ppt`
- `hugohe3/ppt-master`（若当前公开仓库可正常访问）
- Assertion-Evidence Approach
- MIT Communication Lab 的科研/技术演示指导
- PLOS 的科研演示设计指导

审计必须基于实际源码、`SKILL.md`、布局/设计/渲染/QA 文件和公开一手指导页面，而不是只读 README 或二手介绍。

本任务只形成方法审计与下一阶段建议，不得 vendor 整个外部仓库，不得复制许可证不兼容或来源不清的资源，不得直接修改 active Presentation skill / generator / Terra rubric / reference corpus，也不得提前实现 composition layer、multi-candidate search 或 holdout benchmark。
