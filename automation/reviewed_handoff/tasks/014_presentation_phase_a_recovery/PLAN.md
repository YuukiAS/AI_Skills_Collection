---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 014_presentation_phase_a_recovery
decision: PLAN_FROZEN
---

# 014 Presentation Phase A Recovery — Plan

## 目标

在不改写 013 历史结论、也不绕过 review-limit 的前提下，执行用户已经明确授权的人工恢复路径：验证 Presentation regression 的完整 CI/test dependency contract，恢复真实 GitHub CI，然后对 013 原冻结计划下的 TODO consolidation 做一次新的、独立的 recovery review。这里的人工授权是合法的新入口；014 不是 013 的自动第三轮返修。

## 已冻结事实

1. `013_presentation_todo_consolidation` 已在第 2/2 轮因为 CI 测试环境依赖未完整声明而进入 `AWAIT_HUMAN_DECISION`。其历史 `REVIEW_1.md`、`REVIEW_2.md`、`FINAL_REPORT.md` 和 CURRENT 终态必须保持原样，不能迁移成 PASS。
2. 用户已明确授权一次人工依赖修复，授权范围只有 Presentation regression 的 CI/test dependency contract；不得借此改 TODO 分类语义、当前 Terra 四页、source corpus、benchmark 或插件架构。
3. 人工授权后的 main 已包含提交 `fdc2ddf30e6782362af7e3ff1c9322e48dfbef8e`：`Codex Marketplace` 的 Presentation regression 测试环境同时安装 `Pillow>=10` 和 `python-pptx>=1.0`，并在全库测试前显式验证 `PIL` 与 `pptx` 可导入。
4. 现有 regression generator 的第三方顶层导入链至少包括 `PIL` 和 `pptx`；本任务不得继续采用“看到一个 ImportError 补一个包”的策略。Executor 必须先检查 generator 及其直接调用链的第三方导入，再确认当前声明是完整集合。
5. 013 原始内容实现仍以其冻结 PLAN、`base_commit=eec33062f39c2799c46f907ff0869bd627272173`、原 TODO/skill/QA/archetype/tests diff 和 generated/plugin mirror 为审核对象；014 的依赖修复不能替代对这些内容的独立审核。

## Executor 范围

Executor 首先同步最新 main，并做以下工作：

1. 检查 `tests/fixtures/presentations/research_group_meeting/generate_research_group_meeting_regression.py` 及其直接调用链的第三方 Python imports，确认当前 workflow 的 Presentation regression test dependencies 完整；至少核对 `Pillow` 与 `python-pptx`，并考虑 `python-pptx` 自身安装依赖由 pip 正常解析。
2. 检查 `.github/workflows/codex-marketplace.yml` 当前人工授权修复。若 `fdc2ddf...` 已完整满足依赖 contract，不得为了制造新 implementation diff 重写它；若仍存在同一依赖 contract 内、可由现有代码直接证明的遗漏，只允许做一次最小、完整的 dependency declaration 修正，不得触碰 Presentation 内容逻辑。
3. 在本地现有环境运行至少：
   - `python -m unittest tests.test_presentations`
   - `python -m unittest discover -s tests`
   - `python scripts/skills.py validate`
   - `python scripts/build_codex_marketplace.py --validate --check --path-report`
   - `python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection`
   - `git diff --check`
4. 独立准备 013 内容 closure 所需的可审核材料：核对 TODO 全量四分类、三类 `PROMOTE_NOW` 的 active-layer 落点、对应 regression tests、source/generated mirror 一致性，以及 013 PLAN 明确禁止的 source expansion / benchmark / Terra repair 是否确实没有发生。
5. 写 `results/014_presentation_phase_a_recovery/RESULT.md`，明确区分：
   - 人工授权依赖修复是否完整；
   - 本地验证结果；
   - 013 内容审核所需事实；
   - 是否存在超出授权范围的新 blocker。
6. `ci_required=true`。若本地验证通过，Executor 将 014 交到 `WAITING_FOR_CI`，`ci_status=PENDING`。`implementation_commit` 可指向真正承载当前授权依赖修复的实现提交；如果无需新增业务实现，不得为了“有新 SHA”改无关文件。

## CI bridge 要求

当前 Scheduled GPT 对 push-triggered GitHub Actions 的发现能力有限，因此本任务继续使用纯机械 CI bridge，语义判断仍归 Planner/Reviewer：

- 当 014 进入 `WAITING_FOR_CI` 后，本地 Codex/CI bridge 使用 `gh run` 查询当前 main/handoff 对应的真实 required workflows。
- 将聚合状态发布为当前 main tip 上 context=`reviewed-handoff/ci-summary` 的 commit status；`pending/success/failure` 必须来自真实 Actions，而不是 Executor 自评。
- failure 的 `target_url` 指向最关键失败 run；success 指向主要 required CI run。
- CI bridge 不写 REVIEW、不改 Planner decision、不自行把 CURRENT 设为 PASS/REVISE。

## 独立审核门槛

只有以下全部成立，014 才可 PASS，并把 Phase A 视为通过人工授权恢复：

1. 干净 GitHub runner 上 `Codex Marketplace` 的 Presentation regression 测试依赖可完整导入，不再出现 Pillow / `python-pptx` 或同一现有导入链的缺包错误。
2. Plan-required CI 真正完成且 required workflows PASS；后续 marketplace generation/validation、skills validation/audit 实际执行，而不是因前序测试失败被跳过。
3. 013 TODO 中每个 checklist item / 独立规则均有且只有四分类之一：`ALREADY_IMPLEMENTED`、`PROMOTE_NOW`、`KEEP_BACKLOG`、`DUPLICATE_OR_SUPERSEDED`，并有可审计依据。
4. 013 冻结的三类 `PROMOTE_NOW` 已进入正确 active layer，并有 regression tests；不是只改 checkbox。
5. 有价值的历史规则仍保留；`KEEP_BACKLOG` 没被伪装成已实现；`DUPLICATE_OR_SUPERSEDED` 有明确覆盖依据。
6. source skill、shared visual QA/archetypes、tests 与 generated/plugin mirror 一致。
7. 013/014 均未扩 source corpus、未做 Source Scout、未创建统计/医学 benchmark、未修改当前 Terra 四页实现或 visual evidence。
8. 013 的历史 review-limit 事实保持可追溯；014 的 PASS 只能表示“用户授权后的 Phase A recovery 完成”，不能重写 013 为从未失败过。

## Review 行为

014 是用户人工授权后的新 bounded recovery task，拥有正常最多两轮独立 review；这不是对 013 自动增加第三轮。若 014 第一轮发现与本授权范围直接相关的最小实现/CI blocker，可 `REVISE` 一次；第二轮仍不能关闭则重新进入 human gate。若发现需要改变 TODO 产品语义、Presentation 科学内容或扩大依赖修复范围，直接停止并报告，不自行扩 scope。

## Out of scope

- 不改写 013 REVIEW/FINAL_REPORT/CURRENT 历史终态；
- 不重做 TODO consolidation；
- 不修 Terra slide 1–3；
- 不生成新的 Terra visual identity；
- 不做 statistical/biostatistical 或 medical-imaging benchmark；
- 不扩 Source Registry / Inspected Page Library / Synthesized Knowledge；
- 不重构 Presentation plugin / marketplace 架构；
- 不把 CI bridge 机制的长期产品化塞进本 recovery task。
