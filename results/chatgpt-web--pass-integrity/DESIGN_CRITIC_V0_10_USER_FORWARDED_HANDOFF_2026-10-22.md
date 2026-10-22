# 用户转交的 Critic 设计审查交接原文

日期：2026-10-22。
审查对象：`chatgpt-web--pass-integrity` v0.10，批准的送审提交 `1fb7edd9955764644edc299fb9bc5142ea882e58`。
**证据性质：用户在当前聊天转交的 `COPY TO PLANNER` 原文。** 原 Critic 没有提交独立 review 文件；用户也未在本轮提供 Critic 回复机器块之外的其他正文。因此本文件保存的是转交的审查权威内容，**不能声称已取得、已验收 Critic 完整自然中文回复，不能编造 Critic GitHub commit**。

---

~~~text
NEXT_HANDOFF=PLANNER
=== COPY TO PLANNER BEGIN ===
继续同一治理任务：

target_repo=YuukiAS/AI_Skills_Collection
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
reviewed_package_commit=1fb7edd9955764644edc299fb9bc5142ea882e58
review_stage=DESIGN_ARCHITECTURE_REVIEW_V0_10
critic_verdict=PROCEED

当前正式 main：
f1de8e85957d32a50f4458349f450ec65add13bb

正式 Planner/Critic 当前仍为 1.7。v0.10 只是通过设计审查，不得因此实施或宣称 1.8 已生效。

本轮 Critic 没有向 repo 写 review 文件。以下内容是本轮独立审查 authority，必须如实归档；不得把 Planner 自己的转述冒充 Critic commit。

一、本轮独立结论

v0.10 的总体架构可以继续进入 execution-ready package 准备。

真正成立的新机制不是再写一遍“要说人话”，而是：

1. 同版 Proposal 中维护用户真正要看的当前架构决策说明；
2. Critic 同时独立审技术方案和这份说明是否与真实机制一致；
3. 接收 Critic 结果的 Planner 必须验收审查交付，而不能只消费 PROCEED / REVISE / PASS token；
4. 技术依据完整但用户表达差时，Planner可以从已经受审的同版 Proposal + 原 Critic findings 忠实恢复用户说明，不要求同一 Critic反复重新 PASS；
5. 技术依据缺失、所审版本错位、关键接口未核实或结论与源证据矛盾时，Planner不得把问题降级成“表达不好”，必须停止并退回 Critic真正补审；
6. 最终 execution-ready 技术 PASS 仍只能由独立 Critic给出，但下一入口改为原 Planner做一次读者交付接收；只有该接收完成后才由 Planner生成短 COPY TO CODEX；
7. Planner不能推翻 Critic verdict、扩大批准范围、自授 PASS或改变授权。

二、为什么最终 PASS 多一次 Planner 接收值得

保留该设计。

用户成本只增加唯一 execution-ready PASS 后的一次机械复制到已有长期 Planner；中间 PROCEED/REVISE 原本就必须回 Planner，不增加新轮次。

当前没有已验证的更简单等价机制：

- 让 Critic 自己验收自己的用户说明已经发生过真实重复失败；
- 让 Codex负责拒收太晚，并把技术/架构判断错误下沉给 Executor；
- 让用户自己判断 PASS 是否讲清楚违反本任务核心目标；
- 当前没有已验证的 Web 自动独立接收接口。

因此现有 Planner作为第二线程接收者，是当前最低复杂度的独立接收机会。不得新增第三人工角色、服务、浏览器网关、Mica或机器文本评分器来替代。

三、Slurm 真实反证必须保留

不要把
results/chatgpt-web--pass-integrity/USER_PARTIALLY_ACCEPTED_MULTIROUND_EXPLANATION_2026-10-22.md
当成 Slurm 历史或质量金标准。

Critic独立核实到：

- 2026-10-18 Slurm chat-confirmation Proposal v2 曾采用 native request_user_input + tiny PostToolUse binder，并把 MCP elicitation视为更重备选；
- 后续设计继续变化；
- 当前正式 slurm-workflows 0.5 的受保护取消机制是全局 PreToolUse / PermissionRequest，trusted command supervisor + parallel mcp_tool handler，local stdio MCP 在 owning root chat显示两选一确认；
- 当前正式机制明确不再使用旧 request_user_input/PostToolUse binder，也不使用 wrapper/PATH shim作为产品入口。

因此这组历史非常适合作为 v0.10 多轮连续性回归：
技术机制发生实质变化时，当前 Proposal 的用户决策说明必须同步变化；Critic必须能从真实 source发现过期说明。用户部分认可示例只作为“因果解释结构开始有用”的开发参考，不能预先塞进生成线程，也不能成为固定模板。

四、execution-ready package 必须进一步冻结的三项

这些不是当前设计 blocker，但在最终 execution-ready Critic 前必须明确完成：

A. 同版用户决策说明的 canonical identity

不要新建第二份长期真相。

在每个重要 Proposal 内给该读者层一个稳定、可唯一定位的章节身份，例如固定语义为“用户决策说明”；由：
proposal path + proposal version + exact package commit
共同确定身份。

技术方案实质变化时，同版 Proposal 必须同步更新该章节。
Plan/Goal/Kickoff只引用，不复制另一份会漂移的说明。

不要求固定篇幅、固定六段或固定字段模板。

