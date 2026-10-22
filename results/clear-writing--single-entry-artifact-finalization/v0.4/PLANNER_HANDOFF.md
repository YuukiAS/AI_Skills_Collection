# 同任务回 Planner：保留模型配置的候选回放入口

task / branch / tracking 不变；唯一批准包为 `48c42f89d23ba168e2d2045034a7f7117c2e0448`。
本次没有改动产品承诺、职责、权限、Gate 成功定义或恢复语义，也没有新建任务。

## 已完成的有界实现

- response-clarity：先按用户问题和读者依赖选择内容，再生成完整回答，按原问题重新通读实际完整候选并实际返修。
- writing-fidelity 与 final-delivery reference：完整来源保真、受审候选身份、GitHub 修改/新建及本地交付、全文回读和实际保存文本质量。
- chinese-prose：全文中文终审及已审候选交接；scientific-rewrite 仅对接交付引用，保留全部 heavy stages/helper。
- ChatGPT wrapper：只识别对象、组合路线，调用唯一共享交付合同；Codex 六入口不变。
- prepare-restore：安全 ZIP/真 gzip tar reader、EOF/CRC/ISIZE 检查，legacy 27-file 集合和 0.6.1 恢复集合语义不变。

生成包是新的开发产物，不是 final candidate。版本仍为同一 0.6 候选，旧 079bd798 只属历史。
机械检查见 `validation/`，独立代码复核见 `review/IMPLEMENTATION_REVIEW.md`。

## 必须闭合的精确缺口

原实际回放 `20261020T040240Z-d4023c2f186e` 的日志证明模型为 `gpt-6.1-sol`、reasoning effort 为 `high`。
当前用户配置与之相同；模型身份不是未知，也没有请求换模型。

仓库 canonical `scripts/candidate_plugin_replay.py` 能安装 exact committed candidate 并解析真实 Skill 消费，
但 `run_child_exec` 固定传入 `--ignore-user-config`，CLI 不接受模型/effort 配置参数。
已安装 pinned CLI 0.153.4 的帮助明确该 flag 不加载 CODEX_HOME/config.toml；不能据当前用户配置声称 child 保留了原模型。

`ai-bridge plugin-replay` 保留当前用户配置，但只接受已安装身份和显式输入，未提供 exact candidate commit 安装入口。
把新 ZIP 当输入让旧插件阅读，只能产生源码消费证据，不能替代批准的 installed-candidate 六路线回放/G5。

请 Planner 为**既有候选回放入口保留已冻结模型配置**确定最小合法处理范围。
不得用默认模型跑一次再倒推通过，也不需要新模型、新服务、CODEX_HOME 或新架构。
本任务未擅改 candidate replay helper / Bridge，未 raw exec、monkeypatch 或复制凭据。
新候选模型请求数为 0，未消费正式 Web 任务或 G6。

## 恢复点

入口闭合后，继续同任务的受影响 known regressions 与 should-not-change，读取完整实际产物，
再完成 required CI/独立实施审查并冻结唯一新版 FINAL_CANDIDATE。
已有代码和本地机械验证保留，不重做架构。

之后仍需 Phase C 的真实 0.5 archive 字节、reader 验证、forward restore、helper 和 fresh Web/GitHub 能力前置。
当前没有 live update，无需 restore；不能因为本地 tar fixtures 通过就声称账户恢复链通过。
G1-G5 全部真实通过后交原 Critic，G6 不由本任务自行选择或运行。
0.6 未发布，Issue #13 仍 open/DOING，#73/#49 接入仍 pending。
