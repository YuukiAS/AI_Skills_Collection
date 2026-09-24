# Codex Executor Repair Prompt — ai-skills-core machine update orchestration

Repository:

`YuukiAS/AI_Skills_Collection`

Exact task branch:

`reviewed/ai-skills-core--machine-update-orchestration`

Pre-amendment remote task tip observed by Planner:

`11a25a714efb0e22119db4c67df7b5e1db08e299`

This is the same task. Do not create a successor. Do not redesign the Critic-PASSed V2.1 architecture.

## 0. First: synchronize identity, not scope

Before editing:

1. `git fetch origin main` and fetch/verify the exact reviewed task branch using the repository's allowed/canonical command shape.
2. Verify:
   - repo origin is `YuukiAS/AI_Skills_Collection`;
   - current worktree is the authorized task worktree for `reviewed/ai-skills-core--machine-update-orchestration`;
   - remote task tip contains the Planner recovery amendment and Bridge snapshot files listed below;
   - no user-owned dirty overlap blocks the exact repair paths.
3. Do not rebase/reset/stash/clean/force.
4. If remote task tip advanced only by this Planner amendment/prompt, consume it normally. If it contains unrelated production changes after the amendment, inspect before editing and stop only for real overlap/semantic conflict.

Read first:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `results/ai-skills-core--machine-update-orchestration/IMPLEMENTATION_REVIEW_RECOVERY_AMENDMENT.md`
- `results/ai-skills-core--machine-update-orchestration/BRIDGE_REVALIDATION_SNAPSHOT.md`
- current Reviewer/evidence/handoff files already named by the task.

## 1. Scope

Repair **only**:

- IR-B001;
- IR-B002;
- IR-B003.

Do not reopen V2.1 architecture.

Do not create a successor task.

Do not rename skills.

Do not add Route D.

Do not add daemon/watcher/database/ledger/machine registry/state machine/Bridge updater engine/duplicated Bridge release policy.

No paid API.

No automation.

Do not execute G2 yet.

Do not advance the Bridge `release` ref.

Do not modify Bridge runtime source.

Do not force/rebase/reset/stash/clean.

## 2. Bridge revalidation: once per repair round

At the start of repair, do **one** bounded Bridge revalidation against the real repo:

`YuukiAS/GPT_Codex_AI_Bridge_Kit`

Read only what G3 needs:

- latest `main`;
- current `release` ref;
- `AGENTS.md`;
- `pyproject.toml`;
- `ai_bridge_kit/__init__.py`;
- `CHANGELOG.md`;
- necessary formal release closure evidence.

Verify the tracked snapshot:

`results/ai-skills-core--machine-update-orchestration/BRIDGE_REVALIDATION_SNAPSHOT.md`

If the observed state is still semantically equivalent, use that frozen snapshot for all repaired G3 evidence.

If values changed since the Planner snapshot, refresh the snapshot **once** before evidence execution, but only from real source. Do not pin AI_Skills behavior to the new values.

After snapshot freeze, do not chase later unrelated Bridge commits or newer versions.

Only re-evaluate if:

- AGENTS owner locator materially changes/disappears;
- release producer semantics change;
- formal release identity/version-source semantics change;
- canonical `ai-bridge` ownership/delegation changes;
- this task's actual Bridge production dependency overlaps the drift.

A new Bridge version/commit by itself is not a blocker and does not require another AI_Skills release.

## 3. IR-B001 — stable installation guidance

Repair `docs/INSTALLATION.md`:

- normal/stable Git Marketplace install -> `release`;
- CLI stable example -> `--ref release`;
- `main` -> clearly labeled explicit development/unreleased mode.

Keep README semantics aligned.

Add the smallest useful regression that fails if README and INSTALLATION disagree again about the stable ref.

Do not add schema/config/control-plane machinery.

## 4. IR-B002 — dynamic Bridge release-state discovery + real G3 evidence

Do not hard-code any current Bridge version/SHA into product behavior.

Repair the existing `bridge-kit-maintainer` / orchestrator references only as needed so the production candidate explicitly performs:

1. discover real Bridge repo/main;
2. discover current `refs/heads/release`;
3. read canonical version source;
4. read Bridge AGENTS owner locator;
5. identify the newest Bridge release commit/version that has sufficient real formal-closure evidence;
6. classify the relation:
   - `ALIGNED`
   - `LAGGING`
   - `AHEAD/INCONSISTENT`
   - `FORMAL_RELEASE_NOT_PROVABLE`
7. daily `update Bridge Kit` remains read-only with respect to `release`;
8. formal producer closure alone may advance `release`;
9. canonical Bridge runtime behavior remains delegated to `ai-bridge`.

Latest formal release **must not** be inferred from:

- newest main SHA;
- highest-looking version string alone;
- changelog heading alone;
- arbitrary docs/TODO/evidence drift.

It must be supported by the existing formal version/changelog/closure-evidence contract.

### Required G3 semantics

Prove on the repaired final candidate:

- Case A: release ref == latest formally closed release -> aligned/current.
- Case B: release ref behind latest formally closed release -> pending/incomplete formal distribution closure; never call the old ref “latest”.
- Case C: main newer with no proof of formal closure -> do not advance/treat as formal.
- Case D: release ref ahead/inconsistent/non-FF target -> fail closed.

For this review round, use the real Bridge snapshot as the actual real-world case. If it is still `LAGGING`, that is the real Case B input; do not “fix” Bridge release just to make the evidence green.

The G3 release-critical path must:

- begin from the real Bridge repo's normal formal-release maintenance entry;
- actually consume Bridge `AGENTS.md` owner locator;
- route to AI Skills Maintainer / `bridge-kit-maintainer`;
- record the exact final AI_Skills candidate SHA;
- record which candidate/plugin/owner path was consumed;
- preserve canonical `ai-bridge` ownership.

