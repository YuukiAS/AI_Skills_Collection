# Local User Repo Writing Lessons - 2026-07-28

This file records locally observed writing-output lessons distilled from the
user-requested `/users/a/e/aereinh/CARE` and `/users/a/e/aereinh/MoSAIC`
repositories.

| source | evidence inspected | local target | decision | distilled lesson |
|---|---|---|---|---|
| `/users/a/e/aereinh/CARE` | `prompts/FINAL_OUTPUT_READABILITY_POLICY.md`; readability validator tests and policy references | `skills/writing/core/writing-fidelity`, `skills/writing/core/chinese-prose` | partially-merged | Human-facing Markdown/PDF/report output must start with natural scientific judgment, then evidence and machine fields. Internal labels, paths, status tokens, loss names, and checklist fragments cannot substitute for meaning. |
| `/users/a/e/aereinh/MoSAIC` | `review/AUTHOR_DECISIONS_GUIDE_CN.md`; `review/CLAIM_TO_TEXT_MAP_CN.md`; `review/UNSUPPORTED_NUMBERS_CN.md` | `skills/writing/core/writing-fidelity`, `skills/writing/core/chinese-prose` | partially-merged | Month labels, old-draft rows, and invented `start/final <project>` labels should not replace the best-supported or author-approved version. Final artifacts must distinguish best row, alternate historical row, partial audit, and unsupported complete-result claims. |

## Boundary

- These are project-derived style and fidelity rules, not CARE/MoSAIC-specific
  active skills.
- No private data, result tables, or project-specific numbers are copied into
  runtime skill rules.
- The rules are intentionally phrased as general Markdown/PDF/report safeguards
  for future writing tasks.

## Routing Reinforcement - 2026-07-28

A follow-up review of CARE readability policy, recent controller reports, and MoSAIC paper-review notes confirmed that the lessons must be active runtime rules, not only provenance. `chinese-prose` now treats “中文为主”, “说人话”, group-meeting materials, and report readability as direct triggers. `writing-fidelity` now distinguishes reports, audits, previews, candidates, old drafts, leaderboard rows, best rows, and author decisions before accepting Markdown/PDF/slides/reports as final.
