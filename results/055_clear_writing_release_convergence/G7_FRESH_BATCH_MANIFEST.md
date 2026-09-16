# G7 Fresh Batch Manifest

Task: `055_clear_writing_release_convergence`

Status: `G7_FRESH_BATCH_FROZEN_BEFORE_OUTPUT`

Freeze time: `2026-09-16`

## Final Candidate Pin

```text
FINAL_CANDIDATE_COMMIT = 79d620a0c60cdd086dd5828c8686bac843291cda
G7 batch size = exactly 3
candidate outputs generated before this manifest = no
```

This manifest freezes the exactly-three public-safe fresh sources before any
candidate output is generated. None of these sources are 050-054 exposed
samples, task result files, CI/final-report/workflow metadata, plugin source,
or private artifacts.

## Source Completeness Preflight

```text
source_1 complete = yes; starts at intended exported note boundary; ends after explicit footer noise; no half sentence/list/formula/table
source_2 complete = yes; includes formula definition, table header/body, interpretation, and limitation; no missing referenced equation/table
source_3 complete = yes; includes data context, results, error analysis, limitations, future work, and final bounded conclusion; no half section
public_safe = yes
private_data = no
050_054_exposed_sample = no
workflow_or_task_metadata_source = no
plugin_source = no
```

## Item F1 — Noisy Code / Reproduction Tokens

```text
item_id = G7_F1_NOISY_CODE_REPRO
source = results/055_clear_writing_release_convergence/g7_fresh_batch/sources/noisy_code_reproduction_source.md
sha256 = 9c9f3d32e04ab47466fc2d7dd90b740fe694907727911a7416443e03ebcc65ef
provenance = executor-authored public-safe technical source, frozen before candidate output
natural_user_task = 请把这份带有导出噪声的中文技术说明改写成可以给合作者看的成稿，保留真正复现实验所需的命令、路径、参数和限制条件，清理导航、缓存、页脚等包装噪声；不要改变完成状态。
PRIMARY_RISK = noisy technical source with legitimate code/path/reproduction tokens
APPLICABLE_GATES = G2,G3,G4,G5
RENDER_REQUIRED = NO
```

Pass criteria:

```text
G2: preserve scientific claims, counts, threshold comparison, caveats, and future-work status.
G3: preserve legitimate command/path/config tokens and explain their role; do not delete them as wrapper noise.
G4: remove wiki/export/footer/cache/navigation wrapper from reader-facing prose.
G5: produce natural reader-facing Chinese, not an execution memo or cleanup checklist.
```

## Item F2 — Formula / Table Structured Content

```text
item_id = G7_F2_FORMULA_TABLE
source = results/055_clear_writing_release_convergence/g7_fresh_batch/sources/formula_table_structured_source.md
sha256 = 85cec2d4ca030db4c7c5c50b1213059cf2e903df85ae03f32e4bb46df99f7ca5
provenance = executor-authored public-safe technical source, frozen before candidate output
natural_user_task = 请把这段公式和表格为主的中文技术笔记整理成读者能直接理解的说明，保留公式、变量含义、表格数值、均值/标准差、比较关系和限制条件。
PRIMARY_RISK = formula/table structured technical content
APPLICABLE_GATES = G2,G3,G5,G6
RENDER_REQUIRED = YES
```

Pass criteria:

```text
G2: preserve threshold interpretation, formula meaning, variable definitions, and conclusion strength.
G3: formula, table headers, numeric values, units/standard deviations, and row meanings remain correct.
G5: explain why epsilon=0.003 is selected without implying it is the lowest validation RMSE.
G6: rendered formula/table must be visible, readable, and not clipped or corrupted.
```

## Item F3 — Long-form Future Work / Limitation / Attribution

```text
item_id = G7_F3_LONG_FUTURE_LIMITATIONS
source = results/055_clear_writing_release_convergence/g7_fresh_batch/sources/long_future_limitations_source.md
sha256 = 690cc84c8c70c895ba8d604a1050be932fb280b3795aba440a9db066bedcf2d3
provenance = executor-authored public-safe technical source, frozen before candidate output
natural_user_task = 请把这份中文项目说明改写成一篇连贯的阶段性技术总结，保留数据来源、结果数值、错误分析、限制、后续工作和未完成状态；不要把建议写成已经完成的行动。
PRIMARY_RISK = long-form future-work/limitation/attribution/reader-relevance decision
APPLICABLE_GATES = G2,G5,G6
RENDER_REQUIRED = YES
```

Pass criteria:

```text
G2: preserve data split, metrics, error categories, limitation scope, and future-work modality.
G5: output reads as a coherent technical summary, not a project task list or internal execution plan.
G6: full rendered artifact must preserve section flow and readability without clipping or broken glyphs.
```

## No Adaptive Replacement

If any item exposes a true product failure, this C6 G7 certification fails for
the frozen batch. Do not replace the item, add a fourth source, mutate C6, or
run Terra before the frozen recovery contract is followed.
