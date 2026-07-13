# Server ZIP Inventory

Inputs reviewed on 2026-07-13:

| File | SHA256 | Classification | v3.5 handling |
|---|---|---|---|
| `skills-CUHK.zip` | `95AC905AC8DABA9FC0FF401777F1197612635764C020F33FC80E813EEE186B3D` | local user-provided server skill bundle | Removed from tracked root after review; generic Slurm behavior merged into `skills/tools/hpc/slurm-workflows/`; public site constraints recorded in `site-profiles/cuhk-central-cluster.json`. |
| `skills-UNC.zip` | `0DA4862079F2F494132669682CAEC9450904EC72817FF6C156424A5B4C035A8C` | local user-provided server skill bundle | Removed from tracked root after review; generic Slurm behavior merged into `skills/tools/hpc/slurm-workflows/`; public site constraints recorded in `site-profiles/unc-longleaf.json`. |

Top-level contents:

| ZIP | Reviewed entries |
|---|---|
| `skills-CUHK.zip` | `writing-core-writing-fidelity/`, `writing-core-scientific-prose/`, `writing-core-chinese-prose/`, `slurm-partition-routing/`, `render-chinese-math-pdf/` |
| `skills-UNC.zip` | `tools-documents-media-render-chinese-math-pdf/`, `writing-core-chinese-prose/`, `writing-core-scientific-prose/`, `writing-core-writing-fidelity/`, `slurm-routing-partition/` |

Decision:

- Existing writing/render source skills remain canonical in `skills/`.
- Site-specific Slurm routing was not copied verbatim into a central active skill.
- Generic Slurm planning, monitoring, job-array, dependency, failure-triage, and safety rules live in `skills/tools/hpc/slurm-workflows/`.
- Public-safe site differences live in `site-profiles/`.
- Reviewed root ZIP inputs are no longer committed; keep future intake bundles in `.tmp/skill-intake/` until reviewed.
- Account names, hostnames, private paths, partitions, QOS values, tokens, and personal scratch paths must be supplied through `~/.config/ai-skills/local-overrides.toml` and are not committed.
