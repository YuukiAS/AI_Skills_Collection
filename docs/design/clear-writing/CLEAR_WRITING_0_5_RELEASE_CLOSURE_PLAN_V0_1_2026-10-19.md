# Clear Writing 0.5 最小 Release Closure Plan v0.1

日期：2026-10-19  
状态：PLANNER_PROPOSAL_FOR_CRITIC  
任务键：`clear-writing--release-closure`

## 1. 目标与边界

最终 4-answer ChatGPT Web closure gate 已由用户真实执行并全部 PASS。当前阶段只做正式发布收口，不再修改 Clear Writing 产品行为，不再增加 Web Gate。

冻结产品候选：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

已通过的用户侧最终验收：

- 显式真实 PRIVATE Clear Writing 入口；
- Project normal entry 下的 `scientific-rewrite`；
- pure exact JSON；
- complex scientific explanation + exact-only 后恢复。

历史 `W2=INCONCLUSIVE` 继续作为诊断事实，不重跑、不改判，也不再作为收窄 release claim 的 blocker。

本计划只允许：

- repository/plugin version；
- README；
- changelog；
- release branch；
- source/generated/release identity；
- final CI；
- actual released PRIVATE plugin identity/parity；
- Issue #13 最终 closure。

明确不做：

- invocation-policy 重设计；
- 六技能架构变化；
- KR-WEB-01..09 重跑；
- W2 / W0 / W1 / W3 / G7；
- PIE、Mica、Research Authoring、Presentations；
- 新写作规则；
- 新 Web test。

## 2. 当前真实版本与发布基线

2026-10-19 实际读取：

```text
origin/main    = 23f51b0bebd8a32f49d899f7fae1ee0e5f17e4cd
origin/release = 6daafa779e1c4af1ef9ec58b4a5df5f30b0c4b17

main VERSION    = 5.5.0
release VERSION = 5.5.0

main writing-style    = 0.4
release writing-style = 0.4
```

当前 `main` 比 `release` 多 336 个提交，含与 Clear Writing 无关的开发状态；例如当前 main 的 Marketplace/test metadata 已出现 Presentations `0.4`，而正式 `release` 仍是 Presentations `0.3`。

因此本 release closure **不得把 current main 整体推进到 release**。这样会把用户明确禁止的无关工作一起正式发布。

采用现有仓库已经使用过的正式 release-isolation 模式：

1. 从当时 current `origin/release` 创建独立 release-candidate branch；
2. 只移植本 Clear Writing 已批准范围；
3. exact candidate 全绿后，使用 canonical formal release producer fast-forward-only 推进 `release`；
4. 再把已经发布的 exact release commit 普通 non-force 整合回 latest `main`，保留 main 上所有无关开发工作。

若执行开始时 `origin/release` 已不再是上述 `5.5.0@6daafa...`，或正式 `writing-style` 已不再是 `0.4`，立即停止并回 Planner late-bind；不得猜新版本。

## 3. 版本决策

按最新 `PLUGIN_VERSIONING_AND_CHANGELOGS.md`：

```text
Repository bump decision: PATCH
Repository: 5.5.0 -> 5.5.1
Reason: Clear Writing 在既有 repository capability 内完成兼容的用户可见质量与 normal-entry 改进，不增加新的 repository-level task/contract。

Affected plugins:
- writing-style: 0.4 -> 0.5
  Reason: 本 refinement 实际改变了正式用户可见行为，新增/正式接入 response-clarity 普通解释路线，并完成复杂科研解释可读性修复、真实回归与 Web 验收；按版本规则必须 exactly once bump。
- all other central plugins: NO_BUMP

Standalone skills: NO_BUMP
Bridge Kit: NO CHANGE
Maturity: NO CHANGE
```

ChatGPT Plugin Creator 显示三段版本是平台规范化：

`source 0.5 -> Web display 0.5.0`

这不改变 repository 两段 plugin version contract。

## 4. Release candidate 的唯一产品来源

正式 release candidate 必须从 `origin/release` 5.5.0 基线构建，但 Clear Writing 行为来源只能来自冻结候选 `fd7a157...`。

允许移植的产品语义只包括已经批准并验证的 Clear Writing 差异：

