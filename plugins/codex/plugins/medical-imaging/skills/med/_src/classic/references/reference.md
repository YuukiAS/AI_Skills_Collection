# References: Classical imaging, radiomics, and DICOM

## Core toolkits (implementation)

### SimpleITK

- **SimpleITK Image-Analysis Notebooks: a Collaborative Environment for Education and Reproducible Research** — Ziv Yaniv et al., *Journal of Digital Imaging*, 2018. DOI: [10.1007/s10278-017-0037-8](https://doi.org/10.1007/s10278-017-0037-8)  
- Documentation: [https://simpleitk.org/documentation/](https://simpleitk.org/documentation/)

### PyRadiomics

- **Computational Radiomics System to Decode the Radiographic Phenotype** — van Griethuysen et al., *Cancer Research*, 2017. DOI: [10.1158/0008-5472.CAN-17-0339](https://doi.org/10.1158/0008-5472.CAN-17-0339)  
- Documentation: [https://pyradiomics.readthedocs.io/](https://pyradiomics.readthedocs.io/)

### pydicom

- Project / docs: [https://pydicom.github.io/pydicom/](https://pydicom.github.io/pydicom/)

### highdicom

- Documentation: [https://highdicom.readthedocs.io/](https://highdicom.readthedocs.io/)  
- GitHub: [https://github.com/ImagingDataCommons/highdicom](https://github.com/ImagingDataCommons/highdicom)

### ANTsPy / ANTs ecosystem

- **The ANTsX ecosystem for quantitative biological and medical imaging** — Tustison et al., *Scientific Reports*, 2021. DOI: [10.1038/s41598-021-87564-6](https://doi.org/10.1038/s41598-021-87564-6)  
- ANTsPy: [https://github.com/ANTsX/ANTsPy](https://github.com/ANTsX/ANTsPy)  
- ANTs core: [https://github.com/ANTsX/ANTs](https://github.com/ANTsX/ANTs)

---

## Classical algorithm / preprocessing anchors

### SyN / ANTs foundational paper

- **Symmetric diffeomorphic image registration with cross-correlation: evaluating automated labeling of elderly and neurodegenerative brain** — Avants et al., *Medical Image Analysis*, 2008. DOI: [10.1016/j.media.2007.06.004](https://doi.org/10.1016/j.media.2007.06.004)

### elastix

- **elastix: a toolbox for intensity-based medical image registration** — Klein et al., *IEEE TMI*, 2010. DOI: [10.1109/TMI.2009.2035616](https://doi.org/10.1109/TMI.2009.2035616)  
- Official site: [https://elastix.lumc.nl/](https://elastix.lumc.nl/)

### N4ITK

- **N4ITK: improved N3 bias correction** — Tustison et al., *IEEE TMI*, 2010. DOI: [10.1109/TMI.2010.2046908](https://doi.org/10.1109/TMI.2010.2046908)  
- Typical usage: **SimpleITK** `N4BiasFieldCorrectionImageFilter` pathway (see SimpleITK examples).

---

## Radiomics standardization anchors (IBSI)

- **The Image Biomarker Standardization Initiative: Standardized Quantitative Radiomics for High-Throughput Image-based Phenotyping** — Zwanenburg et al., *Radiology*, 2020 (IBSI 1). DOI: [10.1148/radiol.2020191145](https://doi.org/10.1148/radiol.2020191145)  
- **The Image Biomarker Standardization Initiative: Standardized Convolutional Filters for Reproducible Radiomics and Enhanced Clinical Insights** — Zwanenburg et al., *Radiology*, 2024 (IBSI 2). DOI: [10.1148/radiol.231319](https://doi.org/10.1148/radiol.231319)  
- IBSI resources: [https://theibsi.github.io/](https://theibsi.github.io/)

---

## Reporting / quality anchor (CLEAR)

- **CheckList for EvaluAtion of Radiomics research (CLEAR)** — Kessler et al., *Insights into Imaging*, 2023. DOI: [10.1186/s13244-023-01415-8](https://doi.org/10.1186/s13244-023-01415-8)

---

## Cross-links to deep learning skill

- Benchmark **dataset** names (MSD, BraTS, ACDC, KiTS, LiTS) and **learning-based registration** comparisons are detailed in `medical-imaging-deep-learning` / `references/reference.md`.
