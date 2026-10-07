# G2 Phase 1 Raw Scope — DII greenfield advisor update

Gate: G2 科研文档语义组织与长期增量维护
Phase: 1 / greenfield authoring
Frozen by Planner: 2026-10-05

## Exact real task

Project: `YuukiAS/Distributed_Imaging_Inference`
Frozen source ref: `c6ed0fb40c702936ec1f41454390ef188a5b4d97`

Natural user request:

> 把这批原始研究材料整理成一份给导师看的研究更新：重点说明 clean CARE / M&Ms 证据现在到底支持什么 site-conditioned measurement heterogeneity，哪些解释已经被排除，哪些仍不确定，以及下一步最值得检验的科学问题。不要按实验运行时间线写，也不要暴露内部 job/audit/provenance 细节。

Expected document family: advisor-facing research update / research-evolution note.
Primary language: English advisor-facing scientific prose.
Output source: Markdown.
No existing advisor/group-meeting report may be used as the primary input or outline.

## Scientific scope

Phase 1 ends before personalized partial-pooling results are revealed. It may conclude that the next discriminating question is whether shared information followed by bounded site-specific adaptation can recover measurement validity, but it must not know whether that experiment succeeds.

The document must reconstruct a reader-first scientific story from raw contracts and machine-readable results:

1. why clean subject-disjoint evidence was necessary;
2. what the CARE clean replication established;
3. whether Pattern H survives robustness checks;
4. what M&Ms does and does not add as supporting replication;
5. what these results imply for the next scientific question;
6. what remains uncertain.

## Allowed raw-evidence classes

Only the exact Phase 1 manifest in `PHASE1_INPUT_MANIFEST.md` may be materialized for the Phase 1 model run.

Allowed:
- experiment contracts;
- decision JSON;
- machine-readable bootstrap/summary CSVs listed in the manifest;
- semantic provenance only when listed in the manifest.

Forbidden:
- any existing reader-facing group-meeting/advisor report;
- `docs/CARE_*RESULT*.md` narrative result reports;
- `deliverables/group_meeting_*/**`;
- `docs/TWO_DAY_EXPERIMENT_SYNTHESIS_2026-09-04.md`;
- `docs/EXPERIMENT_DECISION_LINEAGE_2026-09-04.md`;
- all Phase 2 personalized-partial-pooling files;
- any later narrative that states the Phase 2 result.

## Isolation contract

Before final G2 begins, Executor must materialize the exact Phase 1 manifest into a task-local read-only directory:

`private/exports/research-authoring--formal-production-authoring/final_tasks/G2/runtime_input/phase1/`

The Phase 1 runtime receives only that materialized directory plus the frozen task/rubric. It must not run from the full DII checkout and must not have the Phase 2 directory in its input set.

This is input isolation for final evidence, not a new persistent state system.

## Freshness statement

The exact task above was frozen on 2026-10-05 after Research Authoring candidate C0 existed. The 059 design/development evidence used other DII report-writing regressions; targeted searches of the 059 design/result material found no use of this exact clean subject-disjoint / H-ROBUST / personalized-partial-pooling two-stage task as a 059 product-tuning sample.

The DII repository is not claimed to be globally unseen. The **exact final task, exact raw input set, Phase 1 output, and withheld Phase 2 delta** are the fresh objects.

If pre-final Critic finds direct evidence that this exact task was used to tune C0, G2 remains blocked and no final run starts.
