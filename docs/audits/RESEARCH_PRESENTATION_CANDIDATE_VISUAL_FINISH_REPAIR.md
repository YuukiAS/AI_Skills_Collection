# Research Presentation Candidate Visual Finish Repair

Task: `022_research_presentation_candidate_visual_finish_repair`

This report records the candidate-layer visual finish repair performed after
the 021 blind comparative review. It is implementation evidence, not a Planner
review or a program-level quality pass.

## 021 Gap To 022 Repair Mapping

Statistical estimator/equation gap from 021:

- generated candidates placed a high-quality equation asset into a low-contrast
  black rendering path because transparent pixels were flattened incorrectly;
- the equation was treated like content inside a generic rounded card;
- the annotation described the middle term but did not directly bind to the
  mathematical object.

022 repair:

- transparent equation assets are flattened onto the slide background before
  scaling;
- equation regions are drawn directly as primary scientific objects, without
  decorative card containers;
- equation candidates record `equation_rendering.contrast=high`;
- equation candidates record an `annotation_targets` entry from `annotation` to
  `equation`;
- the renderer draws an amber middle-term marker and a leader from the
  annotation to the equation target.

Medical-image gap from 021:

- generated candidates used generic card/padding treatment around images;
- image evidence was too small or sparse in some layouts;
- panel labels and legend were not sufficiently integrated with the image row;
- synthetic fixture imagery remained a real limitation.

022 repair:

- medical image regions are drawn as semantic panels with adjacent panel labels,
  not rounded UI cards;
- embedded source labels are cropped out before rendering, while the full lesion
  evidence is preserved by contain scaling;
- legend swatches are rendered as a shared image-evidence legend;
- reference-faithful and alternative medical candidates have larger primary
  image regions than their 020 counterparts;
- the manifest records `panel_correspondence`, `legend_binding`, and an explicit
  synthetic evidence boundary.

## Generic Renderer Changes

The repair is implemented in the shared candidate renderer, not by hardcoding a
single slide:

- `visual_tokens` are shared across all three candidates in each case;
- `primary_object_treatment.decorative_card_used=false`;
- `primary_object_treatment.container_role=none`;
- source-derived regions and `geometry_transfer` remain in the manifest;
- preview artifacts are generated into a new task-owned output root so 020
  identities remain intact.

The same logic is mirrored under `plugins/codex/plugins/presentations/shared/`.

## Before And After Candidate SHA

### Statistical estimator/equation

| Strategy | 020 preview SHA | 022 preview SHA |
| --- | --- | --- |
| `reference_faithful` | `cb7c0ee7ae7806b09699ee902a81d009677f95beaf775deea300577efbf1138e` | `3e8c2ca21e5605d1b447dcbb268093126434ff6afa59eb3dc1551a8bad2bc671` |
| `alternative_composition` | `4964d0056724766b8c8d0f34e0c91df9d5c9799f208ee2aa4ab31ddb61d76f7d` | `76ff6138d5d64b96af1e41dcae4b8a94bb618558d49b66489d5cb01742ae1e7c` |
| `controlled_wildcard` | `43f2c9c6d94959f2bb89f775c1f4e72477c9025ee942b06c93b83ff95c3c9efc` | `efb992119ec7da688c8e2b825f7b1c6125c51b78452eb68d4a92c563e27d0b74` |

### Medical-image comparison

| Strategy | 020 preview SHA | 022 preview SHA |
| --- | --- | --- |
| `reference_faithful` | `5f599c2a9ffecee90291fe7c91050f9a57925894ad226a83bb58a82f5fb3da26` | `89c63ca162020df3b7718693f5b01e7dc42d4ed7c5795d6ceda2b9cf62870173` |
| `alternative_composition` | `fc5d853706e7f39b694e9c91eb18a9a2b33600e2f7df56ef5f5e78b715b967f0` | `e16022d1e05c772dacf8d079a1b725be0e141438fd444c3bd48c25da3e251e6c` |
| `controlled_wildcard` | `08ec78b40bb40c389f30f1888c938083a9f1eac979345902c1ba316d387ac83f` | `9230b6d48cefd5dffaf0180844139ac2475bbe7742b6e84423636b1bee628c66` |

## Geometry And Compatibility Preservation

The repaired manifests preserve the core 019/020 contracts:

- statistical sources remain equation-compatible estimator pages;
- medical sources remain medical-image-compatible pages;
- selected source bboxes still drive candidate regions through
  `geometry_transfer`;
