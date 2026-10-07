# 059 Research Authoring C3 开发闭合 — Critic Review v0.1

日期：2026-10-07  
角色：独立 Critic  
任务：`research-authoring--formal-production-authoring`

## 结论

```text
RESULT=REVISE
C3_PROVISIONAL_PRODUCT_COMMIT=04a17a904ce522cb4a517cb33f22e062f2bcbc09
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED
C3_CANDIDATE_READY=NO
C3_DEVELOPMENT_MATRIX=FAIL
FINAL_GATES_NOT_STARTED=YES
BLOCKERS=RA-C3DEV1
NEXT_HANDOFF=PLANNER
```

本轮 product diff总体落在批准范围内；standalone Research Authoring、authoring-only `codex-research-writing`、render-only、离线 wrapper等证据没有暴露新的架构问题。

但是完整 development matrix 不能判 PASS。至少两个 integrated `research-main` 正常入口没有满足冻结的 owner / renderer 顺序，其中 manuscript 路线实际绕过了 `render-chinese-math-pdf`，改由 generic `pdf` + 直接 `pdflatex` 完成最终 PDF。

因此 `04a17a...` 只能保留为本轮 provisional product attempt / regression identity，不能按冻结合同晋升为 C3 final candidate。

## 已核对身份

```text
main=d437b90f880f47c92331a3f12a0d096e44e2f4bd
branch/evidence head=49e8d194027d8e26d5f5e3df88db9d0abb5c2633
provisional product=04a17a904ce522cb4a517cb33f22e062f2bcbc09
```

`04a17a... -> 49e8d...` 只增加 development evidence 和 exact-product offline wrapper；没有 candidate-owned production drift。

offline wrapper manifest绑定 `04a17a...`，不打包 renderer runtime，当前只能作为 provisional packaging evidence；不得用于 live G4。

## RA-C3DEV1 — integrated research-main owner chain仍未闭合

### requirement

冻结 Plan / Goal / Kickoff 对 integrated production 的要求是：

```text
report + formal PDF:
Research Authoring core/report
BEFORE
render-chinese-math-pdf
BEFORE
PDF mechanics

manuscript + PDF:
Research Authoring core/paper
-> LaTeX/source delegate as needed
-> explicit handoff
-> render-chinese-math-pdf
-> PDF + renderer QA
-> Research Authoring scientific QA
```

这不是静态字符串要求，而是本 C3 修复的正常入口能力：artifact Skill可见不等于它可以抢先成为 owner；完整正式生产必须由 Research Authoring稳定语义后再进入被批准的 renderer。

### direct evidence

#### DEV-04 research-main report + formal PDF

权威 run2 trace：

`results/research-authoring--formal-production-authoring/c3_development_matrix/dev04_research_main_report_pdf_run2/trace/child.stdout.jsonl`

实际顺序：

1. 第一条 agent message同时宣布使用 `research-reporting` 与 PDF renderer；
2. 第一个 Skill read 是：
   `.agents/skills/tools-documents-media-render-chinese-math-pdf/SKILL.md`
3. 第二个 Skill read才是：
   `.agents/skills/writing-research-research-reporting/SKILL.md`
4. `research-authoring-core` 更晚才读取。

即：

```text
renderer read
-> report read
-> Research Authoring core read
-> PDF mechanics
```

而不是冻结的：

```text
Research Authoring
-> report
-> handoff
-> renderer
-> PDF mechanics
```

此外实际 renderer evidence记录的是直接：

`pandoc ... --pdf-engine=xelatex`

而不是正常安装的 `render-chinese-math-pdf` canonical orchestration entry。

#### DEV-05 research-main manuscript + PDF

首个 trace：

`results/research-authoring--formal-production-authoring/c3_development_matrix/dev05_research_main_manuscript_pdf/trace/child.stdout.jsonl`

实际最早读取顺序：

```text
latex-paper-authoring
-> writing-fidelity
-> research-authoring-core
-> scientific-writing
-> scientific-prose
-> paper-workflow-orchestrator
-> generic pdf
```

continuation trace：

`.../trace/child_continue.stdout.jsonl`

再次读取：

```text
research-authoring-core
-> latex-paper-authoring
-> paper-workflow-orchestrator
-> generic pdf
```

没有实际读取 `render-chinese-math-pdf`。

随后直接执行：

`pdflatex -interaction=nonstopmode -halt-on-error paper.tex`

