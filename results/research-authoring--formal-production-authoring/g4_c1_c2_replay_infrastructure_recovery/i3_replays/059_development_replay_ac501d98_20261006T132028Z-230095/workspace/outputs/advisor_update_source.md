# CARE sequence modeling: next experiment priority

The next-week decision is whether to prioritize a personalization ablation or expand robustness checks under a clean subject-disjoint split. **Recommendation for advisor consideration: prioritize the personalization ablation.** The temporal comparison is positive in the reported replication and shifted-cohort check, while error inspection identifies short sequences as a concrete target. The pilot motivates this test but does not establish a reproducible personalization benefit.

## Evidence and its scope

The clean subject-disjoint replication completed under the current preprocessing contract, comparing a compact temporal model with a non-temporal baseline. Table 1 summarizes the supplied results; higher macro-F1 and recall indicate better performance.

**Table 1. Reported CARE comparisons.** Differences are temporal minus non-temporal for macro-F1. The personalization row uses short-sequence recall, a separate endpoint.

| Evaluation | Reported result | Evidence boundary |
| --- | --- | --- |
| Clean subject-disjoint replication | Temporal macro-F1: 0.714; non-temporal: 0.671; difference: +0.043 | Paired bootstrap 95% confidence interval for the difference: [0.018, 0.071] |
| Pattern H robustness, shifted cohort | Temporal model remained ahead; reported interval: [0.004, 0.049] | Absolute scores and point difference were not supplied; interval method and confidence level were not separately specified |
| Pilot personalization | Short-sequence recall: 0.46 → 0.51 | One seed; preliminary; no uncertainty interval supplied |

The replication supports a temporal advantage in the reported setting. Pattern H preserves the direction, with a narrower interval whose lower endpoint lies closer to zero. These observations do not establish robustness across other shifts. Error inspection found most residual mistakes in sequences with fewer than four observations; without subgroup counts, this does not establish a higher error rate for that subgroup.

The personalization pilot suggests a possible way to address this error concentration. Its single-seed recall increase does not establish reproducibility or an improvement in overall macro-F1. The notes do not specify whether the pilot used the same split and preprocessing contract. Sample sizes, the bootstrap resampling unit, and the definition of Pattern H are also unavailable. The evidence supports neither clinical validity nor deployability.

## Proposed next experiment and advisor decision

The proposed ablation asks whether personalization reproducibly improves recall for sequences with fewer than four observations while preserving overall macro-F1. Compare personalization enabled versus disabled under the same clean subject-disjoint split and preprocessing contract, repeat across seeds, and report short-sequence recall alongside overall macro-F1 and uncertainty. The experiment owner should specify the personalization protocol, available adaptation data, repeat budget, and uncertainty procedure before execution; these are proposals, not completed work.

A reproducible short-sequence gain without deterioration in overall macro-F1 would support further personalization work. If the gain fails to repeat or introduces an overall trade-off, reconsider its priority. Expanded shifted-cohort checks remain the alternative if the advisor's immediate priority is establishing how stable the temporal advantage is under shift.

**Decision requested:** allocate next week to the controlled personalization ablation, or prioritize expanded robustness checks if uncertainty under cohort shift is the more urgent research question.

*Evidence source: supplied CARE development notes. No external literature or additional experimental results were used.*
