# Formal Release And Update Impact

Normal updates must use a stable formal release channel. The default stable target is the fast-forward-only Git branch `release` for both `YuukiAS/AI_Skills_Collection` and `YuukiAS/GPT_Codex_AI_Bridge_Kit`.

## Consumer Rule

Daily update requests read `release`; they do not advance it. Explicit `main` or development updates are allowed only when the user asks for development mode, and the result must be labeled as development.

## Producer Rule

Only formal release closure may advance `release`.

Before advancing a release ref, the owning producer must verify:

1. repo/origin identity;
2. the target is the exact formally closed release commit;
3. an existing `release` ref can fast-forward to the target;
4. no reviewed/candidate/evidence-only commit is accepted merely because it is newer;
5. the push is non-force;
6. the remote ref equals the intended target after push.

Later docs, TODO, evidence or ordinary main commits do not advance `release` unless they are themselves part of the next formally closed release.

Producer owners:

- AI_Skills `release`: `ai-skills-repository-maintainer`.
- Bridge Kit `release`: `bridge-kit-maintainer`.

## Update Impact Authority

Cross-layer mutation scope is declared only by:

```text
release ref -> matching root CHANGELOG.md release section -> optional ### Update impact
```

If `### Update impact` is absent, treat the release as isolated.

If present, only the declared companion components and managed consumer refreshes may enlarge scope. Component/plugin changelogs may clarify details but cannot independently broaden the mutation set. Contradictory metadata fails closed as `RELEASE_METADATA_INCONSISTENT`.

Do not infer Bridge, Host, repo adaptation or optional plugin mutation from arbitrary diffs, commit messages, TODOs, README prose or model intuition.

