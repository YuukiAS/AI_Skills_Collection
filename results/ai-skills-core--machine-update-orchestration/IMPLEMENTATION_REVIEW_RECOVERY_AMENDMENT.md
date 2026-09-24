# IMPLEMENTATION_REVIEW_RECOVERY_AMENDMENT

Task: `ai-skills-core--machine-update-orchestration`  
Stage: `INDEPENDENT_IMPLEMENTATION_REVIEW_REVISE`  
Date: 2026-09-24  
Frozen architecture authority: Critic-PASSed V2.1 package  
Task branch before this amendment: `11a25a714efb0e22119db4c67df7b5e1db08e299`

This is a minimal implementation-review recovery amendment. It does not reopen V2.1 architecture, scope, Gate taxonomy, authorization, version design, or recovery semantics.

## Reviewer finding disposition

### IR-B001 — ACCEPT

Problem: stable install guidance drifted. README uses `release`, while `docs/INSTALLATION.md` still presents `main` as the normal Marketplace install ref.

Repair boundary:

- normal/stable Marketplace installation uses `release`;
- `main` is documented only as explicit development/unreleased mode;
- add one minimal consistency regression preventing README / INSTALLATION stable-ref drift;
- no new schema, config source, control plane, version bump, or architecture change.

### IR-B002 — ACCEPT / reframed as dynamic release-state discovery + production-consumption evidence

Do not bind this AI_Skills release or capability to a fixed Bridge version/SHA.

The user-visible capability is:

`AI Skills Maintainer / bridge-kit-maintainer`

dynamically discovers from the real Bridge source:

- current `main`;
- current `release` ref;
- current version source;
- latest Bridge release commit/version that is actually provable as formally closed;
- Bridge `AGENTS.md` owner locator;
- the relation among main, latest formal release, and release ref.

The frozen evidence baseline for this repair is:

`results/ai-skills-core--machine-update-orchestration/BRIDGE_REVALIDATION_SNAPSHOT.md`

Current snapshot classification is `LAGGING`: the observed Bridge `release` ref is older than the latest formally closed release proven by Bridge closure evidence.

That concrete Bridge version is evidence only, not an AI_Skills dependency.

Required G3 semantics remain within the existing Gate:

- Case A: release ref equals latest provable formal release -> aligned/current;
- Case B: release ref behind latest provable formal release -> pending/incomplete formal distribution closure; never misreport the old ref as latest;
- Case C: main newer but newer commit lacks formal-closure evidence -> do not advance or treat it as formal merely because main/version is newer;
- Case D: release ref ahead/inconsistent or target is non-fast-forward -> fail closed.

Evidence requirements:

1. start from the real Bridge repository's normal formal-release maintenance entry;
2. actually consume the Bridge `AGENTS.md` owner locator;
3. route to AI Skills Maintainer / `bridge-kit-maintainer`;
4. derive latest formal release from real version + changelog + closure evidence, not highest SHA or version-string guess;
5. prove daily `update Bridge Kit` is read-only with respect to `release`;
6. prove only producer closure may advance `release`;
7. preserve canonical `ai-bridge` runtime ownership/delegation;
8. do not advance the real Bridge `release` ref in this pre-review repair.

The prior `candidate_replay/public_machine_state.md` must no longer hard-code one Bridge version as timeless truth. Replay preparation must regenerate public-safe state from the frozen `BRIDGE_REVALIDATION_SNAPSHOT`.

Snapshot drift rule: after one bounded Bridge revalidation at repair start, do not chase later unrelated Bridge commits/versions. Re-evaluate only on the material drift conditions recorded in the snapshot file.

### IR-B003 — ACCEPT

The existing G4/G5 fixture runner is a proxy because it directly performs the behavior it claims to validate: it replaces managed blocks, fabricates result states, and simulates source restoration itself.

Repair boundary:

Keep task-owned fixture repositories, but change the harness ownership:

Fixture/setup layer may only:

- create/reset task-owned fixtures;
- establish controlled dirty/conflict/failure conditions;
- record before/after hashes and state;
- inject a bounded failure;
- assert expected invariants after the real path runs.

The fixture layer must **not** implement the product behavior or manufacture semantic results.

