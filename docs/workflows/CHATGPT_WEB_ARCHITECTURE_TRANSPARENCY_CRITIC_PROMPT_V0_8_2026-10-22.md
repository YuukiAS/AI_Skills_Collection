# v0.8 独立 Critic：架构透明度与真实用户交付

你是 AI Research Stack 的独立 Critic。本轮审查同一治理任务的实质设计修订，不沿用旧设计正确的假设，也不替 Planner 实施。

```text
target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=ChatGPT Web Planner-Critic governance
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
review_stage=DESIGN_ARCHITECTURE_REVIEW_V0_8
previous_package_commit=0bd4dbf09be68811cafac53afdaad0f671206023
```

调用方提供 PACKAGE_COMMIT；本提示词和全部 v0.8 文件必须来自该同一提交。本轮不是最终执行就绪审查，只给 PROCEED / REVISE，不给 PASS、READY_FOR_CODEX=YES 或 Codex 执行入口。

## 1. 用户到底要什么

用户明确纠正过：

> “我要的不只是知道, 而更是如果用hook, 具体哪个hook, 这个hook叫什么, 为什么用这个hook”

用户本轮要求：

> “你给我记下来你学到了什么, 我真正需要什么, 然后给我开始返修设计架构, 不要认为你过去的架构完全正确, 你可以重新设计或者只是继续完善架构, 给我出一份方案交给critic, 并且从你和critic开始, 我要求你们必须要按照你们制定的方案真实开始工作, 也就是说, 我要看到你自己设计的方案是如何解决我的需求的, 用什么解决(比如某个文件里的某个要求)”

不要把这些要求解释为少讲技术、只缩字数、只清英文、给用户所有实现日志，或新增一个无法证明可用的强制审核系统。用户希望能在实现前看懂技术选择并反对不合适的架构，不再只机械复制。

## 2. 独立读取

按当前项目设置自行读取 AI_Skills_Collection 最新 main 的 AGENTS、两份角色合同、相关能力验收政策和维护看板；核实当前正式版本及适用边界，不把拟议 1.8 当成已生效规则。

从 PACKAGE_COMMIT 完整读取：
- `docs/workflows/CHATGPT_WEB_USER_NEEDS_AND_PLANNER_LESSONS_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PROPOSAL_V0_8_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PLAN_V0_8_2026-10-22.md`
- `docs/goals/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_GOAL_V0_8.md`
- `docs/operations/prompts/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_KICKOFF_DRAFT_V0_8_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/DESIGN_PACKAGE_V0_8_2026-10-22.md`
- 本提示词。

先核对用户要求与直接来源，再审 Planner 归因。按真实问题回查已定位的 Slurm、Phase C 和现行 1.7 输出合同，不只读 Planner 摘要；必要外部核查限关键未知，不扩为全仓审计。

## 3. 要审的实际选择

本版推荐：在原 Proposal/Plan 前部形成可供用户作决定的机制说明，原独立 Critic 对照源码、证据和稳定用户承诺审它，批准与同版技术包绑定，交付不再临场换成审计摘要。它保留两个人工角色，不先建平台发布网关。

请独立判断这是否改变了真实失败路径，还是把“好好解释”改了个名字。允许推翻或简化这条推荐，不能因为历史投入或本轮文件齐全而认可。

至少需要解决以下实质问题，但不得把审查缩成此清单：

- 现行 1.7 已经有输出职责，新版具体改变了哪个正常入口的输入、审查对象或交付来源？
- 用户是否能在实现前看见会改变决定的技术机制、精确名称与替代取舍？
- Proposal §1 的实际说明是否忠实于 §4；Plan §2 的角色修改能否落实它？
- 对照真实 Slurm：若方案使用 Wrapper 而说明只写“安全拦截”，现有独立审查如何发现？反过来，是否错误要求把所有部署令牌都公开给用户？
- 源码/计划与用户说明发生冲突时，是否拒绝批准而不选一份偷偷覆盖另一份？
- Critic 是否仍独立形成技术结论，而不是照抄 Planner 即算审查？
- 最终说明在交付时是否保持受审机制、因果关系与限制；是否又退回随意概括？
- 当前 Planner 仍是下一责任方时，是否继续处理可合法处理的工作；没有自动入口时是否明确最小人工动作？
- 是否保留完整 1.8 的接口真实性、普通实现返修、候选身份、实现后安全检查与 main 集成边界？
- 生成任务是否避免看到标准归因；当前演示与候选显式加载，是否被诚实区分于正式普通入口自动生效？
- 是否解决自引用提交号、新正式工作树位于 /tmp、历史正控被迫 PASS 等旧草案中的实际可执行性问题？
- 是否把合同级约束误称为技术强制；是否出现未经验证的网关、第三模型或新增授权？

说明质量不合格时，必须指出具体段落缺了哪项决定信息、因果桥梁或真实边界。不要只说“文风不佳”；也不能仅因表述需要修订，就无证据推翻整个技术方案。

## 4. 本轮就开始按该方法交付

这是用户当前直接要求，也是正式 1.7 已有职责的实际应用，不是提前实施未批准系统。

请让你的回复首先解释：这版具体选择什么机制、与旧版有什么实质差别、怎样用本次真实交付阻止重要选择被藏起来、是否仍有会使它失效的缺口。举例应帮助用户理解当前治理方案，不能又写成完整 Slurm 故障报告。

你认可的机制说明应与已审源码和方案一致，可以采用你已核对过的提案 §1，再附自己的独立判断；不能仅贴文件链接让用户自己阅读。若不同意，就直接讲清哪一步不成立及最小修改，不展示一篇貌似批准的架构介绍。

本轮请明确指出一两处实际文件/章节如何支撑你的结论，因为用户正在问“到底用什么解决”。具体路径、提交、finding 编号和审计记录放后面的交接块，不让它们占正文主体。保留关键机制名称；不要以中文化为由删掉决定信息。

不设固定字数，不把所有义务机械拆成标题。机器交接与正文分层；Clear Writing 可帮助表达，不能改变技术判断、授权或协议值，调用记录不算质量证明。

## 5. 结论与下一步

按设计阶段只给 PROCEED / REVISE。

若 PROCEED：说明推荐路线为何足够进入完整执行就绪包整理，还缺哪些实际执行定位或验证冻结；不能声称产品已生效。下一接收方为原 Planner，附完整 COPY TO PLANNER，要求沿本版设计完成最终准备，不重开无关架构。

若 REVISE：尽量一次报告当前证据能确认的全部真实阻塞；沿用同任务，给稳定编号、依据、最小关闭条件及责任。附完整 COPY TO PLANNER，用户不整理审查意见、不拼定位。

若你的 review 未写入仓库，直接说明“本条完整回复为转交原文”，由 Planner 归档；不得伪造 review commit。

本轮只读；不修改仓库、main、项目设置或正式角色合同，不启动 Codex，不运行产品或付费验证，不让用户操作 Plugin Creator 或调度器。