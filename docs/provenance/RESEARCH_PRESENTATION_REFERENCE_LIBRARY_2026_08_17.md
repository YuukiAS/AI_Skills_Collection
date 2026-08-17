# Research Presentation Reference Library Intake

Date: 2026-08-17

Scope: Presentation plugin upgrade for `research-presentations` and shared deck-plan/QA references.

## Source Boundary

User-provided Deep Research PDF:

```text
博士科研汇报页面级参考库：Research Presentation Reference Library.pdf
```

The PDF is kept out of git. Text was extracted locally to:

```text
.cache/research-presentation-reference-library/reference-library.txt
```

The report claimed a richer generated bundle/CSV/MD package, but the objective attachment directory contained only `goal-objective.md`, and the repository root contained only the PDF. Therefore this intake rebuilt a compact repository index from the PDF text and public source URLs rather than importing a missing bundle.

## Public Sources Checked

Downloaded or captured into ignored `.cache/research-presentation-reference-library/sources/`:

| Source | Local audit copy | Status |
|---|---|---|
| MIT annotated first PhD committee PDF | `mit_annotated_first_phd_committee.pdf` | downloaded |
| MIT qualifying exam presentation page | `mit_qualifying_exam_presentation.html` | downloaded |
| MIT thesis proposal page | `mit_thesis_proposal.html` | downloaded |
| CMU Long Pham thesis proposal slides | `cmu_long_pham_proposal_slides.pdf` | downloaded |
| SFU ISIC 2025 presentation | `sfu_isic2025_presentation.pdf` | downloaded |
| SFU ISBI 2025 presentation | `sfu_isbi2025_presentation.pdf` | downloaded |
| SFU ISIC 2024a presentation | `sfu_isic2024a_presentation.pdf` | downloaded |
| SFU ISIC 2024b presentation | `sfu_isic2024b_presentation.pdf` | downloaded |
| SFU ISIC 2022 presentation | `sfu_isic2022_presentation.pdf` | downloaded |
| SFU ISIC 2021 presentation | `sfu_isic2021_presentation.pdf` | downloaded |
| SFU researcher page | `sfu_kumar_abhishek.html` | downloaded |
| Joseph Gonzalez lectures archive | `berkeley_joseph_gonzalez_lectures.html` | downloaded |
| Joseph Gonzalez RISE PPTX | `gonzalez_outline_ml_challenges_rise.pptx` | downloaded |
| Kaiming He CVPR ResNet slides | `kaiming_cvpr2016_resnet.pdf` | downloaded |
| Amber Kerr qualifying exam page | URL recorded | live download timed out |

## Rights And Privacy Rule

Committed artifacts contain only metadata, URL, page/source number, page function, visual lesson, what to learn, what not to copy, and rights notes. No downloaded public deck, whole-slide screenshot, full public PDF, original PPTX, private CARE figure, or clinical image is committed by this intake.

## Adopted Repository Files

- `skills/tools/documents-media/presentations/shared/references/RESEARCH_GROUP_MEETING_MODE.md`
- `skills/tools/documents-media/presentations/shared/references/RESEARCH_SLIDE_ARCHETYPES.md`
- `skills/tools/documents-media/presentations/shared/references/RESEARCH_PRESENTATION_ANTIPATTERNS.md`
- `skills/tools/documents-media/presentations/shared/references/research_slide_reference_index.csv`

## Decision

Decision: `reference-only` plus source-layer skill upgrade.

Reason: the Deep Research report is a useful reference library and failure synthesis, but its source assets are not repository-owned. The durable integration is evidence-first workflow, schema/validator checks, scientific QA, reference metadata, and regression fixtures, not copied slide pages.
