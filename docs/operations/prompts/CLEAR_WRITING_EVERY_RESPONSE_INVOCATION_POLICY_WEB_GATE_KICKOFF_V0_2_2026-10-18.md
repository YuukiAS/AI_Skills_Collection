# Clear Writing Web Gate v0.2 — approved-execution kickoff draft

只在以下两项都成立后执行本提示词：

1. 独立 Critic 已对本 v0.2 Plan / Goal / Kickoff 同一 package 给出 execution-ready PASS；
2. 用户在 PASS 之后明确把本提示词发送给执行线程。

在这之前，不做任何真实 ChatGPT Project、插件、账号或 Web Gate 操作。

---

继续 Clear Writing 的真实 ChatGPT Web 调用策略验收，不修改 production candidate。

仓库：`YuukiAS/AI_Skills_Collection`  
任务：`clear-writing--every-response-invocation-policy`  
证据分支：`reviewed/clear-writing--scientific-explanation-readability-repair`

冻结 production candidate：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

先读取并严格执行：

- `automation/reviewed_handoff/tasks/clear-writing--every-response-invocation-policy/PLAN.md`
- `automation/reviewed_handoff/tasks/clear-writing--every-response-invocation-policy/CURRENT.json`
- `docs/goals/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_WEB_GATE_GOAL_V0_2_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_2_2026-10-18.md`
- approved proposal v0.2
- proposal Critic PASS
- 本 package 的 execution-ready Critic PASS

本轮只做真实 Web 证据采集和保存，不改任何 Clear Writing production source。

## 0. 开始前冻结

在第一个模型请求之前，先建立
`results/clear-writing--every-response-invocation-policy/web-gate-v0.2/FREEZE_MANIFEST.json`，
真实记录：

- production candidate commit；
- 当前 ChatGPT Web surface；
- 当前使用模型及可见的思考/模式设置；
- 当前实际 Clear Writing Web candidate/plugin identity，不能确认时写 `UNOBSERVABLE`；
- Project bridge exact bytes + SHA-256；
- Project memory mode；
- conversation isolation policy；
- W0/W1/W2/W3 task-bank commit/hash；
- attempt budget；
- W2 task-order/pair-order；
- frozen rubric；
- stop conditions。

不得凭旧聊天或 repo manifest 声称个人账号里已经安装/加载某 candidate。

## 1. 本提示词授权的测试范围

用户实际发送本提示词后，只授权下列 **测试专用、可逆、最小** 操作：

- 创建空的临时测试 Project / 新测试对话；
- 在测试 Project 中写入 Plan 冻结的 Project bridge exact bytes；
- 若 Web UI 提供 Project memory mode，给 matched test Projects 设置相同模式；
- 查看当前 Clear Writing candidate 是否真实可用、其可见 identity 是什么；
- 使用当前平台要求的用户确认完成已经审过的单一测试 candidate setup，但只限于 frozen candidate；
- 保存 public-safe 测试输出和必要的去身份化证据。

建议测试 Project 名称：

- `CW-W1-v02`
- `CW-W2-T-v02`
- `CW-W2-C-v02`

这些只是测试容器，不是生产 Project。

本授权不包括：

- 修改 AI Research Stack 或其他真实 Project 的 Project setting；
- 修改 global custom instructions；
- 修改 Clear Writing production source；
- 更改 plugin permissions；
- 清理、删除或覆盖用户已有聊天/文件；
- 为 W2 反复切换全局 plugin 安装状态；
- 切换账号、订阅或模型计划来制造 matched condition；
- 发布/公开 Clear Writing；
- 新建第二个 Clear Writing 产品身份来绕过比较约束；
- PIE、Mica、Research Authoring、Presentations；
- G7；
- release/version bump。

如果 W2 必须越过这些边界才能构造 control，直接
`W2=INCONCLUSIVE` 并停止，不要请求用户反复改账号状态来追求 PASS。

## 2. W0 — 先做安全性

W0 不使用 Project bridge。

按 frozen task bank 顺序执行 W0-A 和 W0-B。

### W0-A

在每个 W0-A 请求中，使用当前 Web surface 能提供的最强合法 Clear Writing 显式选择方式，并记录到底只是 plugin-level selection，还是存在更强的具体 Skill load evidence。

逐项检查：

- natural response 质量；
- sibling route 是否合理；
- mixed payload 是否精确保留；
- 长答是否被机械压短；
- prompt/contract 是否保持完整；
- 真分支流程是否保留；
- exact identities 是否不变。

任一 release-critical W0-A failure：停止。

### W0-B

对 exact-only task 做 explicit plugin selection stress。

只允许如下 claim：

如果只能证明 plugin-level selection：

`PLUGIN_SELECTION_DOES_NOT_CONTAMINATE_EXACT_OUTPUT`

不得声称 loaded-skill bypass。

assistant message 必须和 frozen target 完全一致；前言、代码围栏、解释、字段重排都算 FAIL。

任一 W0-B exact contamination：停止。

W0 全部 PASS 后才进入 W1。

