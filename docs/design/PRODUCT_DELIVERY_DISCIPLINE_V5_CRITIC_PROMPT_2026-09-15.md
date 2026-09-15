你是 AI Research Stack 的长期独立 Critic thread。

当前审查对象：

- Repository: `YuukiAS/AI_Skills_Collection`
- Proposal: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md`
- 当前阶段：方案执行前独立审查

你只做审查，不实现 production skill，不修改 Bridge Kit，不修改 Bobbio/Lucerna/Mica/Asteria/SeminarArc AGENTS，不启动 Executor，不调用 paid API。

首先实际读取最新 main：

- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `AGENTS.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md`
- `docs/plugin-todos/workflow-core.md`
- `docs/plugin-todos/web-development.md`
- `docs/plugin-todos/ai-skills-core.md`
- `docs/plugin-todos/scientific-visualization.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/task-template.md`
- `skills/core/codex-system/codex-workflow-protocol/references/verification-matrix.md`
- `skills/core/codex-system/codex-workflow-protocol/references/live-state-delegation.md`
- `skills/tools/frontend/figma-design-to-code/SKILL.md`
- `skills/tools/frontend/design-system-tokens/SKILL.md`
- `skills/tools/frontend/visual-direction/SKILL.md`

再独立读取必要的真实项目依据：

- `YuukiAS/Lucerna` 当前 main `AGENTS.md`，并检查最近 `01033_openai_usage_monitor_shared_vault` 相关 commits/result，确认“用户输入前的实现/测试 checkpoint”与“用户操作后继续暴露 unfinished integration”之间的真实边界；
- `YuukiAS/Bobbio` 当前 develop `AGENTS.md`、`docs/PRODUCT_DESIGN_BRIEF.md`、`docs/design/FIGMA_HANDOFF.md`；
- `YuukiAS/Mica-for-ChatGPT` 当前 main `AGENTS.md`；
- `YuukiAS/Asteria` 当前 main `AGENTS.md`、`prompts/AGENT_RULES.md`，以及 canonical scientific graph visual system / developer visual self-QA 的入口；
- `YuukiAS/GPT_Codex_AI_Bridge_Kit` 当前 main 的 `templates/host/GLOBAL_AGENTS_SNIPPET.md`、`templates/host/CODEX_CONFIG_PROFILE.md` 及 request-user-input / wait-resume 相关实现/测试证据。

用户这轮明确纠正了两个不能混淆的目标：

1. **所有 agent 自己能完成、测试、看出来、修掉的工作必须先彻底收口，再让 GPT Work 或用户验收。** 禁止 `做一点 -> 验收 -> 暴露开发者本可发现的问题 -> 返修 -> 再验收`。中途用户不可替代的 credential/login/OS 授权动作不等于开始产品验收；应当先完成所有不依赖该动作的实现/错误处理/测试/设计/diagnostics，并在用户动作后由 agent 自动继续闭环，直到形成真正 review-ready candidate。
2. **Goal 中可预见需要用户操作时，必须使用持续、阻塞、非过期的 prompt。** 用户不回应就不能继续依赖链；不能把短暂 toast/普通进度消息当 prompt，不能静默轮询，不能因为等待时间到就自动消失、失败或 terminal BLOCKED。只需要一个 pending prompt，不要周期性提醒 daemon。

还需审查 Frontend Design 方向：

- 有 canonical Figma/design 时，production state 缺失必须先改设计，再实现；不能在代码里自己画圆、加按钮、箭头、card、pill、CTA 或发明另一套 spacing/component grammar；
- design 正确、implementation 偏离时只修 implementation；必要 platform/accessibility deviation 应先反馈设计源并形成一致决定；
- generic UI icon 应来自项目既有 canonical icon family、platform-native system 或成熟维护库；不要随手画 ad-hoc SVG / random dots / placeholder emoji；brand/domain-specific exception 需有理由；
- icon/motion 必须统一，但请重点审查 Planner 是否正确拒绝了“所有图标一律动画”的机械规则：成熟平台通常只在 interaction/state transition 时使用 icon animation，static/status/brand icon 不应为动而动；
- layout/style/component/motion 改动要做 system-wide consistency 检查，不能只修当前截图里的一个实例；
- external visual review 和用户验收必须在 producer-local actual-surface whole-product QA 收口后进入。

你必须独立做针对性网页研究，至少核查：

- OpenAI 关于 agent harness / AGENTS / human attention / self-review 的成熟经验；
- Figma 关于 developer handoff、components/variants/states/styles source-of-truth 的官方实践；
- 至少一个成熟平台关于 icon animation / interaction feedback 的官方指导。

不要只复述 Planner 的链接。

重点回答以下问题：

A. v5 是否真正解决了用户最核心的“不要把半成品端上来让我/GPT Work反复验收”的问题，还是只是换了术语？
B. `Pre-Human Readiness / Review Admission Gate` 是否足够强，又会不会把普通小任务搞得过重？如何限定触发范围？
C. “persistent blocking prompt”在现有 Codex/Bridge Kit 中是否真实可实现？哪些是已验证事实，哪些仍需 capability probe？如果现有 runtime 做不到，最小合法 fallback 是什么？不得发明新 watcher/state machine 作为默认答案。
D. Goal authoring 是否必须显式识别 foreseeable human action？应写哪些最小语义，避免把 task template 变成字段泥潭？
E. human action 与 final acceptance 的区分是否清楚？用户完成 secret/login/授权后，谁负责继续、测试、收口？
F. workflow-core 的 12 项候选是否过多、重复或遗漏？能否收敛成更少的真实 capability，而不是 checklist wall？
G. Frontend Design 的 F1–F5 是否机制正确？哪些现有 TODO 已覆盖，应合并而不是新增？
H. 用户“所有图标必须配动效、来自成熟库”的目标应该怎样专业化表达，既防 ad-hoc SVG/粗糙 icon，又不引入无意义动画？
I. “layout/style必须统一”怎样验证才不是关键词/截图特判？设计系统、tokens、shared components、whole-screen comparison 应如何配合？
J. Repo-specific 建议是否遵守“只有项目独有不变量进 AGENTS；通用规则不上各 repo 重复复制”？
K. Lucerna / Bobbio / Mica / Asteria 的建议中，哪些其实已有 active rule，应优先做 consumer/execution replay 而非再加文档？
L. 是否需要 SeminarArc design-source locator？在没有 repo 证据前 Planner 是否保持了正确的不确定性？
M. Capability Gate Matrix 是否能直接证明最终用户少被折腾，而不是只证明多了规则文件？
N. 是否有更简单但同样有效的替代架构？如果有，请作为 blocker 或非阻塞建议说明。

审查必须同时防两个方向：

- **过简**：继续允许半成品、proxy PASS、反复真人 QA；
- **过重**：所有任务都强制 Figma、GPT Work、全套 E2E、额外 schema/state/reviewer。

每条阻塞意见给稳定编号，并写：对应用户要求/合同、证据、因果风险、最小关闭条件和 owner。偏好建议与 blocker 分开。

最终给出：

```text
RESULT = PASS | REVISE
REVIEW_OBJECT = PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md
READY_FOR_IMPLEMENTATION_PLAN = YES | NO
```

如果 `REVISE`，按 Critic contract 自动附一段可以直接发回 Planner thread 的完整 prompt。

如果 `PASS`，只表示方案可以进入“冻结具体 implementation Goal/Kickoff”阶段；不代表 production plugin、Bridge Kit、任何 repo AGENTS 已经修改或通过验收。