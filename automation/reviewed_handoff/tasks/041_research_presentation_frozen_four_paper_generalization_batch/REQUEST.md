# Request — 041_research_presentation_frozen_four_paper_generalization_batch

Create the Planner-owned Stage 5 final acceptance task under the updated Program Goal: Frozen Batch Real-Paper Generalization Acceptance + Human Closure.

Planner must choose and freeze a complete batch of four real public unseen papers before any paper is acquired into a source bundle, rendered, inspected or evaluated:

1. two statistics / biostatistics / methodology papers;
2. two medical-imaging papers that can support real source-image use where scientifically needed.

The purpose is to test generalization of the already shipped normal `research-presentations` production entrypoint, not to tune the system on the holdouts.

040 never executed before being superseded. Its two proposed papers, TMB and self-supervised cardiac-ultrasound segmentation, were not generated or inspected by 040. Planner may decide whether either can be included in the new four-paper batch only after a fresh contamination audit confirms they are still unseen and suitable. If later evidence shows 040 or another task consumed either paper before 041 freezes the batch, that paper must be excluded.

The 038 brms and MedSAM papers are consumed failed holdouts and must not be reused as unseen papers. Failed holdout text, figures, title, DOI, page-specific content and rendered pixels must not be used as tuning fixtures.

Planner must write a `PLAN.md` that lists all four paper identities before `PLAN_FROZEN`. The plan must freeze the production system for the full batch and prohibit adaptive holdout chasing: no sequential replacement, no keeping only winners, no production/gold/layout/rule/prompt/validator/quality-loop changes between papers, and no post-failure paper substitution inside the same batch.

Acceptance requires a complete frozen four-paper batch with 4/4 source fidelity, normal production entry, item/page-level Terra PASS, contact-sheet mature doctoral-group-meeting PASS, independent Planner PASS and no holdout-specific hardcode. Any one paper failing makes the whole batch FAIL and consumes all four papers.

After a failed batch, generic recovery may happen only on independent non-holdout / synthetic / public-safe regression material. Before any next fresh holdout batch is consumed, the workflow must enter a human gate explaining the failure, the generic mechanism repaired and why another batch is worth spending.

Do not execute 041 in this task. This request only asks Scheduled GPT Planner to freeze the next valid batch plan.
