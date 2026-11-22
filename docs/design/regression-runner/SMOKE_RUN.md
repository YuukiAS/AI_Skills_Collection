# 集群模拟运行记录

本轮仅用假数据；剪贴板是文本文件，提问弹窗用标准输入代替。没有访问或控制浏览器，没有调用外部模型。判定输入也是固定假数据，只验证判定落盘与引句检查。

复现：`python3 tools/regression-runner/smoke_test.py`。仅替换该测试自己的 `tools/regression-runner/runs/synthetic-smoke/`，不碰真实运行目录。

```text
{"action": "ask", "case": "SYN-BRANCH", "turn": 2, "clipboard_written": true, "message": "案例 1/4：SYN-BRANCH；第 2/3 轮；接着上一轮。模型：模拟模型；插件：无需；附件：无需。提示词已在剪贴板。请粘贴发送，等完整回答后点击“复制”，再答 好了 / 跳过（余下本案例）/ 停。", "checkpoint": ""}
标准输入代替弹窗：{"action": "stopped", "message": "已保留断点；下次用同一批次继续"}
```

```text
{"action": "ask", "case": "SYN-BRANCH", "turn": 2, "clipboard_written": false, "message": "案例 1/4：SYN-BRANCH；第 2/3 轮；接着上一轮。模型：模拟模型；插件：无需；附件：无需。这是待完成轮次，未改动剪贴板；需要提示词时先重新复制。请粘贴发送，等完整回答后点击“复制”，再答 好了 / 跳过（余下本案例）/ 停。", "checkpoint": ""}
标准输入代替弹窗：模拟用户点击复制后的回答（单行）：{"action": "saved", "case": "SYN-BRANCH", "turn": 2, "checkpoint": ""}
{"action": "ask", "case": "SYN-BRANCH", "turn": 3, "clipboard_written": true, "message": "案例 1/4：SYN-BRANCH；第 3/3 轮；从第 1 轮回答后创建分支。模型：模拟模型；插件：无需；附件：无需。提示词已在剪贴板。请粘贴发送，等完整回答后点击“复制”，再答 好了 / 跳过（余下本案例）/ 停。", "checkpoint": ""}
标准输入代替弹窗：模拟用户点击复制后的回答（单行）：{"action": "saved", "case": "SYN-BRANCH", "turn": 3, "checkpoint": ""}
{"action": "judge", "case": "SYN-BRANCH", "directory": "tools/regression-runner/runs/synthetic-smoke/SYN-BRANCH"}
```

```text
{"action": "ask", "case": "SYN-FAIL", "turn": 1, "clipboard_written": true, "message": "案例 2/4：SYN-FAIL；第 1/1 轮；新对话。模型：模拟模型；插件：无需；附件：无需。提示词已在剪贴板。请粘贴发送，等完整回答后点击“复制”，再答 好了 / 跳过（余下本案例）/ 停。", "checkpoint": ""}
标准输入代替弹窗：模拟用户点击复制后的回答（单行）：{"action": "saved", "case": "SYN-FAIL", "turn": 1, "checkpoint": ""}
{"action": "judge", "case": "SYN-FAIL", "directory": "tools/regression-runner/runs/synthetic-smoke/SYN-FAIL"}
```

```text
{"action": "ask", "case": "SYN-UNKNOWN", "turn": 1, "clipboard_written": true, "message": "案例 3/4：SYN-UNKNOWN；第 1/1 轮；新对话。模型：模拟模型；插件：无需；附件：无需。提示词已在剪贴板。请粘贴发送，等完整回答后点击“复制”，再答 好了 / 跳过（余下本案例）/ 停。", "checkpoint": ""}
标准输入代替弹窗：模拟用户点击复制后的回答（单行）：{"action": "saved", "case": "SYN-UNKNOWN", "turn": 1, "checkpoint": ""}
{"action": "judge", "case": "SYN-UNKNOWN", "directory": "tools/regression-runner/runs/synthetic-smoke/SYN-UNKNOWN"}
```

```text
{"action": "ask", "case": "SYN-SKIP", "turn": 1, "clipboard_written": true, "message": "案例 4/4：SYN-SKIP；第 1/1 轮；新对话。模型：模拟模型；插件：无需；附件：无需。提示词已在剪贴板。请粘贴发送，等完整回答后点击“复制”，再答 好了 / 跳过（余下本案例）/ 停。", "checkpoint": ""}
标准输入代替弹窗：{"action": "skipped"}
{"action": "done", "message": "批次已处理；有缺口或跳过的案例仍为未完成"}
```

已通过 18 项检查：

- 多行提示词逐字进入模拟剪贴板和 prompt 文件
- 原样提示词被拒绝且只提醒一次
- 再次空剪贴板被拒绝并保留断点
- 续跑待完成轮次不会覆盖用户已复制的回答
- 标准输入“停”后不保存后续回答
- 标准输入续跑完成第 2、3 轮，并显示正确分支位置
- 已完成的第 1 轮回答保持原 hash
- 伪造依据句被拒绝，未产生判定文件
- 跳过余下本案例后结束批次
- 结果表分别保留通过、失败、无法判定、跳过
- 总计划 6 轮，实际保存 5 轮，跳过 1 轮
- 格式检查拒绝不存在或未来的分支轮次
- 格式检查拒绝缺少必填字段
- 冻结后输入变化拒绝混用旧运行
- 归档提示词漂移被拒绝
- 旧格式兼容导入但不会伪装成就绪：edge-revision
- 旧格式兼容导入但不会伪装成就绪：keychron-object-evidence
- 旧格式兼容导入但不会伪装成就绪：obsidian-existing-capability

假批次结果：[RESULTS.md](../../../tools/regression-runner/runs/synthetic-smoke/RESULTS.md)。

运行边界：Mac `pbcopy/pbpaste`、Windows PowerShell 系统剪贴板和 Codex 桌面提问弹窗均未在本机实测；真实迁移案例因缺口未执行。

迁移保真核对通过：3 份旧案例的原四字段、6 条判据，以及指令 R1 的 7 条非空提示词和 3 条判据均与原文一致；4 份来源文件 SHA-256 与迁移记录一致。另两轮因含账号标识留空。

`check_case.py` 检查全部 12 个案例格式无误（8 个迁移案例共 42 项缺口，4 个假案例无缺口）；新 skill 通过 skill-creator 的 `quick_validate.py`。
