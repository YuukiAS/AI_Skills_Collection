# Research Presentation Current Round

当前 improvement cycle 仍处于 **Phase A：TODO consolidation recovery**。

`013_presentation_todo_consolidation` 已完成实现，但两轮独立审查都被 GitHub CI 测试环境的依赖声明问题截住：第一轮暴露 Pillow 缺失，第二轮暴露 `python-pptx` 缺失，因此按 Reviewed Handoff 上限进入人工决策点。其 `REVIEW_1.md`、`REVIEW_2.md`、`FINAL_REPORT.md` 与 `AWAIT_HUMAN_DECISION` 历史终态保持不变，不得改写成 PASS。

用户随后明确授权一次人工依赖修复。当前 main 已包含授权后的最小修复提交 `fdc2ddf30e6782362af7e3ff1c9322e48dfbef8e`：Presentation regression 的 CI/test environment 同时安装 `Pillow>=10` 与 `python-pptx>=1.0`，并在全库测试前做显式 import check。

为遵守 013 的 review-limit，同时合法消费这次人工授权，当前标准 Reviewed Handoff task 切换为：

```text
014_presentation_phase_a_recovery
```

当前目标不是重新做 TODO consolidation，而是：

1. 验证授权后的 Presentation regression 依赖 contract 是完整集合，而不是继续逐个追 ImportError；
2. 恢复真实 GitHub CI；
3. 在 CI 通过后，对 013 原冻结计划下的 TODO consolidation 内容做一次新的独立 recovery review；
4. 只有 014 PASS 后，Phase A 才视为通过人工授权恢复并关闭。

## 当前视觉证据基线

`012_presentation_visual_adapter` 仍是 Bridge Kit Shared Visual Review 主路径。当前 canonical Terra evidence 保持不变：

```text
results/012_presentation_visual_adapter/visual_review/visual_inputs.json
results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json
```

当前 review provider/model：`openai / gpt-5.6-terra`。该 evidence 的总体结论仍为 `REVISE`；已知 slide 1–3 findings 仍属于 Phase B，014 不得修改这些页面或生成新的 visual identity。旧 `011_round_handoff` Pages/screenshot route 仅保留历史 provenance。

## Phase A recovery 边界

013 已完成的 TODO 四分类和三类冻结 `PROMOTE_NOW` 是 recovery review 的内容对象，不在 014 中重新设计。014 只允许处理用户已授权的 CI/test dependency contract、必要验证、CI handoff 和独立 closure review。

本轮仍禁止：source corpus 扩张、Source Scout、新 benchmark、Terra 四页返修、Presentation plugin 架构重做。

## CI evidence

当 014 进入 `WAITING_FOR_CI` 后，本地 Codex/CI bridge 使用 `gh run` 读取真实 required workflows，并机械发布当前 main tip 上 context=`reviewed-handoff/ci-summary` 的 commit status。Scheduled Planner 以该 status 与可访问的 CI evidence 为事实来源；CI bridge 不做语义 review。

## 后续顺序

只有 014 经真实 CI + 独立 Planner review PASS 后才进入：

1. **Phase B**：建立新的 bounded task，核对并修复当前 canonical Terra visual blockers；生成新 visual identity 后只做一次正常 Terra review，再由 Planner 独立判断；
2. **Phase C**：至少完成一轮 statistical/biostatistical method group meeting 和一轮 medical-imaging research group meeting benchmark，均需真实 render + mechanical QA + current Terra evidence + Planner review。

当前不执行 Source Scout。
