---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 018_presentation_external_method_audit
decision: PLAN_FROZEN
---

# 018 Research Presentation External Method Audit — Plan

## Objective and value

先回答一个比“继续加规则”更重要的问题：**当前公开 Presentation skill / workflow 中，哪些机制已经被真实实践证明能减少 AI 模板脸、提高构图质量和一次生成成功率；本仓库当前缺的到底是规则、设计搜索、布局约束、参考迁移，还是审查方法。**

本任务只做方法审计，不直接实现下一代 Presentation 架构。它要为后续 `reference -> composition -> candidate -> comparative review` 链路提供可执行依据，避免再次凭空写一批“看起来正确”的设计原则。

上一轮 10 页 synthetic review pack 明确保留为 medium / negative baseline，不得在本任务中提升为 gold exemplar。

## Required reading inside this repository

Executor 必须先读取：

- `AGENTS.md`
- `automation/reviewed_handoff/README.md`
- `automation/reviewed_handoff/schema.json`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `docs/workflows/REVIEWED_HANDOFF_SKILL_INTAKE.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/research-presentations/TODO.md`
- `skills/tools/documents-media/presentations/shared/visual-qa.md`
- `skills/tools/documents-media/presentations/shared/references/RESEARCH_SLIDE_ARCHETYPES.md`
- 当前 reference index / source manifest 与上一轮 016 / 017 的 final report、reference-design audit 和 visual-review evidence。

由于本任务处理外部 skill repo，必须遵守 `REVIEWED_HANDOFF_SKILL_INTAKE.md` 的外部来源与许可证边界。但本任务**不是 skill intake/adoption task**：只允许形成 comparative audit 和 future-adoption recommendation，不得自行 merge / partially merge / create skill / create plugin。

## External audit set

至少实际检查以下公开来源；若某一源在执行时不可访问，必须记录失败原因，不得用 README 摘要或二手文章假装完成源码审计。

### Presentation skills / workflows

1. `zarazhangrui/frontend-slides`
   - 至少检查 `SKILL.md`、style preset / template selection、preview / design recipe、render/QA 相关文件。
   - 重点：真实内容 3-way style preview、show-don't-tell、选定后 design-system lock、anti-AI-slop、fixed-stage / screenshot QA。

2. `andyqiu847-ai/high-quality-slides`
   - 至少检查 `SKILL.md`、layout/design-system 文件、README 中指向的实现约束。
   - 重点：research first -> narrative -> design system -> build、semantic layout inventory、slide-art-director workflow。

3. `brycewang-stanford/many-ppt-skills`
   - 至少检查 registry / comparison method 和 `principles/` 中 8 条原则的原文依据。
   - 重点：show-don't-tell、anti-slop banned list、constraint beats freedom、render-and-look、distill-don't-design。

4. `RFYoung/slideweaver`
   - 至少检查 `SKILL.md`、layout solver / deck profile / shape cookbook / PPTX QA 相关源码。
   - 重点：academic PPTX 的 native editable object、布局求解、deck-level consistency、PowerPoint 打开/图表验证。

5. `wmyung/manuscript-to-editable-slides`
   - 至少检查核心 skill、renderer/layout definitions、QA / montage / acceptance tests。
   - 重点：content-driven layout families、layout rhythm、source coverage、visible internal-language exclusion、real render montage。

6. `sunzhejian/academic-paper-image-ppt`
   - 至少检查 skill contract、preview workflow、editable PPTX assembly / QA 路径。
   - 重点：多套真实内容视觉 preview 先作为 design spec，再翻译为 native editable PowerPoint，而不是直接把 preview image 当最终页。

7. `hugohe3/ppt-master`
   - 若公开仓库可正常读取，检查其核心 skill / reference-deck / layout / native PPTX 相关机制。
   - 若原仓库不可访问或只有 fork，必须明确区分官方源与 fork，不得把 fork 当成官方实现事实。

### Scientific presentation guidance

8. Assertion-Evidence Approach
9. MIT Communication Lab 的 technical / scientific presentation guidance
10. PLOS 关于有效科研演示设计的公开指导

这些指导只用于总结科研表达与视觉组织原则。除非页面有明确可复用许可证，不复制长段原文、图例或模板资产。

## Audit questions

对每个外部项目 / 指导源至少回答：

