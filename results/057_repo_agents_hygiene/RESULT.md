# 057 Repo AGENTS Hygiene Result

Status: `EXECUTED_UNAUDITED`

Current authorized endpoint is `EXECUTED_UNAUDITED`, not a main/develop merge,
Bridge release, 056 execution, or final 057 achievement claim.

## Candidate Summary

- Bridge Kit: `a5c4fe61dc9ab0e228822e854ace5c7e50a4d967`
- Bobbio: `dd977705a2cdfecaa2d4e09127ab4464ae898b32`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829`
- Mica-for-ChatGPT: `7afb2277cd1001204e77e4987d9fcaa447e7c675`
- Asteria: `b34f6c5d27dd9ac7b1193826ac878fca4a953fb5`
- SeminarArc: `c3fc5a64a3abaec7860808fbcb4082b95d2a0302`
- CUHK_Date inspected ref: `711fab75f044b7ad31e5ff8610c076f902ccc949`

## Version Decisions

Repository bump decision: `NONE`
Reason: AI_Skills_Collection only records 057 evidence/control artifacts.

Affected plugins:
- none: `NO_BUMP`
  Reason: no central AI_Skills production plugin behavior changes.

Bridge Kit package candidate: `0.8.2 -> 0.8.3`.

## H1-H9

- H1 semantic preservation: `PASS`
  Evidence: `SEMANTIC_PRESERVATION.md` maps moved/changed hard rules and
  surviving owners for every mutable repo.
- H2 no internal contradiction: `PASS`
  Evidence: Bobbio root + `docs/design/FIGMA_HANDOFF.md` +
  `docs/PRODUCT_DESIGN_BRIEF.md` now agree that Figma is the current canonical
  visual source, the product brief owns durable product/interaction constraints,
  and old PNGs are historical/supporting references. SeminarArc root now owns
  the prominent safety summary while `docs/DEVICE_TESTING.md` owns mechanics,
  command restrictions, volatile inventory and incident evidence.
- H3 discoverability: `PASS`
  Evidence: root AGENTS files point to current owners: Bridge fresh root points
  to `prompts/AGENT_RULES.md`; Bobbio root points to Figma handoff; Asteria root
  points to `docs/operations/development/RUNTIME_OPERATIONS.md`; SeminarArc root
  points to `docs/DEVICE_TESTING.md`.
- H4 managed-block integrity: `PASS`
  Evidence: product repo Bridge managed blocks were not hand-edited; Bridge
  fresh init creates exactly one managed block from canonical source.
- H5 context quality: `PASS`
  Evidence: `SIZE_REPORT.md` records before/after line and byte counts. No gate
  is justified by size reduction alone.
- H6 repo-specific regression protections: `PASS`
  Evidence: grep/inspection confirmed Bobbio Zotero/native/iPad/Pencil rules,
  Lucerna Windows/provider/screenshot/Longleaf invariants, Mica privacy/typing/
  fail-open/manual-authenticated acceptance, Asteria fixed URL/browser/GPT Work
  locators, and SeminarArc device safety protections remain present.
- H7 fresh Bridge normal entry: `PASS`
  Evidence: `python -m ai_bridge_kit.cli init --target
  /tmp/057_repo_agents_hygiene/h7_fresh_cli` created scaffold + one managed
  block + Lite locator; `python -m ai_bridge_kit.cli validate --target
  /tmp/057_repo_agents_hygiene/h7_fresh_cli` exited 0 with 0 errors and the
  expected empty-task warning. Generated Lite rules contain `## Versioning
  Default` and `MAJOR.MINOR.PATCH`.
- H8 existing-root preservation: `PASS`
  Evidence: real CLI normal init and `--force` on
  `/tmp/057_repo_agents_hygiene/h8_existing_project` preserved the project-owned
  root prose before the managed block and did not install the scaffold into the
  existing root.
- H9 no Lite duplication: `PASS`
  Evidence: fresh root `AGENTS.md` points to `prompts/AGENT_RULES.md`; grep
  showed `MAJOR.MINOR.PATCH` and prerelease policy only in generated
  `prompts/AGENT_RULES.md`, not in root.

## Verification

- `python -m unittest tests.test_bridge_cli_router`: `5 tests`, `OK`
- `python -m ai_bridge_kit.cli validate --target /tmp/057_repo_agents_hygiene/h7_fresh_cli`: exit 0, `PASSED: 0 errors, 1 warning(s)`
- `python -m unittest discover -s tests`: `361 tests in 226.196s`, `OK`
- `git diff --check`: exit 0 for Bridge Kit, Bobbio, Lucerna, Mica-for-ChatGPT,
  Asteria and SeminarArc candidate diffs.

## Known Notes

- Bridge CLI prints current host-policy drift diagnostics during init because
  the local Codex home has drifted managed host-policy content. This is machine
  host state, not a target-repo scaffold failure.
- No product/runtime/source code was changed in Bobbio, Lucerna,
  Mica-for-ChatGPT, Asteria or SeminarArc.
- CUHK_Date was inspect-only and unchanged; current visible instruction surface
  is README/config docs, with no root `AGENTS.md` created.
