# 维护分诊备忘录

这条说明应交给候选插件回放基础设施的维护者：需要证明子运行时实际使用了待发布插件，并给出限定范围的路由回执。当前只能确认这项证据要求，不能据此宣布故障已复现、修复完成或产品发布。

- **来源事实：** [维护说明](../inputs/01-single_ai_skills_core_input.md) 第 3 行明确指出基础设施归属、中央 AI_Skills 发布前回放场景，以及所需的 bounded route receipt。材料未提供具体插件身份、候选提交、运行日志或回执。
- **可能的负责层：** Bridge Kit 的 plugin replay 运行时及其候选加载／路由证据层。已安装的 AI Skills Maintainer 中，`bridge-kit-maintainer` 的 Boundary 明确将 plugin replay runtime 与运行时源码修改归 Bridge Kit；AI Skills Maintainer 负责中央维护分诊和回放证据要求。具体 helper 的源码位置尚未核实，不能仅凭名称指定实现文件。
- **初步分类：** 回放过程与实际加载证据问题，不是领域插件产物质量问题。`ai-skills-repository-maintainer` 的 Production Consumption Diagnosis 已要求核查安装身份、实际加载、触发路由和回放真实性；因此应先检查这些既有要求是否被实现与消费。现有材料不足以区分 `not_loaded`、`stale_install`、`consumer_not_routed` 或 `capability_gap`，也不足以判定重复条目或升级维护状态。
- **建议下一步：** 由基础设施负责人定位现有 helper、相关维护条目和候选回放合同，再做一次范围固定的诊断。建议回执关联候选插件 ID、版本及不可变内容身份、调用入口、子运行时／会话身份，以及该子运行时实际加载对应候选的证据和结果定位。上述是待负责人核对的证据清单，不是新建协议或声称已有回执；仅有安装成功、源码阅读、静态字符串检查或生成层一致性不能证明实际消费。
- **本轮边界：** 仅完成说明分诊，未执行回放，未改仓库源码、TODO、版本、发布引用或外部看板。工作区未提供中央 TODO、维护看板政策及候选回放合同，故未核验去重与跟踪状态；本备忘录不替代正式登记、运行回执或发布验收。

规则依据：本会话已安装的 `ai-skills-core/0.5/skills/maint/SKILL.md`（Production Consumption Diagnosis）与 `ai-skills-core/0.5/skills/bridge/SKILL.md`（Boundary）。这些规则支持责任划分，不构成本次子运行时已加载候选插件的证据。
