# 057 Lite Versioning Default — Planner Amendment

- Task key: `057_repo_agents_hygiene`
- Date: 2026-09-17
- Status: `DRAFT_FOR_CRITIC_REVIEW`
- Relationship: bounded user-requested amendment to the already-approved 057 v2 design; it does not reopen the AGENTS-hygiene architecture.

## 1. User requirement

Future repositories using Bridge Kit Lite must not invent ad-hoc version-number conventions. The generic default belongs in the Lite execution authority (`templates/prompts/AGENT_RULES.md`), not in each root `AGENTS.md` copy.

The root AGENTS scaffold should only point to the Lite rules and leave any repository-specific override in the repository's own versioning contract.

## 2. Default versioning contract

When a repository already has an explicit, current, repository-local versioning policy, that policy wins. Examples include an explicit `docs/VERSIONING.md`, a frozen release contract, or another clearly canonical project rule. The Lite rule is the fallback for repositories that do not yet have such a policy.

For a repository with no explicit local policy, use a three-part formal version:

`MAJOR.MINOR.PATCH`

Default meaning:

- `PATCH`: backward-compatible bug fix, polish, reliability/performance correction, or other compatible repair that changes the user-consumable runtime/release candidate without adding a new product capability.
- `MINOR`: backward-compatible user-visible capability or substantial compatible feature stage.
- `MAJOR`: incompatible public/product contract change, migration, removed/renamed public entry, or another change that requires existing users/integrations to adapt. A MAJOR bump requires explicit Planner/user approval; an agent must not decide it merely because a diff is large.

For initial development, `0.y.z` is allowed. Moving to `1.0.0` is an explicit stability/default-use decision, not an automatic consequence of enough commits/tests.

This follows the ordinary SemVer meaning of MAJOR/MINOR/PATCH while adding a stricter local policy for prerelease labels.

## 3. Prerelease labels are opt-in, not default

Do not invent `alpha`, `beta`, `rc`, `preview`, date suffixes, or other prerelease labels merely because the software is unfinished or a branch is experimental.

A prerelease suffix is allowed only when:

1. the current repository has an explicit approved prerelease lifecycle; or
2. the current user/frozen task explicitly authorizes that prerelease scheme.

Without such authority, use the plain repository versioning policy. Do not silently introduce or continue a suffix ladder such as `alpha.1 -> alpha.2 -> beta.1 -> rc.1`.

If a repository already has an approved prerelease history, 057 does not rewrite it. The later all-repo adaptation round should inventory and reconcile each active repository deliberately.

## 4. Release identity rules

- Do not reuse one formal version for two different user-consumable runtime candidates. If behavior changes after a version has already been handed to the user as a candidate/release, the next candidate must receive a new version under the applicable policy.
- Docs/TODO/test-only changes that do not alter a user-consumable release normally do not require a version bump.
- Intermediate implementation commits may remain unreleased; version bump occurs when forming the next actual candidate/release according to the repo contract.
- A commit SHA, build label, branch name, date, or internal diagnostic label may supplement identity but never substitutes for the formal version when a formal version is required.
- Each repo should identify one canonical version source; derived manifests/UI/package metadata must agree with it before release-ready status.
- A release/version bump must be accompanied by the repository's normal changelog/release-note update when such a file exists.

## 5. Precedence and compatibility

This Lite default is deliberately not a universal forced migration.

Precedence:

1. current user/frozen task requirement;
2. explicit current repository-local versioning policy;
3. Lite default in `prompts/AGENT_RULES.md`.

Therefore existing intentional exceptions remain valid, including repositories whose approved product contract uses another version form. The generic Lite policy must not silently rewrite those histories.

## 6. 057 implementation impact

If Critic approves this amendment, 057 v0.2 may additionally modify Bridge Kit's canonical `templates/prompts/AGENT_RULES.md` to add the concise fallback versioning contract above.

It must not copy the same contract into `templates/repo/AGENTS_TEMPLATE.md`. The root scaffold should contain only a short Version/Release section/locator that tells maintainers to define any project-specific override and otherwise follow `prompts/AGENT_RULES.md`.

No new H10 is created:

- H7 fresh normal-entry init verifies the generated `prompts/AGENT_RULES.md` includes the approved Lite fallback and the fresh root points to it;
- H8 continues to protect existing project-owned root AGENTS content;
- H9 verifies root does not duplicate the Lite versioning/default execution rules.

Bridge Kit `0.8.2 -> 0.8.3` remains a compatible PATCH candidate for the combined scaffold + Lite-rule improvement, subject to the same full 057 release gates.

## 7. Future all-repo adaptation

After 057 and 056 are both integrated, the user wants a separate complete adaptation of all currently active repositories. That later round should inventory, per repo:

- installed Bridge/Lite identity;
- root/delegated AGENTS structure;
- versioning authority/current version/changelog parity;
- whether a repo-local versioning override intentionally differs from the Lite default;
- whether any historical alpha/beta/rc convention should be retained, normalized, or retired;
- whether the repo has consumed the final 056 delivery discipline.

That adaptation is not part of 057 execution and must receive its own Planner/Critic scope before mutating additional repositories.

## 8. External basis

Semantic Versioning 2.0.0 defines the conventional `MAJOR.MINOR.PATCH` meaning and treats prerelease identifiers as optional extensions. 057 adopts those numeric semantics but intentionally makes prerelease labels opt-in under this user's repository governance, rather than automatic.

`NEXT_HANDOFF = CRITIC`
