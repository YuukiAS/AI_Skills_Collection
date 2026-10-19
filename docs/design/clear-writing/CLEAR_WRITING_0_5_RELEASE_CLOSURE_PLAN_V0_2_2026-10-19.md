# Clear Writing 0.5 最小 Release Closure Plan v0.2

日期：2026-10-19  
状态：PLANNER_REVISION_FOR_CRITIC  
任务键：`clear-writing--release-closure`  
目标插件：`writing-style / Clear Writing`  
source/evidence branch：`reviewed/clear-writing--scientific-explanation-readability-repair`

上一版：
`docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_1_2026-10-19.md@8e55b993cf9663947c642fa31cc50d952225b4af`

本轮只关闭独立 Critic 的三个 blocker：

- `CW-RC-03`
- `CW-RC-05`
- `CW-RC-07`

其余 release-closure 设计保持不变。

## 1. 目标与已冻结边界

最终 4-answer ChatGPT Web closure gate 已由用户真实执行并全部 PASS。当前阶段只做正式发布收口，不再修改 Clear Writing 产品行为，不再增加 Web Gate。

冻结 production candidate：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

历史：

`W2=INCONCLUSIVE`

继续作为诊断事实保留，不重跑、不改判，也不再作为当前收窄 release claim 的 blocker。

本轮 release closure 只允许处理：

- repository/plugin version；
- README；
- changelog；
- release branch；
- source/generated/release identity；
- deterministic install/upgrade smoke；
- final CI；
- actual released PRIVATE plugin identity/parity；
- Issue #13 的真实 lifecycle / closure copy。

明确不做：

- invocation-policy 重设计；
- 六技能架构变化；
- KR-WEB-01..09 重跑；
- W2 / W0 / W1 / W3 / G7；
- 新写作规则；
- 新 Web Gate；
- PIE、Mica、Research Authoring、Presentations；
- Statistical Modeling / Scientific Visualization production adaptation。

## 2. 当前正式版本与 release isolation

2026-10-19 已实际读取：

```text
origin/main    = 23f51b0bebd8a32f49d899f7fae1ee0e5f17e4cd
origin/release = 6daafa779e1c4af1ef9ec58b4a5df5f30b0c4b17

main VERSION    = 5.5.0
release VERSION = 5.5.0

formal writing-style = 0.4
```

current main 包含大量与本轮 Clear Writing 无关的开发 drift，因此正式 release 不得由 current main 整体推进。

正式路径继续冻结为：

1. execution 时重新读取当时 current `origin/release`；
2. 若仍是正式 `5.5.0 / writing-style 0.4`，从该 exact release 基线建立独立 release candidate；
3. 只移植本 Plan 明确允许的 Clear Writing 0.5 scope；
4. candidate 必须 committed、clean、exact SHA；
5. candidate 通过 RC1–RC5 和独立 final-candidate Critic 后，使用 canonical formal release producer，以 non-force / fast-forward-only 推进 `refs/heads/release`；
6. 完成正式 release 与 PRIVATE plugin parity 后，把 exact released commit 普通 non-force 整合回 then-latest `main`，保留 main 上无关开发工作。

若 execution 开始时：

- `origin/release` 已移动；
- repository formal version 已不是 `5.5.0`；
- formal writing-style 已不是 `0.4`；

立即停止并回 Planner late-bind。不得猜版本、不得 force、不得 wholesale merge current main。

## 3. 版本决策

```text
Repository bump decision: PATCH
Repository: 5.5.0 -> 5.5.1
Reason: Clear Writing 在既有 collection contract 内完成兼容的用户可见质量与正常入口改进，没有新增 repository-level task 或破坏性 contract。

Affected plugins:
- writing-style: 0.4 -> 0.5
  Reason: 本 refinement 已实际改变用户可见 production behavior / quality，原 failure replay、unrelated regression、独立 review 与最终真实 Web closure 均已通过；按版本政策必须 exactly once bump。

- all other central plugins: NO_BUMP

Standalone skills: NO_BUMP
Bridge Kit: NO CHANGE
Maturity: NO CHANGE
```

不推进 `1.0`，也不修改 `docs/PLUGIN_MATURITY.md`。

ChatGPT Plugin Creator 的显示版本允许按 host 规则规范化：

