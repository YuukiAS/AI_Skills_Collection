# Research Authoring route receipt

## Frozen document brief

- Intent and family: author a new, concise advisor-facing research update (`report`) and prepare downstream PDF production; this stage delivers Markdown only.
- Audience and decision: PI/advisor choosing next week's personalization ablation versus expanded robustness checks.
- Authority: `inputs/01-C2_DEV_REPORT_RAW_NOTES.md` only. No external lookup, experimental execution or independent validation of the supplied results.
- Claim spine: temporal advantage in the supplied subject-disjoint replication; direction retained under Pattern H; residual errors concentrated in short sequences; personalization evidence preliminary and single-seed. Prioritizing an ablation is a qualified recommendation.
- Section jobs: opening states the decision and recommendation; evidence section compares results and bounds interpretation; final section states the proposed test and the advisor's choice.
- Visual roles: one comparison table; no necessary figure or formula. No external citation or bibliography authority was supplied.
- Language and scope: English artifacts follow the English input and task; new source authoring, no existing accepted document to revise. Production provenance stays in this receipt and the handoff.

## Route used

Read the installed `research-reporting` aggregate entry, then entered its `research-authoring-core` coordinator before selecting the `research-reporting` delegate. Applied its advisor-report reference. Applied `writing-fidelity` to protected evidence and `scientific-prose` plus its report checklist for the English prose pass. These were authoring workflows applied in this session, not separate agents or external reviewers.

The explicit task contract identifies this standalone Research Authoring surface as lacking the approved PDF renderer companion. Therefore the terminal route for this stage is stable scientific Markdown → full handoff to `render-chinese-math-pdf` (`skills/tools/documents-media/render-chinese-math-pdf`). No alternate renderer, compilation command, PDF opening, rasterization or PDF-derived QA was used. The broader skill catalog does not override this task-specific boundary.

## Claim-to-evidence check

| Source evidence | Report treatment |
| --- | --- |
| Replication complete under current preprocessing contract | Presented as the reported experimental setting, without inventing cohort size or run details |
| Macro-F1 0.714 vs 0.671 | Preserved; +0.043 is arithmetic derived from these scores |
| Paired bootstrap 95% interval [0.018, 0.071] | Preserved for the macro-F1 difference; no resampling unit inferred |
| Pattern H shifted-cohort advantage; interval [0.004, 0.049] | Direction and endpoints preserved; confidence level, method and missing point estimate not invented |
| Most mistakes in sequences with fewer than four observations | Preserved as error concentration, not a quantified subgroup rate |
| Pilot recall 0.46 to 0.51, one seed | Preserved as preliminary; no claim of overall macro-F1 improvement or reproducibility |
| No clinical validity or deployability claims | Explicit limitation retained |
| Choice of next-week priority | Proposed ablation separated from observation and advisor approval; robustness alternative retained |

## Source-only acceptance and delivery

The report was checked against the supplied notes for numerical fidelity, interval attribution, metric separation, single-seed qualification and claim strength. The English prose pass keeps scientific evidence ahead of production details, avoids repeated result summaries and ends with the actual advisor decision. The proposed experiment is clearly future work; its detailed statistical and adaptation design remains with the experiment owner.

Delivered: `advisor_update_source.md`, `downstream_renderer_handoff.md`, and this `route_receipt.md`, all under `outputs/`.

Authoring-stage delivery: complete. Formal PDF production: not performed and pending with the approved downstream owner. No layout, font, pagination or rendered-artifact pass is claimed.
