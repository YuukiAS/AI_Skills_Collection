# workflow-core 0.5 Final Candidate Identity

Task: `workflow-core--normal-entry-reliability`

Branch: `work/workflow-core--normal-entry-reliability`

Approved package commit: `314b28289ee92d4115396fd3c486a4100741692f`

Implementation qualification commit:
`0e6c134fef60cd9c22895dba42d7823e01644793`

Final production candidate commit:
`671eb532e0ec949dc7889427379a1113cf7a6ea9`

Branch HEADs after this candidate are not product candidates when they only add
Final Critic closure evidence or the explicitly bounded maintenance metadata
correction described below.

The Final Critic second-round closure also includes one post-candidate
maintenance metadata correction in `docs/plugin-todos/workflow-core.md`:
the primary TODO status is normalized from the illegal composite
`PROMOTED / RELEASED_IN_5.4.1` to canonical `PROMOTED`. The release fact remains
recorded in that TODO's `release evidence` field and in the version/changelog
metadata. This correction is not a new production candidate.

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

Allowed post-candidate closure metadata correction:

- `docs/plugin-todos/workflow-core.md`: canonical TODO status normalization
  only. This does not change production workflow-core behavior, generated
  payload, version metadata, or release behavior.
