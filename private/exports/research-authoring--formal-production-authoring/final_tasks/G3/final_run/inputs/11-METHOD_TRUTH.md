# METHOD_TRUTH.md

本文件冻结 MoSAIC 论文第一版方法事实。所有条目来自 `/users/a/e/aereinh/MoSAIC/code/source`，upstream commit `d334bd1fb2a99dbbc230510590cd8e3ee08cc377`。本文件不是论文正文，不能把未验证的机制效果写成实验结论。

## Source State

- Source repository: `https://github.com/IndeedLiu/MoSAIC`
- Local source path: `/users/a/e/aereinh/MoSAIC/code/source`
- Commit: `d334bd1fb2a99dbbc230510590cd8e3ee08cc377`
- Source git status at setup: `## main...origin/main`
- Native inference entrypoint: `scripts/infer_and_submit.py`
- Model factory: `myops/models/__init__.py::build_model`
- Label semantics: `myops/data/labels.py`

## Inputs And Label Space

- MyoPS modalities are `LGE`, `C0`, `T2`, in that order inside `MYOPS_MODALITIES` (`myops/data/labels.py`). Missing `C0` or `T2` is represented by a zero-filled channel plus `modality_presence_mask`; inference always starts with `LGE` if present (`scripts/infer_and_submit.py::preprocess_myops_val`, `myops/data/preprocessing.py::preprocess_myops_case`).
- CineMyoPS input is one 4D `Cine` volume. Preprocessing estimates an ED/reference frame by a percentile-based blood-pool heuristic and selects a fixed ED-anchored temporal window (`estimate_cine_reference_frame`, `select_cine_frame_indices`).
- Official labels are `myo=200`, `lv=500`, `rv=600`, `edema=1220`, `scar=2221`. Training labels are compact: MyoPS fine `[myo, lv, rv, edema, scar] -> 1..5`; Cine fine `[myo, lv, scar] -> 1..3`.

## Preprocessing

- MyoPS preprocessing uses robust z-score normalization, optional rigid/affine SimpleITK registration to a reference modality, resampling to `myops_target_spacing: [1.25, 1.25, 10.0]`, and ZHW tensor layout. The final payload stores image, labels, modality masks, supervision masks, bounding boxes, affine/header, original spacing and original shape.
- The final MyoPS configs enable rigid registration to `LGE` in `configs/myops_coarse.yaml`, `configs/myops_fine.yaml`, and `configs/myops_edema_fine.yaml`.
- Cine preprocessing resamples each frame to `cine_target_spacing`, stores the ED/reference image, selected frame indices, and optional temporal summary features. The final cine configs use `cine_target_spacing: [1.25, 1.25, 8.0]`, `cine_frame_fraction: 0.667`, and `max_cine_frames: 20`.

## Model Path

- Stage 1 coarse anatomy uses `CoarseNet` through `build_model(stage="coarse" or arch="2d_coarse")`. MyoPS coarse predicts `ring_myo`, `lv`, `rv`; Cine coarse predicts `ring_myo`, `lv`.
- MyoPS fine scar path uses `FinePathNet` (`myops/models/fine_path_net.py`). The documented input layout is `[B, 7, H, W]`: `LGE`, `C0`, `T2`, three presence masks, and one coarse prior. It uses separate encoders for `LGE`, `C0`, and `T2`; missing modalities are gated by the presence mask.
- `FinePathNet` can use TPS feature alignment (`TPSHead`, `TPSWarper`), multi-scale fusion (`MSFDecoder`), a spatial prior gate (`SpatialPriorGate`), and training-only myocardium consistency heads. In the final `configs/myops_fine.yaml`, `use_tps=true`, `use_spg=true`, and `use_consistency=true`.
- The final MyoPS native inference loads two coarse models, one scar fine model, and one dedicated EdemaNet: `load_myops_models` returns `(coarse_new, coarse_old, scar_model, edema_model)`. New coarse drives scar and final myo mask; old coarse drives the edema branch according to the source comment.
- The edema expert is `EdemaNet` loaded by `myops/inference/edema_predict.py::load_edema_model`. It predicts an edema-zone probability map using LGE, C0, T2, and a cardiac mask derived from coarse anatomy; final pure edema is `edema_zone & ~scar` in `merge_labels`.
- Cine fine path uses `CineHybridNet` (`myops/models/cine_hybrid_net.py`). Input layout is `[B, T+1, H, W]`, where the first `T` channels are ED-anchored selected cine frames and the last channel is a coarse anatomy prior. The default pathology input is `flow`: motion field + motion-warped anatomy + coarse prior, not raw cine intensity.
- Final cine inference loads one coarse model and two cine fine models, averages the fine probabilities, and evaluates three spacings `[1.25,1.25,4.0]`, `[1.25,1.25,8.0]`, `[1.25,1.25,16.0]` when shapes match.

## Losses And Training-Time Modules

- Generic stage loss is implemented in `myops/engine/losses.py::StageLoss` with masked sigmoid Dice, masked BCE, optional pathology Tversky/focal terms, class-specific pathology weights, deep supervision, modality consistency, and registration-related terms.
- Supervision masks come from `SUPERVISION_BY_CENTER` in `myops/data/labels.py`; unannotated classes are masked rather than treated as negatives.
- Cine fine config includes auxiliary weights for pathology, anatomy, consistency, motion, and flow smoothness in `configs/cine_fine.yaml`.
- Dedicated edema training uses `myops/engine/edema_losses.py::EdemaLoss`, a Dice plus weighted cross-entropy loss.
- Training scripts exist (`scripts/5fold_train_all.py`, `scripts/train_full.py`, `scripts/train_single_experiment.py`), but this paper workspace does not authorize training.

## Inference And Postprocessing

- Native inference entrypoint is `scripts/infer_and_submit.py --val-dir <root> --gpu <id>`.
- TTA uses horizontal and vertical flips (`TTA = {"enabled": True, "flips": ["horizontal", "vertical"]}`).
- MyoPS scar thresholds come from `default_thresholds(TRACK_MYOPS, "fine")`, with pathology thresholds 0.3 by default. Edema-zone threshold in the native script is `0.35`.
- Postprocessing constrains pathology labels inside myocardium/anatomy masks, removes small components via `clean_prediction_by_class`, keeps the largest scar component when scar exists, and converts compact labels to official labels before saving.
- Native output layout from `infer_and_submit.py` is `outputs/validation/MyoPS/Anonymous Center/<Case>/<Case>_pred.nii.gz` and `outputs/validation/CineMyoPS/Anonymous Center/<Case>/<Case>_pred.nii.gz`, then ZIPs to `outputs/CARE-Myocardium-UNC.zip`.

## Enabled Versus Present-But-Not-Final

- Enabled in final native inference: MyoPS coarse cascade, MyoPS `FinePathNet` scar expert with TPS/SPG/consistency-enabled checkpoint architecture, dedicated EdemaNet, cine coarse model, two-model cine fine ensemble, TTA, anatomy constraints, and connected-component cleanup.
- Present but not established as final manuscript evidence: ablation configs such as `ablation_no_coarse.yaml`, `2d_earlyfusion`, `pathology_input="intensity"`, `pathology_input="none"`, `use_t2_aux`, and scripts that generate paper tables from missing or external JSON files.
- Unresolved: exact training data manifest used for final checkpoints, exact random seeds for each final checkpoint beyond config defaults, and official leaderboard numbers unless an organizer receipt or committed result file is supplied.
