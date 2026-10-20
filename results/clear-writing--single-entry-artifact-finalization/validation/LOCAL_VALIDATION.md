# 本地候选验证

实现提交：`079bd7987bb33d624d244feb415327d5cf2343d8`。
候选 ZIP SHA-256：`e4c451841583cb6e1ae4212f8d8559b93ef4272f66d687d3f6762f6114a73dc6`。

| 检查 | 实际结果 |
| --- | --- |
| wrapper 单测 | 18/18 PASS；包含 helper 路径、缺失支持、通配符、嵌套/引用式链接、尖括号链接/脚注、中断后重复请求防护与独立采集恢复 |
| writing runtime / Marketplace / scientific-rewrite / wrapper focused tests | PASS；初次 94 项为历史检查，最终 wrapper 18 项和全仓 370 项及 CI 覆盖同一修正提交 |
| full repository tests | 370/370 PASS，84.973 s；命令 `python -m unittest discover -s tests` |
| `python scripts/skills.py validate` | PASS；156 active skills，18 profiles |
| `python scripts/skills.py audit --all` | PASS；保留既有预算提示 |
| Marketplace write / validate / check / path-report | PASS；10 plugins，30 active skills，73 source snapshots，0 paths over budget |
| deterministic build + check | PASS；两个连续 raw ZIP 相同，完整 entry metadata 按 CW06_DETERMINISTIC_ZIP_V1 验证 |
| route inverse transform / support-file parity | PASS；仅两条 CW06_ROUTE_PROJECTION_V1 路径转换 |
| portable root manifest 官方 schema | PASS；使用 `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` 做 JSON Schema 校验 |
| packaged rewrite helper `--help` | PASS；helper 路径可在本地真实执行，不外推为 ChatGPT runtime 已可执行 |
| README installed Clear Writing 终审 | PASS；完整 README，原样放行；run `20261020T035904Z-57285652c495` |
| `git diff --check` | PASS |
| required GitHub CI | PASS；run `39368960081`，四个 job success，exact head 与上述实现提交一致 |

CI 的完整回读见 `GITHUB_CI.json`。README 完整语言审校见上级目录 `README_REVIEW.md`。
六项专业 Skill 正文与 `profiles/codex-writing-style.json` 相对任务起点没有变化。
Codex generated writing-style 仅版本字段随候选变为 0.6；普通六入口未折叠。

## 包装现实检查的本地部分

本地实际构建 29 文件、一个顶层 `skills/clear-writing/SKILL.md`，双 manifest 为 0.6.0，
OpenAI interface 一致且 capabilities 为 `["Interactive"]`。图标原字节复制。

已读取本机缓存 PIE 0.2.8 的 portable manifest 作为结构参考，但没有把缓存当作
当前账户 Plugin Creator 回读，也没有声称 `Interactive` 能导致正确路由。
官方包装说明：`https://developers.openai.com/plugins/build/plugins`。

完整 P0 的当前账户 metadata / release / file-list 由批准的 ChatGPT 阶段回读；
按用户本次明确指令，这个分工不阻塞 Codex 本地实施。
G1-G6 均未由这些机械检查或本地回放替代。

初次实现提交 `f86c4d0d3374a57cd27da1cee74f210c50e18150` 的 365 项测试及
CI `39367512348` 是历史验证，不冒充最新提交的 CI。最新提交的全仓测试与
四项 required CI 已独立重跑通过；中间 8a1b0a77 的 368 项测试与 CI `39368446270`
也保留为历史，不冒充最终提交证据。13 组有效回放不重跑挑选，完整输出及
相同 ZIP 字节身份的沿用边界见 `../known-regression/VERDICTS.md`。
