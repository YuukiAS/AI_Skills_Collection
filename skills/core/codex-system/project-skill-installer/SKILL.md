---
name: project-skill-installer
description: Use when the user asks to install, update, or set up AI_Skills_Collection profiles for the current project. Handles project-local installation only; it does not provide domain knowledge.
status: active
provenance: local
trusted: true
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-05-14
profile_tags:
recommended_scope: global
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Project Skill Installer

Use this skill when the user says anything like:

- "为这个项目安装 skills"
- "给这个 repo 配 skills"
- "setup skills for this project"
- "install project skills"
- "update this project's skills"

This is an infrastructure skill. It installs profile selections and writes project routing docs; it does not replace frontend, presentation, bioinformatics, writing, or OpenAI system skills.

## Workflow

1. Identify the target project root.
   - Prefer a user-specified path.
   - Otherwise use the current working directory.
   - If the current directory is inside a repo, use the repo root when obvious.

2. Locate the central `AI_Skills_Collection` repository.
   - First check the current directory and parent directories.
   - Then check common locations such as `~/AI_Skills_Collection`,
     `~/AI_Skills/AI_Skills_Collection`, `/storage01/users/*/AI_Skills_Collection`,
     and `/project/*/*/AI_Skills_Collection`.
   - If it cannot be found, ask the user for the path.

3. Run the unified installer from the central repository:

```bash
ai-skills install --target repo --project /path/to/project --profile codex-skill-maintenance --mode symlink --write-agents-md
```

If the user stated a domain or exact skill, install that selector directly:

```bash
ai-skills install --target repo --project /path/to/project --domain bayesian --mode symlink --write-agents-md
ai-skills install --target repo --project /path/to/project --skill domain/bayesian/pymc --mode symlink --write-agents-md
```

Examples:

- Writing a paper, literature review, submission, slides, or citations should
  route to `codex-research-writing`.
- Building a website, frontend, dashboard, React/Next.js app, or Tailwind UI
  should route to `codex-webdev`.
- Bayesian, JSDM, HMSC, Stan, PyMC, MCMC, or simulation projects should route
  to `codex-bayesian-jsdm`.
- CMR, CardiacNexus, DICOM, NIfTI, MONAI, nnU-Net, or medical imaging projects
  should route to `codex-cardiacnexus`.
- Bioinformatics, single-cell, RNA-seq, VCF/BAM/GTF, scanpy, or scvi projects
  should route to `codex-bioinformatics-light`.

4. Read or re-read the generated project `AGENTS.md`.
   - The routing block lists the installed skills and their paths under
     `.agents/skills/`.
   - When a future task matches a listed trigger, read that skill's `SKILL.md`
     before acting.

## Important Boundaries

- Complete domain installs are allowed when requested; treat budget output as warnings.
- Do not install the whole central library into global `$HOME/.agents/skills` or explicit codex-home skills.
- Do not clean or rewrite global skills when switching projects.
- Project skills belong in `<project>/.agents/skills/`.
- Explicit codex-home installs use `${CODEX_HOME:-$HOME/.codex}/skills` only when the user asks for that advanced compatibility target.
