# 055 Clear Writing — Production Smoke and Restore Evidence

Date: 2026-09-20
Task: `055_clear_writing_release_convergence`
Candidate: `C6 = 79d620a0c60cdd086dd5828c8686bac843291cda`
Target release identity: `writing-style 0.3`
Result: `PASS`

## Live state before smoke

Recorded files:

- `results/055_clear_writing_release_convergence/production_smoke/before_marketplaces.json`
- `results/055_clear_writing_release_convergence/production_smoke/before_plugins.json`

Relevant before state:

```text
marketplace yuukias-ai-skills root = /overflow/htzhu/mingcheng_new/AI_Skills_Collection
writing-style@yuukias-ai-skills version = 0.1
writing-style@yuukias-ai-skills enabled = true
writing-style source = /overflow/htzhu/mingcheng_new/AI_Skills_Collection/plugins/codex/plugins/writing-style
```

## Temporary install/upgrade

The live `yuukias-ai-skills` marketplace was temporarily replaced with the task
worktree:

```text
/tmp/ai-skills-055-clear-writing-release-convergence
```

`codex plugin add writing-style@yuukias-ai-skills --json` installed:

```text
pluginId = writing-style@yuukias-ai-skills
version = 0.3
installedPath = /overflow/htzhu/mingcheng_new/.codex-homes/mingcheng_new/plugins/cache/yuukias-ai-skills/writing-style/0.3
```

Recorded files:

- `results/055_clear_writing_release_convergence/production_smoke/installed_smoke_marketplaces.json`
- `results/055_clear_writing_release_convergence/production_smoke/installed_smoke_plugins.json`

## Normal user-entry smoke

Prompt:

```text
请把下面这份材料整理成更清楚、自然、读者可直接看的中文技术说明。不要改变事实、数字、公式、路径、命令或限制条件；不要写成执行日志。
```

Smoke input/output/evidence:

- Prompt: `results/055_clear_writing_release_convergence/production_smoke/prompt.md`
- Input copy: `results/055_clear_writing_release_convergence/production_smoke/input.md`
- Output: `results/055_clear_writing_release_convergence/production_smoke/smoke_output.md`
- Event stream: `results/055_clear_writing_release_convergence/production_smoke/smoke_events.jsonl`

Observed production-plugin consumption:

```text
/overflow/htzhu/mingcheng_new/.codex-global/plugins/cache/yuukias-ai-skills/writing-style/0.3/skills/zh/SKILL.md
/overflow/htzhu/mingcheng_new/.codex-global/plugins/cache/yuukias-ai-skills/writing-style/0.3/skills/fidelity/SKILL.md
```

Smoke output preserved the required reader-facing facts:

- 8 samples;
- approximately 12,000 cells;
- command `python scripts/qc_rna.py --input data/raw/demo.h5ad --output data/processed/demo_qc.h5ad --min-genes 300 --max-mito 0.18`;
- comparison between `--max-mito 0.18` and `0.25`;
- approximately 6% additional cell removal;
- limitation that stricter threshold is not proven to improve clustering;
- future work remains future work.

The output reads as a normal Chinese technical note, not a workflow log.

## Mandatory restore

Restore operations:

1. Removed temporary `writing-style@yuukias-ai-skills` 0.3 install.
2. Removed temporary task-worktree `yuukias-ai-skills` marketplace source.
3. Re-added original marketplace source:
   `/overflow/htzhu/mingcheng_new/AI_Skills_Collection`.
4. Reinstalled original `writing-style@yuukias-ai-skills` from that source.

Recorded files:

- `results/055_clear_writing_release_convergence/production_smoke/after_restore_marketplaces.json`
- `results/055_clear_writing_release_convergence/production_smoke/after_restore_plugins.json`

Verified restored state:

```text
marketplace yuukias-ai-skills root = /overflow/htzhu/mingcheng_new/AI_Skills_Collection
writing-style@yuukias-ai-skills version = 0.1
writing-style@yuukias-ai-skills enabled = true
writing-style source = /overflow/htzhu/mingcheng_new/AI_Skills_Collection/plugins/codex/plugins/writing-style
installed plugin identity/version/enabled set restored = true
```

## Decision

```text
PRODUCTION_SMOKE=PASS
PRODUCTION_RESTORE=PASS
SECOND_TERRA_RUN=NO
REPLACEMENT_FRESH_RUN=NO
C6_CHANGED=NO
```
