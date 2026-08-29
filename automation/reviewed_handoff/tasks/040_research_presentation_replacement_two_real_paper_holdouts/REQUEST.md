# Request — 040_research_presentation_replacement_two_real_paper_holdouts

Stage 5 needs a clean replacement unseen evaluation after 038 failed and 039 repaired the generic quality-loop execution gap. This task must evaluate the frozen normal `research-presentations` production path on two **new** real public papers without using 038's brms/MedSAM papers as tuning material or evaluation inputs.

The two Planner-selected candidates are:

1. statistics / methodology: Kristensen, Nielsen, Berg, Skaug & Bell (2016), **TMB: Automatic Differentiation and Laplace Approximation**, Journal of Statistical Software, DOI `10.18637/jss.v070.i05`;
2. medical imaging: Ferreira, Lau, Salaymang & Arnaout (2025), **Self-supervised learning for label-free segmentation in cardiac ultrasound**, Nature Communications, DOI `10.1038/s41467-025-59451-5`.

Planner pre-search of tracked repository content found no exact title or DOI hit for either candidate. The Executor must still perform the full pre-render reference/gold/corpus/tuning exclusion audit required by the Program Goal before either paper is acquired into the holdout bundle. If a real prior tuning use is discovered, stop that paper before first render and return to Planner; do not silently substitute another paper.

Both sources are publicly accessible with reuse-friendly article licensing: Journal of Statistical Software applies Creative Commons Attribution licensing to its articles, and the Nature Communications paper is explicitly CC BY 4.0 with article images included unless separately credited. Executor must record the exact source/version/license and inspect figure-level credit lines before reuse.

This is evaluation-only. The production generator, gold library, layout emitters, storyline rules, validators, quality-loop mapping and shared/plugin behavior are frozen. Each paper gets one normal production invocation from a source bundle frozen and hashed before first render, plus at most the already-shipped single bounded automatic quality repair if fresh structured visual evidence triggers it. No manual slide repair, paper-specific branch, source-bundle rewrite after seeing output, second repair, or holdout-derived rule/gold change is allowed.

Success requires two complete, source-faithful exact-CUHK paper-talk decks, fresh item/page-level and contact-sheet visual evidence for each, real CI, and independent Planner review. If both pass Terra and Planner, the Program must stop at the final user acceptance gate; only the user's explicit acceptance may close `ONE_SHOT_QUALITY_PASS`.