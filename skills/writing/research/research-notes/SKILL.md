---
name: research-notes
description: "为用户本人撰写可复习的研究笔记和方法说明，讲清对象、公式、计算链、证据边界与项目用途；GPT 完成内容判断和写作，Codex 仅承接制作。"
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed: null
last_reviewed: 2026-11-19
profile_tags:
  - research-writing
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Research Notes

用于用户本人学习、复习、理解方法或整理个人研究判断。普通科研问答只有在用户要求形成可持续阅读的笔记、方法说明或正式文档时进入本技能。

## 执行顺序

**RA-01｜绑定读者与任务。** 记录用户要学懂或日后重建的具体问题、权威来源、目标格式、语言、最新接受稿和编辑范围。读者任务足以确定内容时直接继续。

**RA-02｜恢复科学对象与计算。** 在重要结果前说明方法身份、对象层级、假设、输入、计算步骤和输出。读取 [research-notes.md](references/research-notes.md) 处理公式、符号、推导和邻近比较。

**RA-03｜绑定主张与证据。** 区分来源事实、观察结果、解释、假设、限制与计划；数字、公式、比较条件和结论保持正确对应。

**RA-04｜形成可独立复习的理解链。** 当前文档应包含必要定义、中间步骤、直觉、适用条件和项目用途。外链承担来源或延伸阅读，正文承担核心解释。

**RA-07｜调用 Content Selection。** 制作前应用 `CS-03`～`CS-07` 形成唯一内容计划；取得真实成品后应用 `CS-08`、`CS-09` 查看完整对象，并按 `CS-10` 写入同一执行证据文件。

**RA-08｜调用 Clear Writing。** 连续成稿应用 `CW-03`～`CW-08`、`LF-01`～`LF-10`；涉及已有笔记或精确内容时同时应用 `FI-01`～`FI-11`。科研含义仍由本技能确认。

**RA-09｜保护接受基线。** 局部修订恢复真正的接受稿、有效批注、被拒内容和允许改动范围。范围外内容保持原有身份。

**RA-10｜处理后续结果与双语版本。** 待完成结果保留准确位置和状态；结果到来后更新对应事实与解释。双语稿分别可独立阅读，并保持数字、公式和结论强度一致。

**RA-15｜交付执行证据。** 本技能被调用时，使用 [execution-evidence.yaml](references/execution-evidence.yaml) 为每条实际应用规则写“规则编号 → 成品中的原句或位置”；发生改写时填写改前与改后。GPT 将证据文件作为回答附件交付。未调用本技能时不创建该文件。

## 制作交接

需要渲染、机械检查、发布或回读时，填写 [handoff.template.json](references/handoff.template.json)，再交给 [Codex 制作入口](codex-entry.md)。制作约束见 [production-contract.md](references/production-contract.md)。
