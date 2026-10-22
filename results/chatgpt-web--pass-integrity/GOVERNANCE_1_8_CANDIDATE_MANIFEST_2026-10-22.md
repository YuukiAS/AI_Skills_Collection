# Planner–Critic 1.8 候选身份

本次 1.8 文本和本地回归已冻结为同一个候选。它目前只是等待独立安全审查的实现候选，不能称真实 Web 验证通过，更不能称正式 main 已升级。

```text
task_key=chatgpt-web--pass-integrity
IMPLEMENTATION_APPROVED_PACKAGE=230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f
BOOTSTRAP_CRITIC_AUTHORITY=results/chatgpt-web--pass-integrity/CODEX_BOOTSTRAP_AUTHORITY_RECEIPT_2026-10-22.md
GOVERNANCE_CANDIDATE_COMMIT=dcae2eae18729ffd8955ddccecd148a2c1aaaa09
implementation_branch=design/chatgpt-web--pass-integrity-v0-4
implementation_workspace=/overflow/htzhu/mingcheng_new/AI_Skills_Collection
observed_origin_main_at_freeze=f1de8e85957d32a50f4458349f450ec65add13bb
merge_base_with_observed_origin_main=272f5cd1b3599acb0c5b95ef57ce00a0cf1b0ac3
```

当前用户实际发送的 post-review authority 已先于任何 1.8 Web 输出如实记录在上述 receipt；它确认本次 1.7 final Critic 的 `PASS`、`READY_FOR_CODEX=YES`、所审 exact package、批准 locators、实施权限和停止条件。不声称原冻结 package 包含后来才产生的完整 Critic 回复，也不伪造它的 commit。

| 候选组成 | Git blob |
| --- | --- |
| `docs/workflows/PLANNER_ROLE_CONTRACT.md`，1.8 | `262d60d215f0a766b072756af59759b9f9731142` |
| `docs/workflows/CRITIC_ROLE_CONTRACT.md`，1.8 | `2ddde9cbdc1097dfe4794982861e19f48366d85a` |
| `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md` | `b0a275b5c08669b63c714c33a46610695277fed1` |
| `tests/test_chatgpt_web_decision_visibility_contract.py`，八项本地回归 | `7a8dd00e68bfb1410eb4878b5f7d4a276ec5bebc` |
| `results/chatgpt-web--pass-integrity/GOVERNANCE_1_8_LOCAL_VALIDATION_2026-10-22.md` | `241160ac2eb80cd2c6eb13b4319b3f40fa2038d5` |

上述五份文件是本轮 candidate-defining allowlist。冻结验证合同为 package commit `230e35d7e0ccfaed6e04ef7c3b31f9eaa3462e3f` 中的 `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_13_2026-10-22.md`；不是候选期另行改写的标准。后续只可追加绑定本候选的审查、运行或回读证据；上述来源发生实质变化时，旧候选评价失效，须重新冻结并重新审查。

下一步由独立 Critic 实际阅读本候选 diff、两份完整合同、本 manifest、v0.13 冻结验证输入及用户 UI 成本/停止条件，只给 `PROCEED_TO_FINAL_EVALUATION` 或 `REVISE`。它不是第二次 execution-ready 技术 PASS。只有前者才能进入 A/B/C/C2/D/E fresh Web；旧 bootstrap PASS 不替 Case C 的 1.8 Critic 决定结论。用户只承担已批准包规定的必要 Web 界面操作，不手工选择内部 Reviewer，不拼测试标准。
