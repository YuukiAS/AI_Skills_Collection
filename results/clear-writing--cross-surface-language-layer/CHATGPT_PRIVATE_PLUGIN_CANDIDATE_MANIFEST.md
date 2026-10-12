# ChatGPT Private Clear Writing Candidate Manifest

This is a public-safe, same-source candidate manifest for a future private
ChatGPT Clear Writing plugin operation. It is not a personal account mutation,
not a Plugin Creator upload, and not proof that ChatGPT Web has installed or
selected the candidate.

## Candidate Identity

- Product display name: Clear Writing
- Central plugin slug: `writing-style`
- Central source version in this implementation candidate: `0.4`
- Intended future private wrapper: one skills-only Clear Writing package with no MCP server, no external model service, no account secret, and no background watcher.
- Source authority: this reviewed branch after the implementation commit, using the files listed below.

## Skill Source Files

```text
f012b730f95364d5093f16c8c433342121701c5cdcd8b5101a457c4a1e9160a4  skills/writing/core/writing-fidelity/SKILL.md
142b49b8b89f89701a10e55c36aafae8d010478ce7885774a7b6ff9efcac8f67  skills/writing/core/response-clarity/SKILL.md
2e5417d2ca461d15005de2c3e238820d6d05d58f834bab4b51fa78990f5dce04  skills/writing/core/scientific-prose/SKILL.md
ed8165a808854b919758e862231f637d7aded3b6fcf25895c5d1b166509b48c6  skills/writing/core/product-ui-copy/SKILL.md
5919ec2d11cb810415020151393aa2e70feafd8cc72d3580c9f3e4de7effb404  skills/writing/core/scientific-rewrite/SKILL.md
377c6d21bb023f1b52c35b7824f06b463ae113ff568008ce5c2f9cf58261beae  skills/writing/core/chinese-prose/SKILL.md
```

Required support file for the heavy Chinese rewrite route:

```text
76bce3dbac9e81822fa312ab3df8b8af4ea50d1216e3904247d892283efa0e0f  skills/writing/core/scientific-rewrite/scripts/rewrite_support.py
```

New `response-clarity` trigger examples:

```text
3b2399b4022f556d79957412678581229a4bfbea63fa670b4b2e7635ae195327  skills/writing/core/response-clarity/evals/trigger_queries.json
```

Generated Codex payload anchors:

```text
680595dcf2f96352ff72a38b97d2cb107e5ba33b9818b9f4cc3a07b379c7f2ce  .agents/plugins/marketplace.json
c4b05610287b7e091e4c7760bc3c87d4346f79b35bc28b3456d510bb5ebaaa68  plugins/codex/plugins/writing-style/.codex-plugin/plugin.json
08360405d156a9dd44f80aca5432b31ecafd3b24621ae139f37eb54f7f3e2f67  scripts/codex_marketplace_config.json
25863b13c787251a4df5ec400a5657aecb0b5565ddff2cdd6ed85da913577bed  profiles/codex-writing-style.json
```

## Rebuild Recipe For Authorized GPT/Plugin Creator Step

1. Fetch this reviewed branch at the implementation commit.
2. Read `scripts/codex_marketplace_config.json` and the six source skill directories under `skills/writing/core/`.
3. Construct a skills-only Clear Writing plugin wrapper from those same source files, preserving each `SKILL.md`, support files, and assets required by the skills.
4. Hash the wrapper contents before Plugin Creator upload and compare against this manifest.
5. Only after user/account authorization, create or update at most one private Clear Writing plugin identity.
6. Run G1 A/E, B/C, and D exactly as frozen in the v0.3 Gate Matrix. If the environment cannot establish legal matched comparisons, report `INCONCLUSIVE` rather than claiming plugin increment.

No personal plugin id, private URL, Project instruction, chat transcript, token, or account credential is stored in this repository artifact.