`source 0.5 -> Web display 0.5.0`

repository 中央 plugin canonical version 仍是两段 `0.5`。

## 4. RC1 — release scope isolation

正式候选相对当时 current `origin/release` 的 diff 必须只包含本 Plan 允许的 Clear Writing product/test/release metadata。

禁止：

- wholesale merge/cherry-pick 旧 evidence branch；
- 带入旧 W2/control machinery；
- 带入 Presentations、Research Authoring、PIE、Mica 或其他无关 production drift；
- 带入其他 plugin/version bump。

若出现不在 allowlist 内的 production/version drift，RC1 FAIL，停止。

## 5. RC2 / RC3 — frozen candidate identity 与完整 profile exposure

### 5.1 产品语义来源

正式 0.5 的产品行为 authority 仍是：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

允许移植的 production 语义包括：

- `skills/writing/core/response-clarity/**`
- frozen candidate 中 `skills/writing/core/chinese-prose/SKILL.md` 的 approved ordinary-response routing 差异
- writing-style Marketplace source 中：
  - response-clarity exposure
  - frozen candidate 已批准的 description/defaultPrompt
- frozen candidate 对应直接回归 tests

其他已存在 sibling Skill/runtime 内容不在 release closure 中重写。

### 5.2 CW-RC-03：profile 目标改为 frozen candidate exact approved profile

0.5 的：

`profiles/codex-writing-style.json`

目标不再描述为“只加入 response-clarity”，而必须与 frozen candidate `fd7a157...` 的 approved profile 内容一致：

```json
{
  "name": "codex-writing-style",
  "description": "Profile for response clarity, writing fidelity, Product UI Copy, heavy Chinese source-faithful structural rewrites, English scientific prose, and Chinese report/README/document polishing.",
  "max_active_skills": 8,
  "skills": [
    "skills/writing/core/writing-fidelity",
    "skills/writing/core/response-clarity",
    "skills/writing/core/scientific-prose",
    "skills/writing/core/product-ui-copy",
    "skills/writing/core/scientific-rewrite",
    "skills/writing/core/chinese-prose"
  ],
  "secondary_skills": [
    "skills/writing/research/scientific-writing",
    "skills/writing/research/peer-review"
  ]
}
```

这里的 `product-ui-copy` 只是在 profile exposure 上与 frozen candidate 对齐。

**不修改**：

- `skills/writing/core/product-ui-copy/**`
- Product UI Copy runtime semantics
- Product UI Copy architecture
- Product UI Copy Web Gate

因为 `product-ui-copy` 已经属于正式 writing-style 0.4；本轮只修正 0.5 profile exposure，使 release identity 与已通过的 frozen candidate 一致。

### 5.3 0.5 changelog 对 profile 的表达

writing-style 0.5 changelog 必须如实记录：

- `codex-writing-style` profile 现在与已批准的六个 writing skills exposure 对齐；
- 其中新增到 profile exposure 的是 `response-clarity` 与已存在的 `product-ui-copy`；
- 这不代表本轮修改 Product UI Copy 专业行为，也不代表重新发布/重验 Product UI Copy。

### 5.4 Generated layer

仍严格遵守：

- 不手改 `plugins/codex/plugins/**`
- 不手改 generated registry/catalog/Marketplace payload
- 先改 canonical source/config/profile
- 再运行现有 generator
- source/generated parity 必须 PASS

### 5.5 最终安装身份

RC3 不只比较仓库文件，还必须在 RC5 install/upgrade smoke 中验证实际安装后的 `codex-writing-style` profile 正好包含预期六个 writing skills：

1. `writing-fidelity`
2. `response-clarity`
3. `scientific-prose`
4. `product-ui-copy`
5. `scientific-rewrite`
6. `chinese-prose`

不得多、不得少。

## 6. RC4 — version / README / changelog closure

允许且必须同步：

### Repository

- `VERSION`: `5.5.0 -> 5.5.1`
- root `CHANGELOG.md`: 新增 `5.5.1 - 2026-10-19`
- `README.md`：
  - Repository / CLI release -> `5.5.1`
  - Clear Writing row -> `v0.5`
  - 用一句自然中文说明普通解释能力已经进入正式 Clear Writing
  - 不写 W2/Gate/commit/审查流水账

### Plugin

