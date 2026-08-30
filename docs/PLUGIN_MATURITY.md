# Plugin Capability Maturity

本文件只记录能力成熟度，不替代 repository / Marketplace SemVer。

## Maturity definitions

- `experimental`：能力仍在探索，正常用户不应依赖其稳定行为。
- `alpha`：核心 production path 已存在，适合真实使用与持续 refinement，但仍存在已知泛化/质量缺口。
- `beta`：已在多个独立真实任务中稳定工作，主要问题是边缘情况和 polish，而不是核心工作流经常失败。
- `stable`：普通用户自然调用可稳定获得成熟 artifact；真实任务回归长期稳定；失败会明确 fail closed，不依赖项目特例。

成熟度只能由真实任务、真实 artifact/render 和用户验收提升。Synthetic / mechanical / CI PASS 不能单独提升 maturity。

## Current status

| Plugin | Maturity | Basis |
|---|---|---|
| `presentations` | `alpha` (`Base v1`) | Stage 1–4 production path 已成立；041 四篇真实 frozen batch 未通过；043 已在执行前暂停，后续改由真实 TRACE / research presentation feedback 驱动。 |
| `research-writing` | `unclassified` | 已有 Distributed Imaging Inference 等真实 advisor-report 反馈进入 active `research-reporting`，但尚未做跨项目 maturity audit。 |
| `writing-style` | `unclassified` | 待真实跨项目 maturity audit。 |
| `workflow-core` | `unclassified` | 待真实跨项目 maturity audit。 |
| `ai-skills-core` | `unclassified` | 待安装/维护任务 maturity audit。 |
| `scientific-visualization` | `unclassified` | 待真实跨项目 maturity audit。 |
| `web-development` | `unclassified` | 待真实跨项目 maturity audit。 |
| `statistical-modeling` | `unclassified` | 待真实跨项目 maturity audit。 |
| `bioinformatics` | `unclassified` | 待真实跨项目 maturity audit。 |
| `medical-imaging` | `unclassified` | 待真实跨项目 maturity audit。 |

`unclassified` 不表示质量差，只表示当前没有经过同一套真实任务成熟度审计；不要为了填表而猜测 beta/stable。

## Promotion rules

- `experimental -> alpha`：正常 production entry 已存在，至少一个真实任务成功产生可验收 artifact，且已知严重失败有 fail-closed 路径。
- `alpha -> beta`：至少多个独立真实项目使用；相同基础问题不再反复出现；人工修改主要集中在项目科学判断，而不是基础模板/布局/流程语言。
- `beta -> stable`：跨项目 replay/generalization 持续通过，正常用户入口稳定，重大 regression 有真实回归集，用户明确认可作为长期默认工具。

降级是允许的：如果真实用户任务暴露系统性 regression，应降低 maturity 或记录 blocker，而不是拿旧 CI/PASS 维持标签。
