# CardiacNexus Repo-Local Skill Export

This is a short-lived migration package. Copy or merge this directory into the CardiacNexus repository, then maintain these skills only there:

```text
CardiacNexus/
  AGENTS.md
  .agents/
    skills/
      cardiacnexus-feature-contracts/
      cardiacnexus-pipeline-refactor/
      cardiacnexus-strain-registration/
      cardiacnexus-docs-markdoc/
```

After the CardiacNexus repository contains the canonical `.agents/skills/` copy, remove this export package from `AI_Skills_Collection`. The central marketplace must not publish a generic `cardiacnexus` plugin.

Suggested install/check flow after merging into CardiacNexus:

```bash
ai-skills install --target repo --profile codex-cardiacnexus --mode copy --write-agents-md
```

The command above installs only general supporting skills from this central repository. The four CardiacNexus-specific skills in this export should stay repo-local and version with CardiacNexus code, schemas, docs, and tests.
