# Project Instructions Editor 0.2 Web Acceptance Result

## Identity

- `FINAL_CANDIDATE_COMMIT=f0e41f49b46be1a3b9f3c499cb580066f694b031`
- `PRE_ACCEPTANCE_EVIDENCE_TIP=e45060c85d8371700f73fc0bd73373c54fb798ae`
- `LIVE_PRIVATE_USER_WRAPPER_VERSION=0.2.8`
- Acceptance surface: real ChatGPT Web / Project usage with explicit PIE invocation.
- Evidence authority: the user's direct acceptance report in the closure task. No nested Codex or fixture replay was used for this result.

## Verified behavior

1. Missing baseline followed by a complete baseline and an added rule: PASS. PIE requested the complete current setting without reconstructing it from Project history, Memory, or context; after receiving `B`, it produced a Markdown preview and a complete clean final setting while preserving unrelated semantics.
2. Deletion and replacement: PASS. Deletions used strikethrough, replacements used strikethrough for old text plus bold for new text, unchanged rules remained unchanged, the preview matched the clean final, and no extra rule was introduced.
3. Explicit reset with a broad replacement: PASS. PIE required the complete old baseline, removed all four old rules, represented the two new rules clearly at sentence granularity, and returned a clean final containing only the reset rules.
4. Explicitly empty setting to greenfield: PASS. PIE accepted the empty setting as a complete baseline, did not request nonexistent old text, added only the two requested rules, and did not import Project history.
5. No-op: PASS. PIE recognized that the existing setting already covered the request and produced neither a duplicate rule, a fake Markdown diff, nor an identical duplicate setting.

## Accepted non-blocking difference

The fixed baseline-receipt sentence did not appear consistently in the reset and greenfield displays. The user accepted this as non-blocking because baseline provenance, edit semantics, preview behavior, and clean final results were correct. This difference is recorded without another repair or test round.

## Not claimed

- Automatic implicit invocation was not tested and is not required for this 0.2 acceptance.
- The fixed baseline receipt is not claimed to appear consistently on every accepted path.

## Final live status

- `G1_FINAL_LIVE=PASS_EXPLICIT_INVOCATION`
- `G4_FINAL_LIVE=PASS_USER_ACCEPTED_WEB_ARTIFACTS`
- `IMPLICIT_INVOCATION=NOT_TESTED_NOT_REQUIRED`
- `ADDITIONAL_MODEL_REPLAY=NOT_RUN`

