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
candidate marketplace: ai-skills-candidate
candidate identity: <plugin>@ai-skills-candidate
```

The runtime pin is deliberate. Do not turn this helper into a generic runtime registry or expose arbitrary executable/version selection. Changing the pin requires a separate bounded compatibility update with real replay evidence.

## What the helper guarantees

The helper:

- stages the plugin from the exact committed Git tree and committed `.agents/plugins/marketplace.json`, not from dirty working-tree source;
- uses the official pinned Codex package under gitignored `.local-runtime/` and invokes it by absolute path;
- leaves the machine/global Codex install and `PATH` unchanged;
- reuses the existing Codex account identity rather than copying credentials into a second home;
- uses the reserved temporary `@ai-skills-candidate` namespace;
- launches a fresh ephemeral `codex exec --ignore-user-config` child with the candidate enabled process-locally;
- detects candidate/live consumer conflicts by exact top-level `SKILL.md`
  frontmatter `name` overlap;
- when conflicts exist, temporarily moves only those conflicting cached Plugin
  packages outside the plugin discovery root by same-filesystem atomic rename;
- writes a durable recovery manifest before mutation and restores or reconciles
  the original cache paths after success, failure, timeout or ordinary exception;
- records `plugin-add.json`, child JSONL/stdout and stderr in the ignored run directory;
- streams the long-running child stdout/stderr to those run-directory files while the child is still alive;
- proves actual candidate consumption only from parsed `command_execution` JSON events that read `SKILL.md` under the candidate plugin cache path;
- fails the replay if parsed child `command_execution` events read `SKILL.md`
  under any original conflicting package path or quarantine path;
- removes the temporary candidate in `finally` cleanup;
- verifies the pre-existing same-name production plugin identity/enabled state
  and normalized non-candidate plugin list are unchanged.

A replay does **not** prove domain quality by itself. The generic helper proves candidate identity, fresh-runtime loading, actual skill consumption, cleanup and production-identity preservation. The target plugin/task still owns domain-specific route receipts, fidelity checks, rendered artifacts, scientific correctness, qualitative acceptance and unrelated regression.

Consumer isolation is a replay harness boundary, not a product prompt
blacklist. It does not uninstall, remove, update, or disable the user's live
plugins persistently. It also does not claim that `codex exec
--ignore-user-config` makes other plugin-cache skills impossible to discover.
Instead, when the current cache contains a package exposing the same top-level
Skill identity as the candidate, the helper suppresses only that exact cached
package for the duration of the replay, outside the discovery tree, and audits
the JSONL command trace. A replay may pass only when:

```text
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
FINAL_PERSISTENT_STATE_EQUIVALENT_TO_BEFORE = YES
```

If an account-backed plugin reappears at the original path while the
transaction-owned quarantine copy still exists, that passive rehydration is not
by itself a consumer-isolation failure. The helper may keep the rehydrated
original and delete only the exact transaction-owned quarantine duplicate when
all of the following proof is present:

```text
original tree hash == quarantine tree hash == pre-run tree hash
plugin manifest hashes are identical to the pre-run manifest hash
marketplace/plugin/version/path identity is identical
normalized non-candidate plugin state matches the pre-run state; during
restoration this comparison may ignore only the exact candidate plugin IDs
installed by the current replay run
CANDIDATE_PATH_READS > 0
ORIGINAL_CONFLICT_PATH_READS = 0
QUARANTINE_PATH_READS = 0
the quarantine path is owned by the current transaction
```

The full `$CODEX_HOME/config.toml` hash is recorded as diagnostic provenance,
but full config-file drift alone is not a cleanup hard gate. If a future
transaction needs plugin-relevant config validation, it must snapshot an
explicit minimal projection before mutation instead of relying on the full
config file hash.

After deleting the duplicate, the helper fsyncs and rechecks the rehydrated
original package identity and normalized non-candidate plugin state before
removing the recovery manifest. Candidate plugin IDs may be ignored only while
the current run is still inside the restoration step. In multi-record recovery,
that state check is made after any earlier ordinary quarantine restores have
completed, so the comparison is against the restored non-candidate state rather
than an entry-of-cleanup snapshot. After candidate cleanup, the final persistent
plugin-state check still requires the full plugin list to match the replay's
pre-run baseline, with no candidate identity left installed. If any hard proof
is missing or inconsistent, the condition remains `RESTORATION_AMBIGUOUS`: do
not delete, overwrite, continue replay, or treat the output as a candidate PASS.

## Safety boundaries

Do not use this workflow to:

- upgrade or replace the server/global Codex installation;
- change global `PATH`, npm/conda installs, system symlinks or live global plugin configuration;
- add a permanent candidate marketplace;
- clone another AI_Skills checkout merely to replay a candidate;
- modify Bridge Kit or Host Policy just to make a candidate replay work;
- overwrite `writing-style@yuukias-ai-skills` or another production identity with a candidate;
- inject internal subskill/route names into a natural black-box production prompt merely to manufacture a PASS;
- treat a receipt/test/JSONL event as reader-facing PRODUCT PASS.
- work around a consumer-isolation failure by uninstalling/removing a live
  plugin, editing global user plugin state, or adding task-specific prompt
  blacklists.
- move a cached package by copy/delete, across filesystems, or into a hidden
  directory below `plugins/cache/**`.

`replay` is local-only and must not silently download a runtime. If the runtime is missing, run `ensure-runtime` explicitly.

## Private inputs and authorization

Private replay follows the repository `AGENTS.md` authorization boundary. A new private artifact/data scope, provider/endpoint, purpose or credential scope requires explicit user authorization once. Record a non-secret task-local authorization receipt and reuse that authorization for the same bounded scope; do not ask again for every A/B/C replay, retry or fresh child.

Never print, commit or push private plaintext, credentials, `auth.json`, token-bearing config, private child JSONL, stage packets or review PDFs. Keep them under the repository's ignored private/runtime areas and commit only permitted hashes/status/evidence locators.

## Failure classification

Classify before changing anything:

- runtime/package/CLI/config/parser failure -> replay infrastructure failure; fix only when the failure is real and generic;
- child reads an original conflicting package path or quarantine path during
  candidate replay -> replay consumer-isolation failure; restore first, then
  fix the shared replay path or return to Planner/Critic;
- a stale quarantine can be proven by manifest and hash -> recover at helper
  entry before installing a new candidate;
- original and quarantine both exist without full verified-equivalent-rehydration
  proof, hashes do not match, or filesystem assumptions changed ->
  `RESTORATION_AMBIGUOUS`; do not overwrite/delete;
- candidate is loaded but wrong skill/route is selected -> target plugin routing failure;
- correct route is selected but domain receipt/mechanical validation fails -> target plugin implementation failure;
- process/receipt passes but user artifact is poor -> PRODUCT / ARTIFACT failure, not harness success;
- cleanup or production identity changes -> safety failure; stop immediately.

The `codex exec` child has a conservative wall-clock timeout and, on POSIX,
runs in its own process group so replay cleanup can terminate that child tree.
This timeout is an infrastructure safety bound, not a product gate. If it fires,
the helper preserves the current `child.stdout.jsonl` and `child.stderr`,
cleans up the temporary candidate, and exits non-successfully. A partially
written output file or a pre-timeout consumption event is still a replay
failure; only normal child completion plus the existing consumption parser may
produce a successful `run.json`.

Do not keep expanding the helper after a real replay works. New state machines, runtime registries, generic health frameworks and Bridge-managed runtime selection are out of scope unless a later independent production failure proves they are necessary.

## Release boundary

Candidate replay is pre-release evidence. Final closure still requires the task's frozen release gates, including unrelated regression, source/generated parity, required CI/review, version/changelog closure when applicable, and a real released/production-identity install or upgrade smoke. `@ai-skills-candidate` must never be reported as the final released plugin identity.
