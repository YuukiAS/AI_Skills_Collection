# Canonical Goal v0.11：Planner–Critic 1.8 审查交付可信度

日期：2026-10-22；任务键：`chatgpt-web--pass-integrity`。
状态：执行就绪 Critic 待审，**不是已经批准的 Codex Goal**。当前 `main` 角色合同仍为 1.7。

完整方案身份仅由同版准确提交中的：
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_11_2026-10-22.md`；
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_11_2026-10-22.md`；
- 本 Goal；
- `docs/operations/prompts/CHATGPT_WEB_DECISION_VISIBILITY_KICKOFF_DRAFT_V0_11_2026-10-22.md`
确定。文件不写自身提交哈希，由最终交接绑定准确 PACKAGE_COMMIT。原 v0.10 设计 Critic 的用户转交 `PROCEED` 原文归档于 `results/chatgpt-web--pass-integrity/DESIGN_CRITIC_V0_10_USER_FORWARDED_HANDOFF_2026-10-22.md`，它是设计阶段依据，**不等于本版 execution-ready PASS**。

## 用户实际获得什么

复杂架构任务的每个重要 Planner/Critic 回合都要让用户明白当前进度、技术机制、实际选与不选的理由、最重要的真实因果链、安全/恢复条件、证据与未证明处，以及 `PROCEED/REVISE/PASS` 结论为什么成立。用户只机械转发按职责生成的短角色交接内容，不必自行查仓库、改内部状态或反复提醒自然中文。

多轮返修要保留当前完整架构说明，不能只关闭上轮 finding。重要技术变化必须写入同版 Proposal 的稳定 `## 1. 用户决策说明`，由独立 Critic 对照现行技术核对。该节身份为 Proposal path+version+exact package commit；Plan/Goal/Kickoff 仅引用这一份，不复制平行长报告。

**真正新增的接收动作**：现有 `PROCEED/REVISE` 返回原 Planner 时，Planner 先核对 Critic 原始技术依据及给用户的结论是否足够。技术审查充分但文字失焦，忠实从原评审与受审 Proposal 恢复读者说明；专业证据不足则拒收并返回补审。唯一 execution-ready 技术 PASS 仍由 Critic 独立批准，但实施后的正式行为改为先 `NEXT_HANDOFF=PLANNER`，由原 Planner 用已审说明完成一次读者交付后再给短 Codex 指令。增加的用户成本只有最终技术 PASS 后一次机械转发；不产生第二技术 PASS。

## 允许实施的精确范围

获独立最终 Critic `PASS + READY_FOR_CODEX=YES` 并由用户发送适用的短执行入口后，仅在已确认的授权仓库/已有任务分支更新：
1. `docs/workflows/PLANNER_ROLE_CONTRACT.md` 1.7→1.8；
2. `docs/workflows/CRITIC_ROLE_CONTRACT.md` 1.7→1.8；
3. `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md` 的真实修订来源；
4. 当前 `results/chatgpt-web--pass-integrity/**` 的合格真实验证证据及必要的最小机械回归测试。

保留原 v0.7 正确能力：任务提示词不覆盖中央合同、关键跨接口真实性、非终态实际交接、PASS 后解释与新证据分型、候选同一身份与独立预最终安全审查、正式 `main` 集成并回读。无新插件、第三角色、付费模型、服务、数据库、状态机、浏览器拦截、Mica/Bridge 修改。不得修改当前 Project setting、Capability Gate Policy、Clear Writing、Slurm、其它 Plugin 产品或生产服务。

## 先实施，再诚实验证

候选内容冻结后，通过原有确定性检查、真实历史 A/B/C、只读多轮 D、最终技术 PASS→Planner 接收链与独立全文质量审查；评价合同在 `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_11_2026-10-22.md`。不得为了得到正例而对真实有 blocker 的对象强迫 PASS，不能让生成模型收到评分答案。用户必要的 fresh Web UI 操作应由同任务提前准备准确提示词，不得让用户自己搭评审框架。

受控回归通过且获授权后，按现行仓库规则合法合入 `main` 并远端回读正式两份 1.8 角色合同。若以后有尚未用于调规则的真实新任务，提前冻结其正常输入后观察是否无需用户提醒而持续运行；没有新任务时不得声称这一长期表现已被验证。

## 严格禁止

此次设计 `PROCEED` 不能启动 Codex。后续实现不允许自己决定增加职责 owner、改变关键安全/费用/数据授权、选择新 Gate 成功标准、偷偷改角色流向、将普通 bug 扩成大型新系统、操作真实 Slurm 或 Plugin Creator、force Git 或发布插件。真正改变冻结语义，回同一任务的 Planner/Critic；同范围内普通实现错误留同一 Codex 修。任何正式 Critic PASS 均不能替代用户授权。
