# Goal — repair Presentations missing-render CI contract

Repository: `YuukiAS/AI_Skills_Collection`
Task: `presentations--ci-missing-render-contract-repair`
Branch: `reviewed/presentations--ci-missing-render-contract-repair`

Execute the approved bounded Plan:
`docs/design/presentations/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_V0_1_2026-10-18.md`.

Fix only the mismatch between:
- generator missing-dependency classification,
- `--allow-missing-render` validators,
- Presentations regression tests.

Preserve strict production render failure when TeX/canonical fonts are absent.
Do not install or vendor private canonical font resources into the repository or
GitHub CI. Do not modify Clear Writing.

Required result: focused + full tests, generated parity, Marketplace clean
checks and GitHub CI PASS on the same candidate.
