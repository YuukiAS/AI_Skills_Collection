# Speak-As-Human GitHub Intake - 2026-07-30

This intake records public sources reviewed after the local deep-research note
`speak-as-human-deep-research.md`. The integration target is not a new
humanizer skill. The reusable rules were distilled into `chinese-prose`,
`writing-fidelity`, the Chinese final-pass checklist, and generated plugin
descriptions so Chinese Markdown/PDF/report/README outputs trigger a
reader-facing final pass by default.

## Reviewed Sources

| repo | revision | license evidence | decision | local target | distilled use |
|---|---|---|---|---|---|
| `https://github.com/chen3feng/cn-doc-style-guide` | `6da4697b964ac8d45d99b230e5400ab74087c7bd` | `LICENSE` observed, CC0-1.0 | partially-merged | `skills/writing/core/chinese-prose`; checklist | README first-screen expectations: what this is, who it is for, current status, and where more detail lives. |
| `https://github.com/LifelongLazyLearner/qu-ai-wei` | `1600d3fcb5ec9f4db8835f48681b50e3e7f56fff` | `LICENSE` observed, MIT | partially-merged | `skills/writing/core/chinese-prose` | Style-register routing, over-correction protection, and Chinese AI-taste cleanup were rewritten for technical and research outputs. |
| `https://github.com/zLanqing/codex-claude-academic-skills` | `7ed6377f0efb6a38951b48ef03b19d996e454b1f` | `LICENSE` observed, MIT | partially-merged | `skills/writing/core/chinese-prose`; checklist | Research Chinese must preserve technical English objects and separate existing data, user-confirmed decisions, inference, and suggested next steps. |
| `https://github.com/zhlint-project/zhlint` | `c8678fe71ce3bcafe38ac168d11e9a0c6a2cfa0d` | `LICENSE` observed, MIT | reference-only | checklist; source notes | Markdown-aware Chinese lint concepts for CJK/English spacing, punctuation classes, ignored cases, and protected spans. |
| `https://github.com/huacnlee/autocorrect` | `e1a75da3faa9b1f005db97b77f47eb67abe1395e` | `LICENSE` observed, MIT | reference-only | checklist; source notes | CJK formatter/linter categories for mixed Chinese-English spacing, punctuation, code comments, strings, and CI-style checks. |
| `https://github.com/lint-md/lint-md` | `148a9a5de09725954ca00175a5e1b9e7f6ecc524` | `LICENSE` observed, MIT | reference-only | checklist; source notes | Markdown-specific lint categories for empty structures, inline code spacing, headings, and Chinese punctuation context. |
| `https://github.com/Jackychen-12/zh-quality` | `8e7332fc621e7bfd2385cd095499559327450156` | `LICENSE` observed, MIT | reference-only | checklist; source notes | Machine-text artifact categories such as mixed punctuation, protected whitelist needs, and hidden/non-reader-facing defects. |

## Reviewed But Not Adopted

| source | evidence | decision | reason |
|---|---|---|---|
| `xiaofenggan01/aigc-reduce` | Deep-research note flagged the repo goal as reducing AIGC detection/check rates. | rejected | Detection evasion and pseudo-originality are outside this collection's writing-fidelity boundary. |

## Boundary

- No external source text was vendored into active skills.
- Linter repositories were used as rule-category references only; this change
  does not add runtime dependencies.
- Unknown-license and noncommercial-sharealike sources from the research note
  are not copied into runtime guidance.
- The local acceptance standard is user/reader readability plus source fidelity,
  not hiding AI authorship or bypassing detectors.
