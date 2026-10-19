# Clear Writing 0.5 Release Closure — Kickoff Draft v0.2

日期：2026-10-19  
状态：DRAFT / NOT AUTHORIZED  
任务键：`clear-writing--release-closure`

本文件仅供 execution-ready Critic 审查。只有该 Critic 对同一 execution package PASS，且用户随后发送批准后的短 Codex handoff，才允许开始 Stage A。

## 1. 执行定位

仓库：

`YuukiAS/AI_Skills_Collection`

设计 authority：

`docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_2_2026-10-19.md@6e321ced9ee14c936c06397ead9862f70312bd40`

Canonical Goal：

`docs/goals/CLEAR_WRITING_0_5_RELEASE_CLOSURE_GOAL_V0_2_2026-10-19.md`

source/evidence branch：

`reviewed/clear-writing--scientific-explanation-readability-repair`

planned execution branch：

`reviewed/clear-writing--release-closure`

planned task-owned worktree：

`/tmp/ai-skills-clear-writing-release-closure`

frozen product candidate：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

tracking：

Issue `#13`

## 2. 当前批准范围

版本决策固定为：

```text
Repository: 5.5.0 -> 5.5.1
writing-style: 0.4 -> 0.5
all other central plugins: NO_BUMP
standalone skills: NO_BUMP
maturity: NO CHANGE
Bridge Kit: NO CHANGE
```

不得重新设计该版本决策。

最终 4-answer ChatGPT Web Gate 已完成，不得重跑。

## 3. Stage A — 构建 exact formal release candidate

### 3.1 先做 execution-time baseline preflight

任何写入前：

1. fetch remote refs；
2. 读取 `origin/release` exact SHA；
3. 读取 formal `VERSION`；
4. 读取 formal writing-style version；
5. 读取 current `origin/main`。

仅当：

```text
formal repository = 5.5.0
formal writing-style = 0.4
```

时继续。

否则：

`STOP_LATE_BIND_REQUIRED`

停止并返回 Planner，不创建 candidate、不改 branch、不推进 release。

### 3.2 创建 task-owned release candidate

从 execution-time exact `origin/release` 创建：

- branch：`reviewed/clear-writing--release-closure`
- worktree：`/tmp/ai-skills-clear-writing-release-closure`

若同名 branch/worktree 已存在：

- 只有能证明属于本 exact task；
- 基于 current exact formal release baseline；
- worktree/index clean；

才可继续复用。

否则停止，不重置、不 force、不偷偷覆盖。

### 3.3 只移植 approved Clear Writing 0.5 scope

禁止 wholesale merge/cherry-pick 旧 evidence branch。

只能选择性移植 approved Plan/Goal 明确允许的内容：

- `skills/writing/core/response-clarity/**`
- `skills/writing/core/chinese-prose/SKILL.md` 中 frozen candidate 的 approved routing 差异
- writing-style Marketplace source 的 approved response-clarity exposure、description/defaultPrompt
- `profiles/codex-writing-style.json` -> frozen candidate exact approved profile
- 直接相关 regression tests
- 本 release 所需 version / README / changelog / generated metadata

不得修改 `product-ui-copy` Skill/runtime/architecture。

不得修改其他 plugin production behavior。

### 3.4 profile exact contract

`profiles/codex-writing-style.json` 主 skills 必须正好是：

```text
skills/writing/core/writing-fidelity
skills/writing/core/response-clarity
skills/writing/core/scientific-prose
skills/writing/core/product-ui-copy
skills/writing/core/scientific-rewrite
skills/writing/core/chinese-prose
```

同时保留 frozen candidate 的：

- description
- `max_active_skills=8`
- secondary skills

不得多、不得少。

### 3.5 generated layer

先改 canonical source/config/profile，再运行 canonical generator。

禁止手改：

- `plugins/codex/plugins/**`
- generated registry/catalog/Marketplace payload

完成后必须 source/generated parity PASS。

### 3.6 版本与文档

必须同步：

- `VERSION=5.5.1`
- root `CHANGELOG.md` 新增 `5.5.1 - 2026-10-19`
- writing-style version -> `0.5`
- `docs/plugin-changelogs/writing-style.md` 新增 `0.5 - 2026-10-19`
- `README.md`
  - repository release -> `5.5.1`
  - Clear Writing -> `v0.5`
  - 简洁说明普通解释能力已经进入正式 Clear Writing

