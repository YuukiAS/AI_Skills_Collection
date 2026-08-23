---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 019_research_presentation_exemplar_composition_representation
---

# 019 Research Presentation Exemplar Composition Representation — Request

## Why this task exists

018 的外部方法审计已经确认：当前 Research Presentation 系统最关键的缺口不是继续增加抽象审美规则，而是 reference library 仍主要停留在 prose lesson / RRL trace，无法直接约束生成器的构图决策。

本任务要建立一个**小而真实、机器可用、可审计**的 exemplar composition representation 层，把已经 inspected 的真实科研 slide 转成结构化构图记录，为后续 multi-candidate design search、comparative Terra 和真实 holdout one-shot generation 提供稳定输入。

## User-facing product goal

长期目标仍然是：新的真实科研材料一次调用即可生成接近成熟教授组会 / 顶会 oral 的 PPTX 或 Beamer，而不需要用户逐页纠正基础视觉问题。

019 只解决 reference -> composition 这一层，不提前实现后续 candidate search、comparative review 或 holdout benchmark。

## Scope constraint

只允许使用当前已经 `verification_status=inspected` 的 research presentation reference pages。不得扩 source corpus，不得新增 Source Scout，不得把上一轮 10 页 synthetic pack 提升为 gold exemplar。

任何 composition record 必须绑定真实 reference identity 和 rendered-page checksum；只知道 talk metadata、页码或 prose lesson 不足以创建构图记录。
