# Clear Writing 0.5 Release Closure Plan v0.2 — 独立 Critic 复核 Prompt

你现在担任 AI Research Stack 的独立 Critic，只复核 Clear Writing 0.5 release closure 设计 v0.2 的最小返修。

## Active Review Context

target_repo:
`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain:
`writing-style / Clear Writing`

design_topic_or_task_key:
`clear-writing--release-closure`

source/evidence branch:
`reviewed/clear-writing--scientific-explanation-readability-repair`

review_stage:
`RELEASE_CLOSURE_DESIGN_REREVIEW_V0_2`

上一版 Plan:
`docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_1_2026-10-19.md@8e55b993cf9663947c642fa31cc50d952225b4af`

本轮 Plan:
`docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_2_2026-10-19.md@6e321ced9ee14c936c06397ead9862f70312bd40`

frozen production candidate:
`fd7a1578a5042a46a55c5b638f6d550655b1096b`

tracking Issue:
`#13`

上一轮 Critic 结论：
`REVISE`

只剩三个 blocker：

- `CW-RC-03`
- `CW-RC-05`
- `CW-RC-07`

以下已经接受，不得重开：

- repository `5.5.0 -> 5.5.1` PATCH；
- writing-style `0.4 -> 0.5`；
- 其他 plugin / standalone skill NO_BUMP；
- maturity NO CHANGE；
- formal release candidate 从当时 current `origin/release` 构建；
- baseline drift -> stop + Planner late-bind；
- 不 wholesale merge/cherry-pick 旧 evidence branch；
- generated layer 只经 canonical generator；
- README 改动后真实调用 installed Clear Writing；
- exact candidate final CI；
- fast-forward-only formal release producer；
- formal release 后更新现有 PRIVATE plugin：
  `plugins_6ad4fc9abae08191a9ecd81879b2c919`
- expected Web version `0.5.0`，继续 USER / PRIVATE；
- full payload readback parity；
- PRIVATE plugin update failure 不回滚 truthful formal release；
- released commit 最后普通 non-force 整合回 then-latest main；
- 不重开 W2、4-answer Web Gate、六技能架构、PIE、Mica、Research Authoring、Presentations。

## 必须读取

先读取 latest main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

然后读取：

- v0.2 Plan；
- frozen candidate 的
  `profiles/codex-writing-style.json`；
- current formal release 的同一 profile；
- `docs/plugin-todos/writing-style.md` 中 tracking #13 canonical heading；
- `docs/plugin-todos/statistical-modeling.md` tracking #73；
- `docs/plugin-todos/scientific-visualization.md` tracking #49；
- Issue #13 当前 copy。

不要执行任何 release、install、upgrade、plugin update 或 downstream adaptation。

# 1. CW-RC-03 — exact approved profile exposure

v0.2 已把 0.5 的 `profiles/codex-writing-style.json` 明确绑定到 frozen candidate `fd7a157...` 的 exact approved内容：

预期主 skills 为：

1. `writing-fidelity`
2. `response-clarity`
3. `scientific-prose`
4. `product-ui-copy`
5. `scientific-rewrite`
6. `chinese-prose`

并保留 frozen candidate 的 description、`max_active_skills=8` 和 secondary skills。

请确认：

- 这已经消除“只加 response-clarity”造成的候选身份歧义；
- `product-ui-copy` 在本轮只同步 profile exposure；
- `skills/writing/core/product-ui-copy/**` 与 Product UI Copy runtime/architecture 不允许修改；
- 0.5 changelog 要说明 profile exposure 对齐，但不能把它写成 Product UI Copy 新产品行为；
- RC5 fresh install / upgrade smoke 会回读实际 profile，验证六 writing skills 不多不少。

若成立：

`CW-RC-03=CLOSED`

# 2. CW-RC-05 — formal fresh install / upgrade smoke

v0.2 要求所有 release-smoke / test / CI 绑定同一个：

- committed；
- clean；
- exact SHA；
- 以当时 current formal `origin/release` 为 parent/history；
- release diff 只含 RC1 allowlist。

在推进 release ref 之前必须新增 bounded deterministic release smoke：

## Fresh install

从 exact candidate fresh install 后回读：

- repository `5.5.1`
- writing-style `0.5`
- `codex-writing-style` profile
- expected six writing skills
- installed `response-clarity`
- 其他 central plugin / standalone skill 不得有未经批准版本漂移

## Upgrade

另一个干净环境从正式：

`5.5.0 / writing-style 0.4`

通过仓库正式 upgrade path 升级到：

`5.5.1 / writing-style 0.5`

然后回读同一组 identity。

请确认：

