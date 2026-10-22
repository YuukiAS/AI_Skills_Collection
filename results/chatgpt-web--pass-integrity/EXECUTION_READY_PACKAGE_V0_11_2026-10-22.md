# Planner–Critic 1.8 v0.11：最终执行前待审包

日期：2026-10-22。
任务：`chatgpt-web--pass-integrity`。
设计/准备分支：`design/chatgpt-web--pass-integrity-v0-4`。
审查阶段：`FINAL_EXECUTION_READY_REVIEW_V0_11`，当前 `READY_FOR_CODEX=NO`，**未通过、未实施、正式 main 仍为 1.7**。
调用方在 Critic 提示词内提供实际 package commit。本文件**不保存自身所在提交 SHA**，避免自引用或将后续提交与旧审查身份拼接。

## 同一完整包（全部从单一 PACKAGE_COMMIT 读取）

1. `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_11_2026-10-22.md` — 当前唯一 Proposal，第 1 节为同版读者决策说明；
2. `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_11_2026-10-22.md` — 两份角色合同具体改动、真实运行入口、用户成本、正常及失败恢复；
3. `docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_11.md` — 同一执行目标；
4. `docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_11_2026-10-22.md` — 最终实施授权草案，**不能单独使用**；
5. `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_11_2026-10-22.md` — A/B/C 真实任务、D 跨轮更替、未来正常新任务、完整文本专业验收；
6. `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_FINAL_CRITIC_PROMPT_V0_11_2026-10-22.md` — 依据当前正式 1.7 的独立执行就绪审查入口；
7. 本 manifest。
8. `results/chatgpt-web--pass-integrity/DESIGN_CRITIC_V0_10_USER_FORWARDED_HANDOFF_2026-10-22.md` — 用户转交的独立设计阶段 `PROCEED` **原始机器交接**。不是模拟的 review commit，也不代表有完整 user-facing Critic 文章。
9. `results/chatgpt-web--pass-integrity/USER_PARTIALLY_ACCEPTED_MULTIROUND_EXPLANATION_2026-10-22.md` — 用户部分认可的解释段落，已见开发参考，不是质量金标准。

旧 v0.7、v0.8、v0.9、错误扩项 v1.0 与设计阶段 v0.10 仅作历史与真实失败证据；旧 Goal/Kickoff、历史 PASS 都不具有本轮执行权。

## 当前已核实的外部事实

- `YuukiAS/AI_Skills_Collection main@f1de8e85957d32a50f4458349f450ec65add13bb`：Planner/Critic 正式 1.7，Capability Gate Policy 1.2，现行项目设置快照和仓库 AGENTS；
- `YuukiAS/GPT_Codex_AI_Bridge_Kit` 最新 main 的 AGENTS/Review 相关规则已读取，不能沿用旧文档设在 `/tmp` 的新正式工作树，也不能用别的仓库的角色/授权替代本仓库；
- `YuukiAS/AI_Research_Toolkit` 当前《复杂架构的可信解释标准》只供理解因果解释、决定性取舍和多轮身份边界的通用参考，未成为本任务运行依赖；
- 用户转交的 v0.10 独立 Critic verdict 为 `PROCEED`，三项要求 A/B/C 均在新版 Proposal/Plan/Validation 具体落地；它不是本版最终执行就绪审查；
- 本阶段还没有任何真实 Web 候选 1.8 回放、实现后安全门或正式合入证据。真正实施前须有本版独立 `PASS + READY_FOR_CODEX=YES` 及用户随后发送的短执行授权。

## 如果最终 Critic PASS，此次究竟批准什么

只批准在实际可验证的已有任务 branch、合法工作区中修改原两份角色合同/对应治理回归资料，并执行同版无付费的有界真实验证与满足条件的普通 main 集成。**此次首次实施批准仍使用当前 1.7 的 `COPY TO CODEX` 直接入口**；只有 1.8 实际生效后，后续复杂插件任务的最终技术 PASS 才先返回原 Planner 做读者交付接受。

没有新第三角色、Mica、Bridge 修改、Plugin Creator、付费 API、浏览器拦截、控制引擎或未知的生产资源变更。用户普通 `PROCEED/REVISE` 无新转发，未来唯一执行就绪 PASS 后增加一次机械转发作为第二人工线程接收机会。

## 看板追踪的真实待办（不是用户操作要求）

本治理任务此前精确任务键及相关中文语义的 GitHub Issue 检索未确认可复用的专属 Issue；这不表示整个仓库所有历史记录已被排除。根据 AI Skills Maintenance Board 的规则，进入正式跟踪应使用 `maintenance-track`、`kind:governance`、`scope:repo-workflow`、`area:repo`，Project Area=`repo`，状态 `DOING`，执行锚点指向本包最终提交，下一步为独立 execution-ready Critic。新建/实质修改读者面对的 Issue 文案还要求**真正调用当前已安装 Clear Writing**；本 Planner 当前只核实了其 Skill 文本、没有可证明的正式调用结果，故没有擅自创建 Issue 或声称 Project 已同步。交给具备合法调用及 Project 入口的同任务 AI Skills 维护方补齐；不得要求用户手工更新看板，不得让未同步的元数据冒充产品失败或阻挡已合法的只读设计审查。

## 这一阶段的唯一下一入口

独立 Critic 对本包的所有必要原文、专业机制、真实执行角色/权限、交接和质量验收进行**唯一 execution-ready** 审查。若 `REVISE`，自动给原 Planner 带真实 finding 与 source 的完整交接；若 `PASS`，按当前 1.7 合同同回复提供自然中文批准解释、`READY_FOR_CODEX=YES` 及短 `COPY TO CODEX`。本 manifest 和本轮 Planner 都不能冒充 Critic 正式结论。
