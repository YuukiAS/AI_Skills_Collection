# PIE 0.1 Historical-Good Semantic Spine Repair Result

Date: 2026-10-07

## Source Identity

```text
FINAL_SOURCE_COMMIT=b296fe64437f6a0f15a9d91c3881d2cb54db0ec0
PIE_SKILL_VERSION=0.1
```

This repair updates only the Project Instructions Editor production contract,
its editor-contract reference, focused structural regression coverage, and
normal generated registry/catalog timestamps.

## Historical Reads

Read directly:

- C6 `SKILL.md` at `6ddab9029bbd96a21d7e5bf0317f7674c66cd909`
- C6 `references/editor-contract.md` at `6ddab9029bbd96a21d7e5bf0317f7674c66cd909`
- `SERVER_VPS_R6_UNCOACHED_REGRESSION.md` from evidence commit `a708e5a94dcae29b7e491c4af73aafefe14df40c`
- `C6_IMPLEMENTATION_CRITIC_REVIEW.md` from review commit `f099d147ff4f69bb2899a93b8ff057446800e6e0`
- preserved C7/C9/C10/C11 failure summaries on the closure branch

The two named C6 evidence files were not present at the C6 source commit itself;
they were located and read from their later evidence/review commits.

## Repair Summary

```text
SEMANTIC_SPINE_REPAIR=YES
SCOPE_DOMINANCE=YES
DYNAMIC_SET_ABSTRACTION=YES
C11_READER_LAYER_FAILURE_PRESERVED=YES
```

Implemented behavior:

- atomic durable meanings are clustered into semantic families before final
  Project-setting text is drafted;
- heading names/count/order, source labels, source grouping, and duplicated
  rationale are not protected semantics by default;
- broad authorization, safety, privacy, evidence, completion, and fail-closed
  boundaries cannot be replaced by narrower overlapping special cases;
- mutable canonical-source-owned sets are represented as currently supported
  items defined by their source plus a lookup bridge, not frozen member lists;
- normal response rules with the same trigger and user consequence are merged
  into one primary home while genuinely distinct closure/report triggers remain
  separate;
- ordinary Chinese-facing concepts are realized before family drafting without
  token scans, blacklists, translation dictionaries, language ratios, or fixed
  templates.

## Structural Tests

```text
python -m unittest tests.test_project_instructions_editor_contract
PASS: Ran 9 tests

python -m unittest tests.test_standalone_skill_baselines
PASS: Ran 4 tests

python scripts/skills.py validate
PASS: validated 155 active skills, 18 profiles, templates, and trigger eval scaffolds

python scripts/skills.py audit --all
PASS

python scripts/build_codex_marketplace.py --write --validate --check --path-report
PASS

git diff --check
PASS
```

Added fixture:

```text
tests/fixtures/project_instructions_editor/semantic_spine_repair.json
```

The fixture is public-safe and generic. It does not hard-code the historical
Server/VPS domain, platform names, a fixed nine-section layout, banned English
terms, or an English-percentage score.

## Full Unittest Note

An extra non-required `python -m unittest discover -s tests` run was attempted
and was not used as this repair's pass/fail gate. It failed for reasons outside
this PIE repair scope:

- sandbox write denial for generated palette / presentation audit artifacts
  under the exact sibling worktree;
- existing unrelated `presentations` / `research-writing` generated-payload
  drift reported by marketplace tests.

No unrelated central plugin source or runtime behavior was repaired in this
task.

## Development Replay

```text
DEVELOPMENT_REPLAY=NOT_RUN_NO_EXISTING_AUTHORIZED_STANDALONE_RUNTIME_REPLAY_HARNESS
```

Repository search found central plugin replay and historical raw `codex exec`
evidence, but no current, task-authorized standalone PIE runtime replay harness
for this bounded repair. Static/contract tests are therefore not described as
normal-entry behavior PASS. The next real behavior check remains the planned
Server+VPS ChatGPT Web fresh-thread acceptance.

## Wrapper Candidate

```text
WRAPPER_CANDIDATE=private/exports/project-instructions-editor--0.1-closure/project-instructions-editor-v0.1-wrapper-0.2.4-candidate.zip
WRAPPER_CANDIDATE_SHA256=1f70cd5fc1bd6b405eaabb303dcb3685552ec767285c4fb01ea9f82261614772
WRAPPER_MANIFEST=private/exports/project-instructions-editor--0.1-closure/project-instructions-editor-v0.1-wrapper-0.2.4-candidate.MANIFEST.json
WRAPPER_MANIFEST_SHA256=6c0e561286323d1cff0047097f9d3eac1bcd56a5164e54102befa2427932afdf
SKILL_TREE_GIT_SHA=294211fdd39c8b2cc1956b9c4f6822ede2c66188
WRAPPER_VERSION=0.2.4
SKILL_VERSION=0.1
```

The live ChatGPT wrapper was not mutated by this Codex run.

## Stop Point

```text
SERVER_VPS_ACCEPTANCE_READY=YES
READY_FOR_MAIN_RELEASE=NO
C11_READER_LAYER_FAILURE_PRESERVED=YES
```

Stop before real Server+VPS fresh-thread acceptance.
