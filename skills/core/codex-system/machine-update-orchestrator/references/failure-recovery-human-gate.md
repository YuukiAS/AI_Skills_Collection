# Failure, Recovery And Human Gate Rules

Do a bounded preflight before mutation:

- target formal release;
- source/ref/config owner;
- route;
- authoritative update impact;
- candidate managed consumers;
- dirty conflicts;
- authorization;
- should-not-change set.

## Human Gate Classification

Treat ordinary update mechanics as `AGENT_RESOLVABLE`: discovery, public fetch, release resolution, safe Marketplace refresh/reinstall, safe fast-forward within the requested formal update, declared companion updates, validation and managed-consumer refresh.

Ask exactly one minimal `HUMAN_ONLY` question only for genuinely new:

- credential/account/provider;
- private external transfer;
- destructive operation;
- production deployment or live-global side effect outside the update request;
- unresolved user-owned dirty overlap;
- unowned repo rule conflict requiring a product/repo decision;
- irreducible product semantics.

Do not ask for discoverable versions, commits, paths, `CODEX_HOME`, Bridge location, repo inventory or obvious required companions. Do not repeat a gate after the bounded effect was already authorized.

## Recovery

No transaction database is added. Every owner operation should be idempotent or safely re-discoverable.

If a later step fails, keep already valid released updates, do not reset/stash/restore user work, and report `PARTIAL_UPDATE` with the failed owner and step.

Only the special legacy Marketplace source-swap failure restores the exact captured legacy source. Reruns start from fresh discovery.

Primary user-facing reports should be concise and use one of these semantic states: `UPDATED`, `UPDATED_RELOAD_REQUIRED`, `ALREADY_CURRENT`, `PARTIAL_UPDATE`, `DEVELOPMENT_SOURCE_PRESENT`, `RELEASE_METADATA_INCONSISTENT`, `REPO_OWNED_CONFLICT`, `UNKNOWN_OR_UNRELEASED_TARGET`, or an exact unsupported/authority result.