A deterministic locator string test is allowed only as supporting regression; it cannot be the G3 PASS by itself.

### Replay state preparation

Regenerate:

`results/ai-skills-core--machine-update-orchestration/candidate_replay/public_machine_state.md`

from the frozen `BRIDGE_REVALIDATION_SNAPSHOT`.

Do not leave a hand-written timeless statement such as “Bridge current formal release = 0.8.5/0.9.1”.

The public-safe note may record the snapshot's observed values, but must label them as snapshot evidence and point to the snapshot relation/classification.

Because IR-B002 changes production source/reference semantics, rerun fresh candidate replay on the repaired exact final candidate.

Do not advance Bridge release in this repair.

## 5. IR-B003 — remove proxy behavior from G4/G5 fixture runner

Current `run_g4_g5_fixtures.py` cannot remain release-critical evidence while it directly:

- replaces the managed block itself;
- fabricates `UPDATED_RELOAD_REQUIRED`, `REPO_OWNED_CONFLICT`, `HUMAN_ONLY`, `PARTIAL_UPDATE`;
- simulates Marketplace restoration itself.

Refactor the harness so it owns only:

- fixture setup/reset;
- bounded failure injection;
- before/after hashing and Git state capture;
- expected-invariant assertions;
- evidence collation.

It must not implement the behavior under test.

The actual actions and semantic result must come from the exact final candidate and the canonical production-owned owner path selected by it.

Reuse existing mechanisms:

- committed candidate plugin replay/fresh Codex path;
- existing AI_Skills manifest/update path for AI-managed consumers;
- official Codex Marketplace/plugin operations for Marketplace semantics where required;
- canonical owner delegation already frozen in V2.1.

Do not create a second updater/recovery engine merely for tests.

### G4 final-candidate direct evidence

Use only task-owned fixture repos under the already approved private fixture root.

Prove:

1. stale managed consumer -> actual candidate/owner path updates it;
2. unaffected repo -> actual candidate/owner path no-op;
3. unmanaged apparent conflict -> actual candidate returns `REPO_OWNED_CONFLICT`, unowned file hash unchanged;
4. dirty non-overlap -> actual candidate safely proceeds, unrelated dirty hash preserved;
5. dirty overlap -> actual candidate emits one bounded Human Gate, overlapping user file unchanged.

### G5 final-candidate / production-owner evidence

Prove:

- bounded failure after an earlier safe step;
- actual returned `PARTIAL_UPDATE`;
- exact legacy source restoration through the production-owned recovery path;
- fresh-discovery rerun convergence;
- unrelated project-owned content unchanged.

Record for every release-critical case:

- exact final candidate SHA;
- candidate/plugin/owner path consumed;
- actual returned state;
- before/after hashes;
- failure injection point;
- same-final-candidate identity.

If the fixture harness must invoke the candidate/canonical owner as a subprocess, that is acceptable; the harness still must not contain the business logic or manufacture the result.

Do not use unrelated real user repositories.

## 6. G2 stays waiting

Do not perform before repaired Independent Reviewer PASS:

- AI_Skills formal promotion;
- AI_Skills `release` fast-forward;
- real Marketplace `main -> release` migration;
- production ai-skills-core 0.5 reinstall;
- released fresh-session smoke.

G2 remains:

`SEQUENCED WAITING`

Do not change `POST_REVIEW_PROMOTION_G2_RUNBOOK.md` semantics unless a purely mechanical locator correction is required by the repaired final candidate.

## 7. Version

Do not bump again.

Keep task candidate:

- AI_Skills repository `5.2.0`;
- `ai-skills-core 0.5`;
- workflow-core/domain plugins unchanged.

Bridge version is discovered evidence, not an AI_Skills dependency and not modified by this task.

## 8. Validation after repair

After source repair:

1. regenerate the canonical generated layer;
2. run source/generated parity/Marketplace build checks;
3. run focused Maintainer/install/release regressions;
4. run the required full repository test suite;
5. freeze one exact repaired final candidate;
6. rerun G1 as required because candidate identity changed;
7. run repaired G3 against the frozen Bridge snapshot;
8. run repaired candidate-direct G4/G5 evidence;
9. verify no unrelated real project was mutated;
10. update:
   - `candidate_replay/CANDIDATE_REPLAY_EVIDENCE.md`
   - `candidate_replay/public_machine_state.md`
   - `fixture_execution/G4_G5_FIXTURE_EVIDENCE.md`
   - `fixture_execution/g4_g5_fixture_evidence.json`
   - `IMPLEMENTATION_EVIDENCE.md`
   - `COMPLETION_AUDIT.md`
   - `REVIEWER_HANDOFF.md`
   - Independent Reviewer prompt/candidate locators if candidate SHA changed.

All release-critical G1/G3/G4/G5 evidence must bind to the same repaired final candidate.

Do not claim G2 PASS.

## 9. Commit / push / handoff

Commit only the bounded repair and evidence.

Push the exact task branch:

`reviewed/ai-skills-core--machine-update-orchestration`

Verify remote tip equals intended local HEAD.

Then stop at Independent Reviewer handoff.

Do not self-declare full V2.1 Goal PASS.

## 10. Stop conditions

Stop and return to Planner/Critic if this repair actually requires changing:

- V2.1 architecture;
- owner boundary;
- release producer contract;
- Bridge runtime behavior/source;
- authorization scope;
- Gate taxonomy;
- G2 sequencing;
- recovery semantics.

Do not silently expand scope to chase Bridge latest.

NEXT_HANDOFF after successful repair:

`INDEPENDENT_REVIEWER`
