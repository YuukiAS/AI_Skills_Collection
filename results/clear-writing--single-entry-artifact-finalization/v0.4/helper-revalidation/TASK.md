这是同一 Clear Writing 开发回归的机械修复复验，不是新的文稿生成任务。

请实际读取当前已安装候选的 scientific-rewrite SKILL.md 及其 scripts/rewrite_support.py。
仅处理 inputs 中的 FIXED_STAGE_INPUT.json；不要访问网络、其他私有文件或旧插件，不修改任何插件。

该 JSON 保留原始完整来源、原问题、首次完整成稿与原始阶段包。请按 files 中的相对路径将原始 UTF-8 文本逐字节还原到 outputs/fixed-stage/，逐一校验 sha256。不要改写任何原文、文稿、Meaning Map、Reader Plan、realization、assembly 或 semantic audit。

然后使用本次 candidate installed path 下的原生 helper CLI，运行：

`python3 <installed-candidate>/skills/scientific-rewrite/scripts/rewrite_support.py validate-stage --source outputs/fixed-stage/source.md --prompt outputs/fixed-stage/prompt.md --stage-dir outputs/fixed-stage --receipt outputs/STAGE_RECEIPT.json`

保存实际命令、helper SHA-256、所有输入还原哈希、首次文稿 SHA-256、退出码及完整 stdout/stderr 至 outputs/VALIDATION.json。全文读取 STAGE_RECEIPT.json，确认候选文稿哈希仍为 `9d89035bf311e04bf935ff89a50557cc81f7c6df6c5aa9bb65fb3f9ee835988e`。如检查失败，保留原始失败，不修正文稿或包，不声称成功。

最后简洁报告实际验证结果；不要生成新的产品答案，不运行额外模型，不升级或移除正式插件。临候选清理由宿主回放器负责。
