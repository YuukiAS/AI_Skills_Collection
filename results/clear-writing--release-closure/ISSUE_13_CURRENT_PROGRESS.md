问题：

让 Clear Writing（`writing-style`）成为可供各领域复用的表达层：改善普通解释、科研文档和图表文字的可读性，同时保留事实、公式、不确定性、精确机器字符串及各领域的专业判断。

当前进度：

Clear Writing 0.5 已正式发布，仓库版本为 5.5.1，且已整合回 main。现有 PRIVATE 插件已由 ChatGPT / Plugin Creator 更新为 0.5.0；用户确认已实际回读全部 27 个文件并逐文件比对，结果无漂移，唯一版本规范化为仓库 0.5 对应网页端 0.5.0。

#13 保持 open，生命周期为 `ADAPTING`，Area 为 `writing-style`。统计结果与科研图表的下游接入仍未完成，正式发布成功不代表本 Issue 的推广条件全部满足。

当前执行锚点：

- 正式发布：`fd79c4be54fc50bd66d9a51bbc1e681f361f6a77`（仓库 5.5.1 / `writing-style` 0.5）。
- main 整合：`57c5a2c8124752587688475b3ebc09c198d35186`；正式发布提交已是 main 的祖先。
- 维护条目：`docs/plugin-todos/writing-style.md`，``Promote `writing-style` into the generic content-preserving language layer``，`tracking: #13`。
- 批准执行包：`12a8ccd61778cca9a56df826072618cb06a81632`。

下一步：

- #73：`docs/plugin-todos/statistical-modeling.md` 中 `Delegate reader-facing wording without giving away statistical semantics`。由该领域任务完成真实统计分析的结果、图注与结论交接回放，确认统计含义没有漂移。
- #49：`docs/plugin-todos/scientific-visualization.md` 中 `Delegate captions/annotations without giving away visual semantics`。由该领域任务完成真实科研图的图注与标注交接回放，确认图形含义保持一致且表达更清楚。
- 完成这些接入后，逐项核对 #13 原有推广条件及持久证据，再判断能否关闭。当前不填写 Resolution commit，也不在本发布任务中实施下游插件修改。

正式发布不声称 Clear Writing 每轮必然加载，也不声称已证明严格匹配实验中的因果增益。历史 `W2=INCONCLUSIVE` 保留为诊断事实；它不是当前正式发布失败或待重跑项。
