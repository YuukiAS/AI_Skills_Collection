---
name: medical-imaging-deep-learning
description: Use for medical-imaging deep learning tasks involving segmentation, MONAI/nnU-Net baselines, registration or warping, temporal/video imaging, missing-modality fusion, proposal/cascade/refinement models, external method adaptation, and validation evidence gates.
status: active
provenance: unknown
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-03
profile_tags:
recommended_scope: project
license: Apache-2.0
metadata:
  skill-author: AI Skills Collection maintainers
allowed-tools:
---
# Medical imaging deep learning

## Overview

This skill encodes a general **medical-imaging deep learning evidence standard**:

- **Custom research pipelines / transforms / deployment-oriented code paths → MONAI** (PyTorch-first infrastructure).
- **New segmentation task → nnU-Net as the default strong benchmark** before claiming gains from custom architectures.
- **Foundation / promptable segmentation → MedSAM** when the problem matches prompt-based or zero-shot adaptation—**not** as a substitute for validation.
- **Learning-based deformable registration → VoxelMorph** as the primary **deep** anchor, **always** paired with **classical** registration (ANTs/SyN, **elastix**, etc.) for evidence—not optional.
- **Mechanism claims → explicit completion gates** before reporting a model as done.

**High-visibility** here means **widely adopted benchmarks and seminal baselines** (qualitative); do **not** invent citation counts.

Full anchors: [references/reference.md](references/reference.md).

## Workflow inheritance

For complex tasks, first apply the global `codex-workflow-protocol` skill. This skill only adds domain-specific knowledge, gates, and validation requirements. It must not weaken the global completion, escalation, or verification rules.

## When to Use This Skill

Use when you:

- Design **segmentation**, **registration**, **template-building**, or **DL-side QC** for medical images.
- Choose between **MONAI**, **nnU-Net**, **MedSAM**, **VoxelMorph**, and **historical CNN baselines** (U-Net family).
- Define **train/val/test**, **external validation**, and **leakage-safe** splits.
- Compare against **public benchmarks** (MSD, BraTS, ACDC, KiTS, LiTS) when claiming generalization.

Avoid using this skill as a generic “list of cool models” checklist—**bind decisions to validation obligations**.

## Core Tooling / Preferred Stack

| Tool | Role | Default stance |
|------|------|-----------------------------|
| **MONAI** | Training/eval **infrastructure**: transforms, datasets, networks, bundles, deployment hooks | **First choice** for new code in a MONAI-first refactor |
| **nnU-Net** | Self-configuring **strong segmentation baseline** | **Run first** on a new segmentation task; **benchmark** before custom nets |
| **MedSAM** | **Foundation** / promptable segmentation | **After** positioning against classical CNN baselines + nnU-Net-class strong baselines; domain validation required |
| **VoxelMorph** | **Learning-based** pairwise registration | **Never** the only registration; **pair** with classical ANTs/SyN or elastix-style baselines |

## Domain evidence labels for model changes

Use these labels as medical-imaging domain evidence labels inside model-change reports. They do not replace the global final status vocabulary from `codex-workflow-protocol`.

Every final report must still use one global final status: `complete`, `partial_complete`, `qa_failed`, `blocked`, or `blocked_target_not_met`. When useful, add one domain evidence label to explain the model mechanism evidence stage.

- `TRUE_DONE`: the requested mechanism is implemented, trained or inferred as authorized, evaluated on the target split, and supported by checkpoint, prediction, metric, command/log, and same-split baseline evidence.
- `PARTIAL_MECHANISM_INCOMPLETE`: code or experiments exist, but a core mechanism is missing, proxy-only, or below the required gate.
- `PREFLIGHT_SMOKE_ONLY`: only import, shape, one-case, metadata, dryrun, readiness, or resource checks were completed.
- `NOT_DONE`: no implementation, no run, failed run, stale evidence, or missing evidence.

Examples:

