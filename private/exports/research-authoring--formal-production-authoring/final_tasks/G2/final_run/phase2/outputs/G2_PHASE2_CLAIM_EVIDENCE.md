# G2 Phase 2 claim–evidence map

## Authority and inherited anchors

The supplied frozen `inputs/04-G2_PHASE1_PASS_BASELINE.md` is the accepted Phase 1 authority. Its SHA-256 is `ce7914b594d9723d9563fcaf26e1528913858c5eaf63475075ec354acdfc7139`. The original Phase 1 raw files and original claim map are not part of this input package. C1–C11 below preserve the accepted claims and anchor names; they do not represent a new independent verification of those raw files. D1–D4 are the only newly introduced scientific evidence.

| Anchor | Accepted baseline locator (paragraph opening or object) | Change status and claim |
|---|---|---|
| C1 | Subject-disjoint evaluation is necessary | Clean subject-disjoint design, changed checkpoint, and unavailable subject memberships; unchanged. |
| C2 | The scientific target is measurement fidelity; The comparisons address different explanations | Primary endpoint, comparator roles, matched original budget, and physical volume convention; unchanged. |
| C3 | Table 1; FedAvg has higher mean error | Historical CARE shared/local and own/off-site comparisons and Pattern H interpretation; unchanged. |
| C4 | Table 1; The reported intervals most consistently | Historical Table 1 estimates and primary paired uncertainty; unchanged. |
| C5 | The reported intervals most consistently | Historical own/off-site interval consistency and pooled/local uncertainty; unchanged. |
| C6 | Supporting endpoints show an own-site advantage | Historical supporting endpoint results and sample-size differences; unchanged. |
| C7 | The robustness summary reports | Robustness direction counts and missing subgroup detail; unchanged. |
| C8 | These comparisons narrow; Precision is particularly limited | Mechanism ambiguity, small centers, patient independence, clinical and transfer limits; retained. |
| C9 | M&Ms asks a related question | M&Ms design and measurement roles; unchanged. |
| C10 | The supplied M&Ms decision | M&Ms decision-level evidence and limits; unchanged; no personalization result added. |
| C11 | The next discriminating question; A useful test would compare | Phase 1 prospective personalization question; historical uncertainty retained explicitly, current decision updated with D1–D4. |

## New delta anchors and exact selectors

All four files originate from `YuukiAS/Distributed_Imaging_Inference` at `c6ed0fb40c702936ec1f41454390ef188a5b4d97`, under `results/care_personalized_partial_pooling_2026-09-04/`. Local filenames have input-package prefixes; the manifest retains canonical identities.

| Anchor | Local evidence | Fields / row selector | Newly supported claim and boundary |
|---|---|---|---|
| D1 | `inputs/05-experiment_contract.json` | `D_adapt_subjects`, `D_test_subjects`, site counts, `seeds`, `fedavg_anchor_epochs`, `personalization_epochs`, `primary_scope`, `secondary_local_components`, `lambda_grid`, test and lambda selection policies, `decision_rules` | 88/45 subjects, seven centers, three seeds, four anchor epochs plus two personalization epochs; no test-set selection by contract. Policy is not independently audited subject membership. Additional training is a design caveat, not a demonstrated cause. |
| D2 | `inputs/06-personalization_gate_decision.json` | `global_comparison`, `historical_clean_fedavg_exact_reload_available`, `D_test_used_for_hyperparameter_selection`, `decision_labels`, `simple_delta_global_by_seed`, `simple_gap_closure_by_seed`, `finite_lambda_rows`, `lowdim_candidates`, `reasons` | Decision reports `P-SIMPLE`, `P-SHRINK`, `P-LOWDIM`; same-run reference, historical exact reload unavailable. Lower storage is a source-reported judgment with no size measurements supplied. |
| D3 | `inputs/07-gap_closure_summary.csv` | All 18 rows; key `(method, scope, seed, lambda, metric)`; closure mean/bounds, subject count and error-mean columns | Table 2 closure column is an unweighted mean of three seed values, not a newly pooled patient estimate. Counts 27/30/29 and broad intervals qualify closure. No unprovided formula or subset aggregation rule is asserted. |
| D4 | `inputs/08-paired_bootstrap_ci.csv` | 324 rows parsed; primary claims use 36 rows with `metric=scar_fraction_abs_error`, both `Delta_global_personalized_minus_same_run_FedAvg_anchor` and `Delta_local_personalized_minus_local_site_model`; key also includes method, scope, seed, lambda | All 18 primary global intervals below zero. Full LocalFT: all three local intervals include zero. Last-stage: all three local intervals above zero. λ=0.0001, seed 20260830: local estimate 0.0112975423, interval [0.0026374941, 0.0201199943]. No coverage level or resampling unit inferred. |

## Dependency closure and numerical checks

- **Changed summary:** replaces the untested-remedy status with evidence of improvement versus the same-run anchor, retaining uncertainty about local-only value and center transfer (C11 → D1–D4).
- **Changed final section:** preserves its heading and hypothesis history; adds the follow-up design, Table 2, conditional decision interpretation, uncertainty and narrowed next question.
- **Unchanged Table 1:** historical comparisons use a different reference; no subtraction or replacement using new absolute-error means.
- **New Table 2:** groups `(FedAvg_then_LocalFT, full-model, 0.0)`, `(FedAvg_then_LocalDecoder, decoder, 0.0)`, `(FedAvg_then_LocalLastDecoderStage, last-decoder-stage, 0.0)`, and `(FedAvg_then_ProxLocalFT, full-model, λ)` for all three finite λ values. Range = min/max of D4 seed estimates; interval count = number with `ci_high < 0`; closure = arithmetic mean from D3, all rounded to four decimals.
- Decoder mean closure / full LocalFT mean closure is about 1.0362; it exceeds the contract's 70% threshold. This is a descriptive ratio without a paired uncertainty estimate or verified storage count.
- λ=0.001 mean closure exceeds λ=0 mean closure descriptively; no direct method-versus-method paired test is supplied. The closure intervals at λ=0.001 are all positive, but this does not select a test-set winner.
- Three full LocalFT closure intervals are copied from D3 and rounded, not converted to nominal 95% intervals. Closure and paired-error summaries have incompletely specified aggregation relations and remain separate.
- **Retained limitations:** small-center precision, seeds not adding patients, causal ambiguity, clinical tolerance, unseen-center transfer, and M&Ms evidence limits. The delta supplies no center-level personalization estimates or M&Ms personalization results.
- **Next question:** an author interpretation grounded in those limitations, not a frozen new experiment contract or an observed result.
