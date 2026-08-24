---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 024_research_presentation_product_contract_reset
decision: PLAN_FROZEN
---

# 024 Research Presentation Product Contract Reset — Plan

## Frozen decisions

本 Plan 只关闭 Stage 1 的 production-contract 矛盾。不得把它扩成 layout、reference-library、renderer 或 holdout 任务。

## Frozen objective

让正式 `research-presentations` 产品合同、共享路由、默认 deck-plan output 和回归测试与当前 Program Goal 一致：

```text
unspecified research group meeting / paper talk / research update
-> exact CUHK Beamer route
-> canonical templates/cuhk/beamer/source/
-> source-editable .tex + rendered PDF
```

同时保留显式 PowerPoint / `.pptx` / editable / Google Slides 请求的 editable Presentation/Slides 路线。

## Required reading

Executor 至少读取：

- `automation/reviewed_handoff/schema.json`
- `automation/reviewed_handoff/README.md`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- 本任务 `REQUEST.md` / `PLAN.md` / `CURRENT.json`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/template-routing.md`
- `skills/tools/documents-media/presentations/shared/ppt-skill-routing.md`
- `skills/tools/documents-media/presentations/shared/scripts/markdown_to_deck_plan.py`
- `skills/tools/documents-media/presentations/shared/templates/cuhk/README.md`
- `tests/test_presentations.py`
- marketplace source config / generated presentations plugin paths as needed for regeneration

## Implementation scope

### 1. Reset the research default route

修改正式 source contract，使以下语义一致：

- 未指定格式的 group meeting、research update、paper talk、journal club、seminar、defense、methods/results update、research slides：默认 exact CUHK Beamer / `.tex + PDF`；
- 显式要求 PPT、PowerPoint、`.pptx`、editable、Google Slides、later manual editing：仍走 editable Presentation/Slides；
- 显式要求 Beamer / LaTeX / `.tex` / academic PDF：仍走 Beamer；
- outline/storyline-only：仍可停在 deck plan；
- business / teaching / executive 等非 research 默认路由不得被本任务无关改变。

删除或改写与新产品合同直接冲突的旧文案，例如“Do not default academic or research decks to Beamer”以及无格式科研组会默认 editable PPTX 的规则。

### 2. Make the default deck-plan output consistent

`markdown_to_deck_plan.py` 当前默认 `output="pptx"`。对 research presentation 的普通默认调用，调整为与新合同一致的 source-editable LaTeX route。

要求：

- 默认 research call 的 metadata 应反映 `.tex` / source-editable route；
- 显式 `output="pptx"` 仍必须得到 `pptx` + `editable`；
- 显式 `output="tex"` 行为保持正确；
- 不通过隐藏 benchmark flag 或 test-only branch 实现。

如果 Executor 发现该 shared adapter 同时承担不应改成 Beamer 的非 research production path，必须只做最小 research-aware routing，而不能全局破坏其他场景；若无法从现有接口安全区分，应进入 `NEEDS_GPT_PLANNER`，不得猜。

### 3. Lock exact CUHK source semantics

路由文档与 skill 必须明确：

- exact/default academic research deck 使用 `shared/templates/cuhk/beamer/source/` 的真实 `main.tex + styles + assets`；
- `design-tokens.json`、`beamer/main.tex`、`pptx/build_reference_deck.py`、`pptx/cuhk-reference-deck.pptx` 只属于 derived / non-exact / test scaffold；
- 不得把 derived PPTX scaffold 描述为 exact CUHK production source；
- 本任务不修改 canonical CUHK template 本体的视觉设计。

### 4. Update deterministic routing regression tests

更新/增加 targeted tests，至少证明：

1. 普通 research/group-meeting 默认 output 不再是 PPTX，而是 `.tex` / source-editable；
2. 显式 PPTX override 仍是 editable；
3. 显式 TeX route 仍正确；
4. source skill、`template-routing.md`、`ppt-skill-routing.md` 不再包含旧的“无格式科研默认 editable PPTX”产品合同；
5. exact CUHK canonical-source 语义与 `templates/cuhk/README.md` 一致；
6. source/generated presentations plugin mirror 保持一致。

测试只验证 Stage 1 产品合同，不用 synthetic deck、Terra 或视觉评分冒充最终质量。

### 5. Regenerate generated layer from source

若 source skill/shared 文件变化会影响 generated Codex plugin：

- 先修改 `skills/` source；
- 使用仓库现有 marketplace builder 重新生成 `plugins/codex/plugins/presentations/...` 与必要 generated files；
- 不手工维护 generated mirror 作为独立 source of truth。

## Out of scope

024 不得：

- 修改或 recovery `023_research_presentation_deck_design_system_integration`；
- 新增 scientific layout/macros/TikZ composition；
- 扩 reference corpus、重新 inspect 大批 slide 或创建 Gold Composition Library；
- 修改 019–022 的历史 artifacts/机制；
- 修改 Terra core / Bridge Kit reviewer semantics；
- 运行 Stage 5 真实 paper holdout；
- 宣告整套 Presentation 系统成熟。

## Validation

Executor 至少运行：

- Presentation targeted unit tests；
- `python -m unittest discover -s tests`；
- `python scripts/skills.py validate`；
- marketplace build `--write --validate --check --path-report`；
- Reviewed Handoff validation（按仓库现有命令）；
- `git diff --check`。

若本地 Python/命令名不同，使用仓库当前已验证 runtime；不要因为环境差异改变产品语义。

## Acceptance gates

Planner 只有在以下全部成立时才可 PASS 024：

1. active `research-presentations` 对无格式科研组会/论文汇报的默认路由已明确改为 exact CUHK Beamer / `.tex + PDF`；
2. `template-routing.md` 与 `ppt-skill-routing.md` 与该默认一致，不再保留相反规则；
3. 普通 research deck-plan 默认 output 与该 contract 一致，且不是 test-only behavior；
4. 显式 editable PPTX/Slides 请求仍能稳定 override 默认；
5. exact CUHK canonical source 与 derived/non-exact scaffold 的边界清楚且没有倒置；
6. targeted tests 同时覆盖默认 route 与显式 override；
7. source/generated presentations plugin 内容同步；
8. 全库必需 tests / validation / CI 通过；
9. diff 未开始 Stage 2、未修 023、未引入新 renderer/layout/reference corpus；
10. `RESULT.md` 能明确说明普通用户以前会走什么、现在会走什么，以及如何显式请求 PPTX。

024 PASS 只关闭 Stage 1。Planner PASS 后按 Program Goal 创建 Stage 2 — Gold Scientific Composition Library 的独立 bounded task；不得由 Executor自行继续。
