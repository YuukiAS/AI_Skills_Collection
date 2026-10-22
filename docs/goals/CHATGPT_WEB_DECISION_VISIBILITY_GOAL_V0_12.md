# Canonical Goal v0.12：Planner–Critic 1.8 可信架构说明与接收

任务：`chatgpt-web--pass-integrity`。日期：2026-10-22。  
状态：最终 execution-ready Critic 待审；不是 Codex 授权。正式 `main` 角色仍为 1.7。

## 用户结果

以后复杂插件/Bridge/工作流等正式架构设计中，用户每个重要 Planner/Critic 回合都能直接理解：当前进度、真实技术选择及关键替代、代表性成功/失败链、为什么 `REVISE/PROCEED/PASS`、哪些已验证与仍未知、下一责任方。多轮返修后不依赖用户重复提醒，也不让最新 blocker 抹掉当前完整架构。

重要 Proposal 的同版 `## 1. 用户决策说明` 是用户说明的唯一当前来源；实质技术改变同步更新。Critic 从真实 source 独立审技术和说明是否一致。收到 Critic 结果的 Planner 必须验收真实交付：专业依据完整但表达失焦时只从已审 Proposal/原 Critic findings 恢复读者层，专业依据不足则拒收并退回补审。

正式 1.8 下唯一技术 `PASS + READY_FOR_CODEX=YES` 的未来链为：
`Critic -> NEXT_HANDOFF=PLANNER -> Planner delivery acceptance -> short COPY TO CODEX -> user authorization -> Codex`。
Planner不是第二技术批准者，不能改 verdict、增加技术事实、扩 scope 或自授 PASS。普通 `PROCEED/REVISE` 原本就回 Planner；用户永久新增成本只有唯一技术 PASS 后一次机械转发。

## 完整 1.8 合同

实施必须依据同版 `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_12_2026-10-22.md` 的完整 P18/C18 合同，而不是让 Codex读取历史 v0.7 自行合并。

明确包括：task-prompt compatibility、short handoff renderability、critical-interface reality evidence、pre-side-effect probe、conditional capability、non-terminal handoff closure、Planner receiver acceptance、PASS follow-up classification、Critic task-prompt hard gate、future atomic technical PASS route、critical-interface hard gate、whole-response acceptance、user-decision/source consistency、self-contained receiver handoff、`GOVERNANCE_CANDIDATE_COMMIT`、candidate-source变更失效、八项 deterministic replay、fresh Web user-only boundary、post-implementation Critic safety gate、main integration + remote readback。

旧 v0.7 的 direct `NEXT_HANDOFF=CODEX` 在未来正式 1.8 被明确替换；本次首次实施 1.8 的当前 execution-ready review 仍按正式 1.7 直接给 Codex。

## 正控与验证

如果当前 v0.12 exact package 获当前 1.7 最终 `PASS + READY_FOR_CODEX=YES`，该 Critic 实际审过的 exact package commit 自动冻结为 `IMPLEMENTATION_APPROVED_PACKAGE`，在任何 1.8 candidate输出前记录。candidate 1.8 Critic重新完整审它，旧 PASS不自动有效；发现 blocker必须 REVISE，不换样本。只有 candidate自己真实技术 PASS 才继续测试未来 `PASS -> Planner delivery acceptance -> short COPY TO CODEX`。

历史旧 055 包只保留复杂技术兼容材料，不再担任新 receiver 正控。

其它真实负例、中断交接、多轮技术变化、main后新真实任务按同版 Validation Contract 执行。全文质量由独立完整阅读判断，不能用关键词/字数/英文比例/哈希/Skill调用代理。

## 实施范围

最终 Critic真正 PASS且用户实际发送短实施入口后，允许修改：
- `docs/workflows/PLANNER_ROLE_CONTRACT.md` 1.7→1.8；
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` 1.7→1.8；
- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`；
- 当前治理任务结果、验证合同和必要的最小 deterministic tests。

不修改 Project setting、Capability Gate Policy、Clear Writing、Slurm、Bridge Kit、Mica、Plugin Creator、其它正式插件/生产系统；不增加第三人工角色、服务、数据库、状态机、付费模型或浏览器拦截。

## 完成声明

本执行包 PASS只批准实施，不证明 1.8 已生效。候选冻结、实现后安全门、真实 Web评估、合法 main integration/remote readback分别取得证据后才称相应阶段完成。正式 main 后尚未出现的新真实任务未验证前，不得称“长期无需提醒已在新任务证明”。