- `scripts/codex_marketplace_config.json` 中 writing-style -> `0.5`
- `docs/plugin-changelogs/writing-style.md` 新增 `0.5 - 2026-10-19`
- `Unreleased` 恢复 `No pending released changes.`

0.5 changelog 只记录真实用户变化：

- ordinary explanation / diagnostic / progress summary 具备 `response-clarity` route；
- complex scientific explanation 按完整语义/推理单元组织；
- unfamiliar / multi-index object 先建立受来源支持的 reader model；
- missing definition 明确暴露，不猜含义；
- exact-only machine output 保持 activation exemption；
- `codex-writing-style` profile 对齐 frozen candidate 的六 writing skill exposure；
- 最终真实 ChatGPT Web 4-answer closure PASS；
- claim boundary：
  - 不声称 `PLUGIN_LOADED_EVERY_TURN=PASS`
  - 不声称每轮后台必然加载 Clear Writing
  - 不声称 matched causal increment 已证明

README 只要发生修改，结束前必须真实调用当前安装的 Clear Writing 检查受影响 reader-facing 区域。读 `SKILL.md`、grep 或手工声称遵循规则均不能代替。

## 7. RC5 — exact committed clean candidate 的 deterministic release smoke + final CI

`CW-RC-05` 本轮明确补齐正式安装/升级验收。

### 7.1 Candidate identity 前提

所有 RC5 操作必须绑定同一个 exact release candidate：

- candidate 已 commit；
- worktree/index clean；
- 记录 exact SHA；
- candidate parent/history 包含当时 current formal `origin/release`；
- `origin/release..candidate` 只含 RC1 allowlist 范围；
- 后续 smoke / test / CI 不允许在未 commit dirty tree 上取证。

如果 smoke 后需要修改 candidate，旧 smoke/CI evidence 失效；必须对新的 exact committed clean SHA 重跑 RC5。

### 7.2 Fresh install smoke

在隔离临时安装环境中，从 exact candidate 做 fresh install。

必须回读：

- repository identity = `5.5.1`
- writing-style = `0.5`
- `codex-writing-style` profile identity
- profile 六 writing skills exposure 完整
- installed `response-clarity` 存在
- 其他 central plugin / standalone skill version 与正式 `5.5.0` baseline 相比没有未经批准的漂移

该 smoke 只验证安装与 identity，不重新评估写作质量。

### 7.3 Upgrade smoke

另一个干净隔离环境从正式：

`5.5.0 / writing-style 0.4`

开始，按仓库正式 upgrade path 升级到 candidate：

`5.5.1 / writing-style 0.5`

升级后必须回读与 fresh install 同一组 identity：

- repository 5.5.1
- writing-style 0.5
- expected six-skill profile exposure
- response-clarity installed
- 其他 central plugin / standalone skill version无未经批准漂移

不得用直接覆盖文件冒充正式 upgrade path。

### 7.4 Deterministic / CI checks

同一个 exact committed clean SHA 上继续执行：

1. writing-style focused tests；
2. source/generated parity；
3. Marketplace/version/changelog/README consistency；
4. profile/install identity validation；
5. full repository test suite；
6. skill validation；
7. required GitHub CI。

这只是正式发布机械/回归验收，**不重新执行最终 4-answer Web Gate，也不增加新的产品行为 Gate**。

任一项 FAIL：

- 不删测试；
- 不改 rubric；
- 不换 candidate 偷用旧 evidence；
- 停止并归因。

## 8. RC6 — formal release 与真实 PRIVATE ChatGPT plugin

RC1–RC5 全部通过并取得 exact final-candidate independent Critic PASS 后：

1. 使用 canonical `ai-skills-repository-maintainer` formal release producer；
2. 只允许 non-force / fast-forward-only 推进 `refs/heads/release`；
3. target 必须是 exact approved `5.5.1 / writing-style 0.5` candidate；
4. 远端回读 exact SHA、`VERSION=5.5.1`、writing-style `0.5`；
5. 更新**现有** PRIVATE ChatGPT Clear Writing plugin：
   `plugins_6ad4fc9abae08191a9ecd81879b2c919`
6. 预期：
   - Web version `0.5.0`
   - scope `USER`
   - discoverability `PRIVATE`
   - plugin_id 不变
