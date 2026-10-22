我会读取当前候选的 scientific-rewrite 技能及原生 helper，按输入包逐字节还原并校验文件，再执行指定验证；不改动文稿或阶段包。


机械复验通过：12 个文件逐字节还原，SHA-256 全部匹配；原生 helper 退出码为 `0`，stderr 为空。

已全文读取 `outputs/STAGE_RECEIPT.json`，候选文稿哈希仍为：
`9d89035bf311e04bf935ff89a50557cc81f7c6df6c5aa9bb65fb3f9ee835988e`

实际命令、helper 哈希、全部还原哈希及完整 stdout/stderr 已保存至 `outputs/VALIDATION.json`。文稿、阶段包和插件均未修改。