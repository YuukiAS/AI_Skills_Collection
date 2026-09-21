# README Human-Facing Refactor v0.1 — Critic Prompt

你是 AI Research Stack 的长期独立 Critic thread。

这是一个新的实质设计轮次。当前只审 README 重构方案，不实现，不修改 README，不创建 Reviewed Handoff task/branch/worktree，不启动 Codex Executor，不运行 paid API，不修改 plugin production source、generated layer 或 Bridge Kit。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: repository human-facing README / workflow-doc dependency cleanup
- design_topic_or_task_key: `readme-human-facing-refactor`
- source_branch_or_ref: latest `main`
- proposal_path_and_version: `docs/design/readme/README_HUMAN_FACING_REFACTOR_V0_1_2026-09-20.md` / v0.1
- proposal_commit: `13667f59cb60a199d9c0ce518b4ff66806370968`
- review_stage: design review

## 强制读取

先实际读取最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- 当前 `README.md`
- `scripts/codex_marketplace_config.json`
- 上述 v0.1 proposal

并独立做针对性外部检索，优先 GitHub 官方 README / Markdown 文档。不要只复述 Planner 的外部依据。

## 用户目标

用户明确要求：

- 根 README 是给人看的；
- 现在太乱；
- “项目 thread 要写多复杂？不用复杂”这类内部措辞不应出现在 README；
- Planner / Critic 的复制模板也不应继续放 README；
- 需要搞清楚 GPT 现在真正从哪里读取 Planner / Critic 规则；
- 新 README 要非常美观；
- 核心只需清楚展示每个中央插件的名字、版本和用途；
- 用户批准后才开始真正重构。

## 重点审查

请独立判断：

1. **方向是否正确**：把根 README 收敛成“项目首页 + 插件画廊”是否真正符合人类读者，而不是把内部流程换一种方式继续堆进去。
2. **是否过重或过简**：两列本地 SVG 插件卡片是否足够美观、稳定、低维护；是否真的需要保留 proposal 中的最小使用入口与 documentation footer，还是还应更简。
3. **删减是否安全**：proposal 计划从 README 删除的维护、HPC、验证、Presentation、Planner/Critic 等内容，是否已有合适 authority，不会因为移出 README 而丢失真正需要的信息。
4. **Planner / Critic 真实读取链**：项目设置 + `AGENTS.md` + 两个 Role Contract + Capability Gate Policy 是否已经构成正常入口；README 是否不再需要承担角色 prompt authority。
5. **旧依赖是否必须伴随修复**：`PLANNER_ROLE_CONTRACT.md` §10.1 与 `CRITIC_ROLE_CONTRACT.md` §6.2 对 README template 的引用是否确实会在删模板后悬空；若要修，proposal 规定只改这两处是否足够、是否最小。
6. **视觉验收是否真实**：最终是否应要求直接看 GitHub 实际 render、窄窗口与 light/dark，而不是只靠 Markdown syntax/CI。
7. **维护成本**：不要因为追求“美观”引入外部 badge 服务、自定义 CSS、新生成器、新 schema 或新的 README 构建链，除非你能证明这些是必要的。
8. **范围控制**：确认本轮不应顺手修改 `AGENTS.md`、Bridge Kit、plugins、profiles、marketplace source/generated payload 或 plugin versions。

这不是 production plugin refinement，因此不要机械要求 Plugin Capability Gate Matrix；但应检查 proposal 自己的 README 验收是否足够直接证明用户看到的最终效果。

## 输出

先用正常中文给出结论与理由，然后给：

- RESULT = PASS | REVISE
- REVIEW_OBJECT = proposal path + v0.1 + exact commit
- BLOCKERS = 若有，使用稳定编号与最小关闭条件
- NON_BLOCKING = 可选建议

如果 REVISE，按 `CRITIC_ROLE_CONTRACT.md` 自动生成完整的下一条 Planner prompt；如果设计 PASS，但还需要 Planner 准备 execution package，同样生成下一条 Planner prompt。

不要实现 README，也不要替用户批准实现。
