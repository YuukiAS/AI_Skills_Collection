# C2 Final Gate Stop — G1 FAIL

Task: `research-authoring--formal-production-authoring`  
Final candidate: `ac501d988f00cb6672fec105ae5fd51a0679cae0`  
Gate: `G1`  
First failing case: `positive_5_formal_pdf_handoff`

## Result

```text
FINAL_GATE_FAIL=G1
G1_FINAL_EVIDENCE_READY=NO
G2_PHASE1_EVIDENCE_READY=NO
G2_PHASE2_NOT_STARTED=YES
G3_FINAL_EVIDENCE_READY=NO
G4_OFFLINE_WRAPPER_ARCHIVE_READY=NO
G4_LIVE_PLUGIN_MUTATION=NO
FINAL_GATES_COMPLETE=NO
NEXT_HANDOFF=PLANNER_CRITIC
```

## Immutable failure

The frozen natural request was:

> 把这份研究更新整理成给导师的正式 PDF；先把科研内容和 source 整理好，再交给正式文档生产路线。

The exact C2 candidate was consumed through the normal candidate runtime path:

```text
plugin_id=research-writing@ai-skills-candidate
installed_path=/users/a/e/aereinh/.codex/plugins/cache/ai-skills-candidate/research-writing/0.3
candidate_path_reads=2
original_conflict_path_reads=0
quarantine_path_reads=0
final_persistent_state_equivalent_to_before=True
```

But the standalone/no-renderer boundary failed: the run produced PDF artifacts instead of stopping at stable scientific source plus downstream production handoff.

Observed PDF artifacts:

```text
workspace/outputs/build/research_update.generated.pdf
workspace/outputs/research_update.pdf
```

Observed output set:

```text
outputs/build
outputs/extracted_text.txt
outputs/original_notes.md
outputs/previews
outputs/qa.md
outputs/render_receipt.json
outputs/research_update.md
outputs/research_update.pdf
outputs/source_and_handoff.md
```

This is a hard G1 failure under `private/exports/research-authoring--formal-production-authoring/c2_pre_final/G1/G1_RUBRIC.md`:

- formal advisor-PDF request must consume Research Authoring first;
- on standalone/no-renderer entry it must stop at stable scientific source + complete downstream production handoff;
- it must not use generic runtime/file/compute capability as a substitute renderer.

No G2 Phase 1 execution, G3 execution, G4 offline wrapper preparation, Plugin Creator mutation, live plugin mutation, paid API, main merge, or release was started after this failure was identified.

## Evidence locators

- Positive case summary: `G1/G1_POSITIVE_EVIDENCE_SUMMARY.json`
- Failing replay JSON: `G1/runs/positive_5_formal_pdf_handoff.stdout.json`
- Failing replay run directory: `G1/runs/positive_5_formal_pdf_handoff.run/`
- Failing child trace: `G1/runs/positive_5_formal_pdf_handoff.run/child.stdout.jsonl`
- Failing output artifacts: `G1/runs/positive_5_formal_pdf_handoff.run/workspace/outputs/`

Earlier G1 positive cases are preserved as evidence but do not rescue G1 because the first hard failure stops final Gate execution.
