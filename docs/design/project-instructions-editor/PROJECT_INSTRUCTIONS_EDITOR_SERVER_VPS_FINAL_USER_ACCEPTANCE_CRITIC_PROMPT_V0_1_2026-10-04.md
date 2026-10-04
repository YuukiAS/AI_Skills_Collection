# Critic Prompt — Project Instructions Editor Server+VPS Final User Acceptance v0.1

你现在负责审查 project-instructions-editor standalone Skill 的最终用户验收补充方案。

这不是产品重设计，不重新打开已经 PASS 的产品架构、implementation package v0.2 或 G1–G4 taxonomy。

## Active Review Context

target_repo:
YuukiAS/AI_Skills_Collection

target_plugin_or_domain:
standalone Skill / project-instructions-editor

design_topic_or_task_key:
project-instructions-editor--standalone-skill-implementation

source_branch_or_ref:
main

execution branch:
work/project-instructions-editor--standalone-skill-implementation

execution worktree:
../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation

review_stage:
final real-user acceptance addendum

approved implementation Plan:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md

approved recovery Plan:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md

recovery Critic PASS:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_CRITIC_REVIEW_V0_1_2026-10-03.md

acceptance addendum:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_SERVER_VPS_FINAL_USER_ACCEPTANCE_V0_1_2026-10-04.md

acceptance package commit:
8a8b36a9eb55f180a89a7d74cbf294b54cc62fb7

tracking:
Issue #93

current intent:
The user explicitly selected their real Server+VPS ChatGPT Project as the final last-mile acceptance surface after implementation and independent review.

FINAL_SERVER_VPS_USER_ACCEPTANCE=PENDING
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO

## 必须读取

读取 latest main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/skill-todos/project-instructions-editor.md

读取：

- approved implementation Plan v0.2
- approved dependent recovery Plan v0.1
- dependent recovery Critic PASS
- acceptance addendum v0.1

不需要重新审产品职责、三 edit modes、G1–G4、版本策略或 recovery merge route，除非这个 acceptance addendum 自己引入了直接冲突。

## 1. 核心设计

Server+VPS 不替代 public-safe G4，也不创建 G5。

顺序是：

C2
-> G1/G2/G3
-> public-safe G4 packet
-> independent G4 / implementation PASS
-> one real Server+VPS user acceptance
-> only then final integration/release closure can claim the user-selected consumption test passed

请检查这是否符合：

- 用户不是 regression suite；
- final user acceptance 在自动验证和独立评审之后；
- G4 taxonomy 保持不变；
- 一个真实消费对象的人工验收可以作为 overall completion 的最后一公里，而不是新增 capability Gate。

## 2. 隐私边界

acceptance addendum 不把用户完整 Server+VPS Project setting、私有 Project history 或私有基础设施 transcript 提交到公开 repo。

实际 acceptance 使用当时 live Project setting。

repo 最多保留：

- acceptance contract；
- candidate identity；
- user accepted/rejected；
- 必要的 redacted failure category。

请检查这是否与当前 no-private-Project-data-external-transmission 边界一致。

如果你认为用户自己在其 ChatGPT Project 内应用设置构成新的风险，请给直接因果证据；不要把用户正常 Project 使用误判成外部数据传输。

## 3. 真实 failure signature

用户提供的真实不满意回答的核心失败是：

- 先写“验收结论 / 最终 PASS/FAIL”；
- 先堆长审计叙述、状态、源码细节；
- “还剩什么问题 / 用户现在要不要做事 / 下一步是什么”出现得太晚；
- 同一结论以多个 audit/status 形式重复。

Server+VPS 现有 Project setting 已经明确要求：

结论
-> 用户是否需要操作
-> 下一步
-> 必要原因
-> 技术证据

因此 acceptance addendum 不预先规定“一定要再加规则”。

editor 必须允许：

- bounded edit；
- bounded consolidation/reordering；
- no-op + execution-noncompliance diagnosis。

请检查这是否符合 frozen no-op / bounded edit semantics，而不是针对一个坏回答硬编码新规则。

## 4. 语义保真

任何 Server+VPS Project-setting candidate 必须保持原项目已有治理语义，至少：

- Clash_Profile / Remote_Compute_Infrastructure / MACHINE_LOCAL_INFRA ownership；
- Longleaf_Bridge 仅历史；
- proxy-client整体覆盖；
- server-first；
- client live network state 属于用户；
- USER_ACTION_REQUIRED；
- 用户不是 regression suite；
- canonical source first；
- fail closed；
- redundancy；
- secrets/privacy；
- partial evidence 不能冒充 global PASS；
- no unauthorized network mutation。

请检查 acceptance contract 是否足以防止“为了回答更短而削弱生产安全/权限/证据”。

## 5. Downstream frozen natural prompt

实际用户验收在 fresh Server+VPS Project thread 使用短自然问题：

“按最新实现审一下 Workstation 自动恢复，现在到底能不能放心不管了？还有什么会卡住？”

这个 prompt 故意不重复回答格式规则。

如果 acceptance 时 live issue 已变化，可以保持同一自然任务形状，替换为当前 Workstation/remote-recovery状态，不强行测试过时技术事实。

请判断：

