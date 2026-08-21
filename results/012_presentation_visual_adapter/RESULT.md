---
schema: AI_BRIDGE_VISUAL_ADAPTER_RESULT_V1
task_key: 012_presentation_visual_adapter
adapter_commit: c6968a738c5d4d8e81ecdee06063d590633aa856
evidence_commit: c0b88de5c8c475794987bf5abae644b231a72344
bridge_kit_commit: f7c2f97cf44b1a4a52ff188c4a45a7eec57b808e
---

# 012 Presentation Visual Adapter Result

## Why this adapter exists

The previous active visual route for the research presentation round was `011_round_handoff`: a GitHub Pages PDF consumed by an external Planner through screenshots. That route produced real historical evidence and remains valid provenance, but it blocked when the external Planner could not reliably open and screenshot the immutable public PDF. The correct repair was not to keep changing the Pages transport. The current primary route now uses Bridge Kit tracked Visual Review evidence.

## Current visual evidence chain

```text
editable PPTX
-> real PPTX render PNGs
-> MECHANICAL_VISUAL_REVIEW.json
-> Bridge Kit OpenAI Visual Review
-> tracked VISUAL_REVIEW.json
-> Presentation Corpus Planner
```

The adapter is `tests/fixtures/presentations/research_group_meeting/build_ai_bridge_visual_inputs.py`. It reuses the existing public-safe four PNGs from `tests/fixtures/presentations/research_group_meeting/visual_review_packet_source/rendered/`, verifies the real render chain and mechanical review, and writes `results/012_presentation_visual_adapter/visual_review/visual_inputs.json`.

## Rubric

The manifest keeps the Research Presentation rubric in this repository, not in Bridge Kit. It requires pixel-level page review and asks whether each page has a real scientific object, matches its declared archetype, avoids card/table/dashboard substitutes, keeps figures, labels, formulas, axes and legends readable, makes evidence boundaries clear, and contains enough research information for about 30-90 seconds of group-meeting discussion. It explicitly forbids inferring PASS from SHA, file existence, page count, metadata, mechanical PASS, expected object text, or reference IDs.

## Live smoke evidence

### Current production smoke

- Bridge Kit 0.5.4 commit: `f7c2f97cf44b1a4a52ff188c4a45a7eec57b808e`
- Consumer pin / manifest identity commit: `c6968a738c5d4d8e81ecdee06063d590633aa856`
- Generated Terra visual evidence commit: `c0b88de5c8c475794987bf5abae644b231a72344`
- GitHub Actions run: `32466775342`
- Model: `gpt-5.6-terra`
- Canonical evidence: `results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json`
- Result: `overall_decision=REVISE`, `blocking_findings=3`

The four input images remain SHA-bound in both `visual_inputs.json` and `VISUAL_REVIEW.json`:

| Page | Image SHA | Terra visual result |
| --- | --- | --- |
| slide_1 | `94a8ef8d40471ee5675066cc137a2e0f9ea663df39b1f6660fc53d73967e5a88` | REVISE |
| slide_2 | `44ebe447b025f86b307c9b961ced7102720378c096f7a013966c9e062eef09c3` | REVISE |
| slide_3 | `bc92d7263823f05f4d3b0628b60a894c983e93a35d5fc9d5226d720f40863227` | REVISE |
| slide_4 | `4ab75ebf472cbee18808dfc7029d78a979e11e180374a16d2e9c1db18a04ff1e` | PASS |

The Terra run proves the migrated transport works with the new shared default model, Responses API image input, Structured Output validation, and bot write-back. Its `REVISE` decision is model visual evidence for the Planner to consume; it is not a transport failure.

### Historical first smoke

- Adapter implementation commit: `6c1039680768e5440eef1dd3e2dce26bef34f287`
- Generated visual evidence commit: `81cabe4d451e1f29f542168cac7c3a446d0567df`
- Bridge Kit pinned commit: `e915d04756490fafbd111eaa445295f0103b2c94`
- GitHub Actions run: `32463908616`
- Model: `gpt-4.1-mini`
- Canonical evidence: `results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json`
- Result: `overall_decision=PASS`, `blocking_findings=[]`

The four input images are SHA-bound in both `visual_inputs.json` and `VISUAL_REVIEW.json`:

| Page | Image SHA | OpenAI visual result |
| --- | --- | --- |
| slide_1 | `94a8ef8d40471ee5675066cc137a2e0f9ea663df39b1f6660fc53d73967e5a88` | PASS |
| slide_2 | `44ebe447b025f86b307c9b961ced7102720378c096f7a013966c9e062eef09c3` | PASS |
| slide_3 | `bc92d7263823f05f4d3b0628b60a894c983e93a35d5fc9d5226d720f40863227` | PASS |
| slide_4 | `4ab75ebf472cbee18808dfc7029d78a979e11e180374a16d2e9c1db18a04ff1e` | PASS |

## Secret and trigger boundaries

The workflow uses only the repository secret name `OPENAI_VISUAL_REVIEW_API_KEY`, mapped inside the visual job to `OPENAI_API_KEY`. No secret value is stored in repository files. The tracked evidence and result files contain only non-secret run, commit, model, schema, SHA, and review output metadata.

Evidence commit `81cabe4d451e1f29f542168cac7c3a446d0567df` did not start a second Visual Review run. The workflow ignores `results/**/visual_review/**`, so generated evidence commits do not self-trigger the visual review job.

Evidence commit `c0b88de5c8c475794987bf5abae644b231a72344` is also evidence-only under `results/**/visual_review/**`; it did not start a second Visual Review run.

## Conclusion

`VISUAL_TRANSPORT_PASS`.

The active machine visual-evidence path is now Bridge Kit tracked `VISUAL_REVIEW.json`, not GitHub Pages PDF screenshots. The current production evidence is the `gpt-5.6-terra` run, whose visual decision is `REVISE`. This does not mean the Research Presentation Corpus Program has passed or failed. `Planner academic decision still pending`: the external Presentation Corpus Planner still needs to read `VISUAL_REVIEW.json`, `visual_inputs.json`, the mechanical evidence, and the current program contract before making the final academic visual gate decision.
