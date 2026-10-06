# 候选插件回放：维护分诊备忘录

当前应交给回放基础设施负责人核查“子运行时实际加载了哪个候选插件”，交付目标是范围明确、可核对的路由凭据。输入说明提出了这一要求，但没有提供失败日志、候选版本或子运行时记录，因此本次只能确定排查方向，不能认定根因或宣告修复完成。[1]

**责任层。** 最可能涉及 Bridge Kit 的插件回放运行时，以及 AI_Skills 候选回放入口与它的衔接。AI Skills Maintainer 负责检查候选来源、生成内容与实际消费证据是否一致；Bridge Kit 保有回放运行时的实现权。若需要改变 Bridge 运行时行为，应交回 Planner/Critic 冻结范围后由该 owner 实现，不在 AI_Skills 中复制一套回放器。[2][3] 目前未读取 helper 源码，尚不能确定具体文件归属。

**分诊结论。** 这是过程控制与证据验证问题；说明没有报告领域产物质量失败。建议按现有生产消费诊断路径调查，暂不新增同义规则或顶级 skill。先核对安装身份与版本、source/generated/Marketplace 一致性，再查正常入口是否加载候选、技能路由与会话上下文是否正确、回放是否忠实。现有材料不足以在 `not_loaded`、`stale_install`、`consumer_not_routed`、`unfaithful_test` 或 `capability_gap` 等原因中定案。[2]

**建议的最小路由凭据（待负责人确认）。** 将一次回放绑定到候选插件标识、来源提交或内容哈希、解析后的加载路径，以及子运行时或会话标识；记录预期技能路由及子运行时侧实际消费该候选的证据，并附可复核日志位置。父进程的启动参数、源文件读取记录或静态一致性检查，均不能单独证明子运行时已消费候选。[2] 缺失或不匹配时，应明确标为未证实，不计作成功。

**后续与边界。** 先在实际 owner 仓库对照既有 TODO、候选回放合同及 helper 实现，再冻结一个公开、范围有限的回放案例。建议验收既覆盖正确候选被消费，也覆盖加载旧版本或凭据缺失时不能误报成功。本次工作区未提供上述仓库材料，未完成去重、源码诊断或实际回放；没有修改源文件、生成层、TODO、版本或外部看板，也不构成产品发布依据。

依据：

- [1] [Public Maintenance Note](../inputs/01-single_ai_skills_core_input.md)，唯一问题事实来源。
- [2] 当前安装的 AI Skills Maintainer：`ai-skills-core/0.5/skills/maint/SKILL.md`，特别是 `Production Consumption Diagnosis` 与维护／领域责任边界。
- [3] 同一安装包的 `skills/bridge/SKILL.md` 及 `skills/bridge/references/canonical-ai-bridge-delegation.md`，规定 Bridge 回放运行时的实现归属。技能文件仅作为本次分诊规则来源，不作为候选插件实际消费证明。
