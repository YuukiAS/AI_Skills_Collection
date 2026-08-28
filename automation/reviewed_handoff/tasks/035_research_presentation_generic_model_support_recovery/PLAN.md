---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 035_research_presentation_generic_model_support_recovery
decision: PLAN_FROZEN
---

# 035 Research Presentation Generic Model Support Recovery — Plan

## Objective and value

只关闭 034 Review 2 已明确定位的 generic-model source-grounding blocker：`STATISTICAL_MODEL` 页面为了补足模型解释层时，所有 audience-facing supporting science 必须来自当前 source/page-job fields，而不是从 Stage 4 clustered-calibration engineering fixture 写死。

完成后，同一个 normal production/layout path 应同时满足两件事：当前 clustered model page 继续保持公式主导、信息完整、视觉成熟；一个完全无关的统计模型页也只展示自己的模型对象与解释，不出现 ICC / center variation / interval comparison 等当前 fixture 语义，也不出现 `source-grounded` 之类制作语言。

这是 034 review-limit 后的质量保持 recovery。它不改变长期产品合同，也不扩展 Stage 5 范围。

## Frozen decisions

以下已经通过或已被真实 evidence 关闭的能力全部冻结保护：

- 034 dual identity contract：render-input identity 始终存在，pixel identity 只在真实 render 存在时严格绑定；
- 034 title/subtitle audience anti-meta gate；
- 当前 Stage 4 engineering deck 的 source-fidelity map、032 storyline、多 workstream continuity 与 transition；
- Stage 2 gold composition retrieval 和 Stage 3 executable CUHK layouts；
- canonical exact CUHK `.tex + PDF + PNG` production route；
- deck contact sheet、deck-level rhythm rubric、一次 automatic repair 上限、unknown/unsafe finding fail-closed/no-winner；
- medical same-case TP/FP/FN semantics；
- 当前 fresh Terra 已通过的 result / design / failure / next-experiment / medical 页面质量。

不得通过删除模型页 supporting layer、恢复明显欠填充页面、降低 Terra/mature-quality bar或给非 clustered paper 错配 clustered 文案来关闭本 task。

## Implementation scope

### 1. 把 equation supporting copy 改成真正 source-driven

限定修改共享 equation/model emission 及其直接 spec/test/mirror 支撑。优先处理：

- `skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py`；
- normal production spec propagation 若确有必要，可最小修改 `generate_research_presentation_production_entry.py`；
- 对应 `plugins/codex/plugins/presentations/...` mirror；
- `tests/test_presentations.py` 或现有同类 presentation regression fixture。

`STATISTICAL_MODEL` 页面允许保留公式主对象与两个紧凑 supporting blocks，但 body 文案只能来自当前 spec 已有的 source-backed 字段，例如：

- `scientific_objects`；
- `key_message`；
- `annotation`；
- 若已有或确需最小 schema-compatible 扩展，可使用显式 source-backed `caption` / support label。

通用 UI/furniture label 可以使用不携带当前领域科学结论的中性名称，例如 `Model components`、`Interpretation`；也可以消费显式 source-backed label。不要为了保留当前文字而新造复杂 schema。

必须移除或使以下当前 hardcode 不再作为所有 model pages 的默认 audience text：

- `Calibration link`；
- `Center variation and individual variation define the ICC before the interval comparison.`；
- `Source-grounded terms remain attached to the equation.`。

如果 `scientific_objects`、caption 等 supporting source field 不存在，允许减少 supporting block / caption；不得用制作语言或当前 clustered fixture 的科学陈述填空。已有 `annotation` / `key_message` 可在不重复堆字的前提下作为 source-backed fallback。

### 2. 用 unrelated-model regression 证明不是当前 fixture hardcode

必须增加一个有限、public-safe、非 Stage 5 的 model regression，其科学语义与 clustered interval calibration 明显无关。优先复用仓库已有 unrelated model fixture/spec；若不存在，只新增一个最小 synthetic test spec，不扩 corpus。

允许示例包括 survival/Cox、Bayesian logistic、causal estimation 或其他 methodology model。测试至少证明：

- normal/shared model layout/emission path 消费该 spec 提供的 `scientific_objects` / `key_message` / annotation；
- 生成 audience-facing TeX 中出现该 unrelated model 自己的术语；
- 不出现 `ICC`、`center variation`、`interval comparison`、`Calibration link`、`Source-grounded terms`；
- formula 仍是 primary scientific object；
- 不按 unrelated fixture 的完整标题、页号或 test ID 在 production code 写新分支。

