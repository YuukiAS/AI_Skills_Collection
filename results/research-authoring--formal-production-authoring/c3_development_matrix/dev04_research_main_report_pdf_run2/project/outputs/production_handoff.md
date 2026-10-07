# Production Handoff and Route Receipt

## Research Authoring brief

- Task intent: prepare a concise advisor-facing research update from `report_notes.md` and deliver a formal readable PDF.
- Audience: research advisor deciding the next-week priority.
- Document family: advisor-facing research update / technical progress report.
- Source authority: `report_notes.md` only.
- Evidence boundary: 18 internal development validation volumes; baseline nnU-Net-style 3D U-Net; candidate method is baseline plus test-time intensity percentile clipping; same split and fixed preprocessing for all rows.
- Protected quantitative evidence: mean Dice 0.742 vs 0.758; small-lesion Dice 0.421 vs 0.469; HD95 18.4 mm vs 17.9 mm; one severe-motion scan still has disconnected false positives under both methods.
- Interpretation boundary: promising validation-only reliability check, not a final benchmark or external-generalization claim.
- Reader decision: whether to prioritize calibration analysis before architecture changes.
- Table role: compact comparison of metrics and absolute changes; table carries exact values.
- Figure role: none.
- Formula role: none.
- Citation authority: no external citations requested or used.
- Main text vs provenance boundary: scientific argument in `research_update.md`; rendering, route, and QA evidence in `outputs/`.

## Renderer route receipt

- Route: Markdown source to PDF through Pandoc and XeLaTeX.
- Source: `outputs/research_update.md`.
- Target PDF: `outputs/research_update.pdf`.
- Project-local canonical render script: not present in this minimal project checkout; direct Pandoc/XeLaTeX command used as the equivalent formal route.
- Paper: letter.
- Margins: 0.85 inch.
- Font size: 10 pt.
- Language: English scientific report.
- Math content: none beyond metric names and table values.
- Renderer QA required: successful command, non-empty PDF, page count, embedded-font check, text extraction check, table readability check, first-page PNG preview, post-render scientific QA.

## Claim-evidence map

| Claim | Evidence anchor | Strength |
|---|---|---|
| Percentile clipping improved all reported metrics on the validation split. | Table values from `report_notes.md`: mean Dice 0.742 to 0.758, small-lesion Dice 0.421 to 0.469, HD95 18.4 mm to 17.9 mm. | Observed in supplied validation evidence. |
| The clearest observed gain is in small lesions. | Absolute small-lesion Dice change +0.048 versus mean Dice +0.016 and HD95 -0.5 mm. | Supported by supplied metric comparison. |
| Motion-driven disconnected false positives remain unresolved. | One severe-motion scan has disconnected false positives under both methods. | Observed failure case. |
| Calibration should be checked before architecture changes. | Candidate improves metrics without addressing the shared motion failure; advisor's decision point is calibration before architecture. | Recommendation based on bounded evidence, not proof. |

## Route status

Complete. Renderer evidence is recorded in `outputs/renderer_evidence.md`; post-render scientific QA is recorded in `outputs/scientific_qa_note.md`; final PDF is `outputs/research_update.pdf`.
