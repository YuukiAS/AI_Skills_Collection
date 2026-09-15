# C1 Compatibility Replay Result

Status: `PASS_FOR_PUBLIC_COMPATIBILITY_REPLAY`

This is public Phase 4 evidence for G1 compatibility on exact candidate C1. It
does not replace the required private Deep Research / complete G1-G6 evidence.

## Candidate Identity

```text
candidate_commit = 68a5bfb860ef09eeafb994de18878b86a2b13d0d
plugin_id = writing-style@ai-skills-candidate
plugin_version = 0.3
runtime_version = codex-cli 0.153.4
```

All three replays reported:

```text
actual_consumption.proven = true
installed candidate = writing-style@ai-skills-candidate 0.3
stderr bytes = 0
```

The child JSONL files remain in ignored `.local-runtime/` and are not committed.

## Replay Matrix

| Regression | Prior source | Run id | Expected route | Evidence |
|---|---|---|---|---|
| `light_chinese_polish` | `results/052_writing_style_reader_facing_generalization_closure/unrelated_regressions/light_chinese_polish/` | `20260915T062339Z-1370471` | `zh` / ordinary Chinese polish | child JSONL read `skills/zh/SKILL.md`; output is a short Chinese polish result, not heavy structural rewrite |
| `fidelity_only` | `results/052_writing_style_reader_facing_generalization_closure/unrelated_regressions/fidelity_only/` | `20260915T062416Z-1371336` | `fidelity` with Chinese reporting support | child JSONL read `skills/fidelity/SKILL.md` and `skills/zh/SKILL.md`; output is a fidelity risk check, not a rewritten article |
| `english_scientific_prose` | `results/052_writing_style_reader_facing_generalization_closure/unrelated_regressions/english_scientific_prose/` | `20260915T062512Z-1373338` | `sci` / English scientific prose | child JSONL read `skills/sci/SKILL.md` and `skills/fidelity/SKILL.md`; output remains English and preserves evidence boundaries |

## Repo-Local Artifacts

```text
results/055_clear_writing_release_convergence/compatibility_replay/light_chinese_polish/artifacts/output.md
results/055_clear_writing_release_convergence/compatibility_replay/fidelity_only/artifacts/output.md
results/055_clear_writing_release_convergence/compatibility_replay/english_scientific_prose/artifacts/output.md
```

Run receipts and plugin-add receipts are stored beside each output under
`artifacts/`.

Artifact hashes:

```text
a0af275e694ba04cd1c24d3923d43610b7baed6b122a988d05555909dfe5f196  light_chinese_polish/artifacts/output.md
707bd2db88b6eb01331f5f2769c4276051cc010f1ea6f9fdc9dd5d09978a4523  fidelity_only/artifacts/output.md
90bcc90a0a347705e18e3c3c1186419c30cc9167df3a756b781167265a693552  english_scientific_prose/artifacts/output.md
64d4b39fe146fde47d5934315cb8a1487aa0c6f7ccec1e7c742bfcc0e6c0f4db  light_chinese_polish/artifacts/run.json
53f1e72f668ed24b1d6ebce81cfc3b1e2c0d8d4655f7e4a7a06b4972c9e8d313  fidelity_only/artifacts/run.json
ccc41f4b6d3ab76bd04df6074dbe7ab885811cf28279e81f0d25412f227a4d2d  english_scientific_prose/artifacts/run.json
b63e6393314ce93796c54b0c8224396cab1d9ef8fce1c2247756580b2f0f42fe  plugin-add.json for all three replays
```

## Qualitative Checks

`light_chinese_polish`:

- retains `model_registry.json`, `python3 scripts/build.py --check`,
  `AUC=0.84`, date `2026-09-10`, and the internal-validation-only boundary;
- returns a concise Chinese polishing result rather than invoking the heavy
  document rewrite route.

`fidelity_only`:

- preserves `FedAvg`, `Dice=0.81`, `HD95=7.4 mm`,
  `scripts/train_fedavg.py`, `configs/fedavg.yaml`, and
  `\mathcal{L}=\mathcal{L}_{seg}+0.1\mathcal{L}_{reg}`;
- explicitly flags the forbidden overgeneralization that the regularization term
  applies to all methods;
- stays in risk-check mode and does not rewrite the source paragraph.

`english_scientific_prose`:

- preserves `n=42`, `p=0.08`, `95% CI`, internal validation cohort, and the
  preliminary-evidence boundary;
- remains English scientific prose and does not route into Chinese heavy
  rewrite.

## Residual Scope

This compatibility replay supports G1 but does not complete Phase 4. The
required private 054 Deep Research artifacts are still absent from the
authorized private read scope, so complete G1-G6 representative replay,
pre-final Critic bundle preparation, fresh G7, Terra, release CI, production
smoke, final Reviewer, user acceptance, and integration remain pending.
