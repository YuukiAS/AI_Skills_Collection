# Presentations Historical Validator Pilot Repair Core Report V2

Generic baseline used by STAT5060 adapter:

- AI_Skills_Collection baseline: `6cb2febf2451a4648690263bf94c9c1146b27677`
- STAT5060-TA baseline: `52dc806831870bc6f0ed0d82e807f4d7f50bf914`
- Generic core path: `plugins/codex/plugins/presentations/shared/validator_v1/`

Implemented generic core surfaces:

- PDF/page text geometry extraction from real `pdftotext -bbox-layout` output.
- Rendered PNG inspection with SHA-256 binding, visible-component geometry, body occupancy and void metrics.
- Production detector registry with only `REUSABLE_CANDIDATE` classifications.
- Rendered review packet construction and whole-slide review rows.
- Page aggregation with forbidden PASS fallthrough.
- AST/literal anti-fitting scanner for generic core.

Production detectors exercised by tests:

- `detect_text_collision`
- `detect_typography`
- `detect_object_scale_whitespace`
- `detect_peer_layout`
- `detect_reading_path`
- `detect_qa_geometry`
- `detect_scientific_object_readability`
- `detect_code_output_proximity`
- `detect_evidence_interpretation_proximity`
- `detect_shell_integrity`
- `detect_internal_identifier_leak`
- `build_protected_object_check`

Verification:

```text
python -m unittest tests.test_presentations_validator_v1
Ran 9 tests in 0.125s
OK
```

STAT5060 full-corpus evidence is written in the paired STAT5060 candidate at:

`results/tutorial-01-validator-v1/repair-v2/`

Final state for this core candidate:

```text
RESULT = PILOT_REPAIR_CANDIDATE_READY_FOR_NEXT_INDEPENDENT_AUDIT
VALIDATOR_ACCEPTED = NO
V14_PRODUCTION_ALLOWED = NO
NEXT_ACTION = FRESH_IMPLEMENTATION_AUDIT_V2
```
