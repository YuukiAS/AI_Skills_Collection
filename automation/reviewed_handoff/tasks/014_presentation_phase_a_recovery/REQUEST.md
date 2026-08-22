# 014 Presentation Phase A Recovery — Request

本任务承接 `013_presentation_todo_consolidation` 在第 2/2 轮审查后进入人工决策点的状态。用户已明确授权一次人工依赖修复，目的仅是补齐 Presentation regression 在干净 GitHub runner 上所需的 CI/test dependency contract，然后恢复 Phase A 的真实 CI 与独立内容审核。

`013` 的历史 `REVIEW_1.md`、`REVIEW_2.md`、`FINAL_REPORT.md` 与 `AWAIT_HUMAN_DECISION` 必须保持原样，不能改写成 PASS，也不能把本任务当成自动第三轮审查。当前 main 已包含用户授权后的依赖修复提交；本任务首先验证该修复是否完整、真实 CI 是否恢复，然后独立审核 013 原冻结计划的 TODO consolidation 内容。

范围严格限制为：Presentation regression 的 CI/test dependency contract、与该依赖修复直接相关的验证，以及对既有 013 实现的独立 closure review。不得修改 TODO 分类语义、Terra 四页内容、source corpus、reference acquisition、statistical/medical benchmark 或 Presentation 长期架构。只有本 recovery task 独立 PASS 后，Phase A 才视为通过人工授权恢复并关闭，之后才能进入 Phase B。
