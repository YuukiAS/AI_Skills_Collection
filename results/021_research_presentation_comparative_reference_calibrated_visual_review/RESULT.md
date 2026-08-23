---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 021_research_presentation_comparative_reference_calibrated_visual_review
implementation_commit: 6037c6280ec6d9db46e78292ec5013b28f98d9f8
---

# 021 Research Presentation Comparative Reference-Calibrated Visual Review - Executor Result

## Implementation commit

Current implementation commit: `6037c6280ec6d9db46e78292ec5013b28f98d9f8`.

Earlier task commits:

- `54b15cb96bd9b9eb8737b5a635e713a7eb243218` - added comparative review preparation, validators, workflow, manifests, and tests.
- `83a016a6e0f1e7e5b17c16b2952898ecef1a3ddc` - repaired Bridge Kit manifest compatibility by using the supported `generic` workflow type while preserving comparative `review_kind`.
- `2645eeed58ab74d35019f07f39ed8e1e7f574ef2` - repaired Bridge Kit output-path compatibility while keeping Terra-visible task identity anonymous.
- `9c067258bca35ed25ff8ffc8a26171d9a733f163` - GitHub Actions evidence commit containing the two live Terra `VISUAL_REVIEW.json` files.
- `6037c6280ec6d9db46e78292ec5013b28f98d9f8` - decoded comparative review report.

## Implemented

Task 021 now builds two comparative reference-calibrated visual review cases:

- statistical estimator / equation;
- medical-image comparison.

Each case contains exactly three generated candidates from task 020 and two matched inspected reference renders. The reference pages are materialized from public source PDFs at runtime, rendered with `pdftoppm`, checked against the inspected canonical page SHA, anonymized for visible provenance marks, and copied into uniform anonymous runtime filenames.

The Terra-visible manifests use anonymous `item_A` ... `item_E` IDs and neutral runtime paths. Candidate/reference identity, RRL/SRC provenance, source SHA, canonical render SHA, actual review-input SHA, materialization method, and rights notes are stored only in the internal `review_identity_map.json` files.

## Live comparative visual review

The successful workflow run was:

`https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/32634528235`

It ran exactly one `gpt-5.6-terra` comparative review for each immutable case identity:

- statistical review identity: `d97821e39442db72ad90d3855a1f9fc514f9e9e7ddfe62517a7aeb2f560df1c8`
- medical review identity: `8f3aa043d534335b7d9c2342717c0f1b193c448e4585cf16578c056eff03a445`

Both reviews returned `PASS` as assessable comparative evidence packages. This is not a product-quality PASS.

## Decoded findings

The decoded report is:

`docs/audits/RESEARCH_PRESENTATION_COMPARATIVE_VISUAL_REVIEW_REPORT.md`

Key decoded facts:

- Statistical case: the mature inspected reference `RRL-028` was the only item Terra judged mature. All three generated candidates were `REVISE`, with the best generated variant still below the mature reference bar due to weak equation contrast and indirect annotation.
- Medical case: Terra judged every item `REVISE`. Generated candidates had cleaner layout than some references, but no item reached mature research-group-meeting or strong conference-talk quality; the closest generated variants were still limited by synthetic/demo-like image evidence.

The result explicitly preserves no-winner semantics. It does not select a final candidate, lock a deck design system, start a holdout, or declare `ONE_SHOT_QUALITY_PASS`.

## Added files and checks

Added shared/plugin-mirrored preparation and validation scripts:

- `skills/tools/documents-media/presentations/shared/scripts/prepare_comparative_visual_review.py`
- `skills/tools/documents-media/presentations/shared/scripts/validate_comparative_visual_review.py`
- `plugins/codex/plugins/presentations/shared/scripts/prepare_comparative_visual_review.py`
- `plugins/codex/plugins/presentations/shared/scripts/validate_comparative_visual_review.py`

Added consumer workflow:

- `.github/workflows/research-presentation-comparative-visual-review.yml`

Added visual evidence:

- `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/statistical/visual_inputs.json`
- `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/statistical/review_identity.json`
- `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/statistical/review_identity_map.json`
- `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/statistical/VISUAL_REVIEW.json`
- `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/medical/visual_inputs.json`
- `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/medical/review_identity.json`
- `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/medical/review_identity_map.json`
- `results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review/medical/VISUAL_REVIEW.json`

Added regression coverage in `tests/test_presentations.py` for anonymous visible manifests, internal identity mapping, exact candidate/reference counts, forbidden visible provenance terms, and validator execution.

## Verification

- `python skills/tools/documents-media/presentations/shared/scripts/validate_comparative_visual_review.py --require-bytes` - PASS
- `python skills/tools/documents-media/presentations/shared/scripts/validate_comparative_visual_review.py --require-review --require-bytes` - PASS
- `python -m unittest tests.test_presentations` - PASS, 20 tests
- `python -m unittest discover -s tests` - PASS, 116 tests
- `python scripts/skills.py validate` - PASS
- `python scripts/build_codex_marketplace.py --validate --check --path-report` - PASS
- `PYTHONPATH=/home/yuukias/GPT_Codex_AI_Bridge_Kit python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection` - PASS
- `git diff --check` - PASS
- GitHub Actions run `32634528235` - PASS
- Conventional push CI for `2645eeed58ab74d35019f07f39ed8e1e7f574ef2` - PASS for `AI Bridge Visual Review` and `Codex Marketplace`

## Deliberately unchanged

- No Bridge Kit core changes.
- No candidate geometry changes.
- No committed reference screenshots or PDF pages.
- No final deck generation, design-system lock, statistical holdout, medical holdout, or `ONE_SHOT_QUALITY_PASS`.
- No Planner-owned review artifact was written.

## CI handoff

`ci_required=true`; `CURRENT.ci_status` remains `PENDING`.

This handoff moves task 021 to `WAITING_FOR_CI`. Scheduled Planner review remains independent.
