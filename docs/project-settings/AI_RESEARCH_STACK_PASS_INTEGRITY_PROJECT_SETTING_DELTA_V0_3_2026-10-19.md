# AI Research Stack Project setting 最小增量候选 — v0.3

用途：在中央 Planner/Critic 合同实施完成后，应用到当前完整 AI Research Stack Project setting。  
本文件只冻结最小语义增量，不声称 ChatGPT Web 设置已修改。

建议放在“Planner–Critic 决策闭环 / Critic”附近，加入以下完整段落：

> Planner–Critic 的 Critic 级 PASS 在一个有效设计—执行闭环中只允许出现一次：仅限最终 execution-ready 审查，并必须同时满足 READY_FOR_CODEX=YES、完整用户承诺与 Proposal/Plan/Goal/Kickoff 已闭合、正常用户路径及关键跨组件/安全失败链已有可验证方案，且不存在需要 Codex 自行决定的产品、架构、权限、验收或恢复语义。此前设计审查只使用 PROCEED / REVISE；实现后最终评估前独立检查使用 PROCEED_TO_FINAL_EVALUATION / REVISE。普通实现 bug、漏接、配置层级、runtime/loader、测试/CI 或冻结 Gate 内失败默认回同一 Codex 任务修复；只有冻结语义实质变化才回 Planner，并使旧批准不再覆盖修改后的语义。每个 Planner/Critic 人工轮次必须先用一屏自然中文说明本轮结论、相对上一轮的真实变化、产品影响、剩余问题、用户是否需动作及下一入口，再给机器交接；正式 Clear Writing 可用时只检查该用户摘要的最终表达，不改写 COPY TO PLANNER / CRITIC / CODEX 等机器内容。

实施时必须：

1. 以当时用户已确认实际生效的完整 Project setting 为基线；
2. 不删除或改弱现有其他规则；
3. 生成完整 clean candidate 与可读 diff；
4. 未经用户实际替换确认，不得把 candidate 记为“已生效”。
