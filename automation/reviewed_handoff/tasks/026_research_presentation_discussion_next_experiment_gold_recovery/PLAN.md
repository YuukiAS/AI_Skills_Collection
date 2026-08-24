---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 026_research_presentation_discussion_next_experiment_gold_recovery
decision: PLAN_FROZEN
---

# 026 Research Presentation Discussion / Next-Experiment Gold Recovery — Plan

## Frozen decisions

本 Plan 的业务语义保持不变：只关闭 025 留下的 `discussion / next experiment` Stage 2 coverage blocker；保留既有 9 条 production gold 与全部已通过能力；使用一次新的、有界、rights-safe 的公开 source scouting / intake / real-pixel admission；不得降低 mature bar，也不得开始 Stage 3。本节仅补足当前 Reviewed Handoff 的 schema-compatible heading，不新增业务范围。

## Frozen objective

只关闭 025 留下的一个 Stage 2 coverage blocker：为 `discussion / next experiment` scientific job 找到并准入至少一个真正达到 production-gold mature bar 的真实科研演示构图，并证明现有正常 runtime selection / consumption 路径能使用它。

025 已通过的 9 条 gold、selector、recipe builder、statistics / medical runtime probes 和全部历史 evidence 视为已关闭能力，不得重做。025 本身继续保持历史 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`，本任务不是 `REVIEW_3`。

## Required reading

Executor 至少读取：

- `automation/reviewed_handoff/schema.json`
- `automation/reviewed_handoff/README.md`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- 025 的 REQUEST / PLAN / CURRENT / RESULT / REVIEW_1 / REVIEW_2 / FINAL_REPORT
- 025 当前 gold index、gold schema、validator、selector、recipe builder、admission report、runtime probe traces
- 019–022 中与 source identity、real-pixel inspection、comparative mature-bar 和 rights/reuse boundary 有关的既有机制
- 当前 `research-presentations/SKILL.md` 与 `shared/visual-qa.md`

## Implementation scope

026 的实现范围仅限下述 recovery boundaries、有限 source scouting、真实像素准入、单一 discussion / next-experiment gold integration 与对应 runtime proof。不得扩成通用 corpus growth、Stage 3 renderer/layout、023 recovery、Terra core 修改或最终 holdout。本节仅补足当前 schema-compatible heading，不改变已冻结的细节边界。

## Frozen recovery boundaries

### 1. Preserve all passed Stage 2 work

不得重新审查、删除或重写现有 9 条 025 production gold，除非发现明确 regression/identity corruption；普通“想让库更漂亮”不是理由。

不得重做 statistics / medical runtime probes。只允许新增一个最小的 discussion / next-experiment runtime consumption proof，用现有 selector / recipe builder 正常路径证明新 record 可被选择和消费。

### 2. New finite external search space

本任务允许一次新的、严格有界的公开 source scouting，搜索空间与 025 的“只看现有 corpus”不同，因此属于质量保持的 recovery，而不是重复上一轮失败动作。

资源上限：

- 最多检查 8 个公开 source URLs / candidate decks 的可用性与相关性；
- 最多实际 intake/download 4 个公开 decks；
- 最多向 Terra 送审 12 个真实 rendered pages；
- 最多拆成 2 个 gold-admission visual packets；
- 达到关闭条件后立即停止，不为凑额度继续扩 corpus。

候选优先级：

1. 真实研究组会 / conference / seminar 中明确承担 discussion、open questions、limitations-to-next-test、next experiment、future validation、decision / next-step 等学术功能的页面；
2. statistics / biostatistics / medical imaging 或相邻科研方法领域优先；
3. 优先官方作者、实验室、大学、会议或机构公开页面上的 PDF/slides；
4. 不以营销 deck、咨询模板、通用“future work”三卡片页代替真实科研讨论页。

### 3. Rights-safe intake

所有新增 source 必须可公开访问并记录稳定来源 URL、作者/机构（若公开）、页面号、下载/检查日期和 rights note。

若没有明确可复用许可：

- source pixels 只能作为 inspection / comparative evidence；
- production gold payload 只能记录抽象 composition / hierarchy / geometry / relation lesson；
- 不得把 donor pixels、logo、branding、版权 figure 作为 runtime asset 打包；
- source render 如需保存 evidence，只能按 repository 现有 provenance / evidence 规则处理，不得扩大公开分发范围。

任何私有数据、登录后材料、付费购买、许可明显冲突或来源无法定位的候选直接排除，不得为了覆盖继续使用。

### 4. Semantic pre-screen before Terra

Terra 前必须先做轻量语义预筛。候选页面必须有可见 evidence 支持其 scientific job 确实属于下列至少一类：

- `DISCUSSION`
- `NEXT_EXPERIMENT`
- `OPEN_QUESTION`
- `LIMITATION_TO_NEXT_TEST`
- 与上述语义等价、且能明确映射到 Stage 2 的 `discussion / next experiment`

禁止因为标题含 `future`、`next`、`discussion` 等孤立词就自动进入候选。页面必须实际承担研究推理或下一验证动作，而不是结束页、致谢页或泛化 roadmap。

### 5. Real-pixel production-gold admission

每个拟入选页面必须基于实际 rendered pixels 做 026 专用 item-level admission。Terra rubric 至少判断：

- 是否达到 mature research-group-meeting / strong conference-talk 水平；
- 页面是否真正承载 discussion / next-experiment 科研推理，而非泛化模板；
- 主论点、当前证据/限制、下一验证动作之间是否有清楚层级与阅读路径；
- 是否存在 rounded-card dashboard、generic arrows、AI 模板感、空洞 future-work 列表或过量制作元语言；
- 投影尺度下是否可读；
- 是否存在可抽象复用的 composition lesson。

只读取 item-level decision / observation。Terra top-level package `PASS` 不构成 gold admission。

任何 item-level `REVISE` 页面继续作为 rejected candidate；不得为 coverage 强行进入 production gold。

### 6. Admission and runtime integration

对 item-level `PASS` 的页面：

- 按现有 gold schema 新增 record，不创建第二套 gold 数据模型；
- 绑定真实 source/page/render identity 与 026 reviewer-input SHA；
- 记录 scientific job、composition family、primary/supporting regions、reading flow、annotation/caption/panel relations、content capacity 与 rights/reuse boundary；
- 更新 admission report，明确这是 026 recovery admission，并保留 025 admission evidence provenance；
- 正常 selector 必须能针对 discussion / next-experiment query 返回该 record，并给出真实 compatibility reasons；
- recipe builder 必须实际读取该 record 的 source-derived composition fields；不得使用 `force_gold_id`、score override 或 test-specific hardcode。

至少保存一个 deterministic discussion / next-experiment runtime trace，证明：

`RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED`

这里不要求制造一个人为 alternate；只需证明新 record 在正常兼容查询下真实进入 recipe，并且屏蔽/移除该 record 后 selector/recipe 行为发生可解释变化或明确 no-compatible-result。不得为了证明变化而引入不兼容 alternate。

## Stop condition

一旦以下全部成立，立即停止 scouting 并交回 Planner：

1. 至少一个新增真实页面通过 026 item-level production-gold mature-bar admission；
2. 该 record 明确覆盖 `discussion / next experiment` scientific-job family；
3. 正常 selector / recipe 路径证明它被真实选择、消费并影响输出；
4. gold validator、相关 tests、source/plugin mirror 与 required CI 均通过。

如果在 8 source URLs / 4 decks / 12 Terra pages 的上限内没有任何页面达到 item-level `PASS`：

- 不降低 mature bar；
- 不继续无界搜索；
- 不进入 Stage 3；
- 在 RESULT 中记录实际搜索空间、被拒绝候选和原因，并路由回 Planner 判断是否存在新的质量保持机制或真正需要用户决定的问题。

## Validation

### Tests and validation

至少验证：

- 025 现有 9 条 gold 保持不变且 validator 继续通过；
- 新 record 对应真实 source/page/render identity；
- 新 admission evidence 为 026 item-level real-pixel `PASS`；
- rights/reuse boundary 合法且 donor pixels 不进入 runtime payload；
- discussion / next-experiment semantic compatibility gate；
- 正常 selector 可选择新 record；
- recipe builder 实际消费 source-derived fields；
- 屏蔽/移除新 record 后行为发生可解释变化或 no-compatible-result；
- audience-facing anti-meta leakage；
- source/generated plugin mirror（若现有架构要求）；
- 不修改 canonical CUHK template；
- 不修改 025 REVIEW/CURRENT/FINAL_REPORT 的历史语义与结论。

继续运行：

- gold-library / selector / recipe targeted tests；
- Presentation targeted tests；
- `python -m unittest discover -s tests`；
- `python scripts/skills.py validate`；
- marketplace validate/check/path-report（需要写入时按现有 workflow contract）；
- Reviewed Handoff validation；
- `git diff --check`；
- 新增真实 Terra packet 时保存 item-level evidence 与 identity binding。

## Out of scope

026 不得：

- 扩成通用 reference-corpus growth；
- 重做现有 9 条 gold；
- 改写 025 的历史结论、REVIEW/CURRENT 或 PASS/REVISE 语义；
- 修改 Stage 2 mature bar；
- 实现 Stage 3 LaTeX/TikZ/figure/image layouts；
- 修改 canonical CUHK visual identity；
- 恢复 023；
- 运行最终真实 statistical / medical-imaging paper holdout；
- 修改 Terra core / Bridge Kit reviewer semantics；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 026：

1. 025 的 9 条 gold 与历史 evidence 完整保留；
2. scouting/intake 没有超过冻结资源上限；
3. 至少一个新增 discussion / next-experiment page 有真实 source/page/render identity 与 026 item-level pixel `PASS`；
4. 新 record 不是 generic future-work/card template，而是成熟科研 discussion / next-experiment composition；
5. rights/reuse boundary 明确，未把 donor pixels/branding 作为 production runtime asset；
6. 正常 selector 能按 scientific job / object / domain / density 兼容逻辑选择新 record；
7. recipe builder 真正消费其 source-derived composition fields，并有 `selected -> consumed -> output-affected` trace；
8. 无 force-id、score override、test-specific hardcode 或人为兼容绕过；
9. required tests / validation / CI 全部通过；
10. 没有开始 Stage 3、023 recovery 或 final holdout；
11. RESULT 明确列出搜索范围、admitted/rejected candidates、Terra item decisions、rights notes、runtime evidence 与 remaining limitations。

026 PASS 后，Planner 才可把 Stage 2 整体标记为关闭并创建 Stage 3 — Executable CUHK Scientific Layout System 的独立 bounded task。Executor 不得自行继续。
