---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 025_research_presentation_gold_scientific_composition_library
---

# 025 Research Presentation Gold Scientific Composition Library — Request

## Why this task exists

Stage 1 已把普通科研汇报入口纠正为 exact CUHK Beamer / `.tex + PDF`。下一步真正限制质量的不是继续增加抽象规则，而是：现有 reference corpus 虽然已经下载、检查并在 019–022 中形成过 composition records / candidate evidence，但“被 inspect 过”仍不等于“足以作为 production gold composition”。

如果没有一个经过重新筛选、带权限边界、能在运行时按 scientific job 检索并实际改变构图决策的 gold set，Stage 3 仍会让模型从空白画布自由发明布局，最终很容易重新退化成 generic cards、box-arrow、默认图表脸或 AI 模板感。

## User-facing product goal

完成本任务后，系统面对真实科研页面需求时，应能从**已经下载且实际 inspected 的成熟科研演示资源**中检索一小组与当前 scientific job 真正兼容的高质量正文构图，并把选中的 gold record 转成后续 CUHK layout system 可消费的 composition recipe / constraints。

这一阶段不要求直接生成最终漂亮 deck，但必须证明 reference 不是 metadata 装饰：被选中的 gold record 会被运行时代码实际读取，并改变下游 composition recipe；如果移除或替换该 record，输出 recipe 必须随之改变。

## Scope constraint

本任务只负责 Stage 2 — Gold Scientific Composition Library：

- 只从现有已下载 / 已 inspected 的科研 slide 资源中筛选 gold records；不得为了数量无界扩 corpus；
- 优先覆盖 motivation/research question、statistical model/estimator/theorem/proof intuition、method/experiment design、single-result/uncertainty/comparison/negative result/failure、medical-image aligned panels/overlay/error/zoom、discussion/next experiment；
- 每条记录必须绑定真实 source/page/render identity、scientific job、正文区域 composition、primary-object scale、reading order、annotation/legend/panel 关系与 rights/reuse boundary；
- 明确区分可抽象复用的 composition 与只能作为 comparative gold 的页面；
- 建立 production-adjacent 的只读检索 / 选择 / composition-recipe 输出路径，并保存 selected -> consumed -> output-affected trace；
- 保持 source/generated plugin mirror 与必要索引一致。

本任务不得：

- 扩大成新的外部 source scout 或大规模下载任务；
- 实现 Stage 3 的 CUHK LaTeX/TikZ scientific layouts；
- 修改 canonical CUHK template 视觉本体；
- 恢复 023 PPTX renderer；
- 运行最终 statistics / medical-imaging holdout；
- 修改 Terra core 或宣告 `ONE_SHOT_QUALITY_PASS`。

025 PASS 只表示 Stage 2 完成。之后 Planner 才能创建 Stage 3 — Executable CUHK Scientific Layout System。