README 不得加入内部 Gate/W2/commit 流水账。

README 修改完成后，必须通过当前安装的真实 Clear Writing 对受影响 reader-facing 区域做最终语言检查。

如果当前 executor runtime 无法真实调用 installed Clear Writing：

`CLEAR_WRITING_UNAVAILABLE_FOR_README_CHECK`

停止 Stage A，不用只读 Skill 文本冒充调用。

### 3.7 commit + clean identity

完成所有 candidate 文件后：

1. commit；
2. 验证 worktree/index clean；
3. 记录 exact candidate SHA；
4. 验证 candidate history 包含 execution-time exact `origin/release`；
5. 验证 `origin/release..candidate` 只含 approved allowlist。

所有后续 Stage A evidence 都必须绑定该 exact SHA。

如果之后任何 tracked file 改变，旧 smoke/test/CI evidence 全部作废。

## 4. Stage A — deterministic release smoke

### 4.1 Fresh install

在干净隔离环境从 exact candidate 按仓库正式安装入口 fresh install。

回读并记录：

- repository = `5.5.1`
- writing-style = `0.5`
- installed `response-clarity`
- installed `codex-writing-style` profile
- profile 六个 writing skills 不多不少
- 所有其他 central plugin / standalone skill 版本相对 formal `5.5.0` baseline 无未经批准漂移

### 4.2 Formal upgrade

在另一个干净隔离环境：

起点：

`formal 5.5.0 / writing-style 0.4`

通过仓库正式 upgrade path 升到 exact candidate：

`5.5.1 / writing-style 0.5`

不得直接复制/覆盖 candidate 文件模拟 upgrade。

升级后回读与 fresh install 同一组 identity。

### 4.3 deterministic validation

同一 exact committed clean SHA 上执行：

1. writing-style focused tests
2. source/generated parity
3. Marketplace/version/changelog/README consistency
4. profile/install identity validation
5. full repository test suite
6. skill validation
7. required GitHub CI

任一 FAIL 即停止。

不得：

- 删除失败测试
- 修改 rubric
- 换 candidate 继续复用旧证据
- 重跑 4-answer Web Gate

## 5. Stage A 停止点：final-candidate independent Critic

RC1–RC5 全部 PASS 后：

- 冻结 exact candidate SHA；
- 保存完整 final-candidate evidence manifest；
- 推送 execution branch 允许普通 non-force push；
- 停止所有正式分发副作用。

此时**不得**：

- 推进 `refs/heads/release`
- 更新 PRIVATE plugin
- merge 回 main
- 把 Issue #13 标 DONE

返回：

`READY_FOR_FINAL_CANDIDATE_CRITIC`

并给出：

- exact candidate SHA
- baseline release SHA
- allowlist diff
- install/upgrade smoke evidence
- local/full/CI evidence
- README Clear Writing check evidence
- profile exact identity evidence

用户将该 evidence 交独立 Critic。

## 6. Stage B 恢复条件

Stage B 只有在同一 exact candidate 收到独立 final-candidate Critic PASS 后才可恢复。

恢复时先重新读取 `origin/release`。

若 `origin/release` 已从 Stage A baseline 移动：

`STOP_LATE_BIND_REQUIRED`

停止回 Planner。

不得因为 final-candidate PASS 而 force 覆盖新的 release baseline。

## 7. Stage B — formal release

baseline 仍一致时：

1. 使用 canonical `ai-skills-repository-maintainer` formal release producer；
2. target = exact approved candidate SHA；
3. 只允许 non-force / fast-forward-only 更新 `refs/heads/release`；
4. 远端回读：
   - exact release SHA
   - `VERSION=5.5.1`
   - writing-style `0.5`

任何 non-fast-forward 条件立即停止。

## 8. Stage B — update existing PRIVATE Clear Writing

formal release 成功后，只更新现有：

`plugin_id=plugins_6ad4fc9abae08191a9ecd81879b2c919`

禁止：

- 创建第二个 Clear Writing plugin
- 更换 plugin_id
- uninstall/delete
- PUBLIC/UNLISTED
- 非 USER scope

预期：

```text
version = 0.5.0
scope = USER
discoverability = PRIVATE
plugin_id = unchanged
```

记录新的 `current_release_id`。

回读：

