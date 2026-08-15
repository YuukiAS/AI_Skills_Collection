# Changelog

## Unreleased

- Added `ai-skills verify-server-installation` and `scripts/verify_server_installation.py` for server-local installation smoke checks without login, SSH, Codex App UI verification, or Slurm submission.
- The smoke check installs the selected profile/domain/skills into a temporary Codex home by default, validates installed `SKILL.md` frontmatter and icon references, validates the generated marketplace payload paths, and reports optional local tooling availability.
- Documented the server-local smoke gate in `README.md` and `docs/INSTALLATION.md`.
