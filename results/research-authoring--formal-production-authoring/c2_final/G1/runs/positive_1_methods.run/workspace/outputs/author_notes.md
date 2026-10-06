# Author notes for the Methods draft

The Methods draft is based exclusively on `inputs/01-common_experiment_notes.md`. It contains the procedures supported by those notes but is not yet a reproducible, submission-ready Methods section. No dataset, architecture, training settings, or bootstrap parameters have been inferred.

## Details needed before submission

- **Data and task:** Dataset source, prediction task and class definitions, eligibility criteria, subject and sample counts, and class distribution. Add ethics and consent information if applicable.
- **Data partitioning:** Partition roles, sizes, allocation procedure, and random seed. The notes establish subject disjointness but do not specify a training/validation/test design or broader leakage checks.
- **Input preparation:** Input variables, preprocessing, missing-data handling, temporal sequence construction, and the inputs used by the non-temporal baseline.
- **Models and training:** Model identities and architectures, the basis for describing the temporal model as compact, initialization, optimization, hyperparameters, tuning and model-selection procedures, and the number of runs.
- **Evaluation:** Which partition was evaluated, the prediction unit, decision rules, and how macro-F1 was calculated and aggregated across classes, subjects, or runs.
- **Paired bootstrap:** The resampling unit, how pairing was maintained, treatment of repeated observations within subjects, number of replicates, interval construction, nominal confidence level, random seed, and the subtraction order for the reported difference. Subject-disjoint partitioning does not establish subject-level bootstrap resampling.
- **Implementation:** Software and versions, computational environment, and code/data availability as applicable.

## Results retained from the source

The temporal model achieved a macro-F1 of 0.714, compared with 0.671 for the non-temporal baseline. The notes report a paired bootstrap interval for the difference of [0.018, 0.071]. The confidence level and subtraction order are not explicitly stated and should be confirmed before final reporting. These numerical findings belong in Results rather than Methods. They are preliminary research evidence, not clinical validation.
