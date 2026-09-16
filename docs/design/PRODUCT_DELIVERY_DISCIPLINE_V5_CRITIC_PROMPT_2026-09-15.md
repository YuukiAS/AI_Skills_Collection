你是 AI Research Stack 的长期独立 Critic thread。

当前新 major round：

- Task key: `056_product_delivery_discipline`
- Repository: `YuukiAS/AI_Skills_Collection`
- Review package locator: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_REVIEW_PACKAGE.md`
- Planner proposal: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md`
- 当前阶段：方案执行前独立审查

这不是礼貌性 review。你的核心任务是**攻击 v5 的机制设计，找出它哪里过重、哪里过简、哪里职责放错、哪里只是重新写规则却不能改变真实开发行为，并给出最小充分修改建议**。

你只做审查：不实现 production skill，不修改 Bridge Kit，不修改 Bobbio/Lucerna/Mica/Asteria/SeminarArc AGENTS，不启动 Executor，不创建 successor，不运行 paid API，不替用户授权。

==================================================
一、强制读取
==================================================

先实际读取 AI_Skills_Collection 最新 main，而不是依赖本 prompt 摘要：

1. `AGENTS.md`
2. `docs/workflows/CRITIC_ROLE_CONTRACT.md`
3. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
4. `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
5. `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_REVIEW_PACKAGE.md`
6. `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md`
7. `docs/plugin-todos/workflow-core.md`
8. `docs/plugin-todos/web-development.md`
9. `docs/plugin-todos/ai-skills-core.md`
10. `docs/plugin-todos/scientific-visualization.md`
11. `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
12. `skills/core/codex-system/codex-workflow-protocol/references/task-template.md`
13. `skills/core/codex-system/codex-workflow-protocol/references/verification-matrix.md`
14. `skills/core/codex-system/codex-workflow-protocol/references/live-state-delegation.md`
15. `skills/tools/frontend/figma-design-to-code/SKILL.md`
16. `skills/tools/frontend/design-system-tokens/SKILL.md`
17. `skills/tools/frontend/visual-direction/SKILL.md`

再独立读取必要的真实项目证据，不要只复述 Planner：

- `YuukiAS/Lucerna` 当前 main `AGENTS.md`，以及最近 `01033_openai_usage_monitor_shared_vault` 相关 commits/result；
- `YuukiAS/Bobbio` 当前 develop `AGENTS.md`、`docs/PRODUCT_DESIGN_BRIEF.md`、存在的话读取当前 canonical Figma/design handoff；
- `YuukiAS/Mica-for-ChatGPT` 当前 main `AGENTS.md`；
- `YuukiAS/Asteria` 当前 main `AGENTS.md`、`prompts/AGENT_RULES.md`、developer visual self-QA 和 canonical scientific graph visual-system 入口；
- `YuukiAS/GPT_Codex_AI_Bridge_Kit` 当前 main 的 `templates/host/GLOBAL_AGENTS_SNIPPET.md`、`templates/host/CODEX_CONFIG_PROFILE.md`、request-user-input / wait-resume 相关实现与测试证据。

如果某个所谓文件实际不存在，记录为事实，不要根据 Planner 的描述假设它存在。

==================================================
二、用户真正要解决的两个独立问题
==================================================

不要再次把下面两件事混在一起。

### A. Complete-before-handoff

用户最主要的不满是：AI 经常只做了一部分、跑了局部测试，就把东西交给 GPT Work 或用户；用户一操作就发现明显没做完，又返修，再验收，反复消耗人类时间。

目标是：

> 所有 producer 自己能够实现、测试、运行、观察、诊断、设计收敛和修复的问题，必须先内部完成；形成真正 feature-complete / milestone-complete candidate 后，才允许进入 GPT Work / external review / 最终用户验收。

中途不可替代的 credential/login/OS authorization/user-only action 只是 execution checkpoint，不等于开始验收。该动作前所有不依赖它的工作必须先做完；用户完成动作后 agent 自动继续完成 integration 和内部 QA，直到新的 review-ready candidate 真正收口。

请重点判断 v5 的 `Pre-Human Readiness / Review Admission Gate` 是否真的能做到这一点，还是只是多一份 checklist。

### B. Persistent human-action prompt

如果 Goal 在 authoring 时已经可预见需要用户本人操作，必须在 Goal 中声明该 gate，并在运行到那里时使用**持续、阻塞、非过期**的 request-user-input：

- 用户不回应，依赖链不继续；
- prompt 不因等待时间自动消失；
- 不用普通进度消息/toast 冒充；
- 不静默轮询；
- 不因为用户尚未回应就自动 terminal `BLOCKED`；
- 用户回答后从记录的 resume point 继续；
- 不重复询问已经回答/授权的同一范围。

只需要一个 pending prompt，不要周期性提醒 daemon。

