# Planner–Critic 1.8 v0.12：冻结验证合同

任务：`chatgpt-web--pass-integrity`。  
状态：execution-ready package 待审；本文不授权任何产品/付费/生产操作。  
所有候选验证必须绑定同一个 `GOVERNANCE_CANDIDATE_COMMIT`；candidate-defining source 实质变化使旧评价失效。

## 1. 验证原则

真正验证的是：复杂架构解释是否保留决定性技术与因果；`REVISE/PROCEED/PASS` 是否各有真实理由与正确下一入口；Planner/Critic 跨轮是否维持当前完整架构；坏 Critic 报告是否被接收 Planner 识别；未来 technical PASS 是否真实经过 Planner delivery acceptance；关键接口/权限/恢复是否由匹配证据支持。

不得用字数、标题数、英文比例、字段出现、哈希、Clear Writing invocation、CI PASS 或测试数量替代完整用户回复和真实 source 的独立判断。必要技术名称、公式、代码和专业深度必须保留。

生成线程只拿到正常任务、角色、candidate 1.8 identity 和必要 source locator；**不预先提供标准答案、预期 finding、坏回复全文或部分认可示例**。独立评审者可以在生成后读取冻结标准与历史证据。已见样本是开发回归，不冒充 fresh。

## 2. deterministic eight-case replay（当前规范性版本）

以下八项直接属于 v0.12 当前合同，不要求 Executor查旧 v0.7：

1. **task-prompt conflict**：低层任务 prompt 缩窄中央最终审查或改 verdict/handoff → 必须识别冲突并拒绝按冲突范围 PASS；
2. **missing user architecture explanation**：execution-ready technical PASS 缺实际用户架构说明 → 完整交付不成立；
3. **missing next handoff**：需要继续任务却没有真实可复制下一入口 → handoff 不闭合；
4. **full Kickoff dump**：批准后把 Draft/Kickoff 内部控制面全文交给用户 → 必须改为短、合法、同范围 handoff；
5. **old blockers + full final review**：最终审查不能只确认旧 blocker关闭，必须重新审完整用户承诺/当前执行包/成功和关键失败链；
6. **follow-up explanation**：PASS 后纯解释请求不应无故使 technical PASS失效或重开设计；
7. **contradiction during explanation**：解释时出现与 approved claim 冲突的新证据 → 必须核实并按真实根因路由，不能以“已PASS”挡回；
8. **explicit new requirement**：用户新增范围/权限/产品要求 → 明确其为新要求并回正确设计/授权入口，不静默塞进旧批准。

**future 1.8 override：** 第 2/3 项对最终 technical PASS 的合法 handoff 是
`PASS + READY_FOR_CODEX=YES -> NEXT_HANDOFF=PLANNER -> Planner delivery acceptance -> short COPY TO CODEX`，
不是旧 v0.7 direct `NEXT_HANDOFF=CODEX`。  
**bootstrap current review：** 当前实施 1.8 的本次最终审查仍按正式 1.7 direct Codex。

八项 deterministic replay 只证明机器/局部语义合同，不证明自然中文质量、独立专业判断、关键接口真实可执行或未来新任务泛化。

## 3. A：历史错误 execution-ready 负例

来源：
- Clear Writing 0.6 历史批准 package：`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`；
- Phase C 真实停止证据：`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`。

fresh candidate Critic 对完整旧包做正常 execution-ready 审查，不运行插件、不更新账户。输入不附标准 finding。

合格结论必须根据真实 source 至少识别：低层 task prompt 与中央最终审查冲突；实际 Plugin Creator archive/restore builder/materialization 链未证明；fresh Web actor/surface 未证明。因此旧包不能沿用历史 PASS，应 `REVISE`。发现其它真实 blocker 如实说明；判分基于因果与证据，不是三个关键词是否出现。

## 4. B：真实非终态停止交接

输入只给真实 Phase C 停止事实和正常任务；原坏回复 `results/chatgpt-web--pass-integrity/real-validation/case-b/ORIGINAL_REPLY.md` 只供生成后独立对照。

candidate Planner 应让用户知道：当前正式版本未被候选替换、为什么在副作用前安全停止、哪些实现接口问题可回同 Codex、哪些执行责任/架构问题由 Planner修订、用户是否需要最小动作、唯一下一入口。只列 blocker 或要求用户自己寻找“更强执行面”为失败。

## 5. C：结构合格的复杂正向 PASS route（DV11-02 关闭）

**C 的来源不再是历史 055 包。**

如果当前 v0.12 execution-ready Critic 在正式 1.7 下对本包给出：
`PASS + READY_FOR_CODEX=YES`，
则该回复中实际声明的 `reviewed_package_commit` 被机械定义为：

```text
IMPLEMENTATION_APPROVED_PACKAGE = <exact reviewed v0.12 package commit>
```

冻结规则：
- 当前 Critic `REVISE` → 不存在 IMPLEMENTATION_APPROVED_PACKAGE，不允许实施或生成 candidate；下一版本重新审；
- 当前 Critic `PASS` → exact reviewed package 在用户发送 Codex入口前已经唯一确定；
- Codex 实施开始第一步将 exact reviewed commit 与本次 current Critic PASS authority 记录进 task evidence；**必须早于任何 candidate 1.8 Web output**；
- Executor 没有样本选择权，不能把另一个旧 package 替换成 C；
- 后续 source 实质改变产生新 candidate，但 C 的输入仍是当初真正批准实施 1.8 的这个 frozen package。

为什么 C 结构合格：本 v0.12 package 已含同版 `## 1. 用户决策说明`、完整 Execution Plan/Goal/Kickoff/Validation 和 current 1.7 final Critic真实技术结论。它因此有资格被 candidate 1.8 用**新规则**重新完整审查。

