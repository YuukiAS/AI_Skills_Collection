# 047 Public Holdout Evaluation Summary

Implementation freeze commit:
`ade5a1f653f88df07eb0c70edfd016c744b1611a`

This summary is Executor-side evidence only. It does not replace the required
independent Text Review or Scheduled GPT Reviewer artifact reading.

## Frozen Sources

Range hashes are recorded in
`results/047_writing_style_scientific_rewrite_architecture/public_holdout_sources/RANGE_SHA256.json`.

- `HOLDOUT-UNSEEN-001`: Bobbio `README.md` lines 1-70,
  SHA-256 `92429e9035fd855b4130080a8003d8128ee3b4d267672ccf3a60b87c6eb22477`.
- `HOLDOUT-UNSEEN-002`: Distributed Imaging report lines 1-8,
  SHA-256 `e4f1369cdc23c767943bff613f776e60b02b4689b5134f5574b94639bbddd52a`.
- `SNF-CN-TECH-001`: AI Research Toolkit `R_RESEARCH_STACK.md` lines 1-13,
  SHA-256 `2f44f24073713cadb7ad6a012ae3e4959448926a35c66c93e568fc2dd651313b`.
- `SNF-CN-SCI-002`: Asteria `ROADMAP.md` lines 5-17,
  SHA-256 `18400b402f15f290978c974d01c2fc7f1f0479bd718dece264ff3bd79aced4f8`.

## Process Evidence

- Source/generated parity: `python3 scripts/build_codex_marketplace.py --check`
  passed.
- Marketplace validation: `python3 scripts/build_codex_marketplace.py --validate`
  passed.
- Skill validation: `python3 scripts/skills.py validate` passed with
  `validated 150 active skills, 18 profiles, templates, and trigger eval scaffolds`.
- Relevant tests: `python3 -m unittest tests.test_skill_runtime_text_audit
  tests.test_research_writing_routing tests.test_codex_marketplace
  tests.test_scientific_rewrite` passed 52 tests.
- Temporary installation smoke:
  `python3 scripts/verify_server_installation.py --skill scientific-rewrite
  --mode copy --json` passed.
- Default temporary installation smoke:
  `python3 scripts/verify_server_installation.py --mode copy --json` passed.

## Positive Holdouts

### HOLDOUT-UNSEEN-001

Baseline output keeps most original workflow English labels as the reader-facing
structure. Architecture C preserves the exact product/tool chain while explaining
the role of `local-first`, human judgment, Zotero/Notion/Codex handoff, and the
knowledge-supply-chain problem in ordinary Chinese.

Exact fidelity: passed.

Executor semantic assessment: no critical violation observed; reader effort
improved clearly relative to baseline.

### HOLDOUT-UNSEEN-002

Baseline output is essentially the original short report. Architecture C keeps
all frozen experiment facts while rewriting the opening as a clearer scientific
setup and bounded conclusion.

Exact fidelity: passed.

Executor semantic assessment: no critical violation observed; reader effort
improved modestly relative to baseline.

## Should-Not-Fix Controls

Both controls were classified as `NO_DEEP_REWRITE`. Their output is the original
frozen range unchanged.

- `SNF-CN-TECH-001`: passed exact fidelity; no package names or reproducibility
  requirements were changed.
- `SNF-CN-SCI-002`: passed by unchanged output; no product/model/evidence
  distinction was weakened.

## Evidence Gaps

The earlier attempt to inspect the current live Codex Marketplace installation
was superseded by an isolated production-like install. The current live global
Codex Marketplace/cache was not modified.

The isolated install evidence is recorded in
`results/047_writing_style_scientific_rewrite_architecture/isolated_production_replay/`.
It proves that the 047 branch's generated `writing-style` payload installs via
the normal Marketplace/plugin mechanism into a shadow `CODEX_HOME`, and that a
fresh session with an ordinary Chinese scientific rewrite request exposes
`writing-style:scientific-rewrite` from the installed plugin cache.

The remaining production replay gap is model generation, not installation or
routing: the isolated `CODEX_HOME` had no model credentials and no local
`OPENAI_*` API key was present. A minimal isolated `codex exec --ephemeral`
probe reached the OpenAI endpoint after proxy variables were unset, then failed
with `401 Unauthorized: Missing bearer or basic authentication in header`. No
live auth token or secret was copied from the real Codex home.

044 private Text Review is also still pending. Private plaintext was not
committed.

## Executor Interpretation

The public batch is an `EXPERIMENTAL_ARCHITECTURE_PASS_CANDIDATE`, not a
production release. `writing-style` remains `NO_BUMP`, repository remains
`NONE`, and this branch must not merge to `main` before independent review and
user decision.
