# Validator V2 implementation handoff

The Validator V2 source and generated Presentations payload are ready for
integration from the current detached worktree. The worktree is based on
`5160f661a786cc5ec6977dc5b47995e51fb3587b`. The controller reserved publication
for itself, so this handoff has no candidate commit or remote candidate SHA.
The remote implementation ref was last read at the frozen baseline.

- Source: `skills/tools/documents-media/presentations/shared/validator_v2/`
- Generated package: `plugins/codex/plugins/presentations/shared/validator_v2/`
- Production Python code SHA-256:
  `fb79726cf8e3bd5e7c30d0f3556d62f4f04079305738e90f88eb1295e0594834`
- [Changed-file manifest](CHANGED_FILES.tsv)

The CLI accepts Git authority bundles, renders with semantic object maps, and
exact historical locator configurations. In combined mode it matches the PDF
digest to the independently resolved candidate artifact before applying layout
checks. Runtime findings preserve the distinction between failure, review and
missing evidence.

The implementation keeps the existing plugin entry points and release metadata
intact. This is a standalone candidate component. The generated payload was
produced from the source package by the existing Marketplace generator.
The frozen specifications and STAT5060 source and PDF were used as read-only
inputs.

## Evidence and remaining scope

The published test log records 33 passing tests, including 29 for V2 and four
adjacent checks from the existing Presentations suite. The suite used the
generated payload and includes two independent XeLaTeX fixture renders, a
deidentified V19 positive geometry slice and two exact archived V18 geometry
regressions. See the [public test report](PUBLIC_TESTS.md) and
[mutation report](MUTATIONS.md).

The V19 PDF bytes matched the frozen digest. The positive slice covers selected
body and navigation geometry from physical page 39. The V18 controls
independently catch body overflow beyond the rail and section label width
overflow on the archived render. The remaining historical layout classes use
synthetic controls where implemented. This evidence does not establish a
whole-deck V19 replay, the complete historical rejected-render corpus,
production standard/CUHK parity, or held-out acceptance.

The exact legacy V4 review locator is absent at evidence commit
`a255e716cf7a846208a62edc82132c3752a16417`. The
[read-only replay report](LEGACY_REPLAY.json) records `NOT_VERIFIED` for the
exact path. A Planner-approved exact locator would be needed to replay that
historical review as present.

The layout interface relies on an independently prepared map for role labels,
semantic spacing edges, column groups, footer bands and allowed masks.
The source scanner recognizes documented TeX patterns. It does not execute or
fully parse TeX macro expansion. Copy validation matches explicit Git blobs or
the text layer of a PDF under the declared ordered text contract. Typography,
layout geometry and review coverage checks do not authenticate reviewer
identity or establish pedagogical quality. Full production-map authoring and
fresh independent evaluation remain separate work.
