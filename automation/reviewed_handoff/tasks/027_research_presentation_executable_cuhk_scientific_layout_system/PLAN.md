---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 027_research_presentation_executable_cuhk_scientific_layout_system
decision: PLAN_FROZEN
---

# 027 Executable CUHK Scientific Layout System — Plan

## Frozen decisions

027 只实现 Stage 3：把 Stage 2 已验证的 renderer-neutral gold composition recipes 变成 **canonical exact CUHK Beamer content area 内真实可执行、可编译、可复用的 scientific layouts**。

本任务不接普通 one-call production entry，不做 source-ingestion automation，不做最终 paper holdout，也不回到 PPTX/scaffold 路线。

Canonical exact CUHK identity 来自：

`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/`

现有 `main.tex`、`styles/beamerthemesintef.sty`、`styles/sintefcolor.sty` 与 canonical assets 是身份基线。不要为了实现 scientific layout 改写其主题/branding 语义。优先把 reusable scientific layout layer 放在独立 shared source 中，在生成的 build workspace 里加载 canonical source + scientific layout include；不得用 `design-tokens.json` 或 derived PPTX 仿制 exact CUHK。

## Frozen objective

建立一条可验证链路：

```text
realistic scientific page job
-> normal Stage 2 gold selector
-> renderer-neutral gold composition recipe
-> deterministic CUHK content-space resolution
-> native LaTeX/TikZ/figure/image-panel objects
-> exact CUHK .tex
-> compile PDF
-> render actual page pixels
-> item/page-level visual QA
```

关键不是“能生成一个 Beamer 文件”，而是证明 Stage 2 的 source-derived geometry / hierarchy / reading-flow / panel relations 真正决定 Stage 3 页面结构，而不是选择 gold 后又回到 task-specific 手写坐标。

## Required reading

Executor 至少读取：

