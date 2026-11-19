---
name: research-story
description: "接收 GPT 已完成的研究故事正文，执行 Markdown/PDF 渲染、机械检查、发布与回读，并把实际文件、表图和全部页面返回 GPT。"
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
# Research Story：Codex 制作入口

Codex 职责限于渲染、机械检查、发布和回读。研究问题、内容取舍、证据解释、故事组织与文字写作均应由 GPT 在 `research-story` 中完成，并已调用 Content Selection 与 Clear Writing 的适用规则。

1. 读取完整正文与 [handoff.template.json](references/handoff.template.json)，按 `RA-12` 核对来源、候选身份、表图角色、允许改动和目标文件。
2. 按 [production-contract.md](references/production-contract.md) 执行 `RA-13`，保持正文和科研关系，完成目标格式制作及机械检查。
3. 已获得远端写入授权时执行 `RA-14`，发布后回读文件、表图资源和目标页面。
4. 在 [execution-evidence.yaml](references/execution-evidence.yaml) 中追加渲染、检查、发布与回读位置，把完整成品、全部页面和未观察范围交回 GPT。
5. 结果、比较资格、故事主线或措辞需要变化时，返回具体位置和机械证据，由 GPT 决定修订。

[production-contract.md](references/production-contract.md)
[handoff.template.json](references/handoff.template.json)
[execution-evidence.yaml](references/execution-evidence.yaml)
