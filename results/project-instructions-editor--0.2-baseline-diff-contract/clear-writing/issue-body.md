## 目标

为 `project-instructions-editor` 0.2 增加两个边界明确的改进：编辑前必须取得用户提供的当前 Project setting 完整原文；每次实际修改都同时交付易读的 Markdown 修改预览和完整干净结果。

## 范围

- 缺少完整当前设置时，只请求该原文，不根据 Project 上下文、Memory、历史聊天、仓库文件、片段或模型推断重建。
- 用户明确说明当前设置为空时，将其作为从零创建的完整基线。
- 明确重置仍要求当前基线，但不再保留旧设置的语义。
- 修改预览与完整结果来自同一个基线和同一次真实修改。
- 保留 0.1 对现有设置、事实来源归属、授权、安全、隐私、证据、精确标识和预算的保护，也继续保留已删除规则不自动恢复与“无需修改”判断。

## 边界

本轮只准备 0.2 候选和独立实现审查材料，不更新现有个人 Plugin，不执行真实 ChatGPT Web 验收，也不发布正式版本。

Canonical source: `docs/skill-todos/project-instructions-editor.md`

Implementation branch: `reviewed/project-instructions-editor--0.2-baseline-diff-contract`
