# 1.8 候选的独立安全审查入口

候选已经完成本地检查。下一步不是发布或运行 Web 最终验证，而是由独立 Critic 审查同一冻结候选，判断能否开始 A/B/C/C2/D/E。若用户需要使用 ChatGPT Web，只需把下方整段发给现有 Critic 线程，并将其完整回复原文转回当前 Codex 任务；无需自己查文件、挑样本、写结论或找内部 Reviewer。

```text
请对 YuukiAS/AI_Skills_Collection 的同一任务 chatgpt-web--pass-integrity 做“实现后、真实 Web 最终评估前”的独立安全审查。这不是新的 execution-ready 技术 PASS，也不是请你代替用户启动评估。

source_branch=design/chatgpt-web--pass-integrity-v0-4
IMPLEMENTATION_APPROVED_PACKAGE=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f
GOVERNANCE_CANDIDATE_COMMIT=dcae2eae18729ffd8955ddccecd148a2c1aaaa09
候选身份和 blob：results/chatgpt-web--pass-integrity/GOVERNANCE_1_8_CANDIDATE_MANIFEST_2026-10-22.md
实际收到的 bootstrap PASS/READY authority：results/chatgpt-web--pass-integrity/CODEX_BOOTSTRAP_AUTHORITY_RECEIPT_2026-10-22.md
本地回归证据：results/chatgpt-web--pass-integrity/GOVERNANCE_1_8_LOCAL_VALIDATION_2026-10-22.md
冻结验证标准：230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f:results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_13_2026-10-22.md

请实际读取上述身份、从 230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f 到候选的源改动、两份 1.8 角色合同全文、八项本地检查及验证输入。独立判断 P18/C18 是否完整且没有旧 1.7 direct-Codex 语义残留，关键接口、用户说明、整段回复质量、交接权限和停止条件是否安全；核对候选是否保持两个人工角色、不改 Project setting/Capability Gate Policy/AGENTS/产品、不新增状态机或审查协议。检查真实 Web UI 必须由用户完成的动作是否已缩到必要范围；不要把静态测试当作实际 Web 质量。

请只给 PROCEED_TO_FINAL_EVALUATION 或 REVISE，先用自然中文解释依据和本结论尚未证明什么，再列 exact 候选 identity、真实 blocker 或限制、唯一下一责任方及必要的最小动作。若 REVISE，请指出属于同一冻结语义内的实现缺陷，还是必须回 Planner 的语义变化。不得用本次 bootstrap 1.7 PASS 替 Case C 的 candidate 1.8 verdict；Case C 仍完整重审 exact v0.13 package，发现真实 blocker 不换样本。请给出完整原文，供同一任务保存。
```

本文件只是已批准安全门的操作入口，不预判独立 Critic 结论。收到真实 `PROCEED_TO_FINAL_EVALUATION` 之前，不启动 A/B/C/C2/D/E；收到 `REVISE` 则按冻结范围和责任归因处理。
