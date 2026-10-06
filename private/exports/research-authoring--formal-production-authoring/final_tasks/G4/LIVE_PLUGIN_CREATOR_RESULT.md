# G4 Live Plugin Creator Result

Date: 2026-10-06
Task: `research-authoring--formal-production-authoring`

## Outcome

```text
LIVE_PLUGIN_MUTATION_PERFORMED=YES
PLUGIN_CREATE=PASS
PLUGIN_NAME=research-authoring
PLUGIN_VERSION=0.3.0
PLUGIN_SCOPE=USER
PLUGIN_DISCOVERABILITY=PRIVATE
PLUGIN_ID=plugins_6ac4471b735881918c17cd310f262429
RELEASE_ID=pluginrel_6ac4471c7b90819189bc23af890135f3
FINAL_CANDIDATE_COMMIT=1c37c0715aca0096606f24e56192b7857e72bbd6
```

Plugin URL:

`https://chatgpt.com/plugins/plugins_6ac4471b735881918c17cd310f262429`

## Packaging compatibility fix

The first live Plugin Creator call rejected the prepared wrapper because its plugin manifest used `version: 0.3`; Plugin Creator requires semantic versioning such as `0.3.0`.

The correction changed only the ChatGPT distribution wrapper manifest version:

```text
ChatGPT wrapper: 0.3 -> 0.3.0
Research Authoring payload: remains 0.3
Research Authoring final candidate commit: unchanged
G1/G2/G3 evidence: unchanged
```

No Research Authoring source, routing, profile, scientific content, Gate task, rubric, or final-candidate code was changed.

## Live release verification

Plugin Creator metadata was read back after creation and confirmed:

- name: `research-authoring`
- version: `0.3.0`
- scope: `USER`
- discoverability: `PRIVATE`
- current release: `pluginrel_6ac4471c7b90819189bc23af890135f3`

The live release file list was also read directly. It contains the expected skills-only payload:

- `report`
- `paper`
- `litcite`
- `writing-fidelity`
- `chinese-prose`
- `scientific-prose`

and no MCP or connector payload.

The live plugin manifest reports `capabilities = Skills`, `displayName = Research Authoring`, and `version = 0.3.0`.

## Archive identity

The original frozen archive was rejected before mutation because of the non-semver wrapper version.

The exact local archive successfully uploaded to Plugin Creator after the one-field wrapper correction had SHA-256:

`d2c0af3352e61007a981b9b7a8843cd3492fada6e2e28951cd5ab1972515a685`

The repository branch now regenerates a deterministic semver-compatible archive from the same wrapper file tree. Its canonical repository SHA-256 is recorded in `WRAPPER_MANIFEST.json`.

The gzip/tar byte stream is not required to match the successful local upload byte-for-byte; live Plugin Creator file inspection is the authoritative content-identity check.

## Remaining G4 work

This result closes only the live Plugin Creator creation step.

It does not by itself prove full G4 PASS. The remaining frozen G4 work is:

1. use the live private ChatGPT wrapper on the already-approved G2 semantic baseline;
2. preserve the frozen handoff fields and scientific semantics;
3. continue through exact-C Codex `research-main`;
4. produce the real PDF through the approved renderer route;
5. run renderer QA and final Research Authoring scientific QA;
6. submit complete G4 evidence to an independent Reviewer.

No main merge, formal release, paid API call, or other plugin mutation is authorized by this receipt.
