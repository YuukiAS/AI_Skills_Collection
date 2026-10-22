# Planner–Critic 1.8：执行就绪提案 v0.12

日期：2026-10-22  
任务：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
当前正式基线：`main@f1de8e85957d32a50f4458349f450ec65add13bb`，Planner/Critic 仍为 1.7。  
上一最终执行就绪审查：v0.11 @ `3b3a66411b99872b329657529a133745db0114e8`，Critic = `REVISE`；原文归档于 `results/chatgpt-web--pass-integrity/FINAL_CRITIC_V0_11_USER_FORWARDED_REVISE_2026-10-22.md`。  
当前阶段：重新提交完整 execution-ready 包；未获 `PASS`，不得实施。

## 1. 用户决策说明

v0.10 已经通过设计审查，核心架构**不重做**：Planner 在同版 Proposal 中维护用户真正需要阅读的当前技术决策说明；Critic 独立对照真实技术审这份说明；接收 Critic 结果的 Planner 不能只消费 `PROCEED / REVISE / PASS` 状态，而要检查这份审查是否真的足以让用户理解和继续任务；未来唯一技术 `PASS` 仍只能由 Critic 给出，但正式 1.8 生效后先回原 Planner 做一次读者交付接收，之后才生成 Codex 执行入口。

v0.11 被退回不是因为上述架构错误，而是两个执行合同没有完全闭合。

**第一，旧 v0.7 里已经设计正确的 1.8 能力不能只用“继续保留”四个字带过。** 当前正式 main 仍是 1.7；如果 Codex 真正开始实现 1.8，它不能一边读 v0.12、一边自己判断旧 v0.7 哪些规则还有效、哪些已经被新接收机制替代。因此 v0.12 的 Execution Plan 现在把所有仍有效的旧 P18/C18 义务逐项重新冻结：任务提示词不能覆盖中央合同、短 Codex 交接必须可从冻结包生成、关键执行接口要有现实证据或副作用前条件性核验、非终态必须真正完成交接、Critic 必须做接口 hard gate、整篇用户回复是验收对象、候选身份改变使旧证据失效、八项机械回归、实现后独立安全门、fresh Web 用户动作边界和 main 合入回读都写进当前合同。唯一被明确替换的是未来正式 1.8 的最终 PASS 路由：旧版“Critic PASS 直接 `NEXT_HANDOFF=CODEX`”被改成“Critic technical PASS + `READY_FOR_CODEX=YES` → `NEXT_HANDOFF=PLANNER` → Planner delivery acceptance → `COPY TO CODEX`”。本次**首次实施 1.8**的批准仍按当前正式 1.7 直接给 Codex，不提前使用尚未生效的新规则。

**第二，正向 PASS 验证不能再使用一个结构上不满足新 1.8 的旧包。** v0.11 仍拿历史任务作为最终 PASS→Planner 接收链的主要正控，但那个旧 Proposal 没有新 1.8 要求的同版 `## 1. 用户决策说明`。严格执行新规则就应该 REVISE；给它历史豁免又测不到新能力。v0.12 改为：**如果本次完整 v0.12 包获得当前 1.7 的最终 execution-ready PASS，那么 Critic 实际审过并批准的那个 exact PACKAGE_COMMIT，在任何 1.8 candidate source 生成之前被机械冻结为 `IMPLEMENTATION_APPROVED_PACKAGE`，作为候选 1.8 的复杂正向重审对象。** 它已经有同版用户决策说明、Execution Plan、Goal、Kickoff 和真实最终 Critic 技术结论，因此结构上有资格测试未来的新链路。candidate 1.8 Critic 必须重新完整审查，不能沿用当前 1.7 PASS；发现真实 blocker 就 `REVISE`，不得换题。只有 candidate Critic 自己确实给技术 PASS，才继续测试 `NEXT_HANDOFF=PLANNER → Planner读者交付接收 → short COPY TO CODEX`。

这两项修改不会增加新的系统、角色或平台依赖。用户的永久新增成本仍只有：**以后真正到唯一技术 PASS 时，多一次把 Critic 完整交接机械复制给已有 Planner。** 普通 `PROCEED/REVISE` 原来就回 Planner，不新增往返。验证阶段可能需要 fresh ChatGPT Web 对话，这是候选验收的临时 UI 成本，不是以后每个任务额外增加的常规步骤；每次提示词由当前 Planner/Codex 准备完整，用户不整理审查材料。

用户在当前阶段**不需要实施任何动作**。正式 main 仍是 1.7；v0.12 只重新提交最后 execution-ready 审查。若本版仍 `REVISE`，继续同一治理任务收口；若本版 `PASS + READY_FOR_CODEX=YES`，Critic 按当前 1.7 直接给短 Codex 入口，用户实际发送后才允许实施 1.8。

