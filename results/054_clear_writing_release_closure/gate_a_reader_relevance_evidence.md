# Gate A Reader-Relevance Focused Evidence

task: `054_clear_writing_release_closure`
branch: `reviewed/054_clear_writing_release_closure`
worktree: `/tmp/ai-skills-054-clear-writing-release-closure`

## Inheritance And Maintenance Preflight

- current HEAD during Gate A repair: `a8c40e731f01add3e505459ffc49abc1ba84f87f`
- inherited 053 frozen candidate: `d4570c764326cd10b63eae5e605cc8ff885bd7f2`
- ancestry check: `git merge-base --is-ancestor d4570c764326cd10b63eae5e605cc8ff885bd7f2 HEAD` exited `0`
- installed plugin check: `codex plugin list` reported `ai-skills-core@yuukias-ai-skills` installed/enabled at version `0.2`
- production maintainer replay:
  - run_id: `20260913T033238Z-39ab4590f9b0`
  - status: `completed`
  - decision: Executor may proceed to Gate A focused tests and source-first repair
  - repo receipt: `results/054_clear_writing_release_closure/maintenance_preflight/ai_skills_core_maintenance_preflight_receipt.md`

## Focused Regressions

Added independent public-safe/synthetic tests in `tests/test_scientific_rewrite.py`:

- `test_reader_relevance_accounts_irrelevant_source_metadata_without_reader_leakage`
  - should-drop: source wrapper metadata, incidental alternate-language label, language-link count, and archive id are accounted as source context but omitted from reader-facing Chinese prose.
  - should-keep: `GraphSAGE`, `PyTorch Geometric`, `torch_geometric.nn.SAGEConv`, and `ogbn-products` remain reader-facing technical identities.
- `test_reader_relevance_cannot_hide_inline_critical_identity_as_metadata`
  - guardrail: an inline-critical method identity cannot be classified as excludable source metadata.

The fixture is unrelated to 053 Karatsuba H1 and does not use `Karatsuba / Алгоритм Карацубы`.

## Fail-Before Evidence

Command:

```bash
python -m unittest tests.test_scientific_rewrite.ScientificRewriteHeavyRouteTests.test_reader_relevance_accounts_irrelevant_source_metadata_without_reader_leakage tests.test_scientific_rewrite.ScientificRewriteHeavyRouteTests.test_reader_relevance_cannot_hide_inline_critical_identity_as_metadata
```

Observed before repair:

- result: `FAILED (failures=1, errors=1)`
- should-drop error: `ValidationError: source anchors lack meaning ownership: src-001`
- should-keep failure: `AssertionError: ValidationError not raised`

Interpretation:

- the old helper forced every source anchor into reader-facing meaning ownership, so irrelevant source metadata had no valid accounted-but-omitted path;
- the old helper did not reject an attempt to hide an inline-critical method identity as excludable metadata.

## Repair Summary

Source-first repair:

- `skills/writing/core/scientific-rewrite/scripts/rewrite_support.py`
  - added host-authored `source_context_items` validation;
  - allowed source anchors to be accounted as non-reader source context with explicit exclusion decision and rationale;
  - required Reader Plan to bind excluded source-context items;
  - rejected source-context exclusions that reference inline-critical exact items;
  - scoped final exact verification to reader-facing exact items referenced by Meaning Map / Reader Plan.
- `skills/writing/core/scientific-rewrite/SKILL.md`
  - documented source accounting versus final inclusion, semantic reader relevance, and anti-blacklist boundary.
- `skills/writing/core/chinese-prose/SKILL.md`
  - documented `SOURCE_CONTEXT_OMIT` behavior for Chinese realization.
- `skills/writing/core/writing-fidelity/SKILL.md`
  - documented reader relevance as fidelity-preserving source-context accounting, not deletion of substantive content.
- generated `plugins/codex/plugins/writing-style/**` refreshed through `python scripts/build_codex_marketplace.py --write --validate --check --path-report`.

## Pass-After Evidence

Focused command:

```bash
python -m unittest tests.test_scientific_rewrite.ScientificRewriteHeavyRouteTests.test_reader_relevance_accounts_irrelevant_source_metadata_without_reader_leakage tests.test_scientific_rewrite.ScientificRewriteHeavyRouteTests.test_reader_relevance_cannot_hide_inline_critical_identity_as_metadata
```

Result: `Ran 2 tests ... OK`

Focused writing-style tests:

```bash
python -m unittest tests.test_scientific_rewrite
```

Result: `Ran 25 tests ... OK`

Marketplace/generated checks:

```bash
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_scientific_rewrite tests.test_codex_marketplace
python scripts/skills.py validate
python scripts/skills.py audit --all
```

Results:

- marketplace generator: exit `0`; `plugins=10 active_skills=27 source_snapshots=65`; path budget `over_budget=0`
- focused marketplace tests: `Ran 60 tests ... OK`
- skill validation: `validated 150 active skills, 18 profiles, templates, and trigger eval scaffolds`
- skill audit: exit `0`; only profile/domain budget advice was printed

## Non-Blacklist Evidence

Scan command:

```bash
rg -n "Karatsuba|Алгоритм|Cyrillic|Russian|俄|Pas de message|language blacklist|script blacklist|blacklist|delete foreign|foreign alias|外语一律|非中文一律" skills/writing/core/scientific-rewrite skills/writing/core/chinese-prose skills/writing/core/writing-fidelity tests/test_scientific_rewrite.py plugins/codex/plugins/writing-style/skills
```

Relevant result:

- no `Karatsuba` / `Алгоритм` special case;
- `Pas de message` appears only in the independent synthetic should-drop fixture and assertion;
- source/generated skill text explicitly says the repair is semantic reader relevance, not a language or script blacklist.

Helper boundary scan:

```bash
rg -n "write reader-facing prose|does not generate|mechanical only" skills/writing/core/scientific-rewrite/scripts/rewrite_support.py skills/writing/core/scientific-rewrite/SKILL.md plugins/codex/plugins/writing-style/skills/scientific-rewrite/scripts/rewrite_support.py plugins/codex/plugins/writing-style/skills/scientific-rewrite/SKILL.md
```

Result: source and generated helper remain documented as mechanical-only and not reader-facing prose generation.
