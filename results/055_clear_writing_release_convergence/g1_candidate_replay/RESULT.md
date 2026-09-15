# G1 Candidate Replay Result — Bloom Known Regression Smoke

Status: `PASS_FOR_G1_SMOKE_ONLY`

This is not full G1-G6 release evidence and not a product release PASS. It is a
normal-entry candidate replay smoke for exact candidate `C1`.

## Candidate Identity

```text
candidate_commit = 68a5bfb860ef09eeafb994de18878b86a2b13d0d
plugin_id = writing-style@ai-skills-candidate
plugin_version = 0.3
runtime_version = codex-cli 0.153.4
run_id = 20260915T061302Z-1349544
```

The replay helper reported actual candidate consumption:

```text
actual_consumption.proven = true
actual_consumption.event_type = item.started
actual_consumption.line_index = 4
```

The consumed skill path in the child JSONL was under:

```text
/overflow/htzhu/mingcheng_new/.codex-global/plugins/cache/ai-skills-candidate/writing-style/0.3/
```

The child JSONL and stderr remain in ignored `.local-runtime/` and are not
committed.

## Inputs

Task:

```text
results/055_clear_writing_release_convergence/g1_candidate_replay/BLOOM_NORMAL_ENTRY_TASK.md
```

Source:

```text
results/052_writing_style_reader_facing_generalization_closure/known_regression/bloom_filter_wikipedia_excerpt.md
```

## Repo-Local Public Artifacts

```text
results/055_clear_writing_release_convergence/g1_candidate_replay/artifacts/bloom_filter.md
results/055_clear_writing_release_convergence/g1_candidate_replay/artifacts/stage_receipt.json
results/055_clear_writing_release_convergence/g1_candidate_replay/artifacts/plugin-add.json
results/055_clear_writing_release_convergence/g1_candidate_replay/artifacts/run.json
```

Artifact hashes:

```text
0be3a1d56e90c065fc4e6fa26d785e4b5d23f8ff21a59f2c23ad4d0ce08e4bf8  artifacts/bloom_filter.md
d652512838d9874ec218ac475ae3678d62f5f9252287e50487a36bb30e00feed  artifacts/stage_receipt.json
b63e6393314ce93796c54b0c8224396cab1d9ef8fce1c2247756580b2f0f42fe  artifacts/plugin-add.json
7c4d8ba466acbc6d41d93a8453387b58405afed4f0fb8e1f68cd67de3637abfd  artifacts/run.json
5ca536e496c03f74ed6b079111a08884f8ef47ecb703ca9ecbcd6f020672b9df  BLOOM_NORMAL_ENTRY_TASK.md
```

## Mechanical Receipt

The generated stage receipt reports:

```text
schema = SCIENTIFIC_REWRITE_HEAVY_ROUTE_RECEIPT_V2
runtime = scientific-rewrite.meaning-realization.v2
route_selection.selected_route = scientific-rewrite
route_selection.ordinary_user_prompt = true
meaning_map.source_context_item_count = 1
reader_plan.reader_disposition_count = 13
reader_plan.excluded_source_context_item_count = 1
realization_packet_count = 5
assembly.ok = true
semantic_audit.ok = true
exact_verification.exact_item_count = 14
reader_facing_internal_frame.ok = true
standalone_reader_frame.ok = true
external_api_call_count = 0
paid_generation_used = false
private_plaintext_committed = false
```

## Qualitative Reading

The copied candidate was read from start to finish. It presents Bloom filters as
a standalone Chinese technical explanation with sections for definition,
insertion/query, hash construction, deletion difficulty, and time/space tradeoff.

Observed PASS points:

- retains Bloom Filter identity, Burton Howard Bloom attribution, year 1970,
  false positive / false negative semantics, `m`, `k`, `m=18`, `k=3`,
  `{x,y,z}`, `w`, `O(k)`, `O(m)`, `O(n)`, `O(log n)`, and cited years
  2004a/2004b/2006;
- keeps legitimate structured technical content as formulas, a short ordered
  list, and a complexity table;
- clarifies deletion limitations and the auxiliary removal-filter caveat;
- omits webpage wrappers and source packaging instead of preserving them as
  prose;
- does not mention Reviewed Handoff, branch, commit, candidate, audit, CI, or
  other internal process terms in the reader-facing candidate;
- avoids source-process frames such as "原文指出" and "给定材料说明".

Residual scope:

```text
This proves candidate identity and one public known-regression smoke only.
Phase 4 still requires full G1-G6 representative replay from exact C1,
including complete long-document evidence and required render checks.
```
