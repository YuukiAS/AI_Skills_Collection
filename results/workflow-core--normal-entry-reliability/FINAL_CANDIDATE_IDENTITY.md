# workflow-core 0.5 Final Candidate Identity

Task: `workflow-core--normal-entry-reliability`

Branch: `work/workflow-core--normal-entry-reliability`

Approved package commit: `314b28289ee92d4115396fd3c486a4100741692f`

Implementation qualification commit:
`0e6c134fef60cd9c22895dba42d7823e01644793`

Final production candidate commit:
`671eb532e0ec949dc7889427379a1113cf7a6ea9`

Evidence-only branch HEADs after this candidate are not product candidates.
They only add tracked evidence under
`results/workflow-core--normal-entry-reliability/`.

## Product Identity

- Repository version: `5.4.1`
- Affected plugin: `workflow-core`
- Plugin version: `0.4 -> 0.5`
- Other central plugins: `NO_BUMP`

## Final Candidate Product Commit

`671eb532e0ec949dc7889427379a1113cf7a6ea9` is the exact product candidate
that contains the workflow-core release metadata and generated marketplace
payload.

The final candidate commit changed:

- `VERSION`
- `CHANGELOG.md`
- `README.md`
- `docs/plugin-changelogs/workflow-core.md`
- `docs/plugin-todos/workflow-core.md`
- `scripts/codex_marketplace_config.json`
- `registry.json`
- `docs/SKILL_CATALOG.md`
- `plugins/codex/plugins/workflow-core/.codex-plugin/plugin.json`
- release-version expectations in relevant tests

## Evidence-Only Rule

Evidence commits after `671eb532e0ec949dc7889427379a1113cf7a6ea9` must not
modify:

- workflow-core production source;
- generated workflow-core marketplace payload;
- repository or plugin version metadata;
- release changelog content;
- frozen G1-G6 contract.

Final Critic and release closure must preserve this distinction: the evidence
HEAD can be newer, but the product candidate remains the exact commit above.
