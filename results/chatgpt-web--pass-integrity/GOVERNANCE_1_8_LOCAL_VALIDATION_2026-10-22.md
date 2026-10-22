# Planner–Critic 1.8 本地验证记录

两份中央合同已按 v0.13 冻结计划形成 1.8 候选；本地检查通过，但还不能称正式规则升级或真实 Web 验收通过。实际生成的完整用户回复、独立实现后安全审查和 A/B/C/C2/D/E fresh Web 验证仍未发生。

批准来源：`230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f`。启动后实际收到的批准身份与边界先记录于 `CODEX_BOOTSTRAP_AUTHORITY_RECEIPT_2026-10-22.md`；不把后产生的 Critic authority 倒写进原包。

## 合同落点

| 冻结要求 | 唯一主要落点 |
| --- | --- |
| P18-0：同版用户决策说明与身份 | Planner §2.1 |
| P18-1：任务专用 Critic prompt 兼容 | Planner §10.1 |
| P18-2：短 Codex 入口可渲染 | Planner §11 |
| P18-3/3a/3b：关键接口、前置探针与条件能力 | Planner §7.1 |
| P18-4：非终态完整交接 | Planner §10.1 |
| P18-5：接收 Critic 结果的三分法 | Planner §10 |
| P18-6：技术 PASS → Planner 接收 → Codex | Planner §10，§11 只解释短入口 |
| P18-7：PASS 后三类追问 | Planner §10 |
| C18-0：审查身份与独立读源 | Critic §2 |
| C18-1：任务 prompt 冲突硬门 | Critic §6 |
| C18-2：同一回复内完整技术 PASS，先回 Planner | Critic §6.1 |
| C18-3：PASS 后三类追问 | Critic §6.1 |
| C18-4：关键接口证据硬门 | Critic §4.F |
| C18-5：整段用户回复的审查 | Critic §6，§6.3 保留比例化说明 |
| C18-6：读者说明与技术源一致 | Critic §6 |
| C18-7：Planner 接收材料 | Critic §6.1–6.2 |

## 八项本地回归

`tests/test_chatgpt_web_decision_visibility_contract.py` 固定检查：任务 prompt 冲突、缺用户架构说明、缺下一入口、Kickoff 全文转发、只关旧 blocker、PASS 后解释、解释时出现矛盾、新增要求。额外检查两份合同同为 1.8/2026-10-22，及 future technical PASS 的 `NEXT_HANDOFF=PLANNER`。这些是静态条款与局部交接语义检查，不模拟 ChatGPT Web 回复，也不以关键词命中替代真实质量评价。

本地命令与结果：

```text
python -m unittest tests.test_chatgpt_web_decision_visibility_contract tests.test_project_thread_handoff_contract -q
Ran 21 tests — OK
git diff --check — OK
```

两份修改后的合同已完整重读。读者检查重点是：先解释机制和下一步，再给字段；不让用户手工选择内部 Reviewer；不把 `PASS` 说成上线或长期可靠。原有正常使用六问、比例化 PASS 说明、有限同因果一跳检查、owner-first 和简单连续版本规则仍在。新增内容没有第三个人工角色、机器状态、审查协议或控制层；Project setting、Capability Gate Policy、AGENTS、Clear Writing、Slurm、Bridge Kit、Mica、Plugin Creator 及其它产品未修改。

下一门是同一候选的独立 Critic 实现后安全审查，结论只能是 `PROCEED_TO_FINAL_EVALUATION / REVISE`。前者到手前不运行 fresh Web A/B/C/C2/D/E；所有真实 Web 输出须按验证合同保存完整原文，Case C 不换样本。正式 main 远端回读及未来新复杂任务仍分别待证。
