# Repo-local Candidate Plugin Replay

This is the canonical pre-release replay path for testing a committed AI_Skills Marketplace plugin candidate on Linux x86_64 without upgrading the machine-wide Codex CLI or replacing the production plugin identity.

Use it for bounded central-plugin refinement when the implementation candidate is committed but not yet released. It is AI_Skills-owned development tooling, not a Bridge Kit runtime manager and not a second Reviewed Handoff workflow.

## Normal entry

Provision the pinned repo-local runtime once:

```bash
python3 scripts/candidate_plugin_replay.py ensure-runtime
```

Replay an exact committed candidate:

```bash
python3 scripts/candidate_plugin_replay.py replay \
  --plugin <plugin-name> \
  --candidate-commit <commit-sha> \
  --task <repo-local-natural-task.md> \
  --input <repo-local-input-file>
```

Repeat `--input` when a task needs multiple files.

Current compatibility pin:

```text
Codex CLI: 0.153.4
runtime root: .local-runtime/codex/0.153.4/
candidate marketplace: ai-skills-candidate-053
candidate identity: <plugin>@ai-skills-candidate-053
```

The runtime pin is deliberate. Do not turn this helper into a generic runtime registry or expose arbitrary executable/version selection. Changing the pin requires a separate bounded compatibility update with real replay evidence.

## What the helper guarantees

The helper:

- stages the plugin from the exact committed Git tree and committed `.agents/plugins/marketplace.json`, not from dirty working-tree source;
- uses the official pinned Codex package under gitignored `.local-runtime/` and invokes it by absolute path;
- leaves the machine/global Codex install and `PATH` unchanged;
- reuses the existing Codex account identity rather than copying credentials into a second home;
- uses the reserved temporary `@ai-skills-candidate` namespace;
- follows the official local-plugin development loop: stage a local marketplace, apply one Codex cachebuster to the staged plugin manifest, configure that non-default local marketplace with `codex plugin marketplace add`, reinstall with `codex plugin add <plugin>@<candidate-marketplace>`, and launch a fresh ephemeral `codex exec --ignore-user-config` child;
- records `marketplace-add.json`, `plugin-add.json`, child JSONL/stdout and stderr in the ignored run directory;
- proves actual candidate consumption only from parsed `command_execution` JSON events that read `SKILL.md` under the candidate plugin cache path;
- removes the temporary candidate plugin, temporary marketplace config, and staged candidate files in `finally` cleanup;
- records staged-vs-installed `SKILL.md` hashes so the cachebuster-only packaging delta does not hide source drift;
- verifies the pre-existing same-name production plugin identity/enabled state is unchanged.

A replay does **not** prove domain quality by itself. The generic helper proves candidate identity, fresh-runtime loading, actual skill consumption, cleanup and production-identity preservation. The target plugin/task still owns domain-specific route receipts, fidelity checks, rendered artifacts, scientific correctness, qualitative acceptance and unrelated regression.

## Safety boundaries

Do not use this workflow to:

- upgrade or replace the server/global Codex installation;
- change global `PATH`, npm/conda installs, system symlinks or live global plugin configuration;
- add a permanent candidate marketplace;
- require an undocumented no-install/process-local plugin hot-loader when the official local marketplace/cachebuster/reinstall/fresh-session loop fits;
- clone another AI_Skills checkout merely to replay a candidate;
- modify Bridge Kit or Host Policy just to make a candidate replay work;
- overwrite `writing-style@yuukias-ai-skills` or another production identity with a candidate;
- inject internal subskill/route names into a natural black-box production prompt merely to manufacture a PASS;
- treat a receipt/test/JSONL event as reader-facing PRODUCT PASS.

`replay` is local-only and must not silently download a runtime. If the runtime is missing, run `ensure-runtime` explicitly.

## Private inputs and authorization

Private replay follows the repository `AGENTS.md` authorization boundary. A new private artifact/data scope, provider/endpoint, purpose or credential scope requires explicit user authorization once. Record a non-secret task-local authorization receipt and reuse that authorization for the same bounded scope; do not ask again for every A/B/C replay, retry or fresh child.

Never print, commit or push private plaintext, credentials, `auth.json`, token-bearing config, private child JSONL, stage packets or review PDFs. Keep them under the repository's ignored private/runtime areas and commit only permitted hashes/status/evidence locators.

## Failure classification

Classify before changing anything:

- runtime/package/CLI/config/parser failure -> replay infrastructure failure; fix only when the failure is real and generic;
- candidate is loaded but wrong skill/route is selected -> target plugin routing failure;
- correct route is selected but domain receipt/mechanical validation fails -> target plugin implementation failure;
- process/receipt passes but user artifact is poor -> PRODUCT / ARTIFACT failure, not harness success;
- cleanup or production identity changes -> safety failure; stop immediately.

Do not keep expanding the helper after a real replay works. New state machines, runtime registries, generic health frameworks and Bridge-managed runtime selection are out of scope unless a later independent production failure proves they are necessary.

## Release boundary

Candidate replay is pre-release evidence. Final closure still requires the task's frozen release gates, including unrelated regression, source/generated parity, required CI/review, version/changelog closure when applicable, and a real released/production-identity install or upgrade smoke. `@ai-skills-candidate*` must never be reported as the final released plugin identity.
