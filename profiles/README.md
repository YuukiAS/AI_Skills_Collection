# Profiles

Profiles define small project-local skill sets. They replace broad bundles for
day-to-day work.

Install with:

```bash
python3 scripts/install_project_skills.py --project /path/to/project --profile auto --mode symlink --write-agents-md
```

## Available Profiles

- `codex-core-global`: tiny global bootstrap profile. Expected active skills:
  1-3. Use only for `project-skill-installer` and closely related management.
- `codex-webdev`: Next.js, React, Tailwind, Figma handoff, browser testing, and
  visual QA. Expected active skills: about 10-15.
- `codex-research-writing`: manuscripts, literature review, citations, PDFs,
  figures, slides, and peer review. Expected active skills: about 15-25.
- `codex-bayesian-jsdm`: TRACE/JSDM/HMSC, Bayesian modeling, Stan/PyMC, MCMC
  diagnostics, simulations, and theorem-heavy writing. Expected active skills:
  about 12-20.
- `codex-cardiacnexus`: CardiacNexus, CMR, DICOM/NIfTI, MONAI, nnU-Net, UKB,
  and medical imaging pipelines. Expected active skills: about 15-24.
- `codex-bioinformatics-light`: common bioinformatics workflows with one
  umbrella database retrieval skill instead of every provider. Expected active
  skills: about 12-18.
- `codex-skill-maintenance`: maintenance of this repository, skill metadata,
  registry, installers, and system skills. Expected active skills: about 10-18.

## Auto Detection

`--profile auto` scores both project files and optional natural-language intent.
It looks for signals such as `package.json`, `next.config.*`,
`tailwind.config.*`, CMR/DICOM terms, TRACE/JSDM/HMSC/Bayesian terms,
manuscript/LaTeX/bibliography structures, single-cell/RNA-seq/VCF/BAM/GTF paths,
or the `AI_Skills_Collection` repository itself. For new empty folders, use
`--intent "build a website"` or `--intent "write a paper"` so the user's stated
purpose participates directly in profile selection.

If two profiles score close together, the installer chooses one primary profile
and may add only a few secondary skills. It does not stack profiles without
limit.
