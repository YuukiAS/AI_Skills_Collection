---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: clear-writing--cross-surface-language-layer
review_round: 1
decision: REVISE
implementation_commit: cac70c3bfcce6aeeba9c3e80adfa317235b54ee9
---

# Clear Writing：第一轮独立审查（CI 失败归因）

## Decision

**REVISE：必需的全仓 CI 未通过。本次决定只裁定 CI 门槛，尚未裁定新增 `response-clarity` 的真实产品质量。**

- 角色：本任务的人工独立 GPT Reviewer；不是 Planner，也不代 Executor 修改代码。
- 冻结任务：`clear-writing--cross-surface-language-layer`。
- 合同：该任务 `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/PLAN.md` 的 `## Acceptance and regression gates` 与 `ci_required=true`。
- 基线：`34e47fe6d0dc06d57ee1e6e37c0ff0f2fdfefc1b`。
- 当前实现：`cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`。
- CI 被测远端分支提交：`64d9efdf0c2f1cf15485bade34d085c694d2e62a`，它包含当前实现和 `WAITING_FOR_CI` 控制状态；不能要求它与 `implementation_commit` 相同。
- 真实 CI：https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/38260835399
- CI 结果：`failure`；`codex-marketplace` 的全仓 `unittest` 共 341 项，5 项失败；Linux/Windows 安装检查和 Windows 长路径检查通过。之后的生成、校验和生成文件洁净检查因前置测试失败而被跳过，不得说整条流水线已通过。
- `PROCESS_PASS=NO`（要求的 CI 未通过）；`PRODUCT_ARTIFACT_PASS=NOT_ASSESSED`（不能用局部测试和单次回复推断产品验收）。

## Blocking findings

### CW-CI-01：既有全仓基线差异阻断本任务的必需 CI

**依据：** 冻结 PLAN 的 `ci_required=true`、真实产物与回归门槛，以及明确禁止本任务修改 Research Authoring、Presentations、仓库通用生成机制和未经批准的正式版本。

**直接证据：** 上述失败 CI 的 `codex-marketplace` 作业 `114850626740` 提供五项失败：

1. `test_marketplace_keeps_canonical_icon_paths_and_versions`：`tests/test_central_plugin_icon_assets.py:49` 写死要求仓库 `VERSION=5.5.0`，实际 `VERSION=5.4.4`。测试文件与 `VERSION` 在基线和实现提交的 blob 身份相同，此矛盾不是本轮新技能写入造成；不得为了断言擅自将正式版号升到 `5.5.0`。
2. `test_central_plugins_have_exactly_one_source_only_todo_inbox` 与 `test_plugin_changelogs_match_marketplace_set_and_versions`：`tests/test_codex_marketplace.py:158,355` 将 `docs/plugin-todos/` 下所有 Markdown 文件名强制与十个中央插件名相等；日志列出七份工作流程相关待办。相关断言在 `main` 和实施提交均存在，至少两份触发文件已直接确认在基线存在。不能为通过测试删除有效 TODO、修改维护看板事实或改研究插件。
3. `test_generated_layer_matches_source_config`：`tests/test_codex_marketplace.py:473` 报 `publication layer is not current (16 differences)`。Executor 的生成层证据定位这些差异在 `presentations`、`research-writing` 的已生成载荷；本次提交仅改变 `writing-style` 的源及生成载荷，构建器本身未改。未在 `main` 上独立重跑全量生成，因此应把差异归为**强证据支持的既有生成层漂移**，而非冒充已经做过基线 CI 实测。
4. `test_research_presentation_todo_consolidation_and_promotions`：`tests/test_presentations.py:2669` 的源技能/已生成镜像逐字比较失败；测试和演示文稿正式源在基线与当前实现之间 blob 完全相同。此镜像差异须由 Presentations 所属正式维护流程辨明权威，不能在 Clear Writing 分支直接覆盖。

**因果与风险：** 全仓 CI 确实不满足冻结门槛。无论新技能局部测试是否通过，都不能从失败流水线跳转为审查通过；另一方面，让本任务 Executor 直接改变仓库版本、七份待办、研究写作或演示文稿生成载荷，将越过独立审查通过的实施边界，也可能破坏已有正式能力。

**最小关闭条件和责任：**

- Executor 保留当前 Clear Writing 产物和实现，不得为“修绿”修改上述跨范围对象、假造 PASS、选择性排除测试或反复触发相同 CI。
- 在 `REVISE` 事件上仅做必要的无副作用证据核对。若没有**经冻结 PLAN 已授权且实际有效**的同范围修复，按已有 Reviewed Handoff 路线转为 `NEEDS_GPT_PLANNER`，写明此 `CW-CI-01` 和真实 CI 定位，不新增任务链或自行扩大权限。
- 原 Planner 须先核对其他合法维护分支是否已有相关基线修复，选择不改本任务生产范围的最小恢复方式；跨插件/通用生成层真实修复交对应维护权威与必要审查，不能冒充 Clear Writing 的技术缺陷。Plan、权限或 CI 验收口径若需实质变更，按现有 Planner–Critic/用户授权边界处理。
- 关闭时必须有**当前 reviewed 分支、合法候选身份的完整必需 CI 真正通过**的直接证据，且上述五项不再失败；不能用主线另一候选的 PASS 拼接。随后才进入独立完整产物/插件双端实测审查；如实现候选有实质更改，要重新提供其对应回归证据。

## Non-blocking notes

- 已直接读取当前冻结 PLAN、`RESULT.md`、新增 `response-clarity/SKILL.md`、ChatGPT 私有候选清单和 Codex 的真实回放答复。已有源级增加和 `writing-style` 候选加载记录；局部回放不证明普通 ChatGPT 首答增量，也不证明最终版实际选择了具体技能或达到 G0–G7。此处不把尚未轮到的 Web 创建、A/E、B/C、整套幻灯片、完整文本定性审查或最终未见样本当作额外第一轮缺陷。
- `writing-style` 暂留 `0.4` 是冻结执行包允许的研发阶段状态；只有可发布、已验收的 `0.5` 候选才能触发版本及变更日志收口。不要把 CI 的 `5.5.0` 断言误当成版本升级授权。
- 本次记录第一轮 `REVISE` 应按 Review 现行状态合同推进 `CURRENT.ci_status=FAIL`、`review_round=1`、`state=REVISE`、`next_action=RUN_CODEX_REPAIR`；这是失败归因和恢复事件，不代表授权本插件 Executor 处理外部产品。Review 第 2 轮预算有限，不得在基线未变化时反复消耗。
- 若修复必须回到 Planner，外部角色正常接手和等待不属于任务失败。尚不能宣布 Clear Writing 0.5 完成、正式发布或 Issue #13 关闭。