## 2. 已接受的总体架构与不变范围

保留 v0.10/v0.11 已接受方向：同版用户决策说明、Critic 对照真实技术独立审查、Planner 对 Critic 实际交付做三分法接收、最终技术 PASS 经 Planner 一次读者交付后才给 Codex、Planner 不能自授 PASS/扩权/补造技术依据。

保留旧 v0.7 的执行接口真实性、非终态闭合、候选身份、安全门、真实 Web 与 main 回读语义；本版仅将它们完整并入当前执行合同，避免 Executor 跨历史版本拼装。

不修改 AI Research Stack Project setting、`PLUGIN_CAPABILITY_GATE_POLICY.md`、Clear Writing、Slurm、Bridge Kit、Mica、Plugin Creator 或其它插件/生产代码；不新增第三人工角色、服务、数据库、状态机、watcher、daemon、prompt compiler、付费模型或浏览器输出拦截。

## 3. 同版用户决策说明与多轮更新

每个重要架构 Proposal 的用户读者层使用稳定语义 `## 1. 用户决策说明`，身份由 proposal path + proposal version + exact package commit 共同确定；它仍是原 Proposal 的组成部分，不建立第二份长期真相。实质技术、权限、默认行为或恢复边界变化时，Planner 必须提交完整下一版本并同步修改本节；Plan/Goal/Kickoff 只引用同版来源。

Critic 每轮先独立读取用户要求和真实技术，再审这份说明。若实际技术选择发生实质变化而正文几乎不变，或具体机制/安全边界被抽象词掩盖，必须视为实质审查问题。说明是否“自然”不能覆盖技术不真实；技术充分但最终表达失焦，则由接收 Planner 只从已审 Proposal 与 Critic 原 findings 忠实恢复读者解释。

## 4. 正式 1.8 的最终 PASS 与接收边界

正式 1.8 下唯一技术 execution-ready PASS 仍由独立 Critic 给出，并与 `READY_FOR_CODEX=YES` 同时成立。**唯一未来路由**是：

```text
Critic technical PASS + READY_FOR_CODEX=YES
-> NEXT_HANDOFF=PLANNER
-> Planner delivery acceptance
-> short COPY TO CODEX
-> user sends it
-> Codex executes
```

旧 v0.7 `NEXT_HANDOFF=CODEX` 在正式 1.8 中明确由以上链路 **REPLACED BY**，不能与新解释并存。

Planner delivery acceptance 只允许：
- 核对 exact reviewed identity、Critic 原 verdict/findings、同版用户说明与用户授权；
- 技术依据充分但表达失焦时，忠实重组读者说明；
- 生成不扩大范围的短 Codex 入口。

它不允许重新决定技术、增加证据、删除限制、改变授权、自授第二个 PASS。若需要新增技术事实才能解释，说明原独立审查不足，必须退回 Critic；若新证据改变架构/权限/验收/恢复，返回正规 Planner–Critic 轮次。

本次 v0.12 自身仍按当前正式 1.7 审查：若 Critic PASS，则直接给本治理实施的短 `COPY TO CODEX`。这是 bootstrap 边界，不是新 1.8 的未来普通产品行为。

## 5. 验证边界

A：历史错误 execution-ready 负例；B：Phase C 非终态交接；D：真实技术更替多轮；正式 main 后新发生任务的长期默认入口，均继续保留。

C 正向链改为本次**真正获得当前 1.7 execution-ready PASS 的实施批准包**。其 exact PACKAGE_COMMIT 由当前最终 Critic 的 reviewed identity 冻结；只有它 PASS 后才进入实施，所以在 candidate generation 前已经唯一确定。candidate 1.8 Critic重新审它，旧 PASS不自动有效、发现 blocker就 REVISE、不允许换样本。只有真实 candidate PASS 才运行未来新接收链。

历史 `055_clear_writing_release_convergence` 继续可作为复杂技术审查/兼容性材料，但不承担新 receiver 机制唯一正向 PASS 控制。

八项 deterministic replay 在同版 Execution Plan / Validation Contract 重新逐项冻结，不再用“保留旧八项”让 Executor查历史。所有整篇中文质量必须由完整回复和原技术源独立评价，不能靠关键词、字数、英文比例、哈希或 Clear Writing invocation。

## 6. 当前完成边界

v0.12 仍只是待最终审查的完整执行包。只有：
1. 当前正式 1.7 Critic 对同一 package 给唯一 `PASS + READY_FOR_CODEX=YES`；
2. 用户实际发送该次短 Codex 入口；
才授权实施两份角色合同 1.8 及同版有界验证。

实现、候选回归、独立安全门、真实 Web 评估、正式 main 集成和未来新任务长期表现都在之后分别取得证据，不提前宣称完成。
