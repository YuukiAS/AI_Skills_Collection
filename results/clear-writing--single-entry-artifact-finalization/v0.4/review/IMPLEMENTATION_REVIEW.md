# 独立实施审查与执行入口诊断

批准包：`48c42f89d23ba168e2d2045034a7f7117c2e0448`。
独立只读审查者：Epicurus，agent `01a161e2-8115-7d40-8288-b603e848128b`。
早期检查针对未提交实现，最终代码复核已绑定 `0b4248c7eb2abd4b03a06c97061aa895a556a0e7`。
CI 身份另见验证回执，不虚构已完成正式产品审查。

## 代码发现与处置

早期发现一项 P2：tar 遍历结束未必读取 gzip 到 EOF，损坏 CRC/ISIZE 或缺失 trailer 的备份会被接受。
修复使用标准库 `gzip.open`，完成 tar 安全遍历后分块读取 gzip 至 EOF。
新增缺 trailer、坏 CRC、坏 ISIZE 测试，均覆盖 tar.gz/tgz；修复前复现、修复后拒绝。

审查者复核原文：

> gzip P2 可关闭，绑定当前未提交实现。已复核 reader 修复：使用 gzip.open 并读取至 EOF，使尾部校验真正执行。独立运行 37/37 PASS（31 wrapper + 6 contract）；缺 trailer、错误 CRC/ISIZE 在 tar.gz、tgz 下均被拒绝，安全目录兼容及 restore 集合回归通过。此次复核无新增 finding。

职责唯一、完整候选两阶段实际返修、重路线不降级、本地/GitHub交付真实性、新文件非覆盖创建及非事务锁边界，
审查者在本次源文合同检查中未发现其他实质遗漏。
这些是代码/合同证据，不是模型输出质量或真实 Web Gate PASS。

最终提交复核原文：

> 已绑定最终代码提交 0b4248c7eb2abd4b03a06c97061aa895a556a0e7：代码范围内无 remaining finding，gzip P2 已关闭。
> 四项 canonical source 及新增 final-delivery 与 Codex 生成文件逐字节一致。
> 三处旧短语断言已按批准的新职责更新，未见删除测试或弱化语义；补跑 text audit 9/9 PASS。
> 重新计算 ZIP：978b93115a0f66aab6f7a4cce2f590118ce2f0804d7113b02c3626c3b88cfc00，共 30 files。
> 整体 implementation acceptance 仍 pending：新版 known-regression / should-not-change 回放入口尚未闭合。

审查者查询 CI 时仍在运行；Executor 随后实际回读其四项 success，独立保存在 `../validation/GITHUB_CI.json`，
不把后取得的 CI 结果改写成审查者先前已经观察到的结果。

## 回放入口缺口

审查者只读结论：

> candidate helper 仍固定 --ignore-user-config，CLI 没有模型配置传递入口，无法绑定原 gpt-6.1-sol/high。
> 既有 Bridge replay 可继承用户配置，但没有安装、绑定 exact candidate commit 的入口；候选作为输入读取不能冒充 G5。
> 在不改 helper/Bridge、不切换 CODEX_HOME、不 raw exec/monkeypatch 的约束下，没有已验证的现成合法入口。G5 回放仍未执行，不是产品 FAIL，也不是 regression PASS；最终候选冻结仍需等待该缺口闭合。

本次未编辑文件、发起模型请求或操作账户。
整体 implementation acceptance 尚未完成：缺少新语义的已知回归与保护性对照实际产物。
旧 079bd798 的 13 份 PASS 不沿用为本轮 PASS，不冻结 FINAL_CANDIDATE，不进入 Phase C mutation。
