# Bridge Release Channel

Normal Bridge updates resolve the Bridge Kit formal `release` ref, not arbitrary `main`.

Daily `update Bridge Kit` is read-only with respect to the `release` ref. It may fast-forward a canonical local checkout to the already published formal release when ancestry and dirty ownership permit, then refresh the editable package/entry point and verify runtime identity.

Formal Bridge release closure may advance `refs/heads/release` only when all conditions hold:

1. Bridge repo/origin identity is verified as `YuukiAS/GPT_Codex_AI_Bridge_Kit`.
2. The target is the exact formally closed Bridge release commit.
3. The target has matching Bridge version/changelog/closure evidence.
4. An existing `release` ref can fast-forward to the target.
5. The push is non-force and affects only `refs/heads/release`.
6. The remote ref is fetched and verified after push.
7. Later docs, TODO or evidence commits on `main` do not advance `release` unless they are part of a later formally closed release.

Non-fast-forward, inconsistent metadata, ambiguous origin, dirty-overlap ambiguity or missing formal closure evidence fails closed.

Bridge Kit itself remains the runtime implementation owner. This skill owns the formal distribution channel and version/source identity only.
