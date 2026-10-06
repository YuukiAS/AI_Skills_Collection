# 059 Research Authoring G4-C1 正常入口修复 — Canonical Goal v0.1

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
日期：2026-10-06  
Repository：`YuukiAS/AI_Skills_Collection`  
Task key：`research-authoring--formal-production-authoring`

## Authority

Failure-attribution Critic PASS：

- `results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_V2_CRITIC_REVIEW.md`
- commit：`8aa5a2b9bdac737254e6e8527e57ff1750154b09`

Implementation Plan：

- `docs/design/059_RESEARCH_AUTHORING_G4_C1_CONSUMER_REPAIR_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md`
- Plan commit：`d60c039e294fbbf6afc9a7aff9edbba76d45e349`

本 Goal 只把批准的正常入口修复落实成新的 C2 candidate，不重新设计 Research Authoring。

## 1. Goal

在不修改 canonical Research Authoring owner source 的前提下，修复 standalone / renderer-missing Research Authoring report aggregate 的正常入口，使正式 PDF 请求：

```text
Research Authoring semantic/source work
-> stable Markdown/LaTeX source
-> complete downstream production handoff
-> STOP on standalone/no-renderer surface
```

而不是：

```text
generic ChatGPT runtime
-> local/preview/QA PDF compile/render
```

“只是 QA/preview”不能成为越过 renderer owner 的例外。

## 2. Exact execution identity

```text
branch = work/research-authoring--formal-production-authoring
worktree = /overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring
task_key = research-authoring--formal-production-authoring
failed_candidate_C = 1c37c0715aca0096606f24e56192b7857e72bbd6
target_candidate = C2_AFTER_REPAIR
tracking_issue = #99
```

复用同一 059 task，不开 successor task，不换 branch/worktree。

## 3. Required production repair

只修改 source：

`scripts/codex_marketplace_config.json`

且仅修改：

`research-writing -> report -> workflow_notes`

普通 production rule 必须明确：

- standalone / renderer companion缺失时，正式 PDF 任务只能完成科研 source + downstream handoff；
- local/preview/QA compile同样属于 renderer mechanics；
- XeLaTeX、`latexmk`、Pandoc-to-PDF、PDF creation/open/render、page raster/visual inspection、`pdftotext`/`pdfinfo`/`pdffonts` 等 PDF-derived QA 都不能由 standalone Research Authoring执行；
- generic runtime/file/compute 不能替代 `render-chinese-math-pdf`；
- Markdown/LaTeX authoring、source-only fidelity QA、完整 Codex/renderer handoff仍合法；
- 需要编译才能判断的 layout/render correctness 保持 pending，交 downstream owner。

不得写 G4 专用文件名、fixture、hash 或“为了通过 Gate”特判。

## 4. Required tests

修改：

`tests/test_research_writing_routing.py`

新增 focused regression，至少证明：

- no renderer companion -> formal PDF route fail closed；
- QA/preview compile/render 属于 renderer mechanics；
- generic runtime不是 renderer substitute；
- Markdown-only仍允许；
- source + production handoff仍允许；
- coordinator-first不退化；
- paper/litcite route不受本修复改写。

测试是合同回归，不是 final capability PASS。

## 5. Generated parity

必须通过 canonical generator重新生成。

禁止直接手改：

`plugins/codex/plugins/research-writing/skills/report/SKILL.md`

以及其他 generated layer。

只保留 generator真实产生的 diff；不制造无关 registry/catalog/provenance变化。

## 6. Explicit non-goals

默认不得修改：

- `skills/writing/research/research-authoring-core/SKILL.md`
- `skills/writing/research/research-reporting/SKILL.md`
- paper/litcite route
- research profiles
- Clear Writing
- renderer
- Presentations
- Statistical Modeling
- Bridge Kit
- frozen G4 task/rubric/baseline
- live Plugin
- `main` / `release`

若 aggregate层无法表达修复，停止返回 Planner/Critic。

## 7. Development validation

至少运行：

```bash
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_research_writing_routing
python -m unittest tests.test_codex_marketplace
python -m unittest discover -s tests
git diff --check
```

并执行 ai-skills-core当前要求的 source/generated parity检查。

README与 plugin changelog只检查，不默认修改：

```text
README checked: no update required
docs/plugin-changelogs/research-writing.md checked: no update required
```

若这两个结论不真实，停止返回 Planner，不扩大本 Goal。

## 8. Known G4-C1 development replay