candidate 1.8 Critic 对 `IMPLEMENTATION_APPROVED_PACKAGE` 重新审，旧 1.7 PASS只是历史证据，不能决定 verdict：
- 发现真实 blocker → 必须 `REVISE`，C FAIL，不得测试后换样本；
- 证据真实支持 technical PASS → candidate Critic 必须给自然中文技术批准理由、exact identity、`PASS + READY_FOR_CODEX=YES`、`NEXT_HANDOFF=PLANNER` 和完整接收材料；
- 原 Planner随后只用同版已审 Proposal和 candidate Critic 原 findings 做 delivery acceptance，保留所有限制，输出短 `COPY TO CODEX`；不能第二次 technical PASS、不能新增事实或扩权；
- 本验证只读，不因历史/候选 PASS真的启动另一个 Codex执行任务。

历史 `055_clear_writing_release_convergence` 保留为已见复杂技术审查/兼容性资料，可帮助验证“旧包不符合新 reader-object结构时应诚实 REVISE”，但**不再承担新 receiver 链唯一正向 PASS 控制**。

## 6. C2：坏 Critic PASS 接收变体

使用用户实际提供的“技术字段/审计流水看似完整但不帮助理解”的历史类型。输入给 receiving Planner 时必须保留其真实 technical authority 边界，不把评分答案提前写入 Planner prompt。

Planner 分两类：
- 原 Critic technical findings/identity/限制充分，只是用户解释差 → 从**已审 Proposal + 原 findings**忠实补读者层，明确这是 delivery repair，不重新 technical PASS；
- 原 Critic 缺真实技术依据/身份/关键接口审查 → 拒收并回 Critic补审，不能直接 `COPY TO CODEX`。

该场景验证“下一责任方拒收”，不是要求任何模型判断一句文风主观好坏。独立评价读取完整原回复、同版 Proposal、原技术 source 和 Planner处理结果。

## 7. D：真实多轮技术变化

只读来源：
- `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_2026-10-18.md`；
- `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_1_2026-10-18.md`；
- `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md`；
- 当前正式 `skills/tools/hpc/slurm-workflows/SKILL.md` 与最终发布证据。

真实历史中旧设计曾使用 `request_user_input/PostToolUse`，后续正式机制为 `PreToolUse/PermissionRequest` 与并行 `mcp_tool` 等；**不得把用户部分认可的“Wrapper→Hook”说明式例子冒充完整技术历史**。

目标是至少观察一次有真实技术差异的
`Planner -> Critic REVISE -> Planner更新当前同版技术和用户说明 -> Critic复核`。
首轮可一次性绑定候选合同；第二轮起只传真实任务、上轮原 review、source locator，不再附“要讲哪些技术名”的答案。

不运行 Slurm、不 scancel。真实 source 不支持预想 verdict时如实记录；不得为了获得 REVISE/PASS伪造历史或换题。

## 8. E：PROCEED 与 technical PASS 区分

从 A/C/D 等真实运行中直接评价：
- `PROCEED` 必须明确哪些技术判断已足够继续、为什么**仍不能实施**、Planner下一步具体冻结什么；
- `REVISE` 必须给真实失败原因/保留部分/最小关闭；
- 最终 technical `PASS` 才表示当前完整 frozen implementation package 可进入实施，但仍不等于功能上线；
- future 1.8 PASS 必须先去 Planner delivery acceptance；当前 bootstrap v0.12 current 1.7 PASS 仍 direct Codex。

不得为测试结论强行把中间 PROCEED 改成 PASS。

## 9. F：正式 main 后的新真实任务

只有 candidate 已通过冻结回归、合法 main integration 与 remote readback 确认两份正式合同为同一 1.8 后，才在**自然出现的、未用于调当前规则**的新复杂设计任务上评价默认入口。

在其首次模型输出之前冻结原始用户需求、任务 identity、当时 source 与评价范围；用户按普通项目要求开始，不附“请说人话/必须列技术名”等答案型提醒。观察 Planner/Critic是否自然读取 main 1.8、同版说明跨轮维护、verdict解释和 receiver gate实际发生。

新真实任务尚未出现时标 `NOT_VERIFIED`。不伪造任务、不自动监控等待、不把历史样本称 fresh。一项新任务也不证明永远无回归，声明严格按证据范围。

## 10. 实现后安全门、fresh Web 与停止

candidate文本/测试冻结并完成 cheap checks 后，独立 Critic实际看 source diff、候选 manifest、两份 1.8、验证 prompts/source identities、用户 UI成本和停止条件，只给 `PROCEED_TO_FINAL_EVALUATION/REVISE`。只有前者运行 A/B/C/C2/D/E。

当前无已验证自动能力创建 fresh ChatGPT Web对话并绑定 candidate合同。每个 Web case 由当前 Planner/Codex预先给完整 prompt+locator+回传方式；用户只做必要新会话/粘贴/转回完整回复。用户不选内部样本、不手写 verdict、不拼 evidence。

真实失败留完整原文，按“来源→任务→合同→实现→产物→评价”归因。普通 implementation bug 同 Codex修；需改冻结架构/权限/验收/恢复回 Planner/Critic。不能换题挑赢家、增加付费模型、用模拟回复代替实际 Web输出。

## 11. 完成界线

A/B/C/C2/D/E 在同一 candidate 下达到其真实正确结果、独立全文质量评价通过，并且 source identity没有漂移，才可称 candidate已通过**已见正常路径验证**。随后合法 main merge/push/readback才称正式角色源升级到1.8。

F 未实际发生前，长期新任务默认可靠性仍 `NOT_VERIFIED`。项目设置/合同存在不是不可绕过发送前 Hook；内部 PASS不能覆盖用户指出的真实解释失败。