# Kickoff 草案 v1.0：Planner–Critic 可信架构交付

任务：`chatgpt-web--pass-integrity`；日期：2026-10-22。
状态：未获最终设计/执行就绪审批，**不得复制本文直接启动 Codex**。只有用户发送最终明确授权的短执行入口才能开始已批准范围。

## 技术定位

仓库：`YuukiAS/AI_Skills_Collection`
原设计分支：`design/chatgpt-web--pass-integrity-v0-4`
本版唯一提案：`docs/workflows/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_PROPOSAL_V1_0_2026-10-22.md`
同版 Plan：`docs/workflows/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_PLAN_V1_0_2026-10-22.md`
Goal：`docs/goals/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_GOAL_V1_0.md`
本草案与同提交中独立 Critic 审查提示词共同构成**设计送审包**，不是已冻结实施包。

正式基线仍然是 `main` 的 Planner/Critic 1.7。当前不实施任何 1.8 正式角色合同修改。

## 设计审查前需要决定，不能留给 Codex 猜

1. v0.9 的“说明提前写+原 Critic 审核”不足是否成立；本版是否正确区分语义质量、机器同版和受控用户呈现三个不同目标；
2. AI Skills 现有验证程序是否适宜扩展出真实消费的批准包一致性校验，以及在哪一个现有正常执行入口调用才可能真正拒绝错误包。只把脚本挂 CI 而不作为启动/展示门槛，不得宣称强制；
3. 目前 ChatGPT Web 无受控用户最终输出渠道的问题，是否必须通过一个真正可用的受控界面解决；本版暂以 Mica 现有 DOM 内容脚本作为需调查的候选，不假设它已经具备显示/校验功能；
4. Mica 现有 P0 限制、真实权限/认证边界与跨仓库所有权是否允许这项有界研究。未证明时不能给最终 execution-ready PASS，或必须明确只批准较低等级的合同/一致性能力；
5. 原有 1.8 接口真实性、非终态路由、同一候选、正式 main 集成和读者整篇质量验收如何完整保留。

只有经过中间 Critic `PROCEED` 后，Planner 才整理能执行的同版完整方案；未核实 Mica/Bridge 及正常入口消费前，不可宣布全部能力已解决。

## 候选实现预计最小范围（仍受后续设计与授权决定）

- AI Skills 既有 `PLANNER_ROLE_CONTRACT.md`/`CRITIC_ROLE_CONTRACT.md` 的实际源流程与说明审查职责；
- 适量复用当前 `scripts/skills.py`/tests 验证技术包、说明和批准身份，要求实际启动入口消费；
- 如果必要且获得单独授权，进行范围明确的 Mica 浏览器扩展受控说明展示可行性；这**不是本包目前授权的产品实现范围**；
- 相关治理回归记录、独立证据与正式 main 版本回读。

不得新增第三人工角色、另一个专业假 Critic、长期 daemon、数据库、通用提示词编译器或隐形付费审查。

## 真实运行验收边界

真正的正常入口应满足：未审的“PASS”不会被展示为已批准；过期正文不能配新技术包；真实批准的阅读原文能被用户看见；Codex 接收的正式入口与同一批准源一致。人工独立 Critic 的语义判断不能被字符串检查替代。模拟内容脚本/本地 CI 不足以声称真实登录 ChatGPT Web 运行成功。

如果做不到受控用户呈现，允许记录“角色合同+候选一致性已实现”，但不能对用户声称历史最困扰的 Web 解释失效已经被技术保证解决。

## 禁止行为

本轮不修改正式 main、Role Contracts、Project setting、Mica、Bridge、Slurm、Plugin Creator、任何插件产品；不改生产授权、分支保护、权限、浏览器账号，不开展付费/危险操作或实际 Web 自动化。

若设计因现实证据需要跨仓库权限或 UI 实现，按最新 Planner/Critic 和用户授权规则单独冻结边界，不允许 Codex 借通用 Goal 私自扩大范围。

## 下一个角色

唯一下一入口是独立 Critic 的中间**设计**审查；只能 `PROCEED / REVISE`，不能 `PASS + READY_FOR_CODEX=YES`。若 REVISE，原 Planner 负责同 task key 下重新设计并生成下一条 Critic 提示词，不要求用户重新重复所有要求。
