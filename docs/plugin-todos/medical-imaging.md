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

### Hard-case lifecycle and mature-component reuse

status: BLOCKED_NEEDS_EVIDENCE
source: user direction from planned CardiacNexus restructuring, 2026-09-22
problem: medical-imaging workflows need a first-class hard-case loop, not only aggregate metrics. Difficult cases should be discoverable, visually inspectable, and analyzable with enough provenance to explain whether the failure comes from image quality, anatomy, acquisition/domain shift, preprocessing/geometry, labels/reference standard, registration, model behavior, or evaluation. At the same time, project refactors should prefer mature ANTs/MONAI and adjacent ecosystem components over reimplementing lower-quality local substitutes.

candidate action:
- Define a reusable hard-case lifecycle covering discovery -> case retrieval -> visualization -> structured analysis -> failure attribution -> repair/experiment handoff.
- Support hard-case discovery from complementary evidence rather than one score only: worst-case task metrics, surface/landmark errors, component failures, calibration/uncertainty, scanner/site/protocol subgroups, temporal inconsistency, registration plausibility, and domain-specific measurement outliers where applicable.
- Make visualization part of the evidence contract: image/label/prediction overlays, contours, difference/error maps, relevant slices or 3D/temporal views, and case metadata needed for scientific interpretation. Visualization must preserve modality, orientation, physical-space geometry, label meaning, and patient/case identity boundaries.
- Require structured analysis that distinguishes data/acquisition, geometry/preprocessing, annotation/reference-standard, model, registration, evaluation, and domain-shift causes instead of treating every hard case as a model-architecture problem.
- Before implementing common medical-imaging mechanics locally, inspect mature components first. In particular, prefer ANTs/ANTsPy for established registration/transform operations and MONAI for medical-imaging transforms, readers/writers, inferers, metrics, post-processing, caching/data pipelines, and other supported primitives when they fit the task. Also compare adjacent mature implementations such as SimpleITK, nnU-Net, TorchIO, or highdicom when they are the better owner.
- Record reuse decisions as dependency/adapter/selected-port/reference-only/rejected with source, version, license, exact consumed component, adapter boundary, and why local implementation is still necessary when mature components are not used.
- Do not copy mature-library behavior into a local helper merely to reduce imports or make a benchmark pass. Local implementation is justified only when the project has a real semantic or integration gap and the replacement remains testable against the mature baseline.
- Use CardiacNexus restructuring as a real-workflow evidence source and incubator for this candidate. Keep CardiacNexus-specific architecture, dataset conventions, and one-off hard cases project-local; promote only repeated, generalizable mechanisms that survive domain review and are useful outside that repository.

review requirement: validate the loop on real CardiacNexus or another real imaging workflow with actual images, labels/predictions, geometry, case-level evidence, and mature-library reuse decisions. Toy tensors, synthetic hard cases, import checks, or screenshots without case provenance are insufficient.
promotion gate: at least one real hard-case workflow must improve failure discovery or attribution, and at least one mature-component reuse decision must demonstrably replace or prevent unnecessary local reimplementation without changing imaging semantics.

No production change is currently frozen from this candidate.

## Promotion notes

- Wrong modality/anatomy/label/metric semantics are severe production failures and may justify single-project promotion.
- Project-specific model architecture or dataset handling remains project-local unless independently repeated.
- Do not turn presentation image-layout feedback into medical-imaging workflow rules.
- CardiacNexus may incubate generic medical-imaging rules, but project-specific behavior must not be promoted solely because it appears during one refactor.
