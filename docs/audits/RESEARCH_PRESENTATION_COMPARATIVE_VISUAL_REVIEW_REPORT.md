# Research Presentation Comparative Visual Review Report

Task: `021_research_presentation_comparative_reference_calibrated_visual_review`

This report decodes the blind comparative Terra reviews produced for task 021.
It is internal evidence for the Reviewed Handoff Planner. It is not a Planner
decision and does not mark the Presentation improvement cycle complete.

## Execution Identity

- Preparation commit: `54b15cb96bd9b9eb8737b5a635e713a7eb243218`
- Manifest compatibility repair: `83a016a6e0f1e7e5b17c16b2952898ecef1a3ddc`
- Workflow output-path repair: `2645eeed58ab74d35019f07f39ed8e1e7f574ef2`
- Evidence commit: `9c067258bca35ed25ff8ffc8a26171d9a733f163`
- Successful workflow run: `32634528235`
- Workflow URL: `https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/32634528235`

The successful workflow ran exactly one statistical comparative review and one
medical comparative review with `gpt-5.6-terra`.

## Evidence Files

- Statistical manifest: `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/statistical/visual_inputs.json`
- Statistical review: `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/statistical/VISUAL_REVIEW.json`
- Statistical identity map: `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/statistical/review_identity_map.json`
- Medical manifest: `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/medical/visual_inputs.json`
- Medical review: `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/medical/VISUAL_REVIEW.json`
- Medical identity map: `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/medical/review_identity_map.json`

The Terra-visible manifests used anonymous item IDs only. The true candidate
and reference identities are present only in the internal identity maps.

## Statistical Estimator/Equation Case

Review identity: `d97821e39442db72ad90d3855a1f9fc514f9e9e7ddfe62517a7aeb2f560df1c8`

Overall Terra status: `PASS` as an assessable comparative evidence package.

Decoded item map:

| Anonymous item | True identity | Class | Terra item decision | Decoded finding |
| --- | --- | --- | --- | --- |
| `item_A` | `RRL-014` | inspected reference | `REVISE` | Equation readable, but image/mask integration and composition looked unfinished. |
| `item_B` | `statistical_estimator_cluster_robust_variance__alternative_composition` | generated candidate | `REVISE` | Clear topic, but equation contrast was poor and layout was top-heavy. |
| `item_C` | `statistical_estimator_cluster_robust_variance__reference_faithful` | generated candidate | `REVISE` | Best composed generated variant, but equation contrast and direct annotation were insufficient. |
| `item_D` | `statistical_estimator_cluster_robust_variance__controlled_wildcard` | generated candidate | `REVISE` | More balanced than `item_B`, but the estimator remained visually inaccessible. |
| `item_E` | `RRL-028` | inspected reference | `PASS` | Mature, projection-ready equation slide with crisp math and coherent hierarchy. |

Terra's comparative note ranked `item_E` as clearly strongest and the only item
that reached mature talk quality. Among generated candidates, `item_C` led, but
all three generated estimator variants remained below the mature bar because
the equation was not legible enough and annotations did not directly integrate
with the mathematical object.

## Medical Image Comparison Case

Review identity: `8f3aa043d534335b7d9c2342717c0f1b193c448e4585cf16578c056eff03a445`

Overall Terra status: `PASS` as an assessable comparative evidence package.

Decoded item map:

| Anonymous item | True identity | Class | Terra item decision | Decoded finding |
| --- | --- | --- | --- | --- |
| `item_A` | `RRL-013` | inspected reference | `REVISE` | Real image-led gallery, but legend and panel correspondence were weak. |
| `item_B` | `medical_image_lesion_overlay_comparison__controlled_wildcard` | generated candidate | `REVISE` | Clear text treatment, but the image comparison was too small and underdeveloped. |
| `item_C` | `RRL-022` | inspected reference | `REVISE` | Strong underlying image-to-image comparison, but crop failure and markup made it rough. |
| `item_D` | `medical_image_lesion_overlay_comparison__reference_faithful` | generated candidate | `REVISE` | Strongest layout and hierarchy, but synthetic fixture-like imagery kept it below mature quality. |
| `item_E` | `medical_image_lesion_overlay_comparison__alternative_composition` | generated candidate | `REVISE` | Focused failure-mode explanation, but sparse, synthetic, and not fully balanced. |

Terra's comparative note ranked `item_D` strongest for balanced comparison
structure and projection readability, with `item_E` second. It explicitly found
that no anonymous item reached mature research-group-meeting or strong
conference-talk quality in this medical case.

## Planner-Relevant Facts

- The comparative review pipeline can now materialize inspected reference
  pixels and generated candidate pixels into the same anonymous Terra package.
- The Terra-visible package avoids RRL/SRC IDs, author/institution labels,
  candidate strategy names, item classes, and generated/reference/gold/baseline
  labels.
- For the statistical equation case, the mature reference outperformed every
  generated candidate; the generated variants still need better formula
  contrast, scale, and direct mathematical annotation.
- For the medical image case, generated candidates improved layout relative to
  some rough references, but Terra still judged all items below the mature bar,
  mainly because the generated image evidence remained synthetic/demo-like.
- These findings should inform future Planner tasks, but they do not by
  themselves authorize a Presentation Program PASS.
