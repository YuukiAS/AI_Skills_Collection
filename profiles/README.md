# Profiles

Profiles are curated install sets. They are not domains.

- Profile: a hand-picked combination for a workflow, such as `codex-bayesian-jsdm`.
- Domain: a complete area, such as all active `bayesian` skills.
- Single skill: an exact selector, such as `domain/bayesian/pymc`.

Install a profile:

```bash
ai-skills install --target repo --profile codex-research-writing --mode symlink --write-agents-md
```

Install a complete domain:

```bash
ai-skills install --target repo --domain bayesian --mode symlink --write-agents-md
```

Install precise skills:

```bash
ai-skills install --target repo --skill domain/bayesian/pymc --mode symlink --write-agents-md
```

## Available Profiles

- `codex-core-global`: tiny user-level bootstrap profile.
- `codex-workflow-core`: global workflow protocol, source-of-truth discovery, gate-driven completion, verification, escalation, live-state supervision, and writing fidelity.
- `codex-webdev`: React, Next.js, Tailwind, Figma handoff, browser testing, and visual QA.
- `codex-research-writing`: manuscripts, literature review, citations, PDFs, figures, slides, and peer review.
- `codex-scientific-diagrams`: editable scientific method figures, D2, draw.io, PlantUML, Mermaid, Excalidraw, and publication figure planning.
- `codex-writing-style`: writing fidelity guardrail, English scientific prose, Chinese prose polishing, and CJK/math PDF rendering.
- `codex-bayesian-jsdm`: Bayesian modeling, JSDM/HMSC, simulation, diagnostics, and manuscript support.
- `codex-cardiacnexus`: CardiacNexus, CMR, DICOM/NIfTI, MONAI, nnU-Net, UKB, and imaging pipelines.
- `codex-bioinformatics-light`: common bioinformatics workflows without every provider note.
- `codex-skill-maintenance`: maintain this skill repository, registry, docs, and installers.

Budget warnings from `audit` are guidance. They should prompt description compression or profile tuning, but they do not make domain installs invalid.
