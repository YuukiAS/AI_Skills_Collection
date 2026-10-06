# CARE sequence modeling: evidence and next experiment

The immediate decision is whether to prioritize a personalization ablation or expand robustness checks next week. The current evidence favors testing whether the preliminary personalization gain is reproducible: the temporal model leads under both reported evaluation conditions, while short sequences remain the main observed error concentration. This is a recommendation for advisor consideration, not an established benefit of personalization.

## Evidence supporting the decision

A clean subject-disjoint replication finished under the current preprocessing contract, comparing a compact temporal model with a non-temporal baseline. Table 1 summarizes the reported evidence; higher macro-F1 and recall are better.

**Table 1. Reported model comparisons and the short-sequence pilot.** Differences in macro-F1 are temporal minus non-temporal. The pilot measures a different endpoint and should be interpreted separately.

| Evaluation | Reported result | Uncertainty and scope |
| --- | --- | --- |
| Clean subject-disjoint replication | Macro-F1: temporal 0.714; non-temporal 0.671; difference +0.043 (calculated from reported scores) | Paired bootstrap 95% confidence interval for the difference: [0.018, 0.071] |
| Pattern H robustness, shifted cohort | Temporal model remained ahead | Reported interval: [0.004, 0.049]; individual scores, interval method, and confidence level were not specified in the notes |
| Pilot personalization | Short-sequence recall increased from 0.46 to 0.51 | One seed; preliminary; no uncertainty interval reported |

Both reported difference intervals lie above zero. The Pattern H interval is narrower and closer to zero, so that result supports a positive advantage in the tested shifted cohort without establishing broad robustness. The notes do not provide its point estimate; the interval alone does not establish a measured reduction in effect size.

Error inspection found most residual mistakes in sequences with fewer than four observations. This identifies a useful target for follow-up, although the notes provide neither subgroup counts nor error rates by sequence length. The personalization pilot suggests a possible recall gain in this target group; a single seed cannot establish its repeatability, and a recall gain does not establish a macro-F1 gain.

## Proposed priority and evidence needed

Prioritize a controlled personalization ablation to ask whether the short-sequence recall improvement recurs under the clean subject-disjoint evaluation. Before execution, the experiment owner should specify the personalization comparison and permitted adaptation data, preserve the split and preprocessing contract, and define replication and uncertainty assessment. These are proposed requirements, not completed experiments or a frozen statistical protocol.

The decision-relevant outcome is repeatable short-sequence improvement alongside the overall macro-F1 comparison. If the pilot gain does not recur, it would not justify prioritizing personalization on the present evidence. Expanding robustness checks remains the alternative if the advisor considers uncertainty under cohort shift the more urgent question; one Pattern H check does not resolve that uncertainty.

The notes do not include sample sizes, seed counts for the main comparisons, preprocessing details, or a definition of Pattern H. Conclusions therefore remain bounded to the reported comparisons. No claim of clinical validity or deployability is supported.

**Advisor decision requested:** prioritize the personalization ablation next week, or place expanded robustness checks first?

*Evidence basis: supplied CARE development notes; no external literature or independently inspected experiment outputs were used.*
