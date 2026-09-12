# 053 Candidate Replay Recovery

Status: PASS

SAFE_TO_INTEGRATE_INDEPENDENTLY: YES

Date: 2026-09-12

Branch: `reviewed/053_clear_writing_release_quality_hardening`

## Scope

This is a generic AI_Skills candidate-replay workflow fix. It does not change Clear Writing production behavior and does not consume the private Deep Research replay budget, fresh holdout budget, or Terra review budget.

The repaired path follows the OpenAI `plugin-creator` local development loop selected by Planner:

```text
repo-local staged marketplace
-> single Codex cachebuster on staged plugin manifest
-> codex plugin marketplace add
-> codex plugin add writing-style@ai-skills-candidate-053
-> fresh codex exec session
-> parsed child JSONL candidate SKILL.md consumption proof
-> finally remove plugin, marketplace, staged files, and candidate cache residue
```

No `auth.json` copy/symlink was created, no credential path was migrated, and no Bridge Kit or Host Policy files were changed.

## Validation

Focused tests:

```text
python3 -m unittest tests.test_candidate_plugin_replay
Ran 26 tests
OK
```

The tests cover:

- committed candidate source resolution;
- arbitrary runtime/CODEX_HOME flag rejection;
- cachebuster version behavior;
- official `codex plugin marketplace add/remove` command shape;
- top-level `installedPath` use from `codex plugin add --json`;
- candidate identity detection;
- actual consumption requiring parsed JSON `command_execution`;
- child-failure cleanup;
- consumption-proof failure cleanup;
- candidate cache cleanup limited to `ai-skills-candidate-053` namespace.

## Final normal-entry replay smoke

Command:

```text
python3 scripts/candidate_plugin_replay.py replay --plugin writing-style --candidate-commit fcb20edbe2a738db39e3a9d9ed8c6b451ec66526 --task results/052_writing_style_reader_facing_generalization_closure/known_regression/BLOOM_REWRITE_TASK.md --input results/052_writing_style_reader_facing_generalization_closure/known_regression/bloom_filter_wikipedia_excerpt.md
```

Run:

```text
.local-runtime/candidate-plugin-replay/runs/20260912T134800Z-1318419/
```

Result:

```text
runtime_version = codex-cli 0.153.4
candidate_commit = fcb20edbe2a738db39e3a9d9ed8c6b451ec66526
candidate_marketplace = ai-skills-candidate-053
plugin_id = writing-style@ai-skills-candidate-053
cachebuster = local-20260912T134800Z-1318419
installed_version = 0.2+codex.local-20260912T134800Z-1318419
actual_consumption.proven = true
actual_consumption.event_type = item.started
actual_consumption.line_index = 4
```

The child JSONL proved candidate `SKILL.md` consumption by reading:

```text
plugins/cache/ai-skills-candidate-053/writing-style/0.2+codex.local-20260912T134800Z-1318419/skills/scientific-rewrite/SKILL.md
```

The same run also produced the Bloom public known-regression candidate and a passing `SCIENTIFIC_REWRITE_HEAVY_ROUTE_RECEIPT_V2` stage receipt. That output is public-safe, but this file records only the generic replay recovery evidence.

## Cleanup evidence

Post-run CLI state:

```text
candidate_ids = []
candidate_marketplaces = []
production_snapshot = writing-style@yuukias-ai-skills enabled=true marketplaceName=yuukias-ai-skills
```

Post-run filesystem residue check:

```text
/overflow/htzhu/mingcheng_new/.codex-global/plugins/cache/ai-skills-candidate-053: absent
/overflow/htzhu/mingcheng_new/.codex-homes/Longleaf_Connection_Bridge/plugins/cache/ai-skills-candidate-053: absent
```

Run-local cleanup record:

```text
.local-runtime/candidate-plugin-replay/runs/20260912T134800Z-1318419/cleanup.json
candidate_cache_dirs_removed = /overflow/htzhu/mingcheng_new/.codex-global/plugins/cache/ai-skills-candidate-053
```

Credential copy/symlink created: `NO`.

Auto-review denial during final recovery smoke: `NO`.

Live production plugin/cache/config changed after cleanup: `NO`.
