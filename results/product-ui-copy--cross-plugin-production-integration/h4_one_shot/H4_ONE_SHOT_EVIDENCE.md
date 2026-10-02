# H4 One-Shot Fresh Holdout Evidence

Task key: `product-ui-copy--cross-plugin-production-integration`

H4 status: `PASS`

## Candidate Binding

- H2 candidate commit: `a06ff050bc82bb22358dfcb3e4faa885fddd285b`
- Repository version: `5.4.0`
- Candidate plugin versions:
  - `web-development`: `0.4`
  - `writing-style`: `0.4`
- H3 batch path: `results/product-ui-copy--cross-plugin-production-integration/fresh_holdout/final_holdout_batch.json`
- H3 batch blob: `8eec188b2c146713df5a67775ddabe74a336efda`
- Scenario count: `8`

## One-Shot Execution

Command:

```bash
python scripts/candidate_plugin_replay.py replay --plugin web-development --plugin writing-style --candidate-commit a06ff050bc82bb22358dfcb3e4faa885fddd285b --task results/product-ui-copy--cross-plugin-production-integration/h4_one_shot/h4_replay_task.md --input results/product-ui-copy--cross-plugin-production-integration/fresh_holdout/final_holdout_batch.json
```

Run id:

```text
20260929T041437Z-829584
```

Runtime:

```text
codex-cli 0.153.4
```

Actual same-session candidate plugin consumption:

- `web-development@ai-skills-candidate`: `PASS`
  - installed candidate version: `0.4`
  - evidence event: `item.started`
  - stdout JSONL line: `6`
- `writing-style@ai-skills-candidate`: `PASS`
  - installed candidate version: `0.4`
  - evidence event: `item.started`
  - stdout JSONL line: `6`

Child stderr:

```text
empty
```

## H4 Outputs

- Replay task: `results/product-ui-copy--cross-plugin-production-integration/h4_one_shot/h4_replay_task.md`
  - blob: `3c2e508c5353bfbbcfc1e03fb9b4f51775d0e0e6`
- Response: `results/product-ui-copy--cross-plugin-production-integration/h4_one_shot/h4_holdout_response.md`
  - blob: `949490a157febf087aa239aafce366b90bf934b7`
- Verdict: `results/product-ui-copy--cross-plugin-production-integration/h4_one_shot/h4_holdout_verdict.json`
  - blob: `f004ee042fa62b3c2d9d9664ce268e6a28c05c5f`
- Candidate replay metadata: `results/product-ui-copy--cross-plugin-production-integration/h4_one_shot/H4_CANDIDATE_REPLAY_RUN.json`
  - blob: `d25708c20eb683fed64d75cb5da5058e7b1ed521`

## Scenario Verdicts

All 8 scenarios were processed in the frozen H3 order.

| Scenario | Expected | Actual | Verdict |
| --- | --- | --- | --- |
| H3-01 | `KEEP` | `KEEP` | `PASS` |
| H3-02 | `LOCALE/REGISTER` | `LOCALE/REGISTER` | `PASS` |
| H3-03 | `CONTENT ARCHITECTURE` | `CONTENT ARCHITECTURE` | `PASS` |
| H3-04 | `PRODUCT SEMANTICS` | `PRODUCT SEMANTICS` | `PASS` |
| H3-05 | `LEGAL/TRUST/SAFETY` | `LEGAL/TRUST/SAFETY` | `PASS` |
| H3-06 | `WORDING/NATURALNESS` | `WORDING/NATURALNESS` | `PASS` |
| H3-07 | `WORDING/NATURALNESS` | `WORDING/NATURALNESS` | `PASS` |
| H3-08 | `NO_FRONTEND_OR_PRODUCT_UI_COPY` | `NO_FRONTEND_OR_PRODUCT_UI_COPY` | `PASS` |

Top-level verdict from `h4_holdout_verdict.json`:

```text
PASS
```

## Scope Boundary

This H4 evidence proves the frozen fresh holdout text/routing batch was consumed
once by the unchanged H2 candidate in the repo-local candidate runtime, with
both candidate plugins actually loaded and consumed in the same session.

This H4 evidence does not replace:

- the pre-existing rendered acceptance evidence for H2;
- real GitHub CI;
- independent Scheduled GPT Reviewer inspection;
- final user acceptance;
- main merge or release-ref movement authorization.
