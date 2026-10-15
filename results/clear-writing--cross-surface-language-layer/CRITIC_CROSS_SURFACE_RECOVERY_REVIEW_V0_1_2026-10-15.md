# Clear Writing 真实网页回归与 CI 恢复 v0.1 — 独立 Critic 审查

- 审查阶段：execution-ready recovery amendment
- 仓库：`YuukiAS/AI_Skills_Collection`
- 插件：`writing-style / Clear Writing`
- 任务：`clear-writing--cross-surface-language-layer`
- 执行分支：`reviewed/clear-writing--cross-surface-language-layer`
- 审查包提交：`ac44e1cf07df08e9042bfc53e2b2ab79ec4871ad`
- 当前实现：`cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`
- 进入本轮时：`NEEDS_GPT_PLANNER / ci_status=FAIL / review_round=1 / plan_revision=0`
- 决定：**PASS**
- 本 PASS 只批准 recovery package；不代表 ChatGPT Web、G7、PIE 0.2、Research Authoring、Presentations Web 包装或正式发布 PASS。
- 本 Critic 不修改 `CURRENT.json`；下一步必须先回 Planner 完成唯一一次合法 re-plan freeze。

## 1. 审查对象

同一提交上的冻结恢复包：

- `docs/design/clear-writing/CROSS_SURFACE_RECOVERY_PLAN_V0_1_2026-10-15.md`
- `docs/goals/CLEAR_WRITING_CROSS_SURFACE_RECOVERY_GOAL_V0_1_2026-10-15.md`
- `docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_RECOVERY_KICKOFF_V0_1_2026-10-15.md`
- `results/clear-writing--cross-surface-language-layer/REAL_WEB_REGRESSION_BANK_V1.md`
- `docs/design/clear-writing/CROSS_SURFACE_RECOVERY_CRITIC_PROMPT_V0_1_2026-10-15.md`

已重新读取 latest main 的仓库规则、Planner/Critic 合同、Capability Gate、writing-style TODO、PIE TODO、维护看板；并读取当前 task 的 REQUEST/PLAN/CURRENT、REVIEW_1、2026-10-13 Planner recovery 和 Critic recovery boundary。Reviewed Handoff 规则按 Bridge Kit latest main `69fe05897b3f5d537dceca8ed41a8874aa53e101` 复核。

## 2. 七项定向结论

### 2.1 五个真实 Web 案例：PASS

RW-WEB-01..05 被明确冻结为 development / known regression，且永久排除 G7 fresh/unseen。RW-WEB-03 是正向控制，要求保留例子、因果解释和不确定性，足以阻止把“清晰”错误实现成固定短答。

回归库按读者负担、信息增量、来源与建议分层、反馈意图等语义维度判断；没有用词数、英文比例、标题数量、箭头、代码框或固定长度做 PASS oracle。

### 2.2 保留 response-clarity，先 replay 再修：PASS

当前 `response-clarity` 已有正确产品边界：处理普通解释、诊断、建议、状态与结果说明；不拥有领域事实、科研判断、文档语义、UI 产品语义或机器协议。

恢复包先冻结现有 `cac70c3...` 候选的五例 baseline，再允许根据真实失败做 bounded repair；这比预先按已知样本加规则更能区分“现有架构已足够”与“确有通用缺口”。

Codex candidate replay 只能作为开发/路由证据，不得被描述为 ChatGPT Web 产品 PASS；恢复包已保留后续真实 Web A/E、B/C 和 G7 门槛。

### 2.3 禁止表面特判：PASS

Plan 明确禁止禁词表、英文比例、箭头/代码框禁令、固定标题/段落/行数、项目名特判和新 router。允许的修复是信息停止条件、格式复杂度与信息复杂度匹配、来源共识与助手建议分层、写作反馈意图识别，并保护正例中的必要解释。

### 2.4 CI 恢复没有降级验收：PASS

恢复仍要求 full repository tests、Marketplace generation/check 和同一 reviewed branch 的 required GitHub CI；不允许 narrow CI 替代、删除测试、隐藏 diff、标记 known failure、假升 `VERSION` 或把别的 branch PASS 拼进当前候选。

版本断言和 TODO 集合断言只允许修复过时的测试假设，同时保留测试对真实版本合同、中央插件清单和 changelog 的检测能力。

### 2.5 Presentations / Research Authoring generated-only parity：PASS，按以下严格含义解释

