# Development Replay Evidence

Task: `research-authoring--formal-production-authoring`
Candidate commit C0: `1c37c0715aca0096606f24e56192b7857e72bbd6`

This is development regression evidence only. It is not final G1-G4 fresh evidence.

## Replay

Command:

```bash
python scripts/candidate_plugin_replay.py replay \
  --plugin research-writing \
  --candidate-commit 1c37c071 \
  --task results/research-authoring--formal-production-authoring/development_replay/DEV_REPORT_TASK.md \
  --input results/research-authoring--formal-production-authoring/development_replay/DEV_REPORT_RAW_NOTES.md
```

Result:
- runtime: `codex-cli 0.153.4`
- candidate plugin id: `research-writing@ai-skills-candidate`
- candidate version: `0.3`
- installed path: `/users/a/e/aereinh/.codex/plugins/cache/ai-skills-candidate/research-writing/0.3`
- actual consumption: `proven=true`
- consumption event: `item.started`, JSONL line `5`

Durable copies:
- `results/research-authoring--formal-production-authoring/development_replay/raw/run.json`
- `results/research-authoring--formal-production-authoring/development_replay/raw/child.stdout.jsonl`
- `results/research-authoring--formal-production-authoring/development_replay/raw/child.stderr`
- `results/research-authoring--formal-production-authoring/development_replay/advisor_update.md`
- `results/research-authoring--formal-production-authoring/development_replay/route_receipt.md`

## Development Regression Meaning

The replay used a public-safe report-family raw-notes fixture covering:
- advisor-facing scientific organization rather than runtime chronology;
- bounded result slot for incomplete shifted-split evidence;
- separation of internal Slurm/notebook provenance from reader-facing claims;
- conditional claim strength and unresolved seeds;
- document route receipt with Research Authoring core before report delegate.

The generated `route_receipt.md` explicitly records:

```text
research-authoring-core -> research-reporting -> fidelity and language review -> document-level evidence QA -> outputs/advisor_update.md
```

This proves candidate loading and representative development behavior. It does not prove final G2 or G3.
