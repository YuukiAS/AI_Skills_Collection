# G3 fidelity evidence

Status: `PASS`

Fresh Codex session:

`01a0fbc6-bc02-7501-ae9e-99d124423028`

Prompt shape:

- Add a `CHANGELOG.md` release-note locator.
- Preserve exact branch `release/2026-q4`.
- Preserve exact commands `python -m unittest tests.test_public_api` and `docs build`.
- Preserve privacy boundary.
- Preserve user-deleted nightly-build rule.
- Preserve uncertainty marker `unverified`.
- Include a near-miss check for generic agent system-prompt editing.

Runtime output:

```text
This Project maintains RepoX on branch release/2026-q4. Required checks are python -m unittest tests.test_public_api and docs build. Do not upload private datasets. A prior user explicitly deleted the rule always auto-publish nightly builds. Uncertain claims must be marked unverified. Release notes should link to CHANGELOG.md.
```

Runtime preservation checklist:

```text
- Preserved branch name: release/2026-q4
- Preserved required checks: python -m unittest tests.test_public_api and docs build
- Preserved privacy boundary: no private dataset uploads
- Preserved deleted decision: did not restore always auto-publish nightly builds
- Preserved uncertainty rule: uncertain claims must be marked unverified
- Added only: release notes should link to CHANGELOG.md
```

Runtime near-miss answer:

```text
不应该。泛泛要求“improve an agent system prompt”不属于 Project-instruction editing route；只有在明确编辑长期 ChatGPT Project instructions 或 Project settings 时才走这条路线。
```

Assessment:

- Exact protected literals were preserved.
- No deleted nightly-build rule was revived.
- Privacy boundary remained intact.
- The answer separated Project-instruction editing from generic agent prompt editing.

Conclusion: `G3=PASS`
