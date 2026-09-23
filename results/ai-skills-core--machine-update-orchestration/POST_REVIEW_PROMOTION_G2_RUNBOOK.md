# Post-Review Promotion And G2 Runbook

Task key: `ai-skills-core--machine-update-orchestration`  
Status: `DRAFT_RUNBOOK_WAITING_FOR_REVIEWER_PASS`  
Prepared date: 2026-09-24

This runbook records the exact post-review sequence expected by Planner decision D2. It is not current authorization to promote, advance `release`, migrate Marketplace sources, reinstall production plugins, start automation, call paid APIs, or modify Bridge runtime source.

## Current State Before Reviewer

- Task branch: `reviewed/ai-skills-core--machine-update-orchestration`
- Current task branch tip when this runbook was prepared: `6b90e329e402c147661559639bc667b4e183da98`
- Product-surface candidate replayed by fresh child: `24f574ff20028fedaa3c5382594717cb28234184`
- AI_Skills `main`: `7b76e94ad29cf3bd8547026b942553068754d51f`
- AI_Skills `release`: `7b76e94ad29cf3bd8547026b942553068754d51f`
- Bridge `release`: `d27259d6706dee951dc0c0ede8c9b03c65f55ca3`
- Installed production `ai-skills-core@yuukias-ai-skills`: observed as `0.4` before G2.

Pre-release status:

- Source/generated implementation: complete on task branch.
- Deterministic validation: PASS, recorded in `COMPLETION_AUDIT.md`.
- G1/G3 candidate replay: PRE-RELEASE PASS.
- G4/G5 task-owned fixtures: PRE-RELEASE PASS.
- G2: not run, intentionally sequenced after Reviewer PASS and formal release.

## Preconditions To Start

Do not start this runbook unless all are true:

1. An independent Reviewer result is committed or otherwise durably recorded for this task.
2. The Reviewer result is `IMPLEMENTATION_REVIEW_PASS_FOR_PRE_RELEASE_PROMOTION` or a semantically equivalent PASS for the exact candidate.
3. Any Reviewer-noted conditions are either closed or explicitly non-blocking.
4. The exact candidate identity to promote is unambiguous.
5. AI_Skills remote identity and effective push destination still match `YuukiAS/AI_Skills_Collection`.
6. Bridge-side state still requires no Bridge runtime/source modification.
7. The current user has not revoked the no-paid/no-automation boundary.

If any precondition is false, stop and return to Planner/user with evidence.

## Formal Promotion Sequence

1. Re-fetch and verify current refs:
   - AI_Skills `origin/main`
   - AI_Skills task branch
   - AI_Skills `origin/release`
   - Bridge `origin/release` if Bridge evidence is referenced
2. Verify the task branch still contains the exact reviewed candidate and that no post-review source/generated changes were added without re-review.
3. Inspect working trees and dirty ownership. Do not reset, stash, restore or clean user work.
4. Integrate the accepted candidate into AI_Skills `main` using the repository-approved non-force strategy.
5. Re-run required release validation on the integrated formal candidate:
   - `python scripts/skills.py registry --write`
   - `python scripts/skills.py validate`
   - `python scripts/skills.py audit --all`
   - `python scripts/skills.py catalog --write`
   - `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
   - targeted Maintainer tests
   - `python -m unittest discover -s tests`
6. Verify version/release metadata:
   - repository version `5.2.0`
   - `ai-skills-core 0.5`
   - `workflow-core` no bump
   - domain plugins no bump
   - root `CHANGELOG.md` has the matching release section and `### Update impact` semantics
   - `docs/plugin-changelogs/ai-skills-core.md` matches the behavior change
7. Push `main` with a non-force ref update and verify remote `main` equals the intended integrated commit.
8. Fast-forward AI_Skills `release` to the exact formally closed `5.2.0` commit. Do not move `release` to a reviewed/task/evidence-only commit.
9. Verify remote `release` equals the intended formal commit.

## G2 Legacy Marketplace Migration

Only after AI_Skills `release` contains `ai-skills-core 0.5`:

1. Discover the current AI_Skills Marketplace source through official Codex commands and recorded metadata.
2. Record legacy source metadata before mutation:
   - Marketplace name
   - Git source URL
   - ref
   - sparse paths
   - owning config layer
   - installed/enabled plugin state
   - restoration data
3. Proceed only if:
   - source is `https://github.com/YuukiAS/AI_Skills_Collection.git`
   - ref is `main`
   - sparse paths match `.agents/plugins` and `plugins/codex/plugins`
   - source is user-owned/mutable
   - remote `release` is verified at the capability-bearing formal commit
4. Use only official Codex Marketplace/plugin commands.
5. Replace the legacy source with the same source at `release`.
6. If replacement fails after removing the legacy source, restore the exact captured old source, verify restoration, report `PARTIAL_UPDATE`, and stop.
7. Reinstall `ai-skills-core` and any requested target from the `release` Marketplace.
8. Verify installed `ai-skills-core@yuukias-ai-skills` is `0.5`.
9. Return `UPDATED_RELOAD_REQUIRED`; do not claim the current session hot-reloaded.

## Fresh Released Normal-Entry Smoke

After reload/fresh session:

1. Verify the loaded production plugin identity is `ai-skills-core@yuukias-ai-skills` version `0.5`.
2. Exercise normal released Maintainer entry with public-safe requests:
   - `update AI Skills`
   - `update Bridge Kit`
   - `sync this machine`
3. Verify behavior matches the frozen contract:
   - no user-supplied versions, commits, checkout paths, `CODEX_HOME`, inventories, templates or dependency lists required;
   - `update AI Skills` routes through Route A unless formal `### Update impact` declares Route B;
   - `update Bridge Kit` routes through `bridge-kit-maintainer` and canonical `ai-bridge` delegation;
   - `sync this machine` composes Route A/B/C and is not a fourth route;
   - formal scope expansion comes only from `release -> CHANGELOG.md -> ### Update impact`;
   - unmanaged project text remains untouched;
   - status vocabulary is truthful (`UPDATED`, `UPDATED_RELOAD_REQUIRED`, `ALREADY_CURRENT`, `PARTIAL_UPDATE`, `REPO_OWNED_CONFLICT`, `RELEASE_METADATA_INCONSISTENT`, etc.).
4. Record G2 evidence under `results/ai-skills-core--machine-update-orchestration/`.
5. Only after this smoke passes may the overall V2.1 G1-G5 closure be claimed.

## Forbidden During This Runbook

- No Terra, `/v1/responses`, paid API, or new provider call.
- No automation startup.
- No force push.
- No tag creation/deletion.
- No arbitrary branch creation/deletion/rename.
- No remote remap.
- No stash/reset/restore/clean of user work.
- No Bridge runtime source, Host Policy, Lite, Review, Control, Persistent Run or Human Gate implementation changes.
- No Bridge README, QUICKSTART or CHANGELOG edits for this task.
- No direct hand-editing of Codex config.
- No mutation of unrelated real project repositories or unowned project rules.
- No claiming full completion before G2 released production evidence exists.
