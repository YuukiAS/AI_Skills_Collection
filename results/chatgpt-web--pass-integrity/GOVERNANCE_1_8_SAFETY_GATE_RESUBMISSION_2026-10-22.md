# 1.8 同一候选：实现后安全门复审入口

先前独立 Critic 给了 `REVISE`：候选角色合同未发现需重新设计的缺陷，缺的是可核对的真实网页逐案输入和交接安排。本次只补这个准备缺口，**没有**运行 A/B/C/C2/D/E，没有改评分或候选。若需在 ChatGPT Web 复审，用户只把下面整段发回原独立安全审查 Critic 线程，并将其完整原文转回同一 Codex 任务；无需自行组装各 case。

```text
请对同一任务 chatgpt-web--pass-integrity、同一治理候选做“实现后、真实 Web 最终评估前”的独立安全门复审。这是你上次 REVISE 指出的网页执行准备缺口的返修，不是重新设计、不是新的技术 PASS，也不是现在启动网页测试。

target_repo=YuukiAS/AI_Skills_Collection
source_branch=design/chatgpt-web--pass-integrity-v0-4
IMPLEMENTATION_APPROVED_PACKAGE=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f
GOVERNANCE_CANDIDATE_COMMIT=dcae2eae18729ffd8955ddccecd148a2c1aaaa09
prior_task_head=150316eecc3e6b9486dfd1a0eb39b3ee87be376d

候选身份与五个冻结 blob：results/chatgpt-web--pass-integrity/GOVERNANCE_1_8_CANDIDATE_MANIFEST_2026-10-22.md
原安全门入口：results/chatgpt-web--pass-integrity/GOVERNANCE_1_8_SAFETY_GATE_HANDOFF_2026-10-22.md
本次新增逐案提示词、角色、固定来源、轮次依赖和用户回传安排：results/chatgpt-web--pass-integrity/WEB_EVALUATION_INPUTS_AND_HANDOFF_2026-10-22.md
C2 真实原 Critic PASS 全文：0b7446b96d7f4b2a20e9bddf9ef4169bcfff9e64:results/chatgpt-web--pass-integrity/real-validation/case-c2/ORIGINAL_CRITIC_PASS_2026-10-22.md
C2 原文 SHA-256=d4f914f064033abe3edd1d5161f0d2de9808763d4c70956882b0282664b8da22
冻结评价标准：230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f:results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_13_2026-10-22.md

请实际读取新增准备材料与 C2 原文，核对它是否与冻结验证合同一致：A 的旧包正常独立复审不收到停止答案；B 不收到原坏回复；C 对 exact 实施包重新完整审查，真实 REVISE 不换样本，真实 PASS 才由独立 Planner 接收；C2 的真实报告有来源、全文、当时 1.7 technical authority 边界，生成线程不收到评分答案；D 有真实历史时间切片、两角色独立多轮、原文传递与只读来源；E 不加测试消息。检查用户是否只需必要的网页 UI 动作、Codex是否会准备好动态轮次的完整 prompt 和结果归档。无法加载候选合同或真实来源必须停止，不能把静态检查当 Web 表现。

同时复核候选本身的五个冻结 blob 与此前检查范围，确认本次只追加 results 测试准备证据，没有改合同、产品、批准包或评分标准。请只给 PROCEED_TO_FINAL_EVALUATION 或 REVISE，并用自然中文解释依据、尚未证明的事项、exact 候选身份及唯一下一责任方。若仍 REVISE，请指出具体准备或同一冻结语义内的缺口；只有必须改变冻结用户承诺、架构/owner、权限、成功定义、验收或恢复语义时才返回 Planner。不要自己运行 A/B/C/C2/D/E，不合入 main；请给完整原文供同一任务保存。
```

此文件是复审请求，不预判安全门 verdict。收到真实 `PROCEED_TO_FINAL_EVALUATION` 前，所有网页 case 保持 `NOT_RUN`，`main` 集成也不启动。
