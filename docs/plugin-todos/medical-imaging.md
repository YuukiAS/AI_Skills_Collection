# medical-imaging — Long-Term TODO

Canonical maintenance inbox for the `medical-imaging` plugin.

## Open candidates

### Curriculum-driven capability refinement

status: BLOCKED_NEEDS_EVIDENCE
source: user-approved design direction, 2026-09-01
proposal: Use standards, consensus/guideline documents, official tool documentation, mature implementations, landmark papers, and selected textbooks as the main learning sources. Textbooks are supporting material rather than the default production source of truth. See `docs/workflows/CURRICULUM_DRIVEN_DOMAIN_PLUGIN_REFINEMENT.md`.
review requirement: validate modality/task semantics, physical-space geometry, labels, metrics, patient/case structure, and reproducibility on real or realistic imaging artifacts. Toy tensors and import tests are not sufficient.
promotion gate: a bounded competency must improve a real imaging workflow without replacing current standards or mature implementations with a lower-quality local reconstruction.

No production change is currently frozen from this candidate.

Future items should come from real imaging workflows and preserve modality/task semantics, label meaning, patient/case structure, metric semantics and reproducibility. Presentation-specific use of medical images belongs to `presentations`; imaging scientific correctness belongs here.

## Promotion notes

- Wrong modality/anatomy/label/metric semantics are severe production failures and may justify single-project promotion.
- Project-specific model architecture or dataset handling remains project-local unless independently repeated.
- Do not turn presentation image-layout feedback into medical-imaging workflow rules.
