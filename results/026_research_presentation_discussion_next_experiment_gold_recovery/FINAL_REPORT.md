---
schema: AI_BRIDGE_REVIEWED_FINAL_REPORT_V1
task_key: 026_research_presentation_discussion_next_experiment_gold_recovery
---

# 026 Discussion / Next-Experiment Gold Recovery — Final Report

## 本轮解决了什么

026 只处理 Stage 2 最后一个未关闭的覆盖缺口：`discussion / next experiment`。它没有重做 025 已经通过的 9 条 production gold，也没有降低成熟度门槛，而是在新的、严格有界的公开 source 搜索空间里寻找可用页面，并用真实 rendered pixels 做 026 专用 Terra 准入。

最终找到并准入了一个真正达到 production-gold 标准的页面：`RRL-059 / SRC-077 / page 51`，对应新增 gold record `GSC-018`。该页面不是泛化 future-work 三卡片模板，而是以成对科学对象和具体下一步选择策略组织研究推理，因此可以为后续 discussion / next-experiment 页面提供受约束的成熟构图参考。

## 实际新增能力

Stage 2 现在第一次覆盖了完整冻结 scientific-job family，包括此前缺失的 discussion / next experiment。

新增 `GSC-018` 已进入现有 gold schema，而不是创建第二套数据模型；其 source/page/render identity、026 reviewer-input SHA、composition fields 与 `COMPOSITION_ONLY` rights boundary 均有记录。正常 selector 能在 discussion / next-experiment 查询下选中它，recipe builder 会实际消费其 `primary_bbox`、视觉层级、对齐、阅读方向、annotation/caption/panel relation 与内容容量等 source-derived fields。

运行时证明不是“索引里多了一个 ID”：当 `GSC-018` 存在时，正常 selector 能返回并生成对应 composition recipe；移除它后，同一查询得到 `no compatible gold composition record`。因此新增资源满足：

`RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED`

## 搜索与准入结果

实际资源账本为：

- 检查 4 个公开 source URLs；
- 其中 1 个 Google Drive PDF fetch 失败，未 intake；
- 实际 intake/render 3 个公开 decks：`SRC-075`、`SRC-076`、`SRC-077`；
- Terra 共审查 12 个真实 rendered pages；
- 共 2 个 admission packets。

第一批 8 页全部 item-level `REVISE`。第二批 4 页中只有 `item_C` 达到 item-level `PASS`，其余 3 页继续作为 rejected candidates，不为 coverage 强行提升。

这说明 recovery 的价值不在于扩大数量，而在于保持高门槛直到找到一个真正可用的成熟页面。

## 被拒绝的方案与原因

没有采用以下捷径：

- 没有把 025 中已判 `REVISE` 的页面重新包装成 gold；
- 没有把标题里含 `future` / `next` 的普通结束页自动当作 next-experiment；
- 没有降低 Terra mature-bar 来凑 coverage；
- 没有用 `force_gold_id`、score override 或 test-specific hardcode 伪造 runtime consumption；
- 没有把 source pixels、logo、branding 或许可不明 figure 作为 production runtime asset；
- 达到关闭条件后没有继续无界扩 corpus。

## 回归风险

本轮对既有 Stage 2 的回归风险较低：025 的 9 条 production gold、statistics / medical runtime probes 与既有 admission evidence 均保持不变。第一轮 review 发现的唯一问题只是 RESULT 对搜索资源计数写错；第二轮 repair 只修正这一行报告，没有触碰 gold、Terra、selector、recipe 或 corpus。

剩余风险已经转移到 Stage 3：gold composition 目前仍是 renderer-neutral constraints，尚未证明这些约束能在 exact CUHK Beamer content area 中稳定落成成熟的 native LaTeX/TikZ/figure/image layout。因此 026 PASS 不能代替 Stage 3 的真实 render 与视觉验收。

## 可直接理解的使用例子

当后续系统需要制作一页“当前方法局限意味着下一步该验证什么”的科研讨论页时，selector 可以把该 page job 映射到 `GSC-018`。下游不会复制原 donor page 的像素，而是读取它的抽象构图：主要科学对象如何并置、下一选择策略如何成为视觉重点、阅读方向如何组织、哪些说明应邻近主对象。这样 Stage 3 可以把相同构图逻辑重新表达为目标 paper 的真实 scientific content，并放入 CUHK 原生内容区。

## 当前未关闭的问题

026 本身没有剩余 blocker。Stage 2 可以整体关闭。

长期 program 仍未完成：Stage 3 需要把当前 gold composition 真正变成 exact CUHK Beamer 下可执行且成熟的 scientific layouts；Stage 4 还要接入普通 one-call production path 与 bounded quality loop；Stage 5 还需要两个真实、未参与 tuning 的 paper holdout 和最终用户人工验收。

## 技术附录

- final implementation commit: `490f879f1794603b0c906719e6321ec068e07de5`
- final handoff CI locator: `0a130aef3830034ca718d3e0961758dd4594b6d9`
- CI: `reviewed-handoff/ci-summary = success`
- GitHub Actions run: `32784838189`
- reviewed source URLs: 4
- intaken/rendered decks: 3
- Terra-reviewed pages: 12
- admission packets: 2
- newly admitted gold: `GSC-018`
- review rounds used: 2 / 2
- plan revisions used: 1 / 1

026 第二轮独立审核结论：`PASS`。
