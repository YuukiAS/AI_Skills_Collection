# 全仓生成一致性的跨插件语义阻断

## 结论

当前任务不能按 recovery Plan 直接提交 Presentations / Research Writing 的 generated-only 同步。现有 canonical source 与已提交 generated payload 表达了不同的专业行为；选择保留哪一侧需要对应领域负责人判断，已触发冻结计划的 `NEEDS_GPT_PLANNER` 停止条件。

Clear Writing 的最小修复仍在批准范围内：`response-clarity` 只增加回答停止条件和来源/建议分层，现有合同测试锁定这两项语义，同源 generated mirror 与 source 哈希一致。

## 复现

同步 `origin/main@58ee18cd3e68df77c35b314c5cf9b0e83a985423` 后，在候选 `3212a6a088352dee5e15dc0ee1ffc6a0ac0c8fc4` 上运行：

```text
python3 -B scripts/build_codex_marketplace.py --validate --check --path-report
```

加入本次 `response-clarity` source 修改后，检查报告 17 项差异：16 项是第一轮审查已记录的 Presentations / Research Writing 漂移，1 项是本次尚待生成的 `response-clarity` mirror。

随后按 Critic 批准的机械生成探针运行：

```text
python3 -B scripts/build_codex_marketplace.py --write --validate --check --path-report
```

生成器本身成功且二次检查为 clean，但实际工作树变化包含 6,242 行删除。关键语义差异包括：

- 删除 Presentations generated payload 中 7 份执行、累计验收、独立审查和返修合同；
- `plugins/codex/plugins/presentations/skills/business/SKILL.md` 从 `last_reviewed: 2026-10-06` 回退到 `2026-07-13`，并删除非平凡演示文稿的执行前 runbook、golden-page、独立审查和整套回归要求；
- `plugins/codex/plugins/presentations/skills/research/SKILL.md` 从 `last_reviewed: 2026-10-06` 回退到 `2026-07-28`，并删除冻结 authority、patch manifest、独立验证和多项返修约束；
- 删除 Research Writing generated payload 中 6 份 student-assessment 累计验收与交付合同。

这些不是标点、顺序或无语义镜像噪声。虽然现有生成器会从当前 source/config 确定地产生这些字节，但 source 与 generated payload 已经代表实质不同的专业行为。独立 Critic 的批准明确要求在此情形停止，不得把“机械生成”当作跨过领域 owner 的授权。

## 已采取的边界保护

- 未修改 Presentations / Research Writing 的 `skills/**` source、映射、路由、版本、profile、changelog 或 README；
- 未提交上述跨插件 generated 删除；
- 已只撤回本轮生成器造成的 `plugins/codex/plugins/presentations/` 与 `plugins/codex/plugins/research-writing/` 工作树变化；
- 保留了 Clear Writing source、同源 generated mirror、合同测试和公开安全回放证据；
- 未运行或重跑 required GitHub CI，因为当前全仓生成检查仍会在同一 16 项语义漂移上失败；
- 未修改 `VERSION`，未删除合法 TODO，未弱化或跳过测试。

## Planner 需要解决的事实

对应领域负责人必须先确定 Presentations / Research Writing 的真实 canonical behavior，并以获授权的 source-first 变更或其他正式集成方式消除 source/generated 分歧。当前 Clear Writing 任务可以继续消费已获批准的权威修复，但不能替两个领域选择应保留的新旧专业合同。

在该分歧解决前，不应消费第二轮 Reviewer，也不能把 focused test 或 Clear Writing 局部回放描述成 full CI PASS。

## 当前验证结果

以下局部检查通过：

- `python3 -B -m unittest tests.test_skill_runtime_text_audit`：8 项通过；
- `python3 -B -m unittest tests.test_codex_marketplace.CodexMarketplaceTests.test_writing_style_exposes_response_clarity_without_renaming_existing_skills`：1 项通过；
- `python3 -B scripts/skills.py validate`：156 个 active skills、18 个 profiles 通过；
- `python3 -B scripts/build_codex_marketplace.py --validate --path-report`：10 个插件、30 个 active skills、Windows 路径预算通过；
- `skills/writing/core/response-clarity/SKILL.md` 与同源 generated mirror 的 SHA-256 均为 `c3d3f9f10ddb1d709f000de8ae670785314fe67a14cd53f4c86985d0980fbe10`。

撤回跨插件 generated 探针后，`python3 -B scripts/build_codex_marketplace.py --validate --check` 精确恢复为上述 16 项既有 Presentations / Research Writing 差异，没有残留新的 `writing-style` 差异。该命令退出 1，故全仓生成一致性仍未通过。

Repository bump decision: NONE

Affected plugins:

- `writing-style`: NO_BUMP；当前只是未通过全仓门槛的修复候选；
- `presentations`: NO_BUMP；未修改 source，未提交 generated 探针；
- `research-writing`: NO_BUMP；未修改 source，未提交 generated 探针；
- `ai-skills-core`: NO_BUMP；未修改 production behavior；
- `workflow-core`: NO_BUMP；未修改 production behavior。