- six Skills
- references/assets/evals
- `scientific-rewrite/scripts/rewrite_support.py`
- plugin metadata

与 formal repository generated writing-style 做逐文件 parity。

只允许明确的 host normalization，例如：

- source `0.5` -> Web `0.5.0`
- Plugin Creator owner/author serialization

其他 payload drift 停止。

如果当前 Codex/Executor 没有合法 Plugin Creator surface：

`PRIVATE_PLUGIN_UPDATE_HANDOFF_REQUIRED`

在 formal release 成功后停止并返回 Planner/ChatGPT，不创建替代 plugin、不 claim full closure。

如果 plugin update 本身失败：

- 不回滚 truthful formal release；
- 保存准确 failure/recovery evidence；
- Issue #13 保持 open；
- 后续只恢复 PRIVATE plugin update/parity。

## 9. Stage B — main reintegration

仅在 PRIVATE plugin parity PASS 后：

1. fetch then-latest `main`
2. 将 exact released commit 普通 non-force 整合回 main
3. 保留 main 上无关工作
4. 冲突只允许在 approved Clear Writing/release metadata surface 解决
5. 若冲突要求修改其他 plugin behavior，停止回 Planner
6. 验证 exact released commit 是 main ancestor
7. 跑 focused version/parity/integration validation
8. 普通 non-force push main

禁止 force/rebase current main 以迁就 release。

## 10. Issue #13 lifecycle

`CLEAR_WRITING_0_5_FORMAL_RELEASE=PASS` 与 Issue #13 lifecycle 分开判断。

正式 release + PRIVATE parity + main reintegration 后，重新读取：

- `docs/plugin-todos/writing-style.md` tracking #13 canonical heading
- durable evidence
- required downstream consumer truth

如果 canonical promotion gate 仍有 required downstream adaptation：

- 0.5 formal release 仍成功
- Issue #13 保持 open
- lifecycle -> `ADAPTING`
- Area = `writing-style`
- 下一步写 exact downstream adaptation locator
- 不在本 task 修改 downstream plugin

如果 promotion gate 已有 durable evidence 全部满足、canonical source truthfully 更新且无 required downstream pending，才允许：

- Issue #13 -> DONE
- 记录 Resolution commit
- 关闭 Issue

### Reader-facing copy rule

Issue #13 的“问题 / 当前进度 / 当前执行锚点 / 下一步”任何实质更新前，必须真实调用 installed Clear Writing。

如果当前 runtime 不能真实调用：

`CLEAR_WRITING_UNAVAILABLE`

不做 reader-facing Issue mutation，只记录 exact pending mutation。

若没有 GitHub Project field mutation surface，同样只记录 exact pending mutation，不要求用户手工拖看板。

## 11. 允许的外部副作用

Stage A：

- fetch/read repo
- 创建 task-owned branch/worktree
- 修改 approved release-candidate files
- commit
- ordinary non-force push execution branch
- 运行本地 tests/generator/install/upgrade smoke
- 触发 required GitHub CI

Stage B（只有 exact final-candidate Critic PASS 后）：

- canonical fast-forward-only `release` advancement
- existing PRIVATE Clear Writing plugin update
- ordinary non-force main reintegration
- Issue/source lifecycle truth update only within approved rules

## 12. 明确禁止

整个任务都禁止：

- force push
- force release
- destructive reset of unrelated work
- wholesale merge/cherry-pick old evidence branch
- second Clear Writing plugin
- delete/uninstall existing Clear Writing plugin
- PUBLIC/UNLISTED discoverability
- any other plugin/standalone version bump
- maturity change
- W2 / Web Gate rerun
- new writing rule/Skill/router/state machine
- Statistical Modeling / Scientific Visualization / Presentations / Research Authoring / PIE / Mica production changes
- changing Product UI Copy Skill/runtime behavior
- weakening tests to obtain PASS

## 13. 执行返回

Stage A 成功：

`READY_FOR_FINAL_CANDIDATE_CRITIC`

Stage B 完成且 0.5 正式发布闭合：

`CLEAR_WRITING_0_5_FORMAL_RELEASE=PASS`

Issue #13 必须另外返回真实 lifecycle：

- `ISSUE_13=ADAPTING`
- 或 `ISSUE_13=DONE`

不得因为 0.5 release PASS 自动输出 DONE。
