# Research Skill Repo Webpage Record - 2026-07-28

This file records the repo webpages from the user's screenshot request. It is a source record only; no local autopilot skill is installed or exported from this intake.

| item | repo webpage | observed status | local decision | existing / target coverage |
|---|---|---|---|---|
| Academic Research Skills / ARS | https://github.com/Imbad0202/academic-research-skills | public clone checked at `0b58a31feee0`; license files observed: `LICENSE`, `NOTICE.md`, `THIRD_PARTY.md` | reviewed-existing | Already covered by `paper-workflow-orchestrator`, `literature-review`, `peer-review`, `citation-verification`, and `academic-paper-writer-pro`; no duplicate active orchestrator added. |
| Nature Skills | https://github.com/Yuan1z0825/nature-skills | public sparse clone checked at `1562ab71e5ae`; license file observed: `LICENSE` | partially-merged | Added single-paper deep reading card rules from `nature-paper-card` into `literature-review`; other Nature writing/figure/citation/PPT behavior remains covered by existing distilled skills. |
| Scientific Agent Skills | https://github.com/K-Dense-AI/scientific-agent-skills | full clone timed out; sparse tree checked at `e7ac42510774`; license file observed: `LICENSE.md` | reviewed-existing | Current collection already contains many same-name science, discovery, data-science, AI/ML, bioinformatics, medical-imaging, and writing skills; no bulk import. |
| Auto-Research-In-Sleep / ARIS | https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep | public clone checked at `53562a7c64cc`; license file observed: `LICENSE` | record-only | User explicitly asked not to keep local autopilot content. Repo is recorded here only. |
| AI Research Skills | https://github.com/Orchestra-Research/AI-Research-SKILLS | public clone checked at `773a52944ba4`; license file observed: `LICENSE` | record-only / deferred | Broad AI engineering catalog is deferred until a focused AI/ML engineering plugin/profile is approved. No autopilot import. |
| Research-Paper-Writing-Skills | https://github.com/Master-cai/Research-Paper-Writing-Skills | public clone checked at `77e7c2c1ba06`; license file observed: `LICENSE` | reviewed-existing | Already covered by `scientific-writing` and `paper-workflow-orchestrator` for paragraph flow, section structure, visual quality, claim-support alignment, and adversarial self-review. |
| PaperSpine | https://github.com/WUBING2023/PaperSpine | public clone checked at `d4529208cda7`; license file observed: `LICENSE` | reviewed-existing | Already merged historically into `paper-workflow-orchestrator`; current revision matches existing provenance. |
| Paper Craft Skills | https://github.com/zsyggq/paper-craft-skills | anonymous `git ls-remote` returned `Repository not found` | record-only / unresolved | Cannot clone or merge without a public/corrected URL. |

## Local Merge Posture

- Keep this as a webpage/source record only for ARIS/autopilot-related repos.
- Do not add `research-autopilot-loop` or any other autopilot-facing local skill from this intake.
- Avoid bulk-importing overlapping paper-writing orchestrators; prefer existing distilled research-writing plugin skills.
- Revisit `AI-Research-SKILLS` only as a separate AI/ML engineering plugin design, not as part of research-writing.

## Task-Based Runtime Integration

After review, overlapping writing repos that were not bulk-imported were
distilled into task-shaped runtime guidance instead of source-name triggers:

- End-to-end paper workflow sources map to a general manuscript production
  workbench: intake, argument spine, section contracts, draft sequencing,
  revision audit, and submission/rebuttal handoff.
- Single-paper reading sources map to evidence cards, method-map
  reconstruction, claim-evidence chains, limitations, and research ideas.
- Review-oriented sources map to evidence-grounded peer review, acceptance-risk
  diagnosis, reviewer concern ledgers, and rebuttal assessment.
- Style-oriented sources map to non-defensive scientific prose and
  source-faithful final artifact checks.

Source repository names remain in provenance only. Autopilot-style ARIS remains
record-only by user instruction.

## Runtime Routing Reinforcement - 2026-07-28

A second pass found that the eight source repos should not become source-name triggers. The useful content was re-routed into general capabilities: result-to-claim gates, claim-evidence matrices, section contracts, pre-submission reviewer checks, broad-journal figure/claim strategy, single-paper evidence cards, conditional paper-to-slide/figure routing, and final artifact fidelity checks. Autopilot loops remain excluded by user instruction. `zsyggq/paper-craft-skills` remains unresolved because the public repo URL could not be cloned.