The real behavior must be executed by the exact final candidate and the actual production-owned owner path selected by that candidate. Reuse existing candidate replay / AI_Skills managed-update / official Codex Marketplace / canonical owner mechanisms as applicable; do not create a second update engine.

G4 candidate-direct evidence must cover:

- stale managed consumer -> candidate/owner path performs update;
- unaffected repo -> candidate/owner path no-op;
- unmanaged conflict -> candidate returns `REPO_OWNED_CONFLICT` and leaves unowned text unchanged;
- dirty non-overlap -> candidate safely continues;
- dirty overlap -> candidate produces exactly one bounded Human Gate.

G5 candidate/production-owner evidence must cover:

- bounded failure after an earlier safe step;
- truthful `PARTIAL_UPDATE`;
- exact legacy source restoration through the production-owned recovery path;
- fresh-discovery rerun convergence;
- unrelated project-owned content unchanged.

Release-critical evidence must record:

- exact candidate SHA;
- actual candidate/plugin/owner path consumed;
- actual returned state;
- before/after hashes;
- failure injection point;
- same-final-candidate identity.

Do not use unrelated real user repositories.

## Architecture / versions remain frozen

Unchanged:

- public plugin: `AI Skills Maintainer`;
- slug: `ai-skills-core`;
- internal capabilities: `machine-update-orchestrator`, `ai-skills-repository-maintainer`, `project-skill-installer`, `bridge-kit-maintainer`, `skill-library-analysis`;
- exactly Route A / Route B / Route C;
- `sync this machine` is composition, not Route D;
- Bridge runtime implementation stays in Bridge Kit / canonical `ai-bridge`;
- no daemon/watcher/database/ledger/machine registry/state machine/fourth route;
- repository candidate version remains `5.2.0`;
- `ai-skills-core` remains `0.5`;
- workflow-core/domain plugins: NO_BUMP;
- this task does not choose or bump Bridge version.

No version bump is introduced by IR-B001/2/3 repair.

## G2 sequencing remains unchanged

G2 remains:

`SEQUENCED WAITING`

Before the Independent Reviewer passes the repaired pre-release candidate, do not perform:

- AI_Skills formal promotion;
- AI_Skills `release` fast-forward;
- real Marketplace `main -> release` migration;
- production `ai-skills-core 0.5` reinstall;
- released fresh-session smoke.

## Exact repair scope

Executor may repair only the surfaces necessary to close IR-B001/2/3, including:

- `docs/INSTALLATION.md`;
- minimal installation-consistency regression;
- `machine-update-orchestrator` / `bridge-kit-maintainer` source references needed for dynamic Bridge release-state discovery;
- their generated ai-skills-core payload through the canonical generator;
- relevant focused tests;
- candidate replay preparation/evidence so Bridge state comes from the frozen snapshot;
- task-owned G4/G5 fixture setup/runner/evidence so product behavior is executed by final candidate / canonical owner paths;
- task evidence, completion audit and Reviewer handoff.

Do not broaden into unrelated plugin/domain work.

## Required revalidation after repair

Because IR-B002/IR-B003 can change production skill/reference behavior, freeze one new exact final candidate after repair and bind release-critical evidence to it.

At minimum rerun:

- source/generated Marketplace parity/build validation;
- affected focused tests;
- required full regression under the existing task contract;
- G1 fresh candidate normal-entry replay if the final candidate identity changed;
- repaired G3 real snapshot/producer-distribution evidence;
- repaired G4/G5 candidate-direct fixture evidence.

Update:

- `IMPLEMENTATION_EVIDENCE.md`;
- `COMPLETION_AUDIT.md`;
- `REVIEWER_HANDOFF.md`;
- candidate/fixture evidence artifacts as appropriate.

Then commit and push the exact task branch and hand it back to the Independent Reviewer.

Do not self-declare full Goal PASS. G2 still remains sequenced after Reviewer PASS.

## Stop conditions

Stop and return to Planner/Critic rather than expanding scope if repair requires a substantive change to any of:

- V2.1 architecture;
- owner boundary;
- release producer contract;
- Bridge runtime behavior/source;
- authorization scope;
- Gate taxonomy;
- G2 sequencing;
- recovery semantics.

Also stop if real source shows the Bridge formal release state cannot be proven under the existing version/changelog/closure-evidence contract without inventing a new release authority.

No paid API. No automation. No Bridge `release` advancement in this repair.
