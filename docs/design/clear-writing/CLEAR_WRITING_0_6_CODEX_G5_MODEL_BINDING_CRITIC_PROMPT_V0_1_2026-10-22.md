# Clear Writing 0.6：Codex G5 候选回放模型绑定最小 execution-ready 复核

你继续担任该 Clear Writing 0.6 原任务的**独立 Critic**。这次只处理同一已批准执行包中 Codex 候选回放模型绑定与当前真实CLI认证入口不兼容的问题；不得重做Clear Writing产品、正式Web Gate、恢复机制或新增任务。

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = writing-style / Clear Writing
task_key = clear-writing--single-entry-artifact-finalization
branch = design/clear-writing--single-entry-artifact-finalization
tracking = #13
review_stage = CODEX_G5_MODEL_BINDING_AMENDMENT_EXECUTION_READY
original_approved_package = 48c42f89d23ba168e2d2045034a7f7117c2e0448
implemented_writing_source = 0b4248c7eb2abd4b03a06c97061aa895a556a0e7
observed_pre_amendment_branch = 2f35ce839a42f81f39cff55f577f44a10206e5a7
```

本轮 `PACKAGE_COMMIT` 由用户转交消息明确提供，必须对该 **exact commit** 审查，不从后续mutable HEAD猜候选。

先读取最新main的`AGENTS.md`、`docs/workflows/PLANNER_ROLE_CONTRACT.md`、`docs/workflows/CRITIC_ROLE_CONTRACT.md`、`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`、`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`。从提交读取当前四份v0.4执行合同：

- `docs/design/clear-writing/CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md`
- `docs/goals/CLEAR_WRITING_0_6_UNIFIED_DELIVERY_GOAL_V0_4_2026-10-22.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_RUNBOOK_V0_4_2026-10-22.md`
- `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_4_2026-10-22.md`

再读取原任务源证据（包括已知新旧时间差）：

- `results/clear-writing--single-entry-artifact-finalization/v0.4/RESULT.md`
- `results/clear-writing--single-entry-artifact-finalization/v0.4/PLANNER_HANDOFF.md`
- `results/clear-writing--single-entry-artifact-finalization/v0.4/validation/CODEX_RUNTIME_PREFLIGHT.json`
- `results/clear-writing--single-entry-artifact-finalization/v0.4/review/IMPLEMENTATION_REVIEW.md`
- `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md`
- `scripts/candidate_plugin_replay.py` 的实际当前实现及最近修正、必要测试；
- Issue #13及此前implementation-review与CI身份。

## 核心审查：只重判新增G5模型身份合同及受影响接口

1. **原历史模型是否真有永久约束依据？** 历史一次 `gpt-6.1-sol/high` 不能代替候选质量与真实账户许可；用户提供的服务端HTTP 400无产品答案，是认证/模型适配基础设施问题，不是Clear Writing产物质量失败。模型请求本身成功传参与实际被服务端接受必须分开。
2. **现有已批准主张没有降低？** Web G1/G2/G3型号仍是`GPT-5.6 Sol`，独立网页正常入口照原样跑。Codex G5仍必须真实安装exact committed candidate，正常加载六条canonical writing入口，获得完整ordinary reply、必要长答、正式文档/聊天及精确机器内容产物，并由真正独立审阅者看完，保持原G5其它标准。
3. **Codex候选回放可执行身份是否足够冻结？** 在首个正式G5产品任务之前，同一repo-local固定CLI、`candidate_plugin_replay.py`、原ChatGPT CLI认证/隔离配置确认当前实际可用的模型及推理强度（模型目录/CLI --model参数不足，必要时要有真正被同路径服务端接受的凭证）；记录model/effort/CLI version/auth surface/候选身份，整个G5批次一致。产品回答产生后绝不换模型挑赢家；服务端无产品输出的基础设施失败依原有界恢复与预算处理，不能隐性多跑费用或无限试模型。若无当前真实可用配置则停止，不以源码阅读或旧插件替代。
4. **实现更改范围是否充分且最小？** 当前`2f35ce8...`已实现模型参数向候选子进程的通用透传并保留`--ignore-user-config`。如果正常入口还需要小型通用参数/可用性探针修复，必须限制在同一helper和相应直接测试，不改auth、CODEX_HOME、产品源码、Bridge、Marketplace、生成器、其它插件，也不改变账户权限。
5. **这次是否是执行合同局部修正？** 对照原v0.4 Plan/Goal/Runbook/Kickoff与当前修改，判断没有留下“必须永远复用历史模型”的冲突，也没有改变写作架构、G1–G6、G6 fresh、forward restore、版本/用户授权。不能把新模型身份当作自由调参或回归期间选择。
6. **审查完成出口**：如果确定上述要求让Codex无需猜测模型或验收/费用语义即可合法继续原任务，可以针对这次最小修订给`DECISION=PASS / READY_FOR_CODEX=YES`；若仍有具体执行/权限/预算或模型解析无法闭合，应`DECISION=REVISE / READY_FOR_CODEX=NO`，稳定编号`CW06-G5M-xx`，列最小可执行关闭条件。此前已冻结且未改变的产品架构不重审。

本轮只读，不修改任何仓库/Issue/Project，不运行候选回放/付费调用，不更换模型、不更新Personal Plugin、不运行正式Web Gate。

按最新角色合同先用一屏自然中文说明本次结果和风险，再给结论；PASS后直接生成绑定用户所给 exact PACKAGE_COMMIT 的简短中文同任务Codex续跑提示词；REVISE给原Planner单一完整最小返修提示词。不得把用户交接拆成待填字段。