# AI Bridge Text Transform

Text Transform is an optional private UTF-8 Markdown/plain text transport. It is
not a project role and does not own writing policy. Consumer repositories
provide public instruction files and any task-local driver; the transport keeps
private source text in encrypted input, decrypts only inside a temporary GitHub
Actions runner directory, calls OpenAI Responses with `store=false`, and writes
back encrypted output plus public metadata.

This is a 049-only historical transport. The GitHub Actions workflow that used
it has been retired from the 050 branch and must not be restored as a GitHub
Actions production path. Task 050 uses host Codex for generation and only allows
bounded candidate-only paid QA under the paid-review budget contract.

The retired 049 workflow was pinned to Bridge Kit commit
`65ea9c59afbe2db88bb5d60bf8752f82719f0087`.

For 049 private style smoke, the historical path was:

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

The installed-entrypoint replay and private-artifact generation paths were
separate in 049. For 050 and later production work, this document is historical
context only; ordinary push must not launch paid model transforms, and external
paid calls require frozen campaign budget context.
