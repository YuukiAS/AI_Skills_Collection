# Research Authoring route receipt

The requested authoring stage is complete: the advisor-facing scientific source and downstream production handoff are saved. The eventual formal PDF has not been produced, and no render or visual QA is claimed.

## Route and frozen brief

Used the installed `research-authoring:research-reporting` entry, read its `research-authoring-core` coordinator first, then applied the `research-reporting` delegate and its mandatory advisor-report reference. Applied `research-authoring:writing-fidelity` to protect evidence and `research-authoring:scientific-prose` with its report checklist for the final English prose pass.

The document family is a report for a PI choosing between personalization and expanded robustness checks next week. Authority is limited to `inputs/01-C2_DEV_REPORT_RAW_NOTES.md` and the current user request. This is new authoring, not an edit of an accepted report. English preserves the source language. No web lookup, literature verification, experiment execution, or independent statistical validation was needed or performed.

The opening states the decision and a conditional recommendation; the evidence section compares the reported outcomes and their limitations; the final section presents a proposed priority and the unresolved advisor choice. Table 1 carries exact results. No figure, formula, or external bibliography is needed. Operational provenance stays in this receipt and the handoff.

## Claim–evidence checks

| Source anchor in raw notes | Treatment in the source report |
| --- | --- |
| Observed evidence, bullets 1–4 | Completed clean subject-disjoint replication; scores and paired bootstrap interval preserved; +0.043 explicitly marked as derived arithmetic |
| Observed evidence, bullet 5 | Pattern H advantage and interval preserved; unspecified method, confidence level, and point estimate remain unspecified |
| Observed evidence, bullet 6 | Residual-error concentration for fewer than four observations retained; no invented subgroup error rate |
| Observed evidence, bullet 7 | Recall values retained with the single-seed, preliminary caveat; no inferred macro-F1 improvement |
| Constraints | No clinical-validity or deployability claim; scientific source delivered without rendering |
| Decision needed | Personalization priority framed as a recommendation; robustness expansion retained as the advisor's alternative |

Final content review checked numerical fidelity, comparator and metric identity, uncertainty placement, separation of observations from proposals, and advisor relevance. The report does not infer mechanism, broad generalization, reproducibility, or statistical significance beyond the supplied information. The proposed follow-up is a decision brief; detailed experiment and statistical design remain with the experiment owner.

## Downstream boundary and status

Required downstream owner: `render-chinese-math-pdf`, dependency `skills/tools/documents-media/render-chinese-math-pdf`. The user's explicit standalone-surface constraint governs this task even if a renderer skill is visible elsewhere in the host catalog. No renderer was invoked, installed, or substituted.

- Current Markdown authoring deliverables: complete.
- Formal PDF: pending approved downstream renderer.
- PDF layout, font, extracted-text, and visual QA: not performed.
- Production instructions and acceptance checks: `downstream_renderer_handoff.md`.

## Artifact identity

SHA-256 values below bind the evidence input and the two handoff artifacts to this receipt. The receipt itself is not self-hashed.

- `inputs/01-C2_DEV_REPORT_RAW_NOTES.md`: `96ece1b53a95ec5fec8935c47c01e02318af8eb6915fb4f876e225c84f512703`

- `outputs/advisor_update_source.md`: `209bf818682d44507353a88614311b4cd26095e4e12c86ead2cbe0b29ca51733`

- `outputs/downstream_renderer_handoff.md`: `4ab65ed61623450d87a3382967a4a7f38c24db513bef28392f950898043d8c4b`
