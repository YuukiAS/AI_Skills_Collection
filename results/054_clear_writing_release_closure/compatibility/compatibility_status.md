# 054 Compatibility Route Status

Status: PASS for the 054 Gate B compatibility route slice.

Candidate commit: `245127e1bb46f860ea1976b1669c467c7a9f763d`

All replay runs used the official local marketplace / cachebuster / reinstall / fresh-session candidate path and record `actual_consumption.proven = true` in their `run.json` files.

## Routes

| Route | Status | Output | Replay metadata |
| --- | --- | --- | --- |
| Python `re` technical rewrite | PASS | `results/054_clear_writing_release_closure/compatibility/python_re/python_re_docs.md` | `results/054_clear_writing_release_closure/compatibility/python_re/run.json` |
| Light Chinese polish | PASS | `results/054_clear_writing_release_closure/compatibility/light_chinese_polish/light_chinese_polish.md` | `results/054_clear_writing_release_closure/compatibility/light_chinese_polish/run.json` |
| Fidelity-only | PASS | `results/054_clear_writing_release_closure/compatibility/fidelity_only/fidelity_only_check.md` | `results/054_clear_writing_release_closure/compatibility/fidelity_only/run.json` |
| English `scientific-prose` | PASS | `results/054_clear_writing_release_closure/compatibility/english_scientific_prose/english_scientific_prose.md` | `results/054_clear_writing_release_closure/compatibility/english_scientific_prose/run.json` |
| Explicit source-comparison/editorial | PASS | `results/054_clear_writing_release_closure/compatibility/source_comparison_editorial/editorial-review.md` | `results/054_clear_writing_release_closure/compatibility/source_comparison_editorial/run.json` |
| Ordinary natural routing | PASS | `results/054_clear_writing_release_closure/compatibility/ordinary_natural_routing/streaming-quantile-sketch-zh.md` | `results/054_clear_writing_release_closure/compatibility/ordinary_natural_routing/run.json` |

## Checks

- Each route replay records candidate commit `245127e1bb46f860ea1976b1669c467c7a9f763d`.
- Python `re` retained Unicode/bytes type boundaries, raw-string escaping, `SyntaxWarning` / `SyntaxError`, module-level convenience functions, and the third-party `regex` package reference.
- Light Chinese polish preserved `model_registry.json`, `python3 scripts/build.py --check`, `AUC=0.84`, `2026-09-10`, and the internal-validation limitation.
- Fidelity-only remained a preservation audit rather than a prose rewrite, keeping metrics, paths, formula, and applicability caveats separate.
- English `scientific-prose` stayed in English and preserved `n=42`, `p=0.08`, 95% CI reporting, and the preliminary-evidence conclusion strength.
- Source-comparison/editorial output legitimately used “原文” and “改写稿” because the task explicitly requested editorial comparison; it preserved the missing `40 ms` issue, possible-tail-latency wording, model identity, and logging boundary.
- Ordinary natural routing produced a standalone Chinese technical explanation, preserved KLL / streaming quantile sketch identities, `n`, median / 95th percentile queries, mergeability, and distributed telemetry relevance, while omitting source page language navigation, edit-link, and template-generation metadata.
- Mechanical scan found no internal workflow / repository / candidate / pipeline leakage in ordinary non-editorial routes.
