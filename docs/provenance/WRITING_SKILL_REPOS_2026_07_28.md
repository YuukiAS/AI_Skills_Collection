# Writing Skill Repo Intake - 2026-07-28

This file records the two writing-related GitHub repos reviewed in this intake and the local merge decision.

| repo | revision | license evidence | decision | local target | notes |
|---|---|---|---|---|---|
| https://github.com/Tina0514/prevent-defensive-ai-writing-skill | `9686ccbacad5` | `LICENSE` observed, README states MIT | partially-merged | `skills/writing/core/scientific-prose` | Distilled confident, non-defensive scientific framing rules: foreground strongest evidence-backed contribution, narrow claims instead of self-attack, keep limitations exact and proportional, avoid reviewer-facing attack surfaces. |
| https://github.com/Haoran-98/ICLR-reviewer | `3a105ae9270f` | no license file observed in clone | partially-merged | `skills/writing/research/peer-review` | Distilled ICLR-style evidence-grounded review workflow: manuscript map, independent reviewer lenses, AC-style synthesis, claim-evidence audit, concern ledger, revision impact, rebuttal status, and citation verification boundaries. Source text was locally rewritten per user instruction. |

## Boundary

- No standalone active skill was imported from either repo.
- Source text was distilled into existing local skills to avoid duplicate writing/review triggers.
- `Haoran-98/ICLR-reviewer` has no observed license file; integration is limited
  to locally rewritten workflow rules with the license status preserved here.
