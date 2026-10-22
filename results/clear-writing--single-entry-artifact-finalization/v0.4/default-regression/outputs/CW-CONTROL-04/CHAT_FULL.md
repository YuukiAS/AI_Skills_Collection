我会使用 Clear Writing，先读取指定的任务和来源，再按原问题说明当前状态与下一步。


根据输入记录，Clear Writing 目前还在等待 CI，尚无通过结果：工作流状态为 `WAITING_FOR_CI`，CI 状态为 `PENDING`。Clear Writing 位于 `writing-style` 插件中，当前候选提交为 `245d2f3f819c3dc333ee0dc6474832bf5e1ef6f1`。

下一步，执行者应运行 `python scripts/build_codex_marketplace.py --validate --check`，并核对 `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/CURRENT.json`。