在 C2 freeze前，用 standalone `research-writing` candidate、无 renderer companion 重放已知 formal-PDF report失败。

这是 development regression，不是 final G4。

必须看到：

- candidate Research Authoring实际消费；
- report aggregate/core/report route可定位；
- source authoring与完整 production handoff成功；
- 没有 PDF creation/render；
- 没有 XeLaTeX/`latexmk`/Pandoc-to-PDF；
- 没有 page raster/visual inspection；
- 没有 `pdftotext`/`pdfinfo`/`pdffonts`；
- render/layout QA留给 downstream；
- Markdown-only和代表性 should-not-change正常。

如果 aggregate实际被消费后仍自行 compile/render：
停止，不能形成 C2。

如果 aggregate未被消费：
记录 loading/consumer failure并停止，不能用更强测试 prompt掩盖。

## 9. C2 candidate

全部 bounded implementation + deterministic regression + development replay通过后，提交：

`C2=<exact new candidate commit>`

C2中的 Research Authoring canonical plugin version仍为：

`research-writing 0.3`

不是 0.4。

Repository `VERSION`不变，maturity不变。

C2之后只允许 task evidence/private packet变化，不得再修改 candidate-owned source。

## 10. First stop — return to Planner

形成 C2后立即停止，不启动任何新的 final Gate。

输出：

```text
C2_CANDIDATE_READY=YES
FINAL_CANDIDATE_COMMIT=<C2>
FINAL_GATES_NOT_STARTED=YES
FINAL_TASKS_NEED_PLANNER_FREEZE=YES
NEXT_HANDOFF=PLANNER
```

Planner随后负责冻结：

- C2新的 G1 natural case bank；
- C2新的 fresh G2 report-family task + Phase 2 delta；
- C2新的 G3 manuscript task；
- Reviewer access/rubrics；
- unchanged frozen G4 task/rubric/baseline；
- offline C2 wrapper identity。

之后再送独立 pre-final Critic。

Executor不得自行选择 final fresh task。

## 11. C2 final-evidence policy

旧 C 的 final evidence不能拼成 C2 release PASS。

- G1：C2直接重跑；
- G2：旧 DII只作 regression，C2需要新的 fresh report task/delta；
- G3：旧 MoSAIC只作 regression/should-not-change，C2需要直接 final evidence；
- G4：从 C2 rebuilt live wrapper完整重跑；第一次 G4 FAIL package永久只作 failure regression。

正式 G4仍使用冻结的普通 natural request，不加 evaluation-only command blacklist。

## 12. Live Plugin boundary

本 Goal只允许准备 C2 offline wrapper archive/manifest，不允许 live mutation。

当前 live release仍绑定失败的 C：

`pluginrel_6ac4471c7b90819189bc23af890135f3`

未来 C2 live update需用户单独 bounded authorization，并在 mutation时重新读取 current release id。

预计 wrapper distribution version下一 patch为 `0.3.1`；canonical Research Authoring payload仍是 `research-writing 0.3 @ C2`。

这个预计值不是本 Goal的 live update授权。

## 13. Maintenance tracking

继续使用 Issue `#99`。

如果当前执行面可以合法调用 Clear Writing并更新 GitHub tracking copy，则把 current anchor更新到本 repair Plan、next action更新到 C2 implementation/pre-final admission，Project继续 `DOING`。

否则记录 exact pending mutation，不要求用户手工维护，不假称同步完成。

## 14. Authorization ceiling

用户未来实际发送 Critic-approved Kickoff后，只授权：

- exact existing branch/worktree；
- approved config/test/generated repair；
- generator/tests；
- development replay；
- C2 candidate commit；
- ordinary non-force push；
- task-local results/private exports；
- offline wrapper preparation；
- stop at C2 candidate.

不授权：

- Plugin Creator live mutation；
- G1-G4 final rerun；
- Codex final PDF；
- paid API；
- main merge/release；
- private/sensitive external upload；
- canonical core/report source expansion；
- other plugin/domain changes；
- destructive Git / force push；
- background automation。

## 15. Positive terminal condition for this bounded Goal

本 Goal本身完成只意味着：

```text
BOUNDED_REPAIR_IMPLEMENTED=YES
C2_CANDIDATE_READY=YES
DEVELOPMENT_G4_C1_REGRESSION=PASS
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

不意味着：

`Research Authoring 0.3 complete`

不意味着：

`G4 PASS`

不意味着：

`released`
