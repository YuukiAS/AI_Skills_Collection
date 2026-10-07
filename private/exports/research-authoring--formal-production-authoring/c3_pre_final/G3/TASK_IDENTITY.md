# G3 Exact Real Manuscript Task

Gate: G3 正式 manuscript production package
Frozen by Planner: 2026-10-05

## Project identity

Repository: `YuukiAS/MoSAIC_Paper`
Frozen source ref: `590bfbac1450fbab5e4ca8ce77c877ece845f094`

Canonical manuscript source:
`submission/mosaic.tex`

The repository records a real production problem: baseline `submission/mosaic.pdf` is 14 pages while the frozen CARE 2026 project requirement allows an absolute maximum of 12 pages including references.

## Exact final task

Natural task:

> Prepare a clean, double-blind CARE 2026 submission package from the current author-approved MoSAIC manuscript truth. Bring the paper within the frozen venue page limit without inventing or strengthening claims, preserve the author-approved result boundary, keep the LNCS template unchanged, verify citations/figures/cross-references, and deliver a buildable submission source package plus final PDF and concise submission manifest. Do not submit to OpenReview.

This is a **read-only source-repo task**. The final Gate must not modify `YuukiAS/MoSAIC_Paper`. After pre-final Critic PASS, Executor materializes the frozen source subset into an AI_Skills task-local input workspace and writes all candidate outputs to the 059 private export.

## Freshness justification

The specific MoSAIC CARE page-limit/submission-package task, exact source ref, and exact manuscript truth files were not used to tune Research Authoring C0.

059 architecture/development work used DII/CAT-TRACE report/manuscript structure as design/regression evidence. Repository history shows older MoSAIC writing lessons influenced generic Clear Writing/fidelity work in July, but that does not make this **new exact Research Authoring manuscript-production task** a 059 tuning sample.

Targeted searches of 059 design/result material found no use of `PAPER_STATUS.md`, `RESULTS_TRUTH.md`, `METHOD_TRUTH.md`, `CLAIM_LEDGER.md`, or `submission/mosaic.tex` as a 059 product-tuning sample.

Pre-final Critic must independently accept this freshness claim. If direct evidence shows this exact task/output was used to tune C0, G3 remains blocked and no final run starts.
