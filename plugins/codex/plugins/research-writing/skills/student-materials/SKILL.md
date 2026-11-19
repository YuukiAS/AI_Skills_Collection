---
name: student-materials
description: "接收 GPT 已完成的学生正文与制作约束，执行模板套用、Markdown/PDF 渲染、机械检查、打包、发布和回读。"
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
# Student Materials：Codex 制作入口

Codex 职责限于渲染、机械检查、打包、发布和回读。学生任务、课程含义、内容删留、文字写作和语义分组均应由 GPT 在 `student-materials` 中完成，并已调用 Content Selection 与 Clear Writing 的适用规则。

1. 读取完整正文与 [handoff.template.json](references/handoff.template.json)，按 `RA-12` 核对课程来源、接受母版、允许改动、文档家族、语义块和目标文件。
2. 按 [production-contract.md](references/production-contract.md) 执行 `RA-13`，保持正文与已批准约束，完成目标格式制作和机械检查。
3. 需要 ZIP 时按显式组件清单打包；执行证据作为用户附件或仓库文件交付，不进入学生包。
4. 已获得远端写入授权时执行 `RA-14`，发布后回读每个目标文件和实际页面。
5. 在 [execution-evidence.yaml](references/execution-evidence.yaml) 中追加差异、渲染、检查、打包、发布与回读位置，把完整成品和未观察范围交回 GPT。
6. 出现新增课程要求、内容删留、措辞或语义布局决定时，返回具体位置和机械证据，由 GPT 或课程负责人处理。

[production-contract.md](references/production-contract.md)
[handoff.template.json](references/handoff.template.json)
[execution-evidence.yaml](references/execution-evidence.yaml)