- `automation/reviewed_handoff/schema.json`
- `automation/reviewed_handoff/README.md`
- `automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- 024 的 PLAN / RESULT / REVIEW / FINAL_REPORT 与 research routing changes
- 025、026 的 PLAN / RESULT / REVIEW / FINAL_REPORT
- 当前 `research_gold_composition_index.json`、gold schema、validator、selector、`build_gold_composition_recipe.py`、runtime traces
- 019–022 中与 composition representation、geometry transfer、semantic compatibility、anonymous comparative mature-bar 有关的 reusable engineering evidence；这些只能作为机制历史，不自动构成 027 PASS
- canonical CUHK Beamer source 下 `main.tex`、`styles/`、`assets/`、README 与 compatibility notes
- 当前 `research-presentations/SKILL.md`、`shared/template-routing.md`、`shared/source-fidelity.md`、`shared/visual-qa.md`
- source/plugin mirror 与 Presentation regression tests

## Implementation scope

### 1. Define an executable CUHK scientific-layout contract

在 Presentation shared layer 建立一个小型、可序列化、可校验的 Stage 3 layout contract / resolved-layout representation。它必须消费 Stage 2 recipe，而不是复制一份新的 reference database。

每个 resolved layout 至少记录：

- page job / dominant scientific object；
- selected gold id、recipe SHA 与 compatibility trace（仅内部 provenance）；
- exact CUHK content safe region；
- source recipe 中实际消费的 fields；
- resolved primary/supporting object geometry；
- visual hierarchy / alignment / reading-flow 的 CUHK 映射；
- content-capacity checks；
- native object types（equation / figure / plot / image panel / annotation / caption / connector 等）；
- emitted TeX fragment / macro identity；
- audience-safe output contract。

Audience-facing `.tex` / PDF 不得暴露 gold/RRL/QA/provenance/meta language。

### 2. Map gold geometry into the CUHK content area

建立一个明确的 CUHK content-space resolver。它必须尊重 canonical template 的 section navigation / frame title / footline/page number，所有 scientific objects 必须落在安全内容区，不得覆盖品牌区或页脚。

实际页面几何必须可追溯到 recipe 的至少这些字段：

- `primary_bbox`
- `primary_object_area_ratio`
- `visual_hierarchy`
- `alignment_groups`
- `reading_flow`
- `annotation_legend_caption_panel_relations`
- `content_capacity`

允许做 deterministic fit / clamp / normalization 以适配 CUHK 安全内容区，但必须在 trace 中说明变换；不能先手写最终坐标，再把 source bbox 作为解释性 metadata 附上。

至少增加一个 mutation regression：改变一个兼容 recipe 的 source-derived geometry/capacity field 后，resolved CUHK layout / emitted TeX geometry 必须发生可解释变化；不能只变 provenance ID。

### 3. Build native scientific layout primitives

至少覆盖以下六类最终 holdout 必需 scientific jobs：

1. equation / statistical model / theorem / proof-intuition；
2. quantitative result / uncertainty / comparison；
3. method / experiment design；
4. negative result / failure / model check；
5. medical-image aligned comparison / overlay / error / zoom；
6. discussion / next experiment。

要求：

- **数学页**：核心数学对象必须是 native LaTeX math；不得 rasterize 公式，不得把 `beta_1`、`sum_g` 等源码式字符串当 audience text。支持邻近 term annotation / brace / concise explanation，但标注必须绑定真实数学对象。
- **结果页**：主结果 figure/plot 必须成为视觉中心；支持 presentation-sized legend/tick/annotation/caption。不得默认用小图 + 大段解释卡片。若使用已有 raster/vector figure asset，只负责 layout；不得把默认 Matplotlib fixture 当成成熟视觉证明。
- **方法/实验页**：关系图应由真实 scientific objects 与 relations 驱动，可用 TikZ/native connectors；禁止 generic box-arrow 流程图替代研究机制。连接方向必须科学正确且易读。
- **negative/failure 页**：失败证据本身必须可见并与解释/诊断邻近，不得只写“failure case”文字。
- **医学影像页**：支持同病例 input / GT / prediction / overlay / error / crop/zoom；panel label、legend、callout 必须直接可读，影像区域必须是页面主体之一。fixture 必须有 same-case identity check。
- **discussion/next-experiment 页**：必须通过正常 selector 消费 Stage 2 discussion-compatible gold（当前应可选到 `GSC-018` 或未来同等兼容 record），把“已有证据/限制 -> 下一验证动作”组织成研究推理；禁止 generic future-work 三卡片。

### 4. Capacity and fallback behavior

Stage 3 不允许通过把文字、公式或图像缩到不可读来强行塞入选中的 layout。

如果 content capacity / panel count / dominant-object requirement 不匹配：

- 可以调用正常 selector 寻找另一 compatible gold；
- 可以明确返回 `NO_COMPATIBLE_LAYOUT` / `SPLIT_REQUIRED` 一类内部 failure signal；
- 不允许回退到 generic cards、空表格、默认 box-arrow 或“任意绝对坐标”万能模板。

本任务只需建立 failure contract；自动拆页 / bounded repair orchestration 属于 Stage 4。

### 5. Exact CUHK build workspace

实现一个可重复的 Stage 3 integration build path：

- 从 canonical `beamer/source/` 构建；
- 真实加载现有 CUHK theme/styles/assets；
- reusable scientific layout layer 通过显式 include/package/fragment 进入 build；
- 输出 `.tex + PDF`；
- 保存 build manifest，能证明 canonical source 被真实使用。

现有 canonical theme/style/asset 文件不得因本任务被重写。若需要额外 reusable macro/style 文件，应新增为独立 scientific-layout layer，而不是替换 CUHK identity。

### 6. Bounded Stage 3 integration deck

生成一套仅用于 Stage 3 验收的 integration deck，至少包含上述六种 page jobs 各一页主要内容页。

内容可以使用 repository 现有非 holdout regression/scientific fixtures 或为 027 准备的具体、可解释的非 holdout scientific fixture；必须有真实数学对象、具体方法/指标、实际 figure/image panel objects，不能用 `alpha/beta/x/y` 泛化占位符、空表格或 lorem ipsum。

该 integration deck 只是 Stage 3 工程/视觉证据，绝不能被写成 Stage 5 real-paper holdout 或 `ONE_SHOT_QUALITY_PASS`。

每页必须保存内部 trace：

`page job -> selector -> selected gold -> recipe -> resolved content geometry -> emitted TeX object ids`

至少六页中要体现多种不同 composition families / scientific-object structures，不能六页只是同一版式换内容。

### 7. Real render and visual evidence

对 integration deck：

- 真实 compile canonical CUHK `.tex` 到 PDF；
- 真实 render 每个主要内容页到 PNG；
- 做 mechanical checks：编译成功、无溢出/裁切、关键文字和图像存在、对象不越出 CUHK safe region；
- 使用当前 Bridge Kit / `gpt-5.6-terra` 对真实 rendered pixels 做 027 专用 item/page-level visual review。

Terra rubric 至少判断：

- exact CUHK identity 是否真实可见；
- 页面是否达到 mature doctoral research-group meeting / strong conference-talk bar；
- 主科学对象是否足够大且可投影阅读；
- 数学是否像正式排版而非源码；
- medical panels 是否同病例、标签/legend/callout 清楚；
- result figure / negative evidence 是否真正承担视觉中心；
- discussion / next-step 是否是具体科研推理而非模板化 future work；
- 是否存在 generic cards/box-arrow、AI 元语言、无意义留白、默认图表脸或每页同一种模板感；
- selected gold lesson / geometry 是否在当前页面真实体现。

如果现有 gold reference pixels 可按 rights/provenance 规则安全 materialize，可在 visual packet 中加入与该 page job 兼容的真实 gold reference renders 做匿名相对校准；reference pixels 只作审查 evidence，不进入 production asset。

**不能用 Terra top-level overall PASS 代替页面质量。Planner 必须读取每个主要内容页的 item-level decision / observation。主要内容页必须全部达到当前 frozen mature bar 才可 PASS 027。**

### 8. Tests and source/plugin mirror

增加/更新 deterministic tests 至少验证：

- normal selector / recipe 被真实调用；
- gold source-derived geometry 改变会影响 resolved layout / TeX geometry；
- six page-job coverage；
- CUHK safe-region constraints；
- native LaTeX math，不把公式 rasterize；
- medical same-case identity 与 panel/legend relation；
- capacity mismatch 不回退 generic layout；
- internal gold/RRL/QA/provenance language 不泄漏到 audience-facing TeX/PDF text；
- canonical CUHK identity files未被修改；
- source/plugin mirror 同步；
- no holdout-specific hardcode。

## Validation

Executor 至少运行：

- Stage 3 layout contract / resolver / renderer targeted tests；
- Presentation targeted tests；
- `python -m unittest discover -s tests`；
- `python scripts/skills.py validate`；
- marketplace `--write --validate --check --path-report`（按当前 workflow 权限/contract）；
- Reviewed Handoff validation；
- `git diff --check`；
- canonical CUHK source identity check；
- Stage 3 integration `.tex` compilation；
- PDF -> real page PNG render；
- mechanical QA；
- 027 gpt-5.6-terra item/page-level review，并保存 visual inputs、identity binding 与真实 evidence。

若 CI/test environment 缺少本任务真实需要的 LaTeX/render dependencies，应一次性核对 Stage 3 build dependency contract，避免一个 ImportError 补一个包；但不得因此修改业务质量门槛。

## Out of scope

027 不得：

- 修改 Stage 2 gold mature bar、重审 025/026 gold 或扩 source corpus；
- 复制 donor slide pixels/branding 进入 runtime layout assets；
- 修改 023 历史或把 PPTX renderer重新设为主 production route；
- 用 derived CUHK PPTX/design tokens 冒充 canonical exact CUHK；
- 接入普通 one-call production entry / source ingestion / storyline orchestration / automatic repair loop；
- 做完整 deck-level rhythm optimization；
- 使用或调优最终 Stage 5 statistics / medical-imaging holdout papers；
- 修改 Terra core / Bridge Kit reviewer semantics；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 027：

1. canonical exact CUHK `beamer/source/` 被真实用于生成，现有 theme/style/identity files 未被替换或仿制；
2. Stage 2 normal selector -> gold recipe -> CUHK resolver -> emitted TeX 的真实链路成立；
3. source-derived geometry/hierarchy/reading-flow/capacity fields 实际改变 resolved layout，而不是只做 provenance；
4. 至少六类主要 scientific jobs 有 reusable native layout support，并在 integration deck 中各有真实可编译页面；
5. 数学核心对象为 native LaTeX；结果/negative evidence 视觉中心成立；医学影像 panel 同病例且 legend/annotation 可读；discussion/next-step 是具体科研推理；
6. capacity mismatch 有明确 no-compatible/split failure contract，不回落到 generic cards/box-arrow/default plot/万能绝对坐标；
7. audience-facing output 无 RRL/gold/QA/provenance/AI 制作元语言；
8. integration deck 真实 compile/render，mechanical QA 通过；
9. 027 Terra 对每个主要内容页的 item-level/page-level judgement 都达到 frozen mature research-group-meeting / strong conference-talk bar；top-level package PASS 不得冒充质量 PASS；
10. required tests / validation / real CI 全部通过；
11. 没有开始 Stage 4 one-call orchestration 或 Stage 5 holdout；
12. RESULT / FINAL_REPORT 明确列出 implemented layout families、gold-to-layout runtime traces、render/visual evidence、失败/拒绝路径与 remaining limitations。

027 PASS 只关闭 Stage 3。Planner PASS 后才创建 Stage 4 — One-Call Production Entry + Bounded Quality Loop 的独立 bounded task；Executor 不得自行继续。
