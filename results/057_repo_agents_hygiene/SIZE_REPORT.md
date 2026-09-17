# 057 Size Report

Size is context evidence only. H1/H6 semantic preservation and real owner
discoverability decide acceptance; line-count reduction alone is not a PASS
criterion.

## Current Final Counts

| Repo | File | Lines | Bytes |
| --- | --- | ---: | ---: |
| Bridge Kit | `ai_bridge_kit/cli.py` | 763 | 29345 |
| Bridge Kit | `templates/prompts/AGENT_RULES.md` | 215 | 8083 |
| Bridge Kit | `tests/test_bridge_cli_router.py` | 118 | 6248 |
| Bridge Kit | `README.md` | 872 | 35485 |
| Bridge Kit | `CHANGELOG.md` | 428 | 25376 |
| Mica-for-ChatGPT | `AGENTS.md` | 177 | 14064 |
| Asteria | `AGENTS.md` | 116 | 10953 |
| Asteria | `docs/operations/development/RUNTIME_OPERATIONS.md` | 144 | 5166 |
| SeminarArc | `AGENTS.md` | 129 | 7971 |
| SeminarArc | `docs/DEVICE_TESTING.md` | 208 | 14512 |
| Bobbio | `AGENTS.md` | 464 | 19631 |
| Bobbio | `docs/DEVELOPMENT_WORKFLOW.md` | 224 | 11912 |
| Bobbio | `docs/PRODUCT_DESIGN_BRIEF.md` | 452 | 16665 |
| Bobbio | `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md` | 136 | 7370 |

## Current Commit Stats

| Repo | Commit | Summary |
| --- | --- | --- |
| Bridge Kit | `e1d6b781ad7e56d567bed419001069baf439d0a5` | 5 files changed, 105 insertions, 23 deletions |
| Mica-for-ChatGPT | `e49416f874f633aedc7521734ee5b0f441aae970` | 1 file changed, 50 insertions, 70 deletions |
| Asteria | `0ce1d4daca1e410ce551570578dd563d4ef67e90` | 2 files changed, 44 insertions, 23 deletions |
| SeminarArc | `74caaa4ecec16f1bc90987979458d1a4e93f52be` | 2 files changed, 115 insertions, 64 deletions |
| Bobbio | `ab5dccb6b8b87c49671aa097233ce1bcc38be004` | 2 files changed, 57 insertions, 89 deletions |
| Lucerna | `41cd1297af6901531d3135593bc9806bffc38829` | unchanged in E2 |
| CUHK_Date | `711fab75f044b7ad31e5ff8610c076f902ccc949` | inspect only |

## Interpretation

- Bridge grew because it now contains byte-preservation helpers, regressions and
  candidate-version documentation.
- Mica, Asteria, SeminarArc and Bobbio reduce root duplication by moving detailed
  mechanics into existing owner documents or consolidating repeated guidance.
- Lucerna and CUHK_Date did not receive new E2 edits.
