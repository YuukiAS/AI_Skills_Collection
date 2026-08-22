# Research Presentation Current Round

当前 improvement cycle 已进入 **Phase C：跨领域 Presentation benchmark**。

Phase A 已通过人工授权后的 `014_presentation_phase_a_recovery` 合法关闭；013 的两轮 `REVISE`、review-limit 与人工决策历史保持可追溯。Phase B 的 `015_presentation_terra_blocker_repair` 也已完成第二轮独立审核并 PASS：最初的 metric-direction、medical-image area、comparator-path 三个 blocker，以及 REVIEW_1 追加的 synthetic evidence-boundary 与 TP/FP/FN overlay legend 两个局部 blocker均已关闭。

015 第二轮最新 `gpt-5.6-terra` evidence 对 slide 1、2、4 给出 PASS；对 slide 3 新提出 connector direction/arrowhead 可读性意见。但 slide 3 当前 PNG SHA 与上一轮 Terra 给 PASS 时完全相同，且第二轮 implementation 未修改该页，因此该观察被记录为 **non-blocking reviewer-variance / diagram-clarity note**，不以模型对同一像素的重复判断差异推翻已冻结 accepted element。该观察将转入 Phase C statistical benchmark 的真实新页面中继续验证 connector direction、arrowhead、crossing 与 5 秒可读性。

## 当前 bounded task

```text
016_statistical_method_group_meeting_benchmark
```

这是 Phase C 的第一类 benchmark：statistical / biostatistical method group meeting。

### 016 冻结目标

建立一个 5 页、public-safe、真实可编辑/渲染的统计方法组会 benchmark，使用 coherent synthetic multi-center inference story：中心内相关会让 naive iid interval coverage 失真；cluster-robust inference 修正主要问题，但 small-center stress regime 可能仍暴露负结果。

五页分别承担：

1. statistical model / estimand；
2. estimator / variance derivation；
3. simulation design；
4. result figure + uncertainty；
5. negative result + next discriminating experiment。

具体冻结语义以：

```text
automation/reviewed_handoff/tasks/016_statistical_method_group_meeting_benchmark/PLAN.md
```

为准。

本任务使用现有 inspected reference corpus，不扩 source corpus、不做 Source Scout。Simulation 结果必须由 deterministic script 实际生成，不允许手工编造结果图。每页语义检索 2–5 个 inspected reference pages，并保留 retrieval trace。

Slide 3 如果使用 diagram，必须使用真实结构 connector、可见 arrowhead、单一阅读方向并避免 edge crossing；这一要求用于在新 benchmark 中检验 015 留下的 diagram-clarity note，而不是回头重做已接受的 015 slide。

## 视觉与 CI 链路

016 必须重新建立自己的 evidence identity：

```text
editable PPTX
-> real presentation engine
-> PDF / PNG
-> mechanical QA
-> results/016_statistical_method_group_meeting_benchmark/visual_review/visual_inputs.json
-> Bridge Kit gpt-5.6-terra Visual Review
-> tracked VISUAL_REVIEW.json
-> Scheduled Planner independent review
```

每个新 visual identity 正常 live review 一次，不为追求 PASS 重刷 API。Terra 的学术 `REVISE` 不等于 transport failure。

## 后续顺序

016 独立 PASS 后，Phase C 仍必须再完成一轮：

```text
medical-imaging research group meeting benchmark
```

医学影像 benchmark 必须真实检验 image / GT / prediction / overlay、failure case、quantitative result、method/experiment diagram、validation/endpoint semantics 等科研对象，并继续经过 real render + mechanical QA + `gpt-5.6-terra` evidence + Planner review。

只有统计/生统和医学影像两类 benchmark 都通过，且 source/generated/tests/visual evidence 没有未关闭 blocker，才能判断本次 Presentation improvement cycle 是否可以收口。cycle PASS 不等于长期 `PROGRAM_MATURE`。

当前不执行 Source Scout。
