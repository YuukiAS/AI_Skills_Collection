---
name: research-notes
description: "接收 GPT 已完成的研究笔记正文，执行 Markdown/PDF 渲染、机械检查、发布与回读，并把实际文件和页面返回 GPT。"
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
# Research Notes：Codex 制作入口

Codex 职责限于渲染、机械检查、发布和回读。读者任务、内容取舍、公式解释、科研判断与文字写作均应由 GPT 在 `research-notes` 中完成，并已调用 Content Selection 与 Clear Writing 的适用规则。

1. 读取完整正文与 [handoff.template.json](references/handoff.template.json)，按 `RA-12` 核对候选身份、允许改动和目标文件。
2. 按 [production-contract.md](references/production-contract.md) 执行 `RA-13`：保持正文，完成目标格式制作并运行机械检查。
3. 已获得远端写入授权时执行 `RA-14`，发布后回读实际文件和目标页面。
4. 在 [execution-evidence.yaml](references/execution-evidence.yaml) 中追加渲染、检查、发布与回读位置，随后把完整成品、全部目标页面和未观察范围交回 GPT。
5. 内容或表达需要变化时，返回具体冲突位置和机械证据，由 GPT 修订正文后继续制作。

[production-contract.md](references/production-contract.md)
[handoff.template.json](references/handoff.template.json)
[execution-evidence.yaml](references/execution-evidence.yaml)
