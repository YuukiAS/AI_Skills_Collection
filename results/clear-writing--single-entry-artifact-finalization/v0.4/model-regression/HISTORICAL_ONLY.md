# 历史模型配置诊断，不是本轮候选验收

本目录原始输入保留不变，供同任务默认入口按既有集合复用。
原 `INPUT_MANIFEST.json` 和 `RUNS.json` 只记录强制历史配置的诊断：
一次安装前只读失败，以及一次配置绑定成功但服务端 HTTP 400 的请求，没有产品答案。
不得执行原强制配置脚本、再次请求该配置，或把这些记录冒充本轮产品结果。

用户当前决定见 `../DEFAULT_ENTRY_AUTHORITY.md`。
有效候选回放、完整输出及审阅只认 `../default-regression/` 与
`../run_default_regressions.py` 的默认入口，无模型参数。
