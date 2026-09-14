# workflow-core — Long-Term TODO

Canonical maintenance inbox for the `workflow-core` plugin.

## Open candidates

### Keep AI_Skills workflow rules separate from Bridge Kit runtime bugs
status: PROMOTE_NOW
source: 042/043 Reviewed Handoff pause; 044 writing-style production replay
evidence: AI_Skills validation previously exposed a stale-review/implementation binding blocker for 042; task 044 then exposed a second generic runtime problem when an otherwise authorized plugin replay had to launch a fresh `codex exec` on a private local artifact and the Host Policy approval reviewer stopped it before the plugin could be tested. The generic runtime source of truth is `YuukiAS/GPT_Codex_AI_Bridge_Kit`; the bounded Host Policy design is now recorded there in `docs/design/host_policy_plugin_replay_authorization.md`.
target layer: external-runtime
problem: project workflows can be tempted to patch local history, add project-specific approval exceptions, or duplicate generic Reviewed Handoff / Host Policy runtime code when the defect actually belongs to Bridge Kit. Plugin-repair tasks also need a stable production-replay path; raw nested `codex exec` should not become an ad hoc per-task approval negotiation.
candidate action: keep generic validator and Host Policy fixes in Bridge Kit. For plugin production replay, use the Bridge-owned bounded replay path once implemented, rather than broad raw `codex exec` allow rules or AI_Skills-local Host Policy copies. After the Bridge Kit behavior is stable, make the AI_Skills Executor guidance prefer that path for plugin-repair replay without changing Planner/Reviewer authority.
promotion gate: Bridge Kit regression proving legal `PLANNER_DECISION` terminalization where relevant, plus a generic plugin-replay smoke showing an explicitly selected private local input can be processed by a fresh production Codex/plugin runtime and written to a local private replay directory without repeated approval, while dangerous Git/branch/remote actions remain protected.

### Real-task-driven Reviewed Handoff batches
status: PROMOTE_NOW
source: user decision after presentation Stage-5 loop
evidence: `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
target layer: routing/qa
problem: an automation can become an endless synthetic recovery chain even after the product has reached a useful baseline.
candidate action: require explicit real blocker / plugin TODO source for long-running refinement batches and stop the watcher when the batch is closed or user redirects to real workflow refinement.
promotion gate: apply to the next AI_Skills maintenance batch without creating a second state machine.

### 普通产品开发的人工交互、真实交付与重复失败止损
status: NEW
source: 2026-09-14 用户对 Bobbio、Lucerna、Mica、SeminarArc 的跨项目反馈，以及附件 Lite Handoff Completion Discipline 初稿
evidence: [完整修订提案与证据边界](../design/PRODUCT_DELIVERY_DISCIPLINE_V2_2026-09-14.md)；Lucerna `AGENTS.md` 的 Windows release interaction / matching regression 规则（读取 blob `3ecb67774716355856a7a62c1eea25f164a079ef`）；Mica `AGENTS.md` 的 focused-test / manual acceptance 规则（读取 blob `730bb886aa55639663a2f5b2ce735e549d42d593`）；[Frontend Design 既有真实反馈](web-development.md)。对话检索仅得到部分片段，不声称取得完整 thread 或完成现场产品复验。
problem: 需要用户动作时不显式询问，明显可自检的问题却反复叫用户验收；以构建、模拟测试、局部截图和自审替代真实使用路径；每轮修复缺少准确回归，重复运行没有新增证据。部分仓库已有正确规则，仍需确认实际调用、候选构建和执行入口，不能先断言均由已加载的 workflow-core 导致。
project-specific context: Lucerna 的关闭隐藏到托盘与真实额度、Bobbio 的 Windows/Zotero 边界、Mica 的真实 Edge 禁止动作、SeminarArc 的模拟器与设备限制都留在项目内；不把具体 UI 或账户权限变成通用规则。

维护者处理要求（尚未实施）：

- 先检查 active `codex-workflow-protocol`、verification / live-state references、Lite 模板及项目已有规则；已有非完成/证据规则按执行回归处理，不再增加同义口号。通用工作流负责何时要求专业证据，不接管专业设计判断。
- 只缺用户动作时，通过实际可用的交互通道发出最小明确请求，保存恢复点；无专用输入工具就可见消息暂停依赖步骤。不得静默轮询用户，也不得复问同范围已获授权。不能把 repo 计划当作新的操作授权。
- 当前 active skill 的 `blocked` 允许表示缺外部条件/用户决定，与初稿“绝不能 BLOCKED”存在语义差别。先统一行为并映射现有状态，禁止自行增加状态/schema 或使现有 validator 失配。
- 为新增功能、行为变化和 bug 修复要求同批针对性测试；旧失败回放需忠实，间歇故障采用适当证据，不危险回退真实系统。自动化测试与原生/真实服务证据互补，不能相互冒充。
- 诊断请求与最终验收分开；再次请用户试之前必须出现新增故障证据、修复依据和针对性回归。用户已要求止损时，不再启动真人测试循环。
- 同类失败复现或无信息重跑时先核对候选版本、故障假设、fixture 忠实性和规则是否实际加载；复用现有有限尝试预算，停止失败路线而非无理由冻结所有独立工作。
- 交付要核对原目标、对应环境/版本、完整使用路径、关联既有行为、真实数据、设计质量和剩余条件；不能增加原任务未要求的付费审阅、真人验收或全仓检查。
- Lite/AGENTS 保留不依赖插件加载的短底线；完整流程由 Verified Workflow 按需提供。工具真的无法提供交互/恢复或模板分发有缺陷时归 Bridge Kit；不在此复制运行时、审批或 watcher。
- 设计完整性、Figma 往返和整屏质量继续由 Frontend Design 既有 TODO 拥有，见 `web-development.md` 的 canonical design / design-to-code 条目；不在两处维护第二份设计规范。

进入实施前的回放要求：从实际安装与触发入口证明缺用户动作会明确请求、同授权不复问、模拟通过不被写成原生通过、新功能和修复有匹配测试、无信息重复会止损。还须证明纯文档、只读诊断、正常 Lite 任务不会被升级成多角色/付费/全套真机验收。静态检查规则文本存在不是行为 PASS。项目原生/账户验证仍须单独获授权。

## Do not do

- Do not duplicate Bridge Kit core Reviewed Handoff implementation in this repo.
- Do not use workflow-core to make domain judgments for writing, Presentation, statistics or imaging.