7. 记录新的 `current_release_id`；
8. 回读 actual Web release：
   - 六个 Skill
   - references/assets/evals
   - `scientific-rewrite/scripts/rewrite_support.py`
   - plugin metadata
9. 与正式 repository generated writing-style 做逐文件 parity。

允许的 host normalization 仅限已经明确记录的 host-owned 差异，例如：

- source `0.5` -> Web `0.5.0`
- Plugin Creator owner/author serialization

若出现其他 description/defaultPrompt/Skill/support 漂移，停止。

禁止：

- 创建第二个 Clear Writing plugin
- 更换 plugin_id
- PUBLIC / UNLISTED discoverability
- scope 改为非 USER
- 为了 parity 去改 frozen product semantics

若 formal release 已成功、PRIVATE plugin 更新失败：

- 不回滚 truthful formal release；
- Issue #13 不得 DONE；
- 保留准确 failure/recovery evidence；
- 只恢复 PRIVATE plugin update/parity closure。

## 9. Main reintegration

PRIVATE plugin release parity完成后：

1. 读取 then-latest `main`；
2. 将 exact released commit 普通 non-force 整合回 main；
3. 保留 main 上全部无关开发工作；
4. 冲突只允许在本 Plan 批准的 Clear Writing/release metadata surface 内解决；
5. 如果冲突要求改变 Presentations、Research Authoring、Statistical Modeling、Scientific Visualization 或其他 production 行为，停止回 Planner；
6. 验证 released commit 成为 main ancestor；
7. 运行 focused version/parity/integration validation。

## 10. RC7 — Issue #13 与 canonical promotion gate 分离

`CW-RC-07` 本轮明确修正：

**writing-style 0.5 formal release 成功，不自动等于 Issue #13 DONE。**

Issue #13 的 canonical source 仍是：

`docs/plugin-todos/writing-style.md`

heading：

`Promote writing-style into the generic content-preserving language layer`

tracking：

`#13`

该 canonical promotion gate 仍包含多类真实跨域证据/consumer，包括：

- long rewrite
- advisor report
- presentation handoff
- statistical result/caption
- scientific-visualization caption/annotation

当前还存在至少两个显式 downstream candidate：

- `docs/plugin-todos/statistical-modeling.md`
  - `Delegate reader-facing wording without giving away statistical semantics`
  - `tracking: #73`
  - `status: READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER`

- `docs/plugin-todos/scientific-visualization.md`
  - `Delegate captions/annotations without giving away visual semantics`
  - `tracking: #49`
  - `status: READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER`

### 10.1 0.5 formal release 的独立完成条件

Clear Writing 0.5 正式 release 可以在 RC1–RC6 全部成立后独立宣布完成。

这时允许记录：

`CLEAR_WRITING_0_5_FORMAL_RELEASE=PASS`

但**不得自动记录**：

`ISSUE_13=DONE`

### 10.2 Issue #13 DONE 的额外条件

只有以下全部真实成立，才允许 #13 DONE：

1. 0.5 formal release RC1–RC6 PASS；
2. `docs/plugin-todos/writing-style.md` 的 canonical promotion gate 已有 durable evidence 逐项满足；
3. canonical source 的 status/evidence 被 truthfully 更新到实际当前状态；
4. 没有 required downstream consumer pending；
5. Issue 顶部当前进度/锚点/下一步已清理为最终真实 closure；
6. 记录 Resolution commit。

不得仅凭：

- 0.5 release 成功；
- Web 4-answer PASS；
- README/changelog/version完成；

就自动关闭 #13。

### 10.3 若 release 后仍有 downstream adaptation

若 0.5 formal release 完成，但 #13 canonical promotion gate 仍有 required downstream consumer adaptation：

- writing-style 0.5 release 仍然算成功；
- Issue #13 保持 open；
- AI Skills Maintenance lifecycle 从 `DOING` 转为 `ADAPTING`；
- Area 仍为 `writing-style`；
- 下一步必须写成准确 consumer/adaptation locator，而不是旧 A/E、B/C、G7 或 W2 历史；
- 不在本轮实施这些 consumer。

特别禁止为了“把 #13 关掉”顺手修改：

- Statistical Modeling
- Scientific Visualization
- Presentations
- Research Authoring
- PIE
- Mica