最终 `renderer_evidence.md` 也明确记录：

```text
Renderer: pdfTeX
Route: pdflatex
```

所以该 case实际是：

```text
Research Authoring / LaTeX / generic pdf
-> direct pdflatex
-> final PDF
```

而不是 approved：

```text
Research Authoring
-> source/package + handoff
-> render-chinese-math-pdf
-> final PDF + renderer QA
```

这也给出了上一轮尚不存在的 direct evidence：generic `pdf` 的宽 discovery surface在新的 research-document PDF production中确实被实际读取。

### causal risk

这不是“证据命名不漂亮”。

C3 的目标就是防止 artifact能力因为可见而绕过 Research Authoring owner admission。

当前 integrated manuscript正常入口仍然可以：

- 提前选择 `latex-paper-authoring`；
- 读取 broad generic `pdf`；
- 完全不消费批准的 `render-chinese-math-pdf`；
- 直接用 `pdflatex` 生产 final PDF。

因此用户真正使用 `research-main` 时仍无法依赖冻结的：

`Research Authoring -> explicit handoff -> canonical renderer -> post-render scientific QA`

owner chain。

如果现在进入 final G1-G4，final Gate仍在替 development matrix发现基础路由问题，与本轮收口目标冲突。

### minimum closure

遵守当前 Kickoff的 STOP 规则：

1. 不启动 final G1-G4；
2. 不把 `04a17a...` 称为 C3 final candidate；
3. 不修改 development prompt，不删除失败 trace，不挑 run宣称 PASS；
4. 不由 Executor自行扩 scope。

返回 Planner，只处理这一个 integrated-production owner-chain failure。

Planner必须基于这次新 direct evidence决定最小修复层：

- `render-chinese-math-pdf` metadata/profile admission是否仍不足；
- `latex-paper-authoring` metadata是否还会过早抢 owner；
- generic `pdf` 的极宽 discovery description现在已有直接因果证据，是否需要纳入最小范围；
- `research-main` routing notes是否能在现有平台上真实保证 authoring first / renderer after handoff。

如果修 product，形成新的 provisional product commit P2；完整 11-case development matrix重新绑定 P2。

不得继续仅加同义 wording patch并把 `04a17a...` 追认。

Owner：Planner。

## 其他审查结果

### standalone / authoring-only

DEV-01、DEV-03 和 DEV-11 的原始 trace均显示 Research Authoring实际消费并停止在 source/package + downstream handoff，没有最终 PDF mechanics。

尤其 DEV-11：

- exact `codex-research-writing` profile安装 identity绑定 `04a17a...`；
- generic `pdf` 保持安装；
- Research Authoring core/paper/LaTeX delegate实际读取；
- 只产生 source package + handoff；
- 没有 final PDF。

因此上一轮 `RA-C3ER1` 仍保持 CLOSED。

### render-only

DEV-06 最终 continuation与 DEV-07证明 finalized Markdown/LaTeX仍能直接进入 renderer而不要求完整 Research Authoring规划。

DEV-06保留了前一次失败的字体/缓存尝试，最终使用安装的 renderer skill和 canonical helper完成；这些失败没有被删除，符合保留 development failure evidence原则。

### same-product / wrapper

`04a17a... -> 49e8d...` 没有 candidate-owned production source变化。

offline wrapper：

- payload commit=`04a17a...`；
- Research Authoring / Clear Writing来源 commit一致；
- skills-only / PRIVATE / USER；
- no renderer runtime；
- archive SHA256已记录。

包装本身没有发现阻塞，但由于 product P未通过完整 matrix，它目前只是 provisional wrapper，不得进入 live mutation。

### README / Clear Writing evidence

本轮 product commit修改了 README standalone renderer版本卡。

仓库规则要求 README修改必须实际调用 Clear Writing。当前提交的 development evidence中没有找到可独立定位的本任务 Clear Writing调用记录。

由于 `RA-C3DEV1` 已要求形成 P2，这一点本轮不单独新增 blocker；Planner/Executor在形成 P2前必须把 README Clear Writing调用及其 durable locator一起补齐，不能只声称遵守。

## 当前边界

```text
C2_G1_FAIL=PERMANENT
RA-C3ER1=CLOSED
RA-C3DEV1=OPEN

04a17a904ce522cb4a517cb33f22e062f2bcbc09=PROVISIONAL_DEVELOPMENT_ATTEMPT
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED

FINAL_GATES_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```
