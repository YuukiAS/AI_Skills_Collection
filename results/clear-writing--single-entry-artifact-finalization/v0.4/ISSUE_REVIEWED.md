问题：

Clear Writing 0.6 要让 ChatGPT 和 Codex 使用同一套写作规则：先围绕用户的问题组织必要内容，生成全文后重新通读并实际返修；需要保存的文档必须单独完成全文处理、写入和回读，不能用清楚的聊天说明代替。

当前进度：

用户已批准同一任务的 v0.4 执行包 `48c42f89d23ba168e2d2045034a7f7117c2e0448`。共享源文、ChatGPT 单入口、Codex 生成物，以及用于安全恢复 ZIP/tar.gz 的读取器，都已在原分支实现。本地 389 项单测通过，完整 CI 结果见当前证据目录。六条入口均未删除、合并或改名；英文科研和界面文案没有新增专业语义，其他插件未修改。

新版的已知回归和保护性对照尚未运行，不能沿用旧 13 组 PASS。旧候选 `079bd7987bb33d624d244feb415327d5cf2343d8` 仅作为历史记录保留，已明确标记为不可发布；新版 FINAL_CANDIDATE 尚未冻结。

当前执行锚点：

- task：`clear-writing--single-entry-artifact-finalization`。
- branch：`design/clear-writing--single-entry-artifact-finalization`。
- 实现提交：`0b4248c7eb2abd4b03a06c97061aa895a556a0e7`。
- Plan：`docs/design/clear-writing/CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md`。
- 证据：`results/clear-writing--single-entry-artifact-finalization/v0.4/`。
- 精确交接：`results/clear-writing--single-entry-artifact-finalization/v0.4/PLANNER_HANDOFF.md`。

下一步：

下一步由原 Planner 解决候选回放入口无法保留既定 `gpt-6.1-sol/high` 配置的问题。原模型身份已通过实际日志核实，但现有候选入口固定忽略用户配置，也没有模型配置的传参入口，调用时未显式传入模型配置；另一个 Bridge 回放入口也不能证明安装的是精确对应的候选版本。当前没有发送新的候选模型请求，不更换默认模型，也不把读取候选源码计作 G5。

入口问题解决后，在同一任务中继续开展实际回归、完整产物审查，并冻结最终候选。更新任何个人插件之前，仍须取得真实账户的 0.5 archive 字节、验证恢复包，并确认 helper 与 fresh Web/GitHub 路径可执行。当前尚未更新个人插件（无 live update），正式 G1-G6 均未运行，G6 未选择，0.6 未发布。

Issue #13 保持 open，生命周期为 `DOING`，Area 为 `writing-style`，Resolution commit 留空。#73 与 #49 的下游接入仍未完成（pending）；本任务不修改这些插件，0.6 成功也不会自动关闭 #13。该入口缺口不代表 Clear Writing 产品 FAIL，也不意味着因 Plugin Creator 缺席而在本地停工。
