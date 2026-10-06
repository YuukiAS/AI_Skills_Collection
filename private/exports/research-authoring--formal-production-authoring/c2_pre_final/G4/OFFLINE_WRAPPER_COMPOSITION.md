# C2 Offline Research Authoring Wrapper Composition

Status:

`OFFLINE_ONLY / NO_LIVE_MUTATION`

Canonical product commit:

`ac501d988f00cb6672fec105ae5fd51a0679cae0`

Wrapper identity for the next guarded live update:

```text
name=research-authoring
scope=USER
discoverability=PRIVATE
skills-only=YES
distribution_version_expected=0.3.1
```

The distribution version is an offline package identity only. The canonical Research Authoring plugin payload remains `research-writing 0.3 @ C2`.

## Required Research Authoring payload

Rebuild from exact C2:

`plugins/codex/plugins/research-writing/**`

Primary bound blobs:

- plugin manifest: `0f9bcaaf553894cd8b930a639515e077dd031e8f`;
- report aggregate: `9bd0808df090ad250fe922026755cb34c83a1343`;
- report core: `7a11ad99ffd929c851c420bb9bdc32fe55e9acdd`;
- report delegate: `2029a3dae1e222c77735475fba30448cad02beb3`;
- paper aggregate: `66ef4fb75cf468bc5373a10b7168021eab57a0eb`;
- lit/citation aggregate: `3137b3f05c5d6245edc506e7eec6a8ceef1af486`.

## Clear Writing support from the same C2 commit

- `writing-fidelity`: `6668e642da73253307c1a859a6f60ce39b2bbcb9`;
- `chinese-prose`: `1cdadeb56da1c23b7255bf582943880acd01b9bf`;
- `scientific-prose`: `09963c6a984722f1e5b37737025e43fa29b0c309`.

## Explicit exclusions

No:

- PDF renderer runtime;
- Pandoc/XeLaTeX runtime;
- MCP;
- connector;
- database;
- watcher/daemon/state;
- Plugin Creator mutation;
- live account mutation;
- private research data.

The offline package must be reproducibly rebuilt from these exact C2 roots before the future live Plugin update. Live update remains separately user-authorized.
