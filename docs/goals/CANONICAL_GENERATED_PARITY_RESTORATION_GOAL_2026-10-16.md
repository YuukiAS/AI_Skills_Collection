# Goal — Restore canonical source authority without changing generated behavior

Repository: YuukiAS/AI_Skills_Collection
Branch: work/repo--canonical-generated-parity-restoration

Execute `docs/design/source-authority/CANONICAL_GENERATED_PARITY_RESTORATION_PLAN_2026-10-16.md`.

The required result is source-first reproducibility of the current committed Presentations and Research Writing generated payloads.

Do not redesign Presentations or Research Authoring. Treat the current generated plugin trees on the pre-repair main baseline as the behavior to preserve.

Before editing, hash every file under:
- `plugins/codex/plugins/presentations/`
- `plugins/codex/plugins/research-writing/`

Restore canonical source/config so the official Marketplace generator reproduces those trees without deleting or changing any pre-existing generated runtime file.

For Presentations, promote the seven existing generated shared contracts into canonical presentations shared source and reconcile the canonical business/research SKILL wrappers to reproduce current generated wrappers.

For Research Writing, create the minimum canonical shared source corresponding to the current generated `shared/` directory and add the minimum supported `shared` mapping in `scripts/codex_marketplace_config.json`.

PASS requires:
- official generator clean/idempotent;
- every pre-existing generated file in both affected plugin trees byte-identical to the pre-repair snapshot;
- no version/routing/profile/description/default-prompt/domain behavior change;
- affected tests and full repository tests as required by the Plan;
- no weakening, skipping, or allowlisting.

If exact preservation cannot be achieved without a real domain-semantic choice, stop and report the exact conflict.

After validation, commit/push and integrate this repair to current main by ordinary non-force Git. Do not move release. Do not modify the Clear Writing reviewed task. Return only the final main commit, changed canonical source/config paths, validation result, and any remaining blocker.