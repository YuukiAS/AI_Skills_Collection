# AI Skills Maintainer machine update orchestration — Planner response to Critic V2

Date: 2026-09-23  
Task key: `ai-skills-core--machine-update-orchestration`  
V1 review result: `REVISE`  
V1 review source: user-supplied Critic result for package commit `a3dec83de651480ac46179ddae3b553c8f41d134`

## Current source revalidation

AI_Skills_Collection latest main was re-read at `338add2d7ac002a0201a924be3a0ec2818b777c7`.

The commits after the V1 Critic package only add unrelated design/review artifacts and plugin TODO entries for other tasks. They do not modify:

- the V1 machine-update package;
- `AGENTS.md`;
- Planner/Critic/Gate/version contracts;
- `scripts/codex_marketplace_config.json`;
- current `ai-skills-core 0.4`;
- current `workflow-core 0.3`;
- repository `VERSION=5.0.7`.

Bridge latest main was re-read at `b76a7da0fdbb4f92205b0b168241c084c1489c6f`. It remains runtime/package version `0.8.5`; commits after formal release commit `d27259d6706dee951dc0c0ede8c9b03c65f55ca3` are documentation/TODO changes only. This further confirms that `main` can legitimately move beyond the current formal release.

Current OpenAI Codex plugin/Marketplace source was also rechecked. Git Marketplace supports `--ref`, `list`, `upgrade`, and `remove`; plugin management exposes `plugin add` and `plugin list --json --available`. OpenAI's update guidance still uses reinstall plus a new thread/session as the safe loading boundary. The current Marketplace removal implementation also fails closed if the same marketplace is owned by another enabled configuration layer.

## Finding dispositions

### MU-B001 — ACCEPT

The Critic is correct that V1 did not completely define the one-time transition from an existing `main`-pinned Marketplace to the future formal `release` channel.

V2 adds a bounded bootstrap contract:

1. discover the actual Marketplace name, source URL, ref, sparse paths, config layer and installed plugin set;
2. require the existing source to match the expected AI_Skills Git source at `main`;
3. verify the remote `release` ref and generated Marketplace payload are reachable before removing anything;
4. preserve exact source metadata and installed/enabled plugin identity for recovery;
5. when the source is user-owned and mutable, replace the configured source with the same Marketplace identity at `release` using official Codex commands;
6. reinstall only the capability-bearing Maintainer and the explicitly requested target unless another installed plugin lost its prior installed state because of the source migration;
7. if replacement fails after removal, restore the exact previous `main` source from the captured metadata and report `PARTIAL_UPDATE`;
8. when the source is provided by a non-user/system/config layer that the current authority cannot mutate, fail closed with the exact owning layer instead of editing config directly;
9. require a fresh Codex session before claiming the new Maintainer is active.

The bootstrap is explicitly a one-time rollout exception for identities still on `ai-skills-core 0.4`. From the first capability-bearing Maintainer release onward, short Maintainer self-update becomes the normal contract.

G2 is expanded to start from a real legacy `0.4 + main-pinned Marketplace` state.

### MU-B002 — PARTIAL_ACCEPT + REBUT on contract location

The Critic is correct that a moving `release` ref needs a durable producer/lifecycle contract. V1 only defined the consumer side.

However, the requirement to duplicate the full producer contract into both repositories is no longer the right ownership after the user's current instruction:

> AI Skills Maintainer should also maintain Bridge Kit version/adaptation, preferably through a skill inside `ai-skills-core`, without making Bridge Kit itself heavier.

V2 therefore centralizes the release-channel producer contract in AI Skills Maintainer rather than creating two independent release mechanisms.

The internal owners become:

- `ai-skills-repository-maintainer`: AI_Skills repository/plugin release maintenance;
- new `bridge-kit-maintainer`: Bridge Kit distribution/version/source maintenance;
- new `machine-update-orchestrator`: short user request, discovery, route composition and reporting.

The canonical release-channel contract lives once in the Maintainer runtime/reference layer and governs both repositories:

- only a formally closed release may advance `release`;
- the updater used for ordinary machine sync is read-only with respect to `release`;
- advancement is fast-forward-only;
- the target must be the exact formally closed release commit;
- the remote ref must be verified after advancement;
- later docs/evidence/main commits do not move it;
- non-fast-forward or inconsistent state fails closed.

For future Bridge formal release closure, `bridge-kit-maintainer` is the distribution/release owner that verifies Bridge's own version/changelog/closure evidence and advances the Bridge `release` ref. Bridge Kit remains the owner of Bridge runtime implementation and validation commands. No Host/Review/Lite generation logic moves into AI_Skills.

