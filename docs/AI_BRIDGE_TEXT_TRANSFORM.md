# AI Bridge Text Transform

Text Transform is an optional private UTF-8 Markdown/plain text transport. It is
not a project role and does not own writing policy. Consumer repositories
provide public instruction files and any task-local driver; the transport keeps
private source text in encrypted input, decrypts only inside a temporary GitHub
Actions runner directory, calls OpenAI Responses with `store=false`, and writes
back encrypted output plus public metadata.

This repository's installed workflow is pinned to Bridge Kit commit
`65ea9c59afbe2db88bb5d60bf8752f82719f0087`.

For 049 private style smoke, the production path is:

```text
private local segment
-> age public-key encryption
-> encrypted input + manifest + output public recipient committed to the task branch
-> GitHub Actions decrypts input in a temporary runner directory
-> AI_Skills consumer driver invokes the generated scientific-rewrite multistage runtime
-> OpenAI Responses API with store=false performs the model stages
-> runner encrypts the final candidate to the output public recipient
-> results/<task_key>/private_style_smoke/<smoke_id>/output.age + TEXT_TRANSFORM.json + stage_receipt.json
```

Tracked files may include the public input recipient, encrypted input, transform
manifest, output public recipient, encrypted output, public stage receipt, and
`TEXT_TRANSFORM.json`. Tracked files must never include source plaintext,
transformed plaintext, age private identities, or OpenAI API keys.

The installed-entrypoint replay and private-artifact generation paths are
separate. Installed-entrypoint evidence validates plugin install, routing, and
runtime receipts in an isolated Codex home. Private style-smoke generation uses
the frozen secure transport and does not require mutating the user's live global
marketplace or copying Codex auth material.
