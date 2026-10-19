# Goal — Clear Writing 0.5 正式发布收口 v0.2

日期：2026-10-19  
状态：EXECUTION_PACKAGE_DRAFT_FOR_CRITIC  
任务键：`clear-writing--release-closure`

## 1. Authority

目标仓库：

`YuukiAS/AI_Skills_Collection`

目标插件：

`writing-style / Clear Writing`

设计 authority：

`docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_2_2026-10-19.md@6e321ced9ee14c936c06397ead9862f70312bd40`

冻结 production candidate：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

source/evidence branch：

`reviewed/clear-writing--scientific-explanation-readability-repair`

planned execution branch：

`reviewed/clear-writing--release-closure`

planned task-owned worktree：

`/tmp/ai-skills-clear-writing-release-closure`

tracking：

Issue `#13`

本 Goal 只把已批准 Plan v0.2 转成可执行合同，不改变任何设计语义。

## 2. 最终目标

把已经通过真实 ChatGPT Web 验收的 Clear Writing frozen candidate 正式发布为：

```text
Repository: 5.5.0 -> 5.5.1
writing-style: 0.4 -> 0.5
```

其他中央 plugin 与 standalone skill 全部 `NO_BUMP`，maturity `NO CHANGE`，Bridge Kit `NO CHANGE`。

最终正式发布必须同时满足：

1. 只包含已批准 Clear Writing 0.5 product/test/release metadata；
2. 生成层与 source/config/profile 一致；
3. exact committed clean candidate 的 fresh install、正式 upgrade、focused/full validation 与 required CI 全部 PASS；
4. 独立 final-candidate Critic 对 exact SHA PASS；
5. formal `release` 只通过 canonical producer non-force / fast-forward-only 推进；
6. existing PRIVATE Clear Writing plugin 更新到同一正式内容，保持原 `plugin_id`、`USER`、`PRIVATE`；
7. PRIVATE Web payload 与正式 generated writing-style parity；
8. exact released commit 最后普通 non-force 整合回 then-latest `main`；
9. Issue #13 lifecycle 与 0.5 formal release truth 分离，不制造 false-DONE。

## 3. 已完成且禁止重跑的产品验收

最终 4-answer ChatGPT Web closure 已真实 PASS。

本 Goal 禁止重新执行：

- 最终 4-answer Web Gate；
- KR-WEB-01..09；
- W0 / W1 / W2 / W3 / G7；
- matched/control/blind experiment。

历史 `W2=INCONCLUSIVE` 继续保留，不改判。

本阶段只做正式发布的一致性、安装升级、版本、CI、分发与生命周期收口。

## 4. Execution-time baseline gate

Executor 开始任何 release-candidate 写入前，必须重新读取：

- `origin/release`
- formal `VERSION`
- formal writing-style version
- `origin/main`

只有当正式 baseline 仍为：

```text
Repository = 5.5.0
writing-style = 0.4
```

才允许继续。

若 `origin/release`、repository version 或 writing-style formal version 已变化：

`STOP_LATE_BIND_REQUIRED`

立即停止并返回 Planner。不得猜新版本、不得把 current main 当 baseline、不得 force。

## 5. Release-candidate isolation

从 execution-time exact `origin/release` 创建：

- branch：`reviewed/clear-writing--release-closure`
- worktree：`/tmp/ai-skills-clear-writing-release-closure`

如果 branch/worktree 已存在且不能证明属于本 task、基于 exact formal baseline 且 clean，停止，不静默复用。

禁止 wholesale merge/cherry-pick：

`reviewed/clear-writing--scientific-explanation-readability-repair`

旧 evidence branch 只作为 approved source locator 使用。

formal release candidate 相对 baseline 只允许 Clear Writing 0.5 product/test/release metadata。任何无关 production/plugin/version drift 都是 RC1 FAIL。

## 6. Clear Writing 0.5 product identity

产品行为 authority：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

release candidate 必须从该 frozen candidate 选择性移植已批准的 writing-style 语义：

- `skills/writing/core/response-clarity/**`
- `skills/writing/core/chinese-prose/SKILL.md` 中 frozen candidate 的 approved ordinary-response routing 差异
- writing-style Marketplace source 中 frozen candidate 已批准的：
  - response-clarity exposure
  - description/defaultPrompt
- 与这些能力直接相关的既有 regression tests

不得借 release closure 改写其他 sibling Skill 行为。

### codex-writing-style profile

`profiles/codex-writing-style.json` 必须与 frozen candidate 的 approved profile 内容一致，主 skills 正好是：

1. `writing-fidelity`
2. `response-clarity`
3. `scientific-prose`
4. `product-ui-copy`
5. `scientific-rewrite`
6. `chinese-prose`