## 3. W1 — Project policy 行为可靠性

创建/使用空测试 Project `CW-W1-v02`。

把 frozen bridge exact bytes 写入该测试 Project。不要向真实 Project 写入。

执行 W1-S01..S04，严格按 turn 顺序。每轮不手动 `@Clear Writing`。

W1 只判：

`PROJECT_POLICY_BEHAVIOR_RELIABILITY`

检查：

- ordinary -> exact exemption -> ordinary recovery；
- Chinese -> temporary English -> Chinese recovery；
- short -> long；
- explanation -> complete prompt/contract -> ordinary recovery；
- sibling route -> unrelated response；
- 无错误粘滞。

有真实 invocation/load evidence 就保存；没有就写 `UNOBSERVABLE`。

禁止使用“模型说自己用了 Clear Writing”证明加载。

W1 FAIL：停止。

W1 PASS 不等于 plugin causality；继续 W2。

## 4. W2 — strict matched plugin increment

进入 W2 前先做 environment eligibility check。

创建/使用两个空测试 Project：

- `CW-W2-T-v02`
- `CW-W2-C-v02`

两边：

- Project bridge exact bytes 相同；
- memory mode 相同；
- model/surface 相同；
- fresh isolated conversation；
- task/rubric/order/budget 相同；
- 不得互相读取 Project/chat history。

必须能真实证明唯一实质变量是：

`Clear Writing candidate availability / consumption`

Treatment 有 frozen candidate。

Control 不得有 candidate 可用/消费，也不得复制 Skill 正文或模仿 Treatment。

如果当前 ChatGPT 产品表面无法在不越过本授权边界的情况下建立这一条件：

`W2=INCONCLUSIVE`

停止 release。可以记录 diagnostic，但不能继续假装 W2 PASS。

如果环境合法，按 task bank 的 P01..P08 及 frozen pair order 运行，每个 arm/task 只取一次有效模型回答。

先把输出匿名成 A/B 给独立 Reviewer；Reviewer 冻结逐任务判断之后才能 reveal Treatment/Control。

W2 PASS 条件完全使用 Plan 的 frozen scoring rule，禁止看完输出再修改。

## 5. W3 — diagnostic only

只有 W2 已得到 PASS/FAIL/INCONCLUSIVE 结论后才记录 W3。

W3 不使用 Project bridge，不手工调用 Clear Writing。

按 frozen W3-D01..D05 执行。

W3 只描述 no-bridge discoverability/fallback 情况，不影响已经成立的 W0/W1/W2 结果，也不能拯救 W2。

## 6. G7 不执行

本提示词严禁执行 G7。

W0/W1/W2 如果全部达到 release-critical PASS，只写：

`READY_FOR_G7_FREEZE`

然后停止并交回 Planner。

后续 G7 必须另行冻结 exact candidate/plugin identity、bridge、surface/model、memory/isolation、attempt budget、fresh tasks、rubric、Reviewer input 和 stop condition，并再次过独立 Critic。

## 7. 证据保存

所有 repo 证据只写：

`results/clear-writing--every-response-invocation-policy/web-gate-v0.2/`

保存 full raw model outputs，不只保存 Executor verdict。

每个 run 至少记录：

- gate/task/turn；
- timestamp；
- surface/model；
- Project memory mode；
- bridge SHA；
- production candidate；
- actual Web candidate identity 或 `UNOBSERVABLE`；
- conversation isolation id；
- attempt number；
- prompt hash；
- response hash；
- invocation/load evidence；
- exact comparison result（如适用）。

不要保存账号 ID、凭据、私人聊天 URL 或无关项目内容。

如果需要 UI screenshot 且含私人账号信息，放
`private/exports/clear-writing--every-response-invocation-policy/`；
公开结果只记去身份化描述和 hash。

## 8. attempt / retry

每个 frozen task/turn/arm 默认只有一次模型回答。

只有原尝试因为网络/服务中断而完全没有可用模型回答时，才允许一次技术 retry，并保留失败记录。

回答质量差、格式错、插件没按预期工作都属于真实测试结果，不得重跑到成功。

## 9. 最终交独立 Reviewer

执行结束后生成：

- `RESULT.md`
- `FINAL_REVIEW_INPUT_MANIFEST.md`

Reviewer 必须实际读取：

- W0 全部 raw outputs；
- W1 全部多轮输出；
- W2 两 arm、blinded judgments、reveal map；
- W3 evidence；
- freeze manifest；
- attempt/retry log；
- exact comparisons。

Reviewer 分开给：

- PROCESS / IDENTITY；
- W0 PRODUCT SAFETY；
- W1 PROJECT_POLICY_BEHAVIOR_RELIABILITY；
- W2 PLUGIN_INCREMENT PASS / FAIL / INCONCLUSIVE；
- W3 diagnostic。

Reviewer 不得把 W1 写成 plugin causality，不得用 confounded W2 给 PASS。

如果 W0/W1/W2 全 PASS，停止于 `READY_FOR_G7_FREEZE`，不要自行进入 G7。
