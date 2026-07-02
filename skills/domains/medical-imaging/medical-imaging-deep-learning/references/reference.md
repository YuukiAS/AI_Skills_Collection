# References: Medical imaging deep learning

Sections below separate **implementation toolkits**, **canonical architecture baselines**, and **benchmark / dataset papers**. Challenge papers are **evaluation anchors**, not substitutes for software packages.

---

## Implementation toolkit (core)

### MONAI

- **MONAI: An open-source framework for deep learning in healthcare** — Cardoso et al., arXiv: [2211.02701](https://arxiv.org/abs/2211.02701)  
- Official docs: [https://docs.monai.io/](https://docs.monai.io/)

### nnU-Net

- **nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation** — *Nature Methods*, 2021. DOI: [10.1038/s41592-020-01008-z](https://doi.org/10.1038/s41592-020-01008-z)  
- Preprint: arXiv: [1809.10486](https://arxiv.org/abs/1809.10486)  
- **Validation note (rigorous evaluation):** `nnU-Net Revisited` — arXiv: [2404.09556](https://arxiv.org/abs/2404.09556)

### MedSAM

- **Segment Anything in Medical Images** — *Nature Communications*, 2024. DOI: [10.1038/s41467-024-44824-z](https://doi.org/10.1038/s41467-024-44824-z)  
- Preprint: arXiv: [2304.12306](https://arxiv.org/abs/2304.12306)

### VoxelMorph

- **VoxelMorph: A Learning Framework for Deformable Medical Image Registration** — *IEEE TMI*, 2019. DOI: [10.1109/TMI.2019.2897538](https://doi.org/10.1109/TMI.2019.2897538)  
- Preprint: arXiv: [1809.05231](https://arxiv.org/abs/1809.05231)  
- Code/project: [http://voxelmorph.csail.mit.edu/](http://voxelmorph.csail.mit.edu/)

---

## Canonical architecture baselines (CNN / transformer)

These are **model baselines** for comparative positioning—not replacements for the nnU-Net benchmark rule.

- **U-Net: Convolutional Networks for Biomedical Image Segmentation** — Ronneberger et al., arXiv: [1505.04597](https://arxiv.org/abs/1505.04597)  
- **3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation** — Çiçek et al., arXiv: [1606.06650](https://arxiv.org/abs/1606.06650)  
- **UNETR: Transformers for 3D Medical Image Segmentation** — Hatamizadeh et al., arXiv: [2103.10504](https://arxiv.org/abs/2103.10504)  
- **Swin UNETR: Swin Transformers for Semantic Segmentation of Brain Tumors in MRI Images** — Hatamizadeh et al., arXiv: [2201.01266](https://arxiv.org/abs/2201.01266)

---

## Benchmark datasets / challenges (named anchors)

Use these to **position generalization claims** and **choose external validation analogues**.

- **Medical Segmentation Decathlon (MSD)** — *Nature Communications*, 2022. DOI: [10.1038/s41467-022-30695-9](https://doi.org/10.1038/s41467-022-30695-9)  
- **The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS)** — *IEEE TMI*, 2015. DOI: [10.1109/TMI.2014.2377694](https://doi.org/10.1109/TMI.2014.2377694)  
- **Deep Learning Techniques for Automatic MRI Cardiac Multi-structures Segmentation and Diagnosis: Is the Problem Solved? (ACDC)** — *IEEE TMI*, 2018. DOI: [10.1109/TMI.2018.2837502](https://doi.org/10.1109/TMI.2018.2837502)  
- **KiTS19** — *Medical Image Analysis*, 2021. DOI: [10.1016/j.media.2020.101821](https://doi.org/10.1016/j.media.2020.101821)  
- **LiTS** — *Medical Image Analysis*, 2023. DOI: [10.1016/j.media.2022.102680](https://doi.org/10.1016/j.media.2022.102680)

---

## Classical registration baselines (cross-link)

For **non-DL** registration comparisons required alongside VoxelMorph, see the sibling skill `medical-imaging-classical-features` (ANTs/SyN, elastix, ANTsPy).

---

## Mechanism completion checklist

Use this checklist when a medical-imaging deep learning task asks for a method, not just a smoke test.

### Completion states

- `TRUE_DONE`: the mechanism requested by the task is present in code, run on the intended split, evaluated with the intended metric family, and compared with a same-split baseline.
- `PARTIAL_MECHANISM_INCOMPLETE`: the run exists but a key mechanism is missing, substituted by a proxy, or below the required promotion gate.
- `PREFLIGHT_SMOKE_ONLY`: only import, shape, dryrun, metadata, one-case, or readiness checks passed.
- `NOT_DONE`: no implementation/run/evidence, failed run, stale artifact, or unverified claim.

### Segmentation architecture gate

For U-Net-like, encoder-decoder, multiscale, proposal, cascade, or refinement tasks, require:

- class/function names and files implementing the mechanism;
- number of feature scales and where downsampling/upsampling occurs;
- skip connections, decoder blocks, and refinement/cascade path;
- input/output tensor shapes for representative batches;
- checkpoint, prediction, metric, and config/cache paths;
- baseline comparison on the same split;
- ablation or diagnostic showing the requested mechanism affects behavior.

Shallow substitutions to reject:

- one convolutional stem plus a 1x1 head called an encoder-decoder;
- a standard segmentation head renamed as a proposal or refinement module;
- a routing or attention scalar with no evidence of modality/private feature use;
- a cascade name where the second stage only mixes logits from the first stage.

### Registration and warping gate

For registration, alignment, motion compensation, atlas/template building, or feature warping, require:

- moving and fixed image/frame definitions;
- transform family: rigid, affine, deformable, SyN, B-spline, TPS, optical flow, learned flow, feature-level warp, or translation baseline;
- image spacing/orientation/affine handling and interpolation choices for images and labels;
- warp plausibility: inverse/roundtrip consistency, Jacobian/folding, landmarks, mask consistency, or expert visual review;
- downstream metric affected by the warp, not only successful file writing.

Reject these as completion:

- `CopyInformation`, metadata matching, resampling, center crop, or padding as registration;
- translation-only alignment reported as affine/deformable registration;
- deformation fields without plausibility checks;
- improved Dice with impossible folds, warped labels, or broken anatomy.

### Temporal/video imaging gate

For cine, video, 4D, longitudinal, or multi-timepoint data, require:

- reference frame/timepoint policy;
- how non-reference frames enter the model;
- motion estimation, warping, temporal attention, recurrent/transformer aggregation, or consistency loss;
- target-task head and loss, not just an anatomy or reconstruction proxy;
- comparison to a single-frame/reference baseline.

Reject these as completion:

- frame0-only or middle-frame-only inference called temporal modeling;
- reference anatomy prior with no target-task head;
- temporal metadata or frame extraction with no aggregation/evaluation;
- visual demos without metric comparison.

### Missing-modality and label-availability gate

For multimodal learning, require:

- modality availability table by split/subgroup;
- explicit availability mask or routing variable;
- loss masks for labels that depend on a modality;
- metrics for target-available cases;
- caveats for target-missing cases;
- separate reporting of imputation, modality dropout, or mixture-of-experts behavior.

Reject these as completion:

- treating absent modality cases as hard negatives for a target whose label cannot be observed without that modality;
- reporting only all-case averages when target availability is uneven;
- modality dropout claims without missingness-stratified metrics.

### Proposal, hard-negative, refinement, and cascade gate

For lesion/object proposals, hard-negative training, cascades, and refinement:

- report proposal recall/precision or candidate coverage before downstream refinement;
- distinguish mining from training with the mined examples;
- show the second-stage input contract and whether it receives image crops, masks, features, or logits;
- evaluate the cascade against the base model on the same split;
- include false-positive, component, surface/boundary, and calibration metrics when relevant.

Reject these as completion:

- hard-negative mining reports with no retraining;
- logit mixing called a cascade;
- threshold/gate tuning called a proposal model;
- refinement with no independent prediction or metric.

### External method adaptation gate

External methods progress through separate stages:

1. paper/resource search;
2. license/version/dependency review;
3. clone/import/shape smoke;
4. one-case adapter and input/output contract;
5. fold0 or full validation metric;
6. rollback and cleanup criteria.

Only stage 5+ is an integrated method. Stages 1-4 are useful, but must be reported as resource audit or preflight.

### Evidence package for model results

A model result should include:

- command, environment, log path, exit status, job ID if applicable, and elapsed time;
- code paths and key classes/functions;
- checkpoint path and checkpoint selection rule;
- prediction path and cache isolation by task/config/checkpoint/fold;
- metric path and evaluator version;
- same-split baseline;
- target metric plus relevant secondary metrics;
- failure analysis with at least one qualitative or case-level diagnostic when the model underperforms.

If any item is missing, state `evidence not found` rather than inferring completion.
