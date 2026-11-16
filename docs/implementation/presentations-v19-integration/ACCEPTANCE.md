# Presentations V19 integration acceptance

## Decision

- `VALIDATOR_V2_ACCEPTED = YES`
- `SHARED_CORE_ACCEPTED = YES`
- `COURSE_STANDARD_TEMPLATE_ACCEPTED = YES`
- `CUHK_SHARED_CORE_MIGRATION_ACCEPTED = YES`
- `TEMPLATE_PARITY_ACCEPTED = YES`

The accepted implementation is the integrated candidate
`0f91a3518bea33224637fd8e3d77b1736f385c4b`, based on
`5160f661a786cc5ec6977dc5b47995e51fb3587b`.

Component candidates:

- shared core and template parity:
  `41cfc79c76b481055e4cf844bcb33079ed907c69`
- Validator V2:
  `ffce0893fc4d502b17d25c3ed5d52e4bd00c985f`

## Template acceptance

The course-standard and CUHK templates now share one semantic Beamer core and
retain separate skins. The frozen 160 x 90 mm layout contract, typography,
8 mm body rail, title anchors, semantic spacing, navigation, footer, and closing
components are owned by the shared core. Brand colours, credit text, and artwork
remain skin-owned.

The same 11-page semantic specimen compiled through both skins with identical
text, font, geometry, and links outside the declared brand masks. Measured
parity is `0.0 px` maximum geometry delta and `0.0 PDF pt` maximum font delta.
The four canonical CUHK assets retain their frozen hashes. The real CUHK
research specimen also compiled and preserved the expected navigation links.

Evidence:

- `results/presentations-shared-core-template-parity/IMPLEMENTATION.md`
- `results/presentations-shared-core-template-parity/PARITY.md`
- `results/presentations-shared-core-template-parity/CUHK_REGRESSION.md`
- `results/presentations-shared-core-template-parity/parity.json`
- `results/presentations-shared-core-template-parity/v19-style-replay.json`

## Validator acceptance

Validator V2 is accepted as a bounded safety gate, not as a claim of human
quality. Its candidate regression ran once and passed 33 tests. The exact V19
production evidence binds PDF SHA-256
`88eae6b2073715729abd9c2b004d1d0f31541c4314c2b64cd49194346b35d6e1`
and contains 386 PASS, 88 REVIEW, and zero FAIL findings. REVIEW remains REVIEW.
Archived V18 overflow and section-width controls fail deterministically. The
exact legacy V4 locator is unavailable, so that replay remains
`NOT_VERIFIED`.

Independent held-out acceptance covered authority binding, digest mismatch,
role and relationship integrity, geometry and typography ownership, explicit
editable-format routing, generated-text mutation, navigation-mask scope, and
duplicate-token ownership. All required held-out classes passed. Payloads are
not recorded here so the cases remain reusable.

Evidence:

- `docs/implementation/presentations-validator-v2/IMPLEMENTATION.md`
- `docs/implementation/presentations-validator-v2/PUBLIC_TESTS.md`
- `docs/implementation/presentations-validator-v2/MUTATIONS.md`
- `docs/implementation/presentations-validator-v2/COVERAGE.json`
- `docs/implementation/presentations-validator-v2/LEGACY_REPLAY.json`

## Bounded verification

Fresh integration checks passed the nine shared-core tests, the focused legacy
projection-scale check, Marketplace generation/path validation, and hidden
acceptance. An earlier 57-test template run had one stale assertion; the
assertion was updated and its focused rerun passed. No second full 57-test run
was performed because it would not change the acceptance decision.

The complete integration manifest is
`INTEGRATED_CHANGED_FILES.tsv`. Promotion and downstream receipts must name
the exact accepted commit and must not turn REVIEW or NOT_VERIFIED into PASS.
