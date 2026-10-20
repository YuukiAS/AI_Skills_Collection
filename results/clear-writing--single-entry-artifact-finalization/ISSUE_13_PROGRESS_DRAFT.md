问题：

Clear Writing 的个人插件需要一个总入口，识别同一请求中的聊天说明和完整文档，并分别完成写作处理与验收。GitHub 文档只有在全文读取、完整终审候选、写入和回读逐字一致后，才能声称已完成。

当前进度：

0.6 执行包已获用户批准，本地候选已实现并推送。全仓 370 项测试、required GitHub CI 的四个 job，以及 9 组已知回归和 4 组保护性对照均已通过。独立实现审查的实际结论见证据目录中的 `review/IMPLEMENTATION_REVIEW.md`。六项专业 Skill 的源正文、profile 和 Codex 六入口保持不变。

本轮生命周期为 `DOING`，Area 为 `writing-style`，Issue #13 保持 open，Resolution commit 留空。正式发布仍是 `writing-style 0.5` / 仓库 5.5.1；0.6 尚未发布，Personal Plugin 尚未由本轮更新，G1-G6 尚未运行。

当前执行锚点：

- 任务：`clear-writing--single-entry-artifact-finalization`。
- 分支：`design/clear-writing--single-entry-artifact-finalization`。
- 批准执行包：`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`。
- 实现候选：`079bd7987bb33d624d244feb415327d5cf2343d8`。
- CI：`https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/39368960081`。
- 证据目录：`results/clear-writing--single-entry-artifact-finalization/`。

下一步：

由批准包指定的 ChatGPT 阶段读取候选与完整证据，完成账户只读回读、恢复包准备、现有 PRIVATE 插件更新和 G1-G6。候选文件可从证据目录的 `transport/MANIFEST.json` 与有序纯文本分片重建，不需要手工上传 ZIP。G3 必须实际取得 GitHub 最终全文，不能以聊天说明或本地回放替代。只有全部 required Gate 和最终完整产物审查通过后，才执行正式 0.6 发布收口。

本地回放只证明开发阶段的已知回归，不证明 ChatGPT 账户上的插件已更新或真实 Web Gate 已通过；缺少 Codex Plugin Creator 工具不再作为本地实施 blocker。

原有下游接入仍未完成：#73 对应 `docs/plugin-todos/statistical-modeling.md` 中 `Delegate reader-facing wording without giving away statistical semantics`；#49 对应 `docs/plugin-todos/scientific-visualization.md` 中 `Delegate captions/annotations without giving away visual semantics`。本轮不实施这些接入，0.6 成功也不自动关闭 #13。