不要求为 unrelated regression 生成完整七页 deck；目标是直接击穿共享 model-support hardcode。

### 3. 保持当前 engineering deck 的视觉成熟度

重新生成当前 Stage 4 engineering bundle，确保模型页不退回 Review 1 的公式+单句欠填充状态。当前 page 允许因为通用 label/caption 改写而产生新的 pixel identity，但必须保持：

- 公式仍是主对象；
- supporting information 只来自当前 model page source fields；
- 无 audience-facing internal/meta language；
- slide 3–7、storyline、CUHK identity、medical semantics 不做无关变化。

如果当前 deck pixels 变化，生成 task-local `visual_inputs.json` 并等待 fresh `VISUAL_REVIEW.json`，要求至少 model page 与 `deck_contact_sheet` item-level PASS；同时确认其余已通过页面无明显回归。缺 fresh visual evidence 时只等待，不消耗 review round。

### 4. CI / parity

shared 与 plugin mirror 必须保持 parity。Executor 重新运行 targeted/full presentation regressions、skills/marketplace validation、Reviewed Handoff validation 与真实 GitHub CI。不得通过删除 source-fidelity assertion 或把 forbidden current terms 只加入 test blacklist来假装通用化；核心生产文案路径必须真实改变。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 035：

1. 共享 `STATISTICAL_MODEL` renderer 不再无条件输出当前 clustered-calibration 专用 supporting science；
2. audience-facing model support body 全部可追溯到当前 spec/source fields，或为不承载科学结论的中性布局标签；
3. 缺少 supporting source fields 时不显示 `source-grounded` / workflow/provenance 类制作语言，也不虚构 clustered/ICC 文案；
4. unrelated-model regression 真实经过共享 model path，并证明没有当前 fixture term leakage；
5. 当前 Stage 4 engineering model page 仍保持完整、公式主导、source-faithful，不能回到明显欠填充；
6. 034 dual identity、metadata anti-leak、一次 repair budget、fail-closed/no-winner 全部无回归；
7. slide 3–7、032 storyline、多 workstream transition、exact CUHK identity、medical TP/FP/FN 不做无关改变；
8. shared/plugin parity、targeted/full tests、skills/marketplace/Reviewed Handoff validation通过；
9. 真实 GitHub `Codex Marketplace` CI 通过；
10. 若 engineering pixels 变化，fresh task-local Terra 与当前 implementation/pixel/contact-sheet identity 一致，`slide_2_statistical_model` 与 `deck_contact_sheet` item-level PASS，且无新的 blocker；top-level workflow success 不能替代 item-level evidence。

## Natural-language usage / routing expectations

用户仍只需要正常提供研究材料并请求生成科研组会汇报。若论文模型是 clustered mixed model，模型页可以解释 cluster/ICC，因为 source 本身支持；若论文换成 Cox、Bayesian、causal 或其他模型，模型页必须自动使用那篇材料自己的模型组件和解释，不应残留上一份 benchmark 的统计术语，也不应向听众展示“source-grounded”这类内部制作语言。

## Out of scope

035 不得：

- 重写 Stage 2 gold composition library；
- 重设计 Stage 3 全部 scientific layout system；
- 修改 deck-level quality-loop 状态机、review rubric 或 automatic repair 次数；
- 重做 032 storyline/workstream grouping；
- 修改 medical comparison semantics；
- 运行或调优 Stage 5 双-paper holdout；
- 增加新的外部 source/corpus scouting；
- 为了让当前 engineering fixture 像素不变而保留错误的 clustered hardcode；
- 因为发现新的“可以更优雅”的 abstraction 扩大任务。

### Stop condition

一旦 shared model-support path 的 current-fixture hardcode 被移除、unrelated-model regression 通过、当前 engineering model page 保持成熟、真实 CI 与所需 fresh visual evidence闭合，本 task 立即停止。若新的 evidence 暴露与 model-support source-grounding 无关的问题，只记录为 non-blocking backlog；若仍是同一 blocker但本有限机制无法关闭，再按 Program Goal 判断新的 bounded recovery，禁止在 035 内无限重试。
