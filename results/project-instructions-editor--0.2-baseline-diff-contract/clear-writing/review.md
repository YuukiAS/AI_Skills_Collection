# Clear Writing invocation record

Invocation identity: installed `writing-style` 0.4, skill `chinese-prose`

Reviewed surface: root README Project Instructions Editor row and the new 0.2 tracking Issue draft.

The bounded `ai-bridge plugin-replay` attempt was not consumed because its write-isolation probe returned `WRITE_ISOLATION_NOT_ENFORCEABLE`. The active Codex session then invoked the installed `writing-style:chinese-prose` skill directly and applied its README/public-writing workflow to the frozen draft.

## Protected facts

- Product and slug: `Project Instructions Editor`, `project-instructions-editor`
- Candidate version: `v0.2`
- Product surface: `ChatGPT Project instructions`
- Complete user-supplied current setting is required before editing; explicit empty is valid greenfield input.
- Every real change returns a readable Markdown preview and complete clean final from the same baseline and edit.
- PIE 0.1 semantic protections remain in scope.
- This task does not update the live wrapper or complete live Web acceptance.

## Adopted reader-facing copy

README:

> 用于创建、修改、压缩、同步和重构长期 ChatGPT Project instructions。编辑前会先取得当前设置的完整原文；实际修改时，会同时给出易读的修改预览和可直接替换的完整结果，并保护已有决定、事实来源以及授权、安全和证据边界。

Issue title:

> Project Instructions Editor 0.2：真实基线与可审阅修改预览

Issue body:

> ## 目标
>
> 为 `project-instructions-editor` 0.2 增加两个边界明确的改进：编辑前必须取得用户提供的当前 Project setting 完整原文；每次实际修改都同时交付易读的 Markdown 修改预览和完整干净结果。
>
> ## 范围
>
> - 缺少完整当前设置时，只请求该原文，不根据 Project 上下文、Memory、历史聊天、仓库文件、片段或模型推断重建。
> - 用户明确说明当前设置为空时，将其作为从零创建的完整基线。
> - 明确重置仍要求当前基线，但不再保留旧设置的语义。
> - 修改预览与完整结果来自同一个基线和同一次真实修改。
> - 保留 0.1 对现有设置、事实来源归属、授权、安全、隐私、证据、精确标识和预算的保护，也继续保留已删除规则不自动恢复与“无需修改”判断。
>
> ## 边界
>
> 本轮只准备 0.2 候选和独立实现审查材料，不更新现有个人 Plugin，不执行真实 ChatGPT Web 验收，也不发布正式版本。
>
> Canonical source: `docs/skill-todos/project-instructions-editor.md`
>
> Implementation branch: `reviewed/project-instructions-editor--0.2-baseline-diff-contract`

Result: reader-facing wording is concise, facts and technical literals are unchanged, and internal Gate labels are omitted from README copy.
