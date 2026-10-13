# Clear Writing — CW-CI-01 跨负责人基线恢复：独立 Critic 定向审查

- 角色：本 ChatGPT 独立 Critic；只审恢复边界，不冒充 Planner、Executor 或正式产品 Reviewer。
- 审查日期：2026-10-13
- 仓库：`YuukiAS/AI_Skills_Collection`
- 执行分支：`reviewed/clear-writing--cross-surface-language-layer`
- 精确审查对象：`88412b3bb08aafb00ee17afbd43c2fdd7a79bdd7`
- 提案：`results/clear-writing--cross-surface-language-layer/PLANNER_CI_RECOVERY_DECISION_2026-10-13.md`
- 原冻结实施：`automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/PLAN.md`
- 第一轮审查：`results/clear-writing--cross-surface-language-layer/REVIEW_1.md`
- 失败运行：`https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/38260835399`
- 当前已核实：`NEEDS_GPT_PLANNER`；`review_round=1`、`plan_revision=0`、`ci_status=FAIL`；实现提交仍为 `cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`。
- 定向结论：**PASS — 仅批准跨负责人基线恢复的治理与验收边界；不是批准改动冻结插件、不是 CI PASS、不是新的产品方案。**
- 新阻断：无（针对所审恢复判断本身）；已存在的 `CW-CI-01` 仍未实质关闭。
- 不修改 `CURRENT.json`，不消耗第二轮 Reviewer 或现有一次 Plan revision，不自行执行付费操作或仓库修复。

## 核验和归因

CI 测试 341 项、失败 5 项；安装及 Windows 长路径作业成功，完整 Marketplace CI 未通过。五项属于四类已有基线不一致：

1. 仓库 `VERSION=5.4.4`，`tests/test_central_plugin_icon_assets.py` 旧断言却要求 `5.5.0`；绝不能通过随意升级正式版本满足硬编码。
2. `tests/test_codex_marketplace.py` 两项断言把流程专属 `docs/plugin-todos/*.md` 错误纳入中央插件唯一清单；不得删除合法 TODO 迎合测试。
3. 生成层检查报告其他插件 `presentations` 和 `research-writing` 合计 16 处差异；目前仅有 CI 失败与执行端生成差异证据，没有最终权威内容取舍，不得不看差异就运行全量生成并提交。
4. Presentations 技能源与打包镜像内容不同；这是原有内容一致性缺口，不属于此次 `response-clarity` 源码修改。

旧失败不证明 Clear Writing 产品质量已通过，也不证明最新 `main` 已有修复。官方 GitHub 文档指出重跑既有 workflow 使用原触发事件的相同提交，故未经修复重复运行 `38260835399` 不能作为新候选修复证据。

## 批准的最小恢复路线与真实权限

**批准作为下一步的方案原则：** 原 Planner 可沿用同一任务、同一分支与原冻结能力门槛，协调已有正式维护负责人处理已有全仓基线；经其正式授权和有效回归的修复先进入相应合法源分支／主线，再由本任务合法消费。只要恢复的是同一全仓 CI 的既有正确性，而不改变 Clear Writing 的产品语义、完整 CI 门槛、账号／费用／数据／版本边界，就**不需要重新设计架构或重复提交本议题给 Critic**。

职责和最小关闭条件：

- `ai-skills-core`／仓库维护：更新版本断言，使其检验当时有效的正式版本策略，而不是固定一个不存在的未来版本；修正中央插件待办清单范围，同时保留流程专属文件。测试仍必须能检测真正的插件清单／发行配置错误。
- Presentations 负责人：比较真实源与既有打包镜像，决定保留哪种有证据的正式能力；只按其领域批准的范围同步，验证旧功能不退化，不进行内容覆盖式“修绿”。
- Research Authoring 负责人：**此 Clear Writing 任务不准修改 Research Authoring 的任何源码、打包载荷或账户插件**。如独立正常维护确实需要修改受冻结内容，必须得到该领域现行范围内的真实用户授权；这份 Critic PASS 不能替代该授权，也不能把冻结解除默认为已批准。
- 构建与维护负责人：修复后的全层生成必须从真实正常入口符合来源／载荷一致性；不能通过删除测试、标记失败为允许、隐藏 diff、条件跳过、篡改历史报告、按失败样例硬编码来达成。
- 当前 Clear Writing Planner：在跨域修复出现且核实精确提交、owner 权限、源码／载荷保真后，合规引入本任务，**保留原 G0–G7、原始全仓 CI、第一轮审查**。如果原 `PLAN.md` 不需要变更，则无需机械消耗一次 Plan revision；原任务状态合法恢复执行须按 Bridge 状态合同处理。若需要修改冻结 Plan 的实际范围／验收标准，再进行最小修订与对应有效授权。

**当前不批准：** 在 `reviewed/clear-writing--cross-surface-language-layer` 内直接跨域改 Research Authoring/Presentations 正式源或载荷；将全仓 CI 降为仅 `writing-style` 测试；将 `CURRENT.ci_status` 假写为 PASS；取消审查；更改当前正式版本；创建替代任务或 watcher。

如果各负责人无法在保持 Research Authoring 冻结的条件下修复全部基线，则应该把**唯一确切的不可替代权限选择**交给用户决定（例如是否另行批准被冻领域的范围极窄的生成一致性修复）；不能以本批复假称已授权。此处尚无证据允许声称无需新的领域授权就一定可以修复完毕。

## 何时真正解除 CW-CI-01

必须有当前 Clear Writing reviewed 分支上的同一候选（含经授权消费的基线修复）从正式入口重新跑出必需 CI 全部通过。不能靠主线不同候选 PASS、旧局部回放、单独缩窄测试或复跑原失败提交拼成成功。完整 CI 通过后仍需实际 ChatGPT 私有技能安装、A/E 和 B/C 的匹配自动调用对照、专业消费者的完整产物、独立定性审查和用户验收，才可能宣布产品完成。

```text
REVIEW_STAGE=TARGETED_CI_RECOVERY_BOUNDARY
REVIEWED_COMMIT=88412b3bb08aafb00ee17afbd43c2fdd7a79bdd7
FINDING=CW-CI-01
RECOVERY_BOUNDARY_DECISION=PASS
CW-CI-01_ACTUAL_CLOSURE=OPEN
AUTHORIZED_CROSS_OWNER_SOURCE_MUTATION=NO
CLEAR_WRITING_FULL_CI=FAIL
KEEP_CURRENT_STATE=NEEDS_GPT_PLANNER
KEEP_REVIEW_ROUND=1
KEEP_PLAN_REVISION=0
NEXT_HANDOFF=PLANNER_EXISTING_TASK
```
