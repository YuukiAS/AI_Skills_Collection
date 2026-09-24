# ADAPTING Consumer Evidence

Task key: `ai-skills-core--machine-update-orchestration`  
Evidence date: 2026-09-25 local

## Board Requirement

`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` defines this task as a
machine-consumed workflow / shared maintenance mechanism. After central
implementation + formal release + G2, lifecycle is `ADAPTING`, not `DONE`.

Required logical consumers:

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`
4. `Workstation`
5. `Legion`

AI Skills Maintainer is a per-current-consumer adaptation executor, not a
cross-machine controller. This evidence covers only the current consumer that is
actually available in this Codex task.

## Current Consumer: Workstation

Status: `PASS`

Actual target identity discovered from the current machine:

```text
hostname: Workstation
platform: Linux Workstation 6.6.87.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun 5 18:30:46 UTC 2025 x86_64 GNU/Linux
user: yuukias
HOME: /home/yuukias
CODEX_HOME: /home/yuukias/.codex
codex: codex-cli 0.148.0-alpha.9
```

Approved adaptation / update action:

- This same task explicitly authorized post-review formal promotion + G2.
- Real G2 migrated this current consumer's `yuukias-ai-skills` Marketplace from
  `main` to `release`, refreshed the Marketplace snapshot, and reinstalled
  `ai-skills-core@yuukias-ai-skills` through official Codex commands.

Installed / loaded identity:

```text
[marketplaces.yuukias-ai-skills]
last_revision = "c7776e202ae0324fc00b719b6ef8224b8e0498fe"
source_type = "git"
source = "https://github.com/YuukiAS/AI_Skills_Collection.git"
ref = "release"
sparse_paths = [".agents/plugins", "plugins/codex/plugins"]

[plugins."ai-skills-core@yuukias-ai-skills"]
enabled = true
```

`codex plugin list --marketplace yuukias-ai-skills --available --json` confirmed:

- `ai-skills-core@yuukias-ai-skills`: installed true, enabled true, version `0.5`
- `workflow-core@yuukias-ai-skills`: installed true, enabled true, version `0.4`
- companion AI_Skills plugins remained installed/enabled at their expected
  existing versions.

Relevant normal-entry consumption:

- Fresh production replay run: `20260924T172142Z-368783282d6c`
- Wrapper status: `completed`
- Exit code: `0`
- Plugin: `ai-skills-core@yuukias-ai-skills`
- The released `sync this machine` normal entry loaded through
  `ai-skills-core:machine-update-orchestrator`.
- Evidence files:
  - `g2_released_smoke/released_normal_entry_run.json`
  - `g2_released_smoke/released_normal_entry_last_message.txt`
  - `g2_released_smoke/released_normal_entry_smoke_report.md`

Fresh-session / restart boundary:

- The real G2 reinstall placed `ai-skills-core 0.5` at
  `/home/yuukias/.codex/plugins/cache/yuukias-ai-skills/ai-skills-core/0.5`.
- Fresh production plugin replay proved the released normal entry from a new
  Codex child process.
- The user-facing state for this already-updated consumer is `ALREADY_CURRENT`.
- If future updates install/refresh plugin code, the correct state is
  `UPDATED_RELOAD_REQUIRED`; current-session hot reload was not claimed.

Risk-matched should-not-change / failure safety:

- Main and release refs were verified equal at formal commit
  `c7776e202ae0324fc00b719b6ef8224b8e0498fe` after non-force release update.
- Bridge `release` was not advanced.
- Bridge runtime/source and Host state were not modified.
- The fresh replay was read-only and wrapper write isolation passed.
- The canonical main checkout retained pre-existing unrelated untracked files
  untouched.

Durable evidence locator:

- `results/ai-skills-core--machine-update-orchestration/G2_POST_REVIEW_PROMOTION_EVIDENCE.md`
- `results/ai-skills-core--machine-update-orchestration/ADAPTING_CONSUMER_EVIDENCE.md`

## Remaining Required Consumers

These consumers are not marked PASS from this machine. Resolving their exact
identity/locator and performing adaptation requires bounded authority on each
corresponding consumer environment.

| Consumer | Status | Reason |
|---|---|---|
| `Longleaf_Codex` | `PENDING_CONSUMER_AUTHORITY` | Not the current machine; exact current identity/locator must be discovered on that consumer. |
| `Longleaf_Backup_Codex` | `PENDING_CONSUMER_AUTHORITY` | Not the current machine; exact current identity/locator must be discovered on that consumer. |
| `CUHK_Workstation_WSL_Codex` | `PENDING_CONSUMER_AUTHORITY` | Not the current machine; exact current identity/locator must be discovered on that consumer. |
| `Legion` | `PENDING_CONSUMER_AUTHORITY` | Not the current machine; exact current identity/locator must be discovered on that consumer. |

Top-level Maintenance Board Issue `#86` remains open in `ADAPTING`. It cannot be
closed as `DONE` until all required consumers are PASS or policy-backed N/A with
durable evidence.
