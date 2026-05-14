---
name: medical-imaging-deep-learning
description: Aligns with CardiacNexus MONAI-first refactor and high-risk registration/strain awareness.
status: active
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-05-14
profile_tags:
recommended_scope: project
license: Apache-2.0
metadata:
  skill-author: CardiacNexus maintainers
allowed-tools:
---
# Medical imaging deep learning

## Overview

This skill encodes a **project-consistent stack** for CardiacNexus-style work:

- **Custom research pipelines / transforms / deployment-oriented code paths → MONAI** (PyTorch-first infrastructure).
- **New segmentation task → nnU-Net as the default strong benchmark** before claiming gains from custom architectures.
- **Foundation / promptable segmentation → MedSAM** when the problem matches prompt-based or zero-shot adaptation—**not** as a substitute for validation.
- **Learning-based deformable registration → VoxelMorph** as the primary **deep** anchor, **always** paired with **classical** registration (ANTs/SyN, **elastix**, etc.) for evidence—not optional.

**High-visibility** here means **widely adopted benchmarks and seminal baselines** (qualitative); do **not** invent citation counts.

Full anchors: [references/reference.md](references/reference.md).

## When to Use This Skill

Use when you:

- Design **segmentation**, **registration**, **template-building**, or **DL-side QC** for medical images.
- Choose between **MONAI**, **nnU-Net**, **MedSAM**, **VoxelMorph**, and **historical CNN baselines** (U-Net family).
- Define **train/val/test**, **external validation**, and **leakage-safe** splits.
- Compare against **public benchmarks** (MSD, BraTS, ACDC, KiTS, LiTS) when claiming generalization.

Avoid using this skill as a generic “list of cool models” checklist—**bind decisions to validation obligations**.

## Core Tooling / Preferred Stack

| Tool | Role | CardiacNexus default stance |
|------|------|-----------------------------|
| **MONAI** | Training/eval **infrastructure**: transforms, datasets, networks, bundles, deployment hooks | **First choice** for new code in a MONAI-first refactor |
| **nnU-Net** | Self-configuring **strong segmentation baseline** | **Run first** on a new segmentation task; **benchmark** before custom nets |
| **MedSAM** | **Foundation** / promptable segmentation | **After** positioning against classical CNN baselines + nnU-Net-class strong baselines; domain validation required |
| **VoxelMorph** | **Learning-based** pairwise registration | **Never** the only registration; **pair** with classical ANTs/SyN or elastix-style baselines |

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

### Registration / template building

- **VoxelMorph** (or similar) **must** be reported against **ANTs/SyN** and/or **elastix**-class classical baselines on the **same** preprocessed images.  
- **Template building** is a **separate validated stage**: inverse consistency, Jacobian plausibility, and **downstream** checks (warped-mask overlap, strain biomarker bias if applicable).  
- **Strain / deformation-dependent phenotypes** (CardiacNexus): treat **registration** as **high-risk**—do not optimize **Dice alone**.

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

## Common Pitfalls / Validation Notes

- **Leakage** via slice shuffling, repeated patients, or preprocessing computed on global stats.  
- **Mixing NIfTI/DICOM orientation fixes** across modalities without a single library boundary.  
- **Reporting only in-distribution Dice** with no **external** cohort.  
- **Template building** without reporting **smoothness / plausibility** of mean shape and transforms.  
- **Treating MedSAM** as “segmentation solved” without **domain fine-tuning** and **external** test.

## References

Canonical papers and benchmark anchors are maintained in [references/reference.md](references/reference.md).