同时保留 frozen candidate 的 description、`max_active_skills=8` 与 secondary skills。

`product-ui-copy` 本轮只同步已有 profile exposure。禁止修改：

- `skills/writing/core/product-ui-copy/**`
- Product UI Copy runtime semantics
- Product UI Copy architecture

## 7. Generated layer

必须先修改 canonical source/config/profile，再运行仓库现有 canonical generator。

禁止手改：

- `plugins/codex/plugins/**`
- generated registry/catalog/Marketplace payload

最终必须证明 source/generated parity。

## 8. Version / README / changelog

必须形成：

```text
Repository bump decision: PATCH
Repository: 5.5.0 -> 5.5.1

Affected plugins:
- writing-style: 0.4 -> 0.5
- all other central plugins: NO_BUMP

Standalone skills: NO_BUMP
Bridge Kit: NO CHANGE
Maturity: NO CHANGE
```

必须同步：

- `VERSION` -> `5.5.1`
- root `CHANGELOG.md` -> 新 `5.5.1 - 2026-10-19`
- `scripts/codex_marketplace_config.json` writing-style -> `0.5`
- `docs/plugin-changelogs/writing-style.md` -> 新 `0.5 - 2026-10-19`
- `README.md`
  - Repository / CLI release -> `5.5.1`
  - Clear Writing -> `v0.5`
  - 用普通中文说明普通解释能力已经进入正式 Clear Writing

README 不写内部 Gate/W2/commit 流水账。

只要 README 被修改，必须真实调用当前安装的 Clear Writing 检查受影响 reader-facing 区域；只读 Skill 文本、grep 或自称遵循规则不算。

writing-style 0.5 changelog 必须如实记录 `codex-writing-style` profile 对齐六 writing skills，包括已有 `product-ui-copy` 的 profile exposure；不得把它写成 Product UI Copy 新行为。

## 9. Exact final candidate

所有 pre-release evidence 必须绑定同一个：

- committed
- clean
- exact SHA

并证明：

- candidate history 包含 execution-time exact `origin/release`
- `origin/release..candidate` 只有 approved allowlist
- candidate diff 没有未经批准的其他 plugin / standalone version drift

candidate 只要修改，之前的 install/upgrade smoke、local tests、CI evidence 全部失效，必须在新 exact committed clean SHA 上重跑。

## 10. RC5 deterministic release checks

### Fresh install smoke

在干净隔离环境从 exact candidate 走正式安装入口。

回读并验证：

- repository `5.5.1`
- writing-style `0.5`
- installed `response-clarity`
- installed `codex-writing-style` profile
- profile 六 writing skills 不多不少
- 其他 central plugin / standalone skill 相对 formal `5.5.0` baseline 没有未经批准版本漂移

### Formal upgrade smoke

在另一个干净隔离环境，从正式：

`5.5.0 / writing-style 0.4`

通过仓库正式 upgrade path 升到 exact candidate：

`5.5.1 / writing-style 0.5`

不得直接覆盖文件冒充 upgrade。

升级后回读与 fresh install 相同的 repository/plugin/profile identity，并验证其他 plugin/standalone version 没有未经批准漂移。

### 同一 exact SHA 的 deterministic validation

必须运行：

1. writing-style focused tests
2. source/generated parity
3. Marketplace/version/changelog/README consistency
4. profile/install identity validation
5. full repository test suite
6. skill validation
7. required GitHub CI

这些是发布机械/回归验收，不是新的 Web product Gate。

## 11. Final-candidate independent Critic gate

RC1–RC5 全部 PASS 后：

- 冻结 exact candidate SHA；
- 写完整 final-candidate evidence manifest；
- 停止在 release ref / PRIVATE plugin / main side effect 之前；
- 将 exact candidate + RC1–RC5 evidence 交独立 Critic。

没有 exact final-candidate Critic PASS，不得推进 formal `release`。

该 Critic PASS 后无需重新设计；后续只按本 Goal 已冻结的发布步骤恢复。

## 12. Formal release

final-candidate Critic PASS 且 execution-time formal baseline 未变化时：

1. 使用 canonical `ai-skills-repository-maintainer` formal release producer；
2. 只允许 non-force / fast-forward-only 推进 `refs/heads/release`；
3. target 必须是 exact approved `5.5.1 / writing-style 0.5` candidate；
4. 远端回读：
   - exact release SHA
   - `VERSION=5.5.1`
   - writing-style `0.5`

若 `release` 在等待 final-candidate Critic 期间移动，停止并回 Planner late-bind；不得 force。

## 13. Existing PRIVATE ChatGPT plugin

formal release 成功后，更新现有：

`plugin_id=plugins_6ad4fc9abae08191a9ecd81879b2c919`

禁止创建第二个 Clear Writing plugin。

