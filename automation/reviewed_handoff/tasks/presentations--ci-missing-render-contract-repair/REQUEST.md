# Reviewed Handoff Request

Task: `presentations--ci-missing-render-contract-repair`

## Objective

Repair one Presentations CI portability regression that blocks unrelated full-repository CI.

Observed failing Clear Writing CI:
- workflow run: `39097236717`
- failing job: `codex-marketplace`
- local full suite on the same Clear Writing candidate: `347/347 PASS`
- GitHub-hosted runner: three Presentations render-probe failures caused by missing TeX/canonical font resources.

The failure was introduced by the Presentations release-acceptance hardening in commit:
`f717d28beef4dd1cbbb66cb491712769d1250aac`.

## Root cause to preserve

Current Presentations generator introduced the typed state
`BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`, but the existing validators/tests
still encode the older missing-render contract.

In particular:

- `compile_pdf()` probes/materializes canonical fonts before checking whether
  any TeX engine exists, so a host missing both resources reports
  `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE` instead of
  `BLOCKED_MISSING_TEX_ENGINE`;
- Stage 3 and production-entry `--allow-missing-render` validators do not allow
  the new canonical-font missing state;
- the Stage 3 regression test assumes only `COMPILED` /
  `BLOCKED_MISSING_TEX_PACKAGE` when an engine exists, and
  `BLOCKED_MISSING_TEX_ENGINE` otherwise, despite the new typed font-resource
  dependency.

## Boundary

This is not a Presentation redesign and not a request to install host-local
canonical resources into GitHub Actions.

The repair must preserve strict production behavior:
- real production/render validation still fails closed when required TeX/font
  resources are absent;
- only the explicit non-render test/contract path
  `--allow-missing-render` may accept typed missing-environment states;
- missing source files, broken resource token replacement, unexpected fonts,
  or other product defects must remain failures.

Do not modify Clear Writing production source. After this external repair is
integrated to main, the Clear Writing task may consume it and rerun required CI.

Tracking: Presentations Issue #98 / font-resource ownership.