1. 它实际解决什么问题？
2. 质量提升来自哪一个**具体机制**，而不是宣传语？
3. 该机制属于：内容/叙事、风格探索、布局选择、设计系统约束、reference transfer、native PPTX/Beamer rendering、visual QA、用户交互，还是其他层？
4. 它如何避免 AI 模板脸或低质量默认 attractor？
5. 它是否真正做 multi-candidate / visual search；如果做，候选差异是构图还是只换皮肤？
6. 它是否在生成后看真实 pixels / montage / contact sheet？
7. 它是否支持 editable PPTX；若支持，原生对象/布局能力边界是什么？
8. 对科研汇报有哪些特别有价值的机制？有哪些偏商业/网页 presentation、不宜直接搬入科研场景？
9. 当前许可证是什么；可借的是思想、数据结构、少量 MIT-compatible implementation，还是只能 reference-only？
10. 与本仓库当前 `research-presentations` / `visual-qa` / reference library 相比，缺口在哪里？

## Required deliverables

### 1. Main audit report

新增：

`docs/audits/RESEARCH_PRESENTATION_EXTERNAL_METHOD_AUDIT.md`

报告必须包含：

- executive conclusion：当前最大架构缺口是什么；
- 每个项目的实际机制审计，不得只列功能清单；
- license / reuse boundary；
- 与当前仓库的 capability gap matrix；
- 哪些机制值得下一阶段采用，按“必要 / 值得试验 / 暂不采用”分类；
- 明确指出哪些现有规则已经有了、问题其实在执行链没有落地；
- 明确指出上一轮 10 页 synthetic pack 为什么不能作为 gold visual baseline；
- 推荐下一 bounded task 的最小目标，但**不得直接实现它**。

### 2. Structured adoption matrix

新增：

`docs/audits/research_presentation_external_method_matrix.json`

至少包含每个 source 的：

- `source_name`
- `source_url`
- `source_type`
- `upstream_commit_or_version`（能确认时）
- `license`
- `files_actually_inspected`
- `mechanisms`
- `research_relevance`
- `current_repo_equivalent`
- `gap`
- `reuse_boundary`
- `recommended_disposition`

`recommended_disposition` 在本任务只允许使用：

- `concept_only`
- `candidate_for_future_adoption`
- `reference_only`
- `not_recommended`

这些不是正式 intake taxonomy 决策，不得据此修改 active skill。

### 3. Next-step architecture recommendation

在主报告中给出下一 task 的**单一最小推荐方向**。默认优先判断是否应先实现：

- exemplar composition representation；
- internal multi-candidate design search；
- comparative Terra review；
- 或其他被审计证据更强支持的第一步。

只能推荐一个作为 019 的首要目标，并解释为什么它是当前瓶颈；其余放后续 roadmap。

## Evidence requirements

- 每个外部 skill repo 至少检查 README 以外的一个实际实现/skill/design/QA 文件；核心项目应检查多个文件。
- 报告中区分“上游明确实现”“根据源码推断”“公开指导原则”三类证据。
- 记录访问日期和上游 commit / tag（可确认时）。
- 不把 star 数、宣传语或二手排行当作质量证据。
- 不下载或提交大批 binary demo deck / screenshots；必要的临时 clone 放 `.tmp/skill-intake/`，不得提交。

## Out of scope

本任务禁止：

- 修改 `research-presentations/SKILL.md`、`visual-qa.md`、archetype rules；
- 修改 generator / PPTX renderer / Beamer renderer；
- 修改 Terra / Bridge Kit；
- 扩充现有 research presentation reference corpus；
- vendor / copy 外部仓库；
- 新增 plugin / skill / profile exposure；
- 做 synthetic 或 real holdout benchmark；
- 把任何 external source 直接判为 merged / partially merged / adopted；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

## Acceptance gates

Planner/Reviewer 只有在以下全部满足时才可 PASS：

1. 所有 required external sources 都被真实检查，或对不可访问源有明确失败记录；
2. 不是 README-only audit；
3. 每个 source 有 license / reuse boundary；
4. 主报告明确比较当前仓库已有能力与外部机制，能区分“我们已经写了规则”与“真正缺失的生成/审查机制”；
5. 审计明确回答 reference corpus 为什么没有真正进入 composition decision；
6. 对 multi-candidate design search、design-system lock、native PPTX、render-and-look、contact-sheet/deck rhythm、comparative review 分别给出是否采用及理由；
7. structured matrix 与主报告一致；
8. 没有未经授权的 upstream code / asset 被复制进 active repository；
9. 只推荐一个最小 019 方向，没有提前实现；
10. repository validation / CI 通过。

## Validation

至少运行：

```bash
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
git diff --check
```

如果本机缺少某个非本任务引入的依赖，记录真实 blocker，不得为了让审计 task 通过而扩展 CI 依赖或修改无关 workflow。

## Handoff

本任务 `ci_required=true`。Executor 完成 audit artifact 后写 `RESULT.md`，提交实现，然后把 task 置为等待真实 CI。Scheduled Planner 在 CI 成功后独立审查报告和实际外部证据；不得因为文档存在就自动 PASS。
