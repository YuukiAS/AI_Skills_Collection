# Research Authoring route receipt

The requested authoring-stage deliverables are complete: the advisor-facing source and downstream production handoff. The eventual formal PDF remains pending with the renderer owner.

## Document brief and route

- Family: advisor-facing research report; audience: PI/advisor.
- Decision: next week's priority, personalization ablation or expanded robustness checks for a clean subject-disjoint split.
- Authority: only `../inputs/01-C2_DEV_REPORT_RAW_NOTES.md`. No external literature, hidden experimental artifacts, or independently rerun analyses were used.
- Language: English, following the supplied notes and task; interactive status messages are Chinese under workspace policy.
- Route used: Research Authoring `research-reporting` entry → `research-authoring-core` coordinator → `research-reporting` delegate and advisor-report reference → `writing-fidelity` and `scientific-prose` passes → document-level QA → downstream renderer handoff.
- Scope: new report, not an incremental edit. The opening frames the decision; Table 1 carries evidence; interpretation distinguishes uncertainty; the final section requests a real advisor choice.
- Scientific roles: one evidence table; no required figures or formulas. Operational provenance belongs here, outside the advisor report.
- Citation authority: supplied notes only. No bibliography or unsupported external citation was added.

## Claim–evidence checks

| Source anchor in raw notes | Treatment in source report |
| --- | --- |
| Replication finished under current preprocessing contract; clean subject-disjoint split | Reported as supplied; no independent audit claimed |
| Macro-F1 0.714 and 0.671 | Exact values retained; +0.043 is a derived subtraction, not an additional measured result |
| Paired bootstrap 95% CI [0.018, 0.071] | Retained as the interval for the main macro-F1 difference |
| Pattern H shifted cohort; temporal model ahead; interval [0.004, 0.049] | Direction and endpoints retained; missing point estimates, interval method, and confidence level disclosed |
| Most residual mistakes in sequences with fewer than four observations | Preserved without converting error concentration into a subgroup error-rate claim |
| Pilot recall 0.46 to 0.51; one seed | Preserved as preliminary; no repeated-seed evidence or uncertainty invented |
| Decision between robustness and personalization | Robustness-first recommendation explicitly framed as interpretation for discussion; alternative retained |
| No clinical validity or deployability claims | Both boundaries explicitly retained |

## QA and production boundary

Source-level review checked numerical fidelity, evidence strength, metric separation, missing-method disclosures, and advisor relevance. The English prose pass retained the caveats and removed the need for an execution chronology. The recommendation is editorial synthesis of the supplied evidence, not an observed finding or an approved experimental protocol. No statistical design or analysis was executed.

The user explicitly defines this standalone surface as lacking the approved renderer companion. The route honors that constraint even if a generic skill catalog lists rendering capabilities elsewhere. No renderer was invoked, installed, or replaced; no PDF was created or visually inspected. The exact downstream dependency is `skills/tools/documents-media/render-chinese-math-pdf`. Scientific authoring remains owned by Research Authoring; artifact mechanics and rendered QA belong to that renderer owner.

Delivered files: `advisor_update_source.md`, `downstream_renderer_handoff.md`, and this `route_receipt.md`. The handoff specifies artifact purpose, table/figure roles, protected content, remaining production checks, and PDF acceptance. The current three-file request is complete; eventual formal-PDF production is not complete.
