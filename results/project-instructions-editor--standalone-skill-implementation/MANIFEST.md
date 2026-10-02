# Evidence manifest

## Candidate

`FINAL_CANDIDATE_COMMIT=227bb9dbc5e35d546822d27d7985d4d81c371d1c`

Candidate commit message:

`Add project instructions editor standalone skill`

Candidate base:

`98721a20 docs: approve project instructions editor implementation package v0.2`

## Deterministic Validation

All commands were run from the task worktree after implementing the candidate.

```text
python scripts/skills.py registry --write
result: PASS, wrote registry.json with 155 skills

python scripts/skills.py catalog --write
result: PASS, wrote docs/SKILL_CATALOG.md and 16 domain pages

python scripts/audit_skill_provenance.py --write
result: PASS

python scripts/skills.py validate
result: PASS, validated 155 active skills, 18 profiles, templates, and trigger eval scaffolds

python scripts/skills.py audit --all
result: PASS, with profile/domain budget advice only

python scripts/build_codex_marketplace.py --write --validate --check --path-report
result: PASS, plugins=10 active_skills=29 over_budget=0

python scripts/icon_audit.py --scope active-skills --check
result: PASS

python -m unittest tests.test_project_instructions_editor_contract
result: PASS, 6 tests

python -m unittest tests.test_standalone_skill_baselines
result: PASS, 4 tests

python -m unittest tests.test_central_plugin_icon_assets
result: PASS, 4 tests

python -m unittest discover -s tests
result: PASS, 323 tests
```

## Candidate Install From C

Install command:

```text
python scripts/skills.py install --target repo --project /tmp/project-instructions-editor-gates/workspace --skill core/codex-system/project-instructions-editor --mode copy --write-agents-md --json
```

Install facts:

- `collection_commit=227bb9dbc5e35d546822d27d7985d4d81c371d1c`
- `project_path=/tmp/project-instructions-editor-gates/workspace`
- `skills_root=/tmp/project-instructions-editor-gates/workspace/.agents/skills`
- installed skill: `.agents/skills/core-codex-system-project-instructions-editor`

Installed skill files matched the candidate commit file list.

Per-file SHA-256:

- `SKILL.md`: `03e281319a96e7cbf645f8e4acb8b19eb0e3349dbeff4b85e509e49bc1aeadd8`
- `agents/openai.yaml`: `ff19811ea5b995a8223702e8f1df97a1764276a395a088514f11f65a802540f3`
- `assets/app-facing.svg`: `ea22de6450795051f7c21872aa2e9ea531b48f2f034c83e4d5049d067ba08995`
- `evals/trigger_queries.json`: `ffb509aed8901f0f2d67e12bb8cb11fab367803a77ca4534097c0cedb65e9c18`
- `references/editor-contract.md`: `405eca267b98bd51bebe752de71164df7881ea9618dc4d176c0fd0ed4a0f213a`

## Portable Package

Archive command:

```text
git archive --format=zip -o private/exports/project-instructions-editor-v0.1.zip 227bb9dbc5e35d546822d27d7985d4d81c371d1c skills/core/codex-system/project-instructions-editor
```

Archive path:

`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation/private/exports/project-instructions-editor-v0.1.zip`

Archive SHA-256:

`534240c780c282536bdd6badcc2e39ba21a36518cf799abd6e6b7b9af04baf2f`

`private/exports/` remains ignored and untracked.

## Gate Summary

- G1 positive fresh session: `01a0fbc5-47c1-74a2-a857-b7cc31565a12`, PASS.
- G1 near-miss fresh session: `01a0fbc5-c809-75d1-9615-f08a79696223`, PASS.
- G2 fresh session: `01a0fbc6-1b43-7ec3-85e7-1459228f008b`, PASS.
- G3 fresh session: `01a0fbc6-bc02-7501-ae9e-99d124423028`, PASS.
- G4 packet fresh session: `01a0fbc8-e4f3-7910-b54d-39a29ac5ca30`, ready for independent review; Executor does not claim PASS.
