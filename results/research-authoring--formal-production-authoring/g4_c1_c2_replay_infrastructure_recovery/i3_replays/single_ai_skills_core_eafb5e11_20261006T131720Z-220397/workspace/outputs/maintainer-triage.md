# 候选插件回放：维护分诊备忘录

该说明提出的要求是：证明子运行时实际使用了指定的预发布插件，并提供范围明确、可核对的路由回执。最可能的主责层是 **Bridge Kit 的 plugin replay 运行时与证据生成层**；AI Skills Maintainer 负责中央插件的维护验收与证据消费。本次仅作分诊，没有执行回放或验证该能力是否已实现。

依据是[输入说明](../inputs/01-single_ai_skills_core_input.md)唯一正文段，以及已安装的 [AI Skills Repository Maintainer](</users/a/e/aereinh/.codex/plugins/cache/ai-skills-candidate/ai-skills-core/0.5/skills/maint/SKILL.md>) 中的 “Production Consumption Diagnosis”、[Bridge Kit Maintainer](</users/a/e/aereinh/.codex/plugins/cache/ai-skills-candidate/ai-skills-core/0.5/skills/bridge/SKILL.md>) 中的 “Boundary”。后者明确将 plugin replay 运行时归于 Bridge Kit；其在 AI Skills Maintainer 内的维护入口不拥有 Bridge 运行时语义。

输入没有给出失败日志、候选版本、运行标识或已有回执。当前只能记录为待核实的基础设施证据需求，不能认定为已复现回归、缺失规则或能力缺口。工作区未提供中央 TODO、实现或测试，尚不能确认重复条目与已有覆盖情况。

建议维护者先检查既有回放路径，再要求同一次运行的回执至少能关联以下证据（这是验收建议，不是已核实的现行字段）：

- 指定候选的插件标识与可校验内容身份，以及本次回放和子运行时标识。
- 子运行时实际加载的插件路径、身份及其与指定候选的对应关系。
- 正常任务入口如何路由到目标技能，以及子运行时实际调用该能力的证据位置。

仅有安装成功、源码读取、生成物一致、命令退出成功或子运行时自述，均不足以证明实际消费。若证据不完整，应明确标为未证明，并按既有诊断分类区分 `not_loaded`、`stale_install`、`consumer_not_routed` 等原因；当前不能选定其中任何一种。

后续如需修复回执生成或运行时行为，应交由 Bridge Kit Planner/Critic 冻结范围；AI_Skills_Collection 只在需要时调整已有证据验收契约，不复制回放运行时、不新建产品技能。本次没有修改仓库源文件、TODO、看板、版本或发布状态，也没有发布或产品质量通过结论。
