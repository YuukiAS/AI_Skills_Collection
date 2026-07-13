# hpc

Active skills: 1

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain hpc --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill tool/hpc/slurm-workflows --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `slurm-workflows` (`skills/tools/hpc/slurm-workflows`): Plan, submit, monitor, diagnose, and safely iterate Slurm jobs with generic resource estimation, job arrays, log/scratch layout, queue inspection, failure classification, and optional race execution policy supplied by a site profile.

## Main References

- `skills\tools\hpc\slurm-workflows\references\site-profile-contract.md`