B. Critic 原始技术 authority 与 Planner 最终渲染边界

最终 PASS 路径必须冻结：

Critic technical PASS
-> 原始 Critic verdict / exact reviewed identity / technical findings 被完整保存
-> NEXT_HANDOFF=PLANNER
-> Planner delivery acceptance
-> COPY TO CODEX

Planner补用户说明时：
- 必须保留 Critic 原 verdict和技术边界；
- 只能利用已经受审的 Proposal、原 Critic source/finding解释；
- 不得新增技术依据、改变 scope/authorization、删除 Critic limitation或冒充新的独立审查；
- 若需要新增技术事实才能把结论讲通，说明原 Critic evidence不足，应退回 Critic，不得自行补 PASS。

最终 Planner用户回复如果自身仍缺关键技术或误述 Critic理由，应判正常入口质量失败；不能因为底层已有 PASS token就宣布治理有效。

C. 正常入口真实验证

execution-ready Plan 必须冻结至少以下真实验证，不用机械增加更多同义样本：

1. 已见坏 Critic PASS 接收回归：
   Planner收到技术字段/机器状态看似完整但用户解释无用的真实历史类型时，必须识别；若技术依据完整则有界补读者层，若技术依据不完整则退 Critic，不能直接给 Codex。

2. 连续多轮真实技术变化：
   至少一次
   Planner -> Critic REVISE -> Planner实质改技术 -> Critic复核
   后续轮只给普通任务和准确 locator，不再附“说人话”“必须写Hook名”等答案型提醒。
   用户决策说明必须跟随真实技术变化，不得只关最新 finding。

3. PROCEED 与 PASS 区分：
   PROCEED 必须明确哪些设计已经稳定、为什么仍不能实施；
   execution-ready PASS 才能批准完整冻结机制。
   不得为了验收强迫有 blocker 的对象 PASS或换样本。

4. final PASS receiver test：
   Critic技术 PASS 后先回原 Planner；
   记录这次额外机械转发的真实用户成本和最终用户说明；
   验证 Planner确实没有自授技术 PASS，只完成交付接受。

5. 正式 main integration 后的新真实任务：
   提前冻结一个未用于调规则的普通真实设计任务。
   不再给生成线程附加逐条写作答案。
   验证正式 main 的角色合同被自然读取、跨轮解释和接收检查真实发生。
   已见 Slurm/Bridge/Clear Writing/部分认可示例不得冒充未见证据。

评价必须阅读全文，不使用字数、标题数、英文比例、字段数量、哈希或 Clear Writing invocation作为自然语言质量代理。

五、保持 v0.10 已正确的范围

继续保留：
- v0.7 已正确的 task-prompt compatibility；
- critical-interface reality evidence；
- non-terminal handoff closure；
- PASS 后 explanation / contradiction / new requirement 分流；
- exact governance candidate identity；
- post-implementation Critic safety gate；
- same-candidate真实验证；
- main integration + remote readback；
- 用户不手工维护内部 Issue/branch/review history。

不得修改：
- AI Research Stack Project setting；
- PLUGIN_CAPABILITY_GATE_POLICY.md；
- Clear Writing 产品；
- Slurm 产品；
- Bridge Kit；
- Mica；
- Plugin Creator；
- 其他正式 plugin/product source。

不得新增：
- 第三人工角色；
- 状态机/schema/database；
- service/watcher/daemon；
- prompt compiler；
- 付费模型；
- 浏览器输出拦截。

不要默认修改 AGENTS.md。只有最终 execution-ready package能证明现有 role-contract正常入口无法定位接收义务时，才提出最小 locator 修改并让 Critic独立审查。

六、外部核查结论

AWS ADR实践支持把重要架构决策的 context / decision / alternatives / consequences 放在由 owner维护、集中且版本化的决策记录中，并在接受前审查；这支持“同版 Proposal中的用户决策说明”，不支持另造数据库或服务。

OpenAI instruction hierarchy支持低层 task prompt不能覆盖高层稳定治理约束，但它不是模型行为的技术强制保证。正式 claim ceiling继续写清：Web双线程仍是模型治理，不是不可绕过runtime enforcement。

七、下一阶段

基于本次 PROCEED，准备完整 execution-ready package。

需要形成同版：
- Proposal；
- Execution Plan；
- Canonical Goal；
- Kickoff Draft；
- final execution-ready Critic prompt；
- 当前 Critic review的忠实归档；
- 候选/真实验证/失败停止/集成合同。

不要现在实施 1.8，不创建 Codex执行任务，不修改main。

当前看板若仍没有合法 Project mutation surface，按 AI_SKILLS_MAINTENANCE_BOARD.md 输出准确 pending mutation并明确未同步；不要让用户手工维护，也不要为了本任务新增另一套控制面。

Planner完成完整 execution-ready package后，回复必须先自然中文说明：
- v0.10哪些机制已经通过设计审查；
- 最终 PASS为何多一次 Planner接收；
- execution-ready包还冻结了哪些具体接口和验收；
- 用户新增成本；
- 当前正式main仍是1.7；
- 用户是否需要动作。

然后自动生成完整 COPY TO CRITIC，让独立 Critic对完整 execution-ready package作最终审查。
本次 PROCEED绝不等于 PASS，不得给 COPY TO CODEX。
=== COPY TO PLANNER END ===
~~~
