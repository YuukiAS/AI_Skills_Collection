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
