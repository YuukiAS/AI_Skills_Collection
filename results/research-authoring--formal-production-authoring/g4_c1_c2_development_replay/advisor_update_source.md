# CARE sequence modeling: evidence and next experiment

The compact temporal model outperformed the non-temporal baseline in the completed clean subject-disjoint replication. The immediate decision is whether to spend next week expanding robustness checks or testing personalization. **The recommendation for discussion is to prioritize robustness checks:** the advantage persisted in the reported shifted cohort, while the personalization result remains a single-seed pilot.

## Evidence from the current comparison

The replication used the current preprocessing contract and a clean subject-disjoint split. Table 1 summarizes the supplied results; higher macro-F1 and recall are better.

**Table 1. Reported performance and uncertainty.** The main comparison is temporal versus non-temporal modeling. The personalization pilot measures short-sequence recall and is a separate comparison.

| Evaluation | Metric and comparison | Reported result | Evidence boundary |
| --- | --- | --- | --- |
| Clean subject-disjoint replication | Macro-F1: compact temporal model vs non-temporal baseline | 0.714 vs 0.671; difference +0.043 | Paired bootstrap 95% confidence interval for the difference: [0.018, 0.071] |
| Pattern H, shifted cohort | Temporal-model advantage | Model remained ahead; reported interval [0.004, 0.049] | Point estimates, interval method, and confidence level were not specified for this condition |
| Personalization pilot | Short-sequence recall, before vs after personalization | 0.46 to 0.51 | One seed; preliminary; uncertainty not reported |

The positive interval for the main difference supports an advantage under the evaluated replication conditions. Pattern H retained that direction, with a narrower reported interval whose lower bound was closer to zero. These observations support further testing of the temporal comparison; they do not establish broad robustness across cohorts.

Error inspection placed most residual mistakes in sequences with fewer than four observations. This identifies a useful subgroup for follow-up, but error counts and subgroup denominators were not supplied, so the finding does not establish a higher error rate for short sequences. The pilot suggests personalization may improve recall in this subgroup; one seed cannot establish a reproducible benefit.

## Decision for next week

Prioritizing expanded robustness checks would address whether the temporal advantage persists beyond the reported conditions under a clean subject-disjoint evaluation. Short sequences deserve explicit attention because they account for most residual mistakes in the supplied inspection. Persistence of the advantage would strengthen the case for making personalization the next focus; an inconsistent advantage would make the underlying comparison the more immediate uncertainty.

A personalization ablation remains a reasonable alternative if the advisor prioritizes short-sequence recall. Its central question would be whether the pilot improvement repeats under a controlled comparison. The notes do not specify the personalization protocol or establish that the pilot followed the clean evaluation contract. Those details and the replication design need agreement before interpreting an ablation as confirmatory. These are proposed priorities, not completed or approved experiments.

The available notes omit sample sizes, full preprocessing details, bootstrap resampling details, and the definition of Pattern H. The update therefore summarizes reported evidence rather than an independently verified analysis. It supports neither clinical validity nor deployability.

**Advisor decision requested:** prioritize expanded robustness checks next week, or select a personalization ablation to test the preliminary short-sequence recall improvement?
