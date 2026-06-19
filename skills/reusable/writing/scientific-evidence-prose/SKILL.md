---
name: scientific-evidence-prose
description: English scientific report writing and revision pass. Use for research reports, progress reports, figure-heavy PDFs, manuscripts, technical summaries, and slide text that must keep evidence, uncertainty, captions, and conclusions scientifically defensible without AI-sounding prose.
status: active
provenance: local
trusted: true
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-06-01
profile_tags:
recommended_scope: project
license: MIT-compatible synthesis from cited public/academic writing guidance
---
# Scientific Evidence Prose

Use this skill as the final English writing pass for scientific reports and research communication. It is not a layout tool. It makes prose scientifically defensible, readable, and less template-like.

## Use When

- Writing or revising English research reports, progress PDFs, lab updates, manuscripts, thesis sections, figure captions, or technical summaries.
- Turning experiment notes, ablations, error analysis, tables, or figures into report prose.
- Checking whether a result statement overclaims beyond the evidence.
- Making slide/report text sound like a researcher describing evidence, not a generic AI summary.

Do not use it for pure citation search, document conversion, or journal formatting. Use the relevant discovery, PDF, DOCX, PPTX, or venue skill for those tasks.

## Core Rule

Every paragraph should answer one reader question:

1. What question is being addressed?
2. What evidence is available?
3. What can be concluded from that evidence?
4. What remains uncertain?
5. What decision or next step follows?

If any part is missing, keep the wording bounded rather than filling the gap with confident prose.

## Workflow

1. Identify the document type: report, progress update, manuscript section, figure caption, slide text, or executive summary.
2. Protect the evidence ledger: numbers, metrics, cohorts, baselines, sample sizes, methods, dates, versions, figure labels, statistical qualifiers, and source attributions.
3. Mark claims by strength:
   - `observed`: directly shown in the supplied result.
   - `supported`: follows from multiple supplied observations.
   - `hypothesis`: plausible but not yet tested.
   - `speculation`: useful idea, but not evidence-backed.
4. Rewrite so confidence matches claim strength.
5. Remove AI-like prose patterns: grand openings, vague importance claims, "this highlights", "underscores", unsupported "significant", generic future-work endings, and symmetrical three-item filler.
6. Check information flow: old/context information first, new/emphasized result last.
7. For figures, check that captions and body text do different jobs.
8. Return the revised text. If the input is risky, add a short "Evidence notes" section listing overclaims or missing evidence.

## Report Paragraph Pattern

Prefer this order in English scientific reports:

```text
[Question/context]. [Specific evidence and comparison]. [Interpretation with boundary]. [Uncertainty or competing explanation]. [Decision or next step].
```

Keep it in normal prose. Do not mechanically label every sentence unless the user asked for a checklist.

## Claim Boundaries

Use bounded verbs when evidence is incomplete:

- "suggests", "is consistent with", "we observed", "in this subset", "under this setting"

Avoid stronger verbs unless evidence supports them:

- "proves", "demonstrates" for single runs or unreplicated experiments.
- "significant" without a statistical or practical definition.
- "robust" without sensitivity, subgroup, or external validation.
- "generalizes" without external data or held-out conditions.

## Figure Captions

For figure-heavy reports, captions should usually contain:

1. What is being compared.
2. Under which condition, cohort, model, or dataset.
3. Which metric or visual encoding matters.
4. The main observation.
5. Abbreviations, panels, error bars, and sample sizes if needed.

Do not dump the full method into the caption. Put method differences in nearby prose if they explain the result.

## English Style Pass

Use direct, concrete sentences:

- Replace vague openings with the actual research question.
- Replace "This highlights the importance of..." with the observed consequence.
- Replace "Future work should explore..." with the next test and the decision it will enable.
- Prefer active voice when responsibility matters: "We reran the ablation" instead of "The ablation was rerun".
- Keep technical terms if they are the right terms. Removing expertise is not the goal.

## References

Read `references/scientific-report-checklist.md` when doing a full report pass. Read `references/source-notes.md` when provenance matters.
