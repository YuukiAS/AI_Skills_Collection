# Public-Safe Machine State Note

- Current installed production plugin observed before candidate replay: `ai-skills-core@yuukias-ai-skills` version `0.4`.
- Candidate commit under test: supplied by the replay command and recorded in `run.json`.
  Do not rely on this public note as the candidate identity authority.
- Requested target: `update Bridge Kit`.
- Bridge repository identity under test:
  `YuukiAS/GPT_Codex_AI_Bridge_Kit`.
- Allowed read-only Bridge source for this replay:
  `private/exports/ai-skills-core--machine-update-orchestration/bridge_git_snapshot`.
- Supplemental raw copied files from the same Bridge observation are available
  at:
  `private/exports/ai-skills-core--machine-update-orchestration/bridge_source_snapshot`.
- The allowed Bridge read scope contains raw source/ref/closure inputs only:
  `AGENTS.md`, `pyproject.toml`, `ai_bridge_kit/__init__.py`, `CHANGELOG.md`,
  `results/reviewed-handoff--first-bootstrap-normal-entry/EVIDENCE.md`, and
  raw Git refs.
- Do not use
  `results/ai-skills-core--machine-update-orchestration/BRIDGE_REVALIDATION_SNAPSHOT.md`
  as a classification answer key. It is Executor evidence only.
- The candidate must discover the Bridge owner locator, version sources,
  formal closure evidence, current release ref, latest provable formal release,
  and release/ref relation from the allowed Bridge source.
- This replay is a no-mutation dry run. It must not change Marketplace, Host, Bridge runtime, Git refs, or project repositories.
