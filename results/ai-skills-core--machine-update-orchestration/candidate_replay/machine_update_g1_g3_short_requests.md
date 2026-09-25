# Candidate Replay Task: AI Skills Maintainer Short Machine Update Requests

Use AI Skills Maintainer.

This is a no-mutation dry run. Do not mutate files, Git refs, Marketplace state, Host state, Bridge runtime, Codex config, or project repositories.

Read the attached public-safe machine state note. For each normal user request below, return a concise route report:

1. `update AI Skills`
2. `sync this machine`
3. `update Bridge Kit`

For each request, identify:

- the Maintainer route that applies;
- the internal Maintainer owner skill responsible for the route;
- whether formal `release` and optional root `### Update impact` may expand scope;
- for `update Bridge Kit`, read the allowed Bridge source named in the public
  machine state note and dynamically discover:
  - Bridge `AGENTS.md` owner locator;
  - version sources;
  - current `release` ref;
  - newest formal release commit/version with sufficient closure evidence;
  - the release-state classification selected by the candidate from
    `ALIGNED`, `LAGGING`, `AHEAD/INCONSISTENT`, or
    `FORMAL_RELEASE_NOT_PROVABLE`;
- what must remain delegated to canonical Bridge / Codex / project-owner commands;
- the correct dry-run result state.

Do not ask the user for versions, commits, checkout paths, `CODEX_HOME`, repository inventories, adaptation templates, or dependency/component lists.
