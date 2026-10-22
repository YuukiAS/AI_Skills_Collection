# Planner–Critic 1.8 v0.12：最终 execution-ready 待审包

日期：2026-10-22  
任务：`chatgpt-web--pass-integrity`  
分支：`design/chatgpt-web--pass-integrity-v0-4`  
阶段：`FINAL_EXECUTION_READY_REVIEW_V0_12`  
当前：`READY_FOR_CODEX=NO`；正式 main 仍为 Planner/Critic 1.7。  
本文件不包含自身提交 SHA；用户交给 Critic 的提示词必须提供**当前分支最新 exact PACKAGE_COMMIT**，避免自引用哈希。

## 当前同版完整包

Critic 必须从单一 PACKAGE_COMMIT 读取：

1. `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_12_2026-10-22.md`
2. `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_12_2026-10-22.md`
3. `docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_12.md`
4. `docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_12_2026-10-22.md`
5. `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_12_2026-10-22.md`
6. `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_FINAL_CRITIC_PROMPT_V0_12_2026-10-22.md`
7. 本 manifest

当前直接审查依据：
- `results/chatgpt-web--pass-integrity/FINAL_CRITIC_V0_11_USER_FORWARDED_REVISE_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/DESIGN_CRITIC_V0_10_USER_FORWARDED_HANDOFF_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/USER_PARTIALLY_ACCEPTED_MULTIROUND_EXPLANATION_2026-10-22.md`

历史 v0.7 可用于 Critic核对“旧语义是否已完整并入当前 Plan”，但**不再是实施 authority**。旧 v0.11 package只作为 DV11-01/02 的被退回版本；旧 v0.10设计 `PROCEED` 只证明总体架构方向，不替代本版 final review。

## v0.12 相比 v0.11 的唯一实质修订

**DV11-01 closed by design candidate：** v0.12 Execution Plan 将所有仍有效的 Planner/Critic 1.8 P18/C18、candidate identity、八项 deterministic replay、fresh Web边界、安全门、main integration/readback逐项写为当前规范。旧 v0.7 future C18-2 direct `NEXT_HANDOFF=CODEX` 被明确标为 `REPLACED BY` future 1.8 `technical PASS -> Planner delivery acceptance -> COPY TO CODEX`；当前 bootstrap仍按正式1.7 direct Codex。

**DV11-02 closed by design candidate：** Case C 不再使用结构上不满足新 reader-object 的历史055 package。若本 v0.12 exact package获得当前1.7 final PASS，则 Critic实际审的 exact `reviewed_package_commit` 在实施开始、任何 candidate 1.8输出之前被唯一冻结为 `IMPLEMENTATION_APPROVED_PACKAGE`。candidate 1.8重新完整审它，旧PASS不自动有效、真实 blocker就REVISE、不换样本；只有真实 candidate PASS才继续 Planner receiver链。当前 final review REVISE则没有 Case C/实施。

旧055继续作为已见复杂技术/兼容性材料，不承担新接收机制唯一正控。

## 执行和验证边界

本包不修改 Project setting、Capability Gate Policy、任何 Plugin、Clear Writing、Slurm、Bridge Kit、Mica、Plugin Creator 或生产服务；不授权付费、实际调度/插件 mutation、账号或 credential 变化、新第三人工角色/服务/database/state machine/watcher/daemon/prompt compiler/浏览器拦截。

实施目标只包括正式两份角色合同 1.8、现有 collaboration regression、当前 results/validation及必要最小 deterministic tests。真实候选完成后仍需 implementation safety gate、冻结 Web评估、合法 main integration/readback。正式 main升级后，新真实任务出现前长期默认可靠性仍 `NOT_VERIFIED`。

## 看板 pending mutation

当前任务仍属于 AI Skills repo-level governance maintenance。精确任务键搜索未确认已有专属 Issue；当前 Planner未创建 reader-facing Issue，因为 Maintenance Board要求该文案创建前**真实调用**当前安装的 Clear Writing，而本线程没有可证明的正式调用结果。不得把仅阅读 Skill文档冒充调用。

后续具备合法 Clear Writing + Project mutation入口的同任务维护动作应：
- 先按语义重新搜索/reuse现有 Issue；
- 无合适项才建立 `maintenance-track`；
- kind=`kind:governance`；
- scope=`scope:repo-workflow`；
- area=`area:repo`；
- Status=`DOING`；
- current execution anchor=本次最终 v0.12 package commit；
- next step=独立 `FINAL_EXECUTION_READY_REVIEW_V0_12`；
- 同源 source/Issue backlink按 Board规则维护。

当前 Project 未同步；**用户无需手工维护**。此 metadata 不是 execution-ready technical blocker。

## 当前唯一下一入口

独立 Critic 使用当前正式 1.7 对整个 v0.12 execution package作最终 review。若 `REVISE`，给原 Planner完整下一交接；若 `PASS + READY_FOR_CODEX=YES`，本次按 current 1.7 直接给短 `COPY TO CODEX`，用户实际发送才授权实施。