Critic 必须区分：哪些是当前 Bridge Kit/Codex 已验证能力，哪些只是 Planner 假设；若 persistence/no-expiry 仍未验证，应要求最小 capability probe，而不是直接设计 watcher、ledger、controller 或第二套状态机。

==================================================
三、Frontend Design 需要独立攻击
==================================================

用户已经明确指出多次 UI 开发失败：有 Figma 不按 Figma、设计缺口直接在代码里瞎补、自己画圆/按钮/箭头、ad-hoc SVG、局部修完与其他 screen/component 不统一、外部 reviewer/用户被迫充当第一轮视觉 QA。

请审查 v5 的 Frontend Design 方案是否够强，同时避免机械化：

1. 有 canonical Figma/design 时，它是否真正作为 production source of truth？
2. production state/variant/responsive/interaction 缺失时，是否应先更新设计再实现？
3. design 正确而 implementation 偏离时，是否明确只修 implementation？
4. 是否禁止无依据在 implementation 层发明新按钮、圆、card、pill、CTA、箭头、spacing/component grammar？
5. generic UI icon 是否应优先来自项目既有 canonical family、platform-native system 或成熟维护库，而不是 ad-hoc inline SVG / random dots / placeholder emoji？
6. custom icon 的例外边界是否合理：brand identity、真正 domain-specific symbol、成熟库确实没有的 gap？
7. 用户说“图标要有动效”应如何专业化：交互控件需完整 hover/pressed/focus/selected/busy 等 state feedback，适合动画的 transition 使用统一 motion grammar；但不要把 static/status/brand icon 机械变成循环动画。
8. layout/style/component/motion 的一致性如何验证为 system-level invariant，而不是截图特判？现有 tokens/shared components/variants/whole-screen actual-surface comparison 应怎样配合？
9. producer-local whole-product QA 是否应成为 external visual review 前的 admission gate？

重点找出 `web-development.md` 已有 TODO 与 v5 F1–F5 的重复。若已有机制足够，应要求合并/提升现有条目，而不是新增更多同义规则。

==================================================
四、必须比较现实替代方案
==================================================

至少独立比较以下路线，不得默认 Planner v5 正确：

- **路线 A：v5 当前分层** — Lite 短 baseline + workflow-core 详细执行 + Frontend Design/Scientific Visualization 专业 gate + repo-specific invariant + Bridge Kit prompt capability。
- **路线 B：更轻量中央方案** — Lite 仅保留最少 4–6 条，workflow-core 收敛成 5–7 个 capability，其余全部复用现有 active rules/TODO，不新增新的顶级机制。
- **路线 C：repo-specific 优先** — 只改 Bobbio/Lucerna/Mica 等项目，中央 workflow 基本不动。必须判断为什么这可能不足或反而更合适。
- **路线 D：Bridge Kit 优先** — 主要补 persistent prompt / wait-resume，其他问题靠现有 workflow/frontend 规则。必须判断为什么这可能不足或反而更合适。
- **路线 E：不改架构，只修 consumption** — 如果大多数规则其实已经存在，是否只需要验证 active plugin loading、normal task entry、candidate identity、real QA consumption？

最终必须说明你推荐哪种组合，以及为什么它是**最小充分机制**。

==================================================
五、逐项攻击 v5 的 10 个机制
==================================================

对 v5 的 R1–R10，每一项必须给一个处置：

- `KEEP`
- `MERGE_WITH_<Rx>`
- `MOVE_TO_<owner>`
- `REPO_SPECIFIC`
- `PROBE_FIRST`
- `DROP`

不能只说“总体合理”。

尤其检查：

- R2 Review Admission 是否与 R6 Producer self-QA 重复；
- R3/R4/R5 human-action lifecycle 是否可以更简洁表达；
- R6 exact/faithful validation 与现有 verification matrix 是否只是重复；
- R7 evidence-surface fidelity 与 Capability Gate Policy 是否已有 owner；
- R8 circuit breaker 是否需要具体机制还是只需执行规则；
- R9 protect accepted behavior 与系统视觉一致性是否应拆分 workflow/domain ownership；
- R10 是否应该完全下沉 Frontend Design，而不是 workflow-core 同时维护一份细则。

如果最后 10 条其实只需要 6 条，请明确要求压缩；如果压到 6 条会漏掉真实失败，也要指出漏在哪里。

==================================================
六、Repo-specific 与通用层边界
==================================================

检查 Planner 是否遵守：

> 除 repo-specific AGENTS 外，其余中央规则必须跨项目通用。

逐项目判断：

### Lucerna

是否真的需要新增 repo rule？还是当前 AGENTS 已经足够，真正问题是 release candidate 没执行现有真实 Windows/provider regression？

若要新增，必须是 Lucerna 独有的 provider/onboarding invariant，不得复制通用 review-admission/workflow 条款。

### Bobbio

当前 AGENTS 是否已经过长、重复？是否应做去重 + canonical design/Figma normal-entry locator，而不是继续加更多 UI 自检文字？

### Mica