- 这种 prompt 是否真实测试 Project instructions 的 downstream consumption；
- 是否避免 prompt-level coaching 冒充 Project-setting效果；
- 是否仍足够自然，不是合成 benchmark。

## 6. Human acceptance rubric

PASS 要求首次回答无需返修，即满足：

- 开头先告诉用户是否 ready / 剩余 bounded blocker；
- 立即告诉用户是否需要操作；
- 下一步在深层技术证据之前；
- 不用 PASS/FAIL matrix 开头；
- 不先堆 SHA/PID/job/log；
- 不重复结论；
- 普通解释自然中文；
- ownership 正确；
- MACHINE_LOCAL_INFRA 不因相关 repo evidence 被错误改成 repo owner；
- 不擅自改变 network state；
- 不让用户代替自动 regression；
- 真需用户动作时按 bounded USER_ACTION_REQUIRED contract；
- source-only / partial evidence 不冒充 live/global verification。

请检查这个 rubric 是否直接来自用户当前 Server+VPS Project contract，而不是新增不相关偏好。

## 7. 非绑定好答案示例

acceptance addendum 给了一个与当前 maintenance-guard failure 对应的“好答案形状”示例：

先用一段话告诉用户：

- 还没完全解决；
- 只剩 maintenance guard 一个小问题；
- 用户现在不用做事；
- 下一步只修 PendingFileRenameOperations 判定；
- 其他已经通过部分不要再动。

之后再解释 stale pending rename 为什么会 permablock reboot。

该示例明确标为 non-binding，不是固定模板或新永久规则。

请检查它是否只是 rubric illustration，而不是把最终输出 hardcode 成一段标准答案。

## 8. Failure handling

如果真实 Server+VPS 首次回答仍失败：

USER_ACCEPTANCE=FAIL

必须保留第一次输出，不在同一 candidate 上边改边宣布 PASS。

返回现有 project-instructions-editor implementation task，归因：

- Project-setting edit quality；
- normal consumption/noncompliance；
- another owner/plugin；
- product-surface limitation。

如果 candidate-owned behavior 改变：
形成新 candidate并重跑 affected same-final-candidate evidence。

请检查这里是否防止 user acceptance 被“修到满意为止”而失去验收意义。

## 9. 用户操作边界

只有以下全部完成后才允许请求用户：

- independent G4 PASS；
- implementation overall PASS；
- exact Server+VPS Project-setting candidate ready，或 editor给出 justified no-op。

届时仅一次：

USER_ACTION_REQUIRED
DEVICE = ChatGPT Server+VPS Project
WHY = final real-world acceptance of Project-setting output
ACTION = apply accepted Project-setting edit if any, open fresh Project thread, send frozen natural acceptance question once
CHANGES_NETWORK_STATE = NO
RETURN = first response only

不得让用户多设备、多 prompt、多轮陪跑。

请检查是否符合 user-is-not-regression-suite 与 current live-account mutation边界。

## 10. Completion semantics

public-safe G4 PASS 是必要条件，但不冒充这个用户选择的真实消费验收。

在真实 acceptance 之前：

FINAL_SERVER_VPS_USER_ACCEPTANCE=PENDING

即使 implementation review已经 PASS，也不能声称用户选择的 Server+VPS 实战验收已经完成。

acceptance PASS 也不自动授权 main integration/release/tag/publish；后续仍按 existing closure authority执行。

## 11. Maintenance state

Issue #93保持 open / DOING / standalone-skill。

当前 acceptance anchor：

docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_SERVER_VPS_FINAL_USER_ACCEPTANCE_V0_1_2026-10-04.md

如果没有 GitHub Project field mutation surface，只记录 pending mutation，不要求用户手工维护。

Issue reader-facing copy 只有真实调用 Clear Writing 后才可实质修改。没有 invocation surface：

CLEAR_WRITING_UNAVAILABLE

## 12. PASS / REVISE

如果 acceptance addendum 足够、不过重、不改变 Gate taxonomy：

CRITIC_RESULT=PASS
SERVER_VPS_FINAL_ACCEPTANCE_PLAN=PASS
GATE_TAXONOMY_CHANGED=NO
PRIVATE_PROJECT_SETTING_COMMITTED=NO
FINAL_SERVER_VPS_USER_ACCEPTANCE=PENDING
APPROVED_ACCEPTANCE_PATH=
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_SERVER_VPS_FINAL_USER_ACCEPTANCE_V0_1_2026-10-04.md
APPROVED_PACKAGE_COMMIT=
8a8b36a9eb55f180a89a7d74cbf294b54cc62fb7
NEXT_HANDOFF=EXECUTOR_CONTINUE_EXISTING_RECOVERY

此 PASS 只批准未来 final user acceptance contract，不表示当前 recovery/Gates/implementation已经完成，也不要求现在就让用户测试。

如果 REVISE：

CRITIC_RESULT=REVISE
FINAL_SERVER_VPS_USER_ACCEPTANCE=PENDING
NEXT_HANDOFF=PLANNER

每个 blocker 给稳定 ID、直接证据、因果风险和最小关闭条件。

不要因为可以写得更详细而阻塞，也不要重新审已经 PASS 的 product design / G1–G4。
