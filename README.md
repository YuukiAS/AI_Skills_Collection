# AI Skills Collection

This repository is a central skill library plus project-local installer. It is
not meant to install every skill into global `~/.codex/skills`.

The new operating model is:

1. Keep the complete library in this repository.
2. Select a small profile for a specific project.
3. Install or link those skills into `<project>/.codex/skills/`.
4. Generate a short `<project>/AGENTS.md` routing block so Codex knows when to
   read each project-local skill.

This avoids warnings such as `Skill descriptions were shortened to fit the 2%
skills context budget` and avoids deleting/reinstalling global skills when
switching projects.

## Layout

- `skills/`: callable workflows. Each `SKILL.md` should be a clear executable
  workflow, not a general knowledge page.
- `shared/`: non-callable resources such as templates, provider notes, reference
  packs, schemas, prompt fragments, and AGENTS templates.
- `palette/`: shared color palette resources.
- `profiles/`: small project profiles that list which skills to install.
- `scripts/install_project_skills.py`: project-local installer.
- `scripts/audit_skill_budget.py`: budget and profile audit tool.
- `registry.json`: generated active skill registry with governance fields.
- `bundles/`: legacy deployment subsets kept for compatibility. Do not use them
  for daily project switching.

## Project-Local Install

```bash
python3 scripts/install_project_skills.py \
  --project /path/to/project \
  --profile auto \
  --mode symlink \
  --write-agents-md
```

`--profile auto` scores the project and chooses a profile such as
`codex-webdev`, `codex-research-writing`, `codex-bayesian-jsdm`,
`codex-cardiacnexus`, `codex-bioinformatics-light`, or
`codex-skill-maintenance`.

For a new or empty directory, pass the user's natural-language purpose as
`--intent` so auto detection can use semantic intent as well as files:

```bash
python3 scripts/install_project_skills.py \
  --project /path/to/project \
  --profile auto \
  --intent "write a research paper with citations and slides" \
  --mode symlink \
  --write-agents-md
```

`--mode symlink` links project skills back to this central repository. If
symlinks fail, the installer falls back to copy mode and reports that choice.
Use `--mode copy` explicitly for Windows filesystem locations where symlink
permissions are unreliable.

The installer writes:

- `<project>/.codex/skills/<skill-name>/`
- `<project>/.codex/skills/.ai-skills-collection-manifest.json`
- a managed block in `<project>/AGENTS.md` when `--write-agents-md` is set

The manifest records profile name, install time, central repo path and commit,
install mode, installed skills, AGENTS.md management status, and the last audit
summary. Sync only updates paths recorded in that project manifest.

## AGENTS.md Routing

`AGENTS.md` is intentionally short. It does not copy skill bodies. It says where
project skills live, lists the installed skill index, gives trigger summaries
and relative paths, records common build/test commands, and tells Codex to read
the relevant `SKILL.md` before acting.

Existing `AGENTS.md` content is preserved. The installer only updates:

```md
<!-- AI_SKILLS_COLLECTION_START -->
...
<!-- AI_SKILLS_COLLECTION_END -->
```

## Tiny Global Bootstrap

Global `~/.codex/skills` should contain only a tiny loader profile. Recommended
bootstrap:

```bash
python3 scripts/install_project_skills.py --global --profile codex-core-global --mode symlink
```

After that, normal usage is to enter a project and tell Codex: "为这个项目安装
skills" or "install project skills". The global `project-skill-installer` skill
will find this repository, run the project installer, and then read the
project's `AGENTS.md`.

Do not install the whole repository into global `~/.codex/skills`.

## Agent Operating Procedure

When an agent is running on a new server after this repository has been pulled,
bootstrap global skills once:

```bash
cd /path/to/AI_Skills_Collection
python3 scripts/install_project_skills.py --global --profile codex-core-global --mode symlink --prune-global
```

Use this only for the tiny global loader. It moves older broad global installs
to a timestamped backup instead of deleting them.

When the user asks to set up skills for a project, do not install a broad bundle
globally. Install project-local skills:

```bash
python3 /path/to/AI_Skills_Collection/scripts/install_project_skills.py \
  --project /path/to/project \
  --profile auto \
  --intent "user's natural-language project purpose" \
  --mode symlink \
  --write-agents-md
```

Examples of intent routing:

- "write a paper", "literature review", "citations", "slides" ->
  `codex-research-writing`
- "build a website", "React", "Next.js", "Tailwind", "dashboard" ->
  `codex-webdev`
- "Bayesian", "JSDM", "HMSC", "Stan", "PyMC", "MCMC" ->
  `codex-bayesian-jsdm`
- "CMR", "DICOM", "NIfTI", "MONAI", "nnU-Net", "CardiacNexus" ->
  `codex-cardiacnexus`
- "bioinformatics", "single-cell", "RNA-seq", "scanpy", "scvi", "VCF/BAM/GTF" ->
  `codex-bioinformatics-light`

If project installation fails because `<project>/.codex/skills` resolves to
global `~/.codex/skills`, repair the project-local directory explicitly:

```bash
python3 /path/to/AI_Skills_Collection/scripts/install_project_skills.py \
  --project /path/to/project \
  --profile auto \
  --intent "user's natural-language project purpose" \
  --mode symlink \
  --write-agents-md \
  --repair-project-codex-symlink
```

The repair mode backs up the project `.codex` symlink and creates a real local
`.codex/skills/`. It must not be used to clean or rewrite global skills.

## Validation And Audits

Run before committing:

```bash
python3 scripts/generate_registry.py
python3 scripts/validate_skills.py
python3 scripts/audit_skill_budget.py --all
```

Audit one profile:

```bash
python3 scripts/audit_skill_budget.py profiles/codex-webdev.json
```

Audit an installed project:

```bash
python3 scripts/audit_skill_budget.py --project /path/to/project
```

## Windows And WSL

The installer uses Python `pathlib` and recognizes common Windows drive paths
from WSL. Prefer keeping WSL projects on the Linux filesystem for reliable
symlinks. For projects on Windows-mounted drives, use `--mode copy` or allow the
installer to fall back to copy mode when symlink creation fails.
