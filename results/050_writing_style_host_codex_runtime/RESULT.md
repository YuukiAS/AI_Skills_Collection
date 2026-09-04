---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 050_writing_style_host_codex_runtime
implementation_commit: 508639ae9f4007d311b6f2646fa201ae4dd20bbe
---

# 050 Writing Style Host-Codex Runtime — style-smoke handoff

## Process / Mechanical Status

Status: `PROCESS_MECHANICAL_PASS_AWAITING_HUMAN_STYLE_DECISION`.

The production `writing-style` heavy scientific rewrite route has been changed
to the frozen 050 architecture: host Codex owns document understanding, Meaning
Cards, unit writing, semantic self-audit, repair and assembly; deterministic
code only validates exact literals, stage/dataflow identity and privacy-safe
receipts.

Implementation commit: `508639ae9f4007d311b6f2646fa201ae4dd20bbe`.

The private SMOKE-A/B/C samples were generated from the exact frozen 049 source
segment identities and validated through the generated `writing-style`
`scientific-rewrite` helper. Public Git evidence contains only hashes, ranges,
unit/stage counts, verification status and local private locators.

Maintenance companion preflight:

- configured installed plugin id: `ai-skills-core@yuukias-ai-skills`;
- `codex plugin list --json` could not load the stale configured marketplace
  source `/tmp/ai-skills-048`;
- `ai-bridge plugin-replay --dry-run` succeeded for run
  `20260904T010735Z-a882b2215b99`;
- actual `ai-bridge plugin-replay` stopped before semantic execution with
  `WRITE_ISOLATION_NOT_ENFORCEABLE` because the child Codex preflight used
  `network_access=false` and could not reach the Codex backend. The write
  canary was unchanged.

The 050 smoke therefore used the current production-equivalent controlled
host-Codex route with the generated `writing-style` payload from this branch.
No OpenAI `/v1/responses`, `/v1/responses/input_tokens`, Terra call, or paid
GitHub workflow was run.

## Product / Style Status

Status: `AWAITING HUMAN STYLE DECISION`.

Mechanical fidelity and dataflow checks are not style acceptance. The next
authority is the user: return `STYLE_ACCEPT` if all three samples are good
enough to authorize full private generation, or `STYLE_REJECT` with concrete
feedback for bounded generic repair.

## Private Human-Readable Package

Private package root:
`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke`

Combined reader file:
`/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke/STYLE_SMOKE_FOR_USER.md`

Individual candidates:

- SMOKE-A:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke/SMOKE-A/final_candidate.md`
- SMOKE-B:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke/SMOKE-B/final_candidate.md`
- SMOKE-C:
  `/overflow/htzhu/mingcheng_new/.tmp/codex-Longleaf_Connection_Bridge/050_private_style_smoke/SMOKE-C/final_candidate.md`

## Smoke Evidence

| Smoke | Source segment SHA-256 | Units | Exact literals | Candidate SHA-256 | Exact | Dataflow |
|---|---:|---:|---:|---|---|---|
| SMOKE-A | `3e18bea855cc4afccacc47b7ed60600ef637cbffd7ea412fcb54fe4b0575a5db` | 2 | 55 | `2acfd6f6e245af7fd39b1f3322f79eb1edaf32f736223743ccd4c36fea7e1ec0` | PASS | PASS |
| SMOKE-B | `20161b96ba82a610d3669d49aae01eeff32f98eeb1737438c892a869b5660e88` | 4 | 53 | `3d460cdd01959424ac6b96298c2299d0f7c1458a6af1bae74726f045a8c260b3` | PASS | PASS |
| SMOKE-C | `22eacc455a07341d24f52666e911dea1f0e8edd46d8bbaeed896a5fc2f973a48` | 8 | 113 | `d67a927b704bedbeb06f8b6dcc8e10b60902b6f8c9b9191eb1aa24a3470e0d96` | PASS | PASS |

Full private source SHA-256 for all three:
`f447de7acaae76486e42e6281f9280b482c770303a67c0861256ddba67316213`.

Public receipts:

- `results/050_writing_style_host_codex_runtime/private_style_smoke/SMOKE-A/stage_receipt.json`
- `results/050_writing_style_host_codex_runtime/private_style_smoke/SMOKE-B/stage_receipt.json`
- `results/050_writing_style_host_codex_runtime/private_style_smoke/SMOKE-C/stage_receipt.json`

## Local Validation

- `python3 -m unittest tests.test_scientific_rewrite` — PASS, 16 tests.
- `python3 -m unittest tests.test_codex_marketplace` — PASS, 36 tests.
- `python3 -m unittest tests.test_skill_runtime_text_audit tests.test_paid_review_workflows` — PASS, 10 tests.
- `python3 -m unittest tests.test_scientific_rewrite tests.test_codex_marketplace tests.test_skill_runtime_text_audit tests.test_paid_review_workflows` — PASS, 62 tests.
- `python3 -m unittest discover -s tests` — PASS, 189 tests.
- `python3 scripts/build_codex_marketplace.py --write` — PASS.
- `python3 scripts/build_codex_marketplace.py --validate` — PASS.
- `python3 scripts/build_codex_marketplace.py --check` — PASS.
- `python3 scripts/build_codex_marketplace.py --path-report` — PASS.
- `python3 scripts/skills.py validate` — PASS.
- `python3 scripts/skills.py audit --all` — PASS.

Reviewed-handoff validator remains red only for the previously known 049/050
old-template section mismatch. Frozen `PLAN.md` was not edited for that.

## Version Decision

Repository bump decision: `NONE`.

Affected plugins:

- `writing-style`: `NO_BUMP`
  Reason: 050 is stopped at the first human style gate. Plugin release is not
  complete until user `STYLE_ACCEPT` and the later final private-report
  acceptance path.
