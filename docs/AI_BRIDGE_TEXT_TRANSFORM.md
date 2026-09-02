# AI Bridge Text Transform

Text Transform is a shared optional transport for private UTF-8 Markdown/plain
text generation. It is not a new project role and does not own product logic.
Consumer repositories provide public instruction files; this tool moves private
source text to an OpenAI Responses API call with `store=false` and returns only
encrypted output.

This repository's installed workflow is pinned to Bridge Kit commit
`27fff1659e3840438602c1b832d0e09a7b12ff91`.

The production path is:

```text
private local text
-> age public-key encryption
-> encrypted input + manifest + output public recipient committed to the task branch
-> GitHub Actions decrypts input in a temporary runner directory
-> OpenAI Responses API with store=false generates transformed plaintext
-> runner encrypts transformed plaintext to the output public recipient
-> results/<task_key>/text_transform/output.age + TEXT_TRANSFORM.json
```

Tracked files may include the public input recipient, encrypted input, transform
manifest, output public recipient, encrypted output, and `TEXT_TRANSFORM.json`.
Tracked files must never include source plaintext, transformed plaintext, age
private identities, or OpenAI API keys.

Install:

```bash
ai-bridge text-transform install --target /path/to/project
```

Create the local-only output receiver:

```bash
ai-bridge text-transform create-output-receiver \
  --target /path/to/project \
  --task-key 048_example
```

The private identity stays under `${AI_BRIDGE_STATE_HOME:-~/.ai-bridge}` unless
`--identity-output` is explicitly provided. Do not commit it.

Encrypt a private source artifact from the user machine:

```bash
ai-bridge text-transform encrypt \
  --target /path/to/project \
  --task-key 048_example \
  --input /private/path/source.md \
  --output results/048_example/text_transform/input.age \
  --manifest results/048_example/text_transform/text_transform_inputs.json \
  --output-recipient-file results/048_example/text_transform/output.age.pub \
  --instruction-file plugins/codex/plugins/writing-style/skills/scientific-rewrite/SKILL.md \
  --goal "Rewrite the complete source according to the bound public instructions." \
  --implementation-commit <commit> \
  --external-upload-authorization "User authorized this private text transform through OpenAI Responses API with store=false for this task."
```

After GitHub Actions writes back encrypted output, decrypt locally:

```bash
ai-bridge text-transform decrypt \
  --target /path/to/project \
  --result results/048_example/text_transform/TEXT_TRANSFORM.json \
  --identity-file ~/.ai-bridge/text-transform/<repo>/<task>/output_identity.txt \
  --output /private/path/rewritten_report.md
```

The result metadata records source SHA-256, instruction bundle identity, model,
`store=false`, output plaintext SHA-256, output ciphertext SHA-256, and Bridge
Kit commit. It does not contain the transformed plaintext.
