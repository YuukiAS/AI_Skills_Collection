# Test-time percentile clipping for lesion segmentation: a preliminary internal validation study

## Abstract

This study examines test-time percentile clipping before an existing three-dimensional U-Net lesion-segmentation inference pipeline. The preliminary evaluation uses one internal validation split containing 18 volumes. Reported small-lesion Dice values suggest an increase from 0.421 to 0.469, while mean Dice changes from 0.742 to 0.758. HD95 changes from 18.4 to 17.9 mm. These aggregate values have not been independently verified against case-level outputs, and uncertainty estimates are unavailable. A motion-corrupted scan remains a failure case after clipping. The results therefore suggest a possible improvement in segmentation metrics on this split, while leaving the consistency of that improvement and its applicability to other imaging conditions unresolved. They motivate further evaluation of the preprocessing step but do not establish broad robustness.

## Introduction

The question addressed here is whether adding percentile clipping at test time may improve the outputs of an existing lesion-segmentation pipeline. The intervention is placed before three-dimensional (3D) U-Net inference. This preliminary study focuses on the numerical comparison available for one internal validation split, with particular attention to the reported small-lesion Dice score.

The evaluation considers small-lesion Dice, mean Dice, and HD95, alongside a recorded failure on a motion-corrupted scan. Its purpose is to describe the available evidence for this preprocessing change and define the limits of its interpretation. No claim of methodological novelty or superiority over other segmentation approaches is made.

## Methods

### Study scope

The evaluation uses one internal validation split comprising 18 volumes. The imaging modality, lesion type, acquisition characteristics, inclusion criteria, and reference-annotation procedure have not been specified. The number of unique participants and the number of lesions are also unavailable; the volume count should not be interpreted as either quantity. No external validation results are supplied.

### Inference pipeline and intervention

The comparison concerns an existing 3D U-Net inference pipeline and a configuration that adds test-time percentile clipping before that pipeline. The clipping percentiles, the spatial scope used to estimate them, treatment of background voxels, and the order of clipping relative to other intensity processing remain to be documented. The available description does not establish the model checkpoint, training protocol, inference settings, or whether all other pipeline settings were identical between the compared configurations. These details are needed to reproduce the comparison and isolate the contribution of clipping.

### Evaluation and reporting

The available outcomes are small-lesion Dice, mean Dice, and HD95 in millimetres. The definition of a small lesion, the aggregation units and weighting for the Dice scores, and the HD95 implementation and aggregation procedure are not supplied. Table 1 retains the metric labels used in the study notes pending confirmation of those definitions.

This manuscript reports the supplied aggregate values descriptively. Absolute changes are calculated as the value with clipping minus the value for the existing pipeline, using the reported precision. Case-level measurements, uncertainty estimates, and statistical test results are unavailable. No inferential analysis is introduced, and numerical changes are not interpreted as evidence of statistical significance.

## Results

The preliminary comparison suggests higher Dice values with clipping on the internal validation split (Table 1). Small-lesion Dice changes from 0.421 to 0.469, an absolute difference of 0.048, and mean Dice changes from 0.742 to 0.758, a difference of 0.016. HD95 changes from 18.4 to 17.9 mm, a difference of −0.5 mm. These differences summarize the supplied rounded values and do not establish the distribution of effects across volumes or lesions.

**Table 1. Preliminary segmentation metrics on one internal validation split of 18 volumes.** Values are reported for the existing pipeline and the configuration with test-time percentile clipping. Change is the clipping value minus the existing-pipeline value; Dice differences are absolute score differences, not relative percentages. Metric definitions, aggregation procedures, and small-lesion subgroup counts require confirmation. No uncertainty estimates are available.

| Metric | Existing pipeline | With clipping | Absolute change |
|:---|---:|---:|---:|
| Small-lesion Dice | 0.421 | 0.469 | +0.048 |
| Mean Dice | 0.742 | 0.758 | +0.016 |
| HD95 (mm) | 18.4 | 17.9 | −0.5 |

The motion-corrupted scan remains a failure case after clipping. No case-specific metric or image is available to characterize that failure further. The aggregate comparison therefore does not establish successful segmentation under motion corruption.

## Discussion

The reported values are consistent with a possible benefit of test-time percentile clipping in this internal split. The absolute change in small-lesion Dice is larger than the change in mean Dice, but the two summaries cannot establish a preferential benefit for small lesions without their definitions, denominators, and case-level measurements. The HD95 change provides an additional descriptive outcome; its practical meaning depends on the evaluation implementation and imaging context.

The persistent motion-corruption failure limits the interpretation of the intervention as a robustness measure. A change in aggregate scores can coexist with an unresolved failure under a particular imaging condition. The present evidence does not identify a mechanism for the numerical changes or show which cases contribute to them.

A reproducible account of the clipping configuration and the comparison protocol is needed to evaluate this finding. Case-level results would help assess whether the aggregate change reflects broadly consistent improvements or a smaller set of cases. Further evaluation beyond this internal split would be needed before extending the conclusion to other data or acquisition conditions. These are requirements for stronger claims, not experiments reported in this study.

## Limitations

The study is preliminary and restricted to one internal validation split of 18 volumes. The available evidence contains aggregate values rather than case-level outputs, preventing assessment of variability, paired changes, or the concentration of errors. The tentative Dice improvements have not been independently verified against the underlying evaluation records.

Incomplete documentation of the data, reference annotations, clipping settings, model configuration, and metric definitions limits reproducibility and interpretation. The role of the validation split in selecting clipping thresholds is unknown, so selection-related optimism cannot be assessed. No external evaluation or systematic corruption analysis is available, and the motion-corrupted scan remains a failure. The findings support neither a general robustness claim nor a conclusion about clinical utility.

## Conclusion

Test-time percentile clipping is associated with tentative increases in reported small-lesion and mean Dice and a lower reported HD95 on one internal validation split. The unresolved motion-corruption failure and incomplete protocol and uncertainty information constrain this observation to a preliminary, split-specific comparison.

## Declarations

Author names, affiliations, contributions, funding, competing interests, and any applicable ethics approval and consent information are pending author confirmation. Data and code availability have not been specified; no public release or access arrangement is asserted.

## References

Citation support is pending. No external references were supplied or added. Verified methodological references and relevant prior work must be incorporated before submission; this paragraph is a placeholder, not a bibliography.
