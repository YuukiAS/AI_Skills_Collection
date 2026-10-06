# 059 Research Authoring G4-C1 正常入口修复 — Kickoff Draft v0.1

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-06

只有独立 Critic 对下列同版执行包给出 execution-ready PASS，并逐字批准本 Kickoff 后，用户实际发送批准正文才形成执行授权：

- Plan：`docs/design/059_RESEARCH_AUTHORING_G4_C1_CONSUMER_REPAIR_IMPLEMENTATION_PLAN_V0_1_2026-10-06.md` @ `d60c039e294fbbf6afc9a7aff9edbba76d45e349`
- Goal：`docs/goals/059_RESEARCH_AUTHORING_G4_C1_CONSUMER_REPAIR_GOAL_V0_1.md` @ `bb4d03c20d48ea1d1ecdafdd0bee9d19d3d3c2c4`
- Repair authority：`results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_V2_CRITIC_REVIEW.md` @ `8aa5a2b9bdac737254e6e8527e57ff1750154b09`

## Kickoff 正文

继续执行同一个 059 task，只做已批准的 G4-C1 normal-entry consumer repair。

Repository：

`YuukiAS/AI_Skills_Collection`

Task：

`research-authoring--formal-production-authoring`

Branch：

`work/research-authoring--formal-production-authoring`

Worktree：

`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

失败候选：

`C=1c37c0715aca0096606f24e56192b7857e72bbd6`

目标：

形成新的 `C2`，然后停止给 Planner；不要启动 C2 final Gates。

开始前：

1. 在 exact worktree 核实 repo/origin/branch/dirty ownership，并 `git fetch origin main`；
2. 读取 current `AGENTS.md`、Capability Gate/version/maintenance policy、本 repair Plan/Goal、v2 Critic PASS；
3. 本轮正式 production refinement 使用 `workflow-core + ai-skills-core + research-writing`；
4. 确认从 C 到当前 HEAD 没有未经批准的 candidate-owned production change。

只允许的 production repair：

1. 修改 `scripts/codex_marketplace_config.json` 中：
   `research-writing -> report -> workflow_notes`。

   将 standalone / renderer-missing formal-PDF normal entry 明确为：
   - stable scientific source + complete downstream production handoff 后停止；
   - QA/preview/local compile也是 renderer mechanics；
   - XeLaTeX/`latexmk`/Pandoc-to-PDF、PDF creation/open/render、page raster/visual inspection、`pdftotext`/`pdfinfo`/`pdffonts` 等不能由 standalone Research Authoring执行；
   - generic runtime/file/compute 不能替代 `render-chinese-math-pdf`；
   - Markdown/LaTeX source、source-only QA、完整 downstream handoff仍允许；
   - compile/render 才能确认的 layout QA 留给 downstream renderer。

2. 修改 `tests/test_research_writing_routing.py`，增加对应 focused regression。

3. 通过 canonical generator重新生成；禁止手改 generated files。只保留 generator真正需要的 generated parity diff。

默认 ZERO WRITE：

- `skills/writing/research/research-authoring-core/SKILL.md`
- `skills/writing/research/research-reporting/SKILL.md`
- paper/litcite route
- profiles
- Clear Writing
- renderer
- Presentations
- Statistical Modeling
- Bridge Kit
- frozen G4 task/rubric/baseline
- live Plugin
- main/release

若 aggregate层无法表达修复，或 normal candidate runtime根本不消费 aggregate，立即停止回 Planner/Critic。

验证按 Goal/Plan执行，至少：

```bash
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_research_writing_routing
python -m unittest tests.test_codex_marketplace
python -m unittest discover -s tests
git diff --check
```

然后做已知 G4-C1 development replay：

- standalone `research-writing` candidate only；
- renderer companion absent；
- 使用普通 formal-PDF report request；
- 必须实际消费 Research Authoring/report aggregate；
- 允许 source + production handoff；
- 不得创建/渲染/检查 PDF；
- 不得执行 XeLaTeX/`latexmk`/Pandoc-to-PDF、page raster、`pdftotext`/`pdfinfo`/`pdffonts`；
- 不得通过在 replay prompt 中加入 test-specific command blacklist 来拿 PASS。

如果 replay仍越界，停止；不要继续形成 C2。

全部通过后形成 exact：

`C2=<new candidate commit>`

`research-writing` 仍是未发布的 `0.3` candidate；不要 bump 0.4，不改 root `VERSION`。

可以准备 C2 offline wrapper archive/manifest，但：

**本 Kickoff 不授权 Plugin Creator live update。**

也不授权：

- 新 G1-G4 final execution；
- G4 ChatGPT rerun；
- Codex final PDF；
- paid API；
- main merge/release；
- private/sensitive data external upload；
- force push/destructive Git；
- 扩大到 canonical core/report source或其他 plugin。

C2提交并 ordinary non-force push 后，立即停止并报告：

```text
BOUNDED_REPAIR_IMPLEMENTED=YES
C2_CANDIDATE_READY=YES
FINAL_CANDIDATE_COMMIT=<C2>
DEVELOPMENT_G4_C1_REGRESSION=PASS
FINAL_GATES_NOT_STARTED=YES
FINAL_TASKS_NEED_PLANNER_FREEZE=YES
NEXT_HANDOFF=PLANNER
```

不要自行选择新的 G1/G2/G3 final fresh tasks。Planner 将在 C2 后冻结新的 final packet，再送 pre-final Critic。
