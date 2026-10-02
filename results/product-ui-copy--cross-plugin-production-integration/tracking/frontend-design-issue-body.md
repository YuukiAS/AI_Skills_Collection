问题：
Frontend Design 在改具体措辞之前，需要先判断页面里哪些文字确实该出现、各自承担什么 UI 角色，以及它们是否和邻近模块重复表达同一个产品状态。实际生产审计显示，即使单句文案本身通顺，如果整页结构重复、普通状态被写成口号，或把内部产品/法律状态直接暴露给用户，界面仍会像由说明稿逐块拼起来，而不是成熟的产品界面。

当前进度：
已在 `reviewed/product-ui-copy--cross-plugin-production-integration` 分支完成 Product UI Copy 的候选实现与 H4 fresh holdout；本 Issue 用于替换原本误绑定到 `#73` 的 Frontend Design tracking locator。

当前执行锚点：
任务：`product-ui-copy--cross-plugin-production-integration`
分支：`reviewed/product-ui-copy--cross-plugin-production-integration`
候选提交：`a06ff050bc82bb22358dfcb3e4faa885fddd285b`
来源条目：`docs/plugin-todos/web-development.md` 的 “Product UI copy needs an explicit Frontend Design content-architecture contract”

下一步：
保持该条目在 AI Skills Maintenance Project 中处于 `DOING`，等待当前 reviewed handoff 完成 Reviewer 复核、CI 和最终接收后，再按真实 closure 更新进度；不要复用或关闭 `#73`。
