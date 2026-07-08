# CardiacNexus architecture map

## Top-level pipeline flow

1. `step1_prepare_data_cmr.py`
   - scans raw UKB zip folders
   - generates Slurm scripts under `jobs/prepare_data_*`
   - delegates work to `scripts/prepare_data.py`
2. `step2_segment.py`
   - scans subject folders under `data/visit*/nii`
   - generates Slurm scripts under `jobs/segment_*`
   - dispatches modality-specific segmentation scripts in `src/segmentation/*`
3. `step3_extract_feature_separate.py`
   - generates Slurm scripts under `jobs/extract_feature_*`
   - runs modality-specific feature extraction in `src/feature_extraction/*`
   - generates `aggregate.pbs`
4. `step4_extract_feature_combined.py`
   - generates combined-feature jobs
   - aggregates cross-modality outputs

## Key directories

- `config.py`: current single source of runtime configuration, but strongly machine-coupled.
- `scripts/`: data prep, aggregation, experimental helpers, one-off scripts.
- `src/segmentation/`: per-modality segmentation wrappers and legacy deploy scripts.
- `src/feature_extraction/`: per-modality phenotype extraction.
- `utils/`: shared helpers for logging, Slurm, I/O, image geometry, QC, cardiac mechanics.
- `model/`: trained weights expected by the wrappers.
- `libs/`: external or vendored modality-specific code.
- `jobs/`: generated Slurm batch scripts (per-step, per-visit folders).
- `docs/`: separate documentation website, not runtime pipeline logic.

## Current high-risk seams

- `config.py` absolute paths
- `sys.path.append(...)`
- `os.system(...)`
- TF1 deploy wrappers for SA/LA/Aortic dist
- duplicated `nnUNet` / `UMamba` code paths
- MIRTK-dependent strain analysis in `eval_strain_lax.py`, `eval_strain_sax.py`, and `utils/cardiac_utils.py`
- schema-free CSV aggregation in `scripts/aggregate_csv.py`

## Refactor targets

- packaged, layered configuration
- reusable backend adapters
- Slurm generation separated from business logic
- stable phenotype output contracts
- pluggable registration backends with regression benchmarks
