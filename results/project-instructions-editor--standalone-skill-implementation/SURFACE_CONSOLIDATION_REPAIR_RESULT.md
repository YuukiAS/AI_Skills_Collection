# PIE 0.1 Surface Consolidation Repair Result

Date: 2026-10-07

## Final Source

```text
FINAL_SOURCE_COMMIT=4eb3c0422c4fe268a0039416574c26d471725eee
PIE_SKILL_VERSION=0.1
STRUCTURAL_CONSOLIDATION_REPAIR=YES
```

The repair keeps `FINAL_ROUTE=SIMPLE_FORMAL_CORE`. It does not add C12, Clear
Writing next-version behavior, sibling Skill chaining, MCP finalizer,
`OPENAI_API_KEY`, hosted services, token scoring, English ratios, blacklists,
translation tables, or fixed section templates.

## Source Changes

- Added durable semantic-map guidance before drafting complex replacements.
- Added explicit dispositions: direct Project rule, short locator bridge,
  source-only, task-only, another verified layer, and omit/no change.
- Added candidate expansion discipline: new or changed durable rules require
  current semantic support.
- Added final semantic coverage and redundancy review over the actual
  replacement text.
- Restored the narrow current-artifact language responsibility: Chinese Project
  replacements should digest ordinary source labels into natural Chinese while
  preserving exact identifiers, without claiming future cross-turn reader-layer
  enforcement.
- Normal user output should not expose internal preservation labels, semantic
  maps, disposition tables, invariant checklists, or coverage/redundancy review
  unless the user asks for audit evidence.

## Focused Tests

```text
FOCUSED_TESTS=PASS
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
python scripts/skills.py validate
python scripts/skills.py audit --all
git diff --check
```

Focused fixture:

```text
tests/fixtures/project_instructions_editor/surface_consolidation_repair.json
```

## Broad Validation

`python scripts/build_codex_marketplace.py --validate --check --path-report`
still fails with the pre-existing unrelated central-plugin generated drift:

```text
publication layer is not current (13 differences)
```

The reported paths are confined to `plugins/codex/plugins/presentations/**` and
`plugins/codex/plugins/research-writing/**`.

`python -m unittest discover -s tests` was rerun with worktree write access.
The write-access-only palette/gallery errors disappeared. Remaining failures are
the same unrelated central-plugin generated/TODO drift:

```text
tests.test_codex_marketplace.CodexMarketplaceTests.test_central_plugins_have_exactly_one_source_only_todo_inbox
tests.test_codex_marketplace.CodexMarketplaceTests.test_generated_layer_matches_source_config
tests.test_codex_marketplace.CodexMarketplaceTests.test_plugin_changelogs_match_marketplace_set_and_versions
tests.test_presentations.PresentationSharedTests.test_research_presentation_todo_consolidation_and_promotions
```

These failures are not repaired in this bounded PIE standalone Skill task.

## Wrapper Candidate

```text
WRAPPER_CANDIDATE=YES
WRAPPER_CANDIDATE_VERSION=0.2.3
WRAPPER_PACKAGE=private/exports/project-instructions-editor--0.1-closure/project-instructions-editor-v0.1-wrapper-0.2.3-candidate.zip
WRAPPER_PACKAGE_SHA256=52d37676402c9b42bfffdee28d2c66dd17cac38dfaf25b48d5ab38d666f2b590
WRAPPER_MANIFEST=private/exports/project-instructions-editor--0.1-closure/project-instructions-editor-v0.1-wrapper-0.2.3-candidate.MANIFEST.json
WRAPPER_MANIFEST_SHA256=68bc88cfe0b267831c7fa3397140966548ac842b35a01cbce5bfad5308ff9d5b
PIE_SKILL_TREE_GIT_SHA=76f71354c6168d95698ec550e55d31268c5e1052
```

The archive was generated from exact source commit
`4eb3c0422c4fe268a0039416574c26d471725eee`, not from a mutable worktree. It is
a ChatGPT Web `skills-only` wrapper candidate package; it does not mutate the
live ChatGPT wrapper by itself.

## Acceptance Boundary

```text
SERVER_VPS_ACCEPTANCE_READY=YES
C11_READER_LAYER_FAILURE_PRESERVED=YES
```

Stop before real Server+VPS fresh-thread acceptance. The next action is to
update the existing private/user `project-instructions-editor` ChatGPT Web
wrapper from the `0.2.3` candidate package and run one fresh-thread acceptance
for PIE 0.1 editor semantics. Future cross-turn natural-Chinese reader-layer
behavior remains out of PIE 0.1 scope and is not reclassified as PASS.
