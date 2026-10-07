# Downstream Production Handoff

## Package

- Source package: `outputs/manuscript_source_package/`
- Main source: `outputs/manuscript_source_package/paper.tex`
- Bibliography placeholder: `outputs/manuscript_source_package/references.bib`

## Audience And Purpose

The package is intended for a research or production owner preparing a compact preliminary manuscript for formal PDF production. The purpose is to document an evidence-bounded internal validation of test-time percentile clipping before an existing 3D U-Net lesion segmentation inference pipeline.

## Source Authority

The sole source authority for the manuscript content is `manuscript_notes.md`. The manuscript preserves the following evidence boundary:

- preliminary study;
- one internal validation split with 18 volumes;
- method adds test-time percentile clipping before existing 3D U-Net inference;
- small-lesion Dice changes from 0.421 to 0.469;
- mean Dice changes from 0.742 to 0.758;
- HD95 changes from 18.4 mm to 17.9 mm;
- motion-corrupted scan remains a failure case;
- no broad robustness claim is supported;
- no external citations, datasets, reviewer comments, venue requirements, or additional experiments are invented.

## Claim And Evidence Boundary

Supported claim: on the supplied internal validation split, test-time percentile clipping is associated with numerically improved Dice metrics and a small HD95 decrease.

Conditional claim: percentile clipping may help with some intensity-related variation in this split.

Unsupported claims to avoid: broad robustness, scanner/protocol generalization, clinical reliability, statistical significance, superiority over other preprocessing methods, or resolution of motion-corrupted acquisitions.

## Sections And Scientific Roles

- Abstract: compact summary of method, evidence, metrics, and limitation.
- Introduction: establishes the narrow preprocessing question without adding literature claims.
- Methods: documents the existing 3D U-Net pipeline, test-time clipping insertion point, validation split, and unavailable method details.
- Results: reports only the supplied aggregate metrics and the motion-corrupted failure case.
- Limitations: names missing external validation, uncertainty estimates, per-case distributions, exact clipping percentiles, and remaining failure mode.
- Discussion: interprets the result as preliminary and defines follow-up checks before stronger claims.
- Table 1: carries the quantitative metric comparison.
- Citation Support Status: explicitly marks citation support as pending.

## Renderer And Venue QA Still Required

The downstream renderer or venue owner should verify:

- LaTeX compilation with the chosen engine and template;
- table placement and page breaks;
- title, author list, affiliations, acknowledgments, funding, conflicts, data availability, and ethics statements if required;
- exact test-time clipping percentiles, if they are available from the implementation owner;
- bibliography policy for a citation-pending package;
- whether the target venue requires structured abstracts, word limits, figure/table numbering conventions, or specific statements;
- PDF typography, margins, hyperlinks, overfull boxes, and embedded fonts;
- post-render scientific QA to confirm that the PDF still preserves the preliminary scope and failure-case limitation.

## Rendering Route

Recommended next route: an admitted LaTeX/PDF renderer or venue-template owner should consume `paper.tex`, apply the chosen template if needed, render the PDF, and return the rendered artifact for post-render scientific QA. This authoring package does not claim final PDF QA completion.
