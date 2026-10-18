# Clear Writing invocation-policy / Web Gate revision — 独立 Critic Review v0.2

日期：2026-10-18  
审查阶段：proposal v0.2 re-review after REVISE  
审查对象：`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md`  
Proposal commit：`1f905d294c3c2e5b0951c9d5e818c285d236cef7`  
上一轮 Critic review：`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_CRITIC_REVIEW_V0_1_2026-10-18.md@8e01bb693e6b8e6285f1acf0a49a85f3419cd442`  
Frozen production candidate：`fd7a1578a5042a46a55c5b638f6d550655b1096b`

## Decision

**PASS**

本轮只复核 `CW-IP-01`、`CW-IP-02`、`CW-IP-03` 以及 v0.2 对既有已认可方向的影响。没有重新审六技能架构、`response-clarity` 已通过的内容质量、KR-WEB-01..09 或四组 should-not-change。

## External reality check

2026-10-18 再次核对 OpenAI 当前官方资料：

- Skills in ChatGPT：已安装 Skill 可以在“有帮助时”自动使用，surface 的 availability / installation / syncing 可以不同；
- Developers / Skills activation：模型先看到 Skill metadata；只有请求匹配或用户直接调用时才加载完整 instructions；
- Plugins in ChatGPT：已安装插件在请求相关时自动使用，也可以用 `@` 或 composer 直接选择；
- Projects in ChatGPT：Project instructions 只在对应 Project 内生效并覆盖 global custom instructions；Project memory mode 会影响同 Project chat history 的可见范围；
- Custom GPT retirement / migration FAQ 进一步明确：相关 Skill 可能自动使用，但 plugin 不一定在每个请求上运行。

未发现普通 ChatGPT Web 可公开依赖的 every-response pre-send Skill finalizer hook。因此上一轮对“Project policy 必须真实 Web 验证、不能把 automatic selection 当每轮保证”的判断保持成立。

## Finding closure

### CW-IP-01 — CLOSED

v0.2 已把强调用范围改成：

- natural-language final response；
- mixed natural-language + machine-payload final response。

Pure JSON/YAML/code/command/raw log/verbatim/exact machine output 明确成为 **activation exemption**，不为了形式上的“每轮调用”强制加载 Clear Writing。

Mixed task 仍由匹配的既有 writing Skill 处理解释层，并要求机器 payload 精确保留。

v0.2 还正确收窄 W0 exact-only stress 的 claim：

- `@Clear Writing` / plugin-level selection 后 exact output 仍必须不受污染；
- 若当前 surface 只能证明 plugin-level selection，不能证明具体 Skill full instructions 被加载，则只能声称  
  `PLUGIN_SELECTION_DOES_NOT_CONTAMINATE_EXACT_OUTPUT`；
- 不得升级成 loaded-skill bypass PASS。

因此不再存在“没有 coordinator，却声称由 Clear Writing 自己执行全局 bypass”的 ownership 循环，也没有新增第七 coordinator。

### CW-IP-02 — CLOSED

W1 的正式 claim 已改成：

`PROJECT_POLICY_BEHAVIOR_RELIABILITY`

v0.2 明确：

- 用户无需每轮手工 `@`；
- 多轮最终行为必须持续满足 route、exact exemption、语言恢复和 sibling switching；
- surface 有 invocation/load evidence 时必须记录；
- 没有 evidence 时禁止靠模型自述或最终文字推断 plugin 已加载；
- W1 PASS alone 不证明 plugin causality；
- plugin incremental causality 只由 W2 matched comparison 关闭；
- W1 FAIL 仍足以说明 Project-setting policy 作为正常入口不可靠。

行为可靠性与 plugin causality 已正确分离。

### CW-IP-03 — CLOSED

W2 已改成严格的 release-critical matched evidence。

Treatment / Control 冻结条件包括：

- Project-setting exact bytes 相同；
- same ChatGPT surface；
- same model；
- same pre-frozen task set；
- same task-order policy；
- same attempt budget；
- same rubric；
- same evaluation procedure；
- fresh isolated conversation context；
- 两 arm 不得读取彼此输出、conversation 或 Project history。

若使用 Project，必须冻结并记录 Project memory mode，并采用防 cross-arm contamination 的测试结构。

唯一允许的实质差异已明确为：

`Clear Writing candidate availability / consumption`

Control 明确禁止复制 Skill 正文、根据 treatment 输出补规则或模拟 Clear Writing。

v0.2 同时禁止挑赢家、重复到成功、中途改 rubric、看完一 arm 再改另一 arm 任务、改变 task-order policy 或切换 model/surface。

无法合法建立 matched condition 时，强制：

`W2=INCONCLUSIVE`

并停止 release；已知有混杂的 fallback 只能是 `DIAGNOSTIC_ONLY`，不能代替 plugin incremental-value PASS。

G7 freeze identity 也已补齐：production candidate、actual Web plugin/release identity、Project bridge exact bytes、surface/model、Project memory mode、conversation isolation、attempt budget、fresh task set、task-order policy、W0/W1/W2 rubric、Reviewer input 和 stop condition 均需预冻结。已知回归、旧 controls、W0/W1/W2 及调试样本永久排除 fresh G7。

## Change-impact check

v0.2 没有破坏上一轮已认可方向：

- Project-policy normal entry 仍是待真实验证的主要路线；
- W0 -> W1 -> W2 -> W3 顺序保持；
- W3 仍是 non-release-critical discoverability/fallback diagnostic；
- fresh G7 仍是最终 generalization Gate；
- 六技能职责不变；
- `fd7a1578a5042a46a55c5b638f6d550655b1096b` 不变；
- 没有新增 Skill/router/state machine；
- pure exact-only 没有被重新强塞回 Clear Writing。

## Scope and claim boundary

本 PASS **只批准** Clear Writing invocation-policy / Web Gate design v0.2。

本 PASS 不代表：

- Project setting 已修改；
- W0/W1/W2/W3 已执行或 PASS；
- every-turn behavior 已真实 Web 验证；
- plugin incremental value 已证明；
- G7 已 PASS；
- 用户验收已 PASS；
- release 已完成。

下一步只能由 Planner 基于本 PASS 冻结 Web Gate execution package。该 execution package 在正式执行 W0/W1/W2/W3 前仍不得修改 production candidate、Project setting、ChatGPT account/personal plugin 或 Reviewed Handoff machine state；任何需要 live Project/account/plugin mutation 的步骤必须在 execution-ready review 与用户实际授权之后发生。

Issue #13 继续作为 canonical tracking Issue，保持 `DOING / area:writing-style`。本 PASS 不机械改变 Project Status。