- 新增 `skills/writing/core/response-clarity/**`；
- `skills/writing/core/chinese-prose/SKILL.md` 中已批准的 ordinary-response routing 调整；
- `scripts/codex_marketplace_config.json` 中 writing-style 自身的：
  - response-clarity skill exposure；
  - 已批准 description/defaultPrompt 变化；
  - version `0.4 -> 0.5`；
- `profiles/codex-writing-style.json` 加入 response-clarity；
- 直接验证上述能力的既有 tests。

不允许从旧 evidence branch wholesale merge/cherry-pick 101 个历史提交，不允许带入旧 control docs、W2 machinery、Presentations、Research Authoring 或其他无关 production drift。

Generated layer 仍服从仓库规则：

- 不手改 `plugins/codex/plugins/writing-style/**`；
- 不手改生成的 registry/catalog/Marketplace payload；
- 先落 source/config，再调用现有 canonical generator；
- generated writing-style 必须与 source/config parity。

## 5. Release metadata

只允许更新与本次正式 release 直接相关的公共 metadata：

### Repository

- `VERSION`: `5.5.0 -> 5.5.1`
- root `CHANGELOG.md`: 新增 `5.5.1 - 2026-10-19`
- `README.md`:
  - Repository / CLI release -> `5.5.1`
  - Clear Writing row -> `v0.5`
  - 用一句自然中文反映普通解释能力已经进入正式 Clear Writing，不写内部 Gate/W2 流水账

### Plugin

- `docs/plugin-changelogs/writing-style.md`: `0.5 - 2026-10-19`
- `Unreleased` 回到 `No pending released changes.`

0.5 changelog 只记录真实用户行为：

- ordinary explanations / diagnostics / progress summaries 获得 `response-clarity` sibling route；
- complex scientific explanations 以完整语义/推理单元组织段落；
- unfamiliar / multi-index objects 先建立受来源支持的 reader model；
- missing definitions 明确暴露而不是猜含义；
- exact-only machine output 保持 activation exemption；
- 真实 ChatGPT Web 4-answer closure PASS；
- claim boundary：不声称每轮后台必然加载 plugin，也不声称 matched causal increment 已证明。

### README Clear Writing 检查

只要 README 被修改，Executor 必须真实调用已安装 Clear Writing 对受影响读者区域做最终语言检查；读取 `SKILL.md` 或 grep 不算。

## 6. Final candidate identity

正式 release candidate 必须区分三类 identity：

### A. 产品行为 identity

下列生产 Skill/support 内容必须与 `fd7a157...` 对应冻结内容一致，不允许 release closure 顺手重写：

- response-clarity；
- writing-fidelity；
- scientific-prose；
- product-ui-copy；
- scientific-rewrite + support script；
- chinese-prose（除已冻结候选本身包含的 routing 差异外）。

### B. repository release metadata

允许且预期变化：

- repository `5.5.1`；
- writing-style `0.5`；
- README/changelog/version/registry/generated manifest 等对应 release metadata。

### C. ChatGPT PRIVATE plugin identity

正式 repository release 完成后，更新**现有** PRIVATE plugin，不创建第二个：

```text
plugin_id = plugins_6ad4fc9abae08191a9ecd81879b2c919
expected version = 0.5.0
scope = USER
discoverability = PRIVATE
```

更新后必须重新记录新的 `current_release_id`。

对 Web release 做实际回读：

- 六个 Skill 文本；
- references/assets/evals；
- `scientific-rewrite/scripts/rewrite_support.py`；
- plugin metadata。

Skill/support payload 与正式 repository generated writing-style 做逐文件 parity。

允许的平台规范化只包括已经观察到并明确记录的 host-owned 差异，例如：

- source `0.5` -> Web display `0.5.0`；
- Plugin Creator 自己序列化的 owner/author 元数据。

除明确列出的 host normalization 外，description、skills、default prompts 或 Skill 文件内容不得漂移。

如果出现其他差异，停止 closure，不创建替代 plugin，不静默接受。

## 7. 最小 Capability Gate Matrix

本 release closure 不重新做产品 Gate；产品 Gate 已完成。这里只有发布一致性 Gate。