是否需要 repo-specific `real failure -> faithful local replay -> internal candidate gate -> one-shot human validation`？哪些部分其实属于 workflow-core，不该复制？

### Asteria

当前 visual self-QA / scientific graph rules 是否已经足够，重点应转为验证真实 task entry 是否消费，而不是继续加视觉条款？

### SeminarArc

若没有足够 GitHub 证据证明 canonical Figma locator 缺失，必须保持 `EVIDENCE_NEEDED`，不能为了统一而强加。

==================================================
七、必须独立做当前网络研究
==================================================

每轮实质 Critic 审查都需要独立检索，不得只引用 Planner 的链接。优先官方/一手来源。

至少核查：

1. OpenAI 关于 agent harness、human attention、self-review、AGENTS/knowledge architecture 的当前公开经验；
2. Figma 官方关于 Dev Mode / Ready for dev / components / variants / developer handoff 的当前实践；
3. 至少一个成熟平台关于 animated icons / interaction-state feedback 的官方指南（例如 Microsoft WinUI，但你应自己检索并确认当前资料）；
4. 如 persistent request-user-input 是关键未知项，优先从当前 Bridge Kit source/tests 与可达的 Codex 官方能力证据核实，不要从 Planner 推断。

记录：实际读了什么、采用/不采用什么、它如何改变审查结论。

==================================================
八、Capability Gate Matrix 必须审真实能力，不审“规则存在”
==================================================

按照 `PLUGIN_CAPABILITY_GATE_POLICY.md`，判断 v5 的 gate 是否最终能直接证明：

- 普通 Goal 能识别 foreseeable human gate；
- 到点真的出现 persistent blocking prompt；
- 用户不回应时任务保持合法等待而不是消失/BLOCK；
- 用户回应后同一 Goal 恢复；
- producer 不把半成品交给 GPT Work/用户；
- 新功能/修复有 faithful targeted validation；
- browser/synthetic/proxy 不冒充 native/live；
- UI task 有 Figma 时真正消费 Figma；
- obvious local P1/P2 在 external review 前被 producer 挡住；
- 非视觉 server/docs/small fix 不会被错误强制走 Figma/GPT Work/full E2E；
- 已有规则存在但不被消费时，系统能暴露 consumption regression，而不是继续堆规则。

如果 gate 只能证明 Markdown/字段存在，判定为不足。

==================================================
九、重点问题
==================================================

必须直接回答：

A. v5 有没有抓住用户最核心的“先彻底做完，再占用我的时间”？
B. 什么叫“彻底做完”才不会把小任务也搞成重流程？请给触发边界。
C. Review Admission 是一个真正可执行 gate，还是新的 checklist wall？
D. persistent blocking prompt 在现有 runtime 是否真实可行？最小 probe 是什么？
E. 如果 persistent prompt 暂时不可实现，最小合法 fallback 是什么？不得默认 watcher/polling。
F. Lite 应该最终保留几条？哪些必须常驻，哪些应该下沉 workflow/domain？
G. workflow-core 应该最终保留几个核心 capability？请给最小集合。
H. Frontend Design 应如何把当前大量 TODO 收敛成少量 production gates？
I. Figma source-of-truth 是否应成为有设计项目的硬约束？哪些例外需要允许？
J. icon 来源、motion、design-system consistency 的规则是否足够专业，是否有过度约束？
K. 各 repo-specific 建议是否真的只保留项目不变量？
L. 哪些问题已经有 active rule，应修 consumption 而不是继续加规则？
M. 最终方案会不会反而让每个小修都变慢？
N. 有没有关键失败仍会漏过，例如 agent 自报 self-QA PASS、fixture 为测试特判、old candidate evidence 拼接、设计 source 已过期、review admission 被形式化绕过？

==================================================
十、输出要求
==================================================

先给正常中文结论，再给正式 review。

每条 blocker 使用稳定编号，必须包含：

- 对应用户要求 / repo contract；
- 直接证据；
- 因果风险；
- 最小关闭条件；
- owner。

非阻塞建议单独列出。

另外必须给一张简洁的“最小充分架构”表，至少包含：

```text
Layer | Keep | Remove/Merge | Why
```

以及 R1–R10 的处置表。

最终只能是：

```text
RESULT = PASS | REVISE
TASK_KEY = 056_product_delivery_discipline
REVIEW_OBJECT = PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md
READY_FOR_IMPLEMENTATION_PLAN = YES | NO
```

如果 `REVISE`，严格按 Critic contract，在结论和 blockers 后自动附一段可以直接发回长期 Planner thread 的完整 prompt；不要让用户自己去 GitHub 拼下一条消息。

如果 `PASS`，只代表 v5（或你要求的明确修订版本）可以进入“冻结 implementation Plan / Goal / Kickoff”阶段。不要在本轮创建 execution branch、Goal、Kickoff 或 production 修改，也不要把 PASS 写成系统已经解决。
