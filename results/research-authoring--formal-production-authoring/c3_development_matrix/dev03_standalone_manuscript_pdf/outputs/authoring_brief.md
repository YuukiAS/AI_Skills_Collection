# Authoring brief

## Scope and authority

Document family: paper / manuscript source package. Surface: standalone Research Authoring candidate; source and handoff only. Language: English, matching the notes. Audience: lesion-segmentation researchers and manuscript coauthors. Purpose: communicate a preliminary evaluation of test-time percentile clipping without treating it as established robustness.

Sole scientific authority: `inputs/01-manuscript_notes.md`. No raw images, per-volume results, executable methods, references, author metadata, or venue specifications were supplied. No literature discovery or new experiment is required or performed. The source notes' “may improve” wording remains provisional throughout the paper.

## Claim–evidence spine

| Claim | Evidence | Permitted strength / destination |
|---|---|---|
| Test-time percentile clipping precedes an existing 3D U-Net inference pipeline | Method statement in notes | Descriptive method; Methods |
| Evaluation concerns one internal validation split of 18 volumes | Study boundary in notes | Split-specific; Abstract and Methods |
| Small-lesion Dice 0.421 to 0.469; mean Dice 0.742 to 0.758 | Tentative aggregate values in notes | Preliminary reported comparison, not independently verified; Table 1 and Results |
| HD95 18.4 to 17.9 mm | Aggregate values in notes | Descriptive comparison; Table 1 |
| Motion-corrupted scan remains a failure | Explicit negative observation | Retained in Abstract, Results, and interpretation |
| Broad robustness, significance, generalization, novelty | No supporting evidence | Excluded |

Absolute differences are editorial arithmetic on the supplied rounded values, not new analyses. The 18-volume count is not a lesion count or a confirmed patient count.

## Section outline frozen before drafting

- Abstract: question, intervention, evaluation scope, tentative values, persistent failure, bounded conclusion.
- Introduction: ask whether the intervention merits further evaluation; no unsupported field-wide gap or novelty claim.
- Methods: describe the known pipeline change, split and metrics; explicitly identify missing reproducibility information.
- Results: present all supplied values in Table 1 and retain the negative finding.
- Discussion: interpret numerical changes within this split; distinguish aggregate behavior from corruption tolerance.
- Limitations: address unavailable protocol details, uncertainty, selection history, and external evidence.
- Conclusion: state a provisional split-specific finding.
- Declarations and references: visible pending statements, without fabricated metadata or citations.

Main text contains scientific content and necessary limitations. Production instructions, provenance, evidence checks, and author actions remain outside `paper.md`. Table 1 is the complete quantitative summary. No figures or equations are warranted by the supplied material.

## Owner route

Research Authoring core → paper-workflow-orchestrator → scientific-writing → reviewer-style source audit → scientific-prose → stable source/package and production handoff. Delegates are applied within this session; no independent peer review is claimed. No renderer is admitted on this standalone surface. A downstream admitted renderer must return its PDF to Research Authoring for final scientific QA.