- same-family medical sources still produce different primary bboxes;
- audience-facing text still avoids RRL/SRC IDs, candidate strategies,
  provenance, and QA language.

## Known Limitation

The medical candidates still use deterministic synthetic regression fixture
imagery. 022 can improve image prominence, panel labels, legend integration, and
layout finish, but it cannot convert synthetic phantom evidence into real
clinical research evidence. Any remaining Terra concern about synthetic/demo
realism must be left for the later real medical-imaging holdout.

## New Comparative Review

022 generated a new blind comparative review package with candidate previews
from:

`docs/audits/research_presentation_candidate_visual_finish_repair/generated`

The package writes its task-owned visual evidence under:

`results/022_research_presentation_candidate_visual_finish_repair/visual_review`

Visible review identity uses `022_visual_finish_comparison`, anonymous item IDs,
and the same matched references as 021.

The GitHub Actions workflow completed successfully on run `32639276412` and
committed the live Terra evidence in `9b7b5bc`.

### Statistical estimator/equation decoded result

Evidence:

- `results/022_research_presentation_candidate_visual_finish_repair/visual_review/statistical/VISUAL_REVIEW.json`
- `review_identity_sha256=e68fc684220a87f638e7670bccf1be7c3745b079429af5bc0642f56a55f45637`
- `review_identity=f1fa4cc1b301f2717ca9316a31e0741d0c28efabaa7bbc6f5e39dfb682db1aca`
- `status=PASS`, with no package-level blocking findings

Decoded anonymous mapping:

| Anonymous item | Real identity | Terra decision | Decoded meaning |
| --- | --- | --- | --- |
| `item_A` | 022 `alternative_composition` candidate | `REVISE` | Readable, but detached lower text and excess whitespace keep it below the mature-talk bar. |
| `item_B` | reference `RRL-014`, page 18 | `REVISE` | Weak estimator comparison for this page job because the imagery is fragmented and edge-cropped. |
| `item_C` | 022 `reference_faithful` candidate | `PASS` | Strongest item; direct math annotation and balanced central composition reach mature research-group-meeting quality. |
| `item_D` | reference `RRL-028`, page 14 | `REVISE` | Clean equation, but under-annotated and mostly blank. |
| `item_E` | 022 `controlled_wildcard` candidate | `REVISE` | Solid and readable, but lower content split weakens composition versus `item_C`. |

Terra's relative ordering places the repaired `reference_faithful` statistical
candidate first. This is the only statistical item judged to reach the mature
research-group-meeting / strong conference-talk bar. The result specifically
validates the 022 repair focus: high-contrast equation treatment, direct
middle-term annotation, and removal of generic card framing.

### Medical-image comparison decoded result

Evidence:

- `results/022_research_presentation_candidate_visual_finish_repair/visual_review/medical/VISUAL_REVIEW.json`
- `review_identity_sha256=68fef1307429e6792d548eb8363bb37239f5164aafb6ad997fe7a818d4741ac3`
- `review_identity=20e12347bfbb02ffeded337d9b9d1203b930467db2240ab11d1adbd6e5c6cf47`
- `status=PASS`, with no package-level blocking findings

Decoded anonymous mapping:

| Anonymous item | Real identity | Terra decision | Decoded meaning |
| --- | --- | --- | --- |
| `item_A` | 022 `alternative_composition` candidate | `PASS` | Coherent three-panel comparison that reaches mature research-group-meeting quality, with some unused lower whitespace. |
| `item_B` | reference `RRL-013`, page 14 | `REVISE` | Image-specific but cluttered; contour encodings are not explained. |
| `item_C` | reference `RRL-022`, page 21 | `REVISE` | Scientifically specific but visibly cropped/incompletely framed in this rendered page. |
| `item_D` | 022 `reference_faithful` candidate | `REVISE` | Clean and legible, but images remain underscaled and interpretation is under-integrated. |
| `item_E` | 022 `controlled_wildcard` candidate | `PASS` | Best item; asymmetric layout gives the lesion overlay visual priority and groups the error map, takeaway, and legend as support. |

Terra's relative ordering places the repaired `controlled_wildcard` medical
candidate first, followed by the repaired `alternative_composition` candidate.
Both are judged to reach mature research-group-meeting quality. The result also
records a remaining implementation lesson: the reference-faithful medical path
is clean but still too conservative because the evidence bands remain
underscaled.
