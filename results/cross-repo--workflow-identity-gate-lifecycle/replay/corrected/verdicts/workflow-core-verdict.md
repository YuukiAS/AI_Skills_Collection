# Workflow-Core Corrected Replay Verdict

Task key: `cross-repo--workflow-identity-gate-lifecycle`
Plugin: `workflow-core`
Candidate commit: `ce63f50238555849a48256068e6fa0d46e21a97b`

## Frozen Input Identity

- `workflow-core-task.md` sha256: `37ddf02b8fe1f59d9e5cb816869f74b20f37341dc89a26231c37e13d0756c7f1`
- `workflow-core-input.md` sha256: `e2146d8b8094a6855ee2b2512ead8e20c9756034cd3a4993e7775e9d33e6d5b3`

## Run Evidence

- Run receipt: `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/artifacts/workflow-core-run.json`
- Substantive output: `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/outputs/workflow-core-final-response.md`
- Actual consumption proven: true

## Verdict

PASS. The corrected replay output matches the frozen expected behavior:

- W1: classifies an explainably isolated local validator change as `NARROW_OK`.
- W2: classifies shared prompt/assembly/runtime/router/normal-entry changes as `BROAD_FULL_REQUIRED`.
- W3: rejects unresolved multi-gate failure as `NOT_RELEASE_READY` and does not stitch old evidence into a release claim.
- W4: rejects maturity promotion as `MATURITY_NOT_PROVEN` without inventing fixed paid or fresh sample counts.
- All scenarios preserve the same-final-candidate requirement where release evidence is needed.

This verdict closes only the `workflow-core` half of `C-WIGL-I2-REPLAY-CAPABILITY-EVIDENCE`; the `ai-skills-core` corrected replay remains pending explicit user approval after auto-review rejected the escalated command.
