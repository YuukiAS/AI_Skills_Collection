# Research Presentation Current Round

当前 improvement cycle 已进入 **Phase A：TODO consolidation**。

当前标准 Reviewed Handoff task：

```text
013_presentation_todo_consolidation
```

当前状态：

```text
PLAN_FROZEN
```

下一动作：本地 Reviewed Handoff watcher 启动 Codex Executor，严格执行 `013_presentation_todo_consolidation/PLAN.md`。本轮只整理 `research-presentations/TODO.md`、提升 Planner 已冻结的少量高价值通用规则并补 regression tests；不扩 source corpus，不做 Source Scout，不开始新的 benchmark，不返修当前 Terra 四页 regression。

## 当前视觉证据基线

`012_presentation_visual_adapter` 已建立 Bridge Kit Shared Visual Review 主路径。当前 canonical Terra evidence 仍为：

```text
results/012_presentation_visual_adapter/visual_review/visual_inputs.json
results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json
```

当前 canonical review provider/model：

```text
openai / gpt-5.6-terra
```

该 evidence 的总体结论仍为 `REVISE`；已知视觉 findings 将在 Phase A 独立 PASS 后进入新的 bounded Phase B task。旧 `011_round_handoff` Pages/screenshot route 只保留历史 provenance，不再是 primary machine-consumption path。

## Phase A 冻结边界

TODO 中每个 checklist item / 独立规则必须归入且只归入：

- `ALREADY_IMPLEMENTED`
- `PROMOTE_NOW`
- `KEEP_BACKLOG`
- `DUPLICATE_OR_SUPERSEDED`

有用历史经验必须保留。当前已经存在于 active archetype/skill 的 metric favorable-direction、medical evidence area、experiment-design comparator path 等规则不得重复造第二套；当前 Terra failure 说明实现未遵守规则，不说明规则不存在。

本轮只允许提升三类已经有真实返修证据的通用规则：revision scope/correction regression、diagram semantic gate + structural connectors、real evidence vs conceptual grounding。theorem/simulation/derivation/prior/scaling 等更细规则若尚缺对应 benchmark，则保留 backlog 或按已有更强规则标注，不在本轮强行硬编码。

## 后续顺序

只有 013 经独立 Planner review PASS 后才进入：

1. Phase B：建立新的 bounded task，核对并修复当前 canonical Terra visual blockers，生成新 visual identity 后只做一次正常 Terra review，再由 Planner 独立判断；
2. Phase C：至少完成一轮 statistical/biostatistical method group meeting 和一轮 medical-imaging research group meeting benchmark，均需真实 render + mechanical QA + current Terra evidence + Planner review。

当前不执行 Source Scout。
