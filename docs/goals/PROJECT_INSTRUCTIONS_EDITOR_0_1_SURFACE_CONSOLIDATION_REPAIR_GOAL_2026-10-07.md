# Project Instructions Editor 0.1 — Surface Consolidation Repair Goal

在 `YuukiAS/AI_Skills_Collection` 的：

```text
work/project-instructions-editor--0.1-closure
```

完成 PIE 0.1 发布前最后一个 bounded repair。

本轮不走新的 Critic，不创建 C12，不修改 Clear Writing，不引入 MCP/API/外部 finalizer，不重新做 C5–C11 的普通英文逐词追杀。

先读取最新：

```text
AGENTS.md
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_1_SURFACE_CONSOLIDATION_REPAIR_V0_1_2026-10-07.md
skills/core/codex-system/project-instructions-editor/SKILL.md
skills/core/codex-system/project-instructions-editor/references/editor-contract.md
docs/skill-todos/project-instructions-editor.md
```

再只读取设计文档点名的 C5/C7/C9/C10/C10-B3/C11 历史证据，不扩展成全历史审计。

## 修复目标

解决最新真实 Server+VPS 输出暴露的问题：

> PIE 0.1 在收缩跨轮 reader-layer 职责后，过度保守地保存 source wording 和规则，导致当前 Project setting 自身出现结构膨胀、重复长期语义、内部合同化和 source-label echo。

不要把它重新解释成“又有几个英文词没翻译”。

实现设计文档中的三项机制：

1. **Durable Meaning Map**：写 candidate 前按长期语义而不是 source 段落建立内部 meaning map，区分 `PROJECT_DIRECT / PROJECT_BRIDGE / SOURCE_ONLY / TASK_ONLY / OMIT`。
2. **Semantic Consolidation Pass**：按语义效果去重；同 trigger/owner/force/failure behavior 的长期规则只保留一个主要表达；不同授权/安全/证据边界不得强行合并。
3. **Surface Expansion + Coverage/Redundancy Gate**：candidate 扩张必须对应新增或修复的长期语义；最终逐段检查“去掉这段到底会丢哪个独立长期语义”，重复 source explanation / audit rationale / volatile inventory 必须合并或移出 Project。

同时恢复一个窄的 current-artifact language contract：

- PIE 不保证未来每轮聊天的最终阅读层；
- 但它当前生成的 Project setting 应按该 Project 的 durable language 表达普通概念；
- formal product/repo/protocol/command/path/file/field/state/version/exact UI string 保持精确；
- 不做 Latin-token scan、禁词表、比例、翻译表；
- 少量孤立普通英文不单独阻断 0.1；
- 但大面积 source English labels 继续组织 setting、导致它像内部审计合同，仍属于 PIE current-artifact defect。

## 重点修改

优先修改：

```text
skills/core/codex-system/project-instructions-editor/SKILL.md
skills/core/codex-system/project-instructions-editor/references/editor-contract.md
tests/test_project_instructions_editor_contract.py
```

必要时新增一个 public-safe structural fixture：

```text
tests/fixtures/project_instructions_editor/semantic_consolidation_regression.json
```

fixture 必须测试“重复语义 + volatile inventory + protected absence + exact identities + auth/privacy/evidence”，不能测试固定词汇、固定章节数或英文计数。

正常用户输出合同也要收敛：`preservation-sensitive`、meaning map、内部 disposition、完整 invariant checklist 默认不向用户展示。普通编辑请求先短结论，再给 replacement 和少量关键变化；只有用户明确要求 formal audit 才暴露内部审查字段。

## 必须保护

任何修复都不得破坏：

- live setting precedence；
- bounded edit 默认；
- R5 protected absence；
- R6 no-op eligibility；
- semantic ownership / effective enforcement；
- canonical locator bridge；
- mandatory/optional force；
- authorization / safety / privacy / evidence strength / uncertainty / completion；
- exact identifiers；
- missing evidence 时的 honest degradation；
- greenfield / explicit reset；
- non-Chinese Project 不被强制中文。

不得把 deletion/rejection history 变成新的长期 tombstone rule。

## 测试

至少：

```text
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
python scripts/skills.py validate
```

再运行与本次 source/generated parity 直接相关的生成/校验。

现有 C5–C11 只作为 known development regression。不要重新宣称它们是 fresh。

在本地/任务 runtime 做一个完整 public-safe replay，人工审最终 replacement：

- 不应因为 source 有很多章节就自动变成更多章节；
- 重复 ownership/current-source/auth/reporting 语义应合并；
- volatile inventory 应变成 locator bridge；
- protected absence / exact identity / authorization / privacy / evidence 不漂移；
- 当前 setting 普通正文按目标 Project 语言表达；
- 不依靠关键词/section count 判 PASS。

## Wrapper

当前 Web personal wrapper：

```text
plugin_id=plugins_6ac24c3637188191937fe99610ace3f2
wrapper_version=0.2.2
Skill version=0.1
```

修复通过后准备 wrapper `0.2.3` update candidate，内嵌同一最终 PIE 0.1 source。

如果当前 Codex 没有 Plugin Creator，只准备 archive + exact handoff，不声称已更新网页插件。

## 最终 Server+VPS 验收

完成 source、tests 和 wrapper candidate 后停止仓库修改，给出唯一下一步：更新 Web wrapper 后在真实 Server+VPS Project fresh thread 运行冻结自然请求。

这次真实验收关注：

- preservation-sensitive；
- bounded consolidation / justified no-op；
- semantic consolidation；
- source ownership / locator；
- protected absence；
- authorization/privacy/safety/evidence/completion/exact identifiers；
- no unsupported durable rules；
- candidate 不因 source 复杂度无理由膨胀；
- setting 不再系统性照抄 source/audit labels。

单个英文 token、未来跨轮中文稳定性、未来回复机械换行不作为 PIE 0.1 blocker，继续交 Clear Writing #13。

如果上述结构性与保真能力 PASS，才完成 PIE 0.1 -> main/release 5.5.0 closure。

## Stop rule

一旦发现实现方向变成：

- 新英文词规则；
- Latin-token mandatory scan；
- 固定翻译表；
- section-count gate；
- chinese-prose sibling chain；
- external finalizer；
- Server+VPS 特判；

立即停止并报告偏离设计。

最终只报告：

```text
FINAL_SOURCE_COMMIT=
PIE_SKILL_VERSION=0.1
STRUCTURAL_CONSOLIDATION_REPAIR=
FOCUSED_TESTS=
WRAPPER_CANDIDATE=
SERVER_VPS_ACCEPTANCE_READY=
C11_READER_LAYER_FAILURE_PRESERVED=YES
```