### 10.4 若 durable evidence 已经足够

如果 release closure 时重新读取 canonical source 和 durable evidence 后，能够证明 #13 原 promotion gate 已经在现有历史工作中实际满足，而且没有 required downstream consumer pending，则：

- truthfully 更新 `docs/plugin-todos/writing-style.md` 对应 heading 的 status/evidence；
- 清理 reader-facing Issue #13 顶部“当前进度 / 当前执行锚点 / 下一步”，移除旧 A/E、B/C、G7 等历史 blocker 表述；
- 写 Resolution commit；
- Project Status -> `DONE`；
- 关闭 Issue。

不得通过降低 promotion gate 或删除 downstream requirement 来制造 DONE。

### 10.5 无 Project mutation surface

若 execution 环境仍没有 GitHub Project field mutation surface：

- 继续更新可合法更新的 Issue/source evidence；
- 输出 exact pending mutation；
- 不要求用户手工拖看板；
- 不声称 Project Status 已同步。

release 完成但 downstream pending 时，pending mutation 应是：

```text
Issue #13
Status = ADAPTING
Area = writing-style
Resolution commit = <blank until full closure>
Next action = <exact downstream adaptation locator>
```

只有 full closure 后才允许：

```text
Issue #13
Status = DONE
Area = writing-style
Resolution commit = <exact final closure commit>
```

## 11. Reader-facing Issue copy

Issue #13 是用户直接看的入口。

任何实质改写前必须真实调用当前安装的 Clear Writing。

正式关闭前顶部必须只保留真实当前状态：

```text
问题：
当前进度：
当前执行锚点：
下一步：
```

不得让已失效的 A/E、B/C、G7、W2、旧 Web Gate 等历史描述继续出现在顶部冒充当前 blocker。

历史可留在后部 evidence/history，不得删除真实历史。

## 12. Release-closure Gate Matrix v0.2

| Gate | 证明什么 | 主要证据 | 失败 |
| --- | --- | --- | --- |
| RC1 | formal release scope isolated | release baseline -> candidate allowlist diff | 无关 production/version drift |
| RC2 | 产品语义仍绑定 frozen candidate | source semantic/file parity | Skill/support 漂移 |
| RC3 | profile 与 frozen candidate exact approved exposure 一致 | profile exact diff + install readback | 六技能 profile 多/少/错 |
| RC4 | version/README/changelog closure一致 | 5.5.1 / 0.5 consistency + Clear Writing README check | version/docs drift |
| RC5 | exact committed clean candidate 可 fresh install / formal upgrade 且全回归通过 | fresh install + 5.5.0→5.5.1 upgrade + full CI | install/upgrade/version/profile/CI fail |
| RC6 | stable release 与 PRIVATE Web release 是 exact approved identity | fast-forward release + remote readback + same plugin_id 0.5.0 parity | release/plugin identity drift |
| RC7 | #13 lifecycle 不发生 false-DONE | canonical promotion gate + downstream checklist + Issue/Project truth | release success 被错误等同 DONE |

不得新增新的 Web product Gate。

## 13. 停止条件

以下任一发生即停止，不扩 scope：

- formal `origin/release` baseline/version漂移；
- writing-style formal baseline 已不是 0.4；
- candidate 不是 committed clean exact SHA；
- release diff 出现无关 production/version drift；
- profile 不等于 frozen candidate approved six-skill exposure；
- Skill/support 与 frozen candidate 不一致；
- fresh install / upgrade smoke FAIL；
- final CI FAIL；
- release target 非 fast-forward；
- PRIVATE plugin update 产生新 plugin_id、非 USER、非 PRIVATE 或 payload drift；
- main reintegration 需要修改无关 plugin behavior；
- #13 要 DONE 但 canonical promotion gate / downstream consumer truth 尚未满足。

## 14. 本轮不执行

本轮仍只冻结 release-closure 设计：

- 不写 Goal/Kickoff；
- 不启动 Codex；
- 不构建 release candidate；
- 不推进 `release`；
- 不更新 PRIVATE plugin；
- 不修改 downstream plugins；
- 不改 Issue #13 lifecycle 到 ADAPTING/DONE。

独立 Critic PASS 后，Planner 才基于本 v0.2 冻结同版 Goal + Kickoff execution package，交 execution-ready Critic。
