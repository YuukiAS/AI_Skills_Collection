# A foundation model for generalizable disease detection from retinal images

## Identity
Zhou and colleagues, Nature 622:156-163, 2023, DOI 10.1038/s41586-023-06555-x.

## Clinical problem
Retinal images are abundant and clinically informative, but disease-detection labels are scarce. The paper presents RETFound as a self-supervised retinal foundation model for label-efficient adaptation.

## Pretraining and modalities
RETFound trains separate CFP and OCT models with masked autoencoding, beginning from ImageNet SSL weights and then pretraining on 904,170 colour fundus photographs and 736,442 OCT scans.

## Fine-tuning tasks
The model is adapted to ocular disease diagnosis, ocular prognosis such as fellow-eye wet AMD conversion, and systemic disease prediction including myocardial infarction, heart failure, ischaemic stroke, and Parkinson's disease.

## Real retinal image evidence
Figure 1 shows the overall RETFound construction and application route with CFP/OCT. Figure 2 reports ocular disease classification, Figure 3 reports systemic disease prediction, and Extended Data Figure 6 shows reconstructed CFP/OCT anatomy and RELPROP saliency maps.

## Generalization evidence
RETFound is evaluated internally and externally. It often outperforms SL-ImageNet, SSL-ImageNet, and SSL-Retinal comparison models across diagnosis, prognosis, systemic prediction, label efficiency, and adaptation efficiency.

## Limitations and interpretation
The paper notes reduced performance across external datasets and imaging devices, UK-dominant development cohorts, separate rather than fused CFP/OCT models, and missing covariates such as demographics and visual acuity.
