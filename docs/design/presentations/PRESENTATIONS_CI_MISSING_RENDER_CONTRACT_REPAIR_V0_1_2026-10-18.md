# Presentations CI missing-render contract repair v0.1

Date: 2026-10-18
Status: PLANNER_PACKAGE_FOR_CRITIC
Task: `presentations--ci-missing-render-contract-repair`
Tracking: #98

## Objective

Close the exact generator/validator/test mismatch exposed by GitHub Actions run
`39097236717` without changing Presentation layout, typography policy, visual
quality rules, or Clear Writing.

## Verified failure mechanism

The current GitHub workflow intentionally installs only Python presentation
regression dependencies before running the full unit suite. It does not install
the private/host-local `render_resources/chinese_math_pdf` bundle or a TeX
toolchain.

That is compatible with the existing tests because they invoke validators with
`--allow-missing-render`; this mode is meant to validate non-render contracts
on hosts that cannot actually compile the deck.

Commit `f717d28...` added fixed canonical font-resource binding to the
Presentations generator, but did not update the corresponding missing-render
contract:

1. `compile_pdf()` calls `materialize_font_binding()` before checking whether
   a TeX engine exists.
2. On a clean GitHub runner with neither dependency, this returns
   `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`.
3. The Stage 3 validator separately observes
   `tex_engine_available=false` and requires
   `BLOCKED_MISSING_TEX_ENGINE`.
4. Both Stage 3 and production-entry allow-missing-render allowlists omit
   `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`.
5. The Stage 3 unit test also omits this newly introduced typed state.

This explains all three CI failures while local full tests pass on a host with
the real TeX/font bundle.

External sanity check: GitHub-hosted runner images expose a bounded installed
software image and should not be treated as carrying project-private render
resources. The repo's own renderer contract already says canonical font files
come from host-local `render_resources/chinese_math_pdf`, not from the public
repository.

## Frozen repair

### R1 — primary missing dependency precedence

In
`skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py`:

- resolve/check the TeX engine before attempting font materialization for the
  compile-status decision;
- if no TeX engine exists, return `BLOCKED_MISSING_TEX_ENGINE`;
- dependency-probe evidence may still record that canonical fonts are also
  absent.

Do not hide secondary missing-resource evidence; only make the primary
compile-status classification internally consistent.

### R2 — allow-missing-render accepts typed font-resource absence

In both:
- `validate_cuhk_scientific_layout_stage3.py`
- `validate_research_presentation_production_entry.py`

when and only when `--allow-missing-render` is explicitly active, accept
`BLOCKED_MISSING_CANONICAL_FONT_RESOURCE` as a legitimate environmental
non-render state.

Do not add source/logic defects such as
`BLOCKED_FONT_RESOURCE_TOKEN_MISSING` to this allowlist.

Strict validation without `--allow-missing-render` remains unchanged: missing
canonical fonts still block production render acceptance.

### R3 — regression tests match the typed dependency contract

Update `tests/test_presentations.py` so it proves at least:

- no TeX engine + no canonical font bundle resolves primary compile status to
  `BLOCKED_MISSING_TEX_ENGINE`;
- TeX engine present + canonical font bundle absent can resolve to
  `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`;
- allow-missing-render accepts those typed environmental states;
- strict validation still rejects missing-render states;
- source/generated Presentations script parity remains exact.

Prefer direct deterministic unit seams/mocking over installing TeX just to
manufacture the states.

## Alternatives rejected

### Install TeX + canonical fonts in GitHub CI

Rejected as the default fix. The canonical font bundle is deliberately
host-local/private deployment state, and the existing CI tests explicitly
support `--allow-missing-render`. Installing a full render environment would
make the CI heavier while leaving the generator/validator state mismatch
unfixed for other minimal hosts.

### Skip or remove the three tests

Rejected. The failures expose a real cross-host typed-state bug.

### Treat all probe failures as allowed

Rejected. That would hide source/token/font-policy regressions.

## Implementation scope

Allowed source:
- the three Presentations shared scripts named above;
- `tests/test_presentations.py`;
- official generated mirrors produced by the Marketplace generator;
- task-local evidence.

No template visual design, font policy identity, course-standard/CUHK
architecture, README, plugin routing, version, changelog, Clear Writing, or CI
workflow redesign is authorized.

Maintenance contract:
`workflow-core + ai-skills-core + presentations`.

## Acceptance

Same final candidate must pass:

1. focused Presentations dependency-state regressions;
2. full `tests/test_presentations.py`;
3. full repository unit suite;
4. source/generated parity;
5. Marketplace write/check plus clean second check;
6. `git diff --check`;
7. required GitHub CI on a GitHub-hosted runner.

GitHub CI PASS must come without installing private canonical font resources and
without weakening/skipping the render probes.

## Out of scope

- real deck visual redesign;
- new fonts or font substitutions;
- changing the canonical font policy;
- modifying render-chinese-math-pdf resource ownership;
- Clear Writing changes;
- paid review;
- release/version bump;
- Issue #98 broader shared-core implementation.

## Recovery

After this repair reaches main, the Clear Writing Planner may merge that exact
main into
`reviewed/clear-writing--scientific-explanation-readability-repair` and rerun
its unchanged full CI. No new Clear Writing production edit is implied.
