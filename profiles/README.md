# Profiles

Profiles are curated install sets. They are not domains.

- Profile: a hand-picked combination for a workflow, such as `codex-bayesian-jsdm`.
- Domain: a complete area, such as all active `bayesian` skills.
- Single skill: an exact selector, such as `domain/bayesian/pymc`.

Install a profile:

```bash
python3 scripts/skills.py install --target repo --profile codex-research-writing --mode symlink --write-agents-md
```

Install a complete domain:

```bash
python3 scripts/skills.py install --target repo --domain bayesian --mode symlink --write-agents-md
```

Install precise skills:

```bash
python3 scripts/skills.py install --target repo --skill domain/bayesian/pymc --mode symlink --write-agents-md
```

## Available Profiles

- `codex-core-global`: tiny user-level bootstrap profile.
- `codex-webdev`: React, Next.js, Tailwind, Figma handoff, browser testing, and visual QA.
- `codex-research-writing`: manuscripts, literature review, citations, PDFs, figures, slides, and peer review.
- `codex-writing-style`: source-faithful writing guardrail, English scientific prose, and Chinese final-pass editing.
- `codex-bayesian-jsdm`: Bayesian modeling, JSDM/HMSC, simulation, diagnostics, and manuscript support.
- `codex-cardiacnexus`: CardiacNexus, CMR, DICOM/NIfTI, MONAI, nnU-Net, UKB, and imaging pipelines.
- `codex-bioinformatics-light`: common bioinformatics workflows without every provider note.
- `codex-skill-maintenance`: maintain this skill repository, registry, docs, and installers.

Budget warnings from `audit` are guidance. They should prompt description compression or profile tuning, but they do not make domain installs invalid.
