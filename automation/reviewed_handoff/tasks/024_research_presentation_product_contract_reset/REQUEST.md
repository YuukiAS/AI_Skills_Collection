---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 024_research_presentation_product_contract_reset
---

# 024 Research Presentation Product Contract Reset — Request

## Why this task exists

长期 Research Presentation 产品目标已经重新冻结为：普通用户只提供真实科研 paper 或等价材料，在未显式指定其他格式时，一次调用 `research-presentations` 应优先生成基于 canonical CUHK Beamer source 的 `.tex + PDF`，而不是默认进入 editable PPTX/scaffold 路线。

当前仓库仍存在明确矛盾：

- active `research-presentations/SKILL.md` 明确写着未指定格式的 group meeting / research update / research slides 默认 editable Presentation/Slides；
- `shared/template-routing.md` 与 `shared/ppt-skill-routing.md` 仍锁定相同旧默认；
- `shared/scripts/markdown_to_deck_plan.py` 的默认 `output` 仍为 `pptx`，对应测试也把这一行为当成正确契约；
- 但 `shared/templates/cuhk/README.md` 已明确 `beamer/source/` 才是 exact CUHK canonical source，derived PPTX scaffold 只用于 non-exact workflow；
- `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 已明确第一成熟 production route 默认 exact CUHK Beamer/PDF。

如果不先关闭这个矛盾，后续即使 Gold Composition Library 和 CUHK scientific layouts 做得再好，普通用户入口仍可能走到错误的旧 PPTX 路线，形成“内部能力存在、production entrypoint 不消费”的假完成。

## User-facing product goal

完成本任务后，普通科研组会、paper talk、research update 等请求在**未指定格式**时，应稳定路由到 exact CUHK Beamer source，并以 `.tex + PDF` 作为第一成熟默认交付。

用户如果明确要求 PowerPoint、`.pptx`、editable、Google Slides 或后续手工编辑，仍应保留 editable Presentation/Slides 路线；本任务不是删除 PPTX 能力，而是纠正默认优先级。

## Scope constraint

本任务只负责产品合同、路由与回归测试一致性：

- 修改正式 `research-presentations` source skill 及必要 shared routing 文档；
- 修改真正承担默认 output contract 的 adapter / schema-facing logic（若需要）；
- 更新相关 tests，使默认科研路由与 Program Goal 一致，同时保留显式 PPTX/Slides override；
- 明确 exact CUHK 只来自 `templates/cuhk/beamer/source/`，derived `design-tokens.json` / PPTX scaffold 不得作为 exact production source；
- regenerate 必要的 generated marketplace/plugin mirror，并验证 source/generated 一致性。

本任务不得：

- 修复或恢复 023 renderer；
- 建立新的 layout/macros；
- 扩 reference corpus 或做 Gold Composition Library；
- 开始 statistical / medical-imaging holdout；
- 修改 Terra core 或 comparative review 机制；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

024 PASS 只表示 Stage 1 — Product Contract Reset 完成。之后 Planner 才能创建 Stage 2。
