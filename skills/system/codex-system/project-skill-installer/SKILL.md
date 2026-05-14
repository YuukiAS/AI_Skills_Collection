---
name: project-skill-installer
description: Use when the user asks to install, update, or set up skills for the current project. Finds AI_Skills_Collection, runs project-local installation, then reads AGENTS.md.
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
---
# Project Skill Installer

Use this skill when the user says anything like:

- "为这个项目安装 skills"
- "给这个 repo 配 skills"
- "setup skills for this project"
- "install project skills"
- "update this project's skills"

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

3. Run the project-local installer from the central repository:

```bash
python3 scripts/install_project_skills.py --project /path/to/project --profile auto --mode symlink --write-agents-md
```

If the user stated the project purpose in natural language, pass it through:

```bash
python3 scripts/install_project_skills.py --project /path/to/project --profile auto --intent "write a research paper" --mode symlink --write-agents-md
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
     `.codex/skills/`.
   - When a future task matches a listed trigger, read that skill's `SKILL.md`
     before acting.

## Important Boundaries

- Do not install the whole central library into global `~/.codex/skills`.
- Do not clean or rewrite global skills when switching projects.
- Project skills belong in `<project>/.codex/skills/`.
- The global directory should contain only a tiny core loader such as this skill.