预期：

```text
Web version = 0.5.0
scope = USER
discoverability = PRIVATE
plugin_id = unchanged
```

记录新的 `current_release_id`。

更新后回读：

- six Skills
- references/assets/evals
- `scientific-rewrite/scripts/rewrite_support.py`
- plugin metadata

并与 formal repository generated writing-style 做逐文件 parity。

允许的 host normalization 只包括已明确记录的 host-owned 差异，例如：

- source `0.5` -> Web `0.5.0`
- Plugin Creator owner/author serialization

其他 description/defaultPrompt/Skill/support drift 一律停止。

如果当前 Executor 环境没有合法 Plugin Creator 更新入口：

`PRIVATE_PLUGIN_UPDATE_HANDOFF_REQUIRED`

在 truthful formal release 后停止，不创建替代 plugin、不声称 closure。由具有 canonical Plugin Creator 表面的 Planner/ChatGPT 在同一已批准范围内完成更新与 parity。

formal release 已成功但 PRIVATE plugin 更新失败时，不回滚真实 formal release；Issue #13 不得 DONE。

## 14. Main reintegration

PRIVATE plugin parity 完成后：

1. 读取 then-latest `main`
2. 把 exact released commit 普通 non-force 整合回 main
3. 保留 main 上所有无关开发工作
4. 冲突只允许在 approved Clear Writing/release metadata surface 内解决
5. 若冲突要求修改其他 plugin behavior，停止回 Planner
6. 验证 released commit 是 main ancestor
7. 执行 focused version/parity/integration validation

## 15. Issue #13 lifecycle

Clear Writing 0.5 formal release PASS **不自动等于** Issue #13 DONE。

canonical source：

`docs/plugin-todos/writing-style.md`

heading：

`Promote writing-style into the generic content-preserving language layer`

tracking：

`#13`

formal release RC1–RC6 全部成立后，可以记录：

`CLEAR_WRITING_0_5_FORMAL_RELEASE=PASS`

但只有以下也全部成立，#13 才能 DONE：

1. canonical promotion gate 的 durable evidence 已逐项满足；
2. canonical source status/evidence truthfully 更新；
3. 没有 required downstream consumer pending；
4. Issue 顶部当前进度/当前执行锚点/下一步已更新为最终真实状态；
5. Resolution commit 已记录。

如果 formal release 成功但 required downstream adaptation 仍 pending：

- 0.5 release 仍成功；
- #13 保持 open；
- lifecycle -> `ADAPTING`
- Area = `writing-style`
- 下一步写 exact downstream adaptation locator
- 本 execution 不实施 downstream adaptation

明确禁止为关闭 #13 顺手修改：

- Statistical Modeling
- Scientific Visualization
- Presentations
- Research Authoring
- PIE
- Mica

Issue #13 reader-facing copy 任何实质更新前必须真实调用 installed Clear Writing。若当前 runtime 不能真实调用：

`CLEAR_WRITING_UNAVAILABLE`

不得进行 reader-facing Issue mutation，只记录 exact pending mutation。

若没有 GitHub Project mutation surface，也只记录 exact pending mutation，不要求用户手工维护。

## 16. Stop conditions

任一条件成立立即停止，不扩 scope：

- formal release baseline/version drift
- writing-style formal baseline != 0.4
- execution branch/worktree 无法证明属于本 task 且 clean
- candidate 不是 committed clean exact SHA
- release diff 出现无关 production/version drift
- profile != frozen candidate approved six-skill exposure
- Skill/support 与 frozen candidate 漂移
- fresh install / upgrade smoke FAIL
- local validation / required CI FAIL
- final-candidate Critic 非 PASS
- release target 非 fast-forward
- PRIVATE plugin 变成新 plugin_id / 非 USER / 非 PRIVATE / payload drift
- main reintegration 需要修改无关 plugin behavior
- #13 想进入 DONE 但 canonical promotion gate 或 downstream truth 未满足

## 17. 完成定义

本 Goal 的完整 release closure 成功，需要：

- RC1–RC6 全部成立；
- formal `release` 已是 exact `5.5.1 / writing-style 0.5`
- existing PRIVATE plugin 已是 `0.5.0` 且 parity PASS
- exact released commit 已整合回 latest main

Issue #13 是否 DONE 单独按第 15 节判断。

如果 0.5 release 完成而 #13 进入 ADAPTING，这不是 release failure。

## 18. Non-goals

本 Goal 不授权：

- 新 Web Gate
- W2
- 新写作规则
- 新 Skill
- 新 router/state machine
- Product UI Copy 行为修改
- downstream plugin adaptation
- PIE / Mica
- Research Authoring / Presentations production changes
- force push / force release
- delete/uninstall/replace PRIVATE Clear Writing plugin
