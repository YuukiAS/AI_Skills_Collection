# README row copy

用于创建、修改、压缩、同步和重构长期 ChatGPT Project instructions。开始编辑前会要求提供完整当前设置；发生修改时同时给出易读的修改预览和可直接替换的完整结果，并保护已有决定、事实来源和权限、安全、证据边界。

# Tracking Issue

Title: Project Instructions Editor 0.2：真实基线与可审阅修改预览

## 目标

为 `project-instructions-editor` 0.2 增加两个边界明确的改进：编辑前必须取得用户提供的完整当前 Project setting；每次真实修改同时交付易读的 Markdown 修改预览和完整干净结果。

## 范围

- 缺少完整当前设置时，只请求该原文，不根据 Project 上下文、Memory、历史聊天、仓库文件、片段或模型推断重建。
- 用户明确说明当前设置为空时，按完整 greenfield baseline 处理。
- explicit reset 仍要求当前 baseline，但不再承担保留旧设置语义的义务。
- 修改预览与完整结果来自同一个 baseline 和同一个真实修改。
- 保留 0.1 的现有设置保护、事实来源归属、授权、安全、隐私、证据、精确标识、预算、protected absence 和 no-op 合同。

## 边界

本轮只准备 0.2 候选与独立 implementation review 材料，不更新 live personal wrapper，不执行真实 ChatGPT Web acceptance，也不发布 release。

Canonical source: `docs/skill-todos/project-instructions-editor.md`

Implementation branch: `reviewed/project-instructions-editor--0.2-baseline-diff-contract`
