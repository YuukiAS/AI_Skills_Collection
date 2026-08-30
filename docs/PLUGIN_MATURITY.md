# Plugin Capability Status

本文件记录 **可选的能力状态说明**，不替代 repository release SemVer，也不替代每个 plugin 自己的 SemVer。

长期主线是：

```text
plugin version + plugin changelog + real-task evidence
```

status 只在它能帮助用户理解“现在是否适合作为日常默认工具”时使用。不要为了填表强迫每个 plugin 经过固定的 `alpha -> beta -> stable` 梯子。

## Status vocabulary

- `unclassified`：尚未做统一真实任务状态判断；不代表质量差。
- `baseline`：核心 production path 已存在，可以进入真实项目持续 refinement，但仍明确存在基础质量/泛化缺口。
- `alpha`：用户已经在真实 production workflow 中把它作为可用工具使用，核心任务能完成，但仍预期持续暴露和修复非边缘问题。
- `stable`：多个独立真实项目长期正常使用；普通入口可靠；人工修改主要是项目科学判断而不是基础工作流/模板/布局/语言修补。

不使用 `beta` 作为强制中间层。将来如果真实产品需要更多 status，再基于需求增加，不提前设计复杂 maturity taxonomy。

Status 只能由真实任务、真实 artifact/render 和用户验收改变。Synthetic / mechanical / CI PASS 不能单独提升 status。

## Current status

| Plugin | Status | Basis |
|---|---|---|
| `presentations` | `baseline` | Stage 1–4 production path 已成立，但 041 真实 frozen batch 未通过；043 已暂停。下一步直接用于现有 CAT-TRACE deck refinement，真实使用后再决定是否进入 `alpha`。 |
| `research-writing` | `unclassified` | Distributed Imaging Inference 的 advisor-report 反馈已进入 active `research-reporting`；等待下一份独立真实报告验证。 |
| `writing-style` | `unclassified` | 尚未做统一跨项目状态判断。 |
| `workflow-core` | `unclassified` | 尚未做统一跨项目状态判断。 |
| `ai-skills-core` | `unclassified` | 等待独立 version/changelog/maintenance workflow 在真实长期维护中验证。 |
| `scientific-visualization` | `unclassified` | 尚未做统一跨项目状态判断。 |
| `web-development` | `unclassified` | 尚未做统一跨项目状态判断。 |
| `statistical-modeling` | `unclassified` | 尚未做统一跨项目状态判断。 |
| `bioinformatics` | `unclassified` | 尚未做统一跨项目状态判断。 |
| `medical-imaging` | `unclassified` | 尚未做统一跨项目状态判断。 |

## Status change rules

- `baseline -> alpha`：用户在真实正常入口中把 plugin 用于目标工作流并明确认为已经“可用”，即使后续仍会继续完善；不能靠 synthetic acceptance 代替。
- `alpha -> stable`：多个独立真实任务长期稳定；相同基础问题不再反复出现；用户愿意把它当成默认长期工具。
- 允许降级：真实 production 暴露系统性 regression 时，应记录 blocker 或降低 status，而不是拿旧 PASS 维持标签。

Status 改变本身不要求 plugin version bump；只有 runtime/user-visible behavior 真的改变时才按 `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md` bump SemVer。
