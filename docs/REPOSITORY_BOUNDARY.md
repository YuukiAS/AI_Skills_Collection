# Repository Boundary

`AI_Skills_Collection` is the publishing source for active Codex skills in this
workspace. Skills that appear in `registry.json`, profiles, CLI installs, or the
Codex App marketplace must live in this repository under `skills/`.

External software repositories, cloned upstream projects, and broad reference
materials belong in `AI_Research_Toolkit`. A repository containing `SKILL.md`,
prompts, agent configs, or skill-like content is still treated as source
material until a specific skill is reviewed and adapted here.

Before adapting external skill-like content into this repository:

- confirm license and provenance;
- record `source_repo_url`, `source_path`, `source_ref`,
  `source_imported_at`, `source_license`, and `source_note`;
- review quality, safety, dependencies, and trigger boundaries;
- adapt only the specific skill needed, not the whole upstream repository.

`.agents/plugins/marketplace.json` and `plugins/codex/plugins/` are generated
from `skills/` and `scripts/codex_marketplace_config.json`. Do not edit them as
source and do not use symlinks there; together they form the sparse-checkout
Codex App marketplace publication.

`bundles/` and explicit codex-home installs remain compatibility paths. They
are not the design target for new skill publication.
