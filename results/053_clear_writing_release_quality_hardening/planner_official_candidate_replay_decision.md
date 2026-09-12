# 053 Planner decision — official Codex candidate replay

Date: 2026-09-12

Task: `053_clear_writing_release_quality_hardening`

Branch: `reviewed/053_clear_writing_release_quality_hardening`

Status: Planner clarification; no Clear Writing production implementation change.

## Decision

Use option A: the official Codex local-marketplace development loop with the existing authorized `CODEX_HOME` and account identity, a distinct temporary candidate marketplace identity, a Codex cachebuster suffix, `codex plugin add <plugin>@<marketplace>`, and a fresh Codex session/thread for replay.

Do not continue searching for an undocumented no-install/process-local hot-load path. The 053 capability preflight already established that pinned `codex-cli 0.153.4` fails before plugin/model loading under the attempted process-local no-install boundary, while the current official OpenAI `plugin-creator` guidance defines local iteration through marketplace-backed reinstall plus a fresh thread.

This decision is an interpretation of the existing canonical Goal and frozen Plan, not a second Plan revision. `plan_revision` remains `1` (the configured maximum). The canonical Goal already authorizes use of the existing Codex account / `CODEX_HOME`, a reserved temporary candidate identity/cache, install/remove/finally cleanup, and bounded candidate replay. No new product semantics, private-data scope, provider, credential location, paid-call budget, Bridge/Host Policy behavior, schema, state, or ledger is introduced.

## Official source checked

Current OpenAI Codex `main` at decision time: `53c542d944c705f3a66780a19223223bee57cbb6`.

Authoritative files:

- `openai/codex: codex-rs/skills/src/assets/samples/plugin-creator/SKILL.md`
- `openai/codex: codex-rs/skills/src/assets/samples/plugin-creator/references/installing-and-updating.md`

The official guidance says that existing local plugins are iterated by using the configured local/personal marketplace, updating the manifest with one Codex cachebuster suffix, reinstalling with `codex plugin add <plugin>@<marketplace>`, and starting a new thread/session so updated skills/tools are loaded. A non-default local marketplace must first be configured with `codex plugin marketplace add <path-to-marketplace-root>`; marketplace/config files should not be hand-edited as the update mechanism.

## Option comparison

### A — existing authorized home + temporary local marketplace: SELECTED

This is the smallest mature supported path and matches the canonical 053 authorization envelope.

Executor must:

1. Stage the exact committed candidate tree into an ignored temporary local marketplace. The candidate marketplace identity must be distinct from production, for example `ai-skills-candidate-053`; production remains `writing-style@yuukias-ai-skills`.
2. Record the production plugin/marketplace snapshot before any candidate install. At minimum bind production identity, enabled state, version, installed path/cache identity where exposed, and relevant marketplace listing.
3. Keep candidate skill/source bytes tied to the exact committed candidate. A cachebuster may change only the staged candidate manifest version as the official packaging pickup mechanism; record that packaging-only delta and separately hash/verify the staged candidate `SKILL.md`/relevant payload against the committed source.
4. Configure the temporary non-default local marketplace through the supported CLI, install the candidate through `codex plugin add writing-style@<candidate-marketplace>`, and start a fresh session/thread for replay.
5. Prove actual candidate skill consumption from child/session evidence, not merely successful installation or a receipt.
6. Run cleanup in `finally` semantics on success and failure: remove the candidate plugin, remove the temporary marketplace when added for the replay, and remove temporary staging/cache files owned by this replay.
7. Re-read the production snapshot after cleanup and prove before == after for the production `writing-style@yuukias-ai-skills` identity/state. Candidate residue must be absent.
8. Do not copy, symlink, print, or migrate credentials. Continue to use the existing authorized account identity and `CODEX_HOME` only.
9. Do not ask again for the already-frozen candidate install/remove/cache/cleanup authorization.

If option A fails, Executor must record the concrete supported-CLI failure and return to `NEEDS_GPT_PLANNER`; it must not silently fall back to another loader or credential path.

### B — isolated credential-bearing development home: NOT SELECTED

This is unnecessary while A is a documented supported path. It would create a genuinely new credential location and therefore requires one explicit user authorization before setup. Do not create, copy, or symlink credentials into such a home under the current scope.

Only reconsider B if A is proven impossible for a concrete supported-CLI reason. If authorized later, the environment should become the canonical reusable AI_Skills development profile rather than a per-task credential copy.

### C — Bridge/Host-Policy controlled replay entrypoint: REJECTED FOR NOW

Do not redesign Bridge Kit, Host Policy, execpolicy, or create another candidate runtime. A/B have not both been proven impossible, and no current evidence justifies the cross-plugin infrastructure cost.

## Generic workflow hardening required

The observed failure is reusable beyond Clear Writing: AI_Skills candidate replay imposed an invented no-install/process-local constraint and kept probing undocumented overrides even though Codex's supported local-plugin development loop is marketplace + cachebuster + reinstall + fresh session.

This can recur in future central-plugin tasks. Executor should therefore add one concise generic governance rule, preferably in a separate governance commit safe to integrate independently:

> For Codex plugin candidate iteration, prefer the current official `plugin-creator` local-marketplace/cachebuster/reinstall/fresh-session flow. Do not require or repeatedly probe an undocumented no-install/process-local hot-loader. Preserve a distinct candidate identity, exact committed source verification, before/after production snapshot equality, `finally` cleanup, and no credential copy. Escalate only when the supported flow itself is concretely impossible.

Do not create a new schema/state/ledger/framework for this rule.

## Resume boundary

After Gate 0 replay infrastructure succeeds, resume the already frozen 053 sequence at K1–K4 without changing the Clear Writing quality contract, Deep Research replay budget, two-holdout batch, single Terra review budget, or final human acceptance requirement.