允许同步的不是“跨插件产品修改”，而是**现有正式生成器对当前 canonical source/config 的纯机械投影**。

必须同时满足：

1. 该恢复不编辑 Presentations / Research Authoring 的 `skills/**` canonical source；
2. 不改变这两个插件在 `scripts/codex_marketplace_config.json` 中的 source mapping、routing、版本、description/default prompt；
3. 不改 profile、changelog、README、专业规则或用户账户插件；
4. 生成差异必须完全由现有 `scripts/build_codex_marketplace.py` 对已存在 source/config 的确定性复制/聚合产生；
5. 提交前检查实际 diff，只允许对应 generated payload（以及由同一配置机械产生的 marketplace snapshot）发生变化；再次运行生成器应为 clean；
6. 若 source 与 generated 表现代表两个实质不同的专业行为、需要人为选择谁正确、或 regen 暴露任何 source/config 语义冲突，立即停止并回 Planner，不得把“generated-only”当授权绕过领域 owner。

现有 builder 的 copy 路线使用 source tree 直接复制，aggregate 路线由 config 中的 source skill 列表构建自包含 snapshot；因此上述“canonical source 已唯一决定结果”是现实可执行的机械条件，而不是抽象口号。

Research Authoring 个人 Web 插件当前存在 `research-authoring 0.3.1`，但此恢复不得以其个人插件内容反向覆盖仓库 canonical source；generated parity 只能消费当前 repo source/config。

### 2.6 同一 reviewed branch 普通 merge latest main：PASS

允许在五例 baseline packet 冻结后，将最新 `origin/main` 普通 non-force merge 到现有 reviewed branch。禁止 rebase/force/successor。

当前 branch 与 main 已明显 diverged，merge 是获得最新 TODO、规则和共享仓库修复的必要步骤。冲突若只是 task-owned Clear Writing 与最新 main 的可机械合并，可按 Plan 保留双方真实变化；若冲突要求在其他插件专业语义中二选一，停止回 Planner。

full CI PASS 前不应产生第二轮 Reviewer decision；当前 `review_round=1` 必须保留。

### 2.7 Goal / Kickoff 与 Plan：PASS

Goal/Kickoff 没有扩大到：

- ChatGPT 个人插件/账号修改；
- paid API；
- private transcript 提交；
- PIE 0.2；
- release/main merge；
- G7 fresh evaluation；
- Presentations / Research Authoring source-semantic 修改。

Kickoff 的执行权限只有在用户实际发送已审文本后才生效；Critic PASS 本身不代签执行授权。

## 3. Clear Writing / Research Authoring / Presentations 的长期边界

用户提出“三个插件以后都需要 Web + Codex 版本、各负责不同功能”的方向**成立**，但应理解为三种产品职责各自跨表面，而不是三套写作系统互相复制。

### Clear Writing

产品职责：**表达层与保真层**。

拥有：
- 普通聊天解释、结论、诊断、建议和状态说明的清晰度；
- 中文/英文读者表达；
- source-faithful 重写；
- 通用语言保真；
- 已冻结产品语义后的 UI microcopy。

不拥有：
- 科研文档该写哪些 claim/evidence；
- 论文/报告章节与引用 authority；
- slide/deck 故事线、页面结构、视觉布局和 renderer；
- 统计/领域科学判断。

Web 与 Codex 都需要它，因为两端都会产出 reader-facing text。两端应共享 canonical skill source，而不是各自维护不同写作原则。

### Research Authoring（`research-writing`）

产品职责：**科研文档语义与证据组织**。

拥有：
- audience / document purpose；
- claim-evidence spine；
- report/manuscript/literature/citation 结构；
- section jobs；
- table/figure/formula 在科研文档里的科学职责；
- citation/source authority；
- incremental document revision；
- document-level scientific QA。

不拥有：
- 通用“说人话”规则；
- 普通聊天最终表达；
- slide/deck page architecture；
- 低层 PDF/font/render mechanics。

Research Authoring 应在形成文档语义后调用/消费 Clear Writing 做 wording/fidelity，而不是复制一套中文/英文风格规则。

当前事实是：个人 ChatGPT 已有 PRIVATE `research-authoring 0.3.1`，其中包含 Research Authoring 技能和同源 Clear Writing support；而 latest main 的中央 Codex `research-writing 0.2` 尚没有计划中的 canonical `research-authoring-core`。这是 Research Authoring 自己的跨表面收口问题，不是本 Clear Writing recovery 要顺手解决的内容。

