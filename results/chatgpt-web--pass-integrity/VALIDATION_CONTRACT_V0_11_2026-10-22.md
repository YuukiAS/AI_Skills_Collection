# Planner–Critic 1.8 v0.11：真实验证合同

任务：`chatgpt-web--pass-integrity`。当前仅为执行前待审合同，不授权真实产品/付费操作。本文与同版 Proposal/Plan/Goal/Kickoff 绑定同一 PACKAGE_COMMIT。所有候选 Web 评价绑定实际冻结的 `GOVERNANCE_CANDIDATE_COMMIT`。测试全文与判断存 `results/chatgpt-web--pass-integrity/`。

## 1. 验证对象、来源与不变性

直接观察：每轮架构决策和技术理由、真实技术取舍与因果过程、阶段性 `REVISE/PROCEED/PASS` 的原因、同版说明随技术返修更新、接收 Planner 能识别无用或无技术依据的 Critic 报告、唯一技术 PASS 经原 Planner 做读者交付接收再给 Codex，以及正式 main 后普通新任务无需反复提醒。

不能用字数、标题数、哈希、字段、英文比例、读取过 Skill 或测试通过替代完整中文质量。独立审查必须读取完整用户回复、实际技术文件和当前批准范围。必要术语/数学推导不能为压短文字而删除。

冻结时将源任务、实际请求、当前来源提交、候选身份、审查要求与计划次数记录在当前结果目录。运行线程只得到真实任务/角色/必要来源及 candidate role contract，不预先喂预期答案、历史坏回复或部分认可示例。评审者可在之后读取这些已见材料以校准。已见负例是开发回归，不冒充未见样本；同一最终候选的输入、审查口径与样本不能测试失败后临场换题。

## 2. A：历史错误 execution-ready 负例

读取历史 Clear Writing 0.6 批准包 `AI_Skills_Collection@d7b810d194ead881303aaca9c2e4f1d59a97c1f1` 与真实停止证据 `@38a81dc1df9a362ecee4be597cb3db5bd6fcac41`。fresh Critic 从完整源独立重新审执行就绪性，不运行插件。正确结论须基于真实提示词与中央规则冲突、恢复归档与实际字节消费缺口、fresh Web 操作执行者未被证明而作有依据的 `REVISE`，不能沿用旧 PASS。若发现其它真实 blocker 如实补充；不要求生成线程先知道这份评分答案。

## 3. B：Phase C 中断与用户交接

根据同一真实 Phase C 停止证据和正常用户任务让 fresh Planner 继续。旧坏回复在 `results/chatgpt-web--pass-integrity/real-validation/case-b/ORIGINAL_REPLY.md`，只给之后的独立评价，不给生成者。合格答复要让用户直接知道现有版本仍未被更新、为什么停、原同 Codex 能修的实现问题与需 Planner 重定责任/设计的问题、最小用户操作和实际唯一下一入口。仅列 blocker 或让用户寻找“具备某能力的环境”不合格。

## 4. C：真实复杂正控与最终 PASS 接收

锁定 `AI_Skills_Collection@745e6748c5faa7cbad51973142661491224ba5a2` 的 `055_clear_writing_release_convergence` 包；历史原审查 `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_CRITIC_REVIEW_R2.md` 和最终报告 `results/055_clear_writing_release_convergence/FINAL_REPORT.md` 只作事实证据，旧 PASS 不决定新 verdict。fresh Critic 完整审查，若真有 blocker 必须 `REVISE`；不得硬改标准或自动换样本。

只有证据真的支持 `PASS + READY_FOR_CODEX=YES` 时，Critic 给当前已审架构与自己技术理由、当前限制、`NEXT_HANDOFF=PLANNER` 的完整接收材料，**不提供直接 Codex Kickoff**。原 Planner 核实 Critic 原 verdict/同版说明/技术事实，忠实向用户展示，再生成短 `COPY TO CODEX`。不能再次技术批准、不能扩权；本次是只读评估，任何旧授权不因重新审查而生效。

同一测试家族包括坏报告接收：原技术依据充分但文字只是审计流水时，Planner 应从已审原文和原 Critic findings 恢复解释；技术依据/身份缺失时必须拒收并退回专业审查，不得把坏 PASS 直接转为 Codex 指令。

## 5. D：真实技术更替下的连续多轮

用只读历史源 `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_2026-10-18.md`、`docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_1_2026-10-18.md`、`docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md` 及当前正式 `skills/tools/hpc/slurm-workflows/SKILL.md` 和正式发布证据。历史 v2 涉及 `request_user_input/PostToolUse`，正式 0.5 使用 `PreToolUse/PermissionRequest` 与并行 `mcp_tool`，绝不把部分认可的“Wrapper→Hook”教学例子冒充实际完整历史。

至少观察一次技术实质变化后的 `Planner → Critic REVISE → Planner 更新同版技术和用户说明 → Critic 复核`。首轮可为候选合同绑定身份；后续只传普通任务与真实 review/source locator，不再附“必须说人话、具体写哪些 Hook”的答案清单。不修改 Slurm，不实际 `scancel`。若真实材料不支持制造的 REVISE，就保留未达成结论，不伪造历史或改题挑赢家。完整用户正文必须保留当前有效机制、前轮变化、仍未证明的故障和 verdict 原因。

## 6. 正式 main 后新任务默认入口

候选源/评价通过并合入 main、远端回读确认正式合同 1.8 之后，选择一个**新发生、尚未用于调规则**的真实插件/复杂架构任务；在其第一轮生成前记录任务身份、原始用户需求、来源/评审要求。用户仅发正常任务，不特别要求“读规则/讲 Hook”。观察新 Planner/Critic 是否自己消费 main 合同、同版说明是否跨轮保持、最终接收是否按职责完成。

如果真实新任务尚未出现，该项保留 `NOT_VERIFIED`；不能伪造任务、自动安排或把现有历史样本称为 fresh。已见样本通过和合同合入 main 不自动证明长期跨新任务可靠性。

## 7. 实际执行、安全、复核和停止

现有 Web 面没有经验证可自动创建 fresh 对话或选择候选合同；若测试需要，用户只承担打开新 Planner/Critic 对话、粘贴已准备提示词、转回完整原文等必需 UI 动作。每次动作由当前 Planner/Codex提前备齐，用户不自己整理证据或选择内部角色。无付费 API、Plugin Creator mutation、Slurm 操作或其它高影响副作用。

完成候选文本与确定性回归后，独立 Critic 先作 `PROCEED_TO_FINAL_EVALUATION / REVISE` 安全检查；前者允许运行冻结 Web 批次。遇到真实质量失败、候选身份漂移、权限或执行界面无法获取完整回复时保留原文并按原因回同 Codex 或 Planner，不换题追 PASS、不用 CI/模拟产物冒充正常入口。

候选真实 Web 批次符合冻结条件才能称 `CANDIDATE_ACCEPTED`；main 正式回读后才称“1.8 已进入正式规则”；未来新任务正常入口通过前不得称“长期自动有效已证实”。