- If only import, shape, one-case, metadata, dryrun, readiness, or resource checks were completed, the global final status should usually be `partial_complete` or `qa_failed`, with domain evidence label `PREFLIGHT_SMOKE_ONLY`.
- If code or experiments exist but the requested mechanism is missing, proxy-only, or below the required gate, the global final status should usually be `partial_complete` or `qa_failed`, with domain evidence label `PARTIAL_MECHANISM_INCOMPLETE`.
- If no implementation, no run, failed run, stale evidence, or missing evidence exists, the global final status should usually be `partial_complete`, `qa_failed`, or `blocked`, with domain evidence label `NOT_DONE`.
- If the requested mechanism is implemented, trained or inferred as authorized, evaluated on the target split, and supported by checkpoint, prediction, metric, command/log, and same-split baseline evidence, the global final status may be `complete`, with domain evidence label `TRUE_DONE`.

Do not promote a task above the weakest required evidence stage. If training/evaluation was not run, do not label the domain evidence stage as `TRUE_DONE`.

## Forbidden shallow substitutions

Never report these as completed mechanisms:

- Smoke, preflight, dryrun, import, shape, metadata, or one-case checks as model completion.
- A one-layer stem, shallow head, or 1x1 output head as a U-Net-like encoder-decoder.
- Translation, center crop, metadata copying, or resampling as completed registration or warping.
- A frame0, single-frame, or reference-only anatomy proxy as a temporal/video method.
- Logit mixing as a proposal, refinement, or cascade model.
- Hard-negative mining preflight as hard-negative training.
- Search, license notes, clone, import, or tensor-shape smoke as external-method integration.
- Local proxy metrics as challenge-grade or deployment-grade evidence without the target evaluator contract.
- Missing-modality samples as target hard negatives when the target label depends on that missing modality.

### Canonical architecture baselines (not “instead of nnU-Net”)

- **U-Net** (2D): historical canonical CNN segmentation baseline.  
- **3D U-Net**: volumetric canonical baseline.  
- **UNETR / Swin UNETR**: transformer-era **strong baselines** when the narrative involves **global context / transformers**—use to **situate** claims vs. MedSAM or custom attention architectures; **do not** imply they replace nnU-Net as the default segmentation benchmark.

### Benchmark datasets / challenges (named anchors)

Use as **evaluation anchors** and **literature positioning**, not as “mandatory dependencies”:

- **MSD** — multi-task / multi-modality generalization benchmark.  
- **BraTS** — brain tumor multimodal MRI segmentation.  
- **ACDC** — cardiac MRI multi-structure segmentation/diagnosis benchmark.  
- **KiTS19** / **LiTS** — kidney/liver tumor CT benchmarks.

## Workflow / Decision Rules

### Segmentation

1. **Establish geometry** once: consistent **spacing, orientation, affine, origin**; document resampling kernels.  
2. **Patient-level splits** only; no slice-level leakage across patients.  
3. **Default benchmark order:**  
   - **nnU-Net** strong baseline →  
   - optional **U-Net / 3D U-Net** historical baselines →  
   - **MONAI** custom method **only with** documented incremental value.  
4. If claiming **transformer / foundation** value: explicitly relate to **UNETR / Swin UNETR / MedSAM** lineages and justify **why** extra complexity is needed.

### Segmentation architecture gate

When a task asks for **U-Net-like**, **encoder-decoder**, **multiscale**, **cascade**, **proposal**, or **refinement** behavior, the result must list:

- key classes/functions changed;
- feature scales and decoder/skip/refinement paths;
- input/output tensor shapes;
- checkpoint, prediction, metric, and same-split baseline paths;
- ablation or comparison showing the mechanism changed behavior.

If these are absent, label the domain evidence stage as `PARTIAL_MECHANISM_INCOMPLETE` or `PREFLIGHT_SMOKE_ONLY`.

### Registration / template building

- **VoxelMorph** (or similar) **must** be reported against **ANTs/SyN** and/or **elastix**-class classical baselines on the **same** preprocessed images.  
- **Template building** is a **separate validated stage**: inverse consistency, Jacobian plausibility, and **downstream** checks (warped-mask overlap, strain biomarker bias if applicable).  
- Treat **deformation-dependent phenotypes** as **high-risk**—do not optimize **Dice alone**.

### Registration / warping gate

Every registration claim must state:

- transform family: rigid, affine, deformable, SyN, B-spline, TPS, optical flow, feature-level warp, or translation baseline;
- moving and fixed images/frames, image space, interpolation, and label interpolation;
- plausibility checks such as inverse/roundtrip consistency, Jacobian/folding, landmark error, warped-mask consistency, or visual overlays;
- downstream task metric on the same split.