| Gate | 证明什么 | 正常证据 | 失败 |
| --- | --- | --- | --- |
| RC1 — scope isolation | formal release 没夹带 main 上无关开发内容 | release candidate 相对正式 5.5.0 baseline 的 allowlist diff | 出现无关 production/plugin/version drift |
| RC2 — candidate identity | 0.5 行为仍是已通过的 frozen candidate | source-to-candidate semantic/file parity + generated parity | skill/support 内容漂移 |
| RC3 — version/docs closure | repo/plugin/version/README/changelog 一致 | 5.5.1 / 0.5 consistency tests + README Clear Writing check | 任一版本或 changelog 不一致 |
| RC4 — final CI | exact formal candidate 机械与回归检查全绿 | focused writing-style + full repository/Marketplace/skill validation + required GitHub CI | exact candidate CI FAIL |
| RC5 — formal release ref | stable channel 指向 exact approved release candidate | canonical producer fast-forward-only + remote SHA/version readback | non-FF、baseline drift、错误 target |
| RC6 — actual GPT release | 真实 PRIVATE Clear Writing 已更新且与 formal release 一致 | same plugin_id, new release_id, 0.5.0, PRIVATE/USER, full payload readback parity | identity/parity/visibility drift |
| RC7 — main reintegration | release commit 被 latest main 吸收且不覆盖无关工作 | release commit 是 main ancestor；Clear Writing/version focused validation | 冲突要求改变无关 plugin 行为 |

不得再新增 Web Gate。

## 8. Final CI

release ref 前必须在 exact release candidate 上执行：

1. writing-style focused tests；
2. source/generated parity；
3. Marketplace/version/changelog/README consistency；
4. full repository test suite；
5. skill validation；
6. required GitHub CI。

这些只能证明正式 release candidate 的机械与回归完整性，不重新解释用户 Web Gate。

不得重跑最终 4-answer Web test。

若 CI 暴露的是 Clear Writing 本 release diff 的真实 failure，停止。
若是正式 release baseline 本身的既有 failure，也停止并归因，不得删测试或改标准绕过。

## 9. 正式发布顺序

在 exact release candidate 经最终独立 Critic PASS 后：

1. 使用现有 `ai-skills-repository-maintainer` formal release producer；
2. 只允许 non-force、fast-forward-only 推进 `refs/heads/release`；
3. target 必须是 exact approved `5.5.1 / writing-style 0.5` release commit；
4. 远端回读 exact SHA、`VERSION=5.5.1`、writing-style `0.5`；
5. 然后更新现有 PRIVATE ChatGPT Clear Writing plugin 到该正式 release；
6. 回读并完成 RC6 parity；
7. 最后把 exact released commit 普通 non-force 合并进当时 latest `main`，保留 main 上无关工作；
8. 冲突只允许在本计划批准的 Clear Writing/release metadata surface 上解决；若必须修改 Presentations、Research Authoring 或其他 production 行为，停止回 Planner；
9. 验证 release commit 成为 main ancestor，并执行 focused version/parity/integration validation。

如果正式 `release` 在第 1 步前已经移动，停止并重新 late-bind；不得 force。

## 10. Issue #13 closure

正式 closure 完成前 Issue #13 始终：

`DOING / writing-style`

只有以下全部成立后才能 DONE：

- formal `release` 已指向 exact `5.5.1 / writing-style 0.5`；
- final CI PASS；
- README/changelog/version 一致；
- released commit 已整合回 main；
- actual PRIVATE plugin 已更新到 `0.5.0`；
- Web plugin payload parity PASS；
- 没有 required downstream consumer pending。

DONE 时记录 exact release commit、PRIVATE plugin `current_release_id`、README check 和 release parity evidence。

当前 GitHub Project field mutation surface 不可用时，只更新 Issue/source evidence，并记录 exact pending mutation，不要求用户手工拖看板。

## 11. 停止条件

以下任一发生即停止，不自行扩 scope：

- `origin/release` baseline/version 漂移；
- writing-style 正式基线已不是 0.4；
- release candidate 出现无关 production drift；
- candidate Skill/support 与 `fd7a157...` 不一致；
- final CI FAIL；
- release target 非 fast-forward；
- PRIVATE plugin 更新产生新 plugin_id、非 PRIVATE、非 USER 或非预期 payload；
- main reintegration 冲突要求修改无关 plugin 行为。

## 12. 下一阶段

本轮只冻结 release-closure 设计，不执行发布。

独立 Critic PASS 后，Planner 再形成同版 execution package（Goal + Kickoff），交 execution-ready Critic。只有 execution-ready PASS 与用户发送批准的短 Codex handoff 后，才允许 Codex/maintainer 实际构建、发布、更新 PRIVATE plugin 和推进 release。
