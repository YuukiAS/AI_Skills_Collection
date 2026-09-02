---
schema: AI_SKILLS_WRITING_STYLE_PUBLIC_REGRESSION_REPORT_V1
task_key: 048_writing_style_product_cutover_and_readable_report
implementation_identity: 928de2325d781ca630883d03e0f381092675b269
role: regression_only_not_unseen_proof
---

# Public Regression Report

This report records the fixed public regression units required by the 048 revised Plan. These artifacts prove regression behavior only; they are not used as unseen product proof, and they are not seed examples for `scientific-rewrite`.

## Source Retrieval

- `YuukiAS/Bobbio@2d8a054bd34291dc061b8b64d5d841d458cc6296`: shallow cloned to `/tmp/048-Bobbio`; extracted `README.md` lines 1-70.
- `YuukiAS/Distributed_Imaging_Inference@0e895fdbce37c34967d8375059154df1d76397f4`: shallow cloned to `/tmp/048-Distributed_Imaging_Inference`; extracted `docs/SEGCOMM_CORRECTION_STABILITY_REPORT_2026-08-28.md` lines 1-8.
- `YuukiAS/AI_Research_Toolkit@b822dff09794766a1a013b100eb8f78a45514c7b`: downloaded public `R_RESEARCH_STACK.md`; extracted lines 1-13.
- `YuukiAS/Asteria@80ad881bc88ad1caf017959e320e539028eb5a25`: downloaded public `ROADMAP.md`; extracted lines 5-17.

## Results

| Unit | Expected behavior | Exact check | Semantic assessment | Reader-effort assessment |
| --- | --- | --- | --- | --- |
| `positive_a_bobbio` | Meaning-preserving natural rewrite | PASS: 6 checked, 0 missing | Preserves local-first/human-in-the-loop workbench scope, the full knowledge chain, Bobbio Abbey naming rationale, problem inventory, and Radar decision boundary. | Lowers effort by replacing list-like problem fragments with explicit cause/effect prose while keeping the original module sequence. |
| `positive_b_distributed_segcomm` | Meaning-preserving natural rewrite | PASS: 17 checked, 0 missing | Preserves `{1,4,5}`, FedAvg, AdamW state carryover, CARE fold-0, checkpoint, LGE-only, 7 clients, 20 local updates, pooled/FedAvg comparisons, seed caveat, and R=5 vs R=1 conclusion strength. | Lowers effort by separating setup correction from result interpretation and explicitly marking which findings are stable versus seed-sensitive. |
| `should_not_fix_a_ai_research_toolkit` | Low edit / no deep rewrite | PASS: 9 checked, 0 missing | Candidate equals source. It keeps `renv`, `BiocManager`, `sessionInfo()`, version/reproducibility constraints, and method-pair examples unchanged. | No style rewrite was applied because the source already reads as concise operational guidance and contains version-sensitive setup constraints. |
| `should_not_fix_b_asteria` | Low edit / no deep rewrite | PASS: 0 checked, 0 missing | Candidate equals source. It keeps the product positioning, quoted English tagline, and `canvas` framing unchanged. | No style rewrite was applied because the passage is already reader-facing product reasoning rather than log-like scientific prose. |

## Gate Status

- Literal critical drift: 0 observed by deterministic helper.
- Semantic critical violation: 0 observed by manual source/candidate audit for the fixed snippets.
- Should-not-fix over-editing: 0 observed; both should-not-fix candidates are byte-identical to their extracted sources.
- Limitation: This is public regression evidence only. Final product proof still depends on the full private Deep Research transform, deterministic private fidelity report, independent Text Review, Scheduled GPT Reviewer, and user ACCEPT.
