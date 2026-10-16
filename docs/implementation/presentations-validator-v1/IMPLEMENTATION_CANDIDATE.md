# Presentations Validator V1 Implementation Candidate

This candidate implements a generic read-only validator under
`plugins/codex/plugins/presentations/shared/validator_v1/`.

It provides:

- `python -m presentations_validator_v1 validate --authority-bundle <dir> --candidate-bundle <dir> --repo <repo> --out <evidence.json>`
- `python -m presentations_validator_v1 inspect-coverage --out <coverage.json>`
- `python -m presentations_validator_v1 run-public-controls --out <controls.json>`

The top-level `presentations_validator_v1/` package is a minimal routing shim for
that frozen CLI. Production logic lives in the validator package root.

The implementation keeps authority and candidate data separate. Detectors consume
only normalized authority/candidate/repository context. Public accepted controls
and public negative mutations invoke the same detector registry used by real
validation.

This is a Producer candidate only. It does not claim hidden-pack acceptance,
production readiness, or STAT5060 final acceptance.
