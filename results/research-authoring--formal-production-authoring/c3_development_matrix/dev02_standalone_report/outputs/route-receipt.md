# Research Authoring route receipt

- Requested artifact: concise advisor-facing research update in Markdown, with a short comparison table and a clear next decision.
- Route used: installed `research-writing:research-reporting` entry → `research-authoring-core` coordinator → `research-reporting` delegate → source-level scientific QA.
- Entry: `/users/a/e/aereinh/.codex/plugins/cache/ai-skills-candidate/research-writing/0.3/skills/report/SKILL.md`.
- Coordinator and delegate: entry-relative `_src/core/source.md`, then `_src/report/source.md` and its `references/group-meeting-advisor-reports.md`.
- Supporting passes: `writing-fidelity` for source preservation; `scientific-prose` and its report checklist for English scientific wording.

## Document brief and evidence boundaries

- Family and audience: report for an advisor deciding whether next week should prioritize calibration or architecture.
- Source authority: `../inputs/01-report_notes.md`; no external literature or additional experimental evidence used.
- Language: English, following the supplied notes and requested report context.
- Claim/evidence spine: the supplied metric pairs support a descriptive improvement with clipping, especially in small-lesion Dice; the reported motion case establishes a remaining failure. The 18-volume internal validation scope limits interpretation. Calibration-first is an author recommendation for the advisor's decision, not an observed calibration result or an approved experiment.
- Paragraph jobs: recommendation and question; comparison design; metric table; interpretation and limits; proposed next analysis; advisor decision.
- Table role: compare the three supplied metrics directly, preserving all six values and HD95 units. No figures or formulas are needed.
- Citation authority: supplied research notes only; no bibliography requested or invented. Provenance stays in this receipt rather than the advisor narrative.
- Edit scope: new report from notes; no existing canonical report was supplied.

## Delivery and source QA

- Report source: `advisor-research-update.md`.
- Verified against the notes: sample size, internal validation split, baseline identity, fixed preprocessing, clipping intervention, all metric values, severe-motion failure, interpretation boundary, and advisor decision.
- Wording review: distinguishes observations, interpretation, and proposed work; makes no significance, external-generalization, clinical-readiness, or measured-calibration claim. No invented experiment settings, dates, or references.
- Intended format and final route: Markdown source delivered directly. PDF production was not requested; no renderer was invoked and no layout QA is claimed.
- If rendering is later requested, an explicitly admitted renderer should preserve this source, table, and evidence boundaries. Research Authoring should then recheck numeric fidelity, metric directions and units, readable table presentation, and the distinction between observed results and the proposed calibration analysis.