### Presentations

产品职责：**演示文稿语义、页面组织和真实视觉产物**。

拥有：
- deck purpose / audience；
- storyline；
- 每页承担的论证动作；
- 证据选择与 source fidelity；
- slide/page composition；
- research/business deck routing；
- editable artifact、render 和视觉 QA。

不拥有：
- 通用语言风格；
- 研究报告/论文文档结构；
- 把普通研究写作规则复制到 slide writer。

研究报告转 slides 时，Research Authoring 可以提供经过确认的 claim/evidence/source authority；Presentations 决定哪些内容进入 deck、怎样分配到页面以及如何视觉表达；Clear Writing 最终负责 slide copy 的自然表达与保真。三者是可组合的上下游 owner，不是互斥的三个“文本润色器”。

Presentations 未来做 Web + Codex 双表面是合理方向，但 Web 与 Codex 的 renderer/editable-artifact 能力可能不同。应保持一个 canonical Presentations product/skill source，通过 surface-specific adapter/packaging 消费，而不是维护两套不同演示方法论。

## 4. 外部产品现实核对

OpenAI 当前官方文档支持以下判断：

- Skill 先通过 name/description metadata 被考虑，完整指令在任务匹配时加载；安装后的技能可在相关任务中自动使用。
- Plugin 是 ChatGPT 与 Codex 可发现/安装的统一产品包，能够包含一个或多个 skills；同一个 plugin 的具体能力仍可能因 surface 不同而不同。
- Project instructions 在 Project 内优先于全局 custom instructions。

因此，“三个产品各自有 Web + Codex 消费表面”是可行方向，但不能从统一 plugin directory 推断两个表面的运行能力必然完全相同；脚本、renderer、文件编辑等必须分别实测。

## 5. 最终裁定

```text
REVIEW_STAGE=EXECUTION_READY_RECOVERY_AMENDMENT
REVIEWED_PACKAGE_VERSION=v0.1
REVIEWED_COMMIT=ac44e1cf07df08e9042bfc53e2b2ab79ec4871ad
DECISION=PASS
NEW_BLOCKERS=NONE
READY_FOR_CODEX=NO
NEXT_HANDOFF=PLANNER
APPROVED_PLAN_PATH=docs/design/clear-writing/CROSS_SURFACE_RECOVERY_PLAN_V0_1_2026-10-15.md
APPROVED_GOAL_PATH=docs/goals/CLEAR_WRITING_CROSS_SURFACE_RECOVERY_GOAL_V0_1_2026-10-15.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_RECOVERY_KICKOFF_V0_1_2026-10-15.md
```

Planner 下一步只做 existing Reviewed Handoff 的一次最小 re-plan：把批准的 recovery package materialize 到 task-local `PLAN.md`，合法执行 `NEEDS_GPT_PLANNER -> PLAN_FROZEN`，使 `plan_revision: 0 -> 1`，保持 `review_round=1`。完成远端核验后，才可由 Planner 逐字交付已批准 Kickoff 给用户用于 Codex 执行。

## 6. 维护跟踪

`docs/plugin-todos/writing-style.md` 仍以 `tracking: #13` 绑定该长期能力。当前 Issue #13 的 reader-facing copy 尚未反映本轮 v0.1 recovery / Web regression bank / current branch anchor。

本 Critic 不修改该 Issue：仓库维护规则要求 reader-facing Issue 实质改写前真实调用当前安装的 Clear Writing；当前 ChatGPT 账户没有独立 Clear Writing 个人插件可供真实调用。

下一次具备 AI Skills Maintainer / Project mutation 和真实 Clear Writing invocation 的 maintenance action 应核对并同步：

- Issue #13 lifecycle：保持 `DOING`，不得 DONE；
- Area：`writing-style`；
- 当前执行锚点：`reviewed/clear-writing--cross-surface-language-layer@ac44e1cf07df08e9042bfc53e2b2ab79ec4871ad`，随后更新为 Planner re-freeze commit；
- 下一步：一次合法 re-plan freeze -> approved recovery Kickoff -> baseline replay/main merge/bounded repair/full CI -> implementation review；
- Project 尚未由本 Critic 声称已同步。
