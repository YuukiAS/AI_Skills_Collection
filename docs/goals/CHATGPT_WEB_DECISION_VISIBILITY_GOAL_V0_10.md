# 目标草案 v0.10：每轮进度与架构决策都能被用户真正理解

任务：`chatgpt-web--pass-integrity`。日期：2026-10-22。
同版提案：`docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_10_2026-10-22.md`
同版计划：`docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PLAN_V0_10_2026-10-22.md`
状态：只有设计草案；不得被当作 Codex 执行授权。本轮只允许独立 Critic `PROCEED/REVISE`。

## 用户承诺

以后在 AI Research Stack 设计、审查与多轮返修插件、Skills、Profiles 或 Bridge Kit 时，每个重要 Planner/Critic 轮次，用户都能直接从自然中文了解：目前真正进展到哪、稳定了哪些决策、为什么得到 `REVISE` 或 `PROCEED` 或最终 `PASS`、采用的真实技术及替代、正常请求如何经过系统、哪些风险/权限/实际能力仍未解决、下一步由谁负责。不能把用户逼回技术文件、日志和机器字段里找答案。

不需用户每轮重新提醒“说明 Hook/Wrapper/MCP 的确切选择、讲具体例子、删审计垃圾、保持中文”。确切技术名称与必要科研深度保留；无决定价值的机器流水放在 repo 与可复制 prompt。

## 原正常流程必须真实改变的位置

1. 原 Proposal 的用户决策说明成为当前同版完整交付，不再等 Critic PASS 临时创作；
2. 独立 Critic 从用户要求与源码检查说明和技术方案两者，给每种 verdict 有因果与证据的用户判断；
3. 既有 `PROCEED/REVISE` 交给原 Planner 时，由 Planner **接收并检查** Critic 的真实技术/人类说明，不能只按机器 verdict 推进；表达糟糕但技术充分可忠实补读者层，技术缺证据不能补文案冒充；
4. 唯一 Critic 技术 `PASS` 保留严格标准，但下一入口拟变成原 Planner 的一次交付接受，不再直接把不合格 Critic 自报的 PASS 变成 Codex kickoff；由 Planner 以经过 Critic 审查的同版架构说明和独立结论交付给用户，渲染短 Codex prompt；
5. 多轮技术语义变化时更新同一 Proposal 的用户说明，并在新版本上进行独立复审，不静默沿用旧 PASS。

## 验收不可替代

- 完整真实 `REVISE` 回合，用户能理解缺陷、保留机制、最小改动与下一个检查对象；
- 完整真实 `PROCEED` 回合，明确哪些决定已稳定、为什么还不能实施；
- 最终技术 `PASS`，解释当下真实机制、历史阻塞关闭、已审范围，实际由原 Planner 拒收不合格说明并交最终 Codex 入口；
- 至少一次无重复“说人话”提醒的多轮 `Planner→Critic→Planner→Critic`，同一版机制说明随技术真实变化更新；
- 真实坏样本包括 Slurm、Bridge、Clear Writing Phase C、三次垃圾 Critic PASS；不能用计数/关键词自评、不能向生成线程喂标准答案；
- 正式角色合同合入 main 并远端回读后，还要从普通真实新任务入口验证，不把候选文档存在等同于默认生效；
- 对用户确切下一动作，不要求用户手动跟踪 Issue/分支/审查历史。

## 不做什么

没有 Mica 或其它浏览器扩展、外部模型服务、第三人工角色、额外 Review database、控制网关、后台守护程序或重新开发 Bridge。原 v0.7 正确的关键接口现实证据、非终态交接、同一候选评估与集成边界保留。

本治理不修改 Project setting、Capability Gate Policy、目标 Plugin、Slurm、Bridge/Mica 或任何生产环境。v0.10 仅供独立设计审查，当前正式角色仍为 1.7。合同必须先真正被普通模型调用、真实多轮通过评估，才可以宣称此类使用改进已验收；不能保证任意未经本治理流程的 ChatGPT 回复在技术上不可能违规。