This is not an argument against any Bridge-side locator at all. If implementation evidence shows that a short pointer in Bridge's existing maintainer/release guidance is needed so a Bridge-only release task knows to call AI Skills Maintainer, V2 permits a minimal pointer. It rejects duplicating a second full release-channel contract or adding release machinery to Bridge.

This is the only substantive rebuttal to the Critic findings. The need for a producer contract itself is accepted.

### MU-B003 — ACCEPT

V1 used the phrase “release delta explicitly requires” without defining the authoritative source.

V2 defines the formal release entry's existing root `CHANGELOG.md` section as the authoritative update-impact source.

From the first capability-bearing Maintainer release onward, a formal release must use a small Markdown subsection when cross-layer impact exists:

`### Update impact`

It contains only:

- required companion component/version, if any;
- required managed-consumer refresh class, if any.

Absence of `Update impact` means isolated by default.

Authority rules:

1. exact formal `release` ref;
2. that ref's root release changelog entry;
3. component/plugin changelog only for detail inside the root-declared scope;
4. arbitrary diffs, commit messages, TODOs or model inference may not enlarge mutation scope;
5. contradictory release metadata fails closed as `RELEASE_METADATA_INCONSISTENT`.

Bridge releases use Bridge's existing root changelog entry for Bridge-owned Host/consumer impact. A coordinated AI_Skills stack release may declare the Bridge companion in the AI_Skills root release entry.

Legacy 5.0.7 / Bridge 0.8.5 bootstrap remains a bounded compatibility exception backed by the existing 056 final closure; future releases use the new contract.

G1 and G3 are updated accordingly.

### MU-B004 — ACCEPT

V1 was too permissive when it allowed automatic rewriting of arbitrary repo-owned copied/generic rules or AGENTS overrides.

V2 restricts automatic mutation to ownership-proven managed surfaces:

- AI_Skills manifest-managed skills/profile installation and its exact managed block;
- Bridge canonical managed consumers/templates/blocks;
- exact migration targets explicitly named by the authoritative formal release contract with an ownership locator.

Unmarked project-authored `AGENTS.md`, copied rules, science/safety/privacy/Figma/design/deployment/device/server instructions are diagnosis-only.

If such text creates a genuine conflict, Maintainer reports `REPO_OWNED_CONFLICT` with the exact repo/path/reason and requests one bounded repo-owned decision or separate repo task. It does not rewrite the file.

G4 now requires an unmanaged apparently conflicting AGENTS file to remain byte-for-byte unchanged.

## Additional architecture amendment from the user

V2 adds one internal skill to `ai-skills-core`:

`bridge-kit-maintainer`

This is not a new top-level plugin and not a fourth mutation route.

Its responsibility is Bridge **maintenance/distribution**, not Bridge runtime implementation:

- discover active `ai-bridge` executable/runtime/source identity;
- resolve Bridge formal release/version;
- maintain the canonical Bridge checkout/version on the current machine when safe;
- refresh the editable package/entry point from the formal release;
- own Bridge `release` ref advancement during a future formal Bridge release closure;
- delegate Host/Lite/Review/Persistent Run/runtime mutations back to the canonical `ai-bridge` commands;
- verify runtime path/version after update.

It must not copy:

- Host Policy generation;
- Lite/Review/Control templates;
- Human Gate runtime;
- plugin replay implementation;
- Bridge state machines.

This produces a cleaner target model:

- adapt/install a skill/profile -> AI_Skills installer/managed manifest;
- update/refine an AI_Skills plugin/repository release -> AI Skills repository maintainer;
- update/adapt Bridge Kit version/distribution -> Bridge Kit maintainer;
- compose those targets for a machine update -> machine update orchestrator.

The public entry remains exactly **AI Skills Maintainer** and the compatibility slug remains `ai-skills-core`.

## Gate structure

The Critic's conclusion that G1–G5 are already distinct is accepted. V2 does not add G6/G7.

- G1 absorbs authoritative `Update impact` and isolated-by-default routing.
- G2 absorbs the real legacy Marketplace bootstrap and self-update.
- G3 covers Bridge Kit maintainer distribution/version handling plus delegation to canonical Bridge runtime commands.
- G4 narrows mutation to managed surfaces and adds the unmanaged-conflict byte-for-byte negative case.
- G5 remains failure/recovery/Human Gate/should-not-change.

## Version position

No change from V1:

- repository planned release: `5.0.7 -> 5.1.0` MINOR;
- `ai-skills-core: 0.4 -> 0.5`;
- `workflow-core`: NO_BUMP;
- domain plugins: NO_BUMP;
- Bridge Kit: NO_BUMP if only its release-channel/distribution maintenance is centralized in ai-skills-core and Bridge production runtime behavior is unchanged.

If future implementation actually changes Bridge production behavior, that is outside this frozen V2 and must return to Planner/Critic for a Bridge version decision.
