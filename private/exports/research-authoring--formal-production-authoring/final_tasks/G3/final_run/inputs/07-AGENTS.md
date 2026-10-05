# MoSAIC paper agent rules

This repository is the manuscript truth source for MoSAIC. It starts with facts, not prose.

- Do not draft Introduction, Method, Experiments, Discussion, or Abstract until `METHOD_TRUTH.md`, `RESULTS_TRUTH.md`, and `CLAIM_LEDGER.md` have been reviewed by the author.
- Use `/users/a/e/aereinh/MoSAIC/code/source` as source-code evidence. Current upstream commit: `d334bd1fb2a99dbbc230510590cd8e3ee08cc377`.
- Use `/users/a/e/aereinh/MoSAIC/code/weights` for checkpoint inventory only; never commit weights or prediction outputs.
- Preserve uncertainty. Do not upgrade preflight/model-load evidence into completed inference or completed fair comparison.
- Strong manuscript claims must appear in `CLAIM_LEDGER.md` with code evidence, experiment evidence, wording strength, and author-confirmation status.
- No training, validation upload, or fabricated citation is allowed from this repository.