Translation-only work is a **translation baseline**, not registration completion.

### Temporal / video imaging gate

For cine, video, 4D, longitudinal, or time-series imaging, report:

- reference frame or time point and why it was chosen;
- how non-reference frames are used;
- motion estimation, warping, temporal aggregation, or temporal consistency;
- whether the model has a head for the target clinical/anatomical task, not just an anatomy proxy;
- metrics against a single-frame/reference baseline.

Single-frame or reference-only evidence is a baseline/proxy, not temporal-method completion.

### Missing-modality gate

For multimodal models, report:

- modality availability per split/subgroup;
- availability mask, routing, imputation, or dropout behavior;
- loss masks for targets that depend on a modality;
- target-available subgroup metrics and target-missing subgroup caveats.

If a target label depends on a modality, samples missing that modality must not be treated as default hard negatives for that target.

### External method adapter gate

Separate stages clearly:

1. resource search and paper/code triage;
2. license/version/dependency check;
3. clone/import/shape smoke;
4. one-case adapter with input/output contract;
5. fold0 or full validation metric on the same evaluator;
6. rollback criteria and cleanup.

Only stage 5+ can be called an integrated method.

### DL-side QC

- **Failure review** on held-out cases (visual overlays, worst-case mining).  
- If using **uncertainty / calibration**: report **reliability** checks, not only AUC/Dice.  
- **DICOM** → tensor paths must preserve **consistency** with classical preprocessing (same orientation convention as SimpleITK/ANTsPy stack).

### When **not** to jump to foundation models / DL registration

- **Small, single-site** datasets with **weak labels** → foundation models **overfit narratives** easily; **nnU-Net + classical baselines** first.  
- **Regulatory or clinical** claims without external validation → **do not** lead with MedSAM.  
- **Registration** where **topology** must stay physiological → **classical** diffeomorphic/SyN-class methods often remain the **safer default**; learning methods need **Jacobian / folding** audits.

## Benchmark expectations / evaluation baselines

**Rules:**

1. **Segmentation:** **nnU-Net** is the default **modern strong benchmark**. **U-Net / 3D U-Net** are **historical canonical** baselines. Saying “we beat SOTA” **against a weak custom baseline** is invalid.  
2. **Transformers / foundation claims:** acknowledge **UNETR / Swin UNETR** and **MedSAM** as **relevant comparators** when scope overlaps.  
3. **Multi-organ / multi-task generalization:** cite **MSD** as the standard **generalization** anchor.  
4. **Brain / heart / kidney / liver** tumor or structure tasks: **BraTS / ACDC / KiTS / LiTS** are the **default named benchmarks** for positioning.  
5. **Metrics:** **Dice alone is insufficient** for high-stakes segmentation; add **surface / Hausdorff-class** metrics where applicable, **calibration** if probabilistic, **OOD/generalization** and **failure analysis** for real deployment narratives.  
6. **Registration:** **VoxelMorph** does **not** bypass **classical** registration; include **Jacobian / folding / topology** and **landmark or downstream** checks when available.

## Evidence standard for model changes

Every model-change result must include:

- command/log, exit status, job ID if applicable, and elapsed time;
- checkpoint path, prediction path, metric path, and config/cache isolation;
- same-split baseline and target evaluator contract;
- failure analysis with surface/HD, component, calibration, subgroup, or remote false-positive metrics when they matter.

Dice alone is insufficient when boundary accuracy, topology, lesion/component burden, calibration, or false positives drive the task.

## Common Pitfalls / Validation Notes

- **Leakage** via slice shuffling, repeated patients, or preprocessing computed on global stats.  
- **Mixing NIfTI/DICOM orientation fixes** across modalities without a single library boundary.  
- **Reporting only in-distribution Dice** with no **external** cohort.  
- **Template building** without reporting **smoothness / plausibility** of mean shape and transforms.  
- **Treating MedSAM** as “segmentation solved” without **domain fine-tuning** and **external** test.

## References

Canonical papers and benchmark anchors are maintained in [references/reference.md](references/reference.md).

Read [references/reference.md](references/reference.md) for detailed completion checklists and generic examples of shallow substitutions.