- 这是真实 install/upgrade 发布机械验收，不是新的产品行为 Gate；
- 不允许直接覆盖文件冒充 upgrade；
- smoke 之后若 candidate 修改，旧 smoke/CI evidence 失效；
- exact candidate 还必须运行 focused tests、source/generated parity、version/changelog/README consistency、profile/install identity validation、full tests、skill validation、required GitHub CI；
- 不重新执行 4-answer Web Gate。

若成立：

`CW-RC-05=CLOSED`

# 3. CW-RC-07 — formal release 与 Issue #13 lifecycle 分离

v0.2 明确：

`CLEAR_WRITING_0_5_FORMAL_RELEASE=PASS`

**不自动等于**

`ISSUE_13=DONE`

Issue #13 canonical source 仍为：

`docs/plugin-todos/writing-style.md`

heading：

`Promote writing-style into the generic content-preserving language layer`

tracking：

`#13`

其 promotion gate 仍包含多类 durable evidence / downstream consumers。

当前明确相关 downstream source：

### Statistical Modeling

`docs/plugin-todos/statistical-modeling.md`

- heading:
  `Delegate reader-facing wording without giving away statistical semantics`
- `tracking: #73`
- `status: READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER`

### Scientific Visualization

`docs/plugin-todos/scientific-visualization.md`

- heading:
  `Delegate captions/annotations without giving away visual semantics`
- `tracking: #49`
- `status: READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER`

v0.2 冻结：

- RC1–RC6 全部 PASS 后，0.5 formal release 可以独立成功；
- #13 只有 canonical promotion gate 已被 durable evidence truthfully 满足、canonical source 状态/证据已经更新、且没有 required downstream consumer pending 时才能 DONE；
- 如果 release 成功但 downstream adaptation 仍 pending，则 #13 继续 open，Project lifecycle 从 DOING -> ADAPTING；
- 本轮不得为了关 #13 实施 Statistical Modeling、Scientific Visualization、Presentations、Research Authoring、PIE 或 Mica；
- final closure 前必须清理 Issue #13 顶部 `当前进度 / 当前执行锚点 / 下一步`，不能让旧 A/E、B/C、G7、W2 历史冒充当前 blocker；
- 历史保留在后部 evidence/history；
- 没有 Project mutation surface 时记录 exact pending mutation，不要求用户手工维护。

请确认这符合 `AI_SKILLS_MAINTENANCE_BOARD.md` 的 DOING -> ADAPTING -> DONE 语义。

若成立：

`CW-RC-07=CLOSED`

# 4. 改动影响检查

只检查 v0.2 是否因为关闭三个 blocker 新引入 release-closure 风险：

- exact profile exposure 是否无意重开 Product UI Copy；
- install/upgrade smoke 是否扩大成新的产品 Gate；
- Issue #13 ADAPTING 语义是否会错误要求本轮修改 downstream plugins；
- release scope 是否仍只限 Clear Writing 0.5 + repository patch metadata；
- release 成功与 #13 lifecycle 是否清楚分离；
- 版本、release-isolation、PRIVATE plugin parity、main reintegration 等已接受设计是否保持原样。

不得因“可以更稳”新增 Web Gate 或重新要求旧产品验证。

# 输出

给 `PASS` 或 `REVISE`。

若 `REVISE`：

- 只允许围绕 `CW-RC-03 / CW-RC-05 / CW-RC-07` 或本轮修订直接新引入的 release-closure blocker；
- 使用稳定 finding ID；
- 不重开产品 Gate；
- 自动生成给 Planner 的最小返修 prompt。

若 `PASS`：

必须明确输出：

```text
DECISION=PASS
CLOSED_FINDINGS=CW-RC-03,CW-RC-05,CW-RC-07
APPROVED_PLAN_PATH=docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_2_2026-10-19.md
APPROVED_PLAN_COMMIT=6e321ced9ee14c936c06397ead9862f70312bd40
REPOSITORY_BUMP=5.5.0->5.5.1
WRITING_STYLE_BUMP=0.4->0.5
READY_FOR_EXECUTION_PACKAGE=YES
NEXT_HANDOFF=PLANNER
```

并明确：

本 PASS 只批准 release-closure 设计 v0.2。

它不授权：

- 写 Goal/Kickoff 之外的执行；
- 启动 Codex；
- 构建 candidate；
- 推进 release；
- 更新 PRIVATE plugin；
- 改下游 plugin；
- 把 Issue #13 提前标 DONE。

PASS 后唯一下一步是 Planner 基于该 v0.2 冻结同版 Goal + Kickoff execution package，再交 execution-ready Critic。
