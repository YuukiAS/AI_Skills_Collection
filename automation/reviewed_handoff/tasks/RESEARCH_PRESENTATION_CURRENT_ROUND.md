# Research Presentation Current Round

当前 improvement cycle 已进入 **Phase B：Terra blocker repair**。

Phase A 已通过用户授权后的 recovery task `014_presentation_phase_a_recovery` 关闭。013 的两轮 `REVISE`、review-limit 与人工决策历史保持可追溯；014 没有把 013 改写成“从未失败”，而是验证了完整 Presentation regression CI/test dependency contract，并在真实 GitHub runner 上恢复了全库测试与独立 closure review。014 的 `REVIEW_1.md` 结论为 PASS，真实 CI run `32562190645` 的 `codex-marketplace`、Windows sparse checkout、Windows/Linux editable-install smoke 均成功。

当前标准 Reviewed Handoff task：

```text
015_presentation_terra_blocker_repair
```

本阶段只处理当前 canonical `gpt-5.6-terra` 四页 regression 已有证据支持的三个 blocker，不扩 corpus、不做 Source Scout、不提前开始 Phase C benchmark。

## 当前视觉证据基线

当前 canonical evidence 仍为：

```text
results/012_presentation_visual_adapter/visual_review/visual_inputs.json
results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json
```

当前 identity 的总体结论为 `REVISE`：

- slide 1 / RESULT_FIGURE：burden error 的 favorable direction 与 winner claim 不一致；
- slide 2 / FAILURE_CASE：image / GT / prediction / FP-FN overlay 在 oversized panel 中过小，投影可读性不足；
- slide 3 / EXPERIMENT_DESIGN：local-only comparator 只存在于 prose/footer，global/local comparator 没有共同连接到 endpoint evaluation；
- slide 4 / STATISTICAL_MODEL：PASS，是本阶段 accepted element，不得随意重做。

旧 `011_round_handoff` Pages/screenshot route 仅保留历史 provenance，不再是 primary machine-consumption path。

## Phase B 冻结边界

015 以 `automation/reviewed_handoff/tasks/015_presentation_terra_blocker_repair/PLAN.md` 为唯一冻结语义。核心要求：

1. slide 1 保留 synthetic 数值，只修 favorable-direction 表达和错误 winner claim；
2. slide 2 保留同一 synthetic case/metrics，只扩大真实科学图像对象的页面占比；
3. slide 3 把现有 local-only comparator 变成真实 branch，并让两种 comparator 输出都连接 endpoint gate；
4. slide 4 作为 accepted element 保持稳定；
5. 返修后必须重新走真实 editable PPTX -> presentation engine -> PDF/PNG -> mechanical QA；
6. 重新生成 `visual_inputs.json` identity，并对新 identity 只做一次 `gpt-5.6-terra` live review；
7. conventional CI 与 Terra transport 均通过后，由 Scheduled Planner 独立判断旧 blocker 是否真正关闭。

本阶段不得重新提升 Phase A 已存在的同义规则，不得扩 Source Registry / Inspected Page Library / Synthesized Knowledge，不得启动新的统计/医学影像 benchmark。

## 后续顺序

只有 015 经真实 render、mechanical QA、current Terra evidence 与独立 Planner review PASS 后才进入 **Phase C**。Phase C 至少需要分别完成一轮：

1. statistical/biostatistical method group meeting benchmark；
2. medical-imaging research group meeting benchmark。

两类都必须经过真实 render + mechanical QA + `gpt-5.6-terra` evidence + Planner independent review，并继续沿用 Phase A 已保留的 audience-first、notation grounding、one-slide-one-job、scientific-object-first、source fidelity、diagram semantics/geometry、scientific hierarchy、主图面积、evidence boundary、revision scope、real-data grounding 等规则。

当前不执行 Source